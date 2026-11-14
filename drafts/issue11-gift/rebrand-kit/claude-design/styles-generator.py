import json, os, sys
OUT = sys.argv[1]
B = lambda h: f"/_blob/{h}"
P = dict(e36="0e3d5984b4c70c2684bc95d0d793d137", e27="50e16c5811fdeb41086939469fe9f7c9", e34="d248afd98fef1c1fcda5dfb038152b83",
 e20="e1791165572920b6aed78f5406ef0ddd", e21="17f5110bd7af16e7dac2b470173a92d1", e22="7bae4a6ec2052314c0ed63fd1543de31",
 e13="f5170be23a828e783f74d9f69dc3ce0d", e14="055de3509dddcc34acc1bde8e2460f54", e19="71d727f2abc523ae7070e501a6ffe403",
 e10="5db38769e2a8fe9bb8fe6d1937a9cb7a", e28="bd50c724194c82bcbebe293cc388d577", e37="1561a2278d41fcfc9f3147c62b1e62c2",
 e29="3d709aab8fe8d43997995e74fc5e19b1", e31="e39855a95925db9820fdae8ad7190a0c", e32="04e1e88d776f917541f6c0cbdc6d49d4",
 e24="38a3b25768b6ddc939a88e4e5ba361d5", e25="e7b774cf8b81f36eef9d87a3b980fddc", e33="bee38449fbf73a6689d9321f33a525e9",
 e35="23130e1da621f15e9284efe3052b722c", e26="35962210e47ab96e674456132b95227f")
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
F="filter: contrast(1.04) saturate(0.9)"
def img(k, style, alt="Aspirational editorial photo"):
    return f'<img src="{B(P[k])}" alt="{alt}" style="display:block; object-fit:cover; {F}; {style}">'
H = "font-weight:500; letter-spacing:-0.06em; line-height:0.86"
LBL = "font-size:10px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase"
PROMPTS = """<sc-for list="{{prompts}}" as="p" hint-placeholder-count="5">
  <div style="break-inside:avoid; margin-bottom:14px">
    <p style="margin:0 0 3px; font-size:12.5px; font-weight:600; letter-spacing:-0.02em; text-align:left"><span style="color:ACC; margin-right:6px">{{p.n}}</span>{{p.title}}</p>
    <p style="margin:0; font-size:11.5px; line-height:1.48">“{{p.text}}”</p>
    <p style="margin:4px 0 0; font-size:10.5px; line-height:1.4; opacity:0.7; text-align:left">Why it works: {{p.why}}</p>
  </div>
</sc-for>"""
def prompts(acc=PINKTXT): return PROMPTS.replace("ACC", acc)
SPINE = '<div style="position:absolute; left:744px; top:0; width:100px; height:1123px; pointer-events:none; background:linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.08) 42%, rgba(0,0,0,0.18) 50%, rgba(255,255,255,0.10) 54%, rgba(0,0,0,0.05) 62%, rgba(0,0,0,0) 100%)"></div>'
def grain(i): return f'<svg style="position:absolute; inset:0; width:100%; height:100%; pointer-events:none; mix-blend-mode:multiply; opacity:{{{{grain}}}}" aria-hidden="true"><filter id="g{i}"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#g{i})"/></svg>'
DATA = [
 dict(n='11', title='What my kind of love looks like.', text='Ask about affection, communication, independence and how we handle disagreements. Help me sort needs, nice-to-haves and what I’m still figuring out.', why='Knowing your values makes the big choices easier.'),
 dict(n='12', title='Friends we actually make time for.', text='Ask who I want to see more and what gets in the way. Help me write one if-then plan.', why='If-then plans make follow-through much more likely.'),
 dict(n='13', title='Meet more of my people.', text='Ask about my interests and places I already like. Suggest three settings where I’d see the same people often.', why='Seeing the same faces again and again is how friendships start.'),
 dict(n='14', title='Say no, kindly.', text='Help me write a short, kind way to set a boundary with [person]. Then play them, and give me feedback.', why='Ready-made words lower the cost of a boundary.'),
 dict(n='15', title='My inner critic is loud today.', text='Here’s what it says: [paste]. Ask me to check the evidence: what’s true, what’s old, and what a friend would say.', why='Questioning a thought (from CBT) loosens its grip.')]
