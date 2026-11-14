import os, sys, json, math
src = open(os.path.join(os.path.dirname(__file__), "styles.py")).read().split("L = '")[0]
exec(src)
L = 'width:816px; height:1056px; position:relative; overflow:hidden; box-sizing:border-box'
def star(cx, cy, r):
    pts=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5; rr=r if i%2==0 else r*0.4
        pts.append(f"{cx+rr*math.cos(a):.1f}px {cy+rr*math.sin(a):.1f}px")
    return "polygon(" + ", ".join(pts) + ")"
ESSAY = ("Love is the part of the plan nobody puts on a vision board. The friends who text back. The dinner that happens every month because someone booked it. "
 "The boundary you finally said out loud. This chapter is about choosing your people on purpose: who you want more of, how you want to be loved, "
 "and what you won’t keep explaining. Same girl, softer heart, stronger edges. Pick one prompt, answer it honestly, and leave with one small plan. ")
def essay(cols=2, size=12):
    return f'<div style="columns:{cols}; column-gap:24px; text-align:justify; hyphens:auto; font-size:{size}px; line-height:1.5">' + "".join(f"<p style='margin:0 0 10px'>{ESSAY}</p>" for _ in range(2)) + '</div>'
C = {}
# F · Headline over photo (ref: editorial-01 "Love that if it were a character")
rep = "".join("<span style='margin:0 0 18px'>Love</span>" for _ in range(14))
C["CopyF"] = ("Copy F · Headline over photo", f"""
<div style="{L}">
  {img('e20','position:absolute; inset:0; width:100%; height:100%')}
  <p style="position:absolute; left:64px; right:70px; top:80px; margin:0; font-size:96px; {H}; color:#fff; text-shadow:0 2px 24px rgba(0,0,0,0.35)">I keep my circle small, and my standards high.</p>
  <div style="position:absolute; left:18px; top:40px; bottom:40px; writing-mode:vertical-rl; transform:rotate(180deg); display:flex; {LBL}; color:#fff">{rep}</div>
  <div style="position:absolute; left:0; right:0; bottom:0; height:22px; background:{MINT}"></div>
  <span style="position:absolute; right:56px; bottom:44px; font-size:40px; {H}; color:#fff; writing-mode:vertical-rl">10</span>
</div>
<div style="{L}; background:{PEACH}; padding:64px 80px 56px 88px">
  {essay()}
  <div style="margin-top:20px; columns:2; column-gap:24px; text-align:justify; hyphens:auto">{prompts(INK)}</div>
  <span style="position:absolute; left:60px; bottom:44px; font-size:40px; {H}; writing-mode:vertical-rl">11</span>
  <div style="position:absolute; right:18px; top:40px; bottom:40px; writing-mode:vertical-rl; display:flex; {LBL}">{rep}</div>
</div>""")
# G · Scattered coloured words on a colour page (ref: editorial-01 "It's a dirty job someone has to do")
words = [("I",70,380),("keep",250,380),("my",90,470),("circle",70,560),("small,",90,650),("on",420,650),("purpose.",360,740)]
sc = "".join(f'<span style="position:absolute; left:{x}px; top:{y}px; font-size:84px; {H}; color:{PINKTXT}">{w}</span>' for w,x,y in words)
C["CopyG"] = ("Copy G · Scattered words", f"""
<div style="{L}; background:{ICE}">
  <span style="position:absolute; left:64px; top:48px; {LBL}">Chapter 04 · Love</span>
  {img('e31','position:absolute; left:250px; top:90px; width:190px; height:250px')}
  {sc}
</div>
<div style="{L}; background:{ICE}; padding:64px 72px 56px 88px">
  <div style="display:flex; justify-content:space-between; {LBL}"><span>The Rebrand Issue</span><span>11</span></div>
  <div style="margin-top:24px; columns:2; column-gap:26px; text-align:justify; hyphens:auto">{prompts(INK)}</div>
  <div style="margin-top:6px">{essay(2, 11.5)}</div>
  <span style="position:absolute; left:300px; top:420px; font-size:84px; {H}; color:{PINKTXT}; mix-blend-mode:multiply">soft</span>
  <span style="position:absolute; left:520px; top:780px; font-size:84px; {H}; color:{PINKTXT}; mix-blend-mode:multiply">heart</span>
</div>""")
# H · Quote page facing full-bleed photo (ref: editorial-01 Kyoto book / editorial-05 "I need to soak up ideas")
C["CopyH"] = ("Copy H · Quote + full photo", f"""
<div style="{L}; background:#fff; padding:96px 88px">
  <p style="margin:0; font-size:120px; {H}; color:{ROSE}; line-height:0.6">“</p>
  <p style="margin:6px 0 0; font-size:58px; {H}; line-height:0.98">I’m too grown to keep explaining myself.</p>
  <p style="margin:22px 0 0; {LBL}; color:#55524c">Prompt 14 · Say no, kindly</p>
  <div style="position:absolute; left:88px; right:88px; bottom:80px">{essay(2, 11.5)}</div>
</div>
<div style="{L}; background:{LILAC}">
  {img('e27','position:absolute; inset:0; width:100%; height:100%')}
  <p style="position:absolute; right:22px; top:60px; margin:0; writing-mode:vertical-rl; {LBL}; font-size:8px; color:#fff">Photographed for The Rebrand Issue · issue11.app · 11</p>
</div>""")
# I · Giant vertical word + app windows on photo (ref: editorial-05 "Renderizarme / Loading")
load = "".join(f'<span style="writing-mode:vertical-rl; transform:rotate(180deg); font-size:44px; font-weight:400; letter-spacing:-0.04em; color:{INK}; opacity:0.85">future you . . . loading . . . future you</span>' for _ in range(3))
def win(x,y,w,t,body):
    return f'''<div style="position:absolute; left:{x}px; top:{y}px; width:{w}px; background:#fff; border:1px solid {INK}; box-shadow:4px 4px 0 {INK}">
  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 8px; background:{ICE}; border-bottom:1px solid {INK}; font-size:10px; font-weight:600"><span>{t}</span><span>● ● ●</span></div>
  <p style="margin:0; padding:10px 12px; font-size:11.5px; line-height:1.45">{body}</p></div>'''
