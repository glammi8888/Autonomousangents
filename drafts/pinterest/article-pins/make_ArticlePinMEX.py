# ArticlePinMEX (manifestation-examples), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, from the live article's example lists (want + "First move") (issue11.app/blog/manifestation-examples).
# Keyword check: ../2026-11-17-manifestation-examples-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","manifestation examples + my first move 💫",
  [("want → first move",["emergency fund → automate a transfer every payday","a raise → list 3 results, with numbers","a closet i love → remove 10 things i never wear","a calmer mind → 5 min writing before my phone"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinMEX.dc.html','w').write(ns['doc']('Article pin · manifestation-examples · ready for Framer',inner,bg))
print('ok',fs)
