# Winter arc pins (WA1–WA6), Nov 17 2026. Article: issue11.app/blog/winter-arc (live Nov 18).
# Approved / loved layouts only (no new format rounds, Megan Nov 16–17): phone notes, magazine cover,
# rules sheet (article-pin family), CT42 pastel + framed photo + italic, quote over full-bleed photo, CT55 triptych.
# Photos: Megan's editorial set (drafts/issue11-blog/images), colour, no fade (Nov 17), text-shadow on letters only.
# Logo 92px bottom / 76px centred top (Nov 16). issue11.app 19px on every pin (notes: list-size line bottom-left, Nov 17).
# Run: python3 -I gen_winter_arc.py && node render.js
import os
D = os.path.dirname(os.path.abspath(__file__))
IMG = '../../issue11-blog/images/'
LOGO = '../../issue11-gift/rebrand-kit/img/logo-black.png'
FONT = '../../issue11-gift/rebrand-kit/InterTight.ttf'
FONTI = '../styles/fonts/InterTightItalic.woff2'
A = 'alt="Editorial photo (AI-generated)"'
def ph(n): return IMG + (f'megan-editorial-{n}.webp' if isinstance(n, int) else n)

BASE = f"""@font-face{{font-family:'Inter Tight';src:url({FONT});font-weight:100 900}}
@font-face{{font-family:'Inter Tight';src:url({FONTI});font-style:italic;font-weight:100 900}}
body{{margin:0}}
.pin{{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:'Inter Tight',system-ui,sans-serif;color:#0D0D0D}}
.pin :is(h1,.kick,.story,.q,.it,.mo,.sub,.ar p,.cap){{word-spacing:.16em}}
img.f{{position:absolute;object-fit:cover;display:block}}
.full{{inset:0;width:100%;height:100%}}
.w{{filter:invert(1)}}
.tl{{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%);z-index:5}}
.url{{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:600;font-size:19px;z-index:5}}
.sh{{text-shadow:0 2px 18px rgba(0,0,0,.45),0 1px 3px rgba(0,0,0,.35)}}
"""
def doc(title, css, body, bg='#fff'):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{BASE}{css}</style></head>
<body><div class="pin" style="background:{bg}">
{body}
</div></body></html>
"""
T = lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
U = lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
P = {}

# WA1 · phone notes (loved, Nov 17) · copies the viral numbered "winter arc rules" list (1,472 reactions)
def notes(date, title, items):
    lis = ''.join(f'<div style="display:flex;gap:26px;margin:10px 0"><span>–</span><span>{t}</span></div>' for t in items)
    return f"""<div style="position:absolute;inset:0;padding:40px 64px;font-family:-apple-system,'SF Pro Text','Inter Tight',system-ui,sans-serif,'Noto Color Emoji';color:#fff">
  <div style="display:flex;justify-content:space-between;font-size:30px;font-weight:600"><span>10:19</span><span>●●● ◔</span></div>
  <div style="display:flex;justify-content:space-between;margin-top:30px"><span style="width:76px;height:76px;border-radius:50%;background:#1c1c1e;display:flex;align-items:center;justify-content:center;font-size:40px">‹</span><span style="height:76px;padding:0 30px;border-radius:40px;background:#1c1c1e;display:flex;align-items:center;font-size:34px">⤴ ⋯</span></div>
  <p style="margin:34px 0 0;text-align:center;font-size:28px;color:#8e8e93">{date}</p>
  <h1 style="margin:22px 0 0;font-size:80px;font-weight:800;letter-spacing:-0.02em;line-height:1.05;word-spacing:0">{title}</h1>
  <div style="margin-top:50px;padding-left:10px;font-size:54px;line-height:1.3;word-spacing:0">{lis}</div>
  <p style="position:absolute;left:64px;bottom:60px;margin:0;font-size:50px;line-height:1.3">issue11.app</p>
