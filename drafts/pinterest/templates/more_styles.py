import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
_m=Image.open(R+"brand/logo/issue11-wordmark-mask.png").convert("LA"); _a=_m.getchannel("A")
def _mk(c):
    l=Image.new("RGBA",_m.size,c+(0,)); l.putalpha(_a); return l
OUT="/home/user/Autonomousangents/drafts/pinterest/templates/"
IMG=R+"drafts/issue11-blog/images/"
def grad(w,h,stops=[(234,246,255),(217,179,255),(255,77,184),(255,154,122)]):
    g=Image.new("RGB",(w//4,h//4)); px=g.load()
    for y in range(h//4):
        for x in range(w//4):
            t=(x/(w/4)*0.35+y/(h/4)*0.65); t=min(max(t,0),0.999)*(len(stops)-1); i=int(t); f=t-i
            px[x,y]=tuple(int(stops[i][k]+(stops[i+1][k]-stops[i][k])*f) for k in range(3))
    return g.resize((w,h),Image.BICUBIC).filter(ImageFilter.GaussianBlur(30))
def wrap(d,text,f,maxw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)>maxw and cur: out.append(cur); cur=w
        else: cur=t
    out.append(cur); return out

# D: iPhone Notes (dark) prompt list
D_=Image.new("RGBA",(W,H),(0,0,0)); d=ImageDraw.Draw(D_)
d.text((60,70),"9:41",font=IT(30,"SemiBold"),fill=(255,255,255))
d.text((60,150),"‹ Notes",font=IT(34,"Medium"),fill=(255,214,10))
y=250
for l in wrap(d,"future self journal prompts",IT(62,"Bold"),W-120): d.text((60,y),l,font=IT(62,"Bold"),fill=(255,255,255)); y+=72
d.text((60,y+10),"before you reach for your phone, reach for a pen",font=IT(32,"Regular"),fill=(160,160,165)); y+=90
ps=["remember your future: what does a normal tuesday look like in 2027?","write it like it already happened","what am i too grown to keep explaining?","where am i still abandoning myself to keep the peace?","what would i do if i didn’t need the proof?","it’s on my vision board. what’s one small action tonight?","what am i claiming for 2027?","what does protecting my peace look like this week?"]
for p in ps:
    ls=wrap(d,p,IT(38,"Regular"),W-170)
    d.ellipse([70,y+16,82,y+28],fill=(255,255,255))
    for l in ls: d.text((110,y),l,font=IT(38,"Regular"),fill=(255,255,255)); y+=50
    y+=18
paste_logo(D_,_mk((255,255,255)),W-60-110,H-60-85,110)
D_.convert("RGB").save(OUT+"D-notes-prompts.jpg",quality=92)

# E: printable 30-day challenge
E=Image.new("RGBA",(W,H),CREAM); d=ImageDraw.Draw(E)
tightline(d,W//2,70,"ISSUE11 · PRINTABLE",IT(24,"SemiBold"),BLACK,track=0.1)
f=IT(92); y=130
for l in ["30-day future","self challenge."]: tightline(d,W//2,y,l,f,BLACK); y+=88
d.text((W//2,y+20),"one prompt a day. one line is enough.",font=IT(30,"Regular"),fill=BLACK,anchor="ma")
days=["your 2027 in one word","describe a normal tuesday in 2027","what are you done tolerating?","one habit future you has","future you’s morning, hour by hour","what does home look like?","a letter from future you","what are you building?","who do you want around you?","what does money feel like?","dress for the life you want","one thing to start tonight","what would you try if no one watched?","your rebrand in 3 photos","what does rest look like?","a fear future you is over","one money move this week","where are you in 12 months?","what is more possible now?","your cover line for 2027","what are you proud of?","one small risk this week","what will you stop explaining?","a playlist for future you","what does future you say no to?","describe your ideal weekend","one boundary to keep","what changed this month?","what are you claiming?","read day 1 again"]
gx,gy=60,y+90; cw=(W-120-4*12)//5; ch=(H-gy-150-5*12)//6
for i,t in enumerate(days):
    cx=gx+(i%5)*(cw+12); cy=gy+(i//5)*(ch+12)
    d.rectangle([cx,cy,cx+cw,cy+ch],fill=BLUSH)
    d.text((cx+12,cy+10),f"DAY {i+1}",font=IT(18,"SemiBold"),fill=PINK)
    yy=cy+38
    for l in wrap(d,t,IT(19,"Regular"),cw-20)[:4]: d.text((cx+12,yy),l,font=IT(19,"Regular"),fill=BLACK); yy+=23
paste_logo(E,logo_b,W//2,H-125,100,anchor="c")
E.convert("RGB").save(OUT+"E-30-day-printable.jpg",quality=92)

# F: vision board photo collage
F_=Image.new("RGBA",(W,H),CREAM); d=ImageDraw.Draw(F_)
pics=["megan-editorial-20.webp","megan-editorial-16.webp","megan-editorial-26.webp","megan-editorial-34.webp","megan-editorial-21.webp","megan-editorial-37.webp"]
gw=(W-120-16)//2; gh=(H-300-32)//3
for i,p in enumerate(pics):
    try: im=cover(Image.open(IMG+p).convert("RGB"),gw,gh,0.4)
    except Exception: continue
    F_.paste(im,(60+(i%2)*(gw+16),60+(i//2)*(gh+16)))
d.rectangle([0,H-230,W,H],fill=CREAM)
tightline(d,60+(W-120)/2,H-210,"2027 vision board.",IT(80),BLACK)
d.text((W//2,H-110),"Become your own dream girl.",font=IT(30,"Regular"),fill=BLACK,anchor="ma")
paste_logo(F_,logo_b,W-60-90,H-60-70,90)
F_.convert("RGB").save(OUT+"F-vision-collage.jpg",quality=92)

# G: photo + quote with gradient band
G=cover(Image.open(IMG+"megan-editorial-16.webp").convert("RGB"),W,H,0.3).convert("RGBA")
band=grad(W,520).convert("RGBA"); G.alpha_composite(band,(0,H-520)); d=ImageDraw.Draw(G)
tightline(d,W//2,H-480,"ISSUE11 · THE FUTURE ISSUE",IT(24,"SemiBold"),BLACK,track=0.1)
f=IT(100); y=H-420
for l in ["Same girl,","bigger dreams."]: tightline(d,W//2,y,l,f,BLACK); y+=94
d.text((W//2,y+30),"Your 2027 rebrand starts on one page.",font=IT(30,"Regular"),fill=BLACK,anchor="ma")
paste_logo(G,logo_b,W//2,H-60-75,100,anchor="c")
G.convert("RGB").save(OUT+"G-photo-quote.jpg",quality=92)

ims=[Image.open(OUT+f) for f in ["D-notes-prompts.jpg","E-30-day-printable.jpg","F-vision-collage.jpg","G-photo-quote.jpg"]]
s=Image.new('RGB',(4*390+50,600),(255,255,255)); x=10
for i in ims:
    t=i.resize((380,570)); s.paste(t,(x,15)); x+=390
s.save(OUT+"preview-4-more-styles.jpg",quality=85)
