import os, sys, json
R=sys.argv[1]
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"more2.py")).read().split("\nC={}")[0]
exec(src)
C={}
# V · One name repeated in huge type on a colour page, facing a portrait with an ID-card list (ref: editorial-30 "Anya Taylor-Joy")
rep="".join(f'<p style="margin:0; white-space:nowrap; font-size:168px; font-weight:600; letter-spacing:-0.07em; line-height:0.84; color:#fff">Future you</p>' for _ in range(6))
idl=[("Name","Future you"),("Born","January 1, 2027"),("Lives","Her own studio, finally"),("Career","Business popping OFF"),("Savings","$20,000, on purpose"),("Circle","Small and loyal"),("Era","Building")]
ids="".join(f'<p style="margin:0 0 4px; font-size:13px; line-height:1.3"><b style="font-weight:600; color:{ROSE}">{a}:</b> {b}</p>' for a,b in idl)
C["CopyV"]=("Copy V · Repeated name + ID card", f"""
<div style="{L}; background:{ROSE}; padding:56px 0 0 30px">{rep}</div>
<div style="{L}; background:#fff">
  {img('e36','position:absolute; right:0; top:0; width:460px; height:100%')}
  <div style="position:absolute; left:80px; top:90px; width:270px">{ids}</div>
  <p style="position:absolute; left:80px; bottom:60px; margin:0; font-size:10px; color:#55524c">*Fill in yours on the My 2027 page.</p>
</div>""")
# W · White page with circular windows onto a photo + vertical numbers (ref: board-03 Maison Margiela die-cut cover)
circ=[(170,170,70),(470,140,55),(640,330,62),(260,400,80),(560,560,58),(150,690,66),(420,760,72),(680,820,50),(300,930,46)]
holes="".join(f'<img src="/_blob/{P["e24"]}" alt="" style="position:absolute; inset:0; width:{W}px; height:{Ht}px; object-fit:cover; {F}; clip-path:circle({r}px at {x}px {y}px)">' for x,y,r in circ)
rings="".join(f'<div style="position:absolute; left:{x-r}px; top:{y-r}px; width:{2*r}px; height:{2*r}px; border-radius:50%; box-shadow:inset 0 2px 8px rgba(0,0,0,0.25)"></div>' for x,y,r in circ)
C["CopyW"]=("Copy W · Circle windows", f"""
<div style="{L}; background:#F6F3EE">
  {holes}{rings}
  <p style="position:absolute; left:36px; top:120px; margin:0; writing-mode:vertical-rl; transform:rotate(180deg); {LBL}; letter-spacing:0.4em">01 02 03 04 05 06 07 08 09 10 11</p>
</div>
<div style="{L}; background:#F6F3EE; padding:96px 88px 56px 96px">
  <p style="margin:0; {LBL}; color:{PINKTXT}">Chapter 05 · Beauty</p>
  <h2 style="margin:18px 0 0; font-size:96px; {H}">Glowing up, one window at a time.</h2>
  <div style="margin-top:36px; columns:2; column-gap:24px; text-align:justify; hyphens:auto; font-size:12px; line-height:1.5">{para(2)}</div>
  <span style="position:absolute; right:64px; bottom:30px; {LBL}">15</span>
</div>""")
# X · Photo page, facing a white page with pinned paper notes, giant RECAP across the bottom (ref: board-03 "RECAP")
notes=[("first month of 2027",90,150,-3),("I said no, kindly. Twice.",330,260,2),("$____ saved so far",130,430,-2),("booked the trip",380,560,3)]
nt="".join(f'<div style="position:absolute; left:{x}px; top:{y}px; width:220px; padding:16px 18px; background:#fff; box-shadow:0 2px 10px rgba(0,0,0,0.12); transform:rotate({r}deg); font-size:16px; font-weight:500; letter-spacing:-0.02em"><span style="display:block; width:40px; height:10px; margin:-24px auto 8px; background:{MINT}; opacity:0.85"></span>{t}</div>' for t,x,y,r in notes)
C["CopyX"]=("Copy X · Recap notes", f"""
<div style="{L}">{img('e27','position:absolute; inset:0; width:100%; height:100%')}</div>
<div style="{L}; background:{ICE}">{nt}
  <span style="position:absolute; right:56px; top:56px; {LBL}">Your monthly recap</span>
</div>
<p style="position:absolute; left:30px; right:30px; bottom:20px; margin:0; font-size:280px; font-weight:600; letter-spacing:-0.07em; line-height:0.78; color:{INK}">Recap</p>""")
# Y · Vertical word in a colour band + photo stack, facing a full photo with a text column (ref: board-03 "BALENCIAGA")
C["CopyY"]=("Copy Y · Vertical word band", f"""
<div style="{L}; background:#fff; display:grid; grid-template-columns:130px minmax(0,1fr)">
  <div style="background:{LILAC}; display:flex; align-items:center; justify-content:center"><p style="margin:0; writing-mode:vertical-rl; transform:rotate(180deg); font-size:120px; font-weight:600; letter-spacing:-0.06em; line-height:0.8">Fashion</p></div>
  <div style="padding:40px 40px 40px 24px; display:grid; grid-template-rows:1.3fr 1fr; gap:14px">
    {img('e32','width:100%; height:100%')}
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px">{img('e33','width:100%; height:100%')}{img('e20','width:100%; height:100%')}</div>
  </div>
</div>
<div style="{L}">
  {img('e26','position:absolute; inset:0; width:100%; height:100%')}
  <div style="position:absolute; right:56px; top:80px; width:250px; padding:18px; background:{LILAC}">
    <p style="margin:0 0 8px; {LBL}">Dress for the life you want</p>
    <p style="margin:0; font-size:12px; line-height:1.45">Five prompts to build a wardrobe for the woman you’re becoming: what she wears to the meeting, the dinner and the Sunday reset.</p>
  </div>
  <span style="position:absolute; right:56px; bottom:30px; {LBL}; color:#fff">(13)</span>
</div>""")
# Z · Words stacked in ruled boxes over a narrow photo strip (ref: board-03 "AND IT'S NOT EVEN MY…")
wl=[("And","it’s"),("finally",""),("","my"),("year.","")]
rows="".join(f'<div style="display:flex; justify-content:space-between; border-bottom:2px solid {INK}; padding:6px 0; font-size:86px; font-weight:600; letter-spacing:-0.06em; line-height:0.9"><span>{a}</span><span>{b}</span></div>' for a,b in wl)
C["CopyZ"]=("Copy Z · Ruled word stack", f"""
<div style="{L}; background:#fff">
  {img('e29','position:absolute; left:0; top:0; width:100%; height:100%')}
</div>
<div style="{L}; background:#fff; padding:80px 72px 56px 96px">
  <div style="border-top:2px solid {INK}">{rows}</div>
  <div style="margin-top:36px; display:grid; grid-template-columns:200px minmax(0,1fr); gap:24px">
    {img('e31','width:200px; height:260px')}
    <div style="font-size:12px; line-height:1.5; text-align:justify">{para(1)}</div>
  </div>
  <span style="position:absolute; right:64px; bottom:30px; {LBL}">21 · issue11.app</span>
</div>""")
for i,(k,(t,body)) in enumerate(C.items()):
    open(os.path.join(R,"project",f"{k}.dc.html"),"w").write(page(k,t,body,60+i))
c=json.load(open(os.path.join(R,"project","canvas.json")))
pos=[("CopyV",3424,13673,"Repeated name + ID card"),("CopyW",0,14916,"Circle windows"),("CopyX",1712,14916,"Recap notes"),("CopyY",3424,14916,"Vertical word band"),("CopyZ",0,16159,"Ruled word stack")]
for k,x,y,n in pos:
    c["boards"][k+".dc.html"]={"h":1056,"title":f"Inspo remake · {k[-1]} {n}","w":1632,"x":x,"y":y}
    if k+".dc.html" not in c["order"]: c["order"].append(k+".dc.html")
c["notes"]["more3"]={"kind":"title1","maxW":5056,"text":"Inspo remakes V–Z (V is in the row above)","w":240,"x":0,"y":14696}
json.dump(c,open(os.path.join(R,"project","canvas.json"),"w"),ensure_ascii=False,indent=2)
print("ok")
