# Pin style sampler (Nov 15, 2026): 10 affirmation pins, one per viral style, so Megan can pick the styles she likes.
# Megan: "I think what we wrote isn't sharp enough, it needs to land emotionally and resonate" · "I also would like to see
# different styles of pins" · "it needs to give relief, every single one of them" · "They can also be outrageous".
# Usage: python3 generator-styles.py <out_root>  -> writes <out_root>/project/Pin62..Pin71.dc.html
# Reuses batch2 asset ids (lead magnets canvas) and the approved Notes template idea from batch1/generator.py.
import sys, os, re
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
B = dict(re.findall(r'"(\w\d\d)":"([0-9a-f]{32})"', open(f"{HERE}/../batch2/generator-b2.py").read()))
LOGO = "/_blob/d196614efc6265e2205729134fb523b8"
INK = "#0D0D0D"; W = "#FFFFFF"; CREAM = "#F6F3EE"; ICE = "#EAF6FF"; LILAC = "#D9B3FF"
EMO = "'Apple Color Emoji','Noto Color Emoji','Segoe UI Emoji'"
SYS = "-apple-system, 'SF Pro Text', 'Inter Tight', system-ui, sans-serif"
COL = "filter:contrast(1.06) saturate(0.95)"   # colour photos only (Megan: "no images in black and white")
FONTS = "family=Inter+Tight:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500"

def doc(title, inner, bg, serif=False):
    f = FONTS + ("&amp;family=Instrument+Serif" if serif else "")
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
<link href="https://fonts.googleapis.com/css2?{f}&amp;display=swap" rel="stylesheet">
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
def url(fg, align="center", bottom=70, size=30, weight=600):
    return f'<p style="position:absolute; left:80px; right:80px; bottom:{bottom}px; margin:0; color:{fg}; font-size:{size}px; font-weight:{weight}; letter-spacing:0.02em; text-align:{align}">issue11.app</p>'
def logo(white=False, st=""): return f'<img src="{LOGO}" alt="ISSUE11" style="height:40px; width:auto; {"filter:invert(1);" if white else ""} {st}">'
def ph(k, pos, st): return f'<img src="/_blob/{B[k]}" alt="Editorial photo (AI-generated)" style="position:absolute; display:block; object-fit:cover; object-position:{pos}; {COL}; {st}">'
def center(html, pad=100, top=0, bottom=0):
    return f'<div style="position:absolute; left:0; right:0; top:{top}px; bottom:{bottom}px; padding:0 {pad}px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center">{html}</div>'

# 1 · Repeat page: one line written ~14 times like a mantra, cream page
def s1():
    line = "It’s already mine."
    rows = "".join(f'<p style="margin:0; font-size:62px; font-weight:400; letter-spacing:-0.01em; line-height:1.36">{line}</p>' for _ in range(14))
    return (CREAM, f'<div style="position:absolute; left:100px; right:80px; top:100px">{rows}</div>' + url(INK, "left", 70, 28, 500).replace("left:80px", "left:100px"))

# 2 · Soft card: pale Ice, small centered italic, lots of air
def s2():
    q = '<p style="margin:0; font-size:64px; font-style:italic; font-weight:400; letter-spacing:-0.01em; line-height:1.3; white-space:nowrap">I can relax.<br>It’s handled.</p>'
    return (ICE, center(q, 100, 0, 80) + url(INK, "center", 80, 26, 500))

# 3 · Night card: near-black, tiny label pill, bold white centered type, thin rule + url
def s3():
    pill = f'<span style="position:absolute; left:50%; top:130px; transform:translateX(-50%); border:2px solid rgba(255,255,255,0.7); border-radius:40px; padding:12px 30px; color:{W}; font-size:24px; font-weight:600; letter-spacing:0.22em; white-space:nowrap">AFFIRMATION · 2027</span>'
    q = f'<p style="margin:0; color:{W}; font-size:112px; font-weight:800; letter-spacing:-0.045em; line-height:1.0; white-space:nowrap">The universe<br>is obsessed<br>with me.</p>'
    rule = f'<div style="position:absolute; left:50%; bottom:150px; width:120px; height:2px; margin-left:-60px; background:{W}; opacity:0.7"></div>'
    return ("#0B0B0C", pill + center(q, 60) + rule + url(W, "center", 86, 28, 500))

