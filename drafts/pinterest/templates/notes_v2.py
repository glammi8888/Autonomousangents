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
def notes(hook,hl,ps,out,sub="future self journal prompts · save for 2027"):
    im=Image.new("RGBA",(W,H),(0,0,0)); d=ImageDraw.Draw(im)
    d.text((60,60),"11:04 PM",font=IT(30,"SemiBold"),fill=(255,255,255))
    d.text((60,130),"‹ Notes",font=IT(34,"Medium"),fill=(255,214,10))
    f=IT(112,"Bold"); y=215
    for l in wrap(d,hook,f,W-120):
        x=60
        for w in l.split():
            ww=d.textlength(w,font=f)
            if w.strip(".,").lower() in hl:
                d.rectangle([x-8,y+18,x+ww+8,y+118],fill=PINKC)
            d.text((x,y),w,font=f,fill=(255,255,255)); x+=ww+d.textlength(" ",font=f)
        y+=112
    y+=44
    d.text((60,y),sub,font=IT(30,"Regular"),fill=(160,160,165)); y+=80
    fp=IT(44,"Regular")
    for p in ps:
        d.ellipse([70,y+20,84,y+34],fill=(255,255,255))
        for l in wrap(d,p,fp,W-180): d.text((110,y),l,font=fp,fill=(255,255,255)); y+=56
        y+=20
    paste_logo(im,_mk((255,255,255)),W-60-110,H-60-85,110)
    im.convert("RGB").save(OUT+out,quality=92); return y
A=["money that feels calm. not checking my bank app 10x a day","to work for myself","to feel at home in my body","one friend who gets it","to say no without a 3-paragraph apology","to feel like myself again"]
B=["a soft life with a calm nervous system","to be debt free","my dream home","to protect my peace and keep my circle small","to be chosen","to feel like myself again"]
C=["money that feels calm","my own business","my dream home","to feel at home in my body","one friend who gets it","to feel like myself again"]
print(notes("for the girls rebranding their entire life at 11pm",["11pm"],A,"D1-notes-11pm.jpg",sub="my 2027 list · save this for later"))
print(notes("i’m too grown to keep explaining myself.",["grown"],B,"D2-notes-too-grown.jpg",sub="what i want in 2027 · save this for later"))
print(notes("2027, i claim it.",["claim"],C,"D3-notes-claim-it.jpg",sub="my 2027 vision board list · save this for later"))
ims=[Image.open(OUT+f) for f in ["D1-notes-11pm.jpg","D2-notes-too-grown.jpg","D3-notes-claim-it.jpg"]]
s=Image.new('RGB',(3*390+20,600),(255,255,255)); x=10
for i in ims: s.paste(i.resize((380,570)),(x,15)); x+=390
s.save(OUT+"preview-notes-v2.jpg",quality=85)
