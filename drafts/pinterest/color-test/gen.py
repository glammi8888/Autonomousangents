# Generates the 10 colour + variety test pins (Nov 16). Run: python3 gen.py
LOGO='/_blob/d196614efc6265e2205729134fb523b8'
PH={'m28':'1c5357936c0f3bb41b01c25d9f8b01a9','e20':'e0b2acd5fe4e7845cf15c0a2d79a2367','e21':'7c7c9f7639583c427c5ebf34599a953c','e29':'3ffd68c0b9a6904c16daec8559ee45b3','n17':'61c13ba5e0a9205473641aaca015e7c7'}
BASE="""body{margin:0}
.pin{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:'Inter Tight',system-ui,sans-serif;color:#0D0D0D}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.logo{position:absolute;left:52px;bottom:48px;height:66px}
.w{filter:invert(1)}
.tag{position:absolute;font-weight:800;font-size:24px;letter-spacing:.16em;padding:12px 20px;text-transform:uppercase}
"""
def doc(title,css,body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>
{BASE}{css}
</style>
</helmet>
<div class="pin">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1000,"height":1500}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
"""
def img(k,pos,alt='Editorial photo (AI-generated)'):
    return f'<img class="bg" src="/_blob/{PH[k]}" style="object-position:{pos}" alt="{alt}">'
pins={}
# 1 emerald · full-bleed photo · quote
pins['CT01']=doc('Color test 01 · emerald · full-bleed quote',"""
.pin{background:#0B5D45}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,93,69,0) 42%,rgba(11,93,69,.92) 66%,#0B5D45 80%)}
.q{position:absolute;left:52px;right:52px;top:900px;color:#fff;font-weight:900;font-size:124px;line-height:.9;letter-spacing:-.05em}
.q span{color:#9DF2C8}
.tag{right:52px;bottom:52px;background:#9DF2C8;color:#0B5D45}
""",f"""{img('m28','35% 30%')}
<div class="fade"></div>
<div class="q">I'm making money <span>in my sleep</span></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">
<div class="tag">Save this</div>""")
# 2 butter yellow · full-bleed dream closet · quote
pins['CT02']=doc('Color test 02 · butter yellow · full-bleed quote',"""
.pin{background:#111}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 38%,rgba(0,0,0,.78) 72%,rgba(0,0,0,.9) 100%)}
.q{position:absolute;left:48px;right:40px;top:860px;color:#FFE36E;font-weight:900;font-size:158px;line-height:.84;letter-spacing:-.055em;text-transform:uppercase}
.tag{right:52px;bottom:52px;background:#FFE36E;color:#111}
""",f"""{img('e20','50% 50%')}
<div class="fade"></div>
<div class="q">My dream life wants me</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">
<div class="tag">Save this</div>""")
# 3 hot pink + red · full-bleed magazine cover · article self-love
pins['CT03']=doc('Color test 03 · hot pink + red · magazine cover',"""
.pin{background:#FF3EA5}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.55) 100%)}
.kick{position:absolute;left:52px;top:52px;background:#E8112D;color:#fff;font-weight:900;font-size:30px;letter-spacing:.12em;padding:12px 20px;text-transform:uppercase}
h1{position:absolute;left:44px;right:40px;top:1010px;margin:0;color:#FF3EA5;font-weight:900;font-size:126px;line-height:.82;letter-spacing:-.055em;text-transform:uppercase;text-shadow:0 4px 30px rgba(0,0,0,.25)}
.lines{position:absolute;left:52px;top:1268px;display:flex;gap:12px}
.lines span{background:#E8112D;color:#fff;font-weight:800;font-size:30px;padding:10px 16px;letter-spacing:-.01em}
.logo{bottom:auto;top:1394px}
""",f"""{img('n17','50% 20%')}
<div class="fade"></div>
<div class="kick">60 that feel true</div>
<h1>Self love<br>affirmations</h1>
<div class="lines"><span>Self love</span><span>Self worth</span><span>Confidence</span></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 4 cherry red · full-bleed work photo · quote (A) ; 10 = same in black and white (control)
def ct4(color,name,pid):
    return doc(f'Color test {pid[2:]} · {name} · full-bleed quote',f"""
.pin{{background:#111}}
.fade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.35) 100%)}}
.q{{position:absolute;left:52px;right:52px;top:880px}}
.q span{{background:{color};color:#fff;font-weight:900;font-size:96px;line-height:1.22;letter-spacing:-.045em;padding:0 16px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.tag{{right:52px;bottom:52px;background:#fff;color:{color}}}
""",f"""{img('e29','50% 25%')}
<div class="fade"></div>
<div class="q"><span>I'm the girl who always makes it work</span></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">
<div class="tag">Save this</div>""")
pins['CT04']=ct4('#D7092B','cherry red','CT04')
pins['CT10']=doc('Color test 10 · blush + raspberry · one-line type card',"""
.pin{background:#FCD4DA}
.q{position:absolute;left:44px;right:40px;top:470px;color:#C2185B;font-weight:900;font-size:192px;line-height:.82;letter-spacing:-.06em;text-transform:uppercase}
.q i{font-style:italic;font-weight:500;text-transform:none;letter-spacing:-.04em;color:#E8457F}
.tag{right:52px;bottom:52px;background:#C2185B;color:#FCD4DA}
""",f"""<div class="q">2027 <i>is the year I</i> lifemaxx</div>
<img class="logo" src="{LOGO}" alt="ISSUE11">
<div class="tag">Save for 2027</div>""")
# 5 chocolate + baby blue · torn paper · article overthinking at night
pins['CT05']=doc('Color test 05 · chocolate + baby blue · torn paper',"""
.pin{background:#3B2218}
h1{position:absolute;left:48px;right:48px;top:96px;margin:0;color:#A9D4FF;font-weight:900;font-size:118px;line-height:.86;letter-spacing:-.05em;text-transform:uppercase}
.paper{position:absolute;left:40px;right:40px;top:560px;height:760px;background:#A9D4FF;transform:rotate(-1.5deg);
clip-path:polygon(0 3%,4% 0,9% 2%,15% .5%,22% 2.5%,30% .5%,37% 2%,45% 0,53% 2%,61% .5%,69% 2.5%,77% .5%,85% 2%,92% 0,100% 2.5%,100% 97%,95% 100%,88% 98%,80% 99.5%,72% 97.5%,64% 99.5%,56% 98%,48% 100%,40% 98%,32% 99.5%,24% 97.5%,16% 99.5%,8% 98%,0 100%);padding:70px 56px;box-sizing:border-box}
.paper ol{margin:0;padding:0;list-style:none;color:#3B2218}
.paper li{display:flex;gap:22px;padding:22px 0;border-bottom:2px solid rgba(59,34,24,.35);font-weight:800;font-size:52px;line-height:1.06;letter-spacing:-.025em;padding:32px 0}
.paper li:last-child{border-bottom:0}
.paper b{flex:none;font-weight:900;width:44px}
.cta{position:absolute;right:52px;bottom:60px;color:#A9D4FF;font-weight:800;font-size:30px}
""",f"""<h1>How to stop overthinking at night</h1>
<div class="paper"><ol>
<li><b>1</b>Do a brain dump before bed</li>
<li><b>2</b>Write tomorrow's first step</li>
<li><b>3</b>Keep your phone out of reach</li>
<li><b>4</b>Still awake after 20 minutes? Get up, do something calm in dim light</li>
</ol></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">
<div class="cta">+ 9 daytime fixes →</div>""")
# 6 cobalt · Notes screenshot · quote
pins['CT06']=doc('Color test 06 · cobalt · notes screenshot',"""
.pin{background:#1F3FFF}
.card{position:absolute;left:70px;right:70px;top:330px;height:660px;background:#fff;border-radius:44px;box-shadow:0 30px 80px rgba(0,0,40,.35);padding:44px 56px;box-sizing:border-box}
.bar{display:flex;justify-content:space-between;color:#E0A100;font-weight:700;font-size:34px}
.date{margin:60px 0 26px;text-align:center;color:#8A8A8E;font-weight:600;font-size:26px}
.note{font-weight:900;font-size:136px;line-height:.9;letter-spacing:-.05em;color:#1F3FFF}
.tag{left:70px;top:1030px;background:#fff;color:#1F3FFF}
""",f"""<div class="card"><div class="bar"><span>‹ Notes</span><span>Done</span></div><div class="date">16 November 2026 at 21:04</div><div class="note">My nervous system is calm</div></div>
<div class="tag">Save for a hard day</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 7 plum tint · full-bleed carousel cover · article vision board for manifestation
pins['CT07']=doc('Color test 07 · plum tint · carousel cover',"""
.pin{background:#4A0F3E}
.tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(74,15,62,.35) 0%,rgba(74,15,62,.55) 45%,rgba(74,15,62,.92) 75%);mix-blend-mode:multiply}
.tint2{position:absolute;inset:0;background:linear-gradient(180deg,rgba(74,15,62,0) 50%,rgba(74,15,62,.85) 78%)}
.count{position:absolute;right:52px;top:52px;background:rgba(255,255,255,.92);color:#4A0F3E;font-weight:800;font-size:28px;padding:10px 18px;border-radius:999px}
.kick{position:absolute;left:52px;top:780px;color:#FFC2E6;font-weight:800;font-size:30px;letter-spacing:.14em;text-transform:uppercase}
.q{position:absolute;left:48px;right:48px;top:836px;color:#fff;font-weight:900;font-size:112px;line-height:.9;letter-spacing:-.05em}
.q span{color:#FFC2E6}
.swipe{position:absolute;right:52px;bottom:56px;color:#fff;font-weight:800;font-size:32px}
""",f"""{img('e21','50% 40%')}
<div class="tint"></div><div class="tint2"></div>
<div class="count">1 / 6</div>
<div class="kick">Vision board for manifestation</div>
<div class="q">Your vision board isn't broken. <span>It's unfinished.</span></div>
<img class="logo w" src="{LOGO}" alt="ISSUE11">
<div class="swipe">5 steps to finish it →</div>""")
# 8 tangerine · save-this card · article word of the year
WOTY=[('Confidence','Brave · Seen · Bold'),('Calm','Rest · Soft · Enough'),('A fresh start','Begin · Bloom · Leap'),('Money + work','Build · Grow · Wealth'),('Love','Open · Love · Home'),('Energy','Strong · Glow · Alive'),('Joy','Play · Yes · Magic'),('Boundaries','No · Choose · Mine')]
rows=''.join(f'<div class="r"><b>{a}</b><span>{b}</span></div>' for a,b in WOTY)
pins['CT08']=doc('Color test 08 · tangerine · save this card',"""
.pin{background:#FF7A1A}
.card{position:absolute;left:52px;right:52px;top:120px;height:1170px;background:#FFF6EC;border-radius:28px;padding:60px 52px;box-sizing:border-box}
.tab{position:absolute;right:40px;top:-30px;background:#B23A00;color:#FFF6EC;font-weight:800;font-size:26px;letter-spacing:.16em;padding:14px 24px;border-radius:999px}
h1{margin:0;color:#5A1E00;font-weight:900;font-size:112px;line-height:.86;letter-spacing:-.05em;text-transform:uppercase}
h1 em{font-style:normal;color:#FF7A1A}
.r{display:flex;justify-content:space-between;align-items:baseline;padding:19px 0;color:#5A1E00;border-bottom:2px solid #FFB27A}
.r:first-of-type{margin-top:36px;border-top:4px solid #FF7A1A}
.r b{font-weight:600;font-size:28px;letter-spacing:.06em;text-transform:uppercase}
.r span{font-weight:900;font-size:40px;letter-spacing:-.03em}
.cta{position:absolute;right:52px;bottom:60px;color:#5A1E00;font-weight:800;font-size:30px}
""",f"""<div class="card"><div class="tab">SAVE THIS</div><h1>Word of the year <em>2027</em></h1>{rows}</div>
<img class="logo" src="{LOGO}" alt="ISSUE11">
<div class="cta">120 words + how to pick →</div>""")
# 9 lilac · list · article new year journal prompts
P=["How do I want to feel next December?","What am I ready to let go of?","What's one small move I can make this week?","What does “enough” look like for me this year?","What's my word of the year?"]
li=''.join(f'<li><b>{i+1}</b>{p}</li>' for i,p in enumerate(P))
pins['CT09']=doc('Color test 09 · lilac · list',"""
.pin{background:#CDB4FF}
.kick{position:absolute;left:52px;top:84px;background:#5B21B6;color:#F3EBFF;font-weight:800;font-size:26px;letter-spacing:.14em;padding:12px 20px;text-transform:uppercase}
h1{position:absolute;left:48px;right:48px;top:170px;margin:0;color:#3B0F7A;font-weight:900;font-size:126px;line-height:.86;letter-spacing:-.05em;text-transform:uppercase}
ol{position:absolute;left:52px;right:52px;top:620px;margin:0;padding:0;list-style:none;border-top:5px solid #5B21B6}
li{display:flex;gap:26px;padding:26px 0;color:#3B0F7A;border-bottom:2px solid #9F7AEA;font-weight:800;font-size:44px;line-height:1.08;letter-spacing:-.025em}
li b{flex:none;width:60px;height:60px;border-radius:50%;background:#5B21B6;color:#F3EBFF;display:flex;align-items:center;justify-content:center;font-size:32px}
.cta{position:absolute;right:52px;bottom:60px;color:#3B0F7A;font-weight:800;font-size:30px}
""",f"""<div class="kick">Answer before 2027</div>
<h1>New year journal prompts</h1>
<ol>{li}</ol>
<img class="logo" src="{LOGO}" alt="ISSUE11">
<div class="cta">All 40 prompts →</div>""")
for k,v in pins.items(): open(f'{k}.dc.html','w').write(v)
print(len(pins))
