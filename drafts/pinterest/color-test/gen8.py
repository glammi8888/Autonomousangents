# Round 7 (CT68–CT77), Nov 16: more indie-magazine pins (Megan: "Keep up Indie magazine style pins please I want to see more options !")
import gen4
gen4.B.update({'shoulder':'68963da8e26c9286d2fba8b5c3edb3bb','sleepcash':'62bbca5a42743009b5377360d4ed86d7','earring':'860f329959c42e11a32a5dcb35db8203','wethair':'a5d556e3904ad3660587c191ff3898c6'})
from gen4 import B, IND, run
from gen import doc, LOGO
A='alt="Editorial photo (AI-generated)"'
def s(k): return f'/_blob/{B[k]}'
P={}
# 68 thin masthead band + full bleed + small italic
P['CT68']=doc('Color test 68 · indie band + full bleed',IND+"""
.pin{background:#111}
img.ph{inset:0;width:100%;height:100%}
.band{position:absolute;left:0;right:0;top:0;height:96px;background:#C9B6FF;color:#2A1650;display:flex;justify-content:space-between;align-items:center;padding:0 40px;font-weight:700;font-size:20px;letter-spacing:.28em;text-transform:uppercase}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(20,10,35,.8) 92%)}
.it{position:absolute;left:52px;right:300px;bottom:190px;color:#fff;font-style:italic;font-weight:400;font-size:58px;line-height:1.05;letter-spacing:-.03em}
""",f"""<img class="ph" src="{s('wethair')}" style="object-position:50% 25%" {A}><div class="sh"></div><div class="band"><span>Vol. 01 · Winter 2027</span><span>The worth issue</span></div>
<div class="it">I am worthy of love, respect, and everything I desire</div><img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="folio" style="color:#fff">P. 68</div>""")
# 69 spread with drop cap column + photo page
P['CT69']=doc('Color test 69 · indie spread · drop cap',IND+"""
.pin{background:#F3E6DA;color:#3A2418}
img.ph{right:0;top:0;width:470px;height:1500px}
.gut{position:absolute;right:470px;top:0;width:24px;height:1500px;background:linear-gradient(270deg,rgba(0,0,0,.16),rgba(0,0,0,0))}
.col{position:absolute;left:52px;width:430px;top:150px}
.k{font-weight:700;font-size:16px;letter-spacing:.3em;text-transform:uppercase;color:#B5651D}
.q{margin-top:30px;font-weight:300;font-size:150px;line-height:.86;letter-spacing:-.06em}
.q b{color:#B5651D}
.q b{font-weight:800}
.cap{margin-top:40px}
""",f"""<img class="ph" src="{s('shoulder')}" style="object-position:92% 20%" {A}><div class="gut"></div>{run('Vol. 01','','#3A2418')}
<div class="col"><div class="k">Body · self love</div><div class="q">I love<br>my <b>hot<br>bod</b></div><div class="cap"><b>Fig. 1</b>Glass skin, sun on the shoulder.</div></div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio" style="right:520px">P. 69</div>""")
# 70 index page of affirmations
lines=["I wake up to money","I'm making money in my sleep","My business is bringing sooooo much money","I make way more money than what I'm able to spend","I make $10,000 a month with ease","I wake up to Stripe notifications"]
idx=''.join(f'<li><span>{x}</span><b>{12+i*7}</b></li>' for i,x in enumerate(lines))
P['CT70']=doc('Color test 70 · indie index page · money',IND+"""
.pin{background:#E7EDDF;color:#1F3A26}
img.ph{left:52px;right:52px;top:110px;width:896px;height:560px}
h1{position:absolute;left:48px;top:700px;margin:0;font-weight:300;font-size:110px;letter-spacing:-.06em;line-height:.9}
h1 b{font-weight:800}
ol{position:absolute;left:52px;right:52px;top:830px;margin:0;padding:0;list-style:none}
li{display:flex;justify-content:space-between;align-items:baseline;padding:13px 0;border-bottom:1px dotted #1F3A26;font-weight:500;font-size:29px;letter-spacing:-.01em}
li b{font-weight:800}
""",f"""{run('Vol. 01 — Winter 2027','Index','#1F3A26')}<img class="ph" src="{s('sleepcash')}" style="object-position:40% 30%" {A}>
<h1><b>Money</b>, an index</h1><ol>{idx}</ol><img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 70</div>""")
# 71 giant initial I + tall photo
P['CT71']=doc('Color test 71 · indie giant initial',IND+"""
.pin{background:#FFF4DC;color:#0E5C2F}
img.ph{right:52px;top:110px;width:520px;height:1220px}
.I{position:absolute;left:40px;top:120px;font-weight:900;font-size:620px;line-height:1;letter-spacing:-.05em;color:#0E5C2F}
.q{position:absolute;left:52px;width:360px;top:900px;font-weight:300;font-size:92px;line-height:.92;letter-spacing:-.05em}
.q b{font-weight:800}
""",f"""<img class="ph" src="{s('cashpile')}" style="object-position:50% 40%" {A}><div class="I">$</div>
<div class="q"><b>I</b> wake up to <b>money</b></div><img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 71</div>""")
# 72 two looks with credits
P['CT72']=doc('Color test 72 · indie looks + credits',IND+"""
.pin{background:#FBEFF2;color:#7A0F3A}
.lk{position:absolute;top:120px;width:430px}
.lk img{display:block;width:430px;height:640px;object-fit:cover}
.lk .cap{margin-top:14px}
.q{position:absolute;left:52px;right:52px;top:1000px;font-weight:600;font-size:96px;line-height:.92;letter-spacing:-.045em}
.q i{font-weight:300}
""",f"""{run('Vol. 01 — Winter 2027','Looks','#7A0F3A')}
<div class="lk" style="left:52px"><img src="{s('pink')}" style="object-position:50% 35%" {A}><div class="cap"><b>Look 01</b>Pink liner, wet freckles</div></div>
<div class="lk" style="right:52px"><img src="{s('orange')}" style="object-position:40% 30%" {A}><div class="cap"><b>Look 02</b>Tangerine flick, glass skin</div></div>
<div class="q">My face card is <i>absolutely</i> lethal</div><img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 72</div>""")
# 73 full bleed inside thin frame
P['CT73']=doc('Color test 73 · indie framed bleed',IND+"""
.pin{background:#DCE6F2}
img.ph{left:40px;top:40px;width:920px;height:1420px}
.fr{position:absolute;left:70px;top:70px;right:70px;bottom:70px;border:2px solid #fff}
.t{position:absolute;left:100px;top:100px;color:#fff;font-weight:700;font-size:17px;letter-spacing:.3em;text-transform:uppercase}
.sh{position:absolute;left:40px;top:40px;width:920px;height:1420px;background:linear-gradient(180deg,rgba(0,0,0,0) 64%,rgba(15,30,70,.8) 90%)}
.q{position:absolute;left:100px;right:100px;bottom:200px;color:#fff;font-weight:300;font-size:92px;line-height:.92;letter-spacing:-.05em}
.q b{font-weight:800}
.logo{left:100px;bottom:100px}
""",f"""<img class="ph" src="{s('blue')}" style="object-position:50% 20%" {A}><div class="sh"></div><div class="fr"></div><div class="t">Vol. 01 · The calm issue</div>
<div class="q">My nervous system is <b>calm</b></div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 74 square photo + two-column caption
P['CT74']=doc('Color test 74 · indie square + columns',IND+"""
.pin{background:#F1EBFF;color:#24124A}
img.ph{left:150px;top:150px;width:700px;height:760px}
.q{position:absolute;left:52px;right:52px;top:960px;text-align:center;font-style:italic;font-weight:400;font-size:70px;letter-spacing:-.03em}
.cols{position:absolute;left:150px;right:150px;top:1090px;display:grid;grid-template-columns:1fr 1fr;gap:40px;border-top:1px solid #24124A;padding-top:16px}
""",f"""{run('Vol. 01 — Winter 2027','Portrait','#24124A')}<img class="ph" src="{s('curls')}" style="object-position:55% 25%" {A}>
<div class="q">I am my own dream girl</div><div class="cols"><div class="cap"><b>Hair</b>Long curls, worn loud.</div><div class="cap"><b>Skin</b>Gloss, freckles, nothing to hide.</div></div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 74</div>""")
# 75 letter page + polaroid corner
P['CT75']=doc('Color test 75 · indie letter page',IND+"""
.pin{background:#FCF3E8;color:#5A2410}
.po{position:absolute;right:70px;top:120px;width:330px;background:#fff;padding:14px 14px 60px;transform:rotate(5deg);box-shadow:0 14px 30px rgba(90,36,16,.25)}
.po img{display:block;width:100%;height:400px;object-fit:cover;object-position:45% 30%}
.k{position:absolute;left:52px;top:160px;font-weight:700;font-size:16px;letter-spacing:.3em;text-transform:uppercase;color:#E2531F}
.dear{position:absolute;left:52px;top:220px;font-style:italic;font-weight:300;font-size:50px}
.q{position:absolute;left:52px;right:52px;top:640px;font-weight:700;font-size:104px;line-height:.92;letter-spacing:-.05em;color:#E2531F}
.q i{font-weight:300;color:#5A2410}
.sig{position:absolute;left:52px;top:1160px;font-style:italic;font-weight:400;font-size:40px}
""",f"""{run('Vol. 01 — Winter 2027','Letters','#5A2410')}<div class="po"><img src="{s('orange')}" {A}></div><div class="k">A letter to you</div><div class="dear">Dear you,</div>
<div class="q">Get up girl, <i>you got people</i> to prove wrong</div><div class="sig">x, ISSUE11</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 75</div>""")
# 76 gatefold three panels
P['CT76']=doc('Color test 76 · indie gatefold',IND+"""
.pin{background:#2A2622}
img.ph{inset:0;width:100%;height:100%}
.fold{position:absolute;top:0;bottom:0;width:2px;background:rgba(255,255,255,.35);box-shadow:0 0 18px rgba(0,0,0,.5)}
.pn{position:absolute;top:56px;color:#fff;font-weight:700;font-size:16px;letter-spacing:.3em}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 58%,rgba(30,25,20,.85) 85%)}
.q{position:absolute;left:52px;right:52px;top:1120px;color:#fff;font-weight:300;font-size:84px;line-height:.95;letter-spacing:-.05em;text-align:center}
.q b{font-weight:800}
""",f"""<img class="ph" src="{s('hair')}" style="object-position:50% 15%" {A}><div class="sh"></div><div class="fold" style="left:333px"></div><div class="fold" style="left:666px"></div>
<div class="pn" style="left:40px">I</div><div class="pn" style="left:373px">II</div><div class="pn" style="left:706px">III</div>
<div class="q">I'm the <b>luckiest girl</b> on the planet</div><img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="folio" style="color:#fff">P. 76</div>""")
# 77 broadsheet
P['CT77']=doc('Color test 77 · indie broadsheet',IND+"""
.pin{background:#F2EEE6;color:#1A1A1A}
.mast{position:absolute;left:52px;right:52px;top:60px;border-top:3px solid #1A1A1A;border-bottom:1px solid #1A1A1A;padding:12px 0;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:.2em;text-transform:uppercase}
h1{position:absolute;left:48px;right:48px;top:140px;margin:0;font-weight:900;font-size:104px;line-height:.88;letter-spacing:-.05em;text-transform:uppercase;color:#8A6A1E}
img.ph{left:52px;top:520px;width:560px;height:780px}
.cols{position:absolute;left:640px;right:52px;top:520px}
.cols i{display:block;height:10px;background:#CFC6B6;margin:0 0 14px}
.cap{position:absolute;left:52px;top:1314px}
""",f"""<div class="mast"><span>Monday edition</span><span>Business</span></div><h1>My business is bringing sooooo much money</h1>
<img class="ph" src="{s('earring')}" style="object-position:55% 25%" {A}><div class="cols">{''.join(f'<i style="width:{w}%"></i>' for w in [100,92,100,96,88,100,94,100,70,100,96,100,90,100,64,100,98,100,86,58])}</div>
<div class="cap"><b>Fig. 77</b>Diamonds, gloss, and a very good quarter.</div><img class="logo" src="{LOGO}" alt="ISSUE11" style="bottom:48px"><div class="folio">P. 77</div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
