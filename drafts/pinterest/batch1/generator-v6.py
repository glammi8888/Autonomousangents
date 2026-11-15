import sys, json
R, PROMPTS = sys.argv[1], sys.argv[2]
chapters=json.load(open(PROMPTS))
B={"e21":"7c7c9f7639583c427c5ebf34599a953c","e22":"192e7090c0bebed08ef694877d2afefc","e28":"e16071495127e8ff2bdc00786c351184","e29":"3ffd68c0b9a6904c16daec8559ee45b3","e20":"e0b2acd5fe4e7845cf15c0a2d79a2367","e14":"a68b319ec36a835300c0e73bd8677e17","e36":"2d5be03e75abb367c4c478e5bf591d8b","e27":"9034e8205048f219499561307a1c9748","e24":"48584939a34a6e613eb4e2f11f2ad13e","e31":"a287df0304e9703741ce0c4247ef23f0","e35":"9ceda159e77c89d8a20b1bd3377080cd"}
LOGO="/_blob/d196614efc6265e2205729134fb523b8"
INK="#0D0D0D"; ICE="#EAF6FF"; LILAC="#D9B3FF"; PEACH="#FF9A7A"; MINT="#7DE3C7"; ROSE="#E84C7A"; PINKTXT="#C2207E"
SYS="-apple-system, 'SF Pro Text', 'Inter Tight', system-ui, sans-serif"
EMO="'Apple Color Emoji','Noto Color Emoji','Segoe UI Emoji'"
POS={"e21":"50% 72%","e22":"50% 62%","e28":"50% 38%","e29":"50% 8%","e36":"50% 20%","e27":"50% 25%","e24":"50% 35%","e31":"50% 30%","e35":"50% 30%","e20":"50% 50%","e14":"50% 40%"}
def img(k,st): return f'<img src="/_blob/{B[k]}" alt="Aspirational editorial photo" style="display:block; object-fit:cover; object-position:{POS.get(k,"50% 50%")}; {st}">'
def logo(white=False,st=""): return f'<img src="{LOGO}" alt="ISSUE11" style="height:40px; width:auto; {"filter:invert(1);" if white else ""} {st}">'
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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>body{{margin:0}}</style>
</helmet>
<div style="width:1000px; height:1500px; position:relative; overflow:hidden; background:{bg}; font-family:'Inter Tight', {EMO}, sans-serif; color:{INK}">
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
# --- Format 1: dark-mode iPhone Notes screenshot (top "how to rebrand yourself" pin, 3,905 reactions)
# ===== v5: photo-led, black & white high-contrast design, photos in colour (2 B&W for contrast) (Megan, Nov 15: "the other pins I want them more visual" + "keep a high contrast like black and white")
B["e34"]="841dd818467d3ee2d8ad91449d66fdc3"; POS["e34"]="50% 12%"; POS["e20"]="50% 55%"; POS["e24"]="50% 8%"; POS["e27"]="50% 20%"; POS["e31"]="60% 30%"
THUMB={"e29":"60% 15%","e24":"50% 5%","e34":"50% 8%","e28":"50% 30%","e31":"70% 35%","e22":"50% 60%"}
BW="filter:grayscale(1) contrast(1.18) brightness(0.96)"
W="#FFFFFF"
COL="filter:contrast(1.06) saturate(0.95)"
def ph(k,st,bw=False,pos=None):
    h=img(k, st+"; "+(BW if bw else COL))
    return h.replace(f"object-position:{POS.get(k,'50% 50%')}", f"object-position:{pos}") if pos else h
def foot(text, dark=True):
    bg,fg=(INK,W) if dark else (W,INK)
    return f'<div style="position:absolute; left:0; right:0; bottom:0; height:110px; padding:0 60px; box-sizing:border-box; background:{bg}; color:{fg}; display:flex; justify-content:space-between; align-items:center"><span style="font-size:30px; font-weight:700; letter-spacing:-0.02em">{text}</span>{logo(dark)}</div>'
