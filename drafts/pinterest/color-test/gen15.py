# Angel number format test (CT143–CT146), Nov 16. Megan: "I think we should do them all but we need to decide on the pin aesthetic format". Same number (888) in 4 formats; lines from ../affirmations/ANGEL-NUMBERS.md (approved).
import gen9, gen8, gen13
from gen import doc
from gen13 import S, T, U, A, s
N,K,L='888','PROSPERITY',"everything you put in motion is coming back to you. money is coming"
P={}
# A · aura gradient (most-saved angel format: 222 alignment 3,379 · 111 1,522 · 777 luck 473)
P['CT143']=doc('Color test 143 · angel format A · aura gradient',S+"""
.pin{background:radial-gradient(circle at 50% 46%,#FFF3B0 0%,#FFD36B 16%,#F7B7C8 38%,#F4E6EE 62%,#FBF6F2 100%);color:#3A2A10}
.n{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:300;font-size:250px;letter-spacing:-.02em;line-height:1}
.k{position:absolute;left:0;right:0;top:780px;text-align:center;font-weight:700;font-size:30px;letter-spacing:.32em}
.l{position:absolute;left:170px;right:170px;top:850px;text-align:center;font-weight:400;font-size:40px;line-height:1.3;text-wrap:balance}
""",f"""{T()}<div class="n">{N}</div><div class="k">{K}</div><div class="l">{L}</div>{U('#3A2A10')}""")
# B · full-bleed photo, big number (CT133 style)
P['CT144']=doc('Color test 144 · angel format B · full-bleed photo',S+"""
.pin{background:#222}
.n{position:absolute;left:0;right:0;top:930px;text-align:center;color:#fff;font-weight:800;font-size:250px;letter-spacing:-.06em;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.35)}
.k{position:absolute;left:0;right:0;top:1195px;text-align:center;color:#fff;font-weight:700;font-size:28px;letter-spacing:.3em}
.l{position:absolute;left:100px;right:100px;top:1245px;text-align:center;color:#fff;font-style:italic;font-weight:400;font-size:42px;line-height:1.25;text-wrap:balance}
""",f"""<img class="f full" src="{s('cashface')}" style="object-position:50% 30%" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.7) 85%)"></div>{T('w')}<div class="n">{N}</div><div class="k">{K}</div><div class="l">{L}</div>{U('#fff')}""")
# C · photo + colour band (CT134 style)
P['CT145']=doc('Color test 145 · angel format C · photo + colour band',S+"""
.pin{background:#1F6B4A}
.n{position:absolute;left:0;right:0;top:960px;text-align:center;color:#F4E9C8;font-weight:800;font-size:250px;letter-spacing:-.06em;line-height:1}
.k{position:absolute;left:0;right:0;top:1205px;text-align:center;color:#F4E9C8;font-weight:700;font-size:28px;letter-spacing:.3em}
.l{position:absolute;left:90px;right:90px;top:1250px;text-align:center;color:#fff;font-weight:600;font-size:40px;line-height:1.2;text-wrap:balance}
""",f"""<img class="f" src="{s('cashface')}" style="left:0;top:0;width:100%;height:930px;object-position:50% 25%" {A}>{T('w')}<div class="n">{N}</div><div class="k">{K}</div><div class="l">{L}</div>{U('#fff')}""")
# D · minimal cream card (ANGEL NUMBER 888 / 999 cards, 856–1,078)
P['CT146']=doc('Color test 146 · angel format D · minimal cream card',S+"""
.pin{background:#F7F2EA;color:#1A1A1A}
.t{position:absolute;left:0;right:0;top:330px;text-align:center;font-weight:500;font-size:28px;letter-spacing:.32em}
.n{position:absolute;left:0;right:0;top:400px;text-align:center;font-weight:800;font-size:240px;letter-spacing:-.03em;line-height:1}
.k{position:absolute;left:0;right:0;top:700px;text-align:center;font-style:italic;font-weight:400;font-size:40px}
.hr{position:absolute;left:440px;right:440px;top:790px;border-top:2px solid #1A1A1A}
.l{position:absolute;left:170px;right:170px;top:850px;text-align:center;font-weight:400;font-size:42px;line-height:1.35;text-wrap:balance}
""",f"""{T()}<div class="t">ANGEL NUMBER</div><div class="n">{N}</div><div class="k">{K.lower()}</div><div class="hr"></div><div class="l">{L}</div>{U('#1A1A1A')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
