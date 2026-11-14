import sys, json
R=sys.argv[1]
B={"e36":"2d5be03e75abb367c4c478e5bf591d8b","e27":"9034e8205048f219499561307a1c9748","e22":"192e7090c0bebed08ef694877d2afefc","e28":"e16071495127e8ff2bdc00786c351184","e24":"48584939a34a6e613eb4e2f11f2ad13e","e29":"3ffd68c0b9a6904c16daec8559ee45b3","e31":"a287df0304e9703741ce0c4247ef23f0","e35":"9ceda159e77c89d8a20b1bd3377080cd","e32":"cb99732ab1173830889a973bed98a4ee"}
LOGO="/_blob/d196614efc6265e2205729134fb523b8"
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
H="font-weight:600; letter-spacing:-0.06em; line-height:0.9"
LBL="font-size:20px; font-weight:600; letter-spacing:0.16em; text-transform:uppercase"
def img(k,st): return f'<img src="/_blob/{B[k]}" alt="Aspirational editorial photo" style="display:block; object-fit:cover; filter:contrast(1.04) saturate(0.9); {st}">'
def logo(white=False,st=""): return f'<img src="{LOGO}" alt="ISSUE11" style="height:44px; width:auto; {"filter:invert(1);" if white else ""} {st}">'
def doc(title, inner, bg):
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
<div style="width:1000px; height:1500px; position:relative; overflow:hidden; background:{bg}; font-family:'Inter Tight', sans-serif; color:{INK}">
{inner}
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
def cover(title, sub, photo):
    return (INK, f"""{img(photo,'position:absolute; inset:0; width:100%; height:100%')}
<p style="position:absolute; left:64px; top:64px; margin:0; {LBL}; color:#fff">Free 2027 Life Glow Up Kit</p>
<h1 style="position:absolute; left:64px; right:64px; top:120px; margin:0; font-size:118px; {H}; color:#fff; text-shadow:0 2px 28px rgba(0,0,0,0.45)">{title}</h1>
<div style="position:absolute; left:0; right:0; bottom:0; padding:40px 64px; background:{ICE}; display:flex; justify-content:space-between; align-items:center">
  <div><p style="margin:0; font-size:34px; font-weight:600; letter-spacing:-0.03em">{sub}</p><p style="margin:8px 0 0; font-size:26px">Free at issue11.app/rebrand-kit</p></div>{logo()}
</div>""")
def notes(title, items, bg=ICE):
    lis="".join(f'<div style="display:flex; align-items:center; gap:22px; padding:22px 0; border-bottom:2px solid rgba(13,13,13,0.12)"><span style="width:44px; height:44px; border-radius:12px; background:{ROSE}; color:#fff; font-size:28px; display:flex; align-items:center; justify-content:center; flex:none">✓</span><span style="font-size:40px; font-weight:500; letter-spacing:-0.03em">{t}</span></div>' for t in items)
    return ("#fff", f"""<div style="position:absolute; inset:0; padding:80px 72px">
  <p style="margin:0; {LBL}; color:{PINKTXT}">Free 2027 Life Glow Up Kit</p>
  <h1 style="margin:24px 0 36px; font-size:96px; {H}">{title}</h1>
  {lis}
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:44px 72px; background:{LILAC}; display:flex; justify-content:space-between; align-items:center"><p style="margin:0; font-size:34px; font-weight:600; letter-spacing:-0.03em">Get yours free on issue11.app</p>{logo()}</div>""")
def split(title, sub, photo, col):
    return (col, f"""<div style="position:absolute; left:0; right:0; top:0; height:640px; padding:72px 64px; box-sizing:border-box">
  <p style="margin:0; {LBL}">Free 2027 Life Glow Up Kit</p>
  <h1 style="margin:22px 0 0; font-size:104px; {H}">{title}</h1>
</div>
{img(photo,'position:absolute; left:0; right:0; bottom:0; width:100%; height:860px')}
<div style="position:absolute; left:64px; bottom:64px; padding:20px 28px; border-radius:999px; background:{INK}; color:#fff; font-size:30px; font-weight:600">{sub} → issue11.app</div>
{logo(True,'position:absolute; right:64px; bottom:76px')}""")
P=[
 ("Pin01","How to glow up in 2027 · photo", cover("How to glow up in 2027","30 ChatGPT prompts + a 30-day challenge","e24")),
 ("Pin02","How to glow up in 2027 · notes", notes("How to glow up in 2027",["My 5-minute glow up morning","A workout I actually like","Walk in like the cover star","Money that feels calm","Dress for the life you want"])),
 ("Pin03","Glow up tips · split", split("Glow up tips you’ll actually use","Free kit","e35",PEACH)),
 ("Pin04","Glow up tips · notes", notes("Glow up tips for 2027",["Start with 5 minutes, not 5 hours","Change your space, not your willpower","Plan for bad days","Say no, kindly","Write it down first"],LILAC)),
 ("Pin05","ChatGPT prompts for self improvement · photo", cover("30 ChatGPT prompts for self improvement","Copy, paste, become YOU","e31")),
 ("Pin06","ChatGPT prompts for self improvement · notes", notes("ChatGPT prompts for self improvement",["“Interview me, one question at a time…”","“Help me pick 3 priorities for 2027”","“Write me a kind if-then plan”","“Turn my goal into a weekly number”","“Write 5 cover lines for my 2027”"])),
 ("Pin07","Self improvement plan 2027 · split", split("Your 2027 self improvement plan","30-day challenge","e29",MINT)),
 ("Pin08","Self improvement plan 2027 · photo", cover("A self improvement plan for 2027","One small thing a day, for 30 days","e36")),
 ("Pin09","How to rebrand yourself · photo", cover("How to rebrand yourself in 2027","Same girl, bigger dreams","e28")),
 ("Pin10","How to rebrand yourself · split", split("How to rebrand your whole life","Start today","e32",LILAC)),
 ("Pin11","Personal rebrand prompts · notes", notes("Personal rebrand prompts",["Physical: looking hotter, feeling better","Money: business popping OFF","Love: my people, my circle","Fashion: dress for the life you want","Finances: $20,000 saved"])),
 ("Pin12","Personal rebrand prompts · photo", cover("Personal rebrand prompts for 2027","30 prompts in 6 chapters","e27")),
 ("Pin13","Future self letter · split", split("Write a letter from future you","Free printable","e22",ICE)),
 ("Pin14","Future self letter · notes", notes("Future self letter prompts",["It’s December 2027. Dear me…","What does my morning look like?","What did I stop apologizing for?","Who is in my circle?","Love, future you"],PEACH)),
]
c=json.load(open(f"{R}/project/canvas.json"))
for i,(k,t,(bg,inner)) in enumerate(P):
    open(f"{R}/project/{k}.dc.html","w").write(doc(t,inner,bg))
    c["boards"][f"{k}.dc.html"]={"x":(i%7)*1080,"y":3300+(i//7)*1620,"w":1000,"h":1500,"title":f"Pin batch 1 · {t}"}
    if f"{k}.dc.html" not in c["order"]: c["order"].append(f"{k}.dc.html")
c["notes"]["pins1"]={"kind":"title1","x":0,"y":3080,"maxW":7480,"text":"Pinterest batch 1 (14 pins → issue11.app/rebrand-kit) · for Megan's review"}
json.dump(c,open(f"{R}/project/canvas.json","w"),ensure_ascii=False,indent=2)
print("ok")
