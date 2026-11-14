import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
OUT="/home/user/Autonomousangents/drafts/pinterest/templates/"
_m=Image.open(R+"brand/logo/issue11-wordmark-mask.png").convert("LA"); _a=_m.getchannel("A")
def _mk(c):
    l=Image.new("RGBA",_m.size,c+(0,)); l.putalpha(_a); return l
PINKC=(246,90,173)
def wrap(d,text,f,maxw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)>maxw and cur: out.append(cur); cur=w
        else: cur=t
    out.append(cur); return out
def notes(hook,hl,ps,out,sub=""):
    im=Image.new("RGBA",(W,H),(0,0,0)); d=ImageDraw.Draw(im)
    Y=(255,214,10); G=(160,160,165)
    d.text((60,70),"11:04",font=IT(30,"SemiBold"),fill=(255,255,255))
    d.text((60,150),"‹ Notes",font=IT(34,"Medium"),fill=Y)
    f=IT(62,"Bold"); y=250
    for l in wrap(d,hook,f,W-120):
        x=60
        for w in l.split():
            ww=d.textlength(w,font=f)
            col=PINKC if w.strip(".,").lower() in hl else (255,255,255)
            d.text((x,y),w,font=f,fill=col); x+=ww+d.textlength(" ",font=f)
        y+=72
    if sub: d.text((60,y+10),sub,font=IT(32,"Regular"),fill=G); y+=90
    else: y+=40
    fp=IT(38,"Regular")
    for n,p in enumerate(ps):
        if n<2:
            d.ellipse([60,y+4,96,y+40],fill=Y)
            d.line([(70,y+23),(76,y+30),(87,y+15)],fill=(0,0,0),width=5,joint="curve")
        else:
            d.ellipse([60,y+4,96,y+40],outline=(99,99,102),width=3)
        for l in wrap(d,p,fp,W-180): d.text((118,y),l,font=fp,fill=(255,255,255)); y+=50
        y+=26
    d.text((60,H-150),"write yours on",font=IT(32,"Regular"),fill=(142,142,147))
    d.text((60,H-108),"issue11.app",font=IT(40,"SemiBold"),fill=Y)
    paste_logo(im,_mk((255,255,255)),W-60-110,H-60-85,110)
    im.convert("RGB").save(OUT+out,quality=92); return y
A=["getting engaged","being rich af","business popping OFF","$20,000 saved","my dream home","become my own dream girl"]
B=["$20,000 saved","business popping OFF","getting engaged","being rich af","to protect my peace","become my own dream girl"]
C=["being rich af","$20,000 saved","business popping OFF","getting engaged","my dream home","become my own dream girl"]
print(notes("My 2027:",[],A,"D1-notes-11pm.jpg",sub="same girl, bigger dreams"))
print(notes("My 2027:",[],B,"D2-notes-too-grown.jpg",sub="it’s on my vision board"))
print(notes("My 2027:",[],C,"D3-notes-claim-it.jpg",sub="yes, i claim it"))
ims=[Image.open(OUT+f) for f in ["D1-notes-11pm.jpg","D2-notes-too-grown.jpg","D3-notes-claim-it.jpg"]]
s=Image.new('RGB',(3*390+20,600),(255,255,255)); x=10
for i in ims: s.paste(i.resize((380,570)),(x,15)); x+=390
s.save(OUT+"preview-notes-v2.jpg",quality=85)
