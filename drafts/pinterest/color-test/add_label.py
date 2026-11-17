# Megan, Nov 17 ("I hope people understand it is the meaning of manifestation lol" → "yes let's do that"): small "manifestation tip" label under the logo on the Later = Never pins (CT216–CT225). Idempotent; run after gen24.py/gen25.py.
import re
for n in range(216,226):
    f=f'CT{n}.dc.html'; h=open(f).read()
    if 'class="mtip"' in h: continue
    col=re.search(r'<div class="url" style="color:([^"]+)"',h).group(1)
    lab=f'<div class="mtip" style="position:absolute;left:0;right:0;top:150px;text-align:center;color:{col};font-weight:700;font-size:22px;letter-spacing:.32em;text-transform:uppercase;z-index:5;{'text-shadow:0 1px 8px rgba(0,0,0,.6);' if n==216 else ''}">manifestation tip</div>'
    h=h.replace('<div class="url"',lab+'<div class="url"',1)
    open(f,'w').write(h)
print('ok')
