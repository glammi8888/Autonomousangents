import os, sys, json
R=sys.argv[1]
B={"e36":"2d5be03e75abb367c4c478e5bf591d8b","e27":"9034e8205048f219499561307a1c9748","e22":"192e7090c0bebed08ef694877d2afefc","e28":"e16071495127e8ff2bdc00786c351184","e24":"48584939a34a6e613eb4e2f11f2ad13e","e29":"3ffd68c0b9a6904c16daec8559ee45b3","e31":"a287df0304e9703741ce0c4247ef23f0","e35":"9ceda159e77c89d8a20b1bd3377080cd","e32":"cb99732ab1173830889a973bed98a4ee"}
LOGO="/_blob/d196614efc6265e2205729134fb523b8"
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
H="font-weight:500; letter-spacing:-0.06em; line-height:0.92"
LBL="font-size:10px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase"
BTN=f"display:block; width:100%; box-sizing:border-box; min-height:52px; border:0; border-radius:999px; background:{INK}; color:#fff; font:600 16px 'Inter Tight', sans-serif; text-align:center; text-decoration:none; padding:16px"
def img(k,st): return f'<img src="/_blob/{B[k]}" alt="Aspirational editorial photo" style="display:block; object-fit:cover; filter:contrast(1.04) saturate(0.9); {st}">'
def shell(title, step, inner, nxt=None, btn="Next"):
    dots="".join(f'<span style="width:{22 if i==step else 8}px; height:8px; border-radius:99px; background:{INK if i<=step else "rgba(13,13,13,0.2)"}"></span>' for i in range(1,5))
    foot=f'<a href="{nxt}" style="{BTN}">{btn}</a>' if nxt else ""
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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>body{{margin:0}}</style>
</helmet>
<div style="width:390px; height:844px; box-sizing:border-box; padding:22px 22px 28px; background:#FFFFFF; font-family:'Inter Tight', sans-serif; color:{INK}; display:flex; flex-direction:column; gap:18px; overflow:hidden">
  <div style="display:flex; justify-content:space-between; align-items:center"><img src="{LOGO}" alt="ISSUE11" style="height:22px; width:auto"><div style="display:flex; gap:5px; align-items:center">{dots}</div></div>
  {inner}
  <div style="margin-top:auto">{foot}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":844}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