</div>"""
P['WA1'] = doc('WA1 · phone notes · winter arc rules', '', notes('November 18, 2026 at 22:14', 'winter arc rules ❄️', [
    'pick 3 areas. not 10',
    '20 min walk, even in a coat and a hat',
    "earlier bedtime. it's dark at 5 anyway",
    'post less, save more',
    "missing a day doesn't end it",
    'who am i on march 1?',
]), bg='#000')

# WA2 · magazine cover (approved template, gen5.cover) · masthead WINTER ARC · real article counts
BAR = '<svg viewBox="0 0 200 60" width="168" height="50" fill="#fff">' + ''.join(f'<rect x="{x}" y="0" width="{w}" height="{h}"/>' for x, w, h in [(4,3,58),(10,3,50),(15,4.5,50),(22.5,1.5,50),(25.5,4.5,50),(32,4.5,50),(38,1.5,50),(41.5,2,50),(45,1.5,50),(49.5,1.5,50),(54,3,50),(59,4.5,50),(66.5,1.5,50),(71,1.5,50),(75.5,1.5,50),(78.5,1.5,50),(81.5,1.5,50),(86,1.5,50),(89.5,2,50),(93.5,4.5,50),(99.5,4.5,58),(105.5,2,50),(109.5,1.5,50),(114,1.5,50),(117.5,2,50),(121.5,4.5,50),(127.5,2,50),(131.5,1.5,50),(136,2,50),(139.5,1.5,50),(144,1.5,50),(147.5,1.5,50),(151,3,50),(155.5,1.5,50),(160,1.5,50),(163,1.5,50),(166,3,50),(171,3,50),(176,1.5,50),(180.5,1.5,50),(185,2,50),(189,1.5,50),(192.5,2,58)]) + '</svg>'
def cover(n, k, pos, mast, mcol, story, lines, msize=150):
    ls = '<br>'.join(f'<b style="color:{mcol}">{a}</b> {b}' for a, b in lines)
    return doc(f'{n} · magazine cover · {mast.lower()}', f"""