C["CopyI"] = ("Copy I · Giant word + app windows", f"""
<div style="{L}; background:{LILAC}; display:flex; gap:10px; padding:56px 40px 56px 56px">
  <span style="writing-mode:vertical-rl; transform:rotate(180deg); font-size:250px; {H}; line-height:0.78">Rebrand</span>
  <span style="writing-mode:vertical-rl; transform:rotate(180deg); font-size:250px; {H}; line-height:0.78; color:#fff">me</span>
  {load}
  <div style="position:absolute; left:470px; bottom:70px; display:grid; grid-template-columns:repeat(3,56px); gap:8px">{"".join(f'<div style="height:56px; background:{INK}"></div>' for _ in range(5))}</div>
</div>
<div style="{L}">
  {img('e22','position:absolute; inset:0; width:100%; height:100%')}
  {win(380,120,320,"Prompt 12 · Friends","Ask who I want to see more and what gets in the way. Help me write one if-then plan.")}
  {win(130,470,300,"Prompt 14 · Boundaries","Help me write a short, kind way to set a boundary. Then play them and give me feedback.")}
  {win(420,800,280,"issue11.app","Want your answers turned into a magazine about YOU? <b>Make your issue.</b>")}
</div>""")
# J · Colour page with star cut-outs, facing photo with colour stars (ref: editorial-12 "trust the process")
stars_l = "".join(f'<img src="{B(P["e24"])}" alt="" style="position:absolute; inset:0; width:816px; height:1056px; object-fit:cover; {F}; clip-path:{star(cx,cy,r)}">' for cx,cy,r in [(220,430,150),(500,700,210)])
stars_r = "".join(f'<div style="position:absolute; inset:0; background:{c}; clip-path:{star(cx,cy,r)}"></div>' for cx,cy,r,c in [(300,420,150,ROSE),(620,640,210,LILAC)])
C["CopyJ"] = ("Copy J · Star cut-outs", f"""
<div style="{L}; background:{ROSE}">
  {stars_l}
  <p style="position:absolute; right:56px; top:48px; margin:0; font-size:64px; {H}; color:#fff; text-align:right; opacity:0.85">glowing up</p>
  <p style="position:absolute; left:48px; bottom:48px; margin:0; font-size:64px; {H}; color:{INK}; opacity:0.85">on my terms</p>
</div>
<div style="{L}">
  {img('e24','position:absolute; inset:0; width:100%; height:100%')}
  {stars_r}
  <p style="position:absolute; left:56px; bottom:56px; margin:0; font-size:34px; {H}; color:#fff; line-height:0.9">become<br>YOU<br>again<br>and again</p>
  <p style="position:absolute; right:16px; top:60px; bottom:60px; margin:0; writing-mode:vertical-rl; {LBL}; font-size:8px; color:#fff">Chapter 05 · Beauty · The Rebrand Issue · issue11.app</p>
</div>""")
# K · Giant letters over text columns across the spread (ref: editorial-20 "WASHINGTON")
big = [("C",60,90),("I",380,90),("R",520,60),("C",880,230),("L",1130,230),("E",1320,480),("Y",130,610),("O",420,640),("U",1010,700)]
bl = "".join(f'<span style="position:absolute; left:{x}px; top:{y}px; font-size:330px; font-weight:600; letter-spacing:-0.06em; line-height:0.8; color:{INK}; mix-blend-mode:multiply">{c}</span>' for c,x,y in big)
C["CopyK"] = ("Copy K · Giant letters over text", f"""
<div style="{L}; background:#fff; padding:72px 64px 56px 72px">
  <div style="display:flex; justify-content:space-between; {LBL}; font-size:8px"><span>Chapter 04</span><span>The Rebrand Issue</span></div>
  <div style="margin-top:18px; columns:3; column-gap:18px; text-align:justify; hyphens:auto; font-size:10.5px; line-height:1.45">{prompts(INK)}{"".join(f"<p style='margin:0 0 8px'>{ESSAY}</p>" for _ in range(3))}</div>
</div>
<div style="{L}; background:#fff; padding:72px 72px 56px 88px">
  <div style="display:flex; justify-content:space-between; {LBL}; font-size:8px"><span>Love</span><span>11</span></div>
  <div style="margin-top:18px; columns:3; column-gap:18px; text-align:justify; hyphens:auto; font-size:10.5px; line-height:1.45">{"".join(f"<p style='margin:0 0 8px'>{ESSAY}</p>" for _ in range(5))}</div>
  {img('e37','position:absolute; right:72px; bottom:56px; width:200px; height:260px')}
</div>
{bl}""")
OUT = sys.argv[1]
for i,(k,(t,body)) in enumerate(C.items()):
    open(os.path.join(OUT, f"{k}.dc.html"),"w").write(page(k,t,body,10+i))
print("ok")
