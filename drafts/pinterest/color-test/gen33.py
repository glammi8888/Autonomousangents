# Diverse carousels in the CAR5 design language (CAR14, CAR15), Nov 17.
# Megan: "for carousel 5 I just want a mix and match not for you to give me the exact same carousel with different pictures and titles... we already agreed on the style, now give me diversity with a similar style, from a graphic design standpoint".
# Same family as CAR5 (Inter Tight, white / lilac #F1EBFF / pink #F8DCEB, black type + light italic, pink accent #C2207E, framed photos, logo top centre, n / 5),
# but every slide is a NEW layout: photo-band cover, contents cover, two-column compare, checklist, highlighter quote, timeline diagram, numbered list, diptych, giant numeral, fill-in-the-blank.
import gen9, gen8, gen13, gen19
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
PK='#C2207E'; LI='#F1EBFF'; PI='#F8DCEB'
N=lambda i,c='#111': f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:{c};z-index:6">{i} / 5</div>'
P={}
def pg(k,t,css,body): P[k]=doc(t,S+css,body)
# ================= CAR14 · how to manifest money (realistic) =================
pg('CAR14-1','Carousel 14 · 1 · photo band cover',f""".pin{{background:#fff}}
.h{{position:absolute;left:56px;right:56px;top:880px;font-weight:900;font-size:136px;line-height:.88;letter-spacing:-.06em;color:#0D0D0D}}
.h i{{font-weight:300;color:{PK};letter-spacing:-.04em}}""",
f"""<img class="f" src="{s('cashface')}" style="left:0;top:0;width:1000px;height:800px;object-position:50% 30%" {A}>{T('w')}{N(1,'#fff')}
<div class="h">how to manifest money <i>(realistic)</i></div>{U('#0D0D0D')}""")
rows=[('more money','my rich af number'),('rich someday','by december 2027'),('i hope','i plan'),('a mood','a number')]
tr=''.join(f'<div class="r"><span>{a}</span><span>{b}</span></div>' for a,b in rows)
pg('CAR14-2','Carousel 14 · 2 · two-column compare',f""".pin{{background:#fff;color:#111}}
.t{{position:absolute;left:70px;right:70px;top:230px;font-weight:800;font-size:96px;letter-spacing:-.05em;line-height:.95}}
.t i{{font-weight:300}}
.hd{{position:absolute;left:70px;right:70px;top:600px;display:flex;font-weight:700;font-size:24px;letter-spacing:.2em;text-transform:uppercase}}
.hd span{{flex:1}} .hd span+span{{color:{PK};padding-left:40px}}
.tb{{position:absolute;left:70px;right:70px;top:660px}}
.r{{display:flex;border-top:2px solid #111;padding:44px 0}} .r:last-child{{border-bottom:2px solid #111}}
.r span{{flex:1;font-size:50px;letter-spacing:-.03em}} .r span:first-child{{color:#9A938C;text-decoration:line-through;text-decoration-thickness:2px}}
.r span+span{{font-weight:800;padding-left:40px;border-left:2px solid #111}}""",
f"""{T()}{N(2)}<div class="t">make it <i>a number</i></div><div class="hd"><span>instead of</span><span>say</span></div><div class="tb">{tr}</div>{U('#111')}""")
cks=["Open a HYSA account just for future you","raise your rates (or ask for a raise)","invest your money","sell what you don't use"]
ck=''.join(f'<div class="ck"><b></b><span>{x}</span></div>' for x in cks)
pg('CAR14-3','Carousel 14 · 3 · checklist',f""".pin{{background:{PI};color:#111}}
.t{{position:absolute;left:80px;right:80px;top:240px;font-weight:300;font-style:italic;font-size:84px;letter-spacing:-.04em;line-height:1}}
.t b{{font-style:normal;font-weight:800}}
.ls{{position:absolute;left:80px;right:80px;top:520px}}
.ck{{display:flex;align-items:flex-start;gap:34px;margin-bottom:84px}}
.ck b{{flex:none;width:58px;height:58px;border:3px solid #111;border-radius:10px;background:#fff}}
.ck span{{font-size:54px;font-weight:600;letter-spacing:-.03em;line-height:1.1;padding-top:2px}}
.ft{{position:absolute;left:80px;top:1270px;font-size:38px;font-weight:500}}
.ft b{{color:{PK}}}""",
f"""{T()}{N(3)}<div class="t"><b>this week's</b><br>money moves</div><div class="ls">{ck}</div><div class="ft">pick <b>one.</b> that's the manifestation.</div>{U('#111')}""")
pg('CAR14-4','Carousel 14 · 4 · highlighter quote + framed photo',f""".pin{{background:#fff;color:#111}}
.q{{position:absolute;left:70px;right:70px;top:250px;font-weight:800;font-size:112px;letter-spacing:-.055em;line-height:1.02}}
.q mark{{background:linear-gradient(transparent 55%,#F7B8D6 55%,#F7B8D6 92%,transparent 92%);color:inherit;padding:0 6px}}
.q i{{font-weight:300}}
.cap{{position:absolute;left:70px;top:1150px;width:430px;font-size:32px;line-height:1.3;font-weight:500}}""",
f"""{T()}{N(4)}<div class="q">you don't <i style="margin-right:.18em">wait</i> for the money. you make the <mark>money move.</mark></div>
<img class="f" src="{s('bobcash')}" style="left:560px;top:960px;width:360px;height:440px;object-position:50% 25%" {A}>
<div class="cap">manifestation without action is a daydream.</div>{U('#111')}""")
steps=[('week 1','say your number'),('week 2','see it, daily'),('week 3','one money move'),('week 4','check. adjust.')]
dots=''.join(f'<div class="d" style="left:{150+i*233}px"><b></b><span class="wk">{w}</span><span class="x">{x}</span></div>' for i,(w,x) in enumerate(steps))
pg('CAR14-5','Carousel 14 · 5 · timeline diagram',f""".pin{{background:{LI};color:#111}}
.t{{position:absolute;left:70px;right:70px;top:230px;font-weight:800;font-size:100px;letter-spacing:-.055em;line-height:.95}}
.t i{{font-weight:300}}
.ln{{position:absolute;left:150px;right:150px;top:720px;height:3px;background:#111}}
.d{{position:absolute;top:700px;width:0}}
.d b{{position:absolute;left:-20px;top:0;width:40px;height:40px;border-radius:50%;background:#111}}
.d:last-child b{{background:{PK}}}
.d .wk{{position:absolute;left:-90px;width:180px;top:-64px;text-align:center;color:#111;font-weight:800;font-size:24px;letter-spacing:.18em;text-transform:uppercase}}
.d .x{{position:absolute;left:-105px;width:210px;top:76px;text-align:center;font-weight:600;font-size:36px;line-height:1.1;letter-spacing:-.02em}}
.lp{{position:absolute;left:70px;right:70px;top:1040px;text-align:center;font-style:italic;font-weight:300;font-size:56px;letter-spacing:-.03em}}
.cm{{position:absolute;left:0;right:0;top:1170px;text-align:center;font-size:22px;letter-spacing:.16em;text-transform:uppercase;color:#6A625A}}""",
f"""{T()}{N(5)}<div class="t">one month, <i>realistically</i></div><div class="ln"></div>{dots}<div class="lp">then go again.</div><div class="cm">conceptual model · desire → imagine → act → evolve</div>{U('#111')}""")
# ================= CAR15 · journal prompts for your dream life =================
pg('CAR15-1','Carousel 15 · 1 · type + circle photo cover',f""".pin{{background:{PI};color:#0D0D0D}}
.a{{position:absolute;left:56px;top:250px;font-weight:900;font-size:210px;letter-spacing:-.07em;line-height:.85}}
.b{{position:absolute;left:60px;top:440px;font-weight:300;font-style:italic;font-size:190px;letter-spacing:-.06em;line-height:.85}}
.c2{{position:absolute;left:60px;top:1130px;width:600px;font-weight:800;font-size:96px;letter-spacing:-.04em;line-height:.95}}
img.ci{{position:absolute;left:540px;top:640px;width:400px;height:400px;border-radius:50%;object-fit:cover;object-position:50% 30%;border:10px solid #fff}}""",
f"""{T()}{N(1)}<div class="a">journal</div><div class="b">prompts</div><img class="ci" src="{s('curls')}" {A}><div class="c2">for your<br>dream life</div>{U('#0D0D0D')}""")
pr=["what do i want so badly i'm embarrassed to say it?","whose life makes me jealous, and which part exactly?","what would i do with a free tuesday?"]
li=''.join(f'<div class="it"><span class="n">0{i+1}</span><span class="p">{x}</span></div>' for i,x in enumerate(pr))
pg('CAR15-2','Carousel 15 · 2 · numbered list',f""".pin{{background:#fff;color:#111}}
.t{{position:absolute;left:70px;top:220px;font-weight:300;font-style:italic;font-size:150px;letter-spacing:-.06em;line-height:1}}
.ls{{position:absolute;left:70px;right:70px;top:480px}}
.it{{display:flex;gap:40px;border-top:2px solid #111;padding:64px 0}} .it:last-child{{border-bottom:2px solid #111}}
.n{{flex:none;width:110px;font-weight:900;font-size:76px;letter-spacing:-.05em;color:{PK};line-height:1}}
.p{{font-weight:600;font-size:52px;letter-spacing:-.03em;line-height:1.15}}""",
f"""{T()}{N(2)}<div class="t">desire</div><div class="ls">{li}</div>{U('#111')}""")
pg('CAR15-3','Carousel 15 · 3 · diptych',f""".pin{{background:{LI};color:#111}}
.cp{{position:absolute;top:900px;font-weight:700;font-size:26px;letter-spacing:.18em;text-transform:uppercase}}
.q{{position:absolute;left:70px;right:70px;top:1010px;text-align:center;font-style:italic;font-weight:300;font-size:66px;letter-spacing:-.035em;line-height:1.08}}
.sm{{position:absolute;left:70px;right:70px;top:1250px;text-align:center;font-size:32px;font-weight:500}}""",
f"""{T()}{N(3)}<img class="f" src="{s('sky')}" style="left:70px;top:200px;width:420px;height:680px;object-position:50% 25%" {A}><img class="f" src="{s('pinkmoney')}" style="left:510px;top:200px;width:420px;height:680px;object-position:50% 30%" {A}>
<div class="cp" style="left:70px">7am</div><div class="cp" style="left:510px">9pm</div>
<div class="q">write one full day in 2027.<br>morning to night.</div><div class="sm">what are you wearing? who texts you first?</div>{U('#111')}""")
pg('CAR15-4','Carousel 15 · 4 · giant numeral',f""".pin{{background:#fff;color:#111}}
.n{{position:absolute;left:40px;top:150px;font-weight:900;font-size:620px;letter-spacing:-.09em;line-height:1}}
.mn{{position:absolute;left:640px;top:520px;font-weight:300;font-style:italic;font-size:120px;letter-spacing:-.05em;color:{PK}}}
.q{{position:absolute;left:70px;right:70px;top:880px;font-weight:800;font-size:72px;letter-spacing:-.045em;line-height:1.02}}
.sm{{position:absolute;left:70px;right:70px;top:1180px;font-size:34px;font-weight:500;line-height:1.3}}""",
f"""{T()}{N(4)}<div class="n">10</div><div class="mn">min</div><div class="q">"what would future me do today?"</div><div class="sm">write it. then do it in the next 10 minutes.</div>{U('#111')}""")
pg('CAR15-5','Carousel 15 · 5 · fill in the blank',f""".pin{{background:{PI};color:#111}}
.t{{position:absolute;left:70px;right:70px;top:220px;font-weight:800;font-size:84px;letter-spacing:-.05em;line-height:.95}}
.t i{{font-weight:300}}
.fl{{position:absolute;left:70px;right:70px;top:480px;font-size:58px;font-weight:600;letter-spacing:-.03em;line-height:2.3}}
.fl u{{display:inline-block;width:380px;border-bottom:3px solid #111;text-decoration:none;height:1em}}
.fl em{{font-weight:300}}
.sm{{position:absolute;left:70px;right:70px;top:1260px;font-size:32px;font-weight:500}} .sm b{{color:{PK}}}""",
f"""{T()}{N(5)}<div class="t">every sunday,<br><i>fill this in</i></div>
<div class="fl">this week i <u></u><br>i don't want <u></u><br><em>anymore.</em><br>next week i will <u style="width:290px"></u></div><div class="sm">screenshot it. <b>save this.</b></div>{U('#111')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
