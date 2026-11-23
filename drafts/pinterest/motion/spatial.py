# 3D "spatial scene" from one photo (Megan Nov 23: "Like a 3D spatial scene for a picture").
# Free: Depth Anything V2 Small (ONNX, onnx-community on Hugging Face) estimates depth, then each frame shifts
# near pixels more than far ones along a slow looping camera path. 6s seamless loop, 1000x1500 (2:3), 30fps.
# Usage: python3 spatial.py <photo> <depth.onnx> <out.mp4> [strength_px]
import sys, cv2, numpy as np, onnxruntime as ort, subprocess, os, tempfile
src, model, out = sys.argv[1:4]; A = float(sys.argv[4]) if len(sys.argv) > 4 else 28
W, H, N = 1000, 1500, 180
img = cv2.imread(src); h, w = img.shape[:2]
if w / h > W / H: nw = int(h * W / H); img = img[:, (w - nw) // 2:(w - nw) // 2 + nw]
else: nh = int(w * H / W); img = img[(h - nh) // 2:(h - nh) // 2 + nh]
img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
x = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (518, 518)).astype(np.float32) / 255
x = ((x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]).astype(np.float32).transpose(2, 0, 1)[None]
s = ort.InferenceSession(model, providers=['CPUExecutionProvider'])
d = s.run(None, {s.get_inputs()[0].name: x})[0].squeeze()
d = cv2.resize(d, (W, H)); d = (d - d.min()) / (d.max() - d.min() + 1e-6)          # 1 = near, 0 = far
d = cv2.dilate(d, np.ones((9, 9), np.uint8)); d = cv2.GaussianBlur(d, (0, 0), 6)     # keep subject edges whole
cv2.imwrite(out.replace('.mp4', '-depth.png'), (d * 255).astype(np.uint8))
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); cx, cy = W / 2, H / 2
Z = 1.10                                                                             # zoom in so edges never show
tmp = tempfile.mkdtemp()
for i in range(N):
    t = 2 * np.pi * i / N
    dx, dy, push = A * np.sin(t), A * 0.45 * np.cos(t), 0.035 * (0.5 - 0.5 * np.cos(t))
    sc = Z + push * d                                                                # near things grow a bit more
    mx = cx + (xx - cx) / sc - (d - 0.5) * dx
    my = cy + (yy - cy) / sc - (d - 0.5) * dy
    cv2.imwrite(f'{tmp}/{i:04d}.png', cv2.remap(img, mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{tmp}/%04d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-movflags', '+faststart', out], check=True)
for f in os.listdir(tmp): os.remove(f'{tmp}/{f}')
print('ok', out)
