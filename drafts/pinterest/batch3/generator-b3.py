# Pinterest batch 3 (Nov 15, 2026): magazine-page pins from the MISE-EN-PAGE layout library (L M T V Z D H P).
# Usage: python3 generator-b3.py <out_root>  -> writes <out_root>/project/Pin29..Pin36.dc.html
# Reuses batch2 asset ids (lead magnets canvas), doc() shell and focal-point approach. Colour photos, B&W design, Inter Tight.
import sys, os, re
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../batch2/generator-b2.py")).read()
B = dict(re.findall(r'"(\w\d\d)":"([0-9a-f]{32})"', src))
LOGO = "/_blob/d196614efc6265e2205729134fb523b8"
INK = "#0D0D0D"; W = "#FFFFFF"
EMO = "'Apple Color Emoji','Noto Color Emoji','Segoe UI Emoji'"
COL = "filter:contrast(1.06) saturate(0.95)"   # colour photos only (Megan: "no images in black and white")
CTA = "Free 2027 Life Glow Up Kit → issue11.app"
def ph(k, pos, st, alt="Editorial photo (AI-generated)"):
    return f'<img src="/_blob/{B[k]}" alt="{alt}" style="position:absolute; display:block; object-fit:cover; object-position:{pos}; {COL}; {st}">'
def logo(white=False): return f'<img src="{LOGO}" alt="ISSUE11" style="height:40px; width:auto; {"filter:invert(1);" if white else ""}">'
def doc(title, inner, bg):
    exec_src = src[src.index("def doc("):src.index("def foot(")]
    ns = {"INK": INK, "EMO": EMO}; exec(exec_src, ns); return ns["doc"](title, inner, bg)
def head(kicker, num, dark=True):
    bg, fg = (INK, W) if dark else (W, INK)
    return (f'<div style="position:absolute; left:0; right:0; top:0; height:72px; padding:0 48px; box-sizing:border-box; background:{bg}; color:{fg}; '
            f'display:flex; justify-content:space-between; align-items:center; font-size:24px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; '
            f'{"" if dark else f"border-bottom:3px solid {INK};"}"><span>{kicker}</span><span>issue11 · {num:03d}</span></div>')
def foot():
    return (f'<div style="position:absolute; left:0; right:0; bottom:0; height:120px; padding:0 48px; box-sizing:border-box; background:{INK}; color:{W}; '
            f'display:flex; justify-content:space-between; align-items:center"><span style="font-size:33px; font-weight:700; letter-spacing:-0.02em">{CTA}</span>{logo(True)}</div>')
def box(t, st=""):  # white label box with black type, used over photos
    return f'<span style="background:{W}; color:{INK}; padding:2px 16px 8px; box-decoration-break:clone; -webkit-box-decoration-break:clone; {st}">{t}</span>'

# L · quote set across a full-bleed photo, vertical credits on both edges
def p29():
    q = "how to glow up: pick one thing. do it for 30 days. then the next one."
    return (INK, ph("e24", "50% 18%", "left:0; top:72px; width:1000px; height:1308px")
      + head("how to glow up · the 2027 issue", 29)
      + f'<p style="position:absolute; left:84px; right:84px; top:830px; margin:0; font-size:76px; font-weight:800; letter-spacing:-0.045em; line-height:1.18">{box("“"+q+"”")}</p>'
      + f'<p style="position:absolute; left:16px; bottom:150px; margin:0; writing-mode:vertical-rl; transform:rotate(180deg); padding:10px 4px; background:{W}; font-size:20px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; white-space:nowrap">the 2027 life glow up kit · free</p>'
      + f'<p style="position:absolute; right:16px; top:100px; margin:0; writing-mode:vertical-rl; padding:10px 4px; background:{W}; font-size:20px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; white-space:nowrap">issue11.app · 30-day plan inside</p>'
      + foot())

