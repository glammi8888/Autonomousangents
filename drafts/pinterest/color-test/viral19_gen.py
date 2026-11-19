# Viral aesthetics replicated (VR01–VR10), Nov 19. Megan: "I think we need to replicate viral pins" + "aesthetically".
# Source: the 16 most-reacted image pins today for manifestation aesthetic / vision board 2027 / affirmations aesthetic / money affirmations / self love quotes aesthetic / glow up aesthetic
# (Apify, ../viral/2026-11-19-viral-aesthetic.json). We copy the LOOK only (layout, type, palette); words = BANK.md lines word for word; photos = our own library.
import gen9, gen8, gen13, gen19
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
B.update({'s3':'cb42026166e754aa61015533d682c479'})
A='alt="Editorial photo (AI-generated)"'
FONTS='family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&amp;family=Oswald:wght@400;500;600&amp;family=Inter+Tight'
SER="font-family:'Cormorant Garamond',serif"; CON="font-family:'Oswald',sans-serif"
P={}
def pin(k,title,css,body):
    h=doc(f'Viral look {k[2:]} · {title}',S+css,body).replace('family=Inter+Tight',FONTS,1); P[k]=h
SH='text-shadow:0 2px 12px rgba(0,0,0,.55)'
# VR01 · moody photo + big white condensed line (viral #0, 2,881 reactions)
pin('VR01','moody photo + condensed line',f""".q{{position:absolute;left:80px;right:80px;top:1130px;text-align:center;color:#fff;{CON};font-weight:400;font-size:96px;line-height:1.08;letter-spacing:-.01em;{SH}}}""",
 f"""<img class="f full" src="{s('red')}" style="object-position:50% 20%" {A}>{T('w')}<div class="q">My dream life wants me</div>{U('#fff')}""")
# VR02 · rainbow aura glow + condensed white (viral #1, 2,184)
pin('VR02','aura glow',f""".pin{{background:radial-gradient(ellipse at 50% 55%,#fff 0%,#fff6f2 10%,#ffd9ec 22%,#e6d4ff 34%,#cfe9ff 44%,#d8ffe9 54%,#fff1c9 64%,#f3c6e6 76%,#c9b3d9 100%)}}
.q{{position:absolute;left:90px;right:90px;top:620px;text-align:center;color:#fff;{CON};font-weight:500;font-size:110px;line-height:1.05;{SH}}}""",
 f"""{T()}<div class="q">I have big plans.</div>{U('#5b4a63')}""")
# VR03 · charcoal + moon + sparkles + thin serif (viral #3, 1,407 range)
stars=''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;color:#cdbf9f;font-size:{f}px">✦</div>' for x,y,f in [(120,330,44),(820,300,34),(160,1180,30),(840,1120,46),(700,420,22),(250,560,20),(760,1300,24)])
pin('VR03','moon + serif',f""".pin{{background:#2b2a28}}
.q{{position:absolute;left:110px;right:110px;top:640px;text-align:center;color:#d8ccb2;{SER};font-weight:400;font-size:82px;line-height:1.15}}
.m{{position:absolute;left:0;right:0;top:330px;text-align:center;color:#d8ccb2;font-size:170px}}""",
 f"""{T('w')}{stars}<div class="m">☾</div><div class="q">I only attract the best of the best</div>{U('#d8ccb2')}""")
# VR04 · 6-photo grid with serif labels (viral #4, 1,929)
cells=[('cashpile','money','50% 50%'),('room','home','50% 50%'),('pinkgloss','glow','50% 30%'),('closet','style','50% 40%'),('wethair','self care','50% 30%'),('bedcash','soft life','50% 40%')]
g=''.join(f'<div class="c" style="left:{(i%2)*500}px;top:{170+(i//2)*443}px"><img src="{s(k)}" style="object-position:{p}" {A}><span>{l}</span></div>' for i,(k,l,p) in enumerate(cells))
pin('VR04','6-photo grid',f""".pin{{background:#f6f1e9}} .c{{position:absolute;width:500px;height:443px;overflow:hidden}} .c img{{width:100%;height:100%;object-fit:cover;display:block}}
.c span{{position:absolute;left:0;right:0;top:180px;text-align:center;color:#fff;{SER};font-weight:600;font-size:66px;{SH}}}""",
 f"""{g}{T()}{U('#fff')}""")
