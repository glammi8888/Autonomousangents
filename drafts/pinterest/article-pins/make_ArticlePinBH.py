# ArticlePinBH (becoming-her), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, from the live article's "Become Her This Week: 6 Small Moves" + the 7am row of "Old You vs Her" (issue11.app/blog/becoming-her).
# Keyword check: ../2026-11-17-becoming-her-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","becoming her, 6 small moves this week 🎀",
  [("this week",["dress like her once. a normal day","keep one promise to myself","say no once. no long explanation","fix one surface. start with a counter","talk to myself like she would","sunday: one line of proof"]),
   ("old me → her",["7am: phone first → water, light, then phone"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinBH.dc.html','w').write(ns['doc']('Article pin · becoming-her · ready for Framer',inner,bg))
print('ok',fs)
