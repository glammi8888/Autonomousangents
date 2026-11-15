# Pinterest batch 2 (Nov 15, 2026): vision board collages, text-only pins, Notes pins.
# Usage: python3 generator-b2.py <out_root>   -> writes <out_root>/project/Pin19..Pin28.dc.html
# Reuses batch1 doc() shell and the approved notes() template (generator.py) incl. the white CTA bar.
import sys, os
R = sys.argv[1]  # scratch folder; copy project/Pin*.dc.html next to this file after a run
os.makedirs(f"{R}/project", exist_ok=True)
B = {"e20":"e0b2acd5fe4e7845cf15c0a2d79a2367","e21":"7c7c9f7639583c427c5ebf34599a953c","e22":"192e7090c0bebed08ef694877d2afefc",
     "e24":"48584939a34a6e613eb4e2f11f2ad13e","e27":"9034e8205048f219499561307a1c9748","e28":"e16071495127e8ff2bdc00786c351184",
     "e29":"3ffd68c0b9a6904c16daec8559ee45b3","e31":"a287df0304e9703741ce0c4247ef23f0","e34":"841dd818467d3ee2d8ad91449d66fdc3",
     "e35":"9ceda159e77c89d8a20b1bd3377080cd","e36":"2d5be03e75abb367c4c478e5bf591d8b",
     "l19":"7ab58c9e707b37ca7f8fb64c351c8287","l20":"73cb8b35f0722c3b2b27876f327172ba","l22":"25cc887437020aebe48755e2332924cf","l23":"f9aebbe835f6f14787a79bcfba5c4f11",
     "m24":"96e935322d947be7c76bdde2bb71f084","m25":"d155e88a421b7a2d7b2c4d747e511273","m26":"a9ca26df86b2661f5b04462f82740107",
     "m27":"717f342673f84bafdb03515ab886308a","m28":"1c5357936c0f3bb41b01c25d9f8b01a9",
     "n14":"742bb7df3d5aa3d310907070916b8a30","n16":"233e3c8b1372ede1ef7ecb0663429ac7","n17":"61c13ba5e0a9205473641aaca015e7c7","n18":"4104fae58009e60889f79ebf1c2348da"}
# Focal points (object-position) per photo so faces stay in frame in small/square tiles.
POS = {"e20":"50% 55%","e21":"50% 60%","e22":"50% 60%","e24":"50% 12%","e27":"50% 20%","e28":"50% 0%","e29":"55% 15%","e31":"65% 30%",
       "e34":"50% 10%","e35":"50% 25%","e36":"50% 15%","l19":"50% 0%","l20":"50% 10%","l22":"50% 10%","l23":"50% 15%",
       "m24":"50% 45%","m25":"50% 20%","m26":"55% 25%","m27":"50% 35%","m28":"40% 30%","n14":"50% 22%","n16":"50% 22%","n17":"50% 15%","n18":"50% 20%"}
LOGO = "/_blob/d196614efc6265e2205729134fb523b8"
INK = "#0D0D0D"; W = "#FFFFFF"
SYS = "-apple-system, 'SF Pro Text', 'Inter Tight', system-ui, sans-serif"
EMO = "'Apple Color Emoji','Noto Color Emoji','Segoe UI Emoji'"
COL = "filter:contrast(1.06) saturate(0.95)"   # colour photos only (Megan: "no images in black and white")
def ph(k, st, pos=None):
    return f'<img src="/_blob/{B[k]}" alt="Editorial photo" style="display:block; object-fit:cover; object-position:{pos or POS[k]}; {COL}; {st}">'
def logo(white=False, st=""): return f'<img src="{LOGO}" alt="ISSUE11" style="height:40px; width:auto; {"filter:invert(1);" if white else ""} {st}">'
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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
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
def foot(text, dark=True):
    bg, fg = (INK, W) if dark else (W, INK)
    return f'<div style="position:absolute; left:0; right:0; bottom:0; height:120px; padding:0 60px; box-sizing:border-box; background:{bg}; color:{fg}; display:flex; justify-content:space-between; align-items:center"><span style="font-size:34px; font-weight:700; letter-spacing:-0.02em">{text}</span>{logo(dark)}</div>'