def label(t,col=INK): return f'<p style="margin:0; font-size:20px; font-weight:600; letter-spacing:0.18em; text-transform:uppercase; color:{col}">{t}</p>'
chapters=json.load(open(PROMPTS))
allp=[t for ch in chapters for t in ch[1]]
CH=[ch[0].split('·')[0].strip() for ch in chapters]
SHORT=["Physical","Money","Love","Fashion","Beauty","Finances"]
CHPH=["e34","e29","e31","e22","e24","e28"]  # Visual QA: photo matches chapter (beauty≠money)

def p03():
    L=["pilates","hot girl walks","skincare","drink water","nails done","new hair","signature scent","early nights"]
    R=["no people-pleasing","unfollow the drama","save every month","ask for the raise","clean out closet","cute pajama sets","solo trip","minding business"]
    col=lambda xs:"".join(f'<p style="margin:0 0 14px; font-size:31px; font-weight:500; display:flex; gap:14px; align-items:center"><span style="flex:none; width:26px; height:26px; border:2.5px solid {INK}; border-radius:50%"></span>{t}</p>' for t in xs)
    return (W, ph("e20","position:absolute; left:0; top:0; width:1000px; height:700px")+
      f'<div style="position:absolute; left:0; top:0; width:1000px; height:700px; display:flex; align-items:flex-end; padding:0 60px 40px; box-sizing:border-box"><h1 style="margin:0; color:{W}; font-size:104px; font-weight:700; letter-spacing:-0.06em; line-height:0.86; text-shadow:0 2px 24px rgba(0,0,0,0.45)">glow up<br>checklist 2027</h1></div>'
      f'<div style="position:absolute; left:60px; right:60px; top:750px; display:grid; grid-template-columns:1fr 1fr; gap:0 40px">'+'<div>'+col(L)+'</div><div>'+col(R)+'</div></div>'+foot("Free 2027 Life Glow Up Kit →"))
def p04():
    tiles="".join(ph(k,"width:100%; height:500px") for k in ["e22","e28","e14","e29"])
    items="".join(f'<p style="margin:0; padding:11px 0; border-bottom:1.5px solid {INK}; font-size:27px; font-weight:500; display:flex; gap:14px"><b style="flex:none; width:42px">{i+1:02d}</b>{p[0].rstrip(".")}</p>' for i,p in enumerate(allp[:10]))
    return (W, f'<div style="position:absolute; left:0; top:0; width:1000px; height:500px; overflow:hidden; display:grid; grid-template-columns:repeat(4,1fr); gap:4px; background:{INK}">{tiles}</div>'
      f'<h1 style="position:absolute; left:60px; right:60px; top:540px; margin:0; font-size:78px; font-weight:700; letter-spacing:-0.06em; line-height:0.9">30 ChatGPT prompts to glow up your whole life</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:735px; display:grid; grid-template-columns:1fr 1fr; gap:0 36px; border-top:3px solid {INK}">{items}</div>'
      f'<p style="position:absolute; left:60px; top:1330px; margin:0; font-size:24px; font-weight:600">+ 20 more in the free kit</p>'+foot("Copy, paste, answer · free"))
def p05():
    sel=[0,5,13]
    rows="".join(f'<div style="padding:16px 0; border-top:2px solid {W}"><p style="margin:0; font-size:32px; font-weight:700">{i+1:02d} · {allp[j][0].rstrip(".")}</p><p style="margin:8px 0 0; font-size:26px; line-height:1.3; opacity:0.9">{allp[j][1][:110]+("…" if len(allp[j][1])>110 else "")}</p></div>' for i,j in enumerate(sel))
    return (INK, ph("e21","position:absolute; left:0; top:0; width:1000px; height:560px")+
      f'<div style="position:absolute; left:60px; right:60px; top:600px; color:{W}">{label("Copy + paste",W)}<h1 style="margin:12px 0 18px; font-size:66px; font-weight:700; letter-spacing:-0.06em; line-height:0.9">ChatGPT prompts for your 2027 rebrand</h1>{rows}</div>'+foot("30 prompts in the free kit",False))
