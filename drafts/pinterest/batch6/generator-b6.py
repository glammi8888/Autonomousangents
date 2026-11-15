# Pinterest batch 6 (Nov 15, 2026): more "reminder 🫧" Notes pins (style 8).
# Megan on Pin81: "This is so good we need a few more like This". Lines are Megan's own, word for word
# (drafts/pinterest/affirmations/BANK.md); no agent copy.
# Usage: python3 generator-b6.py <out_root>  -> writes <out_root>/project/Pin90..Pin102.dc.html
import sys, os, importlib.util
R = sys.argv[1]; os.makedirs(f"{R}/project", exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("st", f"{HERE}/../styles/generator-styles.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)

P = [("Pin90", "I glowed up so hard now my enemies are crying", "I glowed up<br>so hard now<br>my enemies<br>are crying", 112),
     ("Pin91", "I glowed up so hard now my ex is crying", "I glowed up<br>so hard now<br>my ex is<br>crying", 120),
     ("Pin92", "I make way more money than what I'm able to spend", "I make way<br>more money<br>than what I’m<br>able to spend", 108),
     ("Pin93", "My business is bringing sooooo much money", "My business<br>is bringing<br>sooooo much<br>money", 112),
     ("Pin94", "I only attract the best of the best", "I only attract<br>the best of<br>the best", 112),
     ("Pin95", "I am my own dream girl", "I am my own<br>dream girl", 124),
     ("Pin96", "Thank you universe for all the blessings", "Thank you<br>universe for<br>all the<br>blessings", 120),
     ("Pin97", "I am so fit and healthy and I am proud to say that I love my own body",
               "I am so fit and<br>healthy and I am<br>proud to say that<br>I love my own<br>body", 86),
     ("Pin98", "I only get to experience the best. The best friends, connections, family, restaurants, clothing, etc... the universe really spoils me",
               "I only get to<br>experience the best.<br>The best friends,<br>connections, family,<br>restaurants, clothing,<br>etc... the universe<br>really spoils me", 74),
     ("Pin99", "I'm the art director of my life. I create it page by page. I make my own opportunities.",
               "I’m the art director<br>of my life. I create<br>it page by page.<br>I make my own<br>opportunities.", 80),
     # Megan's own rewrites of viral lines (Nov 15): "17. I am no longer proving my worth..." and "4. Get up girl..."
     ("Pin100", "I am no longer proving my worth to someone. You either value me or you're OUT!",
               "I am no longer<br>proving my worth<br>to someone.<br>You either value<br>me or you’re<br>OUT!", 90),
     ("Pin101", "Get up girl, you got people to prove wrong", "Get up girl,<br>you got people<br>to prove wrong", 108),
     ("Pin102", "Imagine what your bullies will feel when they see you succeed",
               "Imagine what<br>your bullies<br>will feel when<br>they see you<br>succeed", 100)]
if __name__ == "__main__":
    for k, line, text, size in P:
        bg, inner = st.s8(text, size)
        open(f"{R}/project/{k}.dc.html", "w").write(st.doc(f"Affirmation 8 · Phone Notes · {line}", inner, bg))
    print("ok", len(P))
