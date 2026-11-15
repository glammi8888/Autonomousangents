# Quote pin styles · 20 options (Nov 15, 2026): Pin103..Pin122, one NEW quote-pin format each, so Megan can pick by number.
# Megan: "Now work with Claude design and give me 20 different pin styles just for the quotes".
# Copy rule (Megan: "The quotes still sound way too AI it needs to stop"): every line is from drafts/pinterest/affirmations/BANK.md,
# word for word (only straight -> curly apostrophes, line breaks, and CSS uppercase on some formats). No invented labels/kickers.
# Pain/spite lines first (Megan: "It's fueled by pain and that is the best").
# Formats recreated generically from viral quote pins (2026-11-15-viral-quote-pins.json / spite-quote-pins.json):
# no real app logos, usernames or trademarks. Inter Tight only, except Pin122 (RULE-BREAKER, monospace) for Megan to decide.
# Lilac accent = #D9B3FF, the colour actually on Pin82 (the brief said #C8A2F0; Pin82's file has #D9B3FF).
# Usage: python3 generator-styles2.py <out_root>  -> writes <out_root>/project/Pin103..Pin122.dc.html
import sys, os, importlib.util
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("st", f"{HERE}/../styles/generator-styles.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
INK, W, LILAC, GREY = st.INK, st.W, "#D9B3FF", "#8A8A8E"

def top_logo(white=False, top=60): return f'<div style="position:absolute; top:{top}px; left:50%; transform:translateX(-50%)">{st.logo(white)}</div>'
def url(fg, bottom=64, size=30): return st.url(fg, "center", bottom, size, 600)
def P_(text, size, weight=700, color=INK, extra=""):
    return f'<p style="margin:0; font-size:{size}px; font-weight:{weight}; color:{color}; letter-spacing:-0.03em; line-height:1.08; white-space:nowrap; {extra}">{text}</p>'

# 103 · Text-post screenshot (generic social post, no app branding, no username)
def s103():
    av = f'<div style="width:110px; height:110px; border-radius:50%; background:{INK}; display:flex; align-items:center; justify-content:center">{st.logo(True)}</div>'
    post = (f'<div style="position:absolute; left:80px; right:80px; top:0; bottom:120px; display:flex; flex-direction:column; justify-content:center">'
            f'<div style="display:flex; align-items:center; gap:28px">{av}{st.logo(False, "height:46px")}</div>'
            f'<div style="margin-top:48px">{P_("I cannot wait<br>to prove to the<br>people doubting<br>me that they<br>were wrong", 92, 600, INK, "letter-spacing:-0.025em; line-height:1.18")}</div>'
            f'<p style="margin:44px 0 0; font-size:30px; color:{GREY}; font-weight:500">11:47 PM · Nov 15, 2026</p>'
            f'<div style="margin-top:36px; height:2px; background:#E3E3E6"></div>'
            f'<div style="display:flex; gap:120px; margin-top:30px">' + "".join(f'<span style="width:44px; height:40px; border:3px solid {GREY}; border-radius:{r}"></span>' for r in ("50% 50% 50% 0", "10px", "50%", "6px")) + '</div>'
            f'<div style="margin-top:30px; height:2px; background:#E3E3E6"></div></div>')
    return (W, post + url(INK))

# 104 · Message bubbles (dark mode chat, our lilac instead of any app colour)
def s104():
    def bub(t, mt): return (f'<div style="align-self:flex-end; margin-top:{mt}px; max-width:800px; background:{LILAC}; color:{INK}; border-radius:54px 54px 14px 54px; padding:34px 46px">'
                            f'{P_(t, 72, 600, INK, "line-height:1.15; letter-spacing:-0.02em")}</div>')
    head = (f'<div style="position:absolute; top:70px; left:0; right:0; display:flex; flex-direction:column; align-items:center; gap:18px">'
            f'<div style="width:120px; height:120px; border-radius:50%; background:#2C2C2E; display:flex; align-items:center; justify-content:center">{st.logo(True)}</div></div>'
            f'<div style="position:absolute; top:240px; left:0; right:0; height:2px; background:#1F1F21"></div>')
    msgs = (f'<div style="position:absolute; left:70px; right:60px; top:260px; bottom:250px; display:flex; flex-direction:column; justify-content:center">'
            + bub("I am no longer proving<br>my worth to someone.", 0) + bub("You either value me<br>or you’re OUT!", 22) + '</div>')
    field = f'<div style="position:absolute; left:70px; right:70px; bottom:140px; height:84px; border:3px solid #3A3A3C; border-radius:44px"></div>'
    return ("#000", head + msgs + field + url(W, 50, 28))

# 105 · Sticky note with tape, on black
def s105():
    note = (f'<div style="position:absolute; left:110px; top:330px; width:780px; height:780px; background:{W}; transform:rotate(-2.5deg); box-shadow:0 30px 60px rgba(0,0,0,0.5); padding:90px 70px; box-sizing:border-box; display:flex; align-items:center">'
            f'<div style="position:absolute; left:50%; top:-34px; width:260px; height:78px; margin-left:-130px; background:rgba(235,235,235,0.75); transform:rotate(3deg)"></div>'
            f'{P_("Get up girl,<br>you got people<br>to prove wrong", 92, 700, INK, "letter-spacing:-0.035em; line-height:1.12")}</div>')
    return (INK, top_logo(True, 90) + note + url(W, 90))

# 106 · Receipt
def s106():
    dash = f'<div style="margin:50px 0; border-top:4px dashed {INK}"></div>'
    rows = "".join(f'<p style="margin:0; font-size:100px; font-weight:800; letter-spacing:-0.025em; line-height:1.12; text-transform:uppercase; white-space:nowrap">{t}</p>' for t in ("I glowed up", "so hard", "now my ex", "is crying"))
    bars = "".join(f'<span style="display:inline-block; width:{w}px; height:120px; background:{INK}; margin-right:{m}px"></span>' for w, m in [(6,5),(3,7),(9,4),(3,4),(6,9),(3,5),(12,4),(3,7),(6,4),(9,6),(3,4),(6,8),(3,4),(9,5),(3,7),(6,4),(12,6),(3,4),(6,5),(3,8),(9,4),(3,6),(6,4),(3,5),(9,7),(3,4),(6,6),(12,4),(3,5),(6,0)])
    zig = f'background:linear-gradient(-45deg, transparent 16px, {W} 0) bottom left, linear-gradient(45deg, transparent 16px, {W} 0) bottom left; background-size:32px 100%; background-repeat:repeat-x'
    paper = (f'<div style="position:absolute; left:110px; right:110px; top:90px; height:1330px; {zig}; padding:0 70px 30px; display:flex; flex-direction:column; justify-content:center; box-sizing:border-box; color:{INK}">'
             f'<div style="text-align:center">{st.logo()}</div>'
             f'<p style="margin:22px 0 0; text-align:center; font-size:26px; font-weight:600; letter-spacing:0.12em; font-variant-numeric:tabular-nums">15/11/2026 · 23:47</p>'
             + dash + rows + dash +
             f'<div style="text-align:center; margin-top:40px; white-space:nowrap">{bars}</div>'
             f'<p style="margin:26px 0 0; text-align:center; font-size:34px; font-weight:700; letter-spacing:0.04em">issue11.app</p></div>')
    return (INK, paper)

# 107 · Highlighted book page (body text shown as grey bars, never invented words)
def s107():
    def bars(n, widths=(100, 96, 100, 88, 100, 93, 70)):
        return "".join(f'<div style="height:22px; width:{widths[i % len(widths)]}%; background:#D8D6D2; border-radius:3px; margin:0 0 30px"></div>' for i in range(n))
    hl = f'background:linear-gradient(transparent 52%, {LILAC} 52%, {LILAC} 94%, transparent 94%); -webkit-box-decoration-break:clone; box-decoration-break:clone; padding:0 6px'
    q = (f'<p style="margin:16px 0 46px; font-size:70px; font-weight:600; letter-spacing:-0.025em; line-height:1.3">'
         + "<br>".join(f'<span style="{hl}">{t}</span>' for t in ("Imagine what your", "bullies will feel when", "they see you succeed")) + '</p>')
    page = (f'<div style="position:absolute; left:70px; right:70px; top:70px; bottom:70px; background:{W}; padding:110px 80px 0; box-sizing:border-box">'
            f'{bars(6)}{q}{bars(6)}'
            f'<div style="position:absolute; left:80px; right:80px; bottom:60px; display:flex; justify-content:space-between; align-items:center">'
            f'<span style="font-size:30px; font-weight:600">issue11.app</span>{st.logo()}</div></div>')
    return (INK, page)

# 108 · Lock screen wallpaper with clock (money photo m24, woman small mid-frame, clock over the sky)
def s108():
    img = st.ph("m24", "50% 0%", "left:0; top:470px; width:1000px; height:1030px")  # photo starts under the clock: clock never on her face
    fade = '<div style="position:absolute; left:0; right:0; top:470px; height:160px; background:linear-gradient(#000, rgba(0,0,0,0))"></div>'
    clock = (f'<div style="position:absolute; left:0; right:0; top:110px; text-align:center; color:{W}">'
             f'<p style="margin:0; font-size:40px; font-weight:600">Friday 1 January</p>'
             f'<p style="margin:0; font-size:270px; font-weight:700; letter-spacing:-0.04em; line-height:1">7:00</p></div>')
    card = (f'<div style="position:absolute; left:50px; right:50px; top:1000px; background:rgba(28,28,30,0.82); border-radius:44px; padding:34px 40px; display:flex; gap:30px; align-items:center">'
            f'<div style="flex:none; width:104px; height:104px; border-radius:26px; background:{W}; display:flex; align-items:center; justify-content:center">{st.logo()}</div>'
            f'{P_("I wake up to money", 70, 700, W, "letter-spacing:-0.03em")}</div>')
    corners = "".join(f'<div style="position:absolute; {s}:80px; bottom:110px; width:96px; height:96px; border-radius:50%; background:rgba(28,28,30,0.6)"></div>' for s in ("left", "right"))
    return (INK, img + fade + clock + card + corners + f'<div style="position:absolute; left:50%; bottom:40px; width:300px; margin-left:-150px; height:10px; border-radius:5px; background:{W}"></div>'
            + url(W, 170, 30).replace("font-weight:600", "font-weight:700; text-shadow:0 1px 8px rgba(0,0,0,0.9)"))

# 109 · Magazine cover with our logo as the masthead (e35 beauty portrait)
def s109():
    img = st.ph("e35", "50% 30%", "left:0; top:0; width:1000px; height:1500px")
    fade = '<div style="position:absolute; left:0; right:0; bottom:0; height:640px; background:linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.8) 60%)"></div>'
    mast = f'<div style="position:absolute; left:0; right:0; top:50px; text-align:center">{st.logo(False, "height:150px")}</div>'
    line = (f'<div style="position:absolute; left:60px; right:60px; bottom:150px">'
            f'{P_("My face card<br>is absolutely<br>lethal", 128, 800, W, "letter-spacing:-0.05em; line-height:0.92; text-transform:uppercase")}</div>')
    return (INK, img + fade + mast + line + st.url(W, "left", 70, 30, 600).replace("left:80px", "left:60px"))

# 110 · Tabloid front page (e36)
def s110():
    def blk(t, inv):
        bg, fg = (INK, W) if inv else (W, INK)
        return f'<span style="display:inline-block; background:{bg}; color:{fg}; padding:0 18px; margin:0 0 10px; font-size:132px; font-weight:800; letter-spacing:-0.05em; line-height:1.0; text-transform:uppercase; white-space:nowrap">{t}</span><br>'
    band = (f'<div style="position:absolute; left:0; right:0; top:0; height:110px; background:{INK}; padding:0 50px; box-sizing:border-box; display:flex; justify-content:space-between; align-items:center">'
            f'{st.logo(True)}<span style="color:{W}; font-size:30px; font-weight:600">issue11.app</span></div>')
    head = '<div style="position:absolute; left:32px; right:20px; top:140px">' + blk("I glowed up", True) + blk("so hard now", False) + blk("my enemies", True) + blk("are crying", False) + '</div>'
    photo = (f'<div style="position:absolute; left:50px; right:50px; top:760px; bottom:50px; border:10px solid {INK}; overflow:hidden">'
             + st.ph("e36", "50% 18%", "left:0; top:0; width:100%; height:100%") + '</div>')
    return (W, band + head + photo)

# 111 · Ransom / cut-out letters
def s111():
    sty = [(W, INK, 800, "normal", -3), (INK, W, 500, "italic", 2), (LILAC, INK, 700, "normal", -1), (W, INK, 400, "italic", 3), (INK, W, 800, "normal", -2)]
    def cut(t, i, fs, pad="4px 18px"):
        bg, fg, wt, it, rot = sty[i % len(sty)]
        bd = f"border:3px solid {INK};" if bg == W else ""
        return f'<span style="display:inline-block; background:{bg}; color:{fg}; {bd} font-size:{fs}px; font-weight:{wt}; font-style:{it}; transform:rotate({rot}deg); padding:{pad}; margin:10px 8px; line-height:1.05">{t}</span>'
    w1 = cut("I", 4, 170) + cut("am", 1, 150) + cut("the", 3, 150)
    w2 = "".join(cut(c, j + 2, 190, "0 14px") for j, c in enumerate("prize,"))
    w3 = cut("always", 0, 170)
    body = (f'<div style="position:absolute; left:40px; right:40px; top:150px; bottom:150px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center">'
            f'<div>{w1}</div><div style="margin-top:20px; white-space:nowrap">{w2}</div><div style="margin-top:20px">{w3}</div></div>')
    return ("#F4F4F4", top_logo(False, 70) + body + url(INK, 70))

# 112 · Film still with subtitles (l23, letterboxed)
def s112():
    frame = f'<div style="position:absolute; left:0; right:0; top:230px; height:1040px; overflow:hidden">' + st.ph("l23", "45% 30%", "left:0; top:0; width:100%; height:100%") + '</div>'
    sub = ('<div style="position:absolute; left:40px; right:40px; top:1060px; text-align:center">'
           + P_("I only date a guy<br>if he can afford me", 62, 600, W, "letter-spacing:-0.01em; line-height:1.2; text-shadow:0 0 6px #000, 0 0 3px #000, 0 2px 10px rgba(0,0,0,0.9)") + '</div>')
    return ("#000", top_logo(True, 95) + frame + sub + url(W, 95))

# 113 · Label-maker tape
def s113():
    def tape(t, rot, ml):
        return (f'<div style="margin:0 0 46px {ml}px; display:inline-block; background:{INK}; color:{W}; padding:22px 40px; transform:rotate({rot}deg); box-shadow:0 8px 18px rgba(0,0,0,0.25); '
                f'font-size:92px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; line-height:1; white-space:nowrap; text-shadow:0 2px 0 rgba(255,255,255,0.18), 0 -1px 0 rgba(0,0,0,0.6)">{t}</div><br>')
    body = ('<div style="position:absolute; left:60px; right:40px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center">'
            + tape("I’m the girl", -2, 0) + tape("who always", 1.5, 70) + tape("makes it work", -1, 20) + '</div>')
    return (W, top_logo(False, 80) + body + url(INK, 80))

# 114 · Giant number, Swiss layout (vertical 180 down the left)
def s114():
    num = (f'<div style="position:absolute; left:20px; top:40px; bottom:40px; width:440px; display:flex; align-items:center; justify-content:center">'
           f'<p style="margin:0; writing-mode:vertical-rl; transform:rotate(180deg); font-size:540px; font-weight:800; letter-spacing:-0.045em; line-height:0.8">180</p></div>')
    rule = f'<div style="position:absolute; left:500px; top:80px; bottom:80px; width:4px; background:{INK}"></div>'
    txt = (f'<div style="position:absolute; left:550px; right:40px; top:80px">{st.logo()}</div>'
           f'<div style="position:absolute; left:550px; right:30px; bottom:170px">{P_("My life<br>can do<br>a 180 in<br>just 1 year", 92, 700, INK, "letter-spacing:-0.04em; line-height:1.0")}</div>'
           f'<p style="position:absolute; left:550px; bottom:80px; margin:0; font-size:30px; font-weight:600">issue11.app</p>')
    return (W, num + rule + txt)

# 115 · Calendar page, January 2027 (1 Jan 2027 is a Friday)
def s115():
    days = "".join(f'<div style="text-align:center; font-size:30px; font-weight:700">{d}</div>' for d in "MTWTFSS")
    cells = ['' for _ in range(4)] + [str(i) for i in range(1, 32)]
    while len(cells) % 7: cells.append('')
    def c(v):
        if v == "1": return f'<div style="display:flex; justify-content:center"><span style="width:76px; height:76px; border-radius:50%; background:{LILAC}; display:flex; align-items:center; justify-content:center; font-size:38px; font-weight:800">1</span></div>'
        return f'<div style="text-align:center; font-size:36px; font-weight:500; line-height:76px">{v}</div>'
    grid = (f'<div style="position:absolute; left:80px; right:80px; top:720px; display:grid; grid-template-columns:repeat(7,1fr); row-gap:14px">{days}' + "".join(c(v) for v in cells) + '</div>')
    hdr = (f'<div style="position:absolute; left:80px; right:80px; top:600px; display:flex; justify-content:space-between; align-items:baseline; border-bottom:4px solid {INK}; padding-bottom:20px">'
           f'<span style="font-size:52px; font-weight:800; letter-spacing:-0.02em">January</span><span style="font-size:52px; font-weight:500">2027</span></div>')
    line = f'<div style="position:absolute; left:80px; right:60px; top:180px">{P_("2027 is the year<br>I lifemaxx", 124, 800, INK, "letter-spacing:-0.05em; line-height:0.98")}</div>'
    return (W, top_logo(False, 70).replace("left:50%; transform:translateX(-50%)", "left:80px") + line + hdr + grid + url(INK, 70))

# 116 · Search bar + photo results grid (dream-life photos: closets e20, e21, e22, money bed m26)
def s116():
    bar = (f'<div style="position:absolute; left:60px; right:60px; top:170px; height:130px; border:5px solid {INK}; border-radius:70px; display:flex; align-items:center; padding:0 40px; gap:30px; box-sizing:border-box">'
           f'<span style="position:relative; flex:none; width:44px; height:44px"><span style="position:absolute; left:0; top:0; width:30px; height:30px; border:6px solid {INK}; border-radius:50%"></span><span style="position:absolute; right:-2px; bottom:0; width:18px; height:6px; background:{INK}; transform:rotate(45deg)"></span></span>'
           f'{P_("Dream life is on its way", 60, 600, INK, "letter-spacing:-0.02em")}<span style="width:5px; height:70px; background:{INK}"></span></div>')
    tiles = [("e21", "50% 40%"), ("m26", "50% 30%"), ("e22", "50% 50%"), ("e20", "50% 55%")]
    grid = ('<div style="position:absolute; left:60px; right:60px; top:350px; bottom:160px; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:20px">'
            + "".join(f'<div style="position:relative; overflow:hidden; border-radius:30px">{st.ph(k, p, "left:0; top:0; width:100%; height:100%")}</div>' for k, p in tiles) + '</div>')
    foot = (f'<div style="position:absolute; left:60px; right:60px; bottom:60px; display:flex; justify-content:space-between; align-items:center">'
            f'<span style="font-size:32px; font-weight:600">issue11.app</span>{st.logo()}</div>')
    return (W, top_logo(False, 70) + bar + grid + foot)

# 117 · Lyric card over a photo (generic, no music-app branding; e27 woman at a desk)
def s117():
    img = st.ph("e27", "40% 10%", "left:0; top:0; width:1000px; height:1500px")
    card = (f'<div style="position:absolute; left:60px; right:60px; top:700px; background:{INK}; border-radius:40px; padding:48px 52px 44px; box-sizing:border-box; color:{W}">'
            f'<div style="display:flex; align-items:center; gap:24px; margin-bottom:38px"><div style="position:relative; width:90px; height:90px; border-radius:12px; overflow:hidden">{st.ph("e27", "40% 10%", "left:0; top:0; width:100%; height:100%")}</div>{st.logo(True)}</div>'
            f'{P_("I’m the art director<br>of my life. I create<br>it page by page.<br>I make my own<br>opportunities.", 76, 800, W, "letter-spacing:-0.035em; line-height:1.1")}'
            f'<p style="margin:40px 0 0; font-size:30px; font-weight:600">issue11.app</p></div>')
    return (INK, img + card)

# 118 · Polaroid with caption (n16 portrait)
def s118():
    pol = (f'<div style="position:absolute; left:110px; top:250px; width:780px; height:960px; background:{W}; transform:rotate(-2deg); box-shadow:0 30px 60px rgba(0,0,0,0.5); padding:40px; box-sizing:border-box">'
           f'<div style="position:relative; width:700px; height:700px; overflow:hidden">{st.ph("n16", "50% 35%", "left:0; top:0; width:100%; height:100%")}</div>'
           f'<div style="height:180px; display:flex; align-items:center; justify-content:center">{P_("I am my own dream girl", 62, 600, INK, "letter-spacing:-0.03em")}</div></div>')
    return (INK, top_logo(True, 100) + pol + url(W, 100))

# 119 · Mixed roman + italic stack (the format of the top "that girl quotes" pin, 5,518 reactions, in Inter Tight)
def s119():
    def ln(a, b, it_first=False):
        r = f'<span style="font-weight:800; font-style:normal">{a}</span>'
        i = f'<span style="font-weight:400; font-style:italic">{b}</span>'
        return f'<p style="margin:0; font-size:230px; letter-spacing:-0.05em; line-height:1.0; white-space:nowrap">{(i + " " + r) if it_first else (r + " " + i)}</p>'
    body = ('<div style="position:absolute; left:70px; right:40px; top:0; bottom:60px; display:flex; flex-direction:column; justify-content:center">'
            + ln("I", "love") + ln("my", "hot") + f'<p style="margin:0; font-size:230px; font-weight:800; letter-spacing:-0.05em; line-height:1.0">bod</p>' + '</div>')
    return (W, top_logo(False, 80).replace("left:50%; transform:translateX(-50%)", "left:80px") + body + st.url(INK, "left", 80, 30, 600))

# 120 · Felt letter board
def s120():
    grooves = "background:repeating-linear-gradient(#141414 0 14px, #070707 14px 17px)"
    rows = "".join(f'<p style="margin:0 0 26px; color:#F2F2F2; font-size:96px; font-weight:500; letter-spacing:0.1em; line-height:1.15; text-transform:uppercase; white-space:nowrap">{t}</p>' for t in ("I only", "attract", "the best", "of the best"))
    board = (f'<div style="position:absolute; left:60px; right:60px; top:180px; bottom:180px; border:22px solid #2A2A2A; {grooves}; box-sizing:border-box; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center">{rows}</div>')
    return (W, top_logo(False, 80) + board + url(INK, 80))

# 121 · Fortune-cookie slip
def s121():
    slip = (f'<div style="position:absolute; left:60px; right:60px; top:560px; height:330px; background:{W}; transform:rotate(-3deg); box-shadow:0 24px 50px rgba(0,0,0,0.5); display:flex; align-items:center; justify-content:center; text-align:center">'
            f'{P_("I’m the luckiest girl<br>on the planet", 84, 600, INK, "letter-spacing:-0.025em; line-height:1.15")}</div>')
    return (INK, top_logo(True, 100) + slip + url(W, 100))

# 122 · RULE-BREAKER typewriter page (monospace, not Inter Tight). Megan decides.
TYPE = "'Courier Prime', 'Courier New', monospace"
def s122():
    page = (f'<div style="position:absolute; left:70px; right:70px; top:70px; bottom:170px; background:{W}; padding:0 60px; box-sizing:border-box; display:flex; align-items:center; font-family:{TYPE}; color:#151515">'
            f'<p style="margin:0; font-size:100px; font-weight:700; line-height:1.3; letter-spacing:-0.01em; white-space:nowrap">My business<br>is bringing<br>sooooo much<br>money</p></div>')
    foot = (f'<div style="position:absolute; left:70px; right:70px; bottom:60px; display:flex; justify-content:space-between; align-items:center">'
            f'<span style="color:{W}; font-size:30px; font-weight:600">issue11.app</span>{st.logo(True)}</div>')
    return ("#1A1A1A", page + foot)

# (pin, number · style, line exactly as in BANK.md, render)
P = [("Pin103", "1 · Text-post screenshot", "I cannot wait to prove to the people doubting me that they were wrong", s103()),
     ("Pin104", "2 · Message bubbles", "I am no longer proving my worth to someone. You either value me or you're OUT!", s104()),
     ("Pin105", "3 · Sticky note", "Get up girl, you got people to prove wrong", s105()),
     ("Pin106", "4 · Receipt", "I glowed up so hard now my ex is crying", s106()),
     ("Pin107", "5 · Highlighted book page", "Imagine what your bullies will feel when they see you succeed", s107()),
     ("Pin108", "6 · Lock screen with clock", "I wake up to money", s108()),
     ("Pin109", "7 · Magazine cover line", "My face card is absolutely lethal", s109()),
     ("Pin110", "8 · Tabloid front page", "I glowed up so hard now my enemies are crying", s110()),
     ("Pin111", "9 · Ransom cut-out letters", "I am the prize, always", s111()),
     ("Pin112", "10 · Film still subtitles", "I only date a guy if he can afford me", s112()),
     ("Pin113", "11 · Label-maker tape", "I'm the girl who always makes it work", s113()),
     ("Pin114", "12 · Giant number (Swiss)", "My life can do a 180 in just 1 year", s114()),
     ("Pin115", "13 · Calendar page", "2027 is the year I lifemaxx", s115()),
     ("Pin116", "14 · Search bar + results", "Dream life is on its way", s116()),
     ("Pin117", "15 · Lyric card on photo", "I'm the art director of my life. I create it page by page. I make my own opportunities.", s117()),
     ("Pin118", "16 · Polaroid caption", "I am my own dream girl", s118()),
     ("Pin119", "17 · Roman + italic stack", "I love my hot bod", s119()),
     ("Pin120", "18 · Felt letter board", "I only attract the best of the best", s120()),
     ("Pin121", "19 · Fortune slip", "I'm the luckiest girl on the planet", s121()),
     ("Pin122", "20 · RULE-BREAKER typewriter (monospace)", "My business is bringing sooooo much money", s122())]
if __name__ == "__main__":
    for k, style, line, (bg, inner) in P:
        d = st.doc(f"Quote style {style} · {line}", inner, bg)
        if k == "Pin122": d = d.replace("&amp;display=swap", "&amp;family=Courier+Prime:wght@400;700&amp;display=swap")
        open(f"{R}/project/{k}.dc.html", "w").write(d)
    print("ok", len(P))
