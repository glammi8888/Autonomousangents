# ONE graph (the manifestation loop) in the look of pin #100, across different approved pin styles (LP1–LP9), Nov 17.
# Megan: "I want the graphs to keep the look of pin # 100" + "Just give me 1 graph in different pin styles and we can mix and match from there".
# #100 look = thick round hand-drawn black arrows (stroke 14), bold floating words, no boxes, small sparkles. Words = her graph: desire · imagine · act · evolve, "continuous creation".
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
ARW='<path d="M190 600 C150 460 220 380 330 360"/><path d="M300 330 l40 30 -40 35"/><path d="M700 380 C860 400 900 520 860 640"/><path d="M820 610 l40 40 45 -45"/><path d="M860 960 C860 1080 780 1150 680 1170"/><path d="M710 1130 l-40 40 45 35"/><path d="M260 1110 C160 1040 140 920 180 830"/><path d="M150 870 l30 -45 40 40"/>'
def loop(ink='#111',fw=800,fs=74,sw=14,mid='continuous<br>creation',midc=None,sp='#E8A9D4',caps=False,font_style='',shadow=''):
    W=lambda t: ' '.join(t.upper()) if caps else t
    ls='.35em' if caps else '-.03em'
    st=f'position:absolute;font-weight:{fw};font-size:{fs}px;letter-spacing:{ls};color:{ink};{font_style}{shadow}'
    o=f'<svg viewBox="0 0 1000 1500" style="position:absolute;inset:0"><g fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ARW}</g></svg>'
    o+=f'<div style="{st};left:0;right:0;text-align:center;top:300px">{W("desire")}</div>'
    o+=f'<div style="{st};right:70px;top:720px">{W("imagine")}</div>'
    o+=f'<div style="{st};left:0;right:0;text-align:center;top:1150px">{W("act")}</div>'
    o+=f'<div style="{st};left:70px;top:720px">{W("evolve")}</div>'
    if mid: o+=f'<div style="position:absolute;left:330px;right:330px;top:800px;text-align:center;font-style:italic;font-weight:500;font-size:38px;line-height:1.1;color:{midc or ink};{shadow}">{mid}</div>'
    if sp: o+=f'<div style="position:absolute;left:470px;top:560px;color:{sp};font-size:110px">✦</div><div style="position:absolute;left:600px;top:1000px;color:{sp};font-size:70px">✦</div>'
    return o
def box(inner,top=0,scale=1):  # place a scaled copy of the 1000x1500 loop
    return f'<div style="position:absolute;left:0;top:{top}px;width:1000px;height:1500px;transform:scale({scale});transform-origin:50% 0">{inner}</div>'
P={}
# LP1 · #100 as is (pink)
P['LP1']=doc('Loop 1 · pin 100 look',S+'.pin{background:#F8DCEB}',f'{T()}{loop()}{U("#111")}')
# LP2 · 101 loud poster title + loop
P['LP2']=doc('Loop 2 · loud poster',S+""".pin{background:#fff;color:#0D0D0D}
.p{position:absolute;left:44px;right:44px;top:190px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
.p .a{font-weight:800;font-size:118px;transform:scaleX(.72);transform-origin:left;display:inline-block;white-space:nowrap}
.p .b{font-weight:900;font-size:106px}""",
f'{T()}<div class="p"><span class="a">the</span> <span class="b">manifestation</span><br><span class="b">loop</span></div>{box(loop(sp=None,mid=None),top=300,scale=.72)}{U("#0D0D0D")}')
# LP3 · 103 plain lowercase, light words, thinner arrows
P['LP3']=doc('Loop 3 · plain lowercase',S+'.pin{background:#fff}',f'{T()}{loop(fw=400,fs=84,sw=8,sp=None)}{U("#111")}')
# LP4 · 42 lilac + framed photo in the middle
P['LP4']=doc('Loop 4 · lilac + framed photo',S+'.pin{background:#F1EBFF}',
 f'{T()}{loop(sp=None,mid=None)}<img class="f" src="{s("sky")}" style="left:340px;top:520px;width:320px;height:460px;object-position:50% 25%" {A}><div style="position:absolute;left:0;right:0;top:1300px;text-align:center;font-style:italic;font-size:44px;color:#111">continuous creation</div>{U("#111")}')
# LP5 · 110 cream letter, brown ink, regular weight
P['LP5']=doc('Loop 5 · cream letter',S+'.pin{background:#FBF3EA}',f'{T()}{loop(ink="#2A211A",fw=400,fs=80,sw=9,sp=None)}{U("#2A211A")}')
# LP6 · 125 aura gradient, green ink
P['LP6']=doc('Loop 6 · aura',S+'.pin{background:radial-gradient(circle at 50% 52%,#FFF6C8 0%,#E9F2B8 18%,#B9D69A 38%,#8DB884 60%,#6E9A72 100%)}',
 f'{T()}{loop(ink="#2D3B22",fw=600,sp="#FFF6C8")}{U("#2D3B22")}')
# LP7 · 114 pink centred, magenta words
P['LP7']=doc('Loop 7 · pink + magenta',S+'.pin{background:#FCD4DA}',f'{T()}{loop(ink="#C2207E",fw=700,sp="#fff",midc="#2A0F18")}{U("#2A0F18")}')
# LP8 · 137 spaced caps on cream
P['LP8']=doc('Loop 8 · spaced caps',S+'.pin{background:#FAF6F0}',f'{T()}{loop(fw=500,fs=38,sw=6,sp=None,caps=True,mid="CONTINUOUS<br>CREATION")}{U("#111")}')
# LP9 · 133 full photo, white arrows
P['LP9']=doc('Loop 9 · full photo',S+'.pin{background:#000}',
 f'<img class="f full" src="{s("closet")}" style="object-position:50% 40%" {A}><div style="position:absolute;inset:0;background:rgba(0,0,0,.0)"></div>{T("w")}{loop(ink="#fff",shadow="text-shadow:0 2px 14px rgba(0,0,0,.75);",sp=None,mid=None)}{U("#fff")}')
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
