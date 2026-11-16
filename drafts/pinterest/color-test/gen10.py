# Round 9 (CT88–CT97), Nov 16: copies of Megan's indie inspo spreads (design/magazine/inspo, layout library in design/magazine/MISE-EN-PAGE.md). Megan: "can you look at the indie magazine layouts and copy them ?"
import gen9, gen8
from gen4 import B
from gen import doc, LOGO
A='alt="Editorial photo (AI-generated)"'
def s(k): return f'/_blob/{B[k]}'
S="""img.f{position:absolute;object-fit:cover;display:block}
.full{inset:0;width:100%;height:100%}
.lab{position:absolute;font-weight:600;font-size:17px;letter-spacing:.24em;text-transform:uppercase}
.url{position:absolute;font-weight:700;font-size:26px}
.bars i{display:block;height:9px;margin:0 0 12px;border-radius:1px}
"""
def bars(n,c,ws=(100,96,100,92,100,98,88,100,94,72)): return '<div class="bars">'+''.join(f'<i style="background:{c};width:{ws[i%len(ws)]}%"></i>' for i in range(n))+'</div>'
P={}
# 88 · HAPPY VICTIMS overprint (editorial-25) → cash pile + rose multiply type
P['CT88']=doc('Color test 88 · inspo overprint (Happy Victims)',S+"""
.pin{background:#111}
.op{position:absolute;left:20px;right:10px;font-weight:900;color:#FF5FA2;mix-blend-mode:multiply;letter-spacing:-.06em;line-height:.8;text-transform:uppercase}
.box{position:absolute;right:52px;top:60px;width:300px;background:#EAF6FF;padding:18px 20px;font-weight:600;font-size:22px;line-height:1.3;color:#111}
.box b{display:block;font-size:15px;letter-spacing:.24em;text-transform:uppercase;margin-bottom:8px}
""",f"""<img class="f full" src="{s('cashpile')}" style="object-position:50% 40%;filter:contrast(1.08) saturate(.9)" {A}>
<div class="op" style="top:520px;font-size:280px">Wake</div><div class="op" style="top:760px;font-size:280px">up to</div><div class="op" style="top:1000px;font-size:250px">money</div>
<div class="box"><b>Vol. 01 · Money</b>I wake up to money</div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 89 · trust the process stars (editorial-12) → lilac page with star windows + photo with lilac stars
star="polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)"
P['CT89']=doc('Color test 89 · inspo star windows (trust the process)',S+f"""
.pin{{background:#D9B3FF}}
.top{{position:absolute;left:0;right:0;top:0;height:720px;overflow:hidden}}
.st{{position:absolute;clip-path:{star};background:url('PH') 50% 30%/1000px auto}}
.ph2{{position:absolute;left:0;right:0;top:720px;height:780px;overflow:hidden}}
.ph2 img{{width:100%;height:100%;object-fit:cover;object-position:50% 35%}}
.s2{{position:absolute;clip-path:{star};background:#D9B3FF}}
.t1{{position:absolute;left:60px;top:70px;font-weight:500;font-size:64px;letter-spacing:-.05em;line-height:.9;color:#3B1A66}}
.t2{{position:absolute;right:60px;top:430px;text-align:right;font-weight:500;font-size:64px;letter-spacing:-.05em;line-height:.9;color:#3B1A66}}
""".replace('PH',s('pinkgloss')),f"""<div class="top"><div class="st" style="left:150px;top:150px;width:300px;height:300px;background-position:-150px -150px"></div><div class="st" style="left:560px;top:260px;width:200px;height:200px;background-position:-560px -260px"></div></div>
<div class="t1">My face card</div><div class="t2">is absolutely<br>lethal</div>
<div class="ph2"><img src="{s('pinkgloss')}" {A}><div class="s2" style="left:760px;top:520px;width:170px;height:170px"></div><div class="s2" style="left:80px;top:80px;width:110px;height:110px"></div></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 90 · repeated name (editorial-30) → oxblood page, DREAM GIRL ×5 + portrait with ID list
rep=''.join('<div>Dream girl</div>' for _ in range(5))
P['CT90']=doc('Color test 90 · inspo repeated name (ID card)',S+"""
.pin{background:#8E1B24}
.rep{position:absolute;left:30px;top:90px;color:#FCE9E4;font-weight:800;font-size:138px;line-height:.86;letter-spacing:-.06em;text-transform:uppercase;white-space:nowrap}
img.f{left:440px;top:700px;width:510px;height:700px}
.id{position:absolute;left:52px;top:740px;width:350px;color:#FCE9E4;font-size:22px;line-height:1.5;font-weight:500}
.id div{border-bottom:1px solid rgba(252,233,228,.4);padding:6px 0}
.id b{font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:15px;margin-right:8px}
.logo{bottom:44px}
""",f"""<div class="rep">{rep}</div><img class="f" src="{s('curls')}" style="object-position:55% 25%" {A}>
<div class="id"><div><b>Name</b>Future you</div><div><b>Issue</b>2027</div><div><b>Hair</b>Curls, worn loud</div><div><b>Skin</b>Gloss</div><div><b>Line</b>I am my own dream girl</div></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 91 · outline type K-pop (editorial-15) → rose page outlined type + portrait with mint bubble
P['CT91']=doc('Color test 91 · inspo outline type + bubble note',S+"""
.pin{background:#E84C7A}
.ol{position:absolute;left:30px;right:20px;top:60px;font-weight:900;font-size:210px;line-height:.82;letter-spacing:-.05em;text-transform:uppercase;color:transparent;-webkit-text-stroke:3px #FFE3EC}
img.f{left:300px;top:640px;width:650px;height:800px}
.bub{position:absolute;left:52px;top:1010px;width:330px;background:#7DE3C7;color:#0B3B2E;border-radius:50%;padding:58px 40px;text-align:center;font-weight:700;font-size:34px;line-height:1.05;letter-spacing:-.02em;transform:rotate(-8deg)}
""",f"""<div class="ol">Glow up era</div><img class="f" src="{s('hair')}" style="object-position:50% 15%" {A}>
<div class="bub">I glowed up so hard now my ex is crying</div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 92 · NOT THE ICING ON THE CAKE (editorial-21) → vertical stacked words + columns
P['CT92']=doc('Color test 92 · inspo vertical stacks + columns',S+"""
.pin{background:#F6F3EE;color:#0D0D0D}
.v{position:absolute;top:60px;writing-mode:vertical-rl;transform:rotate(180deg);font-weight:900;font-size:150px;line-height:.86;letter-spacing:-.04em;text-transform:uppercase}
.col{position:absolute;top:120px}
img.f{left:380px;top:860px;width:270px;height:340px}
.cap{position:absolute;left:380px;top:1215px;font-size:22px;font-weight:600;width:270px}
""",f"""<div class="v" style="left:40px;height:1000px">I am</div><div class="v" style="left:190px;height:1000px">the</div>
<div class="col" style="left:380px;width:270px">{bars(40,'#C9C3B9')}</div>
<div class="v" style="left:680px;height:1000px">prize,</div><div class="v" style="left:830px;height:1000px;color:#3E63C9">always</div>
<img class="f" src="{s('blueclose')}" style="object-position:50% 30%" {A}><div class="cap">I am the prize, always</div>
<img class="logo" src="{LOGO}" alt="ISSUE11">""")
# 93 · BAD giant translucent type (editorial-22) → over the back/shoulder, never the face
P['CT93']=doc('Color test 93 · inspo giant translucent word · long hair',S+"""
.pin{background:#7A4A30}
.big{position:absolute;left:10px;right:10px;top:700px;text-align:center;font-weight:900;font-size:330px;line-height:.8;letter-spacing:-.07em;color:rgba(255,120,90,.62);mix-blend-mode:multiply;text-transform:uppercase}
.top{position:absolute;left:0;right:0;top:50px;text-align:center;color:#fff;font-weight:800;font-size:30px;letter-spacing:.06em;text-transform:uppercase}
.line{position:absolute;left:52px;right:52px;bottom:170px;color:#fff;font-weight:600;font-size:44px;letter-spacing:-.02em;text-shadow:0 2px 16px rgba(0,0,0,.4)}
""",f"""<img class="f full" src="{s('shoulder')}" style="object-position:20% 20%" {A}><div class="top">Hair issue</div><div class="big">Long<br>hair</div>
<div class="line">I love my long hair</div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 94 · CO2MO (editorial-27) → giant word bleeding at top + dense text column of money lines
lines=["I wake up to money","I'm making money in my sleep","My business is bringing sooooo much money","I make way more money than what I'm able to spend","I make $10,000 a month with ease","I wake up to Stripe notifications","A healthy mind, a fit body, and lots of money $$$"]
P['CT94']=doc('Color test 94 · inspo bleed word + text column',S+"""
.pin{background:#1D47B8;overflow:hidden}
.w{position:absolute;left:-20px;top:-40px;white-space:nowrap;color:#fff;font-weight:900;font-size:270px;letter-spacing:-.07em;line-height:1}
.col{position:absolute;right:0;top:280px;width:330px;padding:24px 46px 24px 24px;background:rgba(15,35,110,.82);color:#fff;font-size:21px;line-height:1.45;font-weight:500;text-align:right}
.col p{margin:0 0 14px}
.col b{display:block;font-size:14px;letter-spacing:.24em;text-transform:uppercase;margin-bottom:10px}
""",f"""<img class="f full" src="{s('flying')}" style="object-position:40% 30%" {A}><div class="w">MONEY</div>
<div class="col"><b>Contents · money</b>{''.join(f'<p>{x}</p>' for x in lines)}</div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 95 · gaijin (editorial-33) → one giant lowercase word + 4 photo specimens with captions
spec=[('pink','Pink liner','left:60px;top:200px'),('orange','Tangerine flick','left:720px;top:160px'),('blue','Blue liner','left:80px;top:1060px'),('red','Red liner','left:700px;top:1080px')]
sp=''.join(f'<div class="sp" style="{p}"><img src="{s(k)}" {A}><span>{c}</span></div>' for k,c,p in spec)
P['CT95']=doc('Color test 95 · inspo giant lowercase word + specimens',S+"""
.pin{background:#fff;color:#0D0D0D}
.gw{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:600;font-size:250px;letter-spacing:-.07em;line-height:1}
.sp{position:absolute;width:210px}
.sp img{display:block;width:210px;height:260px;object-fit:cover;object-position:50% 35%}
.sp span{display:block;margin-top:8px;font-size:17px;font-weight:600}
.line{position:absolute;left:0;right:0;top:820px;text-align:center;font-weight:500;font-size:40px;letter-spacing:-.03em}
.url{right:52px;bottom:60px}
""",f"""{sp}<div class="gw">lifemaxx</div><div class="line">2027 is the year I lifemaxx</div><img class="logo" src="{LOGO}" alt="ISSUE11" style="left:400px;bottom:auto;top:900px"><div class="url" style="color:#0D0D0D">issue11.app</div>""")
# 96 · WASHINGTON (editorial-20) → giant letters over dense columns + small photo
P['CT96']=doc('Color test 96 · inspo giant letters over columns',S+"""
.pin{background:#F2F0EA;color:#0D0D0D}
.cols{position:absolute;left:52px;right:52px;top:80px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px}
.L{position:absolute;font-weight:900;font-size:300px;letter-spacing:-.05em;line-height:1;mix-blend-mode:multiply}
img.f{left:52px;top:1080px;width:420px;height:330px}
.q{position:absolute;left:510px;right:52px;top:1090px;font-weight:600;font-size:48px;line-height:1;letter-spacing:-.04em}
.q span{color:#635BFF}
""",f"""<div class="cols">{bars(70,'#C7C3BA')}{bars(70,'#C7C3BA')}{bars(70,'#C7C3BA')}</div>
<div class="L" style="left:40px;top:60px">ST</div><div class="L" style="left:520px;top:300px">RI</div><div class="L" style="left:220px;top:560px;color:#635BFF">PE</div>
<img class="f" src="{s('sky')}" style="object-position:50% 20%" {A}><div class="q">I wake up to <span>Stripe</span> notifications</div>
<img class="logo" src="{LOGO}" alt="ISSUE11" style="left:auto;right:52px">""")
# 97 · "Love that if it were" (editorial-08) → condensed headline over photo + repeated vertical word + green bar
vw=''.join('<span>Business</span>' for _ in range(9))
P['CT97']=doc('Color test 97 · inspo headline over photo + vertical words',S+"""
.pin{background:#111}
.vl,.vr{position:absolute;top:0;bottom:0;writing-mode:vertical-rl;color:#F3E37A;font-weight:600;font-size:22px;letter-spacing:.2em;text-transform:uppercase;display:flex;justify-content:space-around;width:40px;background:rgba(0,0,0,.35)}
.vl{left:0;transform:rotate(180deg)}.vr{right:0}
.h{position:absolute;left:70px;right:70px;bottom:270px;color:#F3E37A;font-weight:800;font-size:96px;line-height:.92;letter-spacing:-.05em;text-transform:uppercase;transform:scaleX(.82);transform-origin:left;width:1050px;text-shadow:0 4px 24px rgba(0,0,0,.5)}
.bar{position:absolute;left:70px;right:70px;bottom:236px;height:12px;background:#3DDC84}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.7) 85%)}
.logo{left:70px}
""",f"""<img class="f full" src="{s('cashface')}" style="object-position:50% 25%" {A}><div class="sh"></div><div class="vl">{vw}</div><div class="vr">{vw}</div>
<div class="h">My business is bringing sooooo much money</div><div class="bar"></div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
