# Carousel 3 (CAR3-1..5), Nov 17. Megan's hook: "How to manifest your dream life 101" (also a real Pinterest search: "how to manifest your dream life").
# The 101 = ISSUE11's method DESIRE → IMAGINE → ACT → EVOLVE taught as 4 lessons (rule · common mistake · do this). Bible §15 palette; one loop diagram (conceptual model). No pitch.
from gen import doc, LOGO
INK='#111'; CREAM='#F4EEE3'; PINK='#F6C6D6'; RED='#C8102E'
MONO="ui-monospace,'DejaVu Sans Mono','Courier New',monospace"
CSS=f""".pin{{background:{CREAM};color:{INK}}}
.lg{{position:absolute;left:64px;top:56px;height:56px}}
.mono{{position:absolute;right:64px;top:72px;font-family:{MONO};font-size:22px;letter-spacing:.08em}}
.url{{position:absolute;right:64px;bottom:56px;font-family:{MONO};font-size:20px;letter-spacing:.06em}}
.no{{position:absolute;left:64px;top:220px;font-family:{MONO};font-size:26px;letter-spacing:.14em;color:{RED}}}
.h{{position:absolute;left:64px;right:64px;top:270px;font-weight:900;font-size:170px;letter-spacing:-.06em;line-height:.9}}
.rule{{position:absolute;left:64px;right:64px;top:480px;font-weight:700;font-size:56px;letter-spacing:-.03em;line-height:1.12}}
.box{{position:absolute;left:64px;right:64px;padding:26px 30px;font-size:38px;line-height:1.28;letter-spacing:-.015em}}
.box b{{display:block;font-family:{MONO};font-weight:400;font-size:22px;letter-spacing:.14em;margin-bottom:10px}}
.mis{{top:900px;border:3px solid {INK}}}
.do{{top:1130px;background:{INK};color:{CREAM}}}
"""
def lesson(i,word,rule,mis,do,mt=900,dt=1130):
    return doc(f'Carousel 3 · slide {i} · {word}',CSS,f"""<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="mono">MANIFESTATION 101 · 0{i}/05</div>
<div class="no">LESSON 0{i-1}</div><div class="h">{word}</div><div class="rule">{rule}</div>
<div class="box mis" style="top:{mt}px"><b>COMMON MISTAKE</b>{mis}</div><div class="box do" style="top:{dt}px"><b>DO THIS</b>{do}</div><div class="url">issue11.app</div>""")
P={}
P['CAR3-1']=doc('Carousel 3 · slide 1 · cover',CSS+f""".pin{{background:{INK};color:{CREAM}}}.lg{{filter:invert(1)}}
.t{{position:absolute;left:64px;right:64px;top:330px;font-weight:900;font-size:150px;letter-spacing:-.06em;line-height:.88}}
.t span{{color:{PINK}}}
.ls{{position:absolute;left:64px;right:64px;top:1020px;font-family:{MONO};font-size:30px;line-height:1.7;letter-spacing:.06em}}""",
f"""<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="mono">MANIFESTATION 101 · 01/05</div>
<div class="t">How to manifest your dream life <span>101</span></div>
<div class="ls">01 DESIRE<br>02 IMAGINE<br>03 ACT<br>04 EVOLVE</div><div class="url">issue11.app</div>""")
P['CAR3-2']=lesson(2,'desire','Get specific. "I want to be rich" is a mood. "I want $5k saved by June" is a desire.','wanting everything at once','pick one thing for this season. write it down.')
P['CAR3-3']=lesson(3,'imagine','See it in detail. Then see what\'s in the way. The dream + the obstacle together is what gets you moving.','only picturing the end result','write the one thing most likely to stop you.')
P['CAR3-4']=lesson(4,'act','Manifestation without action is a daydream.','waiting for a sign before you take action','make one if-then plan: "if it\'s sunday night, then I move $50 to savings."',mt=780,dt=1010)
steps=['desire','imagine','act','evolve']
P['CAR3-5']=doc('Carousel 3 · slide 5 · evolve',CSS+f""".lp{{position:absolute;left:64px;right:64px;top:1000px;display:flex;align-items:center;justify-content:space-between;font-weight:900;font-size:40px;letter-spacing:-.03em}}
.lp span.ar{{font-weight:300}}
.back{{position:absolute;left:64px;right:64px;top:1070px;text-align:center;font-family:{MONO};font-size:22px;letter-spacing:.08em}}""",
f"""<img class="lg" src="{LOGO}" alt="ISSUE11"><div class="mono">MANIFESTATION 101 · 05/05</div>
<div class="no">LESSON 04</div><div class="h">evolve</div><div class="rule">Don't ask "did it manifest yet?" Ask what changed this week that makes it more possible than yesterday. Adjust. Go again.</div>
<div class="lp">{'<span class="ar">→</span>'.join(f'<span>{s}</span>' for s in steps)}</div><div class="back">↺ then back to desire · conceptual model</div><div class="url">issue11.app</div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
