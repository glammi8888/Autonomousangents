# ArticlePinVBQ (vision-board-quotes), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Quotes: BANK.md lines only, word for word (Megan's rule). The article's own 80 lines are not in BANK, so they are not quoted here (issue11.app/blog/vision-board-quotes).
# Keyword check: ../2026-11-17-vision-board-quotes-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","vision board quotes for 2027 ✨",
  [("on my board",["Dream life is on its way","My dream life wants me","I have big plans.","My life can do a 180 in just 1 year","Rich & Stylish 2027","it all worked out"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinVBQ.dc.html','w').write(ns['doc']('Article pin · vision-board-quotes · ready for Framer',inner,bg))
print('ok',fs)
