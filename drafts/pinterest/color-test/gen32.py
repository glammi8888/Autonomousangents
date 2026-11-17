# Carousels in the CAR5 style (CAR12, CAR13), Nov 17. Megan: "I really do like the style of carousel 5 so if we can keep that kind of style it would be great".
# Layout per slide = CAR5: 1 loud poster (101) · 2 plain card (103) · 3 pastel + framed photo (42) · 4 giant word + photos (95) · 5 arrow loop (100).
import gen9, gen8, gen13, gen19
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
B.update({'s3':'cb42026166e754aa61015533d682c479'})
A='alt="Editorial photo (AI-generated)"'
LOOP=open('/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/loop.svg').read().strip()
N=lambda i,c='#111': f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:{c}">{i} / 5</div>'
SM=""".sm{position:absolute;left:90px;right:90px;text-align:center;font-weight:500;font-size:36px;line-height:1.3;letter-spacing:-.015em}
.sm b{font-weight:800}"""
P={}
def car(pre,n,cover,sub,cimg,cpos,k2,w2,s2a,s2b,fimg,fpos,it,s3,gw,spec,line,loop):
    P[f'{pre}-1']=doc(f'Carousel {n} · slide 1 · loud poster cover',S+""".pin{background:#fff;color:#0D0D0D}
.p{position:absolute;left:44px;right:44px;top:200px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
.p .a{font-weight:800;font-size:150px;transform:scaleX(.72);transform-origin:left;display:inline-block;white-space:nowrap}
.p .b{font-weight:900;font-size:168px}
.p .e{font-weight:300;font-style:italic;font-size:110px;text-transform:none;letter-spacing:-.05em;display:block;margin-top:24px}
.sub{position:absolute;left:52px;top:1090px;width:520px;font-weight:900;font-size:48px;line-height:1.05;text-transform:uppercase;letter-spacing:-.02em}
img.f{left:620px;top:1060px;width:330px;height:330px}""",
f"""{T()}{N(1)}<div class="p">{cover}</div><div class="sub">{sub}</div><img class="f" src="{s(cimg)}" style="object-position:{cpos}" {A}>{U('#0D0D0D')}""")
    P[f'{pre}-2']=doc(f'Carousel {n} · slide 2 · plain card',S+SM+""".pin{background:#fff}
.c{top:420px;color:#111;font-weight:400;font-size:170px;line-height:1;letter-spacing:-.05em}
.k{position:absolute;left:0;right:0;top:340px;text-align:center;font-weight:700;font-size:24px;letter-spacing:.2em;color:#C2207E}""",
f"""{T()}{N(2)}<div class="k">{k2}</div><div class="c">{w2}</div><div class="sm" style="top:700px">{s2a}</div><div class="sm" style="top:1000px">{s2b}</div>{U('#111')}""")
    P[f'{pre}-3']=doc(f'Carousel {n} · slide 3 · pastel + framed photo',S+SM+""".pin{background:#F1EBFF}
.it{position:absolute;left:60px;right:60px;top:1000px;text-align:center;font-style:italic;font-weight:400;font-size:62px;letter-spacing:-.03em;color:#111;line-height:1.1}""",
f"""{T()}{N(3)}<img class="f" src="{s(fimg)}" style="left:270px;top:180px;width:460px;height:700px;object-position:{fpos}" {A}>
<div class="it">{it}</div><div class="sm" style="top:1190px">{s3}</div>{U('#111')}""")
    pos=['left:90px;top:200px','right:90px;top:170px','left:110px;top:1040px','right:110px;top:1060px']
    sp=''.join(f'<div class="sp" style="{p}"><img src="{s(k)}" {A}><span>{c}</span></div>' for (k,c),p in zip(spec,pos))
    P[f'{pre}-4']=doc(f'Carousel {n} · slide 4 · giant word + photos',S+""".pin{background:#fff;color:#0D0D0D}
.gw{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:600;font-size:330px;letter-spacing:-.07em;line-height:1}
.sp{position:absolute;width:210px}
.sp img{display:block;width:210px;height:260px;object-fit:cover;object-position:50% 30%}
.sp span{display:block;margin-top:10px;font-size:26px;font-weight:700;line-height:1.1;letter-spacing:-.01em}
.line{position:absolute;left:120px;right:120px;top:850px;text-align:center;font-weight:500;font-size:36px;letter-spacing:-.03em;line-height:1.25}""",
f"""{sp}{N(4)}<div class="gw">{gw}</div><div class="line">{line}</div><img class="tl" src="{LOGO}" alt="ISSUE11" style="top:auto;bottom:120px;height:70px"><div class="url" style="color:#0D0D0D">issue11.app</div>""")
    P[f'{pre}-5']=doc(f'Carousel {n} · slide 5 · arrow loop',S+""".pin{background:#F8DCEB}
.wd{position:absolute;font-weight:800;font-size:74px;letter-spacing:-.03em;color:#111}
svg{position:absolute;inset:0}
.mid{position:absolute;left:330px;right:330px;top:840px;text-align:center;font-weight:500;font-size:30px;line-height:1.25;color:#111}""",
f"""{T()}{N(5)}{LOOP}
<div class="wd" style="left:380px;top:300px">desire</div><div class="wd" style="left:700px;top:720px">act</div><div class="wd" style="left:330px;top:1150px">evolve</div><div class="wd" style="left:40px;top:720px">imagine</div>
<div class="mid">{loop}</div>{U('#111')}""")

car('CAR12',12,'<span class="b">Journal</span><br><span class="b">prompts</span><br><span class="a">for your</span><br><span class="b">dream life</span>',
    'one a night.<br>save this.','curls','50% 30%',
    'PROMPT 01','want','"what do i want so badly<br>i\'m embarrassed to say it?"','<b>mistake:</b> writing what sounds good<br><b>do this:</b> write what\'s true',
    'sky','50% 25%','describe your morning<br>in 2027, minute by minute.','<b>then:</b> what are you wearing? who texts you first?',
    'do',[('closet',''),('room',''),('hair',''),('pinkmoney','')],
    '"what would future me do today?" then do it in the next 10 min.',
    'every sunday: what changed? what don\'t i want anymore? what\'s next?')
car('CAR13',13,'<span class="a">How to</span><br><span class="b">manifest</span><br><span class="b">money</span><span class="e">(realistic)</span>',
    'no overnight.<br>save this.','cashface','50% 25%',
    'STEP 01','number','know your rich af number.<br>say it out loud. write it down.','<b>mistake:</b> "more money" with no number<br><b>do this:</b> one number for this year',
    'pinkmoney','50% 30%','see it: the balance,<br>the bill paid on time.','<b>do this:</b> write what you\'d do with it, line by line',
    'act',[('suit','open a HYSA account'),('bobcash','raise your rates'),('cashpile','invest your money'),('s3','sell what you don\'t use')],
    'the money move is the manifestation. one this week.',
    'every sunday: check the number. adjust. go again.')
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