"""
S={}
chips=["$20,000 saved","Business popping OFF","Getting engaged","Glowing up","Become my own dream girl","Rebranding my entire life"]
FONT13="font:500 13px 'Inter Tight', sans-serif"
ch="".join(f'<button type="button" style="border:1px solid {INK}; background:#fff; border-radius:999px; padding:8px 12px; {FONT13}; color:{INK}">+ {c}</button>' for c in chips)
FONT17="font:500 17px 'Inter Tight', sans-serif"
def goal(i,v):
    bg=ROSE if i<2 else "#fff"
    return f'<div style="display:flex; align-items:center; gap:10px; border-bottom:1px solid rgba(13,13,13,0.25); padding:8px 0"><span style="width:18px; height:18px; border-radius:5px; background:{bg}; border:1.5px solid {ROSE}; flex:none"></span><label for="g{i}" style="position:absolute; left:-9999px">Goal {i+1}</label><input id="g{i}" type="text" value="{v}" placeholder="Write it in your words" style="flex:1; border:0; outline:0; {FONT17}; letter-spacing:-0.02em; color:{INK}; background:transparent"></div>'
lines="".join(goal(i,v) for i,v in enumerate(["Being rich af","My own studio by summer","","",""]))
S["GenWrite"]=("Generator 1 · Write your 2027",1,f"""
  <div><p style="margin:0; {LBL}; color:{PINKTXT}">Free · 2027 wallpaper maker</p>
  <h1 style="margin:10px 0 0; font-size:48px; {H}">My 2027:<br>claim it.</h1>
  <p style="margin:10px 0 0; font-size:14px; line-height:1.45">Write 3 to 7 things you want in 2027, in your own words. They stay on your phone. We add the ISSUE11 logo.</p></div>
  <div style="display:flex; flex-direction:column">{lines}</div>
  <div style="display:flex; flex-wrap:wrap; gap:8px">{ch}</div>""","GenVibe.dc.html")
looks=[("Full photo","e36"),("Framed","e31"),("Scattered words",None),("List","e27")]
cols=[INK,LILAC,ICE,PEACH,MINT]
FONT600="font:600 13px 'Inter Tight', sans-serif"
def look(i,n,k):
    border=("2.5px solid "+INK) if i==1 else "1px solid rgba(13,13,13,0.2)"
    bg=LILAC if i==1 else "#fff"
    inner=img(k,"width:100%; height:100%") if k else f'<p style="margin:0; padding:16px; font-size:24px; {H}; color:{PINKTXT}">Being<br>rich af,<br>on purpose</p>'
    return f'<button type="button" aria-pressed="{str(i==1).lower()}" style="padding:0; border:{border}; border-radius:12px; overflow:hidden; background:{bg}; text-align:left"><div style="height:170px; position:relative">{inner}</div><span style="display:block; padding:8px 10px; {FONT600}">{n}</span></button>'
lk="".join(look(i,n,k) for i,(n,k) in enumerate(looks))
def col(i,c):
    border=("3px solid "+INK) if i==1 else "1px solid rgba(13,13,13,0.2)"
    return f'<button type="button" aria-label="Colour {c}" style="width:44px; height:44px; border-radius:50%; background:{c}; border:{border}"></button>'
cl="".join(col(i,c) for i,c in enumerate(cols))
S["GenVibe"]=("Generator 2 · Pick your vibe",2,f"""
  <h1 style="margin:0; font-size:40px; {H}">Pick your vibe.</h1>
  <div style="display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:10px">{lk}</div>
  <div><p style="margin:0 0 10px; {LBL}">Colour</p><div style="display:flex; gap:12px">{cl}</div></div>""","GenImages.dc.html")
lib=["e36","e27","e22","e28","e24","e29","e31","e35","e32"]
def tile(i,k):
    tick=f'<span style="position:absolute; right:6px; top:6px; width:22px; height:22px; border-radius:50%; background:{ROSE}; color:#fff; font-size:13px; display:flex; align-items:center; justify-content:center">✓</span>' if i in (0,4) else ""
    return f'<button type="button" aria-pressed="{str(i in (0,4)).lower()}" style="padding:0; border:0; position:relative; border-radius:8px; overflow:hidden; height:104px">{img(k,"width:100%; height:100%")}{tick}</button>'
grid="".join(tile(i,k) for i,k in enumerate(lib))
S["GenImages"]=("Generator 3 · Pick your images",3,f"""
  <h1 style="margin:0; font-size:40px; {H}">Pick your images.</h1>
  <label for="up" style="display:flex; align-items:center; justify-content:center; gap:8px; min-height:52px; border:1.5px dashed {INK}; border-radius:14px; font:600 15px 'Inter Tight', sans-serif; background:{ICE}">+ Add your own photos<input id="up" type="file" accept="image/*" multiple style="position:absolute; left:-9999px"></label>
  <p style="margin:-8px 0 0; font-size:12px; color:#55524c">Your photos never leave your phone.</p>
  <p style="margin:0; {LBL}">Or pick from our library</p>
  <div style="display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:6px">{grid}</div>""","GenPreview.dc.html")
S["GenPreview"]=("Generator 4 · Preview + download",4,f"""
  <h1 style="margin:0; font-size:36px; {H}">Your 2027, ready.</h1>
  <div style="display:flex; gap:10px; align-items:flex-end; justify-content:center">
    <div style="width:150px; height:310px; border-radius:22px; overflow:hidden; position:relative; background:{LILAC}; border:3px solid {INK}">
      <div style="position:absolute; inset:8px; border:1px solid #fff"></div>
      {img('e36','position:absolute; left:18px; right:18px; top:92px; width:114px; height:130px')}
      <p style="position:absolute; left:18px; bottom:26px; margin:0; font-size:16px; {H}">Being rich af.<br>My own studio.</p>
      <img src="{LOGO}" alt="ISSUE11" style="position:absolute; left:50%; bottom:7px; transform:translateX(-50%); height:9px; width:auto">
    </div>
    <div style="width:170px; height:110px; border-radius:8px; overflow:hidden; position:relative; background:{LILAC}; border:3px solid {INK}">
      {img('e24','position:absolute; right:0; top:0; width:80px; height:100%')}
      <p style="position:absolute; left:10px; top:14px; margin:0; font-size:13px; {H}">My 2027:<br>claim it.</p>
      <img src="{LOGO}" alt="ISSUE11" style="position:absolute; left:10px; bottom:8px; height:8px; width:auto">
    </div>
  </div>
  <div style="display:flex; flex-direction:column; gap:8px">
    <label for="em" style="{LBL}">Email (we send your wallpapers too)</label>
    <input id="em" type="email" placeholder="you@email.com" style="min-height:48px; box-sizing:border-box; border:1.5px solid {INK}; border-radius:12px; padding:0 14px; font:500 16px 'Inter Tight', sans-serif">
    <label style="display:flex; gap:10px; align-items:flex-start; font-size:13px; line-height:1.35"><input type="checkbox" style="width:20px; height:20px; margin:0"> Yes, send me the ISSUE11 newsletter too (optional)</label>
  </div>""","GenDone.dc.html","Download my wallpapers")
S["GenDone"]=("Generator 5 · Thank you",4,f"""
  <div style="height:300px; border-radius:16px; overflow:hidden">{img('e35','width:100%; height:100%')}</div>
  <h1 style="margin:0; font-size:40px; {H}">Saved to your phone.</h1>
  <p style="margin:0; font-size:15px; line-height:1.45">Set it as your lock screen and say hi to future you every morning.</p>
  <div style="padding:16px; border-radius:14px; background:{ICE}">
    <p style="margin:0; font-size:20px; font-weight:600; letter-spacing:-0.04em; line-height:1.1">Want your answers turned into a magazine about YOU?</p>
    <p style="margin:6px 0 0; font-size:13px; line-height:1.4">ISSUE11 is the manifestation journal that feels like a magazine.</p>
  </div>""","GenWrite.dc.html","Join the waitlist")
c=json.load(open(f"{R}/project/canvas.json"))
for i,(k,(t,step,inner,nxt,*b)) in enumerate(S.items()):
    open(f"{R}/project/{k}.dc.html","w").write(shell(t,step,inner,nxt,*(b or ["Next"])))
    c["boards"][f"{k}.dc.html"]={"x":i*470,"y":2184,"w":390,"h":844,"title":t,"is_interactive":True}
    c["order"].append(f"{k}.dc.html")
c["notes"]["gen"]={"kind":"title1","x":0,"y":1964,"maxW":2300,"text":"Free wallpaper maker: screens (logic OK'd by Megan Nov 14)"}
json.dump(c,open(f"{R}/project/canvas.json","w"),ensure_ascii=False,indent=2)
print("ok")
