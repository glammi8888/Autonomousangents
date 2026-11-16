# Round 12 (CT122–CT131), Nov 16: viral vision board + manifestation formats (../viral/2026-11-16-viral-vb-manifest.json, 230 pins). Megan: "Also same with visionboard / Manifestation in particular !!!! Because that trend is all year long". BANK lines only.
import gen9, gen8
from gen4 import B
from gen import doc, LOGO
B.update({'l23':'f9aebbe835f6f14787a79bcfba5c4f11','closet':'e0b2acd5fe4e7845cf15c0a2d79a2367','room':'192e7090c0bebed08ef694877d2afefc','e21':'7c7c9f7639583c427c5ebf34599a953c'})
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
# 122 · big pink word over a calm photo ("manifesting", 4,377)
P['CT122']=doc('Color test 122 · viral pink keyword over photo · manifesting',S+"""
.pin{background:#222}
.kw{position:absolute;left:0;right:0;top:1000px;text-align:center;color:#FF4FA3;font-weight:800;font-size:178px;letter-spacing:-.07em;line-height:1;text-shadow:0 4px 30px rgba(0,0,0,.25)}
.sub{position:absolute;left:0;right:0;top:1200px;text-align:center;color:#fff;font-weight:500;font-size:40px;text-shadow:0 2px 14px rgba(0,0,0,.5)}
""",f"""<img class="f full" src="{s('bighair')}" style="object-position:50% 25%" {A}>{T('w')}<div class="kw">manifesting</div><div class="sub">I attract the best of the best</div>{U('#fff')}""".replace('I attract the best of the best','I only attract the best of the best'))
# 123 · grey card + "save this pin to affirm!" (3,487)
P['CT123']=doc('Color test 123 · viral save-to-affirm card',S+"""
.pin{background:#D9D9D9;color:#111}
.k{position:absolute;left:0;right:0;top:300px;text-align:center;font-weight:800;font-size:72px;letter-spacing:-.02em}
.q{position:absolute;left:90px;right:90px;top:430px;text-align:center;font-weight:700;font-size:84px;line-height:1.14;letter-spacing:-.03em}
.cta{position:absolute;left:0;right:0;top:1130px;text-align:center;font-weight:700;font-size:44px}
""",f"""{T()}<div class="k">TONIGHT</div><div class="q">The right people, places, and moments find me</div><div class="cta">save this pin to affirm !</div>{U('#111')}""")
# 124 · repeated blocks (Manifesting is so easy for me ×5)
L=["Dream life is on its way","My dream life wants me","The right people, places, and moments find me"]
blk=''.join('<div class="b">'+''.join(f'<div>{x}</div>' for _ in range(5))+'</div>' for x in L)
P['CT124']=doc('Color test 124 · viral repeated blocks',S+"""
.pin{background:#fff}
.bk{position:absolute;left:80px;right:60px;top:250px;color:#222;font-weight:400;font-size:40px;line-height:1.42}
.b{margin-bottom:56px}
""",f"""{T()}<div class="bk">{blk}</div>{U('#222')}""")
# 125 · aura gradient + small text (i attract everything i want)
P['CT125']=doc('Color test 125 · viral aura gradient',S+"""
.pin{background:radial-gradient(circle at 50% 52%,#FFF6C8 0%,#E9F2B8 18%,#B9D69A 38%,#8DB884 60%,#6E9A72 100%)}
.q{position:absolute;left:150px;right:150px;top:700px;text-align:center;color:#2D3B22;font-weight:400;font-size:48px;letter-spacing:-.01em;line-height:1.2}
""",f"""{T()}<div class="q">i only attract the best of the best</div>{U('#2D3B22')}""")
# 126 · notes app journal prompts (article)
pr=["What have you saved the most this year?","Describe an ordinary Tuesday a year from now.","Which \"one day\" have you been saying for too long?","If nobody would see this page, what would you admit you want?","Whose life do you keep watching?","What would you stop saying yes to?","What's one move you could make in 20 minutes?","What's most likely to get in the way this week?","What changed since last week, even slightly?"]
P['CT126']=doc('Color test 126 · viral notes app journal prompts',S+"""
.pin{background:#0D0D0D;color:#fff}
.bar{position:absolute;left:60px;right:60px;top:150px;display:flex;justify-content:space-between;color:#F2B84B;font-size:30px;font-weight:600}
h1{position:absolute;left:60px;right:60px;top:220px;margin:0;font-weight:800;font-size:66px;line-height:1.05;letter-spacing:-.03em}
.sm{position:absolute;left:60px;top:390px;font-weight:700;font-size:30px}
ul{position:absolute;left:60px;right:60px;top:440px;margin:0;padding-left:34px;font-size:34px;line-height:1.5;font-weight:400}
""",f"""{T('w')}<div class="bar"><span>‹ Notes</span><span>Done</span></div><h1>manifestation journal prompts 💌</h1><div class="sm">for one quiet evening:</div><ul>{''.join(f'<li>{x}</li>' for x in pr)}</ul>{U('#fff')}""")
# 127 · 369 method journal page
def rep(x,n): return ''.join(f'<div>{x}</div>' for _ in range(n))
P['CT127']=doc('Color test 127 · viral 369 method page',S+"""
.pin{background:#E9E2D4}
.pg{position:absolute;left:90px;right:70px;top:150px;bottom:110px;background:#FBF8F0;box-shadow:0 18px 40px rgba(60,40,10,.18);padding:50px 50px;transform:rotate(-1deg);color:#2A2A2A;font-style:italic;font-weight:400}
.pg h2{margin:0 0 10px;font-style:normal;font-weight:700;font-size:40px;letter-spacing:.06em;text-align:center}
.pg b{display:block;margin:20px 0 6px;font-style:normal;font-weight:700;font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:#C2207E}
.pg div{font-size:32px;line-height:1.3}
""",f"""{T()}<div class="pg"><h2>369 METHOD</h2><b>Morning ×3</b>{rep('I wake up to money',3)}<b>Afternoon ×6</b>{rep('My nervous system is calm',6)}<b>Night ×9</b>{rep('Thank you universe for all the blessings',9)}</div>{U('#2A2A2A')}""")
# 128 · vision board 2027 grid
ks=['closet','cashpile','room','sky','e21','pinkgloss','l23','hair']
g=''.join(f'<img src="{s(k)}" style="object-position:50% 35%" {A}>' for k in ks)
P['CT128']=doc('Color test 128 · viral vision board grid 2027',S+"""
.pin{background:#111}
.g{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:6px}
.g img{width:100%;height:100%;object-fit:cover;display:block}
.lab{position:absolute;left:0;right:0;top:680px;text-align:center;color:#fff;font-style:italic;font-weight:400;font-size:90px;letter-spacing:-.03em;text-shadow:0 4px 30px rgba(0,0,0,.7)}
""",f"""<div class="g">{g}</div>{T('w')}<div class="lab">2027 vision board</div>{U('#fff')}""")
# 129 · film photo + serif-like caption (everything i want…, 2,875)
P['CT129']=doc('Color test 129 · viral film caption',S+"""
.pin{background:#2A1F1C}
img.f{filter:saturate(.8) contrast(1.05) sepia(.12)}
.c{position:absolute;left:60px;right:60px;top:1100px;text-align:center;color:#fff;font-weight:300;font-size:72px;letter-spacing:-.02em;line-height:1.1;text-shadow:0 2px 18px rgba(0,0,0,.6)}
""",f"""<img class="f full" src="{s('l23')}" style="object-position:50% 30%" {A}>{T('w')}<div class="c">the love of my life is coming to me</div>{U('#fff')}""")
# 130 · dreamy sky + small italic (goddess)
P['CT130']=doc('Color test 130 · viral dreamy photo + small italic',S+"""
.pin{background:#1D47B8}
.c{position:absolute;left:0;right:0;top:1150px;text-align:center;color:#fff;font-style:italic;font-weight:300;font-size:56px;letter-spacing:-.02em;text-shadow:0 2px 16px rgba(0,0,0,.5)}
""",f"""<img class="f full" src="{s('sky')}" style="object-position:50% 20%" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 62%,rgba(10,20,60,.6) 85%)"></div>{T('w')}<div class="c">Dream life is on its way.</div>{U('#fff')}""")
# 131 · torn paper held up (Pray about it, 7,141)
P['CT131']=doc('Color test 131 · viral torn paper note',S+"""
.pin{background:#A9C6E8}
.sky{position:absolute;inset:0;background:linear-gradient(180deg,#8FB4E2 0%,#C9DCF2 60%,#EAF1F8 100%)}
.paper{position:absolute;left:170px;top:430px;width:660px;height:560px;background:#F3EFE6;transform:rotate(8deg);clip-path:polygon(2% 4%,20% 0,38% 3%,55% 0,74% 4%,96% 1%,100% 30%,97% 58%,100% 96%,78% 100%,58% 97%,36% 100%,16% 97%,0 100%,3% 66%,0 34%);box-shadow:0 20px 40px rgba(0,0,0,.2);padding:110px 70px;box-sizing:border-box;font-style:italic;font-weight:400;font-size:84px;line-height:1.15;letter-spacing:-.03em;color:#2A2A2A}
""",f"""<div class="sky"></div>{T()}<div class="paper">it all worked out.</div>{U('#2A2A2A')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