# M · giant overprint type on a photo + small info box
def p30():
    items = ["the “my 2027” list page","6 chapters: body, money, love, style, beauty, home","30 chatgpt prompts","a 30-day challenge","a letter from future you"]
    li = "".join(f'<div style="padding:7px 0; border-top:2px solid {INK}">{t}</div>' for t in items)
    return (W, ph("n14", "50% 25%", "left:0; top:72px; width:1000px; height:800px")
      + head("glow up 2027 · cover", 30)
      + f'<h1 style="position:absolute; left:36px; top:640px; margin:0; font-size:290px; font-weight:800; letter-spacing:-0.075em; line-height:0.8; mix-blend-mode:multiply">glow<br>up</h1>'
      + f'<p style="position:absolute; left:40px; top:1130px; margin:0; font-size:150px; font-weight:800; letter-spacing:-0.06em; line-height:0.8">2027</p>'
      + f'<div style="position:absolute; right:40px; top:900px; width:430px; padding:22px 26px; box-sizing:border-box; background:{W}; border:4px solid {INK}; font-size:27px; font-weight:500; line-height:1.2">'
        f'<p style="margin:0 0 12px; font-size:22px; font-weight:800; letter-spacing:0.16em; text-transform:uppercase">inside the free kit</p>{li}</div>'
      + foot())

# T · giant letters stacked down a white column, facing a full-height portrait
def p31():
    letters = "".join(f'<div>{c}</div>' for c in "LIFEMAXX")
    return (W, head("lifemaxxing 101", 31, False)
      + f'<div style="position:absolute; left:0; top:72px; width:400px; height:1308px; display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:158px; font-weight:800; line-height:0.98; letter-spacing:-0.04em">{letters}</div>'
      + ph("e27", "30% 20%", "left:400px; top:72px; width:600px; height:1308px")
      + f'<div style="position:absolute; left:400px; top:72px; width:6px; height:1308px; background:{INK}"></div>'
      + f'<div style="position:absolute; left:440px; right:40px; top:1100px; padding:20px 24px; background:{W}; border:4px solid {INK}; font-size:30px; font-weight:600; line-height:1.2">'
        f'<b style="display:block; font-size:44px; font-weight:800; letter-spacing:-0.03em">lifemaxxing 2027</b>body, money, love, style, beauty, home. one chatgpt prompt for each.</div>'
      + foot())

# V · one name repeated in huge type + portrait with an ID-card list
def p32():
    rep = "".join('<div>future you</div>' for i in range(4))
    rows = [("name","future you"),("year","2027"),("mornings","no phone till 9"),("money","$500 a month saved"),("closet","stuff i actually wear"),("motto","Become YOU")]
    rr = "".join(f'<div style="display:grid; grid-template-columns:150px 1fr; padding:11px 0; border-top:2px solid {INK}"><b style="font-size:20px; letter-spacing:0.16em; text-transform:uppercase; padding-top:6px">{a}</b><span style="font-size:32px; font-weight:600">{b}</span></div>' for a,b in rows)
    return (INK, head("future self · id card", 32)
      + f'<div style="position:absolute; left:40px; top:100px; color:{W}; font-size:184px; font-weight:800; letter-spacing:-0.06em; line-height:0.86">{rep}</div>'
      + f'<div style="position:absolute; left:0; right:0; top:760px; height:620px; background:{W}"></div>'
      + ph("e36", "50% 4%", f"left:40px; top:790px; width:380px; height:560px; outline:4px solid {INK}")
      + f'<div style="position:absolute; left:450px; right:40px; top:790px; color:{INK}"><p style="margin:0 0 8px; font-size:22px; font-weight:800; letter-spacing:0.16em; text-transform:uppercase">future self · id</p>{rr}'
        f'<p style="margin:14px 0 0; font-size:24px; font-weight:600; line-height:1.25">write a letter from future you. the page is in the free kit.</p></div>'
      + foot())

# Z · words stacked in ruled boxes, facing a full photo
def p33():
    words = [("me 🫱🏻‍🫲🏽 2027", 82), ("and", 128), ("it’s", 128), ("finally", 128), ("my", 128), ("year.", 128)]
    bx = "".join(f'<div style="border:4px solid {INK}; {"" if i==0 else "border-top:none;"} height:172px; box-sizing:border-box; display:flex; align-items:center; padding:0 26px; font-size:{fs}px; font-weight:800; letter-spacing:-0.05em; white-space:nowrap">{w}</div>' for i,(w,fs) in enumerate(words))
    return (W, head("manifesting 2027", 33, False)
      + f'<div style="position:absolute; left:40px; width:500px; top:110px">{bx}</div>'
      + ph("m25", "30% 18%", "left:570px; top:72px; width:430px; height:1308px")
      + f'<div style="position:absolute; left:570px; top:72px; width:4px; height:1308px; background:{INK}"></div>'
      + f'<p style="position:absolute; left:40px; width:500px; top:1188px; margin:0; font-size:34px; font-weight:600; line-height:1.2">manifesting 2027? write it down first. the my 2027 list page is free.</p>'
      + foot())