def p07():
    strip="".join(ph(k,"width:100%; height:380px") for k in ["e20","e28","e24"])
    cells="".join(f'<div style="border:2px solid {INK}; margin:-1px 0 0 -1px; padding:8px 9px; height:120px; box-sizing:border-box; background:{W}"><p style="margin:0; font-size:22px; font-weight:800">{i+1}</p><p style="margin:3px 0 0; font-size:19.5px; line-height:1.15; font-weight:500">{d}</p></div>' for i,d in enumerate(days))
    return (W, f'<div style="position:absolute; left:0; top:0; width:1000px; height:380px; overflow:hidden; display:grid; grid-template-columns:repeat(3,1fr); gap:4px; background:{INK}">{strip}</div>'
      f'<h1 style="position:absolute; left:50px; right:50px; top:410px; margin:0; font-size:62px; font-weight:700; letter-spacing:-0.06em; line-height:0.9">30-day self improvement plan for 2027</h1>'
      f'<div style="position:absolute; left:50px; right:50px; top:550px; display:grid; grid-template-columns:repeat(5,1fr); padding:1px 0 0 1px">{cells}</div>'+foot("Printable + 30 prompts · free"))
def bigtype(k,line,sub,h=1010,bw=False):
    return (INK, ph(k,f"position:absolute; left:0; top:0; width:1000px; height:{h}px",bw)+
      f'<p style="position:absolute; left:60px; right:60px; top:{h+40}px; margin:0; color:{W}; font-size:100px; font-weight:700; letter-spacing:-0.06em; line-height:0.86">{line}</p>'
      f'<p style="position:absolute; left:60px; right:60px; bottom:150px; margin:0; color:{W}; font-size:28px; font-weight:500; opacity:0.85">{sub}</p>'+foot("issue11.app · free kit",False))
def p11():
    rows="".join(f'<div style="display:flex; gap:26px; align-items:center; padding:14px 0; border-top:2px solid {INK}">{ph(CHPH[i],"flex:none; width:150px; height:150px",pos=THUMB.get(CHPH[i]))}<div><p style="margin:0; font-size:20px; font-weight:600; letter-spacing:0.18em; text-transform:uppercase">{i+1:02d} · {CH[i]}</p><p style="margin:8px 0 0; font-size:27px; line-height:1.25">{", ".join(p[0].rstrip(".") for p in chapters[i][1][:2])}</p></div></div>' for i in range(6))
    return (W, f'<h1 style="position:absolute; left:60px; right:60px; top:56px; margin:0; font-size:74px; font-weight:700; letter-spacing:-0.06em; line-height:0.9">Personal rebrand prompts, chapter by chapter</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:250px">{rows}</div>'+foot("5 prompts per chapter · free"))
def p13():
    return (INK, ph("e22","position:absolute; inset:0; width:100%; height:100%")+f"""<div style="position:absolute; inset:150px 90px 250px; background:{W}; padding:60px 64px">
  {label("A letter from future you")}
  <p style="margin:26px 0 0; font-size:64px; font-weight:700; letter-spacing:-0.05em; line-height:1">It’s December 2027. Dear me,</p>
  {''.join(f'<div style="height:58px; border-bottom:2px solid {INK}"></div>' for _ in range(10))}
  <p style="margin:26px 0 0; text-align:right; font-size:40px; font-weight:600">Love, future you</p>
</div>"""+foot("Future self letter printable · free"))
def p16():
    tiles="".join(f'<div style="position:relative; height:470px">{ph(CHPH[i],"width:100%; height:100%")}<p style="position:absolute; left:0; bottom:0; margin:0; padding:10px 14px; background:{W}; font-size:22px; font-weight:700">{i+1:02d} {SHORT[i]}</p></div>' for i in range(6))
    return (INK, f'<h1 style="position:absolute; left:60px; right:60px; top:56px; margin:0; color:{W}; font-size:92px; font-weight:700; letter-spacing:-0.06em; line-height:0.86">Lifemaxxing 101: your 2027 guide</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:300px; display:grid; grid-template-columns:repeat(3,1fr); gap:10px">{tiles}</div>'
      f'<p style="position:absolute; left:60px; right:60px; top:1290px; margin:0; color:{W}; font-size:30px; line-height:1.35">One chapter at a time. Paste the prompt, answer it, do one small thing this week.</p>'+foot("Lifemaxxing guide + 30 prompts · free",False))
