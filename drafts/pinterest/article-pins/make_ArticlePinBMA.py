# ArticlePinBMA (best-manifestation-apps), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, from the live article's sections (affirmations / vision board / actually move) + "How to Choose" (issue11.app/blog/best-manifestation-apps).
# Keyword check: ../2026-11-17-best-manifestation-apps-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","best manifestation apps, by what i actually want 📱",
  [("if i want affirmations",["ThinkUp. in my own voice","I Am. on my home screen"]),
   ("if i want a vision board",["Perfectly Happy","Canva or Milanote to design it"]),
   ("if i want to actually move",["ISSUE11 (ours). one small move a week"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinBMA.dc.html','w').write(ns['doc']('Article pin · best-manifestation-apps · ready for Framer',inner,bg))
print('ok',fs)
