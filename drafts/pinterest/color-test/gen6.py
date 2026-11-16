# Round 6 (CT54–CT63), Nov 16: new styles around Megan's favourites (CT42 lavender + inset photo + italic, CT45 full-bleed + huge type).
import gen
from gen import doc, LOGO
from gen4 import B
def src(k): return f'/_blob/{B[k]}'
A='alt="Editorial photo (AI-generated)"'
S="""
.tl{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%);z-index:5}
.url{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:700;font-size:28px;z-index:5}
.it{position:absolute;left:0;right:0;text-align:center;font-style:italic;font-weight:400;letter-spacing:-.03em}
img.f{position:absolute;object-fit:cover;display:block}
"""
TOP=lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
URL=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
P={}
# 54 split screen
P['CT54']=doc('Color test 54 · split screen · periwinkle',S+"""
.pin{background:#8FA8E8}
img.f{left:0;top:0;width:560px;height:1500px}
.v{position:absolute;right:30px;top:150px;height:1200px;writing-mode:vertical-rl;color:#fff;font-weight:900;font-size:150px;line-height:.9;letter-spacing:-.05em}
.v i{font-weight:300}
.tl{left:780px}
.url{left:560px}
""",f"""<img class="f" src="{src('blue')}" style="object-position:50% 30%" {A}>{TOP()}<div class="v">My nervous system is <i>calm</i></div>{URL('#fff')}""")
# 55 triptych
crops=['30% 30%','55% 45%','50% 80%']
tri=''.join(f'<img class="f" src="{src("pink")}" style="left:{90+i*282}px;top:200px;width:256px;height:760px;object-position:{c}" {A}>' for i,c in enumerate(crops))
P['CT55']=doc('Color test 55 · triptych · blush',S+"""
.pin{background:#FBE7EC}
.it{top:1030px;font-size:66px;color:#7A0F3A}
""",f"""{TOP()}{tri}<div class="it">My face card is absolutely lethal</div>{URL('#7A0F3A')}""")
# 56 circular text around a round photo
P['CT56']=doc('Color test 56 · circle text · cream + red',S+"""
.pin{background:#F6EEE3}
.circ{position:absolute;left:150px;top:300px;width:700px;height:700px;border-radius:50%;overflow:hidden}
.circ img{width:100%;height:100%;object-fit:cover;object-position:50% 28%}
svg{position:absolute;left:60px;top:210px;width:880px;height:880px}
text{font-family:'Inter Tight',sans-serif;font-weight:900;font-size:58px;letter-spacing:6px;fill:#C8322B;text-transform:uppercase}
.big{position:absolute;left:0;right:0;top:1130px;text-align:center;color:#C8322B;font-weight:900;font-size:96px;letter-spacing:-.05em;line-height:.9}
.big i{font-weight:300}
""",f"""{TOP()}<div class="circ"><img src="{src('red')}" {A}></div>
<svg viewBox="0 0 880 880"><defs><path id="c" d="M440,440 m-405,0 a405,405 0 1,1 810,0 a405,405 0 1,1 -810,0"/></defs><text><textPath href="#c" textLength="2530" lengthAdjust="spacing">I AM THE PRIZE, ALWAYS · I AM THE PRIZE, ALWAYS ·</textPath></text></svg>
<div class="big">The prize, <i>always</i></div>{URL('#C8322B')}""")
# 57 knockout type filled with photo
P['CT57']=doc('Color test 57 · photo knockout type · lavender',S+"""
.pin{background:#F1EBFF}
.ko{position:absolute;left:30px;right:30px;top:280px;font-weight:900;font-size:250px;line-height:.8;letter-spacing:-.07em;text-transform:uppercase;text-align:center;background:url('KO1') 50% 25%/cover;-webkit-background-clip:text;background-clip:text;color:transparent}
.it{top:1040px;font-size:64px;color:#111}
""".replace('KO1',src('curls')),f"""{TOP()}<div class="ko">Dream girl</div><div class="it">I am my own dream girl</div>{URL('#111')}""")
# 58 four-photo grid
g=''.join(f'<img class="f" src="{src(k)}" style="left:{90+(i%2)*420}px;top:{190+(i//2)*420}px;width:400px;height:400px;object-position:50% 35%" {A}>' for i,k in enumerate(['pink','blue','red','orange']))
P['CT58']=doc('Color test 58 · four-photo grid · white',S+"""
.pin{background:#fff}
.big{position:absolute;left:60px;right:60px;top:1050px;text-align:center;color:#111;font-weight:900;font-size:76px;line-height:.92;letter-spacing:-.045em}
.big i{font-weight:300}
""",f"""{TOP()}{g}<div class="big">I glowed up so hard <i>now my enemies are crying</i></div>{URL('#111')}""")
# 59 full-bleed + price-tag sticker
P['CT59']=doc('Color test 59 · full-bleed + tag sticker',S+"""
.pin{background:#1A140C}
img.f{inset:0;width:100%;height:100%}
.tag{position:absolute;left:120px;top:1120px;background:#F3D9A4;color:#3A2A0C;font-weight:900;font-size:78px;letter-spacing:-.04em;padding:26px 40px 26px 70px;border-radius:14px;transform:rotate(-4deg);box-shadow:0 16px 40px rgba(0,0,0,.4)}
.tag::before{content:'';position:absolute;left:24px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;background:#1A140C}
""",f"""<img class="f" src="{src('cashface')}" style="object-position:50% 30%" {A}>{TOP('w')}<div class="tag">I wake up to money</div>{URL('#F3D9A4')}""")
# 60 blurred backdrop + polaroid
P['CT60']=doc('Color test 60 · blur backdrop + polaroid',S+"""
.pin{background:#2A2622;overflow:hidden}
.blur{position:absolute;inset:-60px;width:calc(100% + 120px);height:calc(100% + 120px);object-fit:cover;filter:blur(36px) saturate(1.2) brightness(.8)}
.po{position:absolute;left:170px;top:200px;width:660px;background:#fff;padding:24px 24px 120px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.45)}
.po img{display:block;width:100%;height:760px;object-fit:cover;object-position:50% 20%}
.po span{position:absolute;left:0;right:0;bottom:30px;text-align:center;font-style:italic;font-weight:500;font-size:46px;color:#2A2622;letter-spacing:-.03em}
""",f"""<img class="blur" src="{src('hair')}" {A}>{TOP('w')}<div class="po"><img src="{src('hair')}" {A}><span>I'm the luckiest girl on the planet</span></div>{URL('#fff')}""")
# 61 quiet full-bleed, small corner caption
P['CT61']=doc('Color test 61 · quiet full-bleed · corner caption',S+"""
.pin{background:#111}
img.f{inset:0;width:100%;height:100%}
.cap{position:absolute;left:60px;bottom:140px;color:#fff;font-style:italic;font-weight:400;font-size:52px;letter-spacing:-.03em;max-width:600px;line-height:1.05;text-shadow:0 2px 20px rgba(0,0,0,.5)}
.url{text-align:left;left:60px}
""",f"""<img class="f" src="{src('bobcash')}" style="object-position:45% 25%" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 62%,rgba(0,0,0,.75) 90%)"></div>{TOP('w')}<div class="cap">I'm making money in my sleep</div>{URL('#fff')}""")
# 62 knockout number filled with cash photo
P['CT62']=doc('Color test 62 · cash knockout number',S+"""
.pin{background:#0E0E0E}
.ko{position:absolute;left:0;right:0;top:400px;font-weight:900;font-size:236px;line-height:.85;letter-spacing:-.07em;text-align:center;background:url('KO2') 50% 50%/cover;-webkit-background-clip:text;background-clip:text;color:transparent}
.big{position:absolute;left:60px;right:60px;top:760px;text-align:center;color:#D9B3FF;font-weight:900;font-size:100px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase}
.big i{font-weight:300}
""".replace('KO2',src('cashpile')),f"""{TOP('w')}<div class="ko">$10,000</div><div class="big">a month <i>with ease</i></div>{URL('#D9B3FF')}""")
# 63 arch window on peach (CT42 cousin)
P['CT63']=doc('Color test 63 · arch window · peach italic',S+"""
.pin{background:#FCE4D6}
img.f{left:240px;top:190px;width:520px;height:780px;border-radius:260px 260px 0 0}
.it{top:1030px;font-size:60px;color:#8A3415;line-height:1.1}
""",f"""{TOP()}<img class="f" src="{src('orange')}" style="object-position:55% 30%" {A}><div class="it">Get up girl,<br>you got people to prove wrong</div>{URL('#8A3415')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
