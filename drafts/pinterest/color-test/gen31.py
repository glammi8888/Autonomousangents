# More carousel options (CAR9–CAR11), Nov 17. Megan: "ok give me a few more carousel options please".
# Built on the approved templates: CAR9 = CAR5 template (styles 101/103/42/95/100) · CAR10 = CAR6 phone notes · CAR11 = CAR8 photo story, no fade (Megan: "no fade").
# Topics = real Pinterest searches (viral/2026-11-17-manifest-questions.md). Educational, no pitch, no promises.
import gen9, gen8, gen13, gen19, re
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
LOOP=open('/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/loop.svg').read().strip()
N=lambda i,c='#111': f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:{c};z-index:6">{i} / 5</div>'
SM=""".sm{position:absolute;left:90px;right:90px;text-align:center;font-weight:500;font-size:36px;line-height:1.3;letter-spacing:-.015em}
.sm b{font-weight:800}"""
P={}
# ---- CAR9 · CAR5 template · how to make a vision board you actually use ----
P['CAR9-1']=doc('Carousel 9 · slide 1 · loud poster cover',S+""".pin{background:#fff;color:#0D0D0D}
.p{position:absolute;left:44px;right:44px;top:200px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
.p .a{font-weight:800;font-size:150px;transform:scaleX(.72);transform-origin:left;display:inline-block;white-space:nowrap}
.p .b{font-weight:900;font-size:168px}
.sub{position:absolute;left:52px;top:1090px;width:520px;font-weight:900;font-size:48px;line-height:1.05;text-transform:uppercase;letter-spacing:-.02em}
img.f{left:620px;top:1060px;width:330px;height:330px}""",
f"""{T()}{N(1)}<div class="p"><span class="a">How to make</span><br><span class="b">a vision</span><br><span class="b">board</span> <span class="a">you</span><br><span class="a">actually use</span></div>
<div class="sub">save this<br>for january.</div><img class="f" src="{s('room')}" style="object-position:50% 40%" {A}>{U('#0D0D0D')}""")
P['CAR9-2']=doc('Carousel 9 · slide 2 · pick (plain card)',S+SM+""".pin{background:#fff}
.c{top:420px;color:#111;font-weight:400;font-size:170px;line-height:1;letter-spacing:-.05em}
.k{position:absolute;left:0;right:0;top:340px;text-align:center;font-weight:700;font-size:24px;letter-spacing:.2em;color:#C2207E}""",
f"""{T()}{N(2)}<div class="k">STEP 01</div><div class="c">pick</div><div class="sm" style="top:700px">3 areas max.<br>money. home. you.</div>
<div class="sm" style="top:960px"><b>mistake:</b> 40 photos of everything<br><b>do this:</b> one row per area</div>{U('#111')}""")
P['CAR9-3']=doc('Carousel 9 · slide 3 · imagine (pastel + framed photo)',S+SM+""".pin{background:#F1EBFF}
.it{position:absolute;left:60px;right:60px;top:1000px;text-align:center;font-style:italic;font-weight:400;font-size:62px;letter-spacing:-.03em;color:#111;line-height:1.1}""",
f"""{T()}{N(3)}<img class="f" src="{s('sky')}" style="left:270px;top:180px;width:460px;height:700px;object-position:50% 25%" {A}>
<div class="it">pick photos of a normal<br>tuesday in your new life.</div><div class="sm" style="top:1190px"><b>do this:</b> one line under each photo, like it's already yours</div>{U('#111')}""")
spec=[('room','','left:90px;top:200px'),('closet','','right:90px;top:170px'),('hair','','left:110px;top:1040px'),('pinkmoney','','right:110px;top:1060px')]
sp=''.join(f'<div class="sp" style="{p}"><img src="{s(k)}" {A}><span>{c}</span></div>' for k,c,p in spec)
P['CAR9-4']=doc('Carousel 9 · slide 4 · see it (giant word + specimens)',S+""".pin{background:#fff;color:#0D0D0D}
.gw{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:600;font-size:300px;letter-spacing:-.07em;line-height:1}
.sp{position:absolute;width:210px}
.sp img{display:block;width:210px;height:260px;object-fit:cover;object-position:50% 30%}
.sp span{display:block;margin-top:8px;font-size:19px;font-weight:600}
.line{position:absolute;left:120px;right:120px;top:830px;text-align:center;font-weight:500;font-size:36px;letter-spacing:-.03em;line-height:1.25}""",
f"""{sp}{N(4)}<div class="gw">see it</div><div class="line">a board you never look at is just a collage. lock screen, mirror, desk: where you look every day.</div><img class="tl" src="{LOGO}" alt="ISSUE11" style="top:auto;bottom:120px;height:70px"><div class="url" style="color:#0D0D0D">issue11.app</div>""")
P['CAR9-5']=doc('Carousel 9 · slide 5 · evolve (arrow loop)',S+""".pin{background:#F8DCEB}
.wd{position:absolute;font-weight:800;font-size:74px;letter-spacing:-.03em;color:#111}
svg{position:absolute;inset:0}
.mid{position:absolute;left:330px;right:330px;top:840px;text-align:center;font-weight:500;font-size:30px;line-height:1.25;color:#111}""",
f"""{T()}{N(5)}{LOOP}
<div class="wd" style="left:380px;top:300px">desire</div><div class="wd" style="left:700px;top:720px">act</div><div class="wd" style="left:330px;top:1150px">evolve</div><div class="wd" style="left:40px;top:720px">imagine</div>
<div class="mid">every month: take off what you got. swap what you stopped wanting.</div>{U('#111')}""")
# ---- CAR10 · CAR6 phone notes · journal prompts for manifesting your dream life ----
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
def note(k,i,title,secs):
    bg,inner=ns['notes'](f"{i}/5 · November 17, 2026",title,secs,"x")
    inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
    fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
    inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
    P[k]=ns['doc'](f'Carousel 10 · notes · slide {i}',inner,bg)
