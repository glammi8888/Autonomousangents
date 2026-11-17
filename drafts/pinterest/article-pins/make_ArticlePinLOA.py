# ArticlePinLOA (law-of-assumption), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, taken from the live article's "How to Use It This Week" + "Assumptions That Turn Into Moves" (issue11.app/blog/law-of-assumption).
# Keyword check: ../2026-11-17-law-of-assumption-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 17, 2026","law of assumption, the part that works 🫧",
  [("how i use it this week",["write it in present tense. one sentence","describe a normal wednesday as her","find one thing she does that i don't","do it this week. pick a day + time","keep proof"]),
   ("assumption → move",["“I'm financially calm” → one automatic transfer, even $20","“I'm a person who runs” → 15 min, saturday 8am"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinLOA.dc.html','w').write(ns['doc']('Article pin · law-of-assumption · ready for Framer',inner,bg))
print('ok',fs)
