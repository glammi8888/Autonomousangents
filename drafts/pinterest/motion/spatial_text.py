# Spatial scene + big text BEHIND the subject (Megan Nov 23: "You could put text behind the subject too").
# Depth Anything V2 Small (free, ONNX) gives depth; the text sits at a depth between subject and background, so the
# subject covers the letters and, in the loop, the text moves less than the subject and more than the background.
# issue11.app sits in front, bottom-left (logo rule: always visible, never bottom-right). 6s loop, 1000x1500, 30fps.
# Usage: python3 spatial_text.py <photo> <depth.onnx> <out.mp4> "<line1|line2>" [text_y 0-1] [strength_px] [color auto|#hex] [modnet.onnx]
import sys, cv2, numpy as np, onnxruntime as ort, subprocess, os, tempfile
from PIL import Image, ImageDraw, ImageFont
src, model, out, text = sys.argv[1:5]; TY = float(sys.argv[5]) if len(sys.argv) > 5 else .2
A = float(sys.argv[6]) if len(sys.argv) > 6 else 24; COL = sys.argv[7] if len(sys.argv) > 7 else 'auto'
MATTE = sys.argv[8] if len(sys.argv) > 8 else ''   # optional MODNet person cut-out (Apache-2.0, Xenova/modnet ONNX)
W, H, N = 1000, 1500, 180; FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../issue11-gift/rebrand-kit/InterTight.ttf')
img = cv2.imread(src); h, w = img.shape[:2]
if w / h > W / H: nw = int(h * W / H); img = img[:, (w - nw) // 2:(w - nw) // 2 + nw]
else: nh = int(w * H / W); img = img[:nh]                                           # keep the top: never cut heads
img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
x = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (518, 518)).astype(np.float32) / 255
x = ((x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]).astype(np.float32).transpose(2, 0, 1)[None]
s = ort.InferenceSession(model, providers=['CPUExecutionProvider'])
raw = cv2.resize(s.run(None, {s.get_inputs()[0].name: x})[0].squeeze(), (W, H), interpolation=cv2.INTER_CUBIC)
raw = ((raw - raw.min()) / (raw.max() - raw.min() + 1e-6)).astype(np.float32)                            # 1 = near
thr = cv2.threshold((raw * 255).astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[0] / 255
matte = None
if MATTE:                                                                            # people stay in front, clean hair edges
    mi = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (512, 768)).astype(np.float32) / 255
    mi = ((mi - .5) / .5).transpose(2, 0, 1)[None].astype(np.float32); ms = ort.InferenceSession(MATTE, providers=['CPUExecutionProvider'])
    matte = cv2.resize(ms.run(None, {ms.get_inputs()[0].name: mi})[0].squeeze(), (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
    raw = np.maximum(raw, matte * max(thr + .1, float(np.percentile(raw[matte > .5], 50)) if (matte > .5).any() else 1)).astype(np.float32)
d = cv2.GaussianBlur(cv2.dilate(raw, np.ones((9, 9), np.uint8)), (0, 0), 6)        # smooth depth for the motion
# text layer
font = ImageFont.truetype(FONT, 200)
try: font.set_variation_by_axes([800])
except Exception: pass
lines = text.split('|'); L = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(L)
size = min(int(200 * W * .9 / max(dr.textlength(t, font=font) for t in lines)), 330); font = ImageFont.truetype(FONT, size)
try: font.set_variation_by_axes([800])
except Exception: pass
lh = int(size * .9); y = int(H * TY)
for t in lines:
    tw = dr.textlength(t, font=font); dr.text(((W - tw) / 2, y), t, font=font, fill=255); y += lh
ta = np.asarray(L).astype(np.float32) / 255
if COL == 'auto':
    bg = img[(ta > .5) & (raw < thr)]; col = (20, 20, 20) if bg.size and bg.mean() > 140 else (255, 255, 255)
else: c = COL.lstrip('#'); col = (int(c[4:6], 16), int(c[2:4], 16), int(c[0:2], 16))
col = np.array(col, np.float32)
foot = Image.new('L', (W, H), 0); fd = ImageDraw.Draw(foot); ff = ImageFont.truetype(FONT, 40)
try: ff.set_variation_by_axes([600])
except Exception: pass
fd.text((56, H - 100), 'issue11.app', font=ff, fill=255); fa = np.asarray(foot).astype(np.float32)[..., None] / 255
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); cx, cy = W / 2, H * .35; Z = 1.07
dt = thr * .85                                                                       # text depth: just behind the subject
tmp = tempfile.mkdtemp()
for i in range(N):
    t = 2 * np.pi * i / N
    dx, dy, push = A * np.sin(t), A * .45 * np.cos(t), .03 * (.5 - .5 * np.cos(t))
    sc = Z + push * d; mx = (cx + (xx - cx) / sc - (d - .5) * dx).astype(np.float32); my = (cy + (yy - cy) / sc - (d - .5) * dy).astype(np.float32)
    fr = cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT).astype(np.float32)
    dw = cv2.remap(raw, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    occ = np.clip((dw - thr) / .04 + .5, 0, 1)                                       # 1 where the subject is in front
    if matte is not None: occ = np.clip(cv2.remap(matte, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT), 0, 1)
    sct = Z + push * dt; tx = (cx + (xx - cx) / sct - (dt - .5) * dx).astype(np.float32); ty = (cy + (yy - cy) / sct - (dt - .5) * dy).astype(np.float32)
    a = (cv2.remap(ta, tx, ty, cv2.INTER_LINEAR) * (1 - occ))[..., None]
    fr = fr * (1 - a) + col * a
    fc = np.array((255, 255, 255) if fr[-140:-60, 40:330].mean() < 140 else (20, 20, 20), np.float32)
    fr = fr * (1 - fa) + fc * fa
    cv2.imwrite(f'{tmp}/{i:04d}.png', np.clip(fr, 0, 255).astype(np.uint8))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{tmp}/%04d.png', '-c:v', 'libx264', '-profile:v', 'main', '-pix_fmt', 'yuv420p', '-crf', '20', '-movflags', '+faststart', out], check=True)
subprocess.run(['cp', f'{tmp}/0000.png', out.replace('.mp4', '-still.png')])
for f in os.listdir(tmp): os.remove(f'{tmp}/{f}')
print('ok', out, 'thr', round(float(thr), 2), 'size', size)