def cap(t, dark=False):
    bg, fg = (INK, W) if dark else (W, INK)
    return f'<p style="position:absolute; left:0; bottom:0; margin:0; padding:8px 14px; background:{bg}; color:{fg}; font-size:28px; font-weight:700; letter-spacing:-0.01em">{t}</p>'
def tile(k, label=None, pos=None):
    return f'<div style="position:relative; overflow:hidden">{ph(k,"width:100%; height:100%",pos)}{cap(label) if label else ""}</div>'

# ---------- 4 vision board collages (clean grid, no rotation/tape/stickers) ----------
def p19():  # "2027 vision board ideas": white, 3x3 grid with captions
    t = [("e20","dream closet"),("m27","money"),("l19","date nights"),("n16","city nights"),("e27","my own desk"),
         ("n18","shopping day"),("l23","love"),("m25","savings"),("e22","the walk-in")]
    g = "".join(tile(k,c) for k,c in t)
    return (W, f'<h1 style="position:absolute; left:56px; right:56px; top:48px; margin:0; font-size:112px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">2027 vision<br>board ideas</h1>'
      f'<div style="position:absolute; left:56px; right:56px; top:300px; height:900px; display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(3,1fr); gap:8px; background:{INK}; border:8px solid {INK}">{g}</div>'
      f'<p style="position:absolute; left:56px; right:56px; top:1240px; margin:0; font-size:36px; font-weight:600; line-height:1.2">closet, money, love, style, work. pin the pics, then write the list.</p>'
      + foot("Free 2027 list page · issue11.app"))
def p20():  # "vision board 2027": black, 2x3 tall photos
    t = ["e21","n16","l22","m26","e27","e31"]
    g = "".join(tile(k) for k in t)
    return (INK, f'<h1 style="position:absolute; left:56px; right:56px; top:48px; margin:0; color:{W}; font-size:128px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">vision board<br>2027</h1>'
      f'<div style="position:absolute; left:56px; right:56px; top:330px; height:900px; display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(2,1fr); gap:10px">{g}</div>'
      f'<p style="position:absolute; left:56px; right:56px; top:1262px; margin:0; color:{W}; font-size:40px; font-weight:700; letter-spacing:-0.02em">it’s on my vision board. now it’s on my list.</p>'
      + foot("Free 2027 Life Glow Up Kit →", False))
def p21():  # "vision board aesthetic": magazine grid, hero 2x2 + 5 small
    small = ["n14","m28","l20","e36","e24"]
    g = f'<div style="grid-column:1/3; grid-row:1/3; position:relative; overflow:hidden">{ph("e22","width:100%; height:100%")}</div>' + "".join(tile(k) for k in small)
    return (W, f'<p style="position:absolute; left:56px; top:56px; margin:0; font-size:24px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase">2027 · moodboard</p>'
      f'<h1 style="position:absolute; left:56px; right:56px; top:100px; margin:0; font-size:118px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">vision board<br>aesthetic</h1>'
      f'<div style="position:absolute; left:56px; right:56px; top:340px; height:888px; display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(3,1fr); gap:8px; background:{INK}; border:8px solid {INK}">{g}</div>'
      f'<p style="position:absolute; left:56px; right:56px; top:1262px; margin:0; font-size:38px; font-weight:600">big closets, cash, city nights, slow love.</p>'
      + foot("Write your 2027 list · free"))
