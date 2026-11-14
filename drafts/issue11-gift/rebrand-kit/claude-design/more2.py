import os, sys, json
R = sys.argv[1]
P = dict(e36="0e3d5984b4c70c2684bc95d0d793d137", e27="50e16c5811fdeb41086939469fe9f7c9", e34="d248afd98fef1c1fcda5dfb038152b83",
 e20="e1791165572920b6aed78f5406ef0ddd", e21="17f5110bd7af16e7dac2b470173a92d1", e22="7bae4a6ec2052314c0ed63fd1543de31",
 e13="f5170be23a828e783f74d9f69dc3ce0d", e14="055de3509dddcc34acc1bde8e2460f54", e19="71d727f2abc523ae7070e501a6ffe403",
 e10="5db38769e2a8fe9bb8fe6d1937a9cb7a", e28="bd50c724194c82bcbebe293cc388d577", e37="1561a2278d41fcfc9f3147c62b1e62c2",
 e29="3d709aab8fe8d43997995e74fc5e19b1", e31="e39855a95925db9820fdae8ad7190a0c", e32="04e1e88d776f917541f6c0cbdc6d49d4",
 e24="38a3b25768b6ddc939a88e4e5ba361d5", e25="e7b774cf8b81f36eef9d87a3b980fddc", e33="bee38449fbf73a6689d9321f33a525e9",
 e35="23130e1da621f15e9284efe3052b722c", e26="35962210e47ab96e674456132b95227f")
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
F="filter: contrast(1.04) saturate(0.9)"
H="font-weight:500; letter-spacing:-0.06em; line-height:0.86"
LBL="font-size:10px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase"
W,Ht=816,1056
L=f'width:{W}px; height:{Ht}px; position:relative; overflow:hidden; box-sizing:border-box'
def img(k, st, alt="Aspirational editorial photo"): return f'<img src="/_blob/{P[k]}" alt="{alt}" style="display:block; object-fit:cover; {F}; {st}">'
SPINE=f'<div style="position:absolute; left:{W-50}px; top:0; width:100px; height:{Ht}px; pointer-events:none; background:linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.08) 42%, rgba(0,0,0,0.18) 50%, rgba(255,255,255,0.10) 54%, rgba(0,0,0,0.05) 62%, rgba(0,0,0,0) 100%)"></div>'
ESSAY=("Rebranding your life doesn’t start with a new wardrobe. It starts with one honest sentence about what you want, and one small thing you do this week because of it. "
 "Same girl, bigger dreams. Write it down, make it pretty, then go live a little of it. Future you is built in ordinary Tuesdays, not in one big leap. ")
def para(n, size=11.5): return "".join(f"<p style='margin:0 0 9px'>{ESSAY}</p>" for _ in range(n))
def page(name,title,body,i):
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
<div style="width:{2*W}px; height:{Ht}px; position:relative; overflow:hidden; background:#FFFFFF; font-family:'Inter Tight', sans-serif; color:{INK}; display:flex">
{body}
{SPINE}
<svg style="position:absolute; inset:0; width:100%; height:100%; pointer-events:none; mix-blend-mode:multiply; opacity:{{{{grain}}}}" aria-hidden="true"><filter id="m{i}"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#m{i})"/></svg>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"grain":{{"editor":"range","default":0.16,"min":0,"max":0.5,"step":0.02}},"$preview":{{"width":{2*W},"height":{Ht}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ grain: this.props.grain ?? 0.16 }};
  }}
}}
</script>
</body>
</html>
"""
C={}
# L · Quote set across a full-bleed spread photo, vertical credits on both edges (ref: editorial-08 "Everything we use, everything we do")
rep="".join(f"<span style='margin:0 0 22px'>{w}</span>" for w in ["Money","Chapter 03","The Rebrand Issue"]*4)
C["CopyL"]=("Copy L · Quote across the spread", f"""
<div style="position:absolute; inset:0">{img('e29','width:100%; height:100%')}</div>
<div style="position:absolute; inset:0; background:rgba(13,13,13,0.18)"></div>
<p style="position:absolute; left:110px; right:110px; top:150px; margin:0; text-align:center; font-size:112px; {H}; color:{LILAC}">“Everything I do this year is tied to the life I’m building. I’m in my building era.”</p>
<div style="position:absolute; left:22px; top:40px; bottom:40px; writing-mode:vertical-rl; transform:rotate(180deg); display:flex; {LBL}; color:#fff">{rep}</div>
<div style="position:absolute; right:22px; top:40px; bottom:40px; writing-mode:vertical-rl; display:flex; {LBL}; color:#fff">{rep}</div>
<span style="position:absolute; left:64px; bottom:36px; {LBL}; color:#fff">08</span>
<span style="position:absolute; right:64px; bottom:36px; {LBL}; color:#fff">09 · issue11.app</span>""")
# M · Giant overprinted type on a busy photo (ref: editorial-25 "HAPPY VICTIMS" box)
C["CopyM"]=("Copy M · Overprint type on photo", f"""
<div style="position:absolute; inset:0">{img('e22','width:100%; height:100%')}</div>
<p style="position:absolute; left:40px; right:40px; top:40px; margin:0; font-size:300px; font-weight:600; letter-spacing:-0.07em; line-height:0.78; color:{ROSE}; mix-blend-mode:multiply; opacity:0.92">Same girl, bigger dreams</p>
<div style="position:absolute; left:48px; bottom:48px; width:640px; padding:18px 22px; background:{ICE}">
  <p style="margin:0 0 6px; {LBL}">The Rebrand Issue · 2027</p>
  <p style="margin:0; font-size:15px; line-height:1.45">30 prompts, one list and a 30-day challenge to become your own dream girl. Write it in your words. Live a little of it this week.</p>
