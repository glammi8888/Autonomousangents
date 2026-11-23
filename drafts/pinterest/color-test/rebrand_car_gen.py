# CAR-PR: "Project: Personal Rebrand" carousel (PRC-1..5), Nov 23. Megan: "Our very first pin has 10x the amount of impressions of the other pins. I wonder if we should make a carousel about that topic".
# Same winning format (phone notes, CAR6 approved) + same first-pin lines (Physical/Mentally/Wardrobe), extended. Megan's own lines reused where they exist. issue11.app at the bottom, no white footer.
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
note('PRC-1',1,'Project: Personal Rebrand 🎀🫧',[("the plan",["physical","mentally","wardrobe","money + space"]),("when",["starting now, not january"])])
note('PRC-2',2,'Physical ✨',[("the list",["pilates 3x a week (or just walk lol)","drink water. actually","fix my skincare routine","nails always done","8 hours of sleep, no negotiating"])])
note('PRC-3',3,'Mentally 🧠',[("the list",["no more people-pleasing","journal before i touch my phone","unfollow anyone who makes me feel behind","one hard thing a week"])])
note('PRC-4',4,'Wardrobe 👗',[("the list",["get rid of what i don't wear","find my signature scent","invest in cute pajama sets","a uniform i actually love"])])
note('PRC-5',5,'Money + space 💸',[("money",["open a HYSA account just for future me","raise my rates (or ask for a raise)"]),("space",["clean out my camera roll","make my bed every day"])])
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
