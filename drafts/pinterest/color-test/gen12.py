# Round 11 (CT110–CT121), Nov 16: copies of the most-saved pins on Pinterest right now (Apify lergassy~pinterest-search-scraper, 8 searches, 310 pins: ../viral/2026-11-16-viral-pins.json). Megan: "see which pins went viral ... and then make ours similar to theirs too". BANK lines only.
import gen9, gen8
from gen4 import B
from gen import doc, LOGO
A='alt="Editorial photo (AI-generated)"'
def s(k): return f'/_blob/{B[k]}'
S="""img.f{position:absolute;object-fit:cover;display:block}
.full{inset:0;width:100%;height:100%}
.tl{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%);z-index:5}
.url{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:600;font-size:19px;z-index:5}
"""
T=lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
U=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
P={}
# 110 · "send this to yourself" letter (6,420 saves)
P['CT110']=doc('Color test 110 · viral letter + send this to yourself',S+"""
.pin{background:#FBF3EA;color:#2A211A}
.q{position:absolute;left:70px;right:90px;top:380px;font-weight:400;font-size:100px;line-height:1.02;letter-spacing:-.04em}
.k{position:absolute;left:70px;top:1120px;font-weight:600;font-size:18px;letter-spacing:.24em;text-transform:uppercase}
""",f"""{T()}<div class="q">My life can do a 180 in just 1 year. Send this to yourself.</div><div class="k">Save · send · believe</div>{U('#2A211A')}""")
# 111 · orange flat + blue italic (6,136)
P['CT111']=doc('Color test 111 · viral orange + blue italic',S+"""
.pin{background:#FF6533}
.q{position:absolute;left:60px;right:60px;top:470px;text-align:center;color:#24409A;font-style:italic;font-weight:400;font-size:120px;line-height:1;letter-spacing:-.05em}
""",f"""{T()}<div class="q">I make $10,000 a month with ease</div>{U('#24409A')}""")
# 112 · photo + small lowercase caption (lucky girl, 5,718)
P['CT112']=doc('Color test 112 · viral photo + small caption',S+"""
.pin{background:#222}
.cap{position:absolute;left:470px;right:50px;top:1020px;color:#fff;font-weight:500;font-size:62px;line-height:1.15;letter-spacing:-.01em;text-shadow:0 2px 14px rgba(0,0,0,.55)}
""",f"""<img class="f full" src="{s('sleepcash')}" style="object-position:40% 30%" {A}>{T('w')}<div class="cap">i'm the luckiest girl on the planet</div>{U('#fff')}""")
# 113 · stacked repetition "She can. She will…" (5,536) → pink, last line bold
P['CT113']=doc('Color test 113 · viral stacked lines',S+"""
.pin{background:#FCECEF;color:#1A1A1A}
.st{position:absolute;left:60px;right:40px;top:240px;font-size:118px;line-height:1.02;letter-spacing:-.05em}
.st i{font-weight:300}
.st b{font-weight:800}
""",f"""{T()}<div class="st"><b>I am</b> <i>the prize,</i><br><b>I am</b> <i>the prize,</i><br><b>I am</b> <i>the prize,</i><br><b>I am the prize,</b><br><b>always.</b></div>{U('#1A1A1A')}""")
# 114 · pink centred bold (4,770)
P['CT114']=doc('Color test 114 · viral pink centred quote',S+"""
.pin{background:#FCD4DA}
.q{position:absolute;left:110px;right:110px;top:430px;text-align:center;color:#2A0F18;font-weight:700;font-size:86px;line-height:1.35;letter-spacing:-.02em}
""",f"""{T()}<div class="q">I am worthy of love, respect, and everything I desire</div>{U('#2A0F18')}""")
# 115 · wide-spaced plain words on white (3,641)
P['CT115']=doc('Color test 115 · viral spaced words',S+"""
.pin{background:#fff}
.q{position:absolute;left:70px;right:70px;top:500px;color:#111;font-weight:400;font-size:120px;line-height:1.08;letter-spacing:-.03em;text-align:justify;text-align-last:justify;word-spacing:.2em}
""",f"""{T()}<div class="q">my dream life wants me</div>{U('#111')}""")
# 116 · money photo + white italic (2,870)
P['CT116']=doc('Color test 116 · viral money photo + italic',S+"""
.pin{background:#5A4630}
.sh{position:absolute;inset:0;background:rgba(40,25,10,.18)}
.q{position:absolute;left:60px;right:60px;top:560px;text-align:center;color:#fff;font-style:italic;font-weight:300;font-size:104px;line-height:1.05;letter-spacing:-.04em;text-shadow:0 3px 20px rgba(0,0,0,.45)}
""",f"""<img class="f full" src="{s('cashpile')}" style="object-position:50% 40%" {A}><div class="sh"></div>{T('w')}<div class="q">I'm making money in my sleep</div>{U('#fff')}""")
# 117 · note on a tiled wall (2,392)
P['CT117']=doc('Color test 117 · viral note on the wall',S+"""
.pin{background:#2B2723}
.sh{position:absolute;inset:0;background:rgba(0,0,0,.25)}
.note{position:absolute;left:330px;top:1030px;width:340px;background:#F7F2E7;padding:40px 34px;transform:rotate(-3deg);box-shadow:0 18px 40px rgba(0,0,0,.45);font-style:italic;font-weight:400;font-size:58px;line-height:1.1;letter-spacing:-.03em;color:#2B2723}
""",f"""<img class="f full" src="{s('earring')}" style="object-position:50% 25%;filter:blur(6px) brightness(.8)" {A}><div class="sh"></div>{T('w')}<div class="note">I wake up to money</div>{U('#fff')}""")
# 118 · repeat line ×N, one highlighted ("Good things are coming", 1,758)
rep=''.join('<div>Dream life is on its way.</div>' for _ in range(7))+'<div class="hi">Dream life is on its way.</div>'+''.join('<div>Dream life is on its way.</div>' for _ in range(7))
P['CT118']=doc('Color test 118 · viral repeated line',S+"""
.pin{background:#FEFBF4}
.rep{position:absolute;left:90px;top:200px;color:#6A625A;font-weight:300;font-size:56px;line-height:1.28;letter-spacing:-.02em}
.rep .hi{color:#C2207E;font-weight:700}
""",f"""{T()}<div class="rep">{rep}</div>{U('#6A625A')}""")
# 119 · olive flat + dark italic (1,480)
P['CT119']=doc('Color test 119 · viral olive + italic',S+"""
.pin{background:#8A9A5B}
.q{position:absolute;left:70px;right:70px;top:560px;text-align:center;color:#24301A;font-style:italic;font-weight:400;font-size:84px;line-height:1.08;letter-spacing:-.04em}
""",f"""{T()}<div class="q">I make way more money than what I'm able to spend</div>{U('#24301A')}""")
# 120 · black + pink (2027 is my year)
P['CT120']=doc('Color test 120 · viral black + pink 2027',S+"""
.pin{background:#0D0D0D}
.y{position:absolute;left:0;right:0;top:450px;text-align:center;color:#FF8FC0;font-weight:800;font-size:300px;letter-spacing:-.07em;line-height:1}
.t{position:absolute;left:60px;right:60px;top:780px;text-align:center;color:#FF8FC0;font-style:italic;font-weight:300;font-size:90px;letter-spacing:-.04em;line-height:1}
""",f"""{T('w')}<div class="y">2027</div><div class="t">is the year I lifemaxx</div>{U('#FF8FC0')}""")
# 121 · dark celestial (1,198)
stars=''.join(f'<div class="s" style="left:{x}px;top:{y}px;font-size:{z}px">✦</div>' for x,y,z in [(90,300,50),(820,260,70),(150,1150,60),(830,1100,44),(470,1300,36),(860,700,40),(80,760,34)])
P['CT121']=doc('Color test 121 · viral dark celestial',S+"""
.pin{background:#272421}
.s{position:absolute;color:#D9C3A0}
.moon{position:absolute;left:390px;top:300px;width:220px;height:220px;border-radius:50%;box-shadow:-34px 10px 0 0 #D9C3A0}
.q{position:absolute;left:110px;right:110px;top:640px;text-align:center;color:#E8D8BD;font-weight:300;font-size:90px;line-height:1.08;letter-spacing:-.04em}
""",f"""{T('w')}{stars}<div class="moon"></div><div class="q">Thank you universe for all the blessings</div>{U('#E8D8BD')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