note('CAR10-1',1,'journal prompts for my dream life 📓',[("how i use them",["one prompt a night","5 min, no rules","write like it already happened"])])
note('CAR10-2',2,'desire ✨',[("prompts",["what do i want so badly i'm embarrassed to say it?","whose life makes me jealous, and which part exactly?"])])
note('CAR10-3',3,'imagine 🌙',[("prompts",["my morning in 2027, minute by minute","what am i wearing?","who texts me first?"])])
note('CAR10-4',4,'act 💸',[("prompts",["what would future me do today?","what am i avoiding that she wouldn't?","what can i do in 10 min right now?"])])
note('CAR10-5',5,'evolve 🔁',[("every sunday",["what changed?","what do i not want anymore?","what's next?"])])
# ---- CAR11 · CAR8 photo story (no fade) · manifestation tips for beginners ----
def ph(k,i,key,pos,html,fs=84,small=''):
    P[k]=doc(f'Carousel 11 · photo · slide {i}',S+f""".q{{position:absolute;left:60px;right:60px;top:1060px;text-align:center;color:#fff;font-weight:800;font-size:{fs}px;letter-spacing:-.04em;line-height:1.02;text-shadow:0 2px 10px rgba(0,0,0,.55),0 4px 30px rgba(0,0,0,.45);text-wrap:balance}}
.q i{{font-weight:300}}.s{{position:absolute;left:80px;right:80px;top:1320px;text-align:center;color:#fff;font-size:30px;font-weight:600;text-shadow:0 2px 10px rgba(0,0,0,.7)}}""",
      f"""<img class="f full" src="{s(key)}" style="object-position:{pos}" {A}>{T('w')}{N(i,'#fff').replace('z-index:6','z-index:6;text-shadow:0 2px 8px rgba(0,0,0,.7)')}<div class="q">{html}</div>{f'<div class="s">{small}</div>' if small else ''}<div class="url" style="color:#fff;bottom:40px;text-shadow:0 2px 8px rgba(0,0,0,.7)">issue11.app</div>""")
ph('CAR11-1',1,'closet','50% 30%','manifestation tips for beginners <i>(no fluff)</i>',fs=78)
ph('CAR11-2',2,'sky','50% 25%','make it specific',small='a number. a place. a date.')
ph('CAR11-3',3,'hair','50% 25%','write it like it already happened',fs=76)
ph('CAR11-4',4,'flying','50% 30%','do one thing this week that she would do',fs=70)
ph('CAR11-5',5,'pinkmoney','50% 30%','every sunday: adjust. go again.',fs=76)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