# 4 · Text over a flash photo: m28 (asleep on money), white type with soft shadow, kept below the face
def s4():
    sh = "text-shadow:0 2px 18px rgba(0,0,0,0.55), 0 1px 3px rgba(0,0,0,0.5)"
    q = f'<p style="position:absolute; left:60px; right:60px; top:930px; margin:0; color:{W}; font-size:118px; font-weight:800; letter-spacing:-0.06em; line-height:0.9; text-align:center; white-space:nowrap; {sh}">Money finds me<br>even when<br>I’m asleep.</p>'
    bar = (f'<div style="position:absolute; left:0; right:0; bottom:0; height:110px; padding:0 56px; box-sizing:border-box; background:{INK}; color:{W}; display:flex; justify-content:space-between; align-items:center">'
           f'<span style="font-size:30px; font-weight:600; letter-spacing:0.02em">issue11.app</span>{logo(True)}</div>')
    return (INK, ph("m28", "40% 30%", "left:0; top:0; width:1000px; height:1390px") + q + bar)

# 5 · "SAY IT WITH ME:" bold kicker, then the affirmation in regular weight, on paper
def s5():
    html = (f'<p style="margin:0 0 56px; font-size:92px; font-weight:800; letter-spacing:-0.05em; line-height:0.95">SAY IT<br>WITH ME:</p>'
            f'<p style="margin:0; font-size:84px; font-weight:400; letter-spacing:-0.03em; line-height:1.1; white-space:nowrap">Everything I asked for<br>is on its way.</p>')
    return (W, f'<div style="position:absolute; left:80px; right:60px; top:0; bottom:120px; display:flex; flex-direction:column; justify-content:center">{html}</div>' + url(INK, "left", 76, 30, 600))

# 6 · All caps in Lilac on black
def s6():
    q = f'<p style="margin:0; color:{LILAC}; font-size:120px; font-weight:800; letter-spacing:-0.035em; line-height:0.98; text-transform:uppercase; white-space:nowrap">Doors open<br>for me.<br>Even the<br>locked ones.</p>'
    return (INK, center(q, 60, 0, 60) + url(LILAC, "center", 76, 28, 600))

# 7 · Giant one word + a small line under it
def s7():
    html = (f'<p style="margin:0; font-size:250px; font-weight:800; letter-spacing:-0.045em; line-height:0.85; white-space:nowrap">LUCKY.</p>'
            f'<p style="margin:56px 0 0; font-size:46px; font-weight:500; letter-spacing:-0.01em; line-height:1.2; white-space:nowrap">I’m so lucky it’s honestly unfair.</p>')
    return (W, center(html, 40, 0, 80) + url(INK, "center", 76, 28, 600))

# 8 · Phone Notes: approved dark Notes look (batch1 notes()), one affirmation, no list, white CTA bar
def s8():
    inner = f"""<div style="position:absolute; inset:0; padding:40px 64px; font-family:{SYS}, {EMO}; color:#fff">
  <div style="display:flex; justify-content:space-between; font-size:30px; font-weight:600"><span>11:11</span><span>●●● ◔</span></div>
  <div style="display:flex; justify-content:space-between; margin-top:30px"><span style="width:76px; height:76px; border-radius:50%; background:#1c1c1e; display:flex; align-items:center; justify-content:center; font-size:40px">‹</span><span style="height:76px; padding:0 30px; border-radius:40px; background:#1c1c1e; display:flex; align-items:center; font-size:34px">⤴ ⋯</span></div>
  <p style="margin:34px 0 0; text-align:center; font-size:28px; color:#8e8e93">November 15, 2026 at 23:47</p>
  <h1 style="margin:40px 0 0; font-size:66px; font-weight:800; letter-spacing:-0.02em; line-height:1.05">reminder 🫧</h1>
  <p style="margin:48px 0 0; font-size:108px; font-weight:700; letter-spacing:-0.03em; line-height:1.08">Good news is looking for me.</p>
</div>
<div style="position:absolute; left:0; right:0; bottom:0; padding:30px 64px 34px; background:#fff; display:flex; justify-content:space-between; align-items:center; color:{INK}; font-family:'Inter Tight', {SYS}">
  <p style="margin:0; font-size:44px; font-weight:800; letter-spacing:-0.03em">issue11.app</p>{logo()}
</div>"""
    return ("#000", inner)