days=["Write your 2027 list","Pick 1 glow up habit","5-min morning","Walk 20 min","Clear one drawer","Money date","Text a friend","Say no, kindly","Plan 1 outfit","Skincare + water","Rest day","Your savings number","List your wins","Ask for more","Try a new class","Unfollow 10","Read 10 pages","Budget with fun","Cook something nice","Rest day","Letter from future you","1 brave email","Style 3 outfits","Early night","Weekly savings goal","Call your bestie","Glow up check-in","Reset your space","Rest day","Write your cover lines"]
P=[("Pin03","Glow up checklist 2027 · B&W photo",p03()),("Pin04","ChatGPT prompts for self improvement · B&W",p04()),("Pin05","ChatGPT prompts 2027 rebrand · B&W",p05()),
   ("Pin07","Self improvement plan 2027 · B&W printable",p07()),
   ("Pin08","Self improvement plan · B&W type card",bigtype("e27","I’m not behind. I’m becoming.","A 30-day self improvement plan, 5 minutes a day.",bw=True)),
   ("Pin10","How to rebrand yourself · B&W type card",bigtype("e22","Becoming me again, on purpose.","How to rebrand yourself in 2027: 30 prompts + a 30-day plan.")),
   ("Pin11","Personal rebrand prompts · B&W chapters",p11()),("Pin13","Future self letter · B&W",p13()),("Pin16","Lifemaxxing 101 · B&W",p16())]
def p18():
    tiles="".join(ph(k,"width:100%; height:520px") for k in ["e29","e27","e31"])
    rows=[("Palette","black, white, one chrome thing"),("Desk","clean. one candle. laptop open by 9"),("Uniform","3 work outfits i don’t have to think about"),("Mornings","coffee first, inbox after"),("Cast","people who clap when i win"),("Cut","anything that makes me feel small")]
    rr="".join(f'<div style="display:grid; grid-template-columns:200px 1fr; padding:18px 0; border-top:2px solid {INK}"><b style="font-size:20px; letter-spacing:0.18em; text-transform:uppercase; padding-top:5px">{a}</b><span style="font-size:32px; line-height:1.25">{b}</span></div>' for a,b in rows)
    return (W, f'<div style="position:absolute; left:0; top:0; width:1000px; height:520px; overflow:hidden; display:grid; grid-template-columns:repeat(3,1fr); gap:4px; background:{INK}">{tiles}</div>'
      f'<div style="position:absolute; left:60px; right:60px; top:560px">{label("Creative brief · 2027")}<h1 style="margin:12px 0 22px; font-size:84px; font-weight:700; letter-spacing:-0.06em; line-height:0.88">Art direct your life</h1>{rr}<p style="margin:26px 0 0; font-size:26px; font-weight:600">Write yours with 30 prompts in the free kit.</p></div>'+foot("Write your brief · free kit"))
P+=[("Pin17","Art director of my life · B&W type card",bigtype("e29","I’m the art director of my life.","Write the brief for your 2027: 30 prompts + a 30-day plan.",bw=True)),
    ("Pin18","Art direct your life · creative brief",p18())]
c=json.load(open(f"{R}/project/canvas.json"))
for k,t,(bg,inner) in P:
    open(f"{R}/project/{k}.dc.html","w").write(doc(t,inner,bg))
    if f"{k}.dc.html" not in c["boards"]:
        i=int(k[3:])-1
        c["boards"][f"{k}.dc.html"]={"x":(i%7)*1080,"y":3300+(i//7)*1620,"w":1000,"h":1500}
        c["order"].append(f"{k}.dc.html")
    c["boards"][f"{k}.dc.html"]["title"]=f"Pin batch 1 v6 · {t}"
json.dump(c,open(f"{R}/project/canvas.json","w"),ensure_ascii=False,indent=2)
print("ok")
