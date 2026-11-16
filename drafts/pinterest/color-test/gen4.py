# Round 4 (CT31–CT40), Nov 16: indie-magazine pins with Megan's Google Drive photos ("ISSUE11 Images"). Run: python3 gen4.py
import gen
from gen import doc, LOGO
B={'pink':'1c0f150e49d3b005dbf1434c00bbd101','blue':'aad3cb4d8a25e93713be097d5e182795','red':'fe93ea3b39f07ff739b7ef958b5ba623','curls':'2f1673a637c73371ea14b83819994320','hair':'7feef729a80262f2d7e85c6834638c97','cashpile':'b45e07b7551e4b017a09232ac4418b81','bobcash':'bb6331704485e735630ba2d0f3bcaec4','cashface':'09ac110d6a4b99f7489e0491c3418e33','sky':'7aaf709ad270b109bdee2b20f48353e5','orange':'bd88377bd9e692cef7a60b0b39e079f7'}
def im(k,cls='ph',pos='50% 30%'): return f'<img class="{cls}" src="/_blob/{B[k]}" style="object-position:{pos}" alt="Editorial photo (AI-generated)">'
IND="""
.run{position:absolute;left:52px;right:52px;top:44px;display:flex;justify-content:space-between;font-weight:500;font-size:17px;letter-spacing:.26em;text-transform:uppercase}
.folio{position:absolute;right:52px;bottom:60px;font-weight:500;font-size:18px;letter-spacing:.2em}
.cap{font-weight:400;font-size:19px;letter-spacing:.02em;line-height:1.4}
.cap b{font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:15px;margin-right:10px}
img.ph{position:absolute;object-fit:cover;display:block}
"""
def run(l,r,c): return f'<div class="run" style="color:{c}"><span>{l}</span><span>{r}</span></div>'
P={}
# 31 · blush cover, pink close-up · face card
P['CT31']=doc('Color test 31 · indie cover · blush',IND+"""
.pin{background:#F6E6E8;color:#9E1046}
img.ph{left:220px;top:110px;width:728px;height:880px}
.no{position:absolute;left:46px;top:96px;font-weight:200;font-size:150px;letter-spacing:-.06em;line-height:1}
.vt{position:absolute;left:66px;top:330px;writing-mode:vertical-rl;transform:rotate(180deg);font-weight:600;font-size:20px;letter-spacing:.34em;text-transform:uppercase}
.q{position:absolute;left:52px;right:52px;top:1080px;font-weight:600;font-size:94px;line-height:.92;letter-spacing:-.045em}
.q i{font-weight:300}
.cap{position:absolute;left:220px;top:1000px}
""",f"""{run('Vol. 01 — Winter 2027','The face issue','#9E1046')}{im('pink',pos='50% 35%')}<div class="no">31</div><div class="vt">Beauty · pink liner, wet skin</div>
<div class="q">My face card is <i>absolutely</i> lethal</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 31</div>""")
# 32 · powder blue, blue liner · I am the prize, always
P['CT32']=doc('Color test 32 · indie feature · powder blue',IND+"""
.pin{background:#DCE6F2;color:#1E3A6E}
img.ph{left:52px;top:110px;width:560px;height:760px}
.side{position:absolute;left:650px;right:52px;top:120px}
.side .cap{color:#1E3A6E}
.side hr{border:0;border-top:1px solid #1E3A6E;margin:18px 0}
.q{position:absolute;left:46px;right:52px;top:930px;font-weight:300;font-size:150px;line-height:.86;letter-spacing:-.055em}
.q b{font-weight:800;font-style:italic}
""",f"""{run('Vol. 01 — Winter 2027','Self worth','#1E3A6E')}{im('blue',pos='50% 30%')}
<div class="side"><div class="cap"><b>Fig. 2</b>Blue liner, wet hair, no apology.</div><hr><div class="cap"><b>Read</b>Self love affirmations, p. 60</div><hr><div class="cap"><b>Save</b>for the days you forget.</div></div>
<div class="q">I am <b>the prize</b>, always</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 32</div>""")
# 33 · red paper, red liner · glowed up
P['CT33']=doc('Color test 33 · indie red spread',IND+"""
.pin{background:#C8322B;color:#FFF1E4}
img.ph{left:150px;top:110px;width:700px;height:860px;box-shadow:0 0 0 14px #FFF1E4}
.q{position:absolute;left:52px;right:52px;top:1040px;font-weight:700;font-size:78px;line-height:.98;letter-spacing:-.04em}
.q i{font-weight:300}
""",f"""{run('Vol. 01 — Winter 2027','Glow up','#FFF1E4')}{im('red',pos='50% 30%')}
<div class="q">I glowed up so hard <i>now my enemies are crying</i></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="folio" style="color:#FFF1E4">P. 33</div>""")
# 34 · cream note to self, curls · worth line
P['CT34']=doc('Color test 34 · indie note to self',IND+"""
.pin{background:#EFE7DA;color:#3A2418}
img.ph{right:52px;top:110px;width:420px;height:1180px}
.lab{position:absolute;left:52px;top:130px;font-weight:700;font-size:18px;letter-spacing:.3em;text-transform:uppercase;color:#A0522D}
.q{position:absolute;left:52px;width:450px;top:200px;font-weight:600;font-size:76px;line-height:.98;letter-spacing:-.04em}
.q span{display:block;margin-top:40px;font-weight:300;font-style:italic;font-size:76px;color:#A0522D}
.rule{position:absolute;left:52px;width:450px;top:1010px;border-top:1px solid #3A2418}
.cap{position:absolute;left:52px;width:450px;top:1030px;color:#3A2418}
""",f"""{run('Vol. 01 — Winter 2027','Note to self','#3A2418')}{im('curls',pos='55% 30%')}
<div class="lab">A note to self</div><div class="q">I am no longer proving my worth to someone. <span>You either value me or you're OUT!</span></div>
<div class="rule"></div><div class="cap"><b>Fig. 4</b>Curls, gloss, a look that says enough.</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 34</div>""")
# 35 · glow up checklist article, long hair
items=['7+ hours of sleep, most nights','Water before coffee','Sunscreen every morning',"One walk or workout you'd repeat",'Three style words + a closet edit','Three accounts muted, three followed','One promise to yourself, kept daily','One weekly line of proof']
lis=''.join(f'<li><b>{i+1:02d}</b>{x}</li>' for i,x in enumerate(items))
P['CT35']=doc('Color test 35 · indie feature opener · glow up',IND+"""
.pin{background:#F4EFE6;color:#2B2118}
img.ph{left:0;top:0;width:1000px;height:760px}
.k{position:absolute;left:52px;top:800px;font-weight:700;font-size:16px;letter-spacing:.3em;text-transform:uppercase;color:#B5651D}
h1{position:absolute;left:48px;width:420px;top:840px;margin:0;font-weight:300;font-size:104px;line-height:.86;letter-spacing:-.055em}
h1 b{font-weight:800}
ol{position:absolute;left:520px;right:52px;top:820px;margin:0;padding:0;list-style:none}
li{display:flex;gap:16px;padding:9px 0;border-bottom:1px solid #2B2118;font-weight:500;font-size:24px}
li b{font-weight:800;color:#B5651D;width:34px}
.run{color:#fff}
""",f"""{im('hair','ph','50% 22%')}{run('Vol. 01 — Winter 2027','The glow up','#fff')}
<div class="k">Feature · 8 things</div><h1>The <b>glow up</b> checklist</h1><ol>{lis}</ol>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 35</div>""")
# 36 · sage, cash pile · $10,000
P['CT36']=doc('Color test 36 · indie money · sage',IND+"""
.pin{background:#E3E9D6;color:#24402A}
img.ph{left:52px;right:52px;top:110px;width:896px;height:900px}
.q{position:absolute;left:52px;right:52px;top:1050px;font-weight:300;font-size:84px;line-height:.95;letter-spacing:-.05em}
.q b{font-weight:800}
.cap{position:absolute;left:52px;top:1018px;color:#24402A}
""",f"""{run('Vol. 01 — Winter 2027','Money','#24402A')}{im('cashpile',pos='50% 38%')}
<div class="q">I make <b>$10,000 a month</b> with ease</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 36</div>""")
# 37 · night paper, bob on cash · money in my sleep (vertical type)
P['CT37']=doc('Color test 37 · indie night page',IND+"""
.pin{background:#1F1A16;color:#F2E6D0}
img.ph{left:52px;top:110px;width:700px;height:1220px}
.v{position:absolute;right:40px;top:110px;height:1220px;writing-mode:vertical-rl;font-weight:800;font-size:96px;letter-spacing:-.04em;line-height:1;text-align:right}
.v i{font-weight:300}
""",f"""{run('Vol. 01 — Winter 2027','After hours','#F2E6D0')}{im('bobcash',pos='45% 30%')}
<div class="v">I'm making money <i>in my sleep</i></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="folio" style="color:#F2E6D0">P. 37</div>""")
# 38 · champagne, cash on face · sooooo much money (stretched)
P['CT38']=doc('Color test 38 · indie champagne',IND+"""
.pin{background:#EADCC2;color:#4A3214}
.q{position:absolute;left:52px;right:52px;top:110px;font-weight:600;font-size:74px;line-height:1;letter-spacing:-.04em}
.q em{font-style:normal;font-weight:300;letter-spacing:.22em;color:#B07A1E}
img.ph{left:120px;right:120px;top:430px;width:760px;height:860px}
.cap{position:absolute;left:120px;top:1306px;color:#4A3214}
""",f"""{run('Vol. 01 — Winter 2027','Business','#4A3214')}
<div class="q">My business is bringing <em>sooooo</em> much money</div>{im('cashface',pos='50% 45%')}
<div class="cap"><b>Fig. 8</b>Glitter, feathers, a fresh stack.</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 38</div>""")
# 39 · cobalt, sky + cash · Stripe notifications (clipping)
P['CT39']=doc('Color test 39 · indie cobalt clipping',IND+"""
.pin{background:#1D47B8;color:#F4F1E8}
img.ph{left:0;top:0;width:1000px;height:1080px}
.clip{position:absolute;left:70px;right:110px;top:1000px;background:#F4F1E8;color:#1D47B8;padding:34px 40px;transform:rotate(-2deg);box-shadow:0 18px 40px rgba(0,0,40,.35);font-weight:700;font-size:72px;line-height:.98;letter-spacing:-.04em}
.clip small{display:block;margin-bottom:14px;font-weight:600;font-size:16px;letter-spacing:.3em;text-transform:uppercase}
""",f"""{im('sky','ph','50% 20%')}{run('Vol. 01 — Winter 2027','Morning','#F4F1E8')}
<div class="clip"><small>Overheard, 7:02 am</small>I wake up to Stripe notifications</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="folio" style="color:#F4F1E8">P. 39</div>""")
# 40 · peach + tangerine, orange liner · prove wrong
P['CT40']=doc('Color test 40 · indie peach + tangerine',IND+"""
.pin{background:#F8E2D2;color:#E2531F}
img.ph{left:420px;top:110px;width:528px;height:1000px}
.q{position:absolute;left:52px;top:300px;width:350px;font-weight:800;font-size:76px;line-height:.92;letter-spacing:-.05em}
.q i{font-weight:300}
.cap{position:absolute;left:420px;top:1130px;color:#8A3415}
""",f"""{run('Vol. 01 — Winter 2027','Motivation','#E2531F')}{im('orange',pos='60% 30%')}
<div class="q">Get up girl, <i>you got people</i> to prove wrong</div>
<div class="cap"><b>Fig. 10</b>Orange liner, glass skin, zero excuses.</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="folio">P. 40</div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