def page(name, title, body, i):
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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>body{{margin:0}}</style>
</helmet>
<div style="width:1588px; height:1123px; position:relative; overflow:hidden; background:#FFFFFF; font-family:'Inter Tight', sans-serif; color:{INK}; display:flex">
{body}
{SPINE}
{grain(i)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"grain":{{"editor":"range","default":0.16,"min":0,"max":0.5,"step":0.02}},"$preview":{{"width":1588,"height":1123}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    const prompts = {json.dumps(DATA, ensure_ascii=False)};
    return {{ grain: this.props.grain ?? 0.16, prompts }};
  }}
}}
</script>
</body>
</html>
"""
L = 'width:794px; height:1123px; position:relative; overflow:hidden; box-sizing:border-box'
S = {}
# A · Framed page: lilac page, photo inside a thin white frame, vertical running text
S["StyleA"] = ("Style A · Framed", f"""
<div style="{L}; background:{LILAC}; padding:56px">
  <div style="position:absolute; inset:36px; border:1.5px solid #fff"></div>
  {img('e31','position:absolute; left:80px; top:80px; width:560px; height:740px')}
  <p style="position:absolute; right:52px; top:90px; margin:0; writing-mode:vertical-rl; {LBL}; color:#fff">My people, my circle · Chapter 04 · The Rebrand Issue</p>
  <p style="position:absolute; left:80px; bottom:96px; margin:0; font-size:64px; {H}">I keep my circle small.</p>
  <span style="position:absolute; left:80px; bottom:56px; {LBL}">10</span>
</div>
<div style="{L}; padding:64px 72px 56px 88px; display:flex; flex-direction:column">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px">
    {img('e21','width:100%; height:300px')}{img('e13','width:100%; height:300px')}
  </div>
  <h2 style="margin:28px 0 0; font-size:110px; {H}">Love.</h2>
  <div style="margin-top:22px; columns:2; column-gap:28px; text-align:justify; hyphens:auto">{prompts()}</div>
  <div style="margin-top:auto; display:flex; justify-content:space-between; {LBL}"><span>issue11.app</span><span>11</span></div>
</div>""")
# B · Scattered type: headline letters spread over a white page, facing a full-bleed photo
letters = "".join(f'<span style="position:absolute; left:{x}px; top:{y}px; font-size:150px; {H}">{c}</span>' for c,x,y in
  [("l",70,120),("o",330,300),("v",120,520),("e",520,700)])
S["StyleB"] = ("Style B · Scattered type", f"""
<div style="{L}; background:#fff">
  {letters}
  <p style="position:absolute; left:640px; top:120px; margin:0; writing-mode:vertical-rl; {LBL}">Chapter 04 · Prompts 11–15</p>
  <div style="position:absolute; left:72px; right:88px; bottom:64px; columns:2; column-gap:28px; text-align:justify; hyphens:auto">{prompts(ROSE)}</div>
</div>
<div style="{L}">
  {img('e36','position:absolute; inset:0; width:100%; height:100%')}
  <p style="position:absolute; left:88px; bottom:70px; margin:0; font-size:56px; {H}; color:#fff">My people, my circle.</p>
  <span style="position:absolute; right:48px; bottom:36px; {LBL}; color:#fff">11</span>
</div>""")
# C · Contact sheet: photo grid with captions, facing an ice text page
cells = "".join(f'<figure style="margin:0">{img(k,"width:100%; height:300px")}<figcaption style="margin-top:6px; {LBL}; font-size:9px">{c}</figcaption></figure>'
  for k,c in [("e20","Sunday plans"),("e22","The group chat"),("e27","Dinner, 8pm"),("e19","Soft launch"),("e10","Just us"),("e37","Same table, every week")])
S["StyleC"] = ("Style C · Contact sheet", f"""
<div style="{L}; background:#fff; padding:64px 56px 56px 64px">
  <div style="display:flex; justify-content:space-between; {LBL}"><span>Contact sheet</span><span>10</span></div>
  <div style="margin-top:24px; display:grid; grid-template-columns:repeat(3, 1fr); gap:16px 12px">{cells}</div>
  <p style="margin:30px 0 0; font-size:44px; {H}">Your people, your story.</p>
