# Round 8 (CT78–CT87), Nov 16: "more pins with different images too ?? And different layouts" + "I also want the text on the pins to correlate to the images". 8 new Drive photos, each paired with the BANK line it shows.
import gen4
gen4.B.update({'suit':'93627e588ae16e5cf86dc60bcbae487b','bedcash':'73fc9a482935b42b1e643e02ebfc3a48','pinkmoney':'03c9af09041b7d2d6efd614e68331dea','flying':'1b47a89319b10d2a520ecd22bff402a1','redhair':'bda9f11616ec354e2208907843aace41','blueclose':'e6e124f1aad6d754069c4e38a30a8a09','pinkgloss':'4e778283bc9ea80ceaef2cab845c3108','bighair':'034dc4a58467509df431ad7092996c57'})
from gen4 import B, IND, run
from gen5 import cover
from gen import doc, LOGO
A='alt="Editorial photo (AI-generated)"'
def s(k): return f'/_blob/{B[k]}'
S="""
.tl{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%);z-index:5}
.url{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:700;font-size:28px;z-index:5}
img.f{position:absolute;object-fit:cover;display:block}
.full{inset:0;width:100%;height:100%}
"""
TOP=lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
URL=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
P={}
# 78 bed of cash + door-hanger tag
P['CT78']=doc('Color test 78 · door hanger on full bleed',S+"""
.pin{background:#111}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 18%)}
.hg{position:absolute;left:580px;top:640px;width:330px;height:640px;background:#F4EEE2;border-radius:24px;transform:rotate(6deg);box-shadow:0 24px 50px rgba(0,0,0,.45);padding:150px 34px 0;box-sizing:border-box;color:#1F3A26}
.hg::before{content:'';position:absolute;left:50%;top:44px;width:120px;height:120px;margin-left:-60px;border-radius:50%;background:#111}
.hg b{display:block;font-weight:900;font-size:76px;line-height:.9;letter-spacing:-.05em;margin-top:30px}
.hg i{font-style:normal;font-weight:700;font-size:16px;letter-spacing:.3em;text-transform:uppercase}
""",f"""<img class="f full" src="{s('bedcash')}" style="object-position:45% 30%" {A}><div class="sh"></div>{TOP('w')}
<div class="hg"><i>Room 11</i><b>I wake up to money</b></div>{URL('#F4EEE2')}""")
# 79 suit on cash + outline type
P['CT79']=doc('Color test 79 · outline type on full bleed',S+"""
.pin{background:#111}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,15,30,.35) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 55%,rgba(10,20,45,.8) 85%)}
.o{position:absolute;left:40px;right:40px;top:930px;font-weight:900;font-size:100px;line-height:.9;letter-spacing:-.04em;text-transform:uppercase;color:transparent;-webkit-text-stroke:2.5px #B8C8F2}
.o b{color:#B8C8F2;-webkit-text-stroke:0}
""",f"""<img class="f full" src="{s('suit')}" style="object-position:50% 20%" {A}><div class="sh"></div><img class="tl w" style="left:52px;transform:none" src="{LOGO}" alt="ISSUE11">
<div class="o"><b>I make way more money</b> than what I'm able to spend</div>{URL('#B8C8F2')}""")
# 80 pink money + three bands
bands=[('A healthy mind,','#FFD3E4'),('a fit body,','#FF9EC4'),('and lots of money $$$','#E2457F')]
bh=''.join(f'<div class="b" style="background:{c}">{t}</div>' for t,c in bands)
P['CT80']=doc('Color test 80 · photo + three colour bands',S+"""
.pin{background:#FFD3E4}
img.f{left:0;top:0;width:1000px;height:900px}
.bands{position:absolute;left:0;right:0;top:900px;height:600px;display:flex;flex-direction:column}
.b{flex:1;display:flex;align-items:center;padding:0 52px;font-weight:900;font-size:68px;letter-spacing:-.045em;color:#5A0F2E}
.b:last-child{color:#fff}
.url{bottom:22px;color:#fff}
""",f"""<img class="f" src="{s('pinkmoney')}" style="object-position:55% 25%" {A}>{TOP()}<div class="bands">{bh}</div>{URL('#fff')}""")
# 81 money raining + words on falling bill tags
words=[('My business',120,860,-8),('is bringing',380,980,6),('sooooo',140,1090,-4),('much money',420,1200,5)]
tags=''.join(f'<div class="tg" style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{w}</div>' for w,x,y,r in words)
P['CT81']=doc('Color test 81 · falling tags on full bleed',S+"""
.pin{background:#1D47B8}
.tg{position:absolute;background:#F2F0E6;color:#1F4A2A;font-weight:900;font-size:66px;letter-spacing:-.04em;padding:14px 26px;border:3px dashed #9DBF9F;box-shadow:0 14px 30px rgba(0,0,30,.35)}
""",f"""<img class="f full" src="{s('flying')}" style="object-position:50% 20%" {A}><img class="tl w" style="left:auto;right:52px;transform:none" src="{LOGO}" alt="ISSUE11">{tags}{URL('#fff')}""")
# 82 red liner + zoom circle on the eye
P['CT82']=doc('Color test 82 · zoom loupe on the eye',S+"""
.pin{background:#F6EFEA}
img.f{left:0;top:0;width:1000px;height:1000px}
.zoom{position:absolute;right:50px;top:760px;width:340px;height:340px;border-radius:50%;overflow:hidden;border:10px solid #fff;box-shadow:0 20px 40px rgba(0,0,0,.3)}
.zoom img{position:absolute;width:1400px;height:1860px;left:-810px;top:-430px;object-fit:cover}
.q{position:absolute;left:52px;width:520px;top:1060px;font-weight:300;font-size:84px;line-height:.92;letter-spacing:-.05em;color:#C4141C}
.q b{font-weight:900}
.url{text-align:left;left:52px;color:#C4141C}
""",f"""<img class="f" src="{s('redhair')}" style="object-position:50% 30%" {A}>{TOP('w')}
<div class="zoom"><img src="{s('redhair')}" {A}></div><div class="q">My <b>face card</b> is absolutely <b>lethal</b></div>{URL('#C4141C')}""")
# 83 blue stare + huge cropped type bleeding off the edges
P['CT83']=doc('Color test 83 · huge cropped type',S+"""
.pin{background:#DCE6F2;overflow:hidden}
img.f{left:0;top:0;width:1000px;height:1080px}
.huge{position:absolute;left:-30px;top:1020px;white-space:nowrap;font-weight:900;font-size:250px;letter-spacing:-.07em;line-height:.8;color:#3E63C9;text-transform:uppercase}
.small{position:absolute;left:52px;top:1290px;font-style:italic;font-weight:400;font-size:52px;color:#1E3A6E;letter-spacing:-.03em}
.url{text-align:right;right:52px;left:auto;color:#1E3A6E}
""",f"""<img class="f" src="{s('blueclose')}" style="object-position:50% 20%" {A}><img class="tl" style="left:52px;top:1250px;transform:none;height:0" src="{LOGO}" alt=""><img class="logo" style="left:auto;right:52px;top:44px;bottom:auto;height:76px;filter:invert(1)" src="{LOGO}" alt="ISSUE11"><div class="huge">The prize</div><div class="small">I am the prize, always</div>{URL('#1E3A6E')}""")
# 84 pink gloss + text straddling the seam
P['CT84']=doc('Color test 84 · split seam',S+"""
.pin{background:#F9D7E2}
img.f{left:0;top:0;width:1000px;height:960px}
.url{color:#7A0F3A}
.q{position:absolute;left:52px;right:52px;top:1000px;font-weight:900;font-size:120px;line-height:.86;letter-spacing:-.055em;color:#C2185B}
.q i{display:block;font-weight:300;color:#7A0F3A}
""",f"""<img class="f" src="{s('pinkgloss')}" style="object-position:50% 25%" {A}><img class="tl" style="left:52px;transform:none" src="{LOGO}" alt="ISSUE11"><div class="q">Dream girl <i>I am my own dream girl</i></div>{URL('#7A0F3A')}""")
# 85 indie cover B: vertical title + big issue number
P['CT85']=doc('Color test 85 · indie cover · vertical title',S+"""
.pin{background:#EDE6DC}
img.f{left:150px;top:0;width:850px;height:1500px}
.vt{position:absolute;left:10px;top:40px;height:1420px;writing-mode:vertical-rl;transform:rotate(180deg);font-weight:900;font-size:150px;letter-spacing:-.06em;line-height:1;color:#3A2418;text-transform:uppercase;text-align:right}
.no{position:absolute;right:40px;top:40px;font-weight:200;font-size:140px;letter-spacing:-.06em;color:#fff;line-height:1}
.sh{position:absolute;left:150px;top:0;width:850px;height:1500px;background:linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(40,25,15,.75) 88%)}
.story{position:absolute;left:200px;right:52px;bottom:190px;color:#fff;font-weight:900;font-size:66px;line-height:.92;letter-spacing:-.045em}
.story i{display:block;font-style:normal;font-weight:700;font-size:20px;letter-spacing:.3em;text-transform:uppercase;margin-bottom:12px;color:#F2C9A0}
.logo{left:200px}
""",f"""<img class="f" src="{s('bighair')}" style="object-position:50% 25%" {A}><div class="sh"></div><div class="vt">Glow up</div><div class="no">11</div>
<div class="story"><i>Cover story</i>I glowed up so hard now my enemies are crying</div><img class="logo w" src="{LOGO}" alt="ISSUE11">""")
# 86, 87 covers in the loved format
P['CT86']=cover('CT86','pinkmoney','55% 20%','Healthy','#FF9EC4','A healthy mind, a fit body, and lots of money $$$',[('40','money affirmations'),('8','glow up checklist steps'),('60','self love affirmations')],'linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(90,15,46,.75) 100%)')
P['CT87']=cover('CT87','bedcash','45% 30%','Wake up','#F3D9A4','I wake up to money',[('40','money affirmations'),('9','ways to stop overthinking'),('120','words of the year')],'linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 50%,rgba(20,20,10,.75) 100%)')
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
