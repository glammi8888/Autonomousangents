# Carousel 4 (CAR4-1..5), Nov 17. CAR3's "How to manifest your dream life 101" content in CAR1's look (Megan: "The aesthetic of the first carousel you created I liked too"). No pitch (CAR1's "make it in ISSUE11" line removed).
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen13 import A
from gen5 import cover
def s(k): return f'/_blob/{B[k]}'
CSS=""".pin{background:#FBF8F3;color:#111}
.lg{position:absolute;left:52px;top:44px;height:70px}
.ct{position:absolute;right:52px;top:62px;font-weight:700;font-size:22px;letter-spacing:.2em}
.kick{position:absolute;left:52px;top:170px;font-weight:700;font-size:24px;letter-spacing:.24em;color:#C2207E}
.st{position:absolute;left:52px;right:52px}
.n{font-weight:900;font-size:120px;line-height:.85;letter-spacing:-.06em}
.h{max-width:520px;font-weight:900;font-size:58px;line-height:.95;letter-spacing:-.045em;text-transform:uppercase;margin-top:8px}
.p{font-weight:500;font-size:31px;line-height:1.3;letter-spacing:-.015em;margin-top:16px;max-width:520px}
.try{margin-top:20px;border-left:6px solid #C2207E;padding:6px 0 6px 20px;font-size:28px;line-height:1.3;max-width:520px}
.try b{display:block;font-size:20px;letter-spacing:.2em;color:#C2207E;margin-bottom:4px}
.ph{position:absolute;right:52px;width:330px;object-fit:cover}
.url{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-weight:600;font-size:19px}
"""
def head(i): return f'<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="ct">{i} / 5</div><div class="kick">HOW TO MANIFEST YOUR DREAM LIFE 101</div>'
def step(n,h,p,m,t): return f'<div class="n">{n}</div><div class="h">{h}</div><div class="p">{p}</div><div class="try"><b>COMMON MISTAKE</b>{m}</div><div class="try"><b>DO THIS</b>{t}</div>'
P={}
P['CAR4-1']=cover('CAR4-1','closet','50% 40%','101','#F3D9A4','How to manifest your dream life',[('01','desire'),('02','imagine'),('03','act'),('04','evolve')],'linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 45%,rgba(25,18,10,.82) 100%)').replace('Color test AR4-1 · magazine cover · 101','Carousel 4 · slide 1 · manifestation 101')
P['CAR4-2']=doc('Carousel 4 · slide 2 · desire + imagine',CSS,f"""{head(2)}
<div class="st" style="top:240px">{step('01','Desire','Get specific. "I want to be rich" is a mood. "I want $5k saved by June" is a desire.','wanting everything at once','pick one thing for this season')}</div>
<div class="st" style="top:830px">{step('02','Imagine',"See it in detail. Then see what's in the way.",'only picturing the end result','write the one thing most likely to stop you')}</div>
<img class="ph" src="{s('pinkmoney')}" style="top:330px;height:440px;object-position:50% 25%" {A}>
<img class="ph" src="{s('sky')}" style="top:920px;height:440px;object-position:50% 25%" {A}>
<div class="url">issue11.app</div>""")
P['CAR4-3']=doc('Carousel 4 · slide 3 · act',CSS+".big{position:absolute;left:52px;right:52px;top:860px;height:520px;width:auto;object-fit:cover}",f"""{head(3)}
<div class="st" style="top:240px">{step('03','Act','Manifestation without action is a daydream.','waiting for a sign before you take action','one if-then plan: "if it\'s sunday night, then I move $50 to savings"')}</div>
<img class="big" src="{s('suit')}" style="object-position:50% 0%;width:calc(100% - 104px)" {A}>
<div class="url">issue11.app</div>""")
lp=''.join(f'<span>{w}</span>'+('<i>→</i>' if i<3 else '') for i,w in enumerate(['DESIRE','IMAGINE','ACT','EVOLVE']))
P['CAR4-4']=doc('Carousel 4 · slide 4 · evolve + loop',CSS+""".loop{position:absolute;left:52px;right:52px;top:930px;border:4px solid #111;padding:44px 30px 30px;text-align:center}
.loop .r{display:flex;justify-content:space-between;align-items:center;font-weight:900;font-size:44px;letter-spacing:-.03em}
.loop i{font-style:normal;font-weight:300;color:#C2207E}
.loop .b{margin-top:22px;font-size:24px;letter-spacing:.14em;color:#C2207E;font-weight:700}
.loop .lab{margin-top:10px;font-size:18px;letter-spacing:.2em}""",f"""{head(4)}
<div class="st" style="top:240px">{step('04','Evolve','Don\'t ask "did it manifest yet?" Ask what changed this week that makes it more possible. Adjust. Go again.','giving up when it looks different than you pictured','every sunday, write one thing that changed')}</div>
<div class="loop"><div class="r">{lp}</div><div class="b">↺ AND AGAIN</div><div class="lab">CONCEPTUAL MODEL</div></div>
<img class="ph" src="{s('hair')}" style="top:330px;height:440px;object-position:45% 20%" {A}>
<div class="url">issue11.app</div>""")
ck=['Desire · pick one thing for this season','Imagine · name what\'s in the way','Act · one if-then plan this week','Evolve · every sunday, what changed?']
P['CAR4-5']=doc('Carousel 4 · slide 5 · checklist',CSS+""".pin{background:#111;color:#fff}.ct,.url{color:#fff}.kick{color:#FF8FC4}
.big{position:absolute;left:52px;right:52px;top:250px;font-weight:900;font-size:92px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase}
.ck{position:absolute;left:52px;right:52px;top:600px}
.ck div{display:flex;gap:22px;align-items:center;border-top:2px solid rgba(255,255,255,.3);padding:26px 0;font-size:36px;font-weight:600;letter-spacing:-.02em}
.ck span{flex:none;width:40px;height:40px;border:3px solid #FF8FC4}""",f"""<img class="lg w" src="{LOGO}" alt="ISSUE11"><div class="ct">5 / 5</div><div class="kick">SAVE THIS</div>
<div class="big">Your manifestation 101 checklist</div>
<div class="ck">{''.join(f'<div><span></span>{x}</div>' for x in ck)}</div>
<div class="url">issue11.app</div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
