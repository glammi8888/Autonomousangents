# CAR-PR: "Project: Personal Rebrand" carousel (PRC-1..5), Nov 23. Megan: "Our very first pin has 10x the amount of impressions of the other pins. I wonder if we should make a carousel about that topic".
# Megan Nov 23: slide lists = her text word for word (lowercased per "No capital letters"). Cover = physical / mental / outfits / money + space, when: starting now; "No capital letters". Same winning format (phone notes, CAR6 approved) + same first-pin lines (Physical/Mentally/Wardrobe), extended. Megan's own lines reused where they exist. issue11.app at the bottom, no white footer.
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
P={}
def note(k,i,title,secs):
    bg,inner=ns['notes'](f"{i}/5 · November 23, 2026",title,secs,"x")
    inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
    fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
    inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
    P[k]=ns['doc'](f'Personal rebrand carousel · slide {i}',inner,bg)
HEART='<svg viewBox="0 0 64 58" style="height:.82em;width:auto;vertical-align:-.04em;margin-left:.28em"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB4D9"/><stop offset="1" stop-color="#F27BB7"/></linearGradient></defs><path d="M32 56C14 43 2 32 2 18 2 8.6 9.6 2 18.5 2 24.6 2 29.4 5.2 32 10 34.6 5.2 39.4 2 45.5 2 54.4 2 62 8.6 62 18 62 32 50 43 32 56Z" fill="url(#hg)"/><ellipse cx="17" cy="14" rx="6.5" ry="4.2" fill="#fff" opacity=".55" transform="rotate(-30 17 14)"/></svg>'  # drawn 🩷 (light pink heart) so it looks the same everywhere (Megan: "Make it match this one: 🩷")
note('PRC-1',1,'personal rebrand'+HEART,[("the plan",["physical","mental","outfits","money + space"]),("when",["starting now"])])
note('PRC-2',2,'physical',[("the list",["pilates 3x per week","daily hot girl walks","drink water!!!","skincare routine every night and morning","nails and hair always done","8 hrs of sleep minimum"])])
note('PRC-3',3,'mental',[("the list",["no more people pleasing","journal before opening my phone","unfollow anyone that makes me feel not good enough","do 1 hard thing a week"])])
note('PRC-4',4,'outfits',[("the list",["get rid of what i don't wear","find my signature scent","invest in cute pajama sets","buy 1 investment piece (shoes or bag)"])])
note('PRC-5',5,'money + space',[("money",["open hysa for future me","raise my rates or ask for a raise"]),("space",["clean up my camera roll","make my bed everyday","sunday resets"])])
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
