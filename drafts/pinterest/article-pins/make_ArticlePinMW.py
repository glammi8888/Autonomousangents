# ArticlePinMW (mirror-work), Nov 17 scheduled run · phone-notes format (Megan: "the phone notes format works").
# Lines in the notes voice, from the live article's "How Do I Do a Mirror Exercise?" + "What to Say When Affirmations Feel Fake" (sentences copied from the article) (issue11.app/blog/mirror-work).
# Keyword check: ../2026-11-17-mirror-work-keywords.json (Pinterest autocomplete via Apify).
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
bg,inner=ns['notes']("November 18, 2026","mirror work affirmations, the 2 minute version 🪞",
  [("while i brush my teeth",["look at my eyes, not my pores","3 slow breaths","one kind, true sentence. out loud, 3 times","end with one small promise. then keep it"]),
   ("what i say when it feels fake",["“You're doing better than you think.”","“You're allowed to want more.”"])],"x")
inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
open('ArticlePinMW.dc.html','w').write(ns['doc']('Article pin · mirror-work · ready for Framer',inner,bg))
print('ok',fs)