# 9 · Magazine pull quote (layout H): quote page facing a photo strip, magazine furniture, logo
def s9():
    head = (f'<div style="position:absolute; left:0; right:0; top:0; height:72px; padding:0 48px; box-sizing:border-box; background:{INK}; color:{W}; display:flex; justify-content:space-between; align-items:center; font-size:22px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase"><span>Affirmation · 2027</span><span>issue11 · 070</span></div>')
    photo = ph("n16", "49% 50%", f"left:520px; top:72px; width:480px; height:1318px")
    q = (f'<div style="position:absolute; left:48px; width:430px; top:72px; bottom:110px; display:flex; flex-direction:column; justify-content:center">'
         f'<p style="margin:0 0 30px; font-size:150px; font-weight:800; line-height:0.6">“</p>'
         f'<p style="margin:0; font-size:84px; font-weight:800; letter-spacing:-0.055em; line-height:0.94; white-space:nowrap">The life<br>I want<br>wants<br>me back.</p>'
         f'<div style="margin-top:44px; width:90px; height:4px; background:{INK}"></div></div>')
    bar = (f'<div style="position:absolute; left:0; right:0; bottom:0; height:110px; padding:0 48px; box-sizing:border-box; background:{INK}; color:{W}; display:flex; justify-content:space-between; align-items:center">'
           f'<span style="font-size:30px; font-weight:600; letter-spacing:0.02em">issue11.app</span>{logo(True)}</div>')
    return (W, head + photo + q + bar)

# 10 · Rule-breaker: big serif (Instrument Serif) on white. Our rule is Inter Tight only, Megan decides.
def s10():
    q = (f'<p style="margin:0; font-family:\'Instrument Serif\', Georgia, serif; font-size:150px; font-weight:400; letter-spacing:-0.02em; line-height:0.98; white-space:nowrap">I’m the girl<br>it all works<br>out for.</p>')
    return (W, center(q, 60, 0, 60) + url(INK, "center", 76, 28, 500))

P = [("Pin62", "1 · Repeat page", "It's already mine.", s1()),
     ("Pin63", "2 · Soft card (Ice, italic)", "I can relax. It's handled.", s2()),
     ("Pin64", "3 · Night card", "The universe is obsessed with me.", s3()),
     ("Pin65", "4 · Text over flash photo", "Money finds me even when I'm asleep.", s4()),
     ("Pin66", "5 · SAY IT WITH ME", "Everything I asked for is on its way.", s5()),
     ("Pin67", "6 · All caps Lilac on black", "Doors open for me. Even the locked ones.", s6()),
     ("Pin68", "7 · Giant word + line", "I'm so lucky it's honestly unfair.", s7()),
     ("Pin69", "8 · Phone Notes", "Good news is looking for me.", s8()),
     ("Pin70", "9 · Magazine pull quote (H)", "The life I want wants me back.", s9()),
     ("Pin71", "10 · RULE-BREAKER serif (not Inter Tight)", "I'm the girl it all works out for.", s10())]
if __name__ == "__main__":
    for k, style, line, (bg, inner) in P:
        open(f"{R}/project/{k}.dc.html", "w").write(doc(f"Style {style} · {line}", inner, bg, serif=(k == "Pin71")))
    print("ok", len(P))
