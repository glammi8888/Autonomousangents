# Round 10 (CT98–CT109), Nov 16: pins in Megan's inspiration formats + lines (drafts/pinterest/inspo-megan/). "now give me a few more pins and then we can switch styles"
import gen9, gen8
from gen4 import B
from gen import doc, LOGO
A='alt="Editorial photo (AI-generated)"'
def s(k): return f'/_blob/{B[k]}'
S="""img.f{position:absolute;object-fit:cover;display:block}
.full{inset:0;width:100%;height:100%}
.tl{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%);z-index:5}
.url{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:700;font-size:28px;z-index:5}
.c{position:absolute;left:60px;right:60px;text-align:center}
"""
T=lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
U=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
P={}
P['CT98']=doc('Color test 98 · soft lowercase on photo · richer and prettier',S+"""
.pin{background:#E9C2D1}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(90,20,50,.45) 100%)}
.c{top:1080px;color:#fff;font-weight:500;font-size:82px;line-height:1.05;letter-spacing:-.04em;text-shadow:0 2px 20px rgba(0,0,0,.35)}
""",f"""<img class="f full" src="{s('pinkmoney')}" style="object-position:55% 20%" {A}><div class="sh"></div>{T('w')}<div class="c">i only get<br>richer and prettier</div>{U('#fff')}""")
bub=''.join(f'<div class="b">{x}</div>' for x in ['U SO TEAAAA','BODY TEA','FACE TEA','HAIR TEA'])
P['CT99']=doc('Color test 99 · message bubbles · tea',S+"""
.pin{background:#000}
.bs{position:absolute;left:70px;top:330px;display:flex;flex-direction:column;gap:22px;align-items:flex-start}
.b{background:#2B2B2D;color:#fff;font-weight:500;font-size:84px;letter-spacing:-.01em;padding:30px 56px;border-radius:90px}
.b:last-child{border-bottom-left-radius:16px}
""",f"""{T('w')}<div class="bs">{bub}</div>{U('#fff')}""")
P['CT100']=doc('Color test 100 · loop with arrows · im sexy',S+"""
.pin{background:#F8DCEB}
.wd{position:absolute;font-weight:800;font-size:74px;letter-spacing:-.03em;color:#111}
svg{position:absolute;inset:0}
.sp{position:absolute;color:#E8A9D4;font-size:120px}
""",f"""{T()}<svg viewBox="0 0 1000 1500"><g fill="none" stroke="#111" stroke-width="14" stroke-linecap="round"><path d="M190 600 C150 460 220 380 330 360"/><path d="M300 330 l40 30 -40 35"/><path d="M700 380 C860 400 900 520 860 640"/><path d="M820 610 l40 40 45 -45"/><path d="M860 960 C860 1080 780 1150 680 1170"/><path d="M710 1130 l-40 40 45 35"/><path d="M260 1110 C160 1040 140 920 180 830"/><path d="M150 870 l30 -45 40 40"/></g></svg>
<div class="wd" style="left:360px;top:300px">i'm sexy</div><div class="wd" style="left:580px;top:720px">i'm funny</div><div class="wd" style="left:320px;top:1150px">i'm pretty</div><div class="wd" style="left:60px;top:720px">i'm smart</div>
<div class="sp" style="left:440px;top:540px">✦</div><div class="sp" style="left:420px;top:830px;font-size:80px">✦</div>{U('#111')}""")
P['CT101']=doc('Color test 101 · loud poster type · prettier and hotter',S+"""
.pin{background:#fff;color:#0D0D0D}
.p{position:absolute;left:44px;right:44px;top:200px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
.p .a{font-weight:800;font-size:150px;transform:scaleX(.72);transform-origin:left;display:inline-block;white-space:nowrap}
.p .b{font-weight:900;font-size:168px}
.p .e{font-weight:900;font-size:220px;text-transform:none;letter-spacing:-.07em;display:block;margin-top:10px}
.sub{position:absolute;left:52px;right:52px;top:1030px;font-weight:900;font-size:64px;line-height:1;text-transform:uppercase;letter-spacing:-.02em}
img.f{left:620px;top:1040px;width:330px;height:330px}
""",f"""{T()}<div class="p"><span class="a">I get</span> <span class="b">prettier</span><br><span class="a">and</span> <span class="b">hotter</span><span class="e">everyday!</span></div>
<div class="sub" style="width:520px">I can't wait for tomorrow</div><img class="f" src="{s('pinkgloss')}" style="object-position:50% 35%" {A}>{U('#0D0D0D')}""")
P['CT102']=doc('Color test 102 · subtitle line on photo · iconic',S+"""
.pin{background:#222}
.c{top:1180px;color:#fff;font-style:italic;font-weight:400;font-size:96px;letter-spacing:-.02em;text-shadow:0 2px 14px rgba(0,0,0,.6)}
""",f"""<img class="f full" src="{s('bighair')}" style="object-position:50% 25%;filter:saturate(.75) contrast(1.05)" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 62%,rgba(0,0,0,.6) 85%)"></div>{T('w')}<div class="c">I am iconic</div>{U('#fff')}""")
P['CT103']=doc('Color test 103 · plain lowercase card · lucky girl syndrome',S+"""
.pin{background:#fff}
.c{top:560px;color:#111;font-weight:400;font-size:150px;line-height:1;letter-spacing:-.04em}
""",f"""{T()}<div class="c">lucky girl<br>syndrome</div>{U('#111')}""")
P['CT104']=doc('Color test 104 · dictionary card · muse',S+"""
.pin{background:#FBF8F3;color:#111}
.wd{position:absolute;left:80px;top:300px;font-weight:900;font-size:170px;letter-spacing:-.05em}
.w span{font-weight:400;font-size:70px;letter-spacing:0}
.d{position:absolute;left:80px;right:80px;top:540px;font-weight:400;font-size:62px;line-height:1.18;letter-spacing:-.02em}
img.f{left:80px;top:1010px;width:300px;height:360px}
.cap{position:absolute;left:410px;top:1300px;font-size:22px;font-weight:600;letter-spacing:.2em;text-transform:uppercase}
""",f"""{T()}<div class="wd">muse <span>n.</span></div><div class="d">A woman, or a force personified as a woman, who is the source of inspiration for a creative artist.</div>
<img class="f" src="{s('curls')}" style="object-position:55% 25%" {A}><div class="cap">see also: you</div>{U('#111')}""")
P['CT105']=doc('Color test 105 · huge lowercase white on black · big deal',S+"""
.pin{background:#0D0D0D}
.c{left:70px;right:40px;top:330px;text-align:left;color:#fff;font-weight:800;font-size:178px;line-height:.9;letter-spacing:-.06em}
""",f"""{T('w')}<div class="c">babe,<br>you're a<br>big deal.<br>act like it.</div>{U('#fff')}""")
P['CT106']=doc('Color test 106 · pink card + emoji · spoiled',S+"""
.pin{background:#F8DCE8}
.c{top:420px;color:#111;font-weight:400;font-size:176px;line-height:1.05;letter-spacing:-.03em}
""",f"""{T()}<div class="c">Spoiled<br>by the<br>Universe ⭐</div>{U('#111')}""")
P['CT107']=doc('Color test 107 · pink text over photo · loser',S+"""
.pin{background:#111}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(20,5,15,.85) 80%)}
.c{top:1060px;color:#FFB8D9;font-weight:700;font-size:80px;line-height:1;letter-spacing:-.04em}
""",f"""<img class="f full" src="{s('wethair')}" style="object-position:50% 15%" {A}><div class="sh"></div>{T()}<div class="c">Never let a loser make you question your worth</div>{U('#FFA6CF')}""")
P['CT108']=doc('Color test 108 · cosy after photo · it all worked out',S+"""
.pin{background:#1A1610}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 60%,rgba(0,0,0,.5) 100%)}
.c{top:1150px;color:#fff;font-weight:400;font-size:96px;letter-spacing:-.04em;text-shadow:0 2px 16px rgba(0,0,0,.5)}
""",f"""<img class="f full" src="{s('sleepcash')}" style="object-position:40% 30%" {A}><div class="sh"></div>{T('w')}<div class="c">it all worked out</div>{U('#fff')}""")
P['CT109']=doc('Color test 109 · big caps three beats · brains beauty booty',S+"""
.pin{background:#fff}
.c{top:420px;color:#0D0D0D;font-weight:500;font-size:150px;line-height:.98;letter-spacing:-.05em;text-transform:uppercase}
""",f"""{T()}<div class="c">Brains,<br>beauty &amp;<br>booty.</div>{U('#0D0D0D')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
