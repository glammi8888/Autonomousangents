from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
F="/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad/fonts/"
R="/home/user/Autonomousangents/"
OUT=R+"drafts/pinterest/templates/"
W,H=1000,1500
BLACK=(13,13,13); CREAM=(245,238,224); BLUSH=(252,210,221); PINK=(246,90,173); RED=(212,8,6)
def font(n,s): return ImageFont.truetype(F+n,s)
AB=lambda s: font("font-archivo-black.ttf",s)
AN=lambda s: font("font-archivo-narrow.ttf",s)
MONO=lambda s: font("IBMPlexMono-Regular.ttf",s)
def tight(d,xy,text,f,fill,track=-0.06,anchor="l"):
    x,y=xy; size=f.size
    widths=[d.textlength(c,font=f)+track*size for c in text]
    total=sum(widths)-track*size
    if anchor=="c": x-=total/2
    for c,w in zip(text,widths):
        d.text((x,y),c,font=f,fill=fill); x+=w
    return total
def lines(d,x,y,ls,f,fill,lh=0.82,anchor="l"):
    for i,l in enumerate(ls): tight(d,(x,y+i*f.size*lh),l,f,fill,anchor=anchor)
    return y+len(ls)*f.size*lh
def cover(img,w,h,fy=0.5):
    r=max(w/img.width,h/img.height); im=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*fy); return im.crop((x,y,x+w,y+h))
_m=Image.open(R+"brand/logo/issue11-wordmark-mask.png")
_a=_m.getchannel("A") if _m.mode in ("RGBA","LA") else _m.convert("L")
def _mk(c):
    l=Image.new("RGBA",_m.size,c+(0,)); l.putalpha(_a); return l
logo_b=_mk(BLACK); logo_c=_mk(CREAM)
def paste_logo(base,logo,x,y,w,anchor="l"):
    r=w/logo.width; l=logo.resize((w,int(logo.height*r)),Image.LANCZOS)
    if anchor=="c": x-=w//2
    base.alpha_composite(l,(int(x),int(y)))

# A: editorial magazine cover pin
img=Image.open(R+"drafts/issue11-blog/images/megan-editorial-20.webp").convert("RGB")
A=cover(img,W,H).convert("RGBA")
ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
for i in range(H//2):
    a=int(170*(i/(H/2))**1.6); od.line([(0,H//2+i),(W,H//2+i)],fill=(13,13,13,a))
for i in range(260):
    od.line([(0,i),(W,i)],fill=(13,13,13,int(150*(1-i/260))))
A.alpha_composite(ov); d=ImageDraw.Draw(A)
paste_logo(A,logo_c,60,60,300)
d.text((W-60,78),"THE FUTURE ISSUE · 2027",font=MONO(24),fill=CREAM,anchor="ra")
d.line([(60,175),(W-60,175)],fill=CREAM,width=2)
lines(d,60,1040,["2027","VISION BOARD","IDEAS"],AB(118),CREAM)
d.rectangle([60,1395,60+20+d.textlength("SEE IT · WRITE IT · BECOME IT",font=MONO(22)),1440],fill=BLUSH)
d.text((75,1404),"SEE IT · WRITE IT · BECOME IT",font=MONO(22),fill=BLACK)
A.convert("RGB").save(OUT+"A-editorial-cover.jpg",quality=92)

# B: type card on Electric Soft gradient
stops=[(234,246,255),(217,179,255),(255,77,184),(255,154,122)]
B=Image.new("RGB",(W,H)); px=B.load()
for y in range(H):
    for x in range(0,W):
        t=(x/W*0.35+y/H*0.65); t=min(max(t,0),0.999)*(len(stops)-1); i=int(t); f=t-i
        c=tuple(int(stops[i][k]+(stops[i+1][k]-stops[i][k])*f) for k in range(3)); px[x,y]=c
B=B.filter(ImageFilter.GaussianBlur(40)).convert("RGBA"); d=ImageDraw.Draw(B)
d.text((W//2,110),"ISSUE11 · NOTE TO SELF · 01 / 11",font=MONO(26),fill=BLACK,anchor="ma")
lines(d,W//2,520,["2027 IS","THE YEAR","I BECOME","ME."],AB(150),BLACK,anchor="c")
d.text((W//2,1180),"Future you is already on her way.",font=font("IBMPlexSerif-Italic.ttf" if False else "IBMPlexMono-Regular.ttf",30),fill=BLACK,anchor="ma")
paste_logo(B,logo_b,W//2,1250,200,anchor="c")
B.convert("RGB").save(OUT+"B-type-card.jpg",quality=92)

# C: magazine page with journal prompts
C=Image.new("RGBA",(W,H),CREAM); d=ImageDraw.Draw(C)
d.text((60,60),"← ISSUE 11 · 01 / WRITING",font=MONO(24),fill=BLACK)
d.text((W-60,60),"NOV 2026",font=MONO(24),fill=BLACK,anchor="ra")
d.line([(60,105),(W-60,105)],fill=BLACK,width=2)
ph=cover(Image.open(R+"drafts/issue11-blog/images/megan-editorial-26.webp").convert("RGB"),W-120,430,0.35)
C.paste(ph,(60,130))
y=lines(d,60,600,["FUTURE SELF","JOURNAL PROMPTS"],AB(82),BLACK)
d.line([(60,y+30),(W-60,y+30)],fill=BLACK,width=2)
prompts=["What does future you do first every morning?","What did she stop apologizing for?","Which habit made the biggest difference?","What does your true self want this week?","Write the one small move you'll make today."]
yy=y+60
for i,p in enumerate(prompts,1):
    d.text((60,yy),f"{i:02d}",font=MONO(28),fill=PINK)
    d.text((130,yy-6),p,font=AN(40),fill=BLACK); yy+=88
d.line([(60,H-200),(W-60,H-200)],fill=BLACK,width=2)
d.text((60,H-118),"SAVE THIS · WRITE IT IN YOUR ISSUE",font=MONO(24),fill=BLACK)
paste_logo(C,logo_b,W-60-150,H-80-115,150)
C.convert("RGB").save(OUT+"C-prompt-page.jpg",quality=92)
print("done")
