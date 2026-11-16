# Colour test round 2 (CT11–CT20), Nov 16: "show me more". Run: python3 gen2.py
import gen
from gen import doc, LOGO
PH={'e36':'2d5be03e75abb367c4c478e5bf591d8b','e24':'48584939a34a6e613eb4e2f11f2ad13e','l23':'f9aebbe835f6f14787a79bcfba5c4f11','n16':'233e3c8b1372ede1ef7ecb0663429ac7','e22':'192e7090c0bebed08ef694877d2afefc','e27':'9034e8205048f219499561307a1c9748','m24':'96e935322d947be7c76bdde2bb71f084','m26':'a9ca26df86b2661f5b04462f82740107'}
def img(k,pos): return f'<img class="bg" src="/_blob/{PH[k]}" style="object-position:{pos}" alt="Editorial photo (AI-generated)">'
def fade(c,a=45,b=75): return f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,{c}00 {a}%,{c}E6 {b}%,{c} 92%)"></div>'
P={}
# 11 lavender · full-bleed + checklist chips · glow up article
items=['7+ hours of sleep, most nights','Water before coffee','Sunscreen every morning',"One walk or workout you'd repeat",'Three style words + a closet edit','One promise to yourself, kept daily']
chips=''.join(f'<div class="c"><i>✓</i>{x}</div>' for x in items)
P['CT11']=doc('Color test 11 · lavender · full-bleed checklist',"""
.pin{background:#2A1B4A}
h1{position:absolute;left:48px;right:48px;top:640px;margin:0;color:#D9C8FF;font-weight:900;font-size:132px;line-height:.84;letter-spacing:-.055em;text-transform:uppercase}
.list{position:absolute;left:52px;right:52px;top:900px;display:flex;flex-direction:column;gap:12px}
.c{align-self:flex-start;background:#D9C8FF;color:#2A1B4A;font-weight:800;font-size:34px;letter-spacing:-.02em;padding:12px 22px 12px 14px;border-radius:999px;display:flex;gap:14px;align-items:center}
.c i{font-style:normal;width:40px;height:40px;border-radius:50%;background:#2A1B4A;color:#D9C8FF;display:flex;align-items:center;justify-content:center;font-size:24px}
.cta{position:absolute;right:52px;bottom:58px;color:#D9C8FF;font-weight:800;font-size:30px}
""",f"""{img('e36','50% 15%')}{fade('#2A1B4A',25,50)}
<h1>Glow up checklist</h1>
<div class="list">{chips}</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="cta">+ the 30-day plan →</div>""")
# 12 fire red · full-bleed beauty portrait · quote
P['CT12']=doc('Color test 12 · fire red · full-bleed quote',"""
.pin{background:#111}
.q{position:absolute;left:44px;right:40px;top:860px;color:#FF2D3F;font-weight:900;font-size:132px;line-height:.82;letter-spacing:-.055em;text-transform:uppercase}
.tag{right:52px;bottom:52px;background:#FF2D3F;color:#fff}
""",f"""{img('e24','50% 18%')}{fade('#120A0A',40,62)}
<div class="q">My face card is absolutely lethal</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 13 rose · full-bleed couple · quote, italic love line
P['CT13']=doc('Color test 13 · rose · full-bleed quote',"""
.pin{background:#5A0F2A}
.q{position:absolute;left:48px;right:48px;top:930px;color:#fff;font-weight:900;font-size:128px;line-height:.92;letter-spacing:-.045em}
.q i{font-weight:500;color:#FF9EC0}
.tag{right:52px;bottom:52px;background:#FF9EC0;color:#5A0F2A}
""",f"""{img('l23','50% 30%')}{fade('#5A0F2A',42,66)}
<div class="q">The <i>love of my life</i> is coming to me</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 14 champagne gold · full-bleed night street · sticker quote
P['CT14']=doc('Color test 14 · champagne gold · sticker quote',"""
.pin{background:#1A1208}
.stk{position:absolute;left:60px;right:60px;top:1000px;background:#F2C14E;color:#2B1A05;padding:34px 40px;border-radius:30px;transform:rotate(-2.5deg);font-weight:900;font-size:86px;line-height:.95;letter-spacing:-.045em;box-shadow:0 20px 50px rgba(0,0,0,.35)}
.star{position:absolute;right:70px;top:930px;font-size:96px;color:#F2C14E;transform:rotate(12deg)}
.tag{right:52px;bottom:52px;background:#F2C14E;color:#2B1A05}
""",f"""{img('n16','50% 25%')}{fade('#1A1208',55,80)}
<div class="star">✦</div>
<div class="stk">I'm the luckiest girl on the planet</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 15 baby blue + cream · full-bleed dream room · text at top
P['CT15']=doc('Color test 15 · baby blue + cream · text on top',"""
.pin{background:#EAF4FF}
.top{position:absolute;inset:0 0 auto 0;height:620px;background:linear-gradient(180deg,#EAF4FF 0%,#EAF4FFEE 55%,#EAF4FF00 100%)}
.q{position:absolute;left:48px;right:48px;top:90px;color:#1B4F9C;font-weight:900;font-size:128px;line-height:.86;letter-spacing:-.055em;text-transform:uppercase}
.q i{font-style:italic;font-weight:500;text-transform:none;color:#5FA8FF}
.tag{right:52px;bottom:52px;background:#EAF4FF;color:#1B4F9C}
""",f"""{img('e22','50% 70%')}<div class="top"></div>
<div class="q">I only attract <i>the best of</i> the best</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 16 sage · full-bleed calm work photo · quote
P['CT16']=doc('Color test 16 · sage · full-bleed quote',"""
.pin{background:#2F4A2A}
.q{position:absolute;left:48px;right:48px;top:950px;color:#DDF2C9;font-weight:900;font-size:118px;line-height:.88;letter-spacing:-.05em}
.tag{right:52px;bottom:52px;background:#DDF2C9;color:#2F4A2A}
""",f"""{img('e27','50% 20%')}{fade('#2F4A2A',40,62)}
<div class="q">I have all the time in the world</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 17 bubblegum + money green · full-bleed cash photo · giant type
P['CT17']=doc('Color test 17 · bubblegum + green · giant type',"""
.pin{background:#FF7EB6}
.band{position:absolute;left:0;right:0;top:960px;bottom:0;background:#FF7EB6}
.q{position:absolute;left:44px;right:40px;top:1000px;color:#0E5C2F;font-weight:900;font-size:176px;line-height:.8;letter-spacing:-.06em;text-transform:uppercase}
.tag{right:52px;bottom:52px;background:#0E5C2F;color:#FF7EB6}
.logo{filter:none}
""",f"""{img('m24','50% 20%')}<div class="band"></div>
<div class="q">I wake up to money</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 18 teal + gold · full-bleed cash photo · money affirmations article
P['CT18']=doc('Color test 18 · teal + gold · article cover',"""
.pin{background:#06403F}
.n{position:absolute;left:44px;top:700px;color:#FFD23F;font-weight:900;font-size:300px;line-height:.8;letter-spacing:-.07em}
h1{position:absolute;left:48px;right:48px;top:950px;margin:0;color:#fff;font-weight:900;font-size:118px;line-height:.86;letter-spacing:-.05em;text-transform:uppercase}
.sub{position:absolute;left:52px;top:1180px;color:#FFD23F;font-weight:800;font-size:40px;letter-spacing:-.02em}
.cta{position:absolute;right:52px;bottom:58px;color:#FFD23F;font-weight:800;font-size:30px}
""",f"""{img('m26','50% 25%')}{fade('#06403F',30,55)}
<div class="n">40</div><h1>Money affirmations</h1><div class="sub">that actually feel true</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="cta">+ one money move each →</div>""")
# 19 peach → pink gradient · type card
P['CT19']=doc('Color test 19 · peach to pink gradient · type card',"""
.pin{background:linear-gradient(160deg,#FFC9A3 0%,#FF9EC4 55%,#FF6FA8 100%)}
.q{position:absolute;left:48px;right:48px;top:600px;color:#fff;font-weight:900;font-size:176px;line-height:.82;letter-spacing:-.06em;text-transform:uppercase;text-shadow:0 6px 40px rgba(180,30,90,.25)}
.q i{display:block;font-style:italic;font-weight:500;text-transform:none;font-size:120px;color:#8C1446;letter-spacing:-.04em}
.tag{right:52px;bottom:52px;background:#fff;color:#C2185B}
""",f"""<div class="q"><i>I am my own</i>dream girl</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
# 20 sky blue gradient · type card with sparkles
P['CT20']=doc('Color test 20 · sky blue · type card',"""
.pin{background:linear-gradient(180deg,#7FC4FF 0%,#BFE3FF 60%,#F2F9FF 100%)}
.q{position:absolute;left:48px;right:48px;top:560px;color:#0B3D91;font-weight:900;font-size:150px;line-height:.86;letter-spacing:-.055em}
.q i{font-style:italic;font-weight:500;color:#fff}
.s{position:absolute;color:#fff;font-size:80px}
.tag{right:52px;bottom:52px;background:#0B3D91;color:#F2F9FF}
""",f"""<div class="s" style="left:70px;top:380px">✦</div><div class="s" style="right:110px;top:440px;font-size:56px">✦</div><div class="s" style="right:80px;top:1060px">✦</div>
<div class="q"><i>Thank you universe</i> for all the blessings</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="tag">Save this</div>""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
