# Pinterest batch 4 (Nov 15, 2026): quote-only pins. Megan: "We should do pins that are quotes only with just our website in the bottom too".
# Usage: python3 generator-b4.py <out_root>  -> writes <out_root>/project/Pin37..Pin46.dc.html
# Format: one quote in big Inter Tight, black on white or white on black, "issue11.app" small at the bottom. Nothing else
# (no logo, no CTA bar, no photo, no kicker, no quote marks). Reuses the doc() shell from ../batch2/generator-b2.py.
import sys, os
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../batch2/generator-b2.py")).read()
INK = "#0D0D0D"; W = "#FFFFFF"
EMO = "'Apple Color Emoji','Noto Color Emoji','Segoe UI Emoji'"
def doc(title, inner, bg):
    exec_src = src[src.index("def doc("):src.index("def foot(")]
    ns = {"INK": INK, "EMO": EMO}; exec(exec_src, ns); return ns["doc"](title, inner, bg)

# pos: where the quote block sits ("top" | "mid" | "low"); size in px at 1000 wide; lines joined with <br>
def pin(lines, size, dark, pos="mid", align="left", track=-0.05, lh=0.94):
    bg, fg = (INK, W) if dark else (W, INK)
    v = {"top": "justify-content:flex-start; padding-top:150px", "mid": "justify-content:center", "low": "justify-content:flex-end; padding-bottom:230px"}[pos]
    q = "<br>".join(lines)
    inner = (f'<div style="position:absolute; inset:0; padding:0 80px; box-sizing:border-box; display:flex; flex-direction:column; {v}; color:{fg}">'
             f'<p style="margin:0; font-size:{size}px; font-weight:800; letter-spacing:{track}em; line-height:{lh}; text-align:{align}">{q}</p></div>'
             f'<p style="position:absolute; left:80px; right:80px; bottom:76px; margin:0; color:{fg}; font-size:34px; font-weight:600; letter-spacing:0.01em; text-align:{align}">issue11.app</p>')
    return bg, inner

P = [
 ("Pin37", "i'm the art director of my life", pin(["i’m the", "art director", "of my life."], 150, False, "low")),
 ("Pin38", "same girl, bigger dreams", pin(["same girl,", "bigger", "dreams."], 200, True, "top")),
 ("Pin39", "i'm not behind. i'm becoming.", pin(["i’m not", "behind.", "i’m", "becoming."], 190, False, "mid")),
 ("Pin40", "i keep my circle small", pin(["i keep", "my circle", "small."], 196, True, "low")),
 ("Pin41", "i'm in my building era", pin(["i’m in my", "building", "era."], 196, False, "top")),
 ("Pin42", "become YOU", pin(["become", "YOU."], 250, True, "mid")),
 ("Pin43", "you don't have to see it to believe it", pin(["you don’t have to see it to believe it.", "but you have to participate to create it."], 104, False, "mid", lh=1.0)),
 # Megan via OPS: "Become your own dream girl" exactly as written (capital B, no period). ISSUE11's brand line: biggest set in the batch.
 ("Pin44", "Become your own dream girl", pin(["Become", "your own", "dream", "girl"], 230, True, "mid")),
 ("Pin45", "me 🫱🏻‍🫲🏽 2027", pin(["me 🫱🏻‍🫲🏽", "2027"], 230, False, "mid", "center")),
 ("Pin46", "can't talk rn. i'm rebranding.", pin(["can’t talk rn.", "i’m", "rebranding."], 170, True, "low")),
]
for k, t, (bg, inner) in P:
    open(f"{R}/project/{k}.dc.html", "w").write(doc(f"Quote · {t}", inner, bg))
print("ok", len(P))
