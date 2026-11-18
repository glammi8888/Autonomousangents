# ArticlePinSM (scripting-manifestation), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, from the live article's "The 5-Line Scripting Method" + the Money example (issue11.app/blog/scripting-manifestation).
# Keyword check: ../2026-11-17-scripting-manifestation-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","scripting manifestation, my 5‑line method ✍️",
  [("the 5 lines",["the scene. where i am, present tense","one detail i can see or touch","who i am now","the line to repeat","the move: one step, a day + a time"]),
   ("example",["“Money is calm in my house.” → sunday 10am: one automatic transfer"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinSM.dc.html','w').write(ns['doc']('Article pin · scripting-manifestation · ready for Framer',inner,bg))
print('ok',fs)