def p22():  # "2027 manifestation board": 3x3 with 2 type tiles
    def tt(text, dark):
        bg, fg = (INK, W) if dark else (W, INK)
        return f'<div style="background:{bg}; color:{fg}; display:flex; align-items:center; padding:0 22px; font-size:46px; font-weight:800; letter-spacing:-0.04em; line-height:0.95">{text}</div>'
    cells = [tile("m24"), tt("i claim it all.", True), tile("n18"), tile("l23"), tile("e20"), tile("e28"),
             tile("e35"), tile("m25"), tt("same girl, bigger dreams", False)]
    return (W, f'<h1 style="position:absolute; left:56px; right:56px; top:48px; margin:0; font-size:96px; font-weight:800; letter-spacing:-0.06em; line-height:0.88">2027 manifestation<br>board</h1>'
      f'<div style="position:absolute; left:56px; right:56px; top:300px; height:900px; display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:repeat(3,1fr); gap:8px; background:{INK}; border:8px solid {INK}">{"".join(cells)}</div>'
      f'<p style="position:absolute; left:56px; right:56px; top:1240px; margin:0; font-size:36px; font-weight:600; line-height:1.2">board done? the free kit has the “my 2027” list page + 30 prompts.</p>'
      + foot("Get it free · issue11.app"))

# ---------- 4 text-only typographic pins (no photos, no AI label) ----------
def lst(items, fs=40, dark=False, num=True):
    fg = W if dark else INK
    return "".join(f'<div style="display:flex; gap:22px; padding:18px 0; border-top:2.5px solid {fg}; font-size:{fs}px; font-weight:500; line-height:1.18"><b style="flex:none; width:{int(fs*1.4)}px; font-weight:800">{(f"{i+1:02d}" if num else "☐")}</b><span>{t}</span></div>' for i,t in enumerate(items))
def p23():
    items = ["a closet where i can see the floor","a savings number. written down","a group chat that actually makes plans",
             "pilates 3x a week (or just walk lol)","one solo trip. lisbon?","a desk with a candle on it","asleep before 12. most nights"]
    return (W, f'<h1 style="position:absolute; left:60px; right:60px; top:56px; margin:0; font-size:104px; font-weight:800; letter-spacing:-0.06em; line-height:0.88">2027 vision board ideas</h1>'
      f'<p style="position:absolute; left:60px; top:300px; margin:0; font-size:42px; font-weight:600">(that aren’t a beach)</p>'
      f'<div style="position:absolute; left:60px; right:60px; top:380px">{lst(items, 50)}</div>'
      f'<p style="position:absolute; left:60px; right:60px; top:1270px; margin:0; font-size:34px; font-weight:600">pin the pics, then write the list. the page is free.</p>' + foot("Write yours · free 2027 list page"))
def p24():
    items = ["a raise. asking this time","friends who clap when i win","skin that looks like i drink water",
             "a closet i actually wear","money i don’t panic about","a trip i pay for myself","more peace. maybe a dog?"]
    return (INK, f'<p style="position:absolute; left:60px; top:60px; margin:0; color:{W}; font-size:26px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase">2027 · claim it</p>'
      f'<h1 style="position:absolute; left:60px; right:60px; top:106px; margin:0; color:{W}; font-size:104px; font-weight:800; letter-spacing:-0.06em; line-height:0.88">things i’m manifesting for 2027</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:420px; color:{W}">{lst(items, 50, True, False)}</div>' + foot("Write your list · free kit", False))
def p25():
    items = ["what do i want my mornings to look like?","what am i done apologizing for?","what money number scares me to say out loud?",
             "who makes me feel bigger, not smaller?","what would 2027 me stop buying?","what does a perfect tuesday look like?"]
    return (W, f'<h1 style="position:absolute; left:60px; right:60px; top:56px; margin:0; font-size:120px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">journal prompts for 2027</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:330px">{lst(items, 52)}</div>'
      f'<p style="position:absolute; left:60px; right:60px; top:1290px; margin:0; font-size:32px; font-weight:600">+ 30 more prompts in the free kit. paste them into chatgpt or your journal.</p>'
      + foot("Free 2027 Life Glow Up Kit →"))
