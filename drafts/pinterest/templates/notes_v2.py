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
    Y=(255,214,10); G=(142,142,147)
    d.text((70,50),"11:04",font=IT(34,"SemiBold"),fill=(255,255,255))
    d.text((52,128),"‹",font=IT(64,"Regular"),fill=Y)
    d.text((92,140),"Notes",font=IT(40,"Regular"),fill=Y)
    # right icons: share + more
    d.rounded_rectangle([W-205,142,W-175,178],4,outline=Y,width=4); d.line([W-190,130,W-190,160],fill=Y,width=4)
    d.ellipse([W-125,135,W-75,185],outline=Y,width=4)
    for k in (-12,0,12): d.ellipse([W-100+k-3,157,W-100+k+3,163],fill=Y)
    d.text((W//2,230),"November 14, 2026 at 11:04 PM",font=IT(28,"Regular"),fill=G,anchor="ma")
    f=IT(84,"Bold"); y=300
    for l in wrap(d,hook,f,W-140):
        x=70
        for w in l.split():
            ww=d.textlength(w,font=f)
            col=PINKC if w.strip(".,").lower() in hl else (255,255,255)
            d.text((x,y),w,font=f,fill=col); x+=ww+d.textlength(" ",font=f)
        y+=96
    y+=30
    fp=IT(52,"Regular")
    for n,p in enumerate(ps):
        if n<2:
            d.ellipse([70,y+8,118,y+56],fill=Y)
            d.line([(83,y+33),(91,y+42),(106,y+22)],fill=(0,0,0),width=6,joint="curve")
        else:
            d.ellipse([70,y+8,118,y+56],outline=(99,99,102),width=4)
        for l in wrap(d,p,fp,W-230): d.text((146,y),l,font=fp,fill=(255,255,255)); y+=66
        y+=34
    d.text((70,H-150),"write yours on",font=IT(32,"Regular"),fill=(142,142,147))
    d.text((70,H-108),"issue11.app",font=IT(40,"SemiBold"),fill=(255,214,10))
    paste_logo(im,_mk((255,255,255)),W-60-110,H-60-85,110)
    im.convert("RGB").save(OUT+out,quality=92); return y
A=["getting engaged","being rich af","business popping OFF","$20,000 saved","my dream home","become my own dream girl"]
B=["$20,000 saved","business popping OFF","getting engaged","being rich af","to protect my peace","become my own dream girl"]
C=["being rich af","$20,000 saved","business popping OFF","getting engaged","my dream home","become my own dream girl"]
print(notes("for the girls rebranding their entire life at 11pm",["11pm"],A,"D1-notes-11pm.jpg",sub="my 2027 list · save this for later"))
print(notes("i’m too grown to keep explaining myself.",["grown"],B,"D2-notes-too-grown.jpg",sub="what i want in 2027 · save this for later"))
print(notes("2027, i claim it.",["claim"],C,"D3-notes-claim-it.jpg",sub="my 2027 vision board list · save this for later"))
ims=[Image.open(OUT+f) for f in ["D1-notes-11pm.jpg","D2-notes-too-grown.jpg","D3-notes-claim-it.jpg"]]
s=Image.new('RGB',(3*390+20,600),(255,255,255)); x=10
for i in ims: s.paste(i.resize((380,570)),(x,15)); x+=390
s.save(OUT+"preview-notes-v2.jpg",quality=85)
