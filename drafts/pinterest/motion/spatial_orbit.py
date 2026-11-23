# Orbit version (Megan Nov 23: "make it seem like the background is moving left and right ... a wow effect"):
# the person is cut out as her own layer and stays almost still, the text swings a little, the background swings most,
# like the camera circling her. The background behind her is filled in (inpaint) so nothing smears.
# Editorial spatial pin (Megan Nov 23: "text behind the subject", "more editorial", "or edgy",
# "think dazed & confused", "2000's experimental"). The genre, not anyone's logo or layout.
# Back layer (behind the person): one huge condensed word stretched to the full width, set so the head overlaps its
# lower part. Front layer: italic serif word, tiny letter-spaced mono captions, issue11.app bottom-left (logo rule).
# Plus a slight colour split on the big word and film grain. Depth Anything V2 Small + MODNet (both free, ONNX).
# Usage: python3 spatial_orbit.py <photo> <depth.onnx> <modnet.onnx> <out.mp4> <big> <italic> <capTopRight> <capBottomRight> [strength]
import sys, os, cv2, numpy as np, onnxruntime as ort, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
src, dmodel, mmodel, out, BIG, ITA, CAPL, CAPR = sys.argv[1:9]; A = float(sys.argv[9]) if len(sys.argv) > 9 else 70
HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.join(HERE, '../../issue11-gift/rebrand-kit')
F_BIG, F_ITA, F_MONO, F_SANS = f'{HERE}/fonts/Anton-Regular.ttf', f'{HERE}/fonts/InstrumentSerif-Italic.ttf', f'{KIT}/IBMPlexMono-Regular.ttf', f'{KIT}/InterTight.ttf'
W, H, N = 1000, 1500, 180; CYC = int(os.environ.get("CYCLES", "2")); TXT = float(os.environ.get("TEXT_SWING", ".45"))
img = cv2.imread(src); h, w = img.shape[:2]
if w / h > W / H: nw = int(h * W / H); img = img[:, (w - nw) // 2:(w - nw) // 2 + nw]
else: img = img[:int(w * H / W)]
img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
x = ((cv2.resize(rgb, (518, 518)) - [.485, .456, .406]) / [.229, .224, .225]).astype(np.float32).transpose(2, 0, 1)[None]
s = ort.InferenceSession(dmodel, providers=['CPUExecutionProvider'])
raw = cv2.resize(s.run(None, {s.get_inputs()[0].name: x})[0].squeeze(), (W, H), interpolation=cv2.INTER_CUBIC)
raw = ((raw - raw.min()) / (raw.max() - raw.min() + 1e-6)).astype(np.float32)
ms = ort.InferenceSession(mmodel, providers=['CPUExecutionProvider'])
mi = ((cv2.resize(rgb, (512, 768)) - .5) / .5).transpose(2, 0, 1)[None].astype(np.float32)
matte = np.clip(cv2.resize(ms.run(None, {ms.get_inputs()[0].name: mi})[0].squeeze(), (W, H), interpolation=cv2.INTER_CUBIC), 0, 1).astype(np.float32)
thr = cv2.threshold((raw * 255).astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[0] / 255
if (matte > .5).any(): raw = np.maximum(raw, matte * max(thr + .1, float(np.percentile(raw[matte > .5], 50)))).astype(np.float32)
d = cv2.GaussianBlur(cv2.dilate(raw, np.ones((9, 9), np.uint8)), (0, 0), 6)
rows = np.where((matte > .5).sum(1) > 8)[0]; head = int(rows[0]) if len(rows) else int(H * .3)
# back layer: the big word, stretched to the full width; the head covers ~30% of its height
def word_mask(text, font_path, size):
    f = ImageFont.truetype(font_path, size); bb = f.getbbox(text); im = Image.new('L', (bb[2] - bb[0] + 4, bb[3] - bb[1] + 4), 0)
    ImageDraw.Draw(im).text((2 - bb[0], 2 - bb[1]), text, font=f, fill=255); return im
M = 34; bw = W - 2 * M
bh = int(np.clip((head - 150) / .7, 300, 560)); by = max(150, head - int(bh * .7))
big = np.asarray(word_mask(BIG, F_BIG, 400).resize((bw, bh), Image.LANCZOS)).astype(np.float32) / 255
back = np.zeros((H, W), np.float32); back[by:by + bh, M:M + bw] = big
# front layer: italic word overlapping the big word's lower-left, captions, url
front = Image.new('L', (W, H), 0); fd = ImageDraw.Draw(front)
fi = ImageFont.truetype(F_ITA, 150); itl = Image.new('L', (W, H), 0)
ImageDraw.Draw(itl).text((M + 6, by - 118), ITA, font=fi, fill=255)        # reads: personal / rebrand
itl = np.asarray(itl).astype(np.float32)[..., None] / 255; PINK = np.array([.97, .62, .80], np.float32)   # brand pastel pink
fm = ImageFont.truetype(F_MONO, 24)
def spaced(xy, text, font, right=False):
    cw = [fd.textlength(c, font=font) + 4 for c in text]; x0 = xy[0] - sum(cw) if right else xy[0]
    for c, wch in zip(text, cw): fd.text((x0, xy[1]), c, font=font, fill=255); x0 += wch
spaced((W - M - 4, 34), CAPL.lower(), fm, right=True); spaced((W - M - 4, H - 84), CAPR.lower(), fm, right=True)  # Megan: no capital letters
fs = ImageFont.truetype(F_SANS, 40)
try: fs.set_variation_by_axes([600])
except Exception: pass
fd.text((M + 4, H - 96), 'issue11.app', font=fs, fill=255)
front = np.asarray(front).astype(np.float32)[..., None] / 255
shadow = np.clip(cv2.GaussianBlur(np.maximum(front, itl)[..., 0], (0, 0), 4) * .55, 0, .55)[..., None]  # soft shadow under all front type
def ink(region):                                   # white type on dark ground, near-black on light ground
    return np.array([1, 1, 1], np.float32) if region.mean() < .6 else np.array([.07, .07, .07], np.float32)
c_back = ink(rgb[by:by + bh][(matte[by:by + bh] < .5)]) if (matte[by:by + bh] < .5).any() else np.ones(3, np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); cx, cy = W / 2, H * .35; Z = 1.16
hole = cv2.dilate((matte > .25).astype(np.uint8), np.ones((31, 31), np.uint8))
sm = cv2.resize((rgb * 255).astype(np.uint8), (W // 2, H // 2)); hm = cv2.resize(hole, (W // 2, H // 2), interpolation=cv2.INTER_NEAREST)
bgc = cv2.resize(cv2.inpaint(sm, hm, 9, cv2.INPAINT_TELEA), (W, H)).astype(np.float32) / 255
bgc = np.where(hole[..., None] > 0, bgc, rgb)                                           # clean plate: background without her
dbg = np.where(hole > 0, 0, raw); dbg = cv2.GaussianBlur(dbg, (0, 0), 25); dbg = dbg / (dbg.max() + 1e-6)
far = (1 - .6 * dbg).astype(np.float32)                                                # far things swing more
rng = np.random.default_rng(7); tmp = tempfile.mkdtemp()
def warp(im, sx, sc, border=cv2.BORDER_REFLECT):
    mx = (cx + (xx - cx) / sc - sx).astype(np.float32); my = (cy + (yy - cy) / sc).astype(np.float32)
    return cv2.remap(im, mx, my, cv2.INTER_LINEAR, borderMode=border)
for i in range(N):
    t = 2 * np.pi * CYC * i / N; s = np.sin(t); dx = A * s                                # CYC swings per 6s loop (Megan: "a bit more rapid")
    fr = warp(bgc, dx * far, Z + .02 * (1 - np.cos(t)) / 2)                             # background: big swing, slight push
    bk = warp(back, dx * TXT, Z, cv2.BORDER_CONSTANT)                                      # text swing: TXT (0 = locked in place)
    split = 3 + 2 * np.sin(t * 2)
    for ch, sx in ((0, split), (2, -split)):
        g = cv2.warpAffine(bk, np.float32([[1, 0, sx], [0, 1, 0]]), (W, H)) * .55
        fr[..., ch] = fr[..., ch] * (1 - g) + g
    fr = fr * (1 - bk[..., None]) + c_back * bk[..., None]
    sub = warp(rgb, dx * .06, Z); m = np.clip(warp(matte, dx * .06, Z, cv2.BORDER_CONSTANT), 0, 1)[..., None]
    fr = fr * (1 - m) + sub * m                                                            # her, nearly still, on top
    fr = fr * (1 - shadow); fr = fr * (1 - itl) + PINK * itl; fr = fr * (1 - front) + np.ones(3, np.float32) * front
    fr = fr + rng.normal(0, .035, (H, W, 1)).astype(np.float32)
    cv2.imwrite(f'{tmp}/{i:04d}.png', (np.clip(fr, 0, 1) * 255).astype(np.uint8)[..., ::-1])
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{tmp}/%04d.png', '-c:v', 'libx264', '-profile:v', 'main', '-pix_fmt', 'yuv420p', '-crf', '20', '-movflags', '+faststart', out], check=True)
for k in (0, 45, 135): subprocess.run(['cp', f'{tmp}/{k:04d}.png', out.replace('.mp4', f'-f{k}.png')])
for f in os.listdir(tmp): os.remove(f'{tmp}/{f}')
print('ok', out)