def p26():
    rows = [("body","walk daily. pilates when i can"),("money","one money date a month"),("love","text back. plan the dinner"),
            ("style","3 outfits i love, not 30 i don’t"),("beauty","spf every day. yes, in winter"),("home","clear one drawer a week")]
    rr = "".join(f'<div style="display:grid; grid-template-columns:190px 1fr; padding:22px 0; border-top:2.5px solid {W}"><b style="font-size:26px; letter-spacing:0.18em; text-transform:uppercase; padding-top:8px">{a}</b><span style="font-size:48px; line-height:1.15; font-weight:500">{b}</span></div>' for a,b in rows)
    return (INK, f'<h1 style="position:absolute; left:60px; right:60px; top:56px; margin:0; color:{W}; font-size:124px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">lifemaxxing 2027: the list</h1>'
      f'<div style="position:absolute; left:60px; right:60px; top:350px; color:{W}">{rr}</div>'
      f'<p style="position:absolute; left:60px; right:60px; top:1250px; margin:0; color:{W}; font-size:32px; font-weight:600">one chapter at a time. a chatgpt prompt for each in the free kit.</p>'
      + foot("Lifemaxxing guide · free", False))

# ---------- 2 Notes pins: approved template copied from batch1/generator.py notes() ----------
def notes(date, title, sections, footer):
    n = sum(len(i)+1 for _,i in sections)
    fs = 38 if n >= 11 else (46 if n >= 8 else 54)
    secs = ""
    for h, items in sections:
        lis = "".join(f'<div style="display:flex; gap:26px; margin:8px 0"><span>–</span><span>{t}</span></div>' for t in items)
        secs += f'<p style="margin:{int(fs*0.9)}px 0 6px; font-weight:700; font-size:{fs+2}px">{h}</p><div style="padding-left:30px; font-size:{fs}px; line-height:1.3">{lis}</div>'
    return ("#000", f"""<div style="position:absolute; inset:0; padding:40px 64px; font-family:{SYS}, {EMO}; color:#fff">
  <div style="display:flex; justify-content:space-between; font-size:30px; font-weight:600"><span>10:19</span><span>●●● ◔</span></div>
  <div style="display:flex; justify-content:space-between; margin-top:30px"><span style="width:76px; height:76px; border-radius:50%; background:#1c1c1e; display:flex; align-items:center; justify-content:center; font-size:40px">‹</span><span style="height:76px; padding:0 30px; border-radius:40px; background:#1c1c1e; display:flex; align-items:center; font-size:34px">⤴ ⋯</span></div>
  <p style="margin:34px 0 0; text-align:center; font-size:28px; color:#8e8e93">{date}</p>
  <h1 style="margin:22px 0 0; font-size:{fs+34}px; font-weight:800; letter-spacing:-0.02em; line-height:1.05">{title}</h1>
  {secs}
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:26px 64px 30px; background:#fff; display:flex; justify-content:space-between; align-items:center; color:#0D0D0D; font-family:'Inter Tight', {SYS}">
  <div><p style="margin:0; font-size:26px; font-weight:500">{footer}</p><p style="margin:4px 0 0; font-size:44px; font-weight:800; letter-spacing:-0.03em">Get it free at issue11.app →</p></div>{logo()}
</div>""")

P = [("Pin19","2027 vision board ideas · collage 3x3",p19()),
     ("Pin20","Vision board 2027 · collage 2x3 black",p20()),
     ("Pin21","Vision board aesthetic · magazine grid",p21()),
     ("Pin22","2027 manifestation board · collage + type tiles",p22()),
     ("Pin23","2027 vision board ideas (that aren't a beach) · text",p23()),
     ("Pin24","Things i'm manifesting for 2027 · text",p24()),
     ("Pin25","Journal prompts for 2027 · text",p25()),
     ("Pin26","Lifemaxxing 2027: the list · text",p26()),
     ("Pin27","Vision board ideas · Notes",notes("November 15, 2026 at 22:41","vision board 2027:",[("the list",["the closet i’m saving for","$300 a month into savings","pilates 3x a week (or just walk lol)","one trip i book myself. lisbon?"])],"The “my 2027” list page · free kit")),
     ("Pin28","Journal prompts · Notes",notes("November 15, 2026 at 23:08","journal prompts for jan 1:",[("answer honestly",["what did 2026 teach me","what am i done saying yes to","what’s my savings number for 2027","who do i want to see more of?"])],"30 prompts · free 2027 kit"))]
for k, t, (bg, inner) in P:
    open(f"{R}/project/{k}.dc.html", "w").write(doc(t, inner, bg))
print("ok", len(P))