</div>
<div style="{L}; background:{ICE}; padding:64px 72px 56px 88px; display:flex; flex-direction:column">
  <div style="display:flex; justify-content:space-between; {LBL}"><span>Chapter 04 · Love</span><span>The Rebrand Issue</span></div>
  <h2 style="margin:40px 0 0; font-size:150px; {H}">Love.</h2>
  <p style="margin:12px 0 0; font-size:22px; font-weight:500; letter-spacing:-0.03em; color:{PINKTXT}">My people, my circle</p>
  <div style="margin-top:30px; columns:2; column-gap:28px; text-align:justify; hyphens:auto">{prompts()}</div>
  <div style="margin-top:auto; display:flex; justify-content:space-between; {LBL}"><span>issue11.app</span><span>11</span></div>
</div>""")
# D · Big word: huge headline at the bottom, small offset photo, facing two stacked photos
S["StyleD"] = ("Style D · Big word", f"""
<div style="{L}; background:#fff; padding:64px 72px">
  {img('e32','position:absolute; right:88px; top:72px; width:300px; height:390px')}
  <p style="position:absolute; left:72px; top:72px; margin:0; width:280px; font-size:13px; line-height:1.5">Five prompts for the people you love, the people you’re still meeting, and the boundaries that protect both.</p>
  <div style="position:absolute; left:72px; right:120px; top:500px; columns:2; column-gap:28px; text-align:justify; hyphens:auto">{prompts()}</div>
  <h2 style="position:absolute; left:56px; bottom:30px; margin:0; font-size:260px; {H}">Love</h2>
</div>
<div style="{L}; background:#fff; padding:40px 40px 40px 72px; display:flex; flex-direction:column; gap:14px">
  {img('e33','width:100%; height:560px')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; flex:1">{img('e35','width:100%; height:100%')}{img('e26','width:100%; height:100%')}</div>
  <div style="display:flex; justify-content:space-between; {LBL}"><span>Chapter 04 · The Rebrand Issue</span><span>11</span></div>
</div>""")
# E · Colour block: peach top band with a giant number, photo below; facing a mint margin text page
S["StyleE"] = ("Style E · Colour block", f"""
<div style="{L}; background:#fff">
  <div style="height:380px; background:{PEACH}; padding:56px 64px; box-sizing:border-box; position:relative">
    <span style="{LBL}">Chapter</span>
    <span style="position:absolute; right:56px; bottom:-30px; font-size:300px; {H}">04</span>
  </div>
  {img('e24','width:100%; height:743px')}
</div>
<div style="{L}; background:#fff; display:grid; grid-template-columns:200px minmax(0,1fr)">
  <div style="background:{MINT}; padding:64px 24px; box-sizing:border-box; display:flex; flex-direction:column; justify-content:space-between">
    <span style="{LBL}">Love</span>
    {img('e25','width:100%; height:230px')}
    {img('e29','width:100%; height:230px')}
    <span style="{LBL}">11</span>
  </div>
  <div style="padding:64px 64px 56px 48px; display:flex; flex-direction:column">
    <h2 style="margin:0; font-size:120px; {H}">Love.</h2>
    <p style="margin:12px 0 0; font-size:30px; font-weight:500; letter-spacing:-0.04em">“I keep my circle small.”</p>
    <div style="margin-top:28px; text-align:justify; hyphens:auto">{prompts(ROSE)}</div>
    <span style="margin-top:auto; {LBL}">issue11.app</span>
  </div>
</div>""")
for i,(k,(t,body)) in enumerate(S.items()):
    open(os.path.join(OUT, f"{k}.dc.html"),"w").write(page(k,t,body,i))
print("ok")
