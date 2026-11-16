# Round 13 (CT132–CT142), Nov 16: viral manifestation formats not yet copied (../viral/2026-11-16-viral-manifest2.json + vb-manifest, 364 pins) + angel numbers (Megan: "Ohhh we can do angel numbers too !!!"). BANK lines only; numbers paired with BANK lines, no invented meanings.
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen13 import S, T, U, A, s
P={}
# 132 · 8888 save-to-affirm (1,532)
P['CT132']=doc('Color test 132 · viral 8888 save to affirm',S+"""
.pin{background:#fff;color:#111}
.n{position:absolute;left:0;right:0;top:330px;text-align:center;font-weight:800;font-size:250px;letter-spacing:-.04em;line-height:1}
.q{position:absolute;left:90px;right:90px;top:660px;text-align:center;font-weight:500;font-size:68px;line-height:1.2;letter-spacing:-.02em}
.cta{position:absolute;left:0;right:0;top:1180px;text-align:center;font-weight:700;font-size:34px}
""",f"""{T()}<div class="n">8888</div><div class="q">I make way more money than what I'm able to spend</div><div class="cta">save this pin to affirm !</div>{U('#111')}""")
# 133 · angel number over sky photo
P['CT133']=doc('Color test 133 · angel number 111 over photo',S+"""
.pin{background:#1D47B8}
.n{position:absolute;left:0;right:0;top:860px;text-align:center;color:#fff;font-weight:800;font-size:330px;letter-spacing:-.06em;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.35)}
.c{position:absolute;left:0;right:0;top:1210px;text-align:center;color:#fff;font-style:italic;font-weight:400;font-size:52px;text-shadow:0 2px 16px rgba(0,0,0,.5)}
""",f"""<img class="f full" src="{s('sky')}" style="object-position:50% 20%" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(10,20,60,.55) 85%)"></div>{T('w')}<div class="n">111</div><div class="c">Dream life is on its way.</div>{U('#fff')}""")
# 134 · 777 lucky
P['CT134']=doc('Color test 134 · angel number 777 lucky',S+"""
.pin{background:#C8102E}
.n{position:absolute;left:0;right:0;top:960px;text-align:center;color:#FFE14D;font-weight:800;font-size:250px;letter-spacing:-.06em;line-height:1}
.c{position:absolute;left:60px;right:60px;top:1230px;text-align:center;color:#fff;font-weight:700;font-size:60px;letter-spacing:-.02em;line-height:1.1}
""",f"""<img class="f" src="{s('red')}" style="left:0;top:0;width:100%;height:930px;object-position:50% 20%" {A}>{T('w')}<div class="n">777</div><div class="c">I'm the luckiest girl on the planet</div>{U('#fff')}""")
# 135 · angel numbers cheat sheet (BANK lines only)
rows=[('111','Dream life is on its way'),('222','The right people, places, and moments find me'),('333','My nervous system is calm'),('777',"I'm the luckiest girl on the planet"),('888',"I make way more money than what I'm able to spend")]
P['CT135']=doc('Color test 135 · angel numbers affirmations sheet',S+"""
.pin{background:#F6D8E4;color:#2A1020}
h1{position:absolute;left:0;right:0;top:170px;margin:0;text-align:center;font-weight:800;font-size:96px;letter-spacing:-.04em;color:#C2207E}
.r{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:40px;border-top:2px solid rgba(194,32,126,.35);padding-top:26px}
.r b{font-weight:800;font-size:96px;letter-spacing:-.04em;width:230px;flex:none;color:#C2207E}
.r span{font-size:40px;line-height:1.2;font-weight:500}
""",f"""{T()}<h1>angel numbers</h1>"""+''.join(f'<div class="r" style="top:{330+i*175}px"><b>{n}</b><span>{t}</span></div>' for i,(n,t) in enumerate(rows))+U('#2A1020'))
# 136 · "money loves me!" repeat over photo (1,557)
P['CT136']=doc('Color test 136 · viral repeated pink line over money photo',S+"""
.pin{background:#333}
.rp{position:absolute;left:40px;right:40px;top:470px;color:#FF4FA3;font-weight:800;font-size:76px;letter-spacing:-.03em;line-height:1.08;text-shadow:0 3px 20px rgba(0,0,0,.35)}
""",f"""<img class="f full" src="{s('cashpile')}" style="object-position:50% 50%" {A}><div style="position:absolute;inset:0;background:rgba(0,0,0,.15)"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 80%,rgba(0,0,0,.6) 100%)"></div>{T('w')}<div class="rp">{''.join('<div>I wake up to money</div>' for _ in range(6))}</div>{U('#fff')}""")
# 137 · big pink spaced text on white (my pinterest boards are my reality, 1,766)
P['CT137']=doc('Color test 137 · viral big pink spaced text',S+"""
.pin{background:#F7F5F6}
.q{position:absolute;left:80px;right:80px;top:330px;text-align:center;color:#FF6FB5;font-weight:300;font-size:128px;line-height:1.28;letter-spacing:.01em}
""",f"""{T()}<div class="q">my<br>dream life<br>wants<br>me</div>{U('#C2207E')}""")
# 138 · spaced caps on cream (I AM CREATING THE LIFE OF MY DREAMS, 1,176)
P['CT138']=doc('Color test 138 · viral spaced caps on cream',S+"""
.pin{background:#FAF6EE;color:#1A1A1A}
.q{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:300;font-size:64px;line-height:1.9;letter-spacing:.32em}
""",f"""{T()}<div class="q">I AM<br>MY OWN<br>DREAM<br>GIRL</div>{U('#1A1A1A')}""")
# 139 · italic over hand holding cash (I get everything I want, 2,441)
P['CT139']=doc('Color test 139 · viral italic over money photo',S+"""
.pin{background:#222}
.c{position:absolute;left:60px;right:60px;top:1060px;text-align:center;color:#fff;font-style:italic;font-weight:800;font-size:92px;letter-spacing:-.04em;line-height:1;text-shadow:0 4px 24px rgba(0,0,0,.7)}
""",f"""<img class="f full" src="{s('sleepcash')}" style="object-position:50% 40%" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 80%,rgba(0,0,0,.6) 100%)"></div>{T('w')}<div class="c">I'm making money in my sleep</div>{U('#fff')}""")
# 140 · sticker caption over sky photo (idk i just have this crazy faith, 1,021)
P['CT140']=doc('Color test 140 · viral sticker over photo',S+"""
.pin{background:#7AA0D8}
.st{position:absolute;left:150px;top:1060px;transform:rotate(-4deg);display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.st span{background:#fff;color:#C2207E;font-weight:800;font-size:76px;letter-spacing:-.03em;padding:4px 18px;line-height:1.05}
""",f"""<img class="f full" src="{s('flying')}" style="object-position:50% 40%" {A}>{T('w')}<div class="st"><span>Spoiled by</span><span>the Universe ⭐</span></div>{U('#fff')}""")
# 141 · old paper save card (Money will fall like rain…, 1,412)
P['CT141']=doc('Color test 141 · viral old paper save card',S+"""
.pin{background:radial-gradient(circle at 50% 45%,#F1E3C4 0%,#E2CC9E 55%,#C9AE7A 100%);color:#1E160C}
.q{position:absolute;left:100px;right:100px;top:400px;text-align:center;font-weight:600;font-size:92px;line-height:1.16;letter-spacing:-.03em}
.cta{position:absolute;left:0;right:0;top:1200px;text-align:center;font-weight:700;font-size:40px}
""",f"""{T()}<div class="q">Thank you universe for all the blessings</div><div class="cta">Save this to affirm!</div>{U('#1E160C')}""")
# 142 · pink 369 method page with big numbers (2,009)
P['CT142']=doc('Color test 142 · viral pink 369 method',S+"""
.pin{background:#F4C6D7;color:#3A0F24}
h1{position:absolute;left:0;right:0;top:150px;margin:0;text-align:center;font-weight:800;font-size:80px;letter-spacing:-.03em;line-height:1}
h1 small{display:block;font-weight:500;font-size:38px;letter-spacing:.2em;margin-top:10px}
.r{position:absolute;left:80px;right:80px;display:flex;gap:40px}
.r b{font-weight:800;font-size:200px;line-height:.9;width:130px;flex:none;color:#C2207E}
.r div{font-size:30px;line-height:1.3;font-style:italic}
.r i{display:block;font-style:normal;font-weight:700;font-size:28px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:6px}
""",f"""{T()}<h1>369<small>MANIFESTATION METHOD</small></h1>
<div class="r" style="top:400px"><b>3</b><div><i>Morning</i>{'<br>'.join(['I wake up to money']*3)}</div></div>
<div class="r" style="top:620px"><b>6</b><div><i>Afternoon</i>{'<br>'.join(['My business is bringing sooooo much money']*6)}</div></div>
<div class="r" style="top:960px"><b>9</b><div><i>Night</i>{'<br>'.join(["I'm making money in my sleep"]*9)}</div></div>{U('#3A0F24')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(list(P))
