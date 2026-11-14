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


def IT(size, w="SemiBold"):
    f=ImageFont.truetype(F+"InterTight.ttf",size)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
def tightline(d,cx,y,text,f,fill,track=-0.055):
    size=f.size; widths=[d.textlength(c,font=f)+track*size for c in text]; total=sum(widths)-track*size
    x=cx-total/2
    for c,w in zip(text,widths): d.text((x,y),c,font=f,fill=fill); x+=w
    return total
def make_quote(lines_, sub, label, out, size=150):
    stops=[(234,246,255),(217,179,255),(255,77,184),(255,154,122)]
    B=Image.new("RGB",(W//4,H//4)); px=B.load()
    for y in range(H//4):
        for x in range(W//4):
            t=(x/(W/4)*0.35+y/(H/4)*0.65); t=min(max(t,0),0.999)*(len(stops)-1); i=int(t); f=t-i
            px[x,y]=tuple(int(stops[i][k]+(stops[i+1][k]-stops[i][k])*f) for k in range(3))
    B=B.resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(30)).convert("RGBA"); d=ImageDraw.Draw(B)
    f=IT(size)
    def wid(l): return sum(d.textlength(c,font=f)-0.055*f.size for c in l)
    while max(wid(l) for l in lines_)>W-160: f=IT(f.size-6)
    lab=IT(24,"SemiBold")
    tightline(d,W//2,110,label.upper(),lab,BLACK,track=0.1)
    lh=0.94; total=len(lines_)*f.size*lh
    y0=(H-total)/2-60
    for i,l in enumerate(lines_): tightline(d,W//2,y0+i*f.size*lh,l,f,BLACK)
    d.text((W//2,1180),sub,font=IT(32,"Regular"),fill=BLACK,anchor="ma")
    paste_logo(B,logo_b,W//2,1250,200,anchor="c")
    B.convert("RGB").save(out,quality=92)