# VR05 · tweet card on pink (viral #6) — our own handle, no celebrity
pin('VR05','tweet card',f""".pin{{background:#F7C6D9}}
.av{{position:absolute;left:90px;top:330px;width:96px;height:96px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}} .av img{{height:46px}}
.nm{{position:absolute;left:210px;top:332px;font-weight:700;font-size:40px;color:#111}} .hd{{position:absolute;left:210px;top:384px;font-size:30px;color:#555}}
.q{{position:absolute;left:90px;right:90px;top:520px;{CON};font-weight:500;font-size:112px;line-height:1.08;color:#111}}""",
 f"""<div class="av"><img src="{LOGO}" alt="ISSUE11"></div><div class="nm">ISSUE11</div><div class="hd">@issue11.app</div><div class="q">I wake up to money</div>{U('#111')}""")
# VR06 · burgundy, 2027 top-left, serif line bottom-right (viral #7)
pin('VR06','burgundy 2027',f""".pin{{background:#4a1417}}
.y{{position:absolute;left:80px;top:220px;color:#f3e6dc;{SER};font-size:120px;font-weight:500}}
.q{{position:absolute;right:80px;left:160px;top:1000px;text-align:right;color:#f3e6dc;{SER};font-size:80px;line-height:1.12}}""",
 f"""{T('w')}<div class="y">2027</div><div class="q">Dream life is on its way</div>{U('#f3e6dc')}""")
# VR07 · cream + small centred serif (viral #9)
pin('VR07','cream serif',f""".pin{{background:#f6f1e9}}
.q{{position:absolute;left:110px;right:110px;top:600px;text-align:center;color:#2b2622;{SER};font-weight:600;font-size:64px;line-height:1.25}}""",
 f"""{T()}<div class="q">I am worthy of love, respect, and everything I desire</div>{U('#2b2622')}""")
# VR08 · pink radial + huge serif 2027 + small caps (viral #11)
pin('VR08','pink 2027',f""".pin{{background:radial-gradient(circle at 50% 50%,#fbe3ea 0%,#f6c8d6 55%,#eeb2c6 100%)}}
.y{{position:absolute;left:0;right:0;top:520px;text-align:center;color:#8e1f3f;{SER};font-weight:600;font-size:300px;line-height:1}}
.s{{position:absolute;left:0;right:0;top:860px;text-align:center;color:#8e1f3f;font-weight:600;font-size:34px;letter-spacing:.22em;text-transform:uppercase}}""",
 f"""{T()}<div class="y">2027</div><div class="s">is the year I lifemaxx</div>{U('#8e1f3f')}""")
# VR09 · linen + bold condensed navy caps (viral #12)
pin('VR09','linen caps',f""".pin{{background:repeating-linear-gradient(0deg,rgba(0,0,0,.03) 0 2px,transparent 2px 5px),repeating-linear-gradient(90deg,rgba(0,0,0,.025) 0 2px,transparent 2px 6px),#e9e1d3}}
.q{{position:absolute;left:130px;right:130px;top:560px;text-align:center;color:#1f3b63;{CON};font-weight:600;font-size:112px;line-height:1.0;text-transform:uppercase}}""",
 f"""{T()}<div class="q">My nervous system is calm</div>{U('#1f3b63')}""")
# VR10 · photo + stacked affirmation list (viral #13)
pin('VR10','stacked list on photo',f""".q{{position:absolute;left:520px;right:60px;top:430px;color:#fff;{CON};font-weight:400;font-size:62px;line-height:1.25;{SH}}}""",
 f"""<img class="f full" src="{s('s3')}" style="object-position:30% 30%" {A}>{T('w')}<div class="q">I am healthy<br>I am wealthy<br>I am rich<br>I am that bitch</div>{U('#fff')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