# D · huge word at the bottom, offset small photo
def p34():
    items = ["audit my socials","clear out the closet","find a signature scent","one money date a month","in bed by 12"]
    li = "".join(f'<div style="padding:10px 0; border-top:2px solid {INK}">{t}</div>' for t in items)
    return (W, head("personal rebrand · 2027", 34, False)
      + ph("n16", "50% 30%", f"left:470px; top:120px; width:490px; height:620px; outline:4px solid {INK}")
      + f'<div style="position:absolute; left:40px; width:390px; top:120px"><p style="margin:0 0 18px; font-size:50px; font-weight:800; letter-spacing:-0.04em; line-height:0.95">my personal rebrand list:</p><div style="font-size:35px; font-weight:500; line-height:1.2">{li}</div></div>'
      + f'<p style="position:absolute; left:40px; right:40px; top:800px; margin:0; font-size:52px; font-weight:700; letter-spacing:-0.03em">can’t talk rn. i’m rebranding.</p>'
      + f'<p style="position:absolute; left:28px; top:900px; margin:0; font-size:262px; font-weight:800; letter-spacing:-0.075em; line-height:0.9">rebrand</p>'
      + f'<p style="position:absolute; left:40px; right:40px; top:1200px; margin:0; font-size:32px; font-weight:600; line-height:1.2">6 chapters + 30 chatgpt prompts to plan yours. free.</p>'
      + foot())

# H · pull quote facing a full photo
def p35():
    return (W, ph("n18", "50% 14%", "left:0; top:72px; width:1000px; height:820px")
      + head("that girl aesthetic · 2027", 35)
      + f'<p style="position:absolute; left:48px; right:48px; top:930px; margin:0; font-size:26px; font-weight:800; letter-spacing:0.16em; text-transform:uppercase">that girl aesthetic, my version</p>'
      + f'<p style="position:absolute; left:40px; right:40px; top:985px; margin:0; font-size:92px; font-weight:800; letter-spacing:-0.06em; line-height:0.9">“i’m the art director of my life.”</p>'
      + f'<p style="position:absolute; left:48px; right:48px; top:1200px; margin:0; font-size:40px; font-weight:600">30 chatgpt prompts + a 30-day plan. free.</p>'
      + foot())

# P · portrait with an itemised list down the edge
def p36():
    items = ["date nights in the rain","a closet i actually wear","$5k emergency fund","learn italian (badly)","my own little desk","a trip w my mom?","phone off at 10"]
    li = "".join(f'<div style="display:flex; gap:14px; padding:16px 0; border-top:2px solid {INK}; font-size:38px; font-weight:500; line-height:1.12"><b style="flex:none; width:52px; font-weight:800">{i+1:02d}</b><span>{t}</span></div>' for i,t in enumerate(items))
    return (W, head("2027 vision board ideas", 36, False)
      + ph("l23", "50% 20%", f"left:40px; top:110px; width:470px; height:1230px; outline:4px solid {INK}")
      + f'<div style="position:absolute; left:540px; right:40px; top:110px"><p style="margin:0 0 22px; font-size:70px; font-weight:800; letter-spacing:-0.05em; line-height:0.92">2027 vision board ideas</p>{li}'
        f'<p style="margin:20px 0 0; font-size:30px; font-weight:600; line-height:1.25">pin the pics, then write the list. the page is free.</p></div>'
      + foot())

P = [("Pin29","L · How to glow up · quote across photo",p29()),("Pin30","M · Glow up 2027 · overprint cover",p30()),
     ("Pin31","T · Lifemaxxing 101 · stacked letters",p31()),("Pin32","V · Future self ID card",p32()),
     ("Pin33","Z · Manifesting 2027 · ruled boxes",p33()),("Pin34","D · Personal rebrand · big word",p34()),
     ("Pin35","H · That girl aesthetic · pull quote",p35()),("Pin36","P · 2027 vision board ideas · portrait + list",p36())]
for k, t, (bg, inner) in P:
    open(f"{R}/project/{k}.dc.html", "w").write(doc(t, inner, bg))
print("ok", len(P))
