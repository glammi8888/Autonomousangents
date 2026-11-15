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
def pin(lines, size, dark, pos="mid", align="left", track=-0.04, lh=0.94):
    bg, fg = (INK, W) if dark else (W, INK)
    v = {"top": "justify-content:flex-start; padding-top:150px", "mid": "justify-content:center", "low": "justify-content:flex-end; padding-bottom:230px"}[pos]
    q = "<br>".join(lines)
    inner = (f'<div style="position:absolute; inset:0; padding:0 80px; box-sizing:border-box; display:flex; flex-direction:column; {v}; color:{fg}">'
             f'<p style="margin:0; font-size:{size}px; font-weight:800; letter-spacing:{track}em; line-height:{lh}; text-align:{align}; white-space:nowrap">{q}</p></div>'
             f'<p style="position:absolute; left:80px; right:80px; bottom:76px; margin:0; color:{fg}; font-size:34px; font-weight:600; letter-spacing:0.01em; text-align:{align}">issue11.app</p>')
    return bg, inner

# Quotes v2 (Nov 15): rebuilt from the viral quote-pin themes (VIRAL-QUOTES.md), in Megan's lexicon and real voice.
# Megan via OPS: "Become your own dream girl" exactly as written (capital B, no period), ISSUE11's brand line: biggest set in the batch.
P = [
 ("Pin37", "Become your own dream girl", pin(["Become", "your own", "dream", "girl"], 196, True, "mid")),
 ("Pin38", "I said I'd do it. so now I have to.", pin(["I said I’d", "do it.", "so now I", "have to."], 178, False, "top")),
 ("Pin39", "I glowed up by going to bed earlier lol", pin(["I glowed up", "by going", "to bed", "earlier lol"], 150, True, "low")),
 ("Pin40", "I'm acting like it's already mine. don't ruin it for me.", pin(["I’m acting", "like it’s", "already mine.", "don’t ruin it", "for me."], 128, False, "mid")),
 ("Pin41", "I'm the art director of my life.", pin(["I’m the", "art director", "of my life."], 160, True, "top")),
 ("Pin42", "me 🫱🏻‍🫲🏽 2027", pin(["me 🫱🏻‍🫲🏽", "2027"], 230, False, "mid", "center")),
 ("Pin43", "I'm paying off the card first. then the trip.", pin(["I’m paying", "off the card", "first. then", "the trip."], 150, True, "low")),
 ("Pin44", "unrealistic? yes. I'm doing it anyway.", pin(["unrealistic?", "yes.", "I’m doing it", "anyway."], 150, False, "top")),
 ("Pin45", "I'm picking me this year. sorry in advance.", pin(["I’m picking", "me this year.", "sorry in", "advance."], 150, True, "mid")),
 ("Pin46", "can't talk rn. I'm rebranding.", pin(["can’t talk", "rn. I’m", "rebranding."], 152, False, "low")),
 ("Pin47", "I only attract the best of the best", pin(["I only", "attract", "the best of", "the best"], 170, False, "mid")),
 ("Pin48", "I only get to experience the best. The best friends, connections, family, restaurants, clothing, etc... the universe really spoils me", pin(["I only get to", "experience the", "best. The best", "friends, connections,", "family, restaurants,", "clothing, etc...", "the universe", "really spoils me"], 86, True, "mid")),
 ("Pin49", "I am so fit and healthy and I am proud to say that I love my own body", pin(["I am so fit", "and healthy", "and I am proud", "to say that I", "love my own", "body"], 120, False, "mid")),
 ("Pin50", "A healthy mind, a fit body, and lots of money $$$", pin(["A healthy mind,", "a fit body,", "and lots of", "money $$$"], 120, True, "mid")),
 ("Pin51", "I'm the art director of my life. I create it page by page. I make my own opportunities.", pin(["I’m the art", "director of", "my life.", "I create it", "page by page.", "I make my own", "opportunities."], 112, False, "mid")),
]
for k, t, (bg, inner) in P:
    open(f"{R}/project/{k}.dc.html", "w").write(doc(f"Quote · {t}", inner, bg))
print("ok", len(P))
