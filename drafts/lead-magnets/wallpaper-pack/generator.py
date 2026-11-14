import os, sys, json
R = sys.argv[1]
B = {"e36":"2d5be03e75abb367c4c478e5bf591d8b","e27":"9034e8205048f219499561307a1c9748","e22":"192e7090c0bebed08ef694877d2afefc","e28":"e16071495127e8ff2bdc00786c351184","e24":"48584939a34a6e613eb4e2f11f2ad13e","e29":"3ffd68c0b9a6904c16daec8559ee45b3","e31":"a287df0304e9703741ce0c4247ef23f0","e35":"9ceda159e77c89d8a20b1bd3377080cd","e32":"cb99732ab1173830889a973bed98a4ee"}
LOGO="/_blob/d196614efc6265e2205729134fb523b8"
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
H="font-weight:500; letter-spacing:-0.06em; line-height:0.88"
LBL="font-size:9px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase"
F="filter: contrast(1.04) saturate(0.9)"
def img(k, st): return f'<img src="/_blob/{B[k]}" alt="Aspirational editorial photo" style="display:block; object-fit:cover; {F}; {st}">'
def doc(title, w, h, inner, bg):
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
<div style="width:{w}px; height:{h}px; position:relative; overflow:hidden; background:{bg}; font-family:'Inter Tight', sans-serif; color:{INK}">
{inner}
<svg style="position:absolute; inset:0; width:100%; height:100%; pointer-events:none; mix-blend-mode:multiply; opacity:{{{{grain}}}}" aria-hidden="true"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"grain":{{"editor":"range","default":0.12,"min":0,"max":0.4,"step":0.02}},"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ grain: this.props.grain ?? 0.12 }};
  }}
}}
</script>
</body>
</html>
"""
mark = lambda c: f'<span style="position:absolute; left:0; right:0; bottom:34px; text-align:center; {LBL}; color:{c}">issue11.app</span>'
# Phone 390x844. Top ~300px stays calm for the lock-screen clock.
P = {}
P["Main"] = ("01 · My 2027: claim it", INK, f"""
{img('e36','position:absolute; inset:0; width:100%; height:100%')}
<p style="position:absolute; left:28px; right:28px; bottom:96px; margin:0; font-size:64px; {H}; color:#fff; text-shadow:0 2px 20px rgba(0,0,0,0.3)">My 2027:<br>claim it.</p>
{mark('#fff')}""")
P["BecomeYou"] = ("02 · Become YOU", LILAC, f"""
<div style="position:absolute; inset:18px; border:1.5px solid #fff"></div>
{img('e31','position:absolute; left:44px; top:300px; width:302px; height:380px')}
<p style="position:absolute; left:44px; bottom:84px; margin:0; font-size:58px; {H}">Become YOU.</p>
<p style="position:absolute; right:26px; top:300px; margin:0; writing-mode:vertical-rl; {LBL}; color:#fff">The Rebrand Issue · 2027</p>
{mark(INK)}""")
P["BuildingEra"] = ("03 · Building era", PEACH, f"""
<p style="position:absolute; left:28px; right:28px; top:300px; margin:0; font-size:76px; {H}">I’m in my building era.</p>
{img('e29','position:absolute; left:0; right:0; bottom:0; width:100%; height:330px')}
<span style="position:absolute; left:0; right:0; bottom:34px; text-align:center; {LBL}; color:#fff">issue11.app</span>""")
P["CalmMoney"] = ("04 · Money that feels calm", INK, f"""
{img('e28','position:absolute; inset:0; width:100%; height:100%')}
<p style="position:absolute; left:28px; right:28px; bottom:96px; margin:0; font-size:58px; {H}; color:#fff">Money that feels <span style="color:{LILAC}">calm.</span></p>
{mark('#fff')}""")
P["BiggerDreams"] = ("05 · Same girl, bigger dreams", "#fff", f"""
<span style="position:absolute; left:24px; top:300px; font-size:120px; {H}">Same</span>
<span style="position:absolute; left:120px; top:400px; font-size:120px; {H}">girl,</span>
<span style="position:absolute; left:24px; top:520px; font-size:120px; {H}; color:{PINKTXT}">bigger</span>
<span style="position:absolute; left:70px; top:620px; font-size:120px; {H}; color:{PINKTXT}">dreams.</span>
{img('e35','position:absolute; right:28px; top:250px; width:110px; height:140px')}
{mark(INK)}""")
P["FutureYou"] = ("06 · It's giving future you", ICE, f"""
{img('e24','position:absolute; left:0; right:0; top:260px; width:100%; height:420px')}
<p style="position:absolute; left:28px; right:28px; bottom:92px; margin:0; font-size:52px; {H}">It’s giving<br>future you.</p>
{mark(INK)}""")
P["BusinessOff"] = ("07 · Business popping OFF", MINT, f"""
<p style="position:absolute; left:16px; top:250px; bottom:60px; margin:0; writing-mode:vertical-rl; transform:rotate(180deg); font-size:110px; {H}">Business</p>
<p style="position:absolute; left:130px; top:250px; margin:0; font-size:46px; {H}">popping OFF.</p>
{img('e32','position:absolute; left:130px; right:28px; top:320px; width:232px; height:400px')}
{mark(INK)}""")
P["CircleSmall"] = ("08 · I keep my circle small", INK, f"""
{img('e22','position:absolute; inset:0; width:100%; height:100%')}
<p style="position:absolute; left:28px; right:28px; bottom:96px; margin:0; font-size:56px; {H}; color:#fff; text-shadow:0 2px 20px rgba(0,0,0,0.3)">I keep my circle small.</p>
{mark('#fff')}""")
# Laptop 1440x900
desires = ["Getting engaged","Being rich af","Business popping OFF","$20,000 saved","Become my own dream girl","Rebranding my entire life","Glowing up"]
lis = "".join(f'<div style="display:flex; align-items:center; gap:14px; padding:9px 0; border-bottom:1px solid rgba(13,13,13,0.15)"><span style="width:22px; height:22px; border-radius:6px; background:{ROSE}; color:#fff; font-size:14px; display:flex; align-items:center; justify-content:center">✓</span><span style="font-size:24px; font-weight:500; letter-spacing:-0.03em">{d}</span></div>' for d in desires)
P["LaptopList"] = ("09 · Laptop: My 2027 list", ICE, f"""
<div style="position:absolute; left:110px; top:120px; width:540px">
  <p style="margin:0; font-size:96px; {H}">My 2027:</p>
  <p style="margin:12px 0 22px; font-size:26px; font-weight:500; letter-spacing:-0.03em; color:{PINKTXT}">claim it</p>
  {lis}
