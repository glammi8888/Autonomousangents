# Carousel 5 (CAR5-1..5), Nov 17. Megan: "I think the carousels can have the style of 100, 101 95 42 103". Manifestation 101 content, one loved style per slide:
# 1 cover = 101 loud poster · 2 desire = 103 plain lowercase card · 3 imagine = 42 pastel + framed photo + italic · 4 act = 95 giant word + specimen photos · 5 evolve = 100 arrow loop. No pitch.
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
LOOP=open('/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/loop.svg').read().strip()
N=lambda i,c='#111': f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:{c}">{i} / 5</div>'
SM=""".sm{position:absolute;left:90px;right:90px;text-align:center;font-weight:500;font-size:36px;line-height:1.3;letter-spacing:-.015em}
.sm b{font-weight:800}"""
P={}
P['CAR5-1']=doc('Carousel 5 · slide 1 · loud poster cover',S+""".pin{background:#fff;color:#0D0D0D}
.p{position:absolute;left:44px;right:44px;top:200px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
.p .a{font-weight:800;font-size:150px;transform:scaleX(.72);transform-origin:left;display:inline-block;white-space:nowrap}
.p .b{font-weight:900;font-size:168px}
.p .e{font-weight:900;font-size:300px;text-transform:none;letter-spacing:-.07em;display:block;margin-top:10px}
.sub{position:absolute;left:52px;top:1080px;width:520px;font-weight:900;font-size:52px;line-height:1.05;text-transform:uppercase;letter-spacing:-.02em}
img.f{left:620px;top:1060px;width:330px;height:330px}""",
f"""{T()}{N(1)}<div class="p"><span class="a">How to</span> <span class="b">manifest</span><br><span class="a">your</span> <span class="b">dream life</span><span class="e">101</span></div>
<img class="f" src="{s('closet')}" style="object-position:50% 40%" {A}>{U('#0D0D0D')}""")
P['CAR5-2']=doc('Carousel 5 · slide 2 · desire (plain card)',S+SM+""".pin{background:#fff}
.c{top:420px;color:#111;font-weight:400;font-size:170px;line-height:1;letter-spacing:-.05em}
.k{position:absolute;left:0;right:0;top:340px;text-align:center;font-weight:700;font-size:24px;letter-spacing:.2em;color:#C2207E}""",
f"""{T()}{N(2)}<div class="k">LESSON 01</div><div class="c">desire</div><div class="sm" style="top:700px">get specific. "i want to be rich" is a mood.<br>"i want $5k saved by june" is a desire.</div>
<div class="sm" style="top:1000px"><b>mistake:</b> wanting everything at once<br><b>do this:</b> pick one thing for this season</div>{U('#111')}""")
P['CAR5-3']=doc('Carousel 5 · slide 3 · imagine (pastel + framed photo)',S+SM+""".pin{background:#F1EBFF}
.it{position:absolute;left:60px;right:60px;top:1000px;text-align:center;font-style:italic;font-weight:400;font-size:62px;letter-spacing:-.03em;color:#111;line-height:1.1}""",
f"""{T()}{N(3)}<img class="f" src="{s('sky')}" style="left:270px;top:180px;width:460px;height:700px;object-position:50% 25%" {A}>
<div class="it">imagine: see it.<br>then see what's in the way.</div><div class="sm" style="top:1190px"><b>do this:</b> write the one thing most likely to stop you</div>{U('#111')}""")
spec=[('cashpile','move $50 to savings','left:90px;top:200px'),('suit','send the email','right:90px;top:170px'),('hair','book the appointment','left:110px;top:1040px'),('flying','walk 20 min','right:110px;top:1060px')]
sp=''.join(f'<div class="sp" style="{p}"><img src="{s(k)}" {A}><span>{c}</span></div>' for k,c,p in spec)
P['CAR5-4']=doc('Carousel 5 · slide 4 · act (giant word + specimens)',S+""".pin{background:#fff;color:#0D0D0D}
.gw{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:600;font-size:330px;letter-spacing:-.07em;line-height:1}
.sp{position:absolute;width:210px}
.sp img{display:block;width:210px;height:260px;object-fit:cover;object-position:50% 30%}
.sp span{display:block;margin-top:8px;font-size:19px;font-weight:600}
.line{position:absolute;left:120px;right:120px;top:850px;text-align:center;font-weight:500;font-size:36px;letter-spacing:-.03em;line-height:1.25}""",
f"""{sp}{N(4)}<div class="gw">act</div><div class="line">manifestation without action is a daydream. one small move this week.</div><img class="tl" src="{LOGO}" alt="ISSUE11" style="top:auto;bottom:120px;height:70px"><div class="url" style="color:#0D0D0D">issue11.app</div>""")
P['CAR5-5']=doc('Carousel 5 · slide 5 · evolve (arrow loop)',S+""".pin{background:#F8DCEB}
.wd{position:absolute;font-weight:800;font-size:74px;letter-spacing:-.03em;color:#111}
svg{position:absolute;inset:0}
.mid{position:absolute;left:330px;right:330px;top:860px;text-align:center;font-weight:500;font-size:30px;line-height:1.25;color:#111}""",
f"""{T()}{N(5)}{LOOP}
<div class="wd" style="left:380px;top:300px">desire</div><div class="wd" style="left:700px;top:720px">act</div><div class="wd" style="left:330px;top:1150px">evolve</div><div class="wd" style="left:40px;top:720px">imagine</div>
<div class="mid">every sunday: what changed? adjust. go again.</div>{U('#111')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
