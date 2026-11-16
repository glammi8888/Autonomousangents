# Colour test round 3 (CT21–CT30), Nov 16: "more magazine-like, art studio-like, innovative". Run: python3 gen3.py
import gen
from gen import doc, LOGO
PH={'n17':'61c13ba5e0a9205473641aaca015e7c7','e27':'9034e8205048f219499561307a1c9748','e24':'48584939a34a6e613eb4e2f11f2ad13e','m26':'a9ca26df86b2661f5b04462f82740107','e20':'e0b2acd5fe4e7845cf15c0a2d79a2367','e22':'192e7090c0bebed08ef694877d2afefc','n18':'4104fae58009e60889f79ebf1c2348da','l23':'f9aebbe835f6f14787a79bcfba5c4f11','e36':'2d5be03e75abb367c4c478e5bf591d8b','e21':'7c7c9f7639583c427c5ebf34599a953c','e35':'9ceda159e77c89d8a20b1bd3377080cd'}
def src(k): return f'/_blob/{PH[k]}'
A='alt="Editorial photo (AI-generated)"'
P={}
# 21 MAGAZINE COVER · n17 · "I am my own dream girl" + real ISSUE11 article cover lines
P['CT21']=doc('Color test 21 · magazine cover',"""
.pin{background:#F7C6D9}
.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 18%}
.dg{position:absolute;left:36px;right:36px;top:40px;color:#FF2E7E;font-weight:900;font-size:150px;white-space:nowrap;line-height:.78;letter-spacing:-.07em;text-transform:uppercase;mix-blend-mode:multiply}
.date{position:absolute;right:44px;top:300px;writing-mode:vertical-rl;color:#fff;font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase}
.story{position:absolute;left:52px;bottom:300px;color:#fff;font-weight:900;font-size:76px;line-height:.92;letter-spacing:-.045em;max-width:620px;text-shadow:0 4px 24px rgba(0,0,0,.35)}
.story i{display:block;font-weight:500;font-size:30px;letter-spacing:.12em;text-transform:uppercase;font-style:normal;color:#FFD1E3;margin-bottom:12px;text-shadow:none}
.lines{position:absolute;right:48px;bottom:150px;text-align:right;color:#fff;font-weight:800;font-size:30px;line-height:1.25;text-shadow:0 2px 14px rgba(0,0,0,.45)}
.lines b{color:#FFD1E3;font-weight:900}
.bar{position:absolute;right:48px;bottom:48px;width:150px;height:64px;background:repeating-linear-gradient(90deg,#fff 0 3px,transparent 3px 6px,#fff 6px 7px,transparent 7px 11px);opacity:.9}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(60,0,30,.55) 100%)}
""",f"""<img class="ph" src="{src('n17')}" {A}><div class="shade"></div>
<div class="dg">Dream girl</div>
<div class="date">The 2027 issue</div>
<div class="story"><i>Cover story</i>I am my own dream girl</div>
<div class="lines"><b>60</b> self love affirmations<br><b>9</b> ways to stop overthinking<br><b>120</b> words of the year</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="bar"></div>""")
# 22 EDITORIAL SPREAD · e27 calm woman · "I have all the time in the world"
bars=''.join(f'<i style="width:{w}%"></i>' for w in [100,96,100,92,100,98,88,100,94,60])
P['CT22']=doc('Color test 22 · editorial spread',"""
.pin{background:#EEF3E2}
.ph{position:absolute;left:0;top:0;width:520px;height:1500px;object-fit:cover;object-position:46% 30%}
.gut{position:absolute;left:520px;top:0;width:30px;height:1500px;background:linear-gradient(90deg,rgba(0,0,0,.18),rgba(0,0,0,0))}
.r{position:absolute;left:580px;right:52px;top:110px;color:#2F4A2A}
.kick{font-weight:800;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:#6E8F4E}
.pq{margin:26px 0 30px;font-weight:900;font-size:84px;line-height:.9;letter-spacing:-.05em}
.pq::before{content:'“';display:block;font-size:160px;line-height:.6;color:#9CC27A}
.body i{display:block;height:12px;background:#C9D8B4;margin:0 0 16px;border-radius:2px}
.cap{margin-top:30px;font-weight:600;font-size:22px;color:#6E8F4E;font-style:italic}
.folio{position:absolute;right:52px;bottom:56px;font-weight:700;font-size:22px;letter-spacing:.2em;color:#6E8F4E}
.logo{left:580px}
""",f"""<img class="ph" src="{src('e27')}" {A}><div class="gut"></div>
<div class="r"><div class="kick">Slow living · The calm issue</div><div class="pq">I have all the time in the world</div><div class="body">{bars}{bars}</div><div class="cap">Read slowly. Save for Sunday.</div></div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">PAGE 27</div>""")
# 23 CONTACT SHEET · e24 beauty · grease pencil · "My face card is absolutely lethal"
pos=['50% 10%','40% 22%','60% 15%','50% 28%','45% 12%','55% 20%']
fr=''.join(f'<div class="f{" pick" if i==4 else ""}"><img src="{src("e24")}" style="object-position:{p};transform:scale({1.0+0.12*(i%3)})" {A}><span>{i+11}A</span></div>' for i,p in enumerate(pos))
P['CT23']=doc('Color test 23 · contact sheet',"""
.pin{background:#F4F1EA}
.sheet{position:absolute;left:52px;right:52px;top:70px;background:#1C1A17;padding:26px 22px;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.f{position:relative;height:300px;overflow:hidden;border:6px solid #1C1A17}
.f img{width:100%;height:100%;object-fit:cover}
.f span{position:absolute;left:8px;bottom:6px;color:#F5A623;font-weight:800;font-size:20px;letter-spacing:.1em}
.pick::after{content:'';position:absolute;inset:-4px;border:7px solid #FF2D3F;border-radius:48% 52% 45% 55%;transform:rotate(-4deg)}
.mark{position:absolute;left:52px;right:52px;top:1120px;color:#FF2D3F;font-weight:900;font-style:italic;font-size:84px;line-height:.92;letter-spacing:-.04em;transform:rotate(-2deg)}
.arrow{position:absolute;left:640px;top:1060px;color:#FF2D3F;font-size:70px;font-weight:900;transform:rotate(-40deg)}
""",f"""<div class="sheet">{fr}</div><div class="arrow">↑</div>
<div class="mark">My face card is absolutely lethal</div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
# 24 PAINT SWATCH CARD · "Dream life is on its way" · e20 chip
P['CT24']=doc('Color test 24 · paint swatch card',"""
.pin{background:#FBF7F2}
.card{position:absolute;left:150px;right:150px;top:90px;height:1230px;background:#fff;box-shadow:0 30px 70px rgba(80,40,40,.18);padding:22px;box-sizing:border-box}
.chip{height:330px;margin-bottom:16px;position:relative}
.chip span{position:absolute;left:22px;bottom:16px;font-weight:700;font-size:20px;letter-spacing:.14em;color:rgba(0,0,0,.55)}
.c1{background:#FFD6E5}.c2{background:#FF8DB8}.c3{height:330px;overflow:hidden}
.c3 img{width:100%;height:100%;object-fit:cover;object-position:50% 45%}
.name{font-weight:900;font-size:74px;line-height:.95;letter-spacing:-.04em;color:#B0124F;margin-top:18px}
.code{font-weight:700;font-size:20px;letter-spacing:.2em;color:#B0124F;margin-top:10px}
.punch{position:absolute;left:50%;top:44px;width:30px;height:30px;margin-left:-15px;border-radius:50%;background:#FBF7F2;box-shadow:inset 0 2px 4px rgba(0,0,0,.2)}
""",f"""<div class="card"><div class="chip c1"><span>SOFT START</span></div><div class="chip c2"><span>ON ITS WAY</span></div><div class="chip c3"><img src="{src('e20')}" {A}></div>
<div class="name">Dream life is on its way</div><div class="code">COLOUR OF THE YEAR · 2027</div></div><div class="punch"></div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
# 25 RISO PRINT · m26 duotone · "I make way more money than what I'm able to spend"
P['CT25']=doc('Color test 25 · riso duotone print',"""
.pin{background:#FFF4DC}
.duo{position:absolute;left:60px;right:60px;top:60px;height:860px;overflow:hidden;background:#FF4F9A}
.duo img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;filter:grayscale(1) contrast(1.25);mix-blend-mode:multiply}
.duo::after{content:'';position:absolute;inset:0;background:#00A6A6;mix-blend-mode:screen;opacity:.45}
.grain{position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.18) 1px,transparent 1.2px);background-size:6px 6px;mix-blend-mode:multiply}
.t1,.t2{position:absolute;left:56px;right:56px;top:960px;font-weight:900;font-size:92px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase}
.t1{color:#00A6A6}.t2{color:#FF4F9A;mix-blend-mode:multiply;transform:translate(6px,5px)}
.stamp{position:absolute;right:60px;bottom:60px;border:3px solid #FF4F9A;color:#FF4F9A;font-weight:800;font-size:22px;letter-spacing:.18em;padding:10px 14px;transform:rotate(-6deg)}
""",f"""<div class="duo"><img src="{src('m26')}" {A}><div class="grain"></div></div>
<div class="t1">I make way more money than what I'm able to spend</div><div class="t2">I make way more money than what I'm able to spend</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="stamp">RISO · 2 COLOUR</div>""")
# 26 TAPED COLLAGE · vision board article steps · e20 e22 n18
P['CT26']=doc('Color test 26 · taped collage',"""
.pin{background:#F3D9B1}
.paper{position:absolute;inset:0;background-image:repeating-linear-gradient(0deg,rgba(120,70,20,.05) 0 2px,transparent 2px 6px)}
h1{position:absolute;left:48px;right:48px;top:60px;margin:0;color:#7A2E12;font-weight:900;font-size:108px;line-height:.86;letter-spacing:-.05em;text-transform:uppercase}
.p{position:absolute;background:#fff;padding:14px 14px 50px;box-shadow:0 14px 30px rgba(80,40,10,.25)}
.p img{display:block;width:100%;height:100%;object-fit:cover}
.p b{position:absolute;left:16px;bottom:10px;font-style:italic;font-weight:600;font-size:26px;color:#7A2E12}
.tape{position:absolute;width:130px;height:38px;background:rgba(255,236,170,.75);transform:rotate(-8deg)}
.steps{position:absolute;left:52px;right:52px;top:1110px;color:#7A2E12;font-weight:800;font-size:36px;line-height:1.5;display:flex;flex-wrap:wrap;gap:10px 12px}
.steps span{background:#FFE9A8;padding:4px 14px}
""",f"""<div class="paper"></div><h1>How to make a vision board</h1>
<div class="p" style="left:60px;top:330px;width:400px;height:330px;transform:rotate(-4deg)"><img src="{src('e20')}" {A}><b>the closet</b></div>
<div class="p" style="left:510px;top:300px;width:400px;height:260px;transform:rotate(3deg)"><img src="{src('e22')}" style="object-position:50% 60%" {A}><b>the home</b></div>
<div class="p" style="left:300px;top:700px;width:380px;height:300px;transform:rotate(-2deg)"><img src="{src('n18')}" style="object-position:50% 30%" {A}><b>the weekend</b></div>
<div class="tape" style="left:200px;top:312px"></div><div class="tape" style="left:650px;top:280px;transform:rotate(6deg)"></div><div class="tape" style="left:430px;top:682px"></div>
<div class="steps"><span>1 Pick your base</span> <span>2 Collect more than you need</span> <span>3 Edit down</span> <span>4 Add the process</span> <span>5 One step under each image</span></div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
# 27 GALLERY WALL LABEL · l23 · "The love of my life is coming to me"
P['CT27']=doc('Color test 27 · gallery wall + label',"""
.pin{background:#7A1631}
.wall{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(255,255,255,.18),rgba(0,0,0,0) 60%)}
.frame{position:absolute;left:150px;right:150px;top:110px;height:820px;background:#E9D3A3;padding:22px;box-shadow:0 30px 60px rgba(0,0,0,.45)}
.mat{width:100%;height:100%;background:#FFF8EC;padding:34px;box-sizing:border-box}
.mat img{width:100%;height:100%;object-fit:cover;object-position:50% 30%}
.label{position:absolute;left:290px;right:290px;top:1010px;background:#FFF8EC;padding:26px 28px;box-shadow:0 8px 20px rgba(0,0,0,.3)}
.label b{display:block;font-weight:900;font-size:42px;line-height:1;letter-spacing:-.03em;color:#2A0A12}
.label span{display:block;margin-top:12px;font-style:italic;font-weight:500;font-size:22px;color:#7A1631}
.label small{display:block;margin-top:8px;font-weight:700;font-size:16px;letter-spacing:.18em;color:#7A1631}
""",f"""<div class="wall"></div><div class="frame"><div class="mat"><img src="{src('l23')}" {A}></div></div>
<div class="label"><b>The love of my life is coming to me</b><span>Manifestation, 2027</span><small>ISSUE11 · ROOM 11</small></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 28 TYPE SPECIMEN · "I'm the art director of my life..."
P['CT28']=doc('Color test 28 · type specimen poster',"""
.pin{background:#FF5A36}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.18) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.18) 1px,transparent 1px);background-size:100px 100px}
.top{position:absolute;left:52px;right:52px;top:60px;display:flex;justify-content:space-between;color:#FFE7DE;font-weight:700;font-size:20px;letter-spacing:.2em;text-transform:uppercase}
.Aa{position:absolute;right:30px;top:90px;color:#FFE7DE;font-weight:900;font-size:300px;letter-spacing:-.08em;line-height:1;opacity:.95}
.q{position:absolute;left:52px;right:52px;top:500px;color:#2A0D05;font-weight:900;font-size:112px;line-height:.9;letter-spacing:-.05em}
.q span{display:block;color:#FFE7DE}
.rule{position:absolute;left:52px;right:52px;top:448px;border-top:2px dashed #FFE7DE}
.meas{position:absolute;left:52px;top:410px;color:#FFE7DE;font-weight:700;font-size:18px;letter-spacing:.14em}
.crop{position:absolute;width:40px;height:40px;border-color:#2A0D05;border-style:solid}
""",f"""<div class="grid"></div><div class="top"><span>Specimen 11</span><span>Black 900 · 100 pt</span></div><div class="Aa">Aa</div>
<div class="meas">↔ BASELINE / CAP HEIGHT</div><div class="rule"></div>
<div class="q">I'm the art director of my life. <span>I create it page by page.</span> I make my own opportunities.</div>
<div class="crop" style="left:20px;top:20px;border-width:3px 0 0 3px"></div><div class="crop" style="right:20px;top:20px;border-width:3px 3px 0 0"></div>
<div class="crop" style="right:20px;bottom:20px;border-width:0 3px 3px 0"></div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
# 29 CONTENTS PAGE · glow up checklist article · e36
items=['7+ hours of sleep, most nights','Water before coffee','Sunscreen every morning',"One walk or workout you'd repeat",'Three style words + a closet edit','Three accounts muted, three followed','One promise to yourself, kept daily','One weekly line of proof']
toc=''.join(f'<li><b>{i+1:02d}</b><span>{x}</span></li>' for i,x in enumerate(items))
P['CT29']=doc('Color test 29 · contents page',"""
.pin{background:#E9FF6B}
.ph{position:absolute;right:52px;top:60px;width:330px;height:440px;object-fit:cover;object-position:50% 15%}
.k{position:absolute;left:52px;top:70px;font-weight:800;font-size:22px;letter-spacing:.24em;color:#3B2A6E}
h1{position:absolute;left:48px;top:120px;margin:0;color:#3B2A6E;font-weight:900;font-size:150px;line-height:.82;letter-spacing:-.06em;text-transform:uppercase}
.sub{position:absolute;left:52px;top:400px;color:#3B2A6E;font-weight:700;font-size:34px;letter-spacing:-.02em;max-width:520px}
ol{position:absolute;left:52px;right:52px;top:560px;margin:0;padding:0;list-style:none}
li{display:flex;align-items:baseline;gap:22px;padding:15px 0;border-bottom:2px dotted #3B2A6E;color:#3B2A6E}
li b{font-weight:900;font-size:58px;letter-spacing:-.04em;width:90px}
li span{font-weight:800;font-size:34px;letter-spacing:-.02em}
.cta{position:absolute;right:52px;bottom:58px;color:#3B2A6E;font-weight:800;font-size:28px}
""",f"""<img class="ph" src="{src('e36')}" {A}><div class="k">CONTENTS</div><h1>Glow<br>up</h1>
<div class="sub">The checklist, in the order that works</div><ol>{toc}</ol>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="cta">+ the 30-day plan →</div>""")
# 30 POLAROID BOARD · "The right people, places, and moments find me" · n18 e21 e35
P['CT30']=doc('Color test 30 · polaroid board',"""
.pin{background:#BFE3FF}
.q{position:absolute;left:48px;right:48px;top:70px;color:#0B3D91;font-weight:900;font-size:104px;line-height:.88;letter-spacing:-.05em}
.q i{font-weight:500;color:#2F7BFF}
.po{position:absolute;background:#fff;padding:18px 18px 74px;box-shadow:0 18px 36px rgba(10,40,90,.25)}
.po img{display:block;width:100%;height:100%;object-fit:cover}
.po b{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-style:italic;font-weight:700;font-size:36px;color:#0B3D91}
.pinh{position:absolute;width:26px;height:26px;border-radius:50%;background:#FF5A8A;box-shadow:0 3px 6px rgba(0,0,0,.3)}
""",f"""<div class="q">The right <i>people, places,</i> and moments find me</div>
<div class="po" style="left:60px;top:450px;width:380px;height:380px;transform:rotate(-5deg)"><img src="{src('n18')}" style="object-position:50% 30%" {A}><b>people</b></div>
<div class="po" style="left:540px;top:480px;width:380px;height:380px;transform:rotate(4deg)"><img src="{src('e21')}" {A}><b>places</b></div>
<div class="po" style="left:300px;top:1000px;width:400px;height:280px;transform:rotate(-1deg)"><img src="{src('e35')}" style="object-position:50% 25%" {A}><b>moments</b></div>
<div class="pinh" style="left:240px;top:452px"></div><div class="pinh" style="left:720px;top:478px"></div><div class="pinh" style="left:490px;top:995px"></div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
