# Variants round (CT173–CT184), Nov 17. Megan: "Do you think we have a good variety of pins to test now ? You can mix and match images too / Especially with pins similar to 42, 95, 45, 122, 133, 144, 62". 2 new photo + line pairs per format. BANK / ANGEL-NUMBERS lines only, each photo matched to its line.
import gen9, gen8, gen13
from gen import doc, LOGO
from gen13 import S, T, U, A, s
P={}
def f42(n,bg,k,pos,line,col='#111'):   # pastel + framed photo + italic line
    P[n]=doc(f'Color test {n[2:]} · like 42 · {line[:30]}',S+f".pin{{background:{bg}}}\n.it{{position:absolute;left:60px;right:60px;top:1050px;text-align:center;font-style:italic;font-weight:400;font-size:64px;letter-spacing:-.03em;color:{col}}}",
      f"""<img class="f" src="{s(k)}" style="left:250px;top:200px;width:500px;height:760px;object-position:{pos}" {A}>{T()}<div class="it">{line}</div>{U(col)}""")
def f45(n,k,pos,html,shade,top=1230):           # full-bleed colour photo + huge caps + italic
    P[n]=doc(f'Color test {n[2:]} · like 45 · huge type',S+f""".big{{position:absolute;left:50px;right:50px;top:{top}px;color:#fff;font-weight:900;font-size:118px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase;text-align:center}}
.big i{{font-weight:300}}""",f"""<img class="f full" src="{s(k)}" style="object-position:{pos}" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 70%,{shade} 88%)"></div>{T('w')}<div class="big">{html}</div>{U('#fff')}""")
def f62(n,k,ko,html,col):              # photo-texture knockout number + caps line
    P[n]=doc(f'Color test {n[2:]} · like 62 · knockout {ko}',S+f""".pin{{background:#0E0E0E}}
.ko{{position:absolute;left:0;right:0;top:400px;font-weight:900;font-size:300px;line-height:.85;letter-spacing:-.07em;text-align:center;background:url('{s(k)}') 50% 50%/cover;-webkit-background-clip:text;background-clip:text;color:transparent}}
.big{{position:absolute;left:60px;right:60px;top:760px;text-align:center;color:{col};font-weight:900;font-size:96px;line-height:.92;letter-spacing:-.05em;text-transform:uppercase}}
.big i{{font-weight:300}}""",f"""{T('w')}<div class="ko">{ko}</div><div class="big">{html}</div>{U(col)}""")
def f95(n,word,line,specs,fs=250):     # giant lowercase word + 4 specimen photos
    pos=[('left:90px;top:200px'),('right:90px;top:170px'),('left:110px;top:1040px'),('right:110px;top:1060px')]
    sp=''.join(f'<div class="sp" style="{p}"><img src="{s(k)}" {A}><span>{lab}</span></div>' for p,(k,lab) in zip(pos,specs))
    P[n]=doc(f'Color test {n[2:]} · like 95 · {word}',S+f""".pin{{background:#fff;color:#0D0D0D}}
.gw{{position:absolute;left:0;right:0;top:500px;text-align:center;font-weight:600;font-size:{fs}px;letter-spacing:-.07em;line-height:1}}
.sp{{position:absolute;width:210px}}
.sp img{{display:block;width:210px;height:260px;object-fit:cover;object-position:50% 30%}}
.sp span{{display:block;margin-top:8px;font-size:17px;font-weight:600}}
.line{{position:absolute;left:140px;right:140px;top:790px;text-align:center;font-weight:500;font-size:38px;letter-spacing:-.03em;line-height:1.25}}""",
      f"""{sp}<div class="gw">{word}</div><div class="line">{line}</div><img class="tl" src="{LOGO}" alt="ISSUE11" style="top:auto;bottom:120px;height:70px"><div class="url" style="color:#0D0D0D">issue11.app</div>""")
def f122(n,k,pos,kw,sub,kc='#FF4FA3'):  # big pink keyword over photo
    P[n]=doc(f'Color test {n[2:]} · like 122 · {kw}',S+f""".pin{{background:#222}}
.kw{{position:absolute;left:0;right:0;top:1000px;text-align:center;color:{kc};font-weight:800;font-size:190px;letter-spacing:-.07em;line-height:1;text-shadow:0 4px 30px rgba(0,0,0,.25)}}
.sub{{position:absolute;left:0;right:0;top:1210px;text-align:center;color:#fff;font-weight:500;font-size:42px;text-shadow:0 2px 14px rgba(0,0,0,.5)}}""",
      f"""<img class="f full" src="{s(k)}" style="object-position:{pos}" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(0,0,0,.45) 90%)"></div>{T('w')}<div class="kw">{kw}</div><div class="sub">{sub}</div>{U('#fff')}""")
def fang(n,k,pos,num,key,line):        # angel number over full-bleed photo (133/144)
    P[n]=doc(f'Color test {n[2:]} · like 133/144 · {num}',S+""".n{position:absolute;left:0;right:0;top:930px;text-align:center;color:#fff;font-weight:800;font-size:250px;letter-spacing:-.06em;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.35)}
.k{position:absolute;left:0;right:0;top:1195px;text-align:center;color:#fff;font-weight:700;font-size:28px;letter-spacing:.3em}
.l{position:absolute;left:100px;right:100px;top:1245px;text-align:center;color:#fff;font-style:italic;font-weight:400;font-size:42px;line-height:1.25;text-wrap:balance}""",
      f"""<img class="f full" src="{s(k)}" style="object-position:{pos}" {A}><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.7) 85%)"></div>{T('w')}<div class="n">{num}</div><div class="k">{key}</div><div class="l">{line}</div>{U('#fff')}""")

f42('CT173','#FCE3D6','pinkgloss','50% 35%','My face card is absolutely lethal')
f42('CT174','#DDF0E6','hair','40% 30%','I love my long hair')
f45('CT175','blue','50% 0%','I am <i>iconic</i>','rgba(10,25,90,.88)')
f45('CT176','orange','50% 0%','I have <i>big plans.</i>','rgba(120,45,0,.88)',top=1160)
f62('CT177','cashpile','8888','money is <i>coming</i>','#9BE3B0')
f62('CT178','sky','2027','is the year <i>I lifemaxx</i>','#BFD6FF')
f95('CT179','muse','muse n. A woman, or a force personified as a woman, who is the source of inspiration for a creative artist.',[('earring','Gold'),('blueclose','Blue'),('redhair','Copper'),('pinkgloss','Pink')])
f95('CT180','richer','i only get richer and prettier',[('cashface','Richer'),('pinkgloss','Prettier'),('bobcash','Richer'),('earring','Prettier')],fs=230)
f122('CT181','earring','50% 25%','spoiled','Spoiled by the Universe ⭐')
f122('CT182','cashface','50% 25%','rich','Rich &amp; Stylish 2027','#FFD24A')
fang('CT183','shoulder','50% 25%','444','PROTECTION',"you're protected 🧿 keep going")
fang('CT184','flying','50% 25%','222','ALIGNMENT',"it's still coming together. what is meant for you will never miss you")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
