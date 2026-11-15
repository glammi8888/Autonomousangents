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
def notes(date, title, sections, footer, photo=None):
    n=sum(len(i)+1 for _,i in sections)
    fs=38 if n>=11 else (46 if n>=8 else 54)
    secs=""
    for h,items in sections:
        lis="".join(f'<div style="display:flex; gap:26px; margin:8px 0"><span>–</span><span>{t}</span></div>' for t in items)
        secs+=f'<p style="margin:{int(fs*0.9)}px 0 6px; font-weight:700; font-size:{fs+2}px">{h}</p><div style="padding-left:30px; font-size:{fs}px; line-height:1.3">{lis}</div>'
    return ("#000", f"""<div style="position:absolute; inset:0; padding:40px 64px; font-family:{SYS}, {EMO}; color:#fff">
  <div style="display:flex; justify-content:space-between; font-size:30px; font-weight:600"><span>10:19</span><span>●●● ◔</span></div>
  <div style="display:flex; justify-content:space-between; margin-top:30px"><span style="width:76px; height:76px; border-radius:50%; background:#1c1c1e; display:flex; align-items:center; justify-content:center; font-size:40px">‹</span><span style="height:76px; padding:0 30px; border-radius:40px; background:#1c1c1e; display:flex; align-items:center; font-size:34px">⤴ ⋯</span></div>
  <p style="margin:34px 0 0; text-align:center; font-size:28px; color:#8e8e93">{date}</p>
  <h1 style="margin:22px 0 0; font-size:{fs+34}px; font-weight:800; letter-spacing:-0.02em; line-height:1.05">{title}</h1>
  {img(photo,'margin-top:26px; width:100%; height:330px; border-radius:22px') if photo else ''}
  {secs}
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:30px 64px; background:#1c1c1e; display:flex; justify-content:space-between; align-items:center; color:#fff; font-family:{SYS}">
  <span style="font-size:30px; font-weight:600">{footer}</span>{logo(True)}
</div>""")
# --- Format 2: ✨ two-column checklist over a photo (top "glow up checklist" pin, 1,416 reactions)
def checklist(title, left, right, photo, footer):
    col=lambda xs: "".join(f'<p style="margin:0 0 10px; font-size:34px; font-weight:600; text-shadow:0 2px 10px rgba(0,0,0,0.55)">✨ {t}</p>' for t in xs)
    return (INK, f"""{img(photo,'position:absolute; inset:0; width:100%; height:100%; filter:brightness(0.62) contrast(1.05)')}
<h1 style="position:absolute; left:0; right:0; top:120px; margin:0; text-align:center; color:#fff; font-size:84px; font-weight:700; letter-spacing:-0.04em; text-shadow:0 2px 16px rgba(0,0,0,0.5)">{title}</h1>
<div style="position:absolute; left:110px; right:90px; top:280px; display:grid; grid-template-columns:1fr 1fr; gap:0 40px; color:#fff">{''.join(['<div>'+col(left)+'</div>','<div>'+col(right)+'</div>'])}</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:34px 64px; background:{ICE}; display:flex; justify-content:space-between; align-items:center"><span style="font-size:32px; font-weight:700">{footer}</span>{logo()}</div>""")
# --- Format 3: numbered cheat sheet (top "chatgpt prompts" pin, 1,875 reactions)
def cheatsheet(title, sub, items, cols=2, bg="#FFFFFF", fs=24, photo=None, photo_h=300):
    cells="".join(f'<div style="display:flex; gap:14px; padding:12px 0; border-bottom:1.5px dashed rgba(13,13,13,0.2)"><span style="flex:none; width:44px; height:44px; border-radius:50%; background:{LILAC}; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:22px">{n}</span><div><p style="margin:0; font-size:{fs+2}px; font-weight:700; color:{PINKTXT}; letter-spacing:-0.02em">{a}</p><p style="margin:2px 0 0; font-size:{fs-4}px; line-height:1.3">{b}</p></div></div>' for n,a,b in items)
    return (bg, f"""<div style="position:absolute; inset:0; padding:56px 56px 130px">
  {img(photo,'width:100%; height:'+str(photo_h)+'px; border-radius:18px; margin-bottom:26px') if photo else ''}
  <h1 style="margin:0; text-align:center; font-size:72px; font-weight:800; letter-spacing:-0.05em; line-height:0.95">{title}</h1>
  <p style="margin:14px 0 24px; text-align:center; font-size:28px; font-weight:500">{sub}</p>
  <div style="display:grid; grid-template-columns:repeat({cols}, minmax(0,1fr)); gap:0 32px; border-top:2px solid {INK}">{cells}</div>
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:30px 56px; background:{INK}; color:#fff; display:flex; justify-content:space-between; align-items:center"><span style="font-size:30px; font-weight:700">Free on issue11.app</span>{logo(True)}</div>""")
# --- Format 4: printable 30-day challenge grid (top "manifestation journal" format, 1,114 reactions)
def grid(title, days, bg):
    cells="".join(f'<div style="border:2px solid {INK}; padding:10px; min-height:150px; background:#fff"><p style="margin:0; font-size:22px; font-weight:800">{i+1}</p><p style="margin:6px 0 0; font-size:19px; line-height:1.25">{d}</p></div>' for i,d in enumerate(days))
    return (bg, f"""<div style="position:absolute; inset:0; padding:56px 50px 130px">
  <h1 style="margin:0 0 26px; text-align:center; font-size:66px; font-weight:800; letter-spacing:-0.05em; line-height:0.95">{title}</h1>
  <div style="display:grid; grid-template-columns:repeat(5, minmax(0,1fr)); gap:8px">{cells}</div>
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:30px 56px; background:{INK}; color:#fff; display:flex; justify-content:space-between; align-items:center"><span style="font-size:30px; font-weight:700">Printable + 30 prompts, free on issue11.app</span>{logo(True)}</div>""")
# --- Format 5: one-line type card (top "2027 vision board" pin, 1,219 reactions)
def typecard(line, sub, bg, col, photo=None):
    ph=img(photo,'position:absolute; left:0; right:0; top:0; width:100%; height:760px') if photo else ''
    top=820 if photo else 430
    return (bg, ph+f"""<p style="position:absolute; left:80px; right:80px; top:{top}px; margin:0; font-size:{110 if photo else 150}px; font-weight:700; letter-spacing:-0.06em; line-height:0.88; color:{col}">{line}</p>
<p style="position:absolute; left:80px; bottom:150px; margin:0; font-size:36px; font-weight:500; color:{col}">{sub}</p>
{logo(col=="#fff",'position:absolute; left:80px; bottom:70px')}""")
allp=[t for ch in chapters for t in ch[1]]
short=[(f"{i+1:02d}",p[0].rstrip('.'),p[2]) for i,p in enumerate(allp)]
days=["Write your 2027 list","Pick 1 glow up habit","5-min morning","Walk 20 min","Clear one drawer","Money date","Text a friend","Say no, kindly","Plan 1 outfit","Skincare + water","Rest day","Your rich af number","List your wins","Ask for more","Try a new class","Unfollow 10","Read 10 pages","Budget with fun","Cook something nice","Rest day","Letter from future you","1 brave email","Style 3 outfits","Early night","Savings goal per week","Call your mom/bestie","Glow up check-in","Reset your space","Rest day","Write your cover lines"]
P=[
 ("Pin01","How to rebrand yourself · Notes 'Project: Rebrand'", notes("November 14, 2026 at 23:11","Project: Rebrand 🎀🫧",[("Physical",["Get my dream bod (walks, Pilates)","5-minute glow up morning"]),("Mentally",["Protect my peace","Say no, kindly"]),("Money",["$20,000 saved"]),("Wardrobe",["Dress for the life I want"])],"30 ChatGPT prompts for each one · free kit")),
 ("Pin02","How to glow up in 2027 · Notes checklist", notes("November 14, 2026 at 07:42","My 2027 glow up ✨",[("Body",["Looking hotter, feeling better","A workout I actually like"]),("Mind",["Becoming me again","5 minutes, one thing"]),("Life",["Business popping OFF","Rebranding my entire life"])],"How to glow up: the free 2027 kit")),
 ("Pin03","Glow up checklist 2027 · ✨ list over photo", checklist("glow up checklist 2027",["5-min morning","dream bod walks","skincare","drink water","early nights","clean my space","new hair","protect my peace","journal"],["money date","savings goal","ask for more","say no kindly","small circle","style 3 outfits","read 10 pages","rest days","write your 2027"],"e21","Free 2027 Life Glow Up Kit →")),
 ("Pin04","ChatGPT prompts for self improvement · 30 cheat sheet", cheatsheet("30 ChatGPT prompts to glow up your whole life","Copy, paste, answer. Built on real behavior-change methods.",[(n,a,"") for n,a,_ in short],cols=2,fs=22)),
 ("Pin05","ChatGPT prompts for self improvement · 6 full prompts", cheatsheet("ChatGPT prompts for your 2027 rebrand","Copy + paste these. 30 more in the free kit.",[(f"{i+1:02d}",allp[j][0].rstrip('.'),allp[j][1][:150]+('…' if len(allp[j][1])>150 else '')) for i,j in enumerate([0,2,5,8,13,29])],cols=1,bg=ICE,fs=24,photo="e21",photo_h=380)),
 ("Pin06","Glow up tips · Notes 'the 2027 rebrand has begun'", notes("November 14, 2026 at 21:03","the 2027 rebrand has begun 🫧",[("glow up tips that actually work",["5 minutes, one thing (not a 90-day plan)","stack it on a habit you already have","plan for bad days: 2-minute version","change your space, not your willpower","say it out loud: I’m in my building era"])],"Glow up tips + 30 prompts · free")),
 ("Pin07","Self improvement plan 2027 · 30-day printable", grid("30-day self improvement plan for 2027",days,PEACH)),
 ("Pin08","Self improvement plan · type card", typecard("I’m not behind. I’m becoming.","A 30-day self improvement plan, 5 minutes a day. Free.",INK,"#fff","e29")),
 ("Pin09","How to rebrand yourself · Notes 'rebranding my entire life at 11pm'", notes("Thursday at 23:04","rebranding my entire life at 11pm 🎀",[("step 1",["write my 2027 list in my own words"]),("step 2",["paste one ChatGPT prompt per chapter"]),("step 3",["do one small thing this week"]),("step 4",["repeat. same girl, bigger dreams."])],"How to rebrand yourself · free kit")),
 ("Pin10","How to rebrand yourself · type card", typecard("Becoming me again, on purpose.","How to rebrand yourself in 2027: 30 prompts + a 30-day plan. Free.",LILAC,INK,"e22")),
 ("Pin11","Personal rebrand prompts · chapters cheat sheet", cheatsheet("Personal rebrand prompts by chapter","Physical · Money · Love · Fashion · Beauty · Finances",[(f"{i+1:02d}",ch[0].split('·')[0].strip()+": "+ch[0].split('·')[1].strip(),", ".join(p[0].rstrip('.') for p in ch[1][:3])) for i,ch in enumerate(chapters)],cols=1,bg="#fff",fs=26,photo="e22")),
 ("Pin12","My 2027 · approved Notes desire format", notes("January 1, 2027","Me 🫱🏻‍🫲🏽 2027",[("claim it",["✅ glowing up","✅ looking hotter","✅ rebranding my entire life","✅ business popping OFF","✅ $20,000 saved","✅ become my own dream girl"])],"write yours on issue11.app · free")),
 ("Pin13","Future self letter · journal page", ("#F6F3EE", img("e21","position:absolute; inset:0; width:100%; height:100%")+f"""<div style="position:absolute; inset:110px 90px 170px; background:#fff; box-shadow:0 6px 30px rgba(0,0,0,0.12); padding:60px 64px">
  <p style="margin:0; font-size:26px; letter-spacing:0.18em; text-transform:uppercase; color:{PINKTXT}; font-weight:600">A letter from future you</p>
  <p style="margin:28px 0 0; font-size:64px; font-weight:700; letter-spacing:-0.04em; line-height:1">It’s December 2027. Dear me,</p>
  {''.join('<div style="height:58px; border-bottom:2px solid rgba(13,13,13,0.25)"></div>' for _ in range(10))}
  <p style="margin:26px 0 0; text-align:right; font-size:40px; font-weight:600">Love, future you</p>
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:30px 60px; background:{INK}; color:#fff; display:flex; justify-content:space-between; align-items:center"><span style="font-size:30px; font-weight:700">Future self letter printable · free</span>{logo(True)}</div>""")),
 ("Pin14","Future self letter prompts · Notes", notes("November 14, 2026 at 22:30","letter to my future self ✍️",[("prompts",["What does my morning look like?","What did I stop apologizing for?","Who is in my circle now?","What am I proud of?","What would I tell 2026 me?"])],"Future self letter prompts · free kit")),
 ("Pin15","Lifemaxxing · Notes 'how to lifemaxx 2027'", notes("November 15, 2026 at 09:12","how to lifemaxx 2027 🫧",[("body",["walks + Pilates, dream bod energy","5-minute glow up morning"]),("money",["know my rich af number","$20,000 saved, on purpose"]),("life",["small circle, big plans","rebranding my entire life"])],"Lifemaxxing guide + 30 prompts · free")),
 ("Pin16","Lifemaxxing 101 · cheat sheet", cheatsheet("Lifemaxxing 101: your 2027 guide","One chapter at a time. Paste the prompt, do one small thing.",[(f"{i+1:02d}",ch[0].split('·')[0].strip()+"maxxing" if False else ch[0].split('·')[1].strip(),"Prompt: "+ch[1][0][0].rstrip('.')) for i,ch in enumerate(chapters)],cols=1,bg=LILAC,fs=28,photo="e22",photo_h=330)),
]
c=json.load(open(f"{R}/project/canvas.json"))
for i,(k,t,(bg,inner)) in enumerate(P):
    open(f"{R}/project/{k}.dc.html","w").write(doc(t,inner,bg))
    if f"{k}.dc.html" not in c["boards"]:
        c["boards"][f"{k}.dc.html"]={"x":(i%7)*1080,"y":3300+(i//7)*1620,"w":1000,"h":1500}
        c["order"].append(f"{k}.dc.html")
    c["boards"][f"{k}.dc.html"]["title"]=f"Pin batch 1 v2 · {t}"
c["notes"]["pins1"]["text"]="Pinterest batch 1 v2: viral formats (Notes, checklist, cheat sheet, printable, type card) → issue11.app/rebrand-kit"
json.dump(c,open(f"{R}/project/canvas.json","w"),ensure_ascii=False,indent=2)
print("ok")