</div>
<span style="position:absolute; right:56px; bottom:48px; {LBL}; color:#fff">issue11.app</span>""")
# N · One giant word across the spread with small photos placed like specimens (ref: editorial-33 "gaijin")
specs=[("e20",70,90,170,210,"Closet","04"),("e28",360,620,160,200,"Money","08"),("e24",120,760,150,190,"Glow","14"),
       ("e31",1000,70,160,210,"Circle","10"),("e32",1330,300,170,220,"Style","12"),("e35",1060,690,150,190,"You","19")]
sp="".join(f'<figure style="position:absolute; left:{x}px; top:{y}px; width:{w}px; margin:0">{img(k,f"width:{w}px; height:{h}px")}<figcaption style="display:flex; justify-content:space-between; margin-top:6px; {LBL}; font-size:9px"><span>{c}</span><span>{n}</span></figcaption></figure>' for k,x,y,w,h,c,n in specs)
C["CopyN"]=("Copy N · Giant word + photo specimens", f"""
<div style="position:absolute; inset:0; background:#fff"></div>
<p style="position:absolute; left:40px; right:40px; top:250px; margin:0; text-align:center; font-size:560px; font-weight:500; letter-spacing:-0.07em; line-height:0.8">glow</p>
{sp}
<p style="position:absolute; right:110px; bottom:70px; margin:0; width:300px; font-size:13px; line-height:1.45">Glow (verb): what happens when you stop waiting for January and start with one small thing. Six chapters, six photos, one future you.</p>
<span style="position:absolute; left:64px; bottom:36px; {LBL}">14</span><span style="position:absolute; right:64px; bottom:36px; {LBL}">15</span>""")
# O · Stacked title over a half photo, facing dense columns with a round photo (ref: editorial-08 "The first 15 years")
C["CopyO"]=("Copy O · Stacked title + dense columns", f"""
<div style="{L}; background:{PEACH}">
  {img('e36','position:absolute; left:0; right:0; bottom:0; width:100%; height:560px')}
  <p style="position:absolute; left:56px; top:64px; margin:0; font-size:118px; {H}">The first<br>30 days of<br>future you</p>
  <span style="position:absolute; right:56px; top:64px; {LBL}">The challenge · p.18</span>
</div>
<div style="{L}; background:{PEACH}; padding:64px 64px 56px 88px">
  <div style="display:flex; justify-content:space-between; {LBL}; border-bottom:1px solid {INK}; padding-bottom:10px"><span>The 30-day challenge</span><span>The Rebrand Issue</span></div>
  <p style="margin:16px 0 0; font-size:20px; font-weight:600; letter-spacing:-0.03em; line-height:1.15">One small thing a day for 30 days. No streaks, no guilt. Miss a day? Pick up where you are.</p>
  <div style="margin-top:18px; columns:3; column-gap:20px; text-align:justify; hyphens:auto; font-size:11px; line-height:1.45">{para(5)}</div>
  {img('e33','position:absolute; left:300px; top:440px; width:230px; height:230px; border-radius:50%')}
  <span style="position:absolute; right:64px; bottom:30px; {LBL}">19</span>
</div>""")
# P · Two portraits with an itemised list down each outer edge (ref: editorial-05 "Jack · Tasmiya" what's-in-the-bag spread)
def items(lst): return "".join(f"<p style='margin:0 0 5px; font-size:15px; font-weight:600; letter-spacing:-0.03em; line-height:1.1'>{t}</p>" for t in lst)
left=["Her 2027 list","A savings goal ($20,000)","Lip oil","The Sunday reset","One boundary, said kindly","Vision board, printed","Gym shoes she actually likes","Money date, monthly","Passport"]
right=["Business popping OFF","Dinner with her people","A new rate, asked for","Glow up morning (5 min)","Her own cover","Calm money","Becoming her own dream girl","Future you letter","issue11.app"]
C["CopyP"]=("Copy P · What's in her 2027", f"""
<div style="{L}; background:{MINT}; display:grid; grid-template-columns:230px minmax(0,1fr)">
  <div style="padding:56px 20px 56px 36px"><p style="margin:0 0 14px; {LBL}">What’s in her 2027</p>{items(left)}</div>
  {img('e27','width:100%; height:100%')}
</div>
<div style="{L}; background:{MINT}; display:grid; grid-template-columns:minmax(0,1fr) 230px">
  {img('e26','width:100%; height:100%')}
  <div style="padding:56px 36px 56px 20px"><p style="margin:0 0 14px; {LBL}">…and in yours?</p>{items(right)}<p style="margin:18px 0 0; font-size:12px; line-height:1.4">Write your list on the My 2027 page.</p></div>
</div>""")
for i,(k,(t,body)) in enumerate(C.items()):
    open(os.path.join(R,"project",f"{k}.dc.html"),"w").write(page(k,t,body,20+i))
c=json.load(open(os.path.join(R,"project","canvas.json")))
pos=[("CopyL",0,9944,"Quote across the spread"),("CopyM",1712,9944,"Overprint type on photo"),("CopyN",3424,9944,"Giant word + photo specimens"),("CopyO",0,11187,"Stacked title + dense columns"),("CopyP",1712,11187,"What's in her 2027")]
for k,x,y,n in pos: c["boards"][k+".dc.html"]={"h":1056,"title":f"Inspo remake · {k[-1]} {n}","w":1632,"x":x,"y":y}
c["notes"]["more"]={"kind":"title1","maxW":5056,"text":"More inspo remakes: L–P","w":240,"x":0,"y":9724}
json.dump(c,open(os.path.join(R,"project","canvas.json"),"w"),ensure_ascii=False,indent=2)
print("ok")
