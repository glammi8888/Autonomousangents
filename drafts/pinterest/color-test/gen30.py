# Carousel templates to pick from (CAR6–CAR8), Nov 17. Megan: "I'd like to have a few more carousel templates too to pick from". Each = 5 slides, no pitch, a searched topic, loved styles only.
import gen9, gen8, gen13, gen19, re
from gen4 import B
from gen import doc, LOGO
from gen12 import S, T, U
A='alt="Editorial photo (AI-generated)"'
B.update({'s3':'cb42026166e754aa61015533d682c479'})
def s(k): return f'/_blob/{B[k]}'
CNT=lambda i,c='#111': f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:{c};z-index:6">{i} / 5</div>'
P={}
# ---- A · phone notes · 369 method explained ----
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
def note(k,i,title,secs):
    bg,inner=ns['notes'](f"{i}/5 · November 17, 2026",title,secs,"x")
    inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
    fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
    inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
    P[k]=ns['doc'](f'Carousel 6 · notes · slide {i}',inner,bg)
note('CAR6-1',1,'369 method explained 🫧',[("what it is",["one sentence","3x in the morning","6x in the afternoon","9x at night","for 21 days"])])
note('CAR6-2',2,'step 1: pick your sentence ✍️',[("make it",["present tense, like it's already yours","short. one line","something you actually want"]),("mine",['"I wake up to money"'])])
note('CAR6-3',3,'step 2: morning ×3 ☀️',[("before your phone",["write it 3 times","say it once out loud","feel it for a second"])])
note('CAR6-4',4,'step 3: afternoon ×6, night ×9 🌙',[("same sentence",["6 times at lunch","9 times before bed","don't change it halfway"])])
note('CAR6-5',5,'step 4: pair it with one action 💸',[("this week",["move $50 to savings","raise your rates (or ask for a raise)"]),("remember",["When manifesting later = never so act now"])])
# ---- B · viral quote pack · scripting examples (110 · 113 · 114 · 125 · 118) ----
P['CAR7-1']=doc('Carousel 7 · slide 1 · letter (110)',S+""".pin{background:#FBF3EA;color:#2A211A}
.q{position:absolute;left:70px;right:90px;top:380px;font-weight:400;font-size:104px;line-height:1.02;letter-spacing:-.04em}
.k{position:absolute;left:70px;top:1120px;font-weight:600;font-size:18px;letter-spacing:.24em;text-transform:uppercase}""",f"""{T()}{CNT(1,'#2A211A')}<div class="q">Scripting examples you can copy. Send this to yourself.</div><div class="k">Save · send · script</div>{U('#2A211A')}""")
P['CAR7-2']=doc('Carousel 7 · slide 2 · stacked (113)',S+""".pin{background:#FCECEF;color:#1A1A1A}
.st{position:absolute;left:60px;right:40px;top:260px;font-size:96px;line-height:1.02;letter-spacing:-.05em}
.st i{font-weight:300}.st b{font-weight:800}
.sm{position:absolute;left:60px;right:60px;top:1050px;font-size:36px;line-height:1.3}""",f"""{T()}{CNT(2)}<div class="st"><b>write it</b> <i>like it's done,</i><br><b>write it</b> <i>like it's real,</i><br><b>write it</b> <i>every night.</i></div><div class="sm">past tense. specific. 5 lines is enough.</div>{U('#1A1A1A')}""")
P['CAR7-3']=doc('Carousel 7 · slide 3 · pink centred (114)',S+""".pin{background:#FCD4DA}
.q{position:absolute;left:110px;right:110px;top:440px;text-align:center;color:#2A0F18;font-weight:700;font-size:86px;line-height:1.3;letter-spacing:-.02em}""",f"""{T()}{CNT(3,'#2A0F18')}<div class="q">it's dec 2027. I worked for myself and i'm booked and busy</div>{U('#2A0F18')}""")
P['CAR7-4']=doc('Carousel 7 · slide 4 · aura (125)',S+""".pin{background:radial-gradient(circle at 50% 52%,#FFF6C8 0%,#E9F2B8 18%,#B9D69A 38%,#8DB884 60%,#6E9A72 100%)}
.q{position:absolute;left:150px;right:150px;top:700px;text-align:center;color:#2D3B22;font-weight:400;font-size:52px;letter-spacing:-.01em;line-height:1.2}""",f"""{T()}{CNT(4,'#2D3B22')}<div class="q">i can afford anything I want</div>{U('#2D3B22')}""")
rep=''.join('<div>I wake up to money.</div>' for _ in range(7))+'<div class="hi">I wake up to money.</div>'+''.join('<div>I wake up to money.</div>' for _ in range(7))
P['CAR7-5']=doc('Carousel 7 · slide 5 · repeated line (118)',S+""".pin{background:#FEFBF4}
.rep{position:absolute;left:90px;top:220px;color:#6A625A;font-weight:300;font-size:56px;line-height:1.28;letter-spacing:-.02em}
.rep .hi{color:#C2207E;font-weight:700}""",f"""{T()}{CNT(5,'#6A625A')}<div class="rep">{rep}</div>{U('#6A625A')}""")
# ---- C · photo story · how to manifest money (full-bleed quote style, 156/158/185) ----
SH='<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 52%,rgba(0,0,0,.75) 90%)"></div>'
def ph(k,i,key,pos,html,fs=84,small=''):
    P[k]=doc(f'Carousel 8 · photo · slide {i}',S+f""".q{{position:absolute;left:60px;right:60px;top:1060px;text-align:center;color:#fff;font-weight:800;font-size:{fs}px;letter-spacing:-.04em;line-height:1.02;text-shadow:0 4px 24px rgba(0,0,0,.6);text-wrap:balance}}
.q i{{font-weight:300}}.s{{position:absolute;left:80px;right:80px;top:1320px;text-align:center;color:#fff;font-size:30px;font-weight:500}}""",
      f"""<img class="f full" src="{s(key)}" style="object-position:{pos}" {A}>{SH}{T('w')}{CNT(i,'#fff')}<div class="q">{html}</div>{f'<div class="s">{small}</div>' if small else ''}<div class="url" style="color:#fff;bottom:40px">issue11.app</div>""")
ph('CAR8-1',1,'cashface','50% 25%','how to manifest money <i>(realistic)</i>')
ph('CAR8-2',2,'cashpile','50% 50%','say your number out loud',small='know your rich af number')
ph('CAR8-3',3,'suit','50% 0%','Open a HYSA account just for future you',fs=70)
ph('CAR8-4',4,'bobcash','50% 25%','raise your rates <i>(or ask for a raise)</i>',fs=76)
ph('CAR8-5',5,'s3','50% 30%',"I make way more money than what I'm able to spend",fs=66)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
