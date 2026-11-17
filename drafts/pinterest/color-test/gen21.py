# Carousel 1 (CAR1-1..5), Nov 17: "Your 2027 vision board, as a magazine" from drafts/social/2026-11-week1-issue11.md P4, cut to Pinterest's 5 slides at 2:3.
# Megan: "ok let's test 'Your 2027 vision board, as a magazine' / Although i think we should make them educative/informative". So it's a how-to with a "Try this" example on each page. Examples come from BANK and the live articles (magazines-for-vision-board, journaling-prompts), not new claims.
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen13 import A
B.update({'s2':'1bbdd0bf5cdc7f980f3968816cf5962b'})
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
def head(i): return f'<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="ct">{i} / 5</div><div class="kick">YOUR 2027 VISION BOARD, AS A MAGAZINE</div>'
def step(n,h,p,t): return f'<div class="n">{n}</div><div class="h">{h}</div><div class="p">{p}</div><div class="try"><b>TRY THIS</b>{t}</div>'
P={}
P['CAR1-1']=cover('CAR1-1','closet','50% 40%','2027','#F3D9A4','Your vision board, as a magazine',[('5','pages to make'),('6','saves for the moodboard'),('1','small move a week')],'linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 45%,rgba(25,18,10,.8) 100%)').replace('Color test AR1-1 · magazine cover · 2027','Carousel 1 · slide 1 · vision board as a magazine')
P['CAR1-2']=doc('Carousel 1 · slide 2 · cover + letter',CSS,f"""{head(2)}
<div class="st" style="top:250px">{step('01','The cover','One line about the year you want, in big type. Put your name on top like a masthead.','"Dream life is on its way"')}</div>
<div class="st" style="top:800px">{step('02',"The editor's letter",'Three sentences to yourself about why this year. Not goals. Reasons.','Which "one day" have you been saying for too long?')}</div>
<img class="ph" src="{s('hair')}" style="top:330px;height:440px;object-position:50% 20%" {A}>
<img class="ph" src="{s('l23')}" style="top:880px;height:440px;object-position:50% 30%" {A}>
<div class="url">issue11.app</div>""")
P['CAR1-3']=doc('Carousel 1 · slide 3 · moodboard',CSS+".g{position:absolute;left:52px;right:52px;top:820px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.g img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block}",f"""{head(3)}
<div class="st" style="top:250px">{step('03','The moodboard','Six saves, one per area of your life. Crop them oddly and keep one colour running through. Less is more editorial.','Home, work, body, love, style, money: one image each')}</div>
<div class="g">{''.join(f'<img src="{s(k)}" style="object-position:50% 30%" {A}>' for k in ['room','suit','shoulder','l23','s2','cashpile'])}</div>
<div class="url">issue11.app</div>""")
P['CAR1-4']=doc('Carousel 1 · slide 4 · small move + proof',CSS,f"""{head(4)}
<div class="st" style="top:250px">{step('04','The small move','Next to each image, write one thing you will do this week. Tiny counts.','"Linen sheets" becomes "wash and iron the good sheets this Sunday"')}</div>
<div class="st" style="top:830px">{step('05','The proof page','Write down what already changed, with the date. Even the small stuff. This is the page you reread.','What changed since last week, even slightly?')}</div>
<img class="ph" src="{s('room')}" style="top:330px;height:440px;object-position:50% 50%" {A}>
<img class="ph" src="{s('sky')}" style="top:910px;height:440px;object-position:50% 25%" {A}>
<div class="url">issue11.app</div>""")
ck=['The cover · one line, big type','The editor\'s letter · three sentences','The moodboard · six saves, one colour','The small move · one thing this week','The proof page · what already changed']
P['CAR1-5']=doc('Carousel 1 · slide 5 · checklist',CSS+""".pin{background:#111;color:#fff}.ct,.url{color:#fff}.kick{color:#FF8FC4}
.big{position:absolute;left:52px;right:52px;top:250px;font-weight:900;font-size:92px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase}
.ck{position:absolute;left:52px;right:52px;top:560px}
.ck div{display:flex;gap:22px;align-items:center;border-top:2px solid rgba(255,255,255,.3);padding:22px 0;font-size:34px;font-weight:600;letter-spacing:-.02em}
.ck span{flex:none;width:40px;height:40px;border:3px solid #FF8FC4}
.end{position:absolute;left:52px;right:52px;top:1150px;font-size:34px;line-height:1.3;font-weight:500}
.end b{color:#FF8FC4}""",f"""<img class="lg w" src="{LOGO}" alt="ISSUE11"><div class="ct">5 / 5</div><div class="kick">SAVE THIS FOR DECEMBER</div>
<div class="big">Your 5 pages, checklist</div>
<div class="ck">{''.join(f'<div><span></span>{x}</div>' for x in ck)}</div>
<div class="end">Paper works. Or make it in <b>ISSUE11</b>: your saves, laid out as your own magazine.</div>
<div class="url">issue11.app</div>""")
for k,v in P.items(): open(f'../carousels/{k}.dc.html','w').write(v); open(f'{k}.dc.html','w').write(v)
print(len(P))
