import os, sys, json
R=sys.argv[1]
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"more2.py")).read().split("\nC={}")[0]
exec(src)
C={}
# Q · Stepped words on a white page facing a grid of small portraits (ref: board-02 "America in Transition")
steps=[("Future",72,170),("you,",250,330),("in",120,490),("progress.",300,650)]
st="".join(f'<span style="position:absolute; left:{x}px; top:{y}px; font-size:64px; {H}">{w}</span>' for w,x,y in steps)
order=["e36","e27","e22","e28","e24","e29","e31","e35","e32","e20","e14","e33"]
cells="".join(img(k,"width:100%; height:100%") for k in order)
C["CopyQ"]=("Copy Q · Stepped words + photo grid", f"""
<div style="{L}; background:#fff">
  <span style="position:absolute; left:72px; top:64px; {LBL}">The Rebrand Issue · My 2027</span>
  {st}
  <p style="position:absolute; left:72px; right:120px; bottom:72px; margin:0; font-size:11.5px; line-height:1.45; columns:2; column-gap:20px; text-align:justify">Twelve pictures, twelve versions of the same girl with bigger dreams. Pick the one that feels like next year, cut it out, and put it where you see it every morning. Then write one sentence under it in your own words.</p>
  <span style="position:absolute; left:72px; bottom:36px; {LBL}">04</span>
</div>
<div style="{L}; background:#fff; padding:64px 64px 64px 96px">
  <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); grid-template-rows:repeat(4, minmax(0,1fr)); gap:10px; height:100%">{cells}</div>
  <span style="position:absolute; right:64px; bottom:30px; {LBL}">05</span>
</div>""")
# R · Colour spread with headline + staggered photos and small text blocks (ref: board-02 pink "EKHO" spread)
ph=[("e31",72,210,230,290),("e24",340,330,200,250),("e36",110,560,260,330),("e20",880,120,240,300),("e29",1170,250,200,250),("e35",940,520,210,270),("e33",1230,600,250,330)]
phs="".join(img(k,f"position:absolute; left:{x}px; top:{y}px; width:{w}px; height:{h}px") for k,x,y,w,h in ph)
C["CopyR"]=("Copy R · Colour spread, staggered photos", f"""
<div style="position:absolute; inset:0; background:{LILAC}"></div>
<p style="position:absolute; left:72px; top:56px; margin:0; font-size:120px; {H}">Soft life, on purpose.</p>
{phs}
<p style="position:absolute; left:440px; top:640px; width:260px; margin:0; font-size:11.5px; line-height:1.45; text-align:justify">Soft life isn’t doing nothing. It’s choosing the slow morning, the calm money and the friends who feel like home, then protecting them.</p>
<p style="position:absolute; left:1180px; top:540px; writing-mode:vertical-rl; margin:0; {LBL}">Chapter 06 · Beauty · The Rebrand Issue</p>
<span style="position:absolute; left:72px; bottom:36px; {LBL}">14</span><span style="position:absolute; right:64px; bottom:36px; {LBL}">15 · issue11.app</span>""")
# S · Dense poster type filling a page, key words in colour, facing a full-bleed photo (ref: board-02 "Hidden Pictures" poster)
words="This is the year I stop waiting for January. I save the money, I book the trip, I keep my circle small, I say no kindly, I glow up slowly and on purpose, I ask for the raise, I post the work, I rest without guilt, I become my own dream girl, and I write it all down first.".split()
hi={"money,":ROSE,"trip,":PINKTXT,"small,":ROSE,"raise,":PINKTXT,"dream":ROSE,"girl,":ROSE,"down":PINKTXT}
ws=" ".join(f'<span style="color:{hi.get(w,INK)}">{w}</span>' for w in words)
C["CopyS"]=("Copy S · Poster type + full photo", f"""
<div style="{L}; background:#fff; padding:56px 56px 56px 64px">
  <p style="margin:0; font-size:66px; font-weight:600; letter-spacing:-0.07em; line-height:0.86">{ws}</p>
  <span style="position:absolute; left:64px; bottom:30px; {LBL}">16</span>
</div>
<div style="{L}">
  {img('e28','position:absolute; inset:0; width:100%; height:100%')}
  <span style="position:absolute; right:48px; bottom:30px; {LBL}; color:#fff">17 · issue11.app</span>
</div>""")
# T · Giant letters stacked down the page facing a full-bleed portrait (ref: board-02 "IRIS")
lt="".join(f'<span style="display:block; font-size:250px; font-weight:600; letter-spacing:-0.06em; line-height:0.78">{c}</span>' for c in "GLOW")
C["CopyT"]=("Copy T · Stacked letters + portrait", f"""
<div style="{L}; background:#F6F3EE; padding:40px 56px">
  <div style="position:absolute; left:56px; top:28px">{lt}</div>
  <div style="position:absolute; right:56px; bottom:72px; width:300px">
    <p style="margin:0 0 8px; {LBL}">Chapter 05 · Beauty</p>
    <p style="margin:0; font-size:22px; font-weight:500; letter-spacing:-0.04em; line-height:1.1">It’s giving future you. Five prompts for the inner and outer glow up.</p>
  </div>
  <span style="position:absolute; left:56px; bottom:30px; {LBL}">14</span>
</div>
<div style="{L}">
  {img('e24','position:absolute; inset:0; width:100%; height:100%')}
  <p style="position:absolute; left:40px; bottom:30px; margin:0; font-size:9px; letter-spacing:0.1em; color:#fff">Photograph · ISSUE11 archive · 15</p>
</div>""")
# U · Huge outlined type on a colour page, outlined type over a portrait + a bubble note (ref: editorial-15 "K-pop's new era of digital intimacy")
OUT=f"color:transparent; -webkit-text-stroke:3px {ICE}; font-weight:600; letter-spacing:-0.06em; line-height:0.84"
C["CopyU"]=("Copy U · Outlined type + bubble", f"""
<div style="{L}; background:{ROSE}">
  <p style="position:absolute; left:48px; right:40px; top:80px; margin:0; font-size:150px; {OUT}">My new era of soft power</p>
  <span style="position:absolute; left:48px; bottom:40px; {LBL}; color:#fff">Issue 2027 · The Rebrand Issue</span>
</div>
<div style="{L}; background:{INK}">
  {img('e35','position:absolute; inset:0; width:100%; height:100%')}
  <p style="position:absolute; left:40px; right:40px; top:60px; margin:0; font-size:150px; color:transparent; -webkit-text-stroke:3px {MINT}; font-weight:600; letter-spacing:-0.06em; line-height:0.84">become YOU</p>
  <div style="position:absolute; right:56px; top:560px; width:280px; padding:22px 26px; border-radius:60px; background:{MINT}">
    <p style="margin:0; font-size:13px; line-height:1.4; text-align:center">Soft power: knowing what you want, saying it out loud, and building it quietly. Your 2027 list starts on page 04.</p>
  </div>
  <span style="position:absolute; right:48px; bottom:30px; {LBL}; color:#fff">09</span>
</div>""")
for i,(k,(t,body)) in enumerate(C.items()):
    open(os.path.join(R,"project",f"{k}.dc.html"),"w").write(page(k,t,body,40+i))
c=json.load(open(os.path.join(R,"project","canvas.json")))
pos=[("CopyQ",0,12430,"Stepped words + photo grid"),("CopyR",1712,12430,"Colour spread, staggered photos"),("CopyS",3424,12430,"Poster type + full photo"),("CopyT",0,13673,"Stacked letters + portrait"),("CopyU",1712,13673,"Outlined type + bubble")]
for k,x,y,n in pos: c["boards"][k+".dc.html"]={"h":1056,"title":f"Inspo remake · {k[-1]} {n}","w":1632,"x":x,"y":y}
c["notes"]["more2"]={"kind":"title1","maxW":5056,"text":"Even more inspo remakes: Q–U","w":240,"x":0,"y":12210}
json.dump(c,open(os.path.join(R,"project","canvas.json"),"w"),ensure_ascii=False,indent=2)
print("ok")
