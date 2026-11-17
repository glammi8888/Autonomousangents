# Carousel 2 (CAR2-1..5), Nov 17. Megan: "nahhh the pin is too salesy. We need to make it educational" + "check the brand philosophy and the marketing frameworks please".
# Built only from design/editorial/MARKETING-PLAYBOOK.md §06 "ISSUE11 signature carousel blueprint" (copy word for word) + EDITORIAL-BIBLE.md §15 visual grammar:
# Provocation → Recognition → Insight (research card, sourced) → Diagram (labelled "conceptual model") → Reframe + Empowerment. Cut to Pinterest's 5 slides; slide 7 "product bridge" dropped (no pitch).
# Palette: near-black, cream, pink, red; bold display type + monospace accents; strong negative space; one diagram; restrained CTA.
from gen import doc, LOGO
INK='#111'; CREAM='#F4EEE3'; PINK='#F6C6D6'; RED='#C8102E'
MONO="ui-monospace,'DejaVu Sans Mono','Courier New',monospace"
def base(bg,fg,inv=False): return f""".pin{{background:{bg};color:{fg}}}
.lg{{position:absolute;left:64px;top:56px;height:56px;{'filter:invert(1)' if inv else ''}}}
.mono{{position:absolute;right:64px;top:72px;font-family:{MONO};font-size:22px;letter-spacing:.08em}}
.ft{{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-family:{MONO};font-size:20px;letter-spacing:.06em}}
.big{{position:absolute;left:64px;right:64px;font-weight:900;letter-spacing:-.05em;line-height:.92}}
.sm{{position:absolute;left:64px;right:64px;font-weight:500;letter-spacing:-.02em;line-height:1.25}}"""
def chrome(i,inv=False,src=''): return f'<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="mono">2027 VISION BOARD · 0{i}/05</div><div class="ft"><span>{src}</span><span>issue11.app</span></div>'
P={}
P['CAR2-1']=doc('Carousel 2 · slide 1 · provocation',base(INK,CREAM,True)+".big{top:470px;font-size:126px}",
  f"""{chrome(1,True)}<div class="big">Your vision board might be doing the easy part for&nbsp;you.</div>""")
P['CAR2-2']=doc('Carousel 2 · slide 2 · recognition',base(CREAM,INK)+".big{top:420px;font-size:104px}.sm{top:900px;font-size:52px}",
  f"""{chrome(2)}<div class="big">Imagining a future can feel like progress.</div><div class="sm">Sometimes the hard part is choosing a&nbsp;step.</div>""")
P['CAR2-3']=doc('Carousel 2 · slide 3 · research card',base(CREAM,INK)+f""".tag{{position:absolute;left:64px;top:300px;font-family:{MONO};font-size:24px;letter-spacing:.14em;background:{INK};color:{CREAM};padding:10px 16px}}
.sm{{top:400px;font-size:58px;font-weight:600;letter-spacing:-.03em;line-height:1.15}}
.src{{position:absolute;left:64px;right:64px;top:1130px;border-top:3px solid {INK};padding-top:22px;font-family:{MONO};font-size:22px;line-height:1.5}}""",
  f"""{chrome(3)}<div class="tag">THE RESEARCH</div><div class="sm">Research on mental contrasting suggests that considering obstacles alongside desired outcomes can support goal pursuit in some settings.</div><div class="src">SOURCE · Gabriele Oettingen, mental contrasting<br>WOOP: Wish, Outcome, Obstacle, Plan</div>""")
steps=['DESIRE','OBSTACLE','IF-THEN PLAN','ACTION','REFLECTION']
flow=''.join(f'<div class="st">{s}</div>'+('<div class="ar">↓</div>' if i<4 else '') for i,s in enumerate(steps))
P['CAR2-4']=doc('Carousel 2 · slide 4 · diagram',base(PINK,INK)+f""".fl{{position:absolute;left:64px;right:64px;top:210px;display:flex;flex-direction:column;align-items:center}}
.st{{width:620px;text-align:center;border:4px solid {INK};padding:24px 0;font-weight:900;font-size:62px;letter-spacing:-.03em;background:{CREAM}}}
.st:nth-child(5){{background:{INK};color:{CREAM}}}
.ar{{font-size:58px;line-height:1.1;font-weight:300}}
.lab{{position:absolute;left:0;right:0;top:1300px;text-align:center;font-family:{MONO};font-size:22px;letter-spacing:.12em}}""",
  f"""{chrome(4)}<div class="fl">{flow}</div><div class="lab">CONCEPTUAL MODEL</div>""")
P['CAR2-5']=doc('Carousel 2 · slide 5 · reframe + one step',base(RED,CREAM,True)+f""".big{{top:330px;font-size:112px}}
.sm{{top:930px;font-size:50px;font-weight:600}}
.box{{position:absolute;left:64px;top:910px;width:30px;height:30px;border:4px solid {CREAM}}}""",
  f"""{chrome(5,True)}<div class="big">The dream is not the problem. The missing bridge&nbsp;is.</div><div class="sm" style="left:120px">Pick one obstacle and write one if&#8209;then plan today.</div><div class="box" style="top:944px"></div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
