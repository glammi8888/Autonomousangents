# CAR-KIT: free 2027 glow up kit carousel (KIT-1..5), Nov 26. Format borrowed from the viral watch
# (drafts/pinterest/viral/VIRAL-WATCH.md: "I made an entire ___ system (FREE)", 47k likes / 1.2k comments);
# content is ours: the real kit at issue11.app/rebrand-kit (prompt titles from drafts/issue11-gift/rebrand-kit/prompts.json).
# Megan Nov 26: "Beautiful we can copy and adapt that content to our content on Pinterest". Phone-notes format, lowercase.
import re
src=open('../batch1/generator.py').read(); ns={}
exec(src[src.index('B={'):src.index('# --- Format 2')],ns)
exec(open('rebrand_car_gen.py').read().split("HEART=",1)[1].split("\n",1)[0].join(["HEART=",""]) if False else "", ns)
HEART=re.search(r"^HEART='(.*?)'  #", open('rebrand_car_gen.py').read(), re.M).group(1)
P={}
def note(k,i,title,secs):
    bg,inner=ns['notes'](f"{i}/5 · November 26, 2026",title,secs,"x")
    inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')].rstrip()
    fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
    inner=inner[:-6]+f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p></div>'
    if i<5: inner=inner[:-6]+f'<p style="position:absolute; right:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">swipe →</p></div>'
    P[k]=ns['doc'](f'Free glow up kit carousel · slide {i}',inner,bg)
note('KIT-1',1,"i made a free 2027 glow up kit"+HEART,[("what's inside",["30 chatgpt prompts to become your own dream girl","my 2027 list","a printable 30-day future self challenge"]),("price",["free"])])
note('KIT-2',2,'body + beauty',[("body",["future me has energy for my life","a workout i actually like","my 5-minute glow up morning"]),("beauty",["my version of polished","edit my beauty routine"])])
note('KIT-3',3,'money + savings',[("money",["what does “rich af” mean for me?","ask for more, no 3-paragraph apology"]),("savings",["a budget with a life in it","$20,000 saved: what’s the plan?"])])
note('KIT-4',4,'love + style',[("love",["friends we actually make time for","say no, kindly"]),("style",["my three style words","shop my closet first"])])
note('KIT-5',5,'how to get it',[("it's free",["tap the link on this pin","or go to issue11.app/rebrand‑kit"]),("why it works",["every prompt uses a real behavior-change method"]),("tonight",["pick one prompt and start"])])
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
