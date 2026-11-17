# CAR16 + CAR17 (Nov 17): Megan's framework diagrams as CONTENT, drawn in ISSUE11's own carousel look (CAR2–CAR4:
# Inter Tight 900, cream/black, magenta + pink accents, mono labels, framed editorial photos, logo top-left).
# Megan: "No I want those graphs to be added to our slides, you can change the style because I don't like the style".
# Instagram 1080x1350. Run: python3 gen34.py  → ../carousels/CAR16/*.dc.html, ../carousels/CAR17/*.dc.html
# Copy sources (word for word unless marked ADAPTED) are listed in ../carousels/README.md and the report.
import os
D=os.path.dirname(os.path.abspath(__file__))
LOGO='/_blob/d196614efc6265e2205729134fb523b8'
PH={'hairwind':'68963da8e26c9286d2fba8b5c3edb3bb','hairwhite':'7feef729a80262f2d7e85c6834638c97',
    'whitejacket':'a5d556e3904ad3660587c191ff3898c6','red':'fe93ea3b39f07ff739b7ef958b5ba623',
    'curls':'2f1673a637c73371ea14b83819994320','soft':'4e778283bc9ea80ceaef2cab845c3108','knit':'034dc4a58467509df431ad7092996c57'}
A='alt="Editorial photo (AI-generated)"'
INK='#111';CREAM='#FBF8F3';PAPER='#F4EEE3';MAG='#C2207E';PINK='#F6C6D6';RED='#C8102E'
MONO="ui-monospace,'DejaVu Sans Mono','Courier New',monospace"
BASE=f"""body{{margin:0}}
.pin{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Inter Tight',system-ui,sans-serif;background:{CREAM};color:{INK}}}
.lg{{position:absolute;left:56px;top:48px;height:66px}}
.w{{filter:invert(1)}}
.ct{{position:absolute;right:56px;top:68px;font-weight:700;font-size:22px;letter-spacing:.2em}}
.kick{{position:absolute;left:56px;right:56px;top:158px;font-weight:700;font-size:24px;letter-spacing:.24em;color:{MAG}}}
.url{{position:absolute;left:0;right:0;bottom:40px;text-align:center;font-weight:600;font-size:20px}}
.mono{{font-family:{MONO}}}
.lab{{position:absolute;left:0;right:0;text-align:center;font-family:{MONO};font-size:20px;letter-spacing:.14em}}
"""
def doc(title,css,body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;500;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>
{BASE}{css}
</style>
</helmet>
<div class="pin">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
"""
def head(i,n,kick,inv=False):
    return f'<img class="lg{" w" if inv else ""}" src="{LOGO}" alt="ISSUE11"><div class="ct">{i} / {n}</div><div class="kick">{kick}</div>'

BAR='<svg viewBox="0 0 200 60" width="150" height="45" fill="#fff" aria-hidden="true">'+''.join(f'<rect x="{x}" y="0" width="{w}" height="{58 if i in (0,20,42) else 50}"/>' for i,(x,w) in enumerate([(4,3),(10,3),(15,4.5),(22.5,1.5),(25.5,4.5),(32,4.5),(38,1.5),(41.5,2),(45,1.5),(49.5,1.5),(54,3),(59,4.5),(66.5,1.5),(71,1.5),(75.5,1.5),(78.5,1.5),(81.5,1.5),(86,1.5),(89.5,2),(93.5,4.5),(99.5,4.5),(105.5,2),(109.5,1.5),(114,1.5),(117.5,2),(121.5,4.5),(127.5,2),(131.5,1.5),(136,2),(139.5,1.5),(144,1.5),(147.5,1.5),(151,3),(155.5,1.5),(160,1.5),(163,1.5),(166,3),(171,3),(176,1.5),(180.5,1.5),(185,2),(189,1.5),(192.5,2)]))+'</svg>'

def cover(title,photo,pos,mast,mcol,kick,story,sub,lines,txt,shadow):
    ls='<br>'.join(f'<b style="color:{mcol}">{n}</b> {x}' for n,x in lines)
    sh='text-shadow:0 2px 18px rgba(0,0,0,.35);' if shadow else ''
    inv=' w' if txt!=INK else ''
    barfill='' if txt!=INK else '.bar svg{fill:#111}'
    return doc(title,f""".pin{{background:#222}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.dg{{position:absolute;left:40px;right:40px;top:36px;font-weight:900;font-size:168px;line-height:.8;letter-spacing:-.07em;text-transform:uppercase;white-space:nowrap;{sh}}}
.story{{position:absolute;left:56px;bottom:250px;color:{txt};font-weight:900;font-size:80px;line-height:.92;letter-spacing:-.045em;max-width:620px;{sh}}}
.story i{{display:block;font-weight:700;font-size:26px;letter-spacing:.2em;text-transform:uppercase;font-style:normal;margin-bottom:14px}}
.story span{{display:block;font-weight:700;font-size:30px;line-height:1.25;letter-spacing:-.01em;margin-top:22px;max-width:520px}}
.lines{{position:absolute;right:52px;bottom:250px;text-align:right;color:{txt};font-weight:800;font-size:30px;line-height:1.3;{sh}}}
.logo{{position:absolute;left:56px;bottom:40px;height:84px}}
.site{{position:absolute;left:0;right:0;bottom:62px;text-align:center;color:{txt};font-weight:600;font-size:20px;{sh}}}
.bar{{position:absolute;right:52px;bottom:40px;display:flex;flex-direction:column;align-items:center}}
.bar span{{font-weight:600;font-size:13px;letter-spacing:.16em;color:{txt};margin-top:2px}}{barfill}""",
f'''<img class="bg" src="/_blob/{PH[photo]}" style="object-position:{pos}" {A}>
<div class="dg" style="color:{mcol}">{mast}</div>
<div class="story"><i style="color:{txt}">{kick}</i>{story}<span>{sub}</span></div>
<div class="lines">{ls}</div>
<img class="logo{inv}" src="{LOGO}" alt="ISSUE11"><div class="site">issue11.app</div><div class="bar">{BAR}<span>8 88888 888 8888</span></div>''')

# two-steps-per-slide layout (CAR4-2 family)
STEP=f""".st{{position:absolute;left:56px;width:600px}}
.n{{font-weight:900;font-size:104px;line-height:.85;letter-spacing:-.06em}}
.h{{font-weight:900;font-size:56px;line-height:.95;letter-spacing:-.045em;text-transform:uppercase;margin-top:8px}}
.h small{{display:block;font-family:{MONO};font-weight:400;font-size:21px;letter-spacing:.04em;text-transform:none;margin-top:8px;color:{MAG}}}
.p{{font-weight:500;font-size:29px;line-height:1.3;letter-spacing:-.015em;margin-top:16px}}
.try{{margin-top:18px;border-left:6px solid {MAG};padding:4px 0 4px 20px;font-size:27px;line-height:1.3}}
.try b{{display:block;font-size:19px;letter-spacing:.2em;color:{MAG};margin-bottom:4px}}
.ph{{position:absolute;right:56px;width:320px;object-fit:cover}}
"""
def step(n,h,sub,p,lab,ex):
    return f'<div class="n">{n}</div><div class="h">{h}<small>({sub})</small></div><div class="p">{p}</div><div class="try"><b>{lab}</b>{ex}</div>'

P={}
# ───────────────────────── CAR16 · THE MANIFESTATION LOOP (6 slides) ─────────────────────────
N=6;K='THE MANIFESTATION LOOP'
P['CAR16/CAR16-1']=cover('Carousel 16 · slide 1 · cover','hairwind','30% 30%','Loop',MAG,'Cover story',
    'The manifestation loop','An intentional, adaptive practice of imagining a future and participating in making it more possible.',
    [('01','desire'),('02','imagine'),('03','embody'),('04','become')],INK,False)

# slide 2 · the diagram: a closed loop, 4 stations, magenta arrowheads clockwise, centre note
import math
cx,cy,r=540,735,318
def arrow(deg):
    a=math.radians(deg);x=cx+r*math.cos(a);y=cy+r*math.sin(a)
    t=a+math.pi/2  # clockwise tangent (screen coords)
    tip=(x+20*math.cos(t),y+20*math.sin(t));b1=(x-16*math.cos(t)+16*math.cos(a),y-16*math.sin(t)+16*math.sin(a));b2=(x-16*math.cos(t)-16*math.cos(a),y-16*math.sin(t)-16*math.sin(a))
    return f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {b1[0]:.1f},{b1[1]:.1f} {b2[0]:.1f},{b2[1]:.1f}" fill="{MAG}"/>'
svg=(f'<svg class="ring" viewBox="0 0 1080 1350" width="1080" height="1350" aria-hidden="true">'
     f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="3"/>'
     f'<circle cx="{cx}" cy="{cy}" r="{r-26}" fill="none" stroke="{PINK}" stroke-width="10"/>'
     +''.join(arrow(d) for d in (-45,45,135,225))+'</svg>')
def node(x,y,n,w,sub,dark=False):
    return (f'<div class="nd{" dk" if dark else ""}" style="left:{x}px;top:{y}px"><span class="nn">{n}</span>{w}'
            f'<small>({sub})</small></div>')
P['CAR16/CAR16-2']=doc('Carousel 16 · slide 2 · the loop diagram',f""".ring{{position:absolute;left:0;top:0}}
.nd{{position:absolute;width:250px;transform:translate(-50%,-50%);background:{CREAM};border:4px solid {INK};padding:16px 14px 14px;text-align:center;font-weight:900;font-size:42px;letter-spacing:-.035em;line-height:1}}
.nd.dk{{background:{INK};color:{CREAM}}}
.nn{{display:block;font-family:{MONO};font-weight:400;font-size:20px;letter-spacing:.14em;color:{MAG};margin-bottom:6px}}
.nd small{{display:block;font-weight:500;font-size:21px;letter-spacing:0;line-height:1.2;margin-top:8px}}
.mid{{position:absolute;left:390px;width:300px;top:630px;text-align:center;font-weight:600;font-size:28px;line-height:1.25;letter-spacing:-.015em}}
.mid b{{display:block;font-family:{MONO};font-weight:400;font-size:22px;letter-spacing:.14em;color:{MAG};margin-top:18px}}""",
f'''{head(2,N,K)}{svg}
{node(540,cy-r,'01','DESIRE','define what you actually want')}
{node(cx+r,cy,'02','IMAGINE','make that future vivid')}
{node(540,cy+r,'03','EMBODY','start practicing being that person')}
{node(cx-r,cy,'04','BECOME','notice the future becoming real',True)}
<div class="mid">Experience feeds back into imagination, belief, and choices.<b>↺ AND AGAIN</b></div>
<div class="lab" style="bottom:86px">CONCEPTUAL MODEL</div><div class="url">issue11.app</div>''')

P['CAR16/CAR16-3']=doc('Carousel 16 · slide 3 · desire + imagine',STEP,f'''{head(3,N,K)}
<div class="st" style="top:212px">{step('01','Desire','define what you actually want','Manifestation begins with desire. Ask whether it reflects genuine values or borrowed expectations.','EXAMPLE','you want to become a confident creative director')}</div>
<div class="st" style="top:772px">{step('02','Imagine','make that future vivid','Explore what it could feel and look like. Something you can see, read, revisit and eventually hold.','EXAMPLE','write one page about a normal tuesday in that life')}</div>
<img class="ph" src="/_blob/{PH['hairwhite']}" style="top:250px;height:420px;object-position:50% 20%" {A}>
<img class="ph" src="/_blob/{PH['whitejacket']}" style="top:810px;height:420px;object-position:50% 20%" {A}>
<div class="url">issue11.app</div>''')

P['CAR16/CAR16-4']=doc('Carousel 16 · slide 4 · embody + become',STEP,f'''{head(4,N,K)}
<div class="st" style="top:212px">{step('03','Embody','start practicing being that person','How would the version of you who lives this life think, feel, choose and behave?','YOUR NEXT MOVE','share one piece of work you\'ve been afraid to show')}</div>
<div class="st" style="top:772px">{step('04','Become','notice the future becoming real','Over time, you start collecting evidence that you are behaving differently.','PROOF','"I finally shared my work."')}</div>
<img class="ph" src="/_blob/{PH['curls']}" style="top:250px;height:420px;object-position:50% 20%" {A}>
<img class="ph" src="/_blob/{PH['soft']}" style="top:810px;height:420px;object-position:50% 25%" {A}>
<div class="url">issue11.app</div>''')

rows=[('DESIRE','What do I actually want?'),('IMAGINE','What does my future look and feel like?'),
      ('EMBODY','How would future you think, feel, choose and behave?'),('BECOME','What changed this week that makes it more possible?')]
P['CAR16/CAR16-5']=doc('Carousel 16 · slide 5 · save this',f""".pin{{background:{INK};color:{PAPER}}}
.kick{{color:{PINK}}}
.t{{position:absolute;left:56px;right:56px;top:220px;font-weight:900;font-size:104px;letter-spacing:-.06em;line-height:.9}}
.t span{{color:{PINK}}}
.ls{{position:absolute;left:56px;right:56px;top:500px;display:flex;flex-direction:column}}
.r{{display:grid;grid-template-columns:250px 1fr;gap:24px;align-items:baseline;border-top:2px solid {PAPER};padding:24px 0}}
.r:last-child{{border-bottom:2px solid {PAPER}}}
.r b{{font-family:{MONO};font-weight:400;font-size:24px;letter-spacing:.14em;color:{PINK}}}
.r span{{font-weight:700;font-size:36px;line-height:1.15;letter-spacing:-.025em}}
.back{{position:absolute;left:56px;right:56px;top:1150px;font-family:{MONO};font-size:22px;letter-spacing:.08em}}""",
f'''{head(5,N,K+' · SAVE THIS',True)}
<div class="t">The loop in <span>4</span> questions</div>
<div class="ls">{''.join(f'<div class="r"><b>0{i+1} {w}</b><span>{q}</span></div>' for i,(w,q) in enumerate(rows))}</div>
<div class="back">↺ then back to desire · conceptual model</div><div class="url">issue11.app</div>''')

P['CAR16/CAR16-6']=doc('Carousel 16 · slide 6 · ending',f""".pin{{background:{PINK}}}
.big{{position:absolute;left:56px;right:56px;top:330px;font-weight:900;font-size:128px;letter-spacing:-.055em;line-height:.9}}
.sm{{position:absolute;left:56px;right:56px;top:900px;font-weight:600;font-size:34px;line-height:1.25;letter-spacing:-.02em}}
.sm b{{display:block;font-family:{MONO};font-weight:400;font-size:22px;letter-spacing:.14em;margin-bottom:12px;color:{MAG}}}
.blg{{position:absolute;left:56px;bottom:120px;height:92px}}""",
f'''{head(6,N,K)}
<div class="big">Your future is not a spectator sport.</div>
<div class="sm"><b>ISSUE11</b>The new way of manifestation.</div>
<img class="blg" src="{LOGO}" alt="ISSUE11"><div class="url">issue11.app</div>''')

# ───────────────────────── CAR17 · THE OLD WAY VS. THE ISSUE11 WAY (7 slides) ─────────────────────────
N=7;K='THE OLD WAY VS. THE ISSUE11 WAY'
T=[('Visualize &amp; wait','Imagine + participate'),('All or nothing','Iterative &amp; adaptive'),('"Be in alignment"','Aligned action'),
   ('Perfect mindset','Human &amp; strategic'),('One-time manifestation','A continuous loop')]
P['CAR17/CAR17-1']=cover('Carousel 17 · slide 1 · cover','red','50% 20%','New way',PINK,'Cover story',
    'The old way vs. the ISSUE11 way','The new way of manifestation, in 5 shifts.',
    [('01','imagine + participate'),('02','iterative &amp; adaptive'),('03','aligned action'),('04','human &amp; strategic'),('05','a continuous loop')],'#fff',True)

P['CAR17/CAR17-2']=doc('Carousel 17 · slide 2 · comparison table',f""".tb{{position:absolute;left:56px;right:56px;top:236px;display:grid;grid-template-columns:1fr 64px 1fr}}
.hd{{font-family:{MONO};font-size:22px;letter-spacing:.14em;padding:22px 20px;border:4px solid {INK}}}
.hd.nw{{background:{INK};color:{CREAM};border-color:{INK}}}
.hd.ar{{border:0}}
.c{{border-bottom:2px solid {INK};padding:30px 20px;min-height:84px;display:flex;align-items:center}}
.o{{font-weight:500;font-size:34px;line-height:1.1;letter-spacing:-.02em;color:#5E5752}}
.a{{justify-content:center;font-weight:300;font-size:44px;color:{MAG};padding:30px 0}}
.nwc{{font-weight:900;font-size:40px;line-height:1;letter-spacing:-.035em;text-transform:uppercase;background:#fff}}
.nb{{font-family:{MONO};font-size:22px;letter-spacing:.06em;position:absolute;left:56px;right:56px;top:1150px;line-height:1.5}}""",
f'''{head(2,N,K)}
<div class="tb"><div class="hd">THE OLD WAY</div><div class="hd ar"></div><div class="hd nw">THE ISSUE11 WAY</div>
{''.join(f'<div class="c o">{o}</div><div class="c a">→</div><div class="c nwc">{n}</div>' for o,n in T)}</div>
<div class="nb">You don't have to see it to believe it.<br>But you have to participate to create it.</div>
<div class="lab" style="bottom:86px">SIMPLIFIED CONCEPTUAL COMPARISON</div><div class="url">issue11.app</div>''')

ROW=f""".st{{position:absolute;left:56px;right:56px}}
.no{{font-family:{MONO};font-size:24px;letter-spacing:.14em;color:{MAG}}}
.sh{{margin-top:12px;display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 18px}}
.sh .o{{font-weight:500;font-size:36px;letter-spacing:-.02em;color:#5E5752}}
.sh .a{{font-weight:300;font-size:44px;color:{MAG}}}
.sh .n{{font-weight:900;font-size:62px;letter-spacing:-.045em;line-height:.95;text-transform:uppercase}}
.p{{font-weight:600;font-size:36px;line-height:1.2;letter-spacing:-.025em;margin-top:22px;max-width:900px}}
.box{{margin-top:26px;padding:22px 26px;font-size:30px;line-height:1.28;letter-spacing:-.015em;max-width:880px}}
.box b{{display:block;font-family:{MONO};font-weight:400;font-size:20px;letter-spacing:.14em;margin-bottom:8px}}
.mis{{border:3px solid {INK}}}
.do{{background:{INK};color:{PAPER}}}
.ph{{position:absolute;right:56px;object-fit:cover}}
"""
def shift(i,p,lab,ex,kind='do'):
    o,n=T[i]
    return f'<div class="no">SHIFT 0{i+1}</div><div class="sh"><span class="o">{o}</span><span class="a">→</span><span class="n">{n}</span></div><div class="p">{p}</div><div class="box {kind}"><b>{lab}</b>{ex}</div>'

P['CAR17/CAR17-3']=doc('Carousel 17 · slide 3 · shifts 1–2',ROW,f'''{head(3,N,K)}
<div class="st" style="top:220px">{shift(0,"You don't have to see it to believe it. But you have to participate to create it.",'DO THIS','one if-then plan: "if it\'s sunday night, then I move $50 to savings"')}</div>
<div class="st" style="top:760px">{shift(1,'A setback is not a verdict. The desired future itself may evolve.','COMMON MISTAKE','giving up when it looks different than you pictured','mis')}</div>
<div class="url">issue11.app</div>''')

P['CAR17/CAR17-4']=doc('Carousel 17 · slide 4 · shifts 3–4',ROW,f'''{head(4,N,K)}
<div class="st" style="top:220px">{shift(2,'Waiting to feel completely ready can postpone meaningful experiments.','DO THIS','do a single meaningful task a day')}</div>
<div class="st" style="top:760px">{shift(3,'The path is allowed to look different. Experience teaches us what to do next.','DO THIS','every sunday, write one thing that changed')}</div>
<div class="url">issue11.app</div>''')

lp=''.join(f'<span>{w}</span>'+('<i>→</i>' if i<3 else '') for i,w in enumerate(['DESIRE','IMAGINE','EMBODY','BECOME']))
P['CAR17/CAR17-5']=doc('Carousel 17 · slide 5 · shift 5 + loop',ROW+f""".loop{{position:absolute;left:56px;right:56px;top:640px;border:4px solid {INK};padding:40px 28px 28px;text-align:center;background:#fff}}
.loop .r{{display:flex;justify-content:space-between;align-items:center;font-weight:900;font-size:44px;letter-spacing:-.03em}}
.loop i{{font-style:normal;font-weight:300;color:{MAG}}}
.loop .b{{margin-top:20px;font-size:24px;letter-spacing:.14em;color:{MAG};font-weight:700}}
.loop .l{{margin-top:8px;font-family:{MONO};font-size:18px;letter-spacing:.14em}}""",
f'''{head(5,N,K)}
<div class="st" style="top:220px"><div class="no">SHIFT 05</div><div class="sh"><span class="o">{T[4][0]}</span><span class="a">→</span><span class="n">{T[4][1]}</span></div><div class="p">Experience feeds back into imagination, belief, and choices.</div></div>
<div class="loop"><div class="r">{lp}</div><div class="b">↺ AND AGAIN</div><div class="l">CONCEPTUAL MODEL</div></div>
<div class="box mis" style="position:absolute;left:56px;top:900px;width:560px;box-sizing:border-box"><b>GOOD TO KNOW</b>Some changes become recognizable only after enough experiences accumulate.</div>
<img class="ph" src="/_blob/{PH['knit']}" style="top:900px;width:340px;height:330px;object-position:50% 18%" {A}>
<div class="url">issue11.app</div>''')

P['CAR17/CAR17-6']=doc('Carousel 17 · slide 6 · save this',f""".pin{{background:{INK};color:{PAPER}}}
.kick{{color:{PINK}}}
.t{{position:absolute;left:56px;right:56px;top:220px;font-weight:900;font-size:104px;letter-spacing:-.06em;line-height:.9}}
.t span{{color:{PINK}}}
.ls{{position:absolute;left:56px;right:56px;top:500px;display:flex;flex-direction:column;gap:30px}}
.r{{display:flex;align-items:center;gap:26px;font-weight:900;font-size:50px;letter-spacing:-.035em;text-transform:uppercase;line-height:1}}
.bx{{flex:0 0 auto;width:34px;height:34px;border:4px solid {PINK}}}
.back{{position:absolute;left:56px;right:56px;top:1150px;font-family:{MONO};font-size:22px;letter-spacing:.08em}}""",
f'''{head(6,N,'THE ISSUE11 WAY · SAVE THIS',True)}
<div class="t">The new way, in <span>5</span> lines</div>
<div class="ls">{''.join(f'<div class="r"><span class="bx"></span>{n}</div>' for o,n in T)}</div>
<div class="back">the new way of manifestation · conceptual model</div><div class="url">issue11.app</div>''')

P['CAR17/CAR17-7']=doc('Carousel 17 · slide 7 · ending',f""".pin{{background:{RED};color:{PAPER}}}
.kick{{color:{PAPER}}}
.big{{position:absolute;left:56px;right:56px;top:300px;font-weight:900;font-size:104px;letter-spacing:-.05em;line-height:.92}}
.sm{{position:absolute;left:56px;right:56px;top:960px;font-weight:600;font-size:34px;line-height:1.25;letter-spacing:-.02em}}
.sm b{{display:block;font-family:{MONO};font-weight:400;font-size:22px;letter-spacing:.14em;margin-bottom:12px}}
.blg{{position:absolute;left:56px;bottom:120px;height:92px}}""",
f'''{head(7,N,K,True)}
<div class="big">You don't have to see it to believe it. But you have to participate to create it.</div>
<div class="sm"><b>ISSUE11</b>The new way of manifestation.</div>
<img class="blg w" src="{LOGO}" alt="ISSUE11"><div class="url">issue11.app</div>''')

for k,v in P.items():
    out=os.path.join(D,'..','carousels',k+'.dc.html');os.makedirs(os.path.dirname(out),exist_ok=True);open(out,'w').write(v)
print(len(P))
