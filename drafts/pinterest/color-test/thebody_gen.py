# "The Body" (Netflix, Nov 2026) trend pins, Nov 20 (TB01–TB04). Megan: "the show "The body" on netflix is trending so that could be a theme" + "my audience is gen z AND millenials both".
# The show's Pinterest aesthetic (../viral/2026-11-20-the-body-pins.json): dark academia, warm dark film grade, grain, orange film date stamp, pink blackletter type, ♱.
# Rights: NO show stills, names, characters or logo. Our own library photos, BANK lines word for word (body theme).
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
FONTS='family=UnifrakturMaguntia&amp;family=Inter+Tight'
BL="font-family:'UnifrakturMaguntia',serif"
GRADE='filter:sepia(.45) saturate(1.2) contrast(1.18) brightness(.58)'
GRAIN='<svg style="position:absolute;inset:0;width:100%;height:100%;opacity:.22;mix-blend-mode:overlay"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'
STAMP='<div style="position:absolute;right:70px;bottom:150px;color:#ff8a2a;font-family:monospace;font-size:34px;letter-spacing:.08em;text-shadow:0 0 8px rgba(255,120,30,.7)">11 20 \'26</div>'
P={}
def pin(k,photo,pos,line,fs,top):
    P[k]=doc(f'The Body trend {k[2:]}',S+f""".pin{{background:#1a0f0c}}
.q{{position:absolute;left:60px;right:60px;top:{top}px;text-align:center;color:#ff9ccf;{BL};font-size:{fs}px;line-height:1.02;text-shadow:0 3px 18px rgba(0,0,0,.6)}}
.x{{position:absolute;left:0;right:0;top:{top-90}px;text-align:center;color:#ff9ccf;font-size:56px}}""",
      f"""<img class="f full" src="{s(photo)}" style="object-position:{pos};{GRADE}" {A}>{GRAIN}{T('w')}<div class="x">♱</div><div class="q">{line}</div>{STAMP}{U('#f3e6dc')}""").replace('family=Inter+Tight',FONTS,1)
pin('TB01','curls','50% 30%','I love my hot bod',130,1000)
pin('TB02','wethair','50% 30%','My face card is absolutely lethal',104,980)
pin('TB03','earring','50% 30%','I am iconic',150,1020)
pin('TB04','shoulder','50% 30%','I am so fit and healthy and I am proud to say that I love my own body',74,960)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