.dg{{position:absolute;left:36px;right:36px;top:28px;font-weight:900;font-size:{msize}px;line-height:.78;letter-spacing:-.07em;text-transform:uppercase;white-space:nowrap;word-spacing:.22em;color:{mcol};text-shadow:0 4px 30px rgba(0,0,0,.3)}}
.date{{position:absolute;right:44px;top:300px;writing-mode:vertical-rl;color:#fff;font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase}}
.story{{position:absolute;left:52px;bottom:300px;color:#fff;font-weight:900;font-size:76px;line-height:.92;letter-spacing:-.045em;max-width:600px}}
.story i{{display:block;font-weight:600;font-size:30px;letter-spacing:.12em;text-transform:uppercase;font-style:normal;margin-bottom:12px;color:{mcol}}}
.lines{{position:absolute;right:48px;bottom:150px;text-align:right;color:#fff;font-weight:800;font-size:30px;line-height:1.25}}
.logo{{position:absolute;left:52px;bottom:44px;height:92px}}
.bar{{position:absolute;right:48px;bottom:44px;padding:8px 10px 4px;display:flex;flex-direction:column;align-items:center}}
.bar span{{font-weight:600;font-size:13px;letter-spacing:.16em;color:#fff;margin-top:2px}}
.site{{position:absolute;left:0;right:0;bottom:62px;text-align:center;color:#fff;font-weight:600;font-size:19px}}
""", f"""<img class="f full" src="{ph(k)}" style="object-position:{pos};transform:scale(1.12);transform-origin:50% 0%" {A}>
<div class="dg">{mast}</div><div class="date sh">The 2027 issue</div>
<div class="story sh"><i>Cover story</i>{story}</div>
<div class="lines sh">{ls}</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="site sh">issue11.app</div><div class="bar">{BAR}<span>8 88888 888 8888</span></div>""", bg='#222')
P['WA2'] = cover('WA2', 36, '50% 30%', 'Winter arc', '#BFE3FF', "I'm in my building era",
                 [('90', 'day winter arc plan'), ('20', 'winter arc ideas'), ('5', 'mistakes to skip')], msize=118)

# WA3 · rules sheet by area (article-pin family, ArticlePinGU) · copies viral "winter arc rules" by-category sheets (1,389 + 630)
AREAS = [('Body', ['Walk 20 minutes every day', 'Stretch five minutes before bed']),
         ('Mind', ['Read 10 pages a night', 'Journal one page on Sunday']),
         ('Money', ['Check your account once a week, calmly', 'Cancel one subscription you forgot you had']),
         ('Style', ['Plan one signature winter outfit', 'Get the haircut you keep screenshotting']),
         ('Home', ['Make your bed every morning', 'Cook one new meal a week'])]
rows = ''.join(f'<div class="ar"><b>{a}</b><div>{"".join(f"<p>{x}</p>" for x in xs)}</div></div>' for a, xs in AREAS)
P['WA3'] = doc('WA3 · winter arc ideas for women · sheet by area', f"""
.top{{position:absolute;left:52px;top:58px;font-weight:700;font-size:24px;letter-spacing:.16em;border:3px solid #0D0D0D;padding:10px 18px}}
h1{{position:absolute;left:48px;right:48px;top:150px;margin:0;font-weight:900;font-size:128px;line-height:.86;letter-spacing:-.055em;text-transform:uppercase}}
.sub{{position:absolute;left:52px;top:410px;font-weight:600;font-size:38px;letter-spacing:-.025em;font-style:italic}}
.list{{position:absolute;left:52px;top:490px;width:580px;border-top:4px solid #0D0D0D}}
.ar{{display:flex;gap:16px;padding:17px 0;border-bottom:1.5px solid #0D0D0D}}
.ar b{{flex:none;width:118px;font-weight:900;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#1E3A6E;padding-top:4px}}
.ar p{{margin:0 0 6px;font-weight:700;font-size:30px;line-height:1.12;letter-spacing:-.015em}}
.phw{{position:absolute;left:658px;right:52px;top:490px;height:800px;overflow:hidden}}
.phw img{{width:100%;height:100%;object-fit:cover;display:block}}
.cap{{position:absolute;left:658px;right:52px;top:1306px;font-weight:600;font-size:23px;line-height:1.3;color:#1E3A6E}}
.logo{{position:absolute;left:52px;bottom:44px;height:92px}}
.site{{position:absolute;left:190px;bottom:78px;font-weight:600;font-size:19px}}
""", f"""<div class="top">SAVE THIS ❄️</div>
<h1>Winter arc for women</h1>
<div class="sub">your whole life, not just the gym</div>
<div class="list">{rows}</div>
<div class="phw"><img src="{ph(24)}" style="object-position:72% 0%" {A}></div>
<div class="cap">One small habit per area. Pick three areas, not ten.</div>
<img class="logo" src="{LOGO}" alt="ISSUE11"><div class="site">issue11.app</div>""", bg='#DCE6F2')

# WA4 · CT42 pastel + framed photo + italic line (loved) · lexicon line, word for word
P['WA4'] = doc('WA4 · like 42 · quiet moments big plans', """
.it{position:absolute;left:60px;right:60px;top:1040px;text-align:center;font-style:italic;font-weight:400;font-size:70px;letter-spacing:-.03em;color:#111;line-height:1.05}
""", f"""<img class="f" src="{ph(33)}" style="left:250px;top:200px;width:500px;height:760px;object-position:50% 40%" {A}>{T()}<div class="it">Quiet moments,<br>big plans</div>{U('#111')}""", bg='#E6EEF8')

# WA5 · quote over full-bleed photo (liked doll-series style 156/158/160–162) · Megan's BANK line, text below the face
P['WA5'] = doc('WA5 · quote over full-bleed · lock in', """
.q{position:absolute;left:56px;width:470px;top:60px;text-align:left;color:#fff;font-weight:800;font-size:58px;line-height:1.04;letter-spacing:-.035em}
""", f"""<img class="f full" src="{ph(29)}" style="object-position:50% 20%" {A}><div class="q sh">if u lock in like a delusional psychopath u can actually get what u want sooner</div><img src="{LOGO}" alt="ISSUE11" style="position:absolute;left:52px;bottom:44px;height:92px"><div style="position:absolute;left:190px;bottom:78px;font-weight:600;font-size:19px">issue11.app</div>""", bg='#222')

# WA6 · CT55 triptych (loved) · the article's 3 months, word for word: Reset / Build / Become
MON = [(3, '50% 12%', 'Month 1', 'Reset'), (27, '62% 30%', 'Month 2', 'Build'), (37, '55% 22%', 'Month 3', 'Become')]
tri = ''.join(f'<img class="f" src="{ph(k)}" style="left:{70+i*292}px;top:300px;width:276px;height:720px;object-position:{pos}" {A}><div class="mo" style="left:{70+i*292}px"><span>{m}</span>{w}</div>' for i, (k, pos, m, w) in enumerate(MON))
P['WA6'] = doc('WA6 · like 55 · triptych · 90 day winter arc plan', """
.kick{position:absolute;left:0;right:0;top:170px;text-align:center;font-weight:900;font-size:96px;letter-spacing:-.055em;line-height:.9;color:#1E3A6E;text-transform:uppercase}
.mo{position:absolute;top:1040px;width:276px;text-align:center;font-weight:900;font-size:58px;letter-spacing:-.04em;color:#1E3A6E}
.mo span{display:block;font-weight:600;font-size:22px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:6px}
.it{position:absolute;left:60px;right:60px;top:1200px;text-align:center;font-style:italic;font-weight:400;font-size:48px;letter-spacing:-.03em;color:#1E3A6E}
""", f"""{T()}<div class="kick">90-day winter arc</div>{tri}<div class="it">who do you want to be on March 1?</div>{U('#1E3A6E')}""", bg='#DCE6F2')

for k, v in P.items():
    open(os.path.join(D, f'{k}.html'), 'w').write(v)
print(sorted(P))
