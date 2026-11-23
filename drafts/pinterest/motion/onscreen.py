# Put a phone-screen render onto the black phone screen in a photo (Megan Nov 23, her own hand-and-phone photo).
# Megan: "Make the writing seem like it's part of the screen. Right now it looks overlapped."
# So: the screen render fills the whole glass (made by screen_render.js at the screen's shape), and it is matched
# to the photo: same softness, warm tint, lifted blacks, slight glow, the photo's own grain, and the original glass
# reflections laid back on top. Only paints where the screen shows, so nails and the clear case stay in front.
# Usage: python3 onscreen.py <photo> <screen.png> <out.png>
import sys, cv2, numpy as np
ph, scr_p, out = sys.argv[1:4]
im = cv2.imread(ph); f = im.astype(np.float32)
g = cv2.GaussianBlur(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), (0, 0), 6)
n, lab, st, _ = cv2.connectedComponentsWithStats((g < 32).astype(np.uint8)); i = 1 + np.argmax(st[1:, 4])
mask = (lab == i).astype(np.uint8)
cnt, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
box = cv2.boxPoints(cv2.minAreaRect(cv2.convexHull(cnt[0])))
e = [(box[k], box[(k + 1) % 4]) for k in range(4)]
short = sorted(e, key=lambda p: np.linalg.norm(p[0] - p[1]))[:2]
top = min(short, key=lambda p: p[0][1] + p[1][1]); bot = [p for p in short if p is not top][0]
tl, tr = sorted(top, key=lambda p: p[0]); bl, br = sorted(bot, key=lambda p: p[0])
scr = cv2.imread(scr_p); h, w = scr.shape[:2]
M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), np.float32([tl, tr, br, bl]))
warp = cv2.warpPerspective(scr, M, (im.shape[1], im.shape[0]), flags=cv2.INTER_AREA).astype(np.float32) / 255
# match the photo: soft focus, warm whites a bit under full brightness, slight bloom
warp = cv2.GaussianBlur(warp, (0, 0), 0.8)
warp = warp * np.array([0.80, 0.86, 0.93], np.float32)                     # BGR: warm, dimmer than pure white
warp = warp + 0.35 * cv2.GaussianBlur(warp, (0, 0), 5)                     # glow around the letters
quad = np.zeros(mask.shape, np.uint8); cv2.fillConvexPoly(quad, np.int32([tl, tr, br, bl]), 1)
a = cv2.GaussianBlur((mask & quad).astype(np.float32), (0, 0), 1.2)[..., None]
glass = f / 255                                                               # the real screen: black level + reflections
lit = 1 - (1 - np.clip(warp, 0, 1)) * (1 - glass)                             # screen blend keeps every reflection
rng = np.random.default_rng(11); hp = f - cv2.GaussianBlur(f, (0, 0), 2)     # the photo's grain
sd = hp[(mask & quad) > 0].std(); grain = rng.normal(0, sd, im.shape[:2])[..., None].astype(np.float32)
res = (lit * 255 + grain * (warp.mean(2, keepdims=True) > .15)) * a + f * (1 - a)
cv2.imwrite(out, np.clip(res, 0, 255).astype(np.uint8)); print('ok', out, round(float(sd), 2))