</div>
{img('e27','position:absolute; right:110px; top:110px; width:520px; height:680px')}
<span style="position:absolute; left:110px; bottom:44px; {LBL}">write yours on issue11.app</span>""")
P["LaptopCover"] = ("10 · Laptop: Main story", "#fff", f"""
{img('e36','position:absolute; left:0; top:0; width:720px; height:900px')}
<div style="position:absolute; left:720px; top:0; right:0; bottom:0; background:{LILAC}"></div>
<img src="{LOGO}" alt="ISSUE11" style="position:absolute; left:800px; top:90px; height:70px">
<p style="position:absolute; left:800px; right:90px; top:330px; margin:0; font-size:104px; {H}">You’re the main story.</p>
<span style="position:absolute; left:800px; bottom:60px; {LBL}">issue11.app</span>""")
boards, order = {}, []
x = 0
for i,(k,(t,bg,inner)) in enumerate(P.items()):
    laptop = k.startswith("Laptop")
    w,h = (1440,900) if laptop else (390,844)
    if laptop:
        bx = 0 if k=="LaptopList" else 1520; by = 1064
    else:
        bx = i*470; by = 0
    open(f"{R}/project/{k}.dc.html","w").write(doc(t,w,h,inner,bg))
    boards[f"{k}.dc.html"] = {"x":bx,"y":by,"w":w,"h":h,"title":t}
    order.append(f"{k}.dc.html")
canvas = {"v":3,"createdOnFiles":{"v":1,"at":"2026-11-14T08:00:00Z"},"title":"ISSUE11 Lead Magnets","launch":{"view":"canvas"},"pages":[],
 "boards":boards,"order":order,"designSystems":[],
 "notes":{"wp":{"kind":"title1","x":0,"y":-260,"maxW":3680,"text":"2027 Manifestation Wallpaper Pack (phone + laptop)"}}}
json.dump(canvas, open(f"{R}/project/canvas.json","w"), ensure_ascii=False, indent=2)
print("ok")
