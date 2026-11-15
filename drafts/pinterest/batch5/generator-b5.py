# Pinterest batch 5 (Nov 15, 2026): Megan's affirmations, word for word (drafts/pinterest/affirmations/BANK.md).
# Megan: "The quotes still sound way too AI it needs to stop" -> no agent copy; lines only (curly apostrophes allowed).
# Line 13 ("Doors and opportunities always come for me") cut by Megan. Added by Megan: "2027 is the year I lifemaxx" (Pin88)
# and "My face card is absolutely lethal" (Pin89) -> 14 pins, Pin76..Pin89.
# Reuses the 14-style sampler (../styles/generator-styles.py). No serif, no pastel backgrounds (waiting on Megan).
# Usage: python3 generator-b5.py <out_root>  -> writes <out_root>/project/Pin76..Pin89.dc.html
import sys, os, importlib.util
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("st", f"{HERE}/../styles/generator-styles.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)  # its __main__ block doesn't run on import

def flash(k, pos, text, size=110, top=900):
    """Style 4 (text over a flash photo) with a chosen library photo; text kept below the faces."""
    bg, inner = st.s4(text, size)
    inner = inner.replace(st.ph("m28", "40% 30%", "left:0; top:0; width:1000px; height:1390px"),
                          st.ph(k, pos, "left:0; top:0; width:1000px; height:1390px")
                          + f'<div style="position:absolute; left:0; right:0; top:{top-260}px; height:{1650-top}px; background:linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.78) 50%)"></div>'
                          ).replace("top:900px", f"top:{top}px")
    return bg, inner

def withlogo(r, white, left=None):
    """Logo on every pin (agent rule): the sampler's text-only styles had none, so add it at the top."""
    bg, inner = r
    pos = f"left:{left}px" if left is not None else "left:50%; transform:translateX(-50%)"
    inner = inner.replace("left:100px; right:80px; top:96px", "left:100px; right:80px; top:150px")  # repeat page: clear the logo
    return bg, f'<div style="position:absolute; top:60px; {pos}">{st.logo(white)}</div>' + inner

# (pin, style, line exactly as Megan wrote it, render)
P = [("Pin76", "3 · Night card", "My life can do a 180 in just 1 year", withlogo(st.s3("My life can<br>do a 180 in<br>just 1 year", 120), True)),
     ("Pin77", "4 · Flash photo (money, m25)", "I wake up to money", flash("m25", "50% 20%", "I wake up<br>to money", 130, 1000)),
     ("Pin78", "4 · Flash photo (love, l23)", "The love of my life is coming to me", flash("l23", "55% 25%", "The love of<br>my life is<br>coming to me", 104, 930)),
     ("Pin79", "7 · Giant word + line", "I am the prize, always", withlogo(st.s7("prize", "I am the prize, always"), False)),
     ("Pin80", "5 · SAY IT WITH ME", "I only date a guy if he can afford me", withlogo(st.s5("I only date<br>a guy if he<br>can afford me", 90), False, 80)),
     ("Pin81", "8 · Phone Notes", "I cannot wait to prove to the people doubting me that they were wrong",
               st.s8("I cannot wait to<br>prove to the<br>people doubting<br>me that they<br>were wrong", 92)),
     ("Pin82", "6 · All caps Lilac on black", "I love my hot bod", withlogo(st.s6("I love<br>my hot<br>bod", 190), True)),
     ("Pin83", "9 · Magazine pull quote (money, m27)", "I’m making money in my sleep", st.s9("I’m making<br>money<br>in my<br>sleep", "m27", "50% 30%", 83, 86)),
     ("Pin84", "3 · Night card", "I’m the luckiest girl on the planet", withlogo(st.s3("I’m the<br>luckiest girl<br>on the planet", 118), True)),
     ("Pin85", "7 · Giant word + line", "Dream life is on its way", withlogo(st.s7("dream", "Dream life is on its way"), False)),
     ("Pin86", "1 · Repeat page", "My dream life wants me", withlogo(st.s1("My dream life wants me", 14, 52), False, 100)),
     ("Pin87", "8 · Phone Notes", "I’m the girl who always makes it work", st.s8("I’m the girl<br>who always<br>makes it work", 108)),
     ("Pin88", "3 · Night card", "2027 is the year I lifemaxx", withlogo(st.s3("2027 is<br>the year I<br>lifemaxx", 150), True)),
     ("Pin89", "4 · Flash photo (beauty, e24)", "My face card is absolutely lethal", flash("e24", "50% 15%", "My face card<br>is absolutely<br>lethal", 104, 1020))]
if __name__ == "__main__":
    for k, style, line, (bg, inner) in P:
        open(f"{R}/project/{k}.dc.html", "w").write(st.doc(f"Affirmation {style} · {line}", inner, bg))
    print("ok", len(P))
