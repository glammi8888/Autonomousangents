# Megan's 11 ISSUE11 framework graphs redone in our CAR5 design family (G01–G11), Nov 17.
# Megan: "Can you redo the graphs I sent you within our style ?" (11 graph images pasted in chat). Wording = hers, word for word (lowercased);
# no eyebrow labels (Megan: "ah no eyebrow please"); Inter Tight, white / lilac / pink, black type + light italic, pink accent, logo top centre, issue11.app.
import math
from gen import doc, LOGO
from gen11 import S, T, U
PK='#C2207E'; LI='#F1EBFF'; PI='#F8DCEB'; HL='#F7B8D6'; INK='#111'
P={}
TT=f""".t{{position:absolute;left:70px;right:70px;top:190px;font-weight:800;font-size:88px;letter-spacing:-.055em;line-height:.95;color:{INK}}}
.t i{{font-weight:300}} svg.g{{position:absolute;left:0;top:0;width:1000px;height:1500px}}"""
DEF=f'<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{PK}"/></marker></defs>'
def tx(x,y,s,fs=36,w=800,it=False,fill=INK,a='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" font-family="Inter Tight" font-size="{fs}" font-weight="{w}" {"font-style=\"italic\"" if it else ""} fill="{fill}" letter-spacing="-0.5">{s}</text>'
def lab(x,y,a,b,fs=40,fill=INK):  # bold label + light italic sub
    return tx(x,y,a,fs,800,fill=fill)+''.join(tx(x,y+fs*(1.0+.85*j),l,int(fs*.8),500,True,fill=fill) for j,l in enumerate(b.split('|')) if l)
def page(k,title,bg,svg,extra=''):
    P[k]=doc(f'Graph {k[1:]} · {title}',S+TT+f'.pin{{background:{bg}}}',
      f'{T()}<div class="t">{title}</div><svg class="g" viewBox="0 0 1000 1500">{DEF}{svg}</svg>{extra}{U(INK)}')
def pt(cx,cy,r,deg): return (cx+r*math.cos(math.radians(deg)),cy+r*math.sin(math.radians(deg)))
def arcs(cx,cy,r,spans):
    o=''
    for a,b in spans:
        x1,y1=pt(cx,cy,r,a); x2,y2=pt(cx,cy,r,b)
        o+=f'<path d="M{x1:.0f} {y1:.0f} A{r} {r} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="{PK}" stroke-width="5" marker-end="url(#ah)"/>'
    return o
def loop(nodes,center,shape='rect',cx=500,cy=900,r=320,fill='#fff'):
    sp=[(-62,-28),(28,62),(118,152),(208,242)] if shape=='rect' else [(-58,-32),(32,58),(122,148),(212,238)]
    o=arcs(cx,cy,r,sp)
    for (a,b),deg in zip(nodes,(-90,0,90,180)):
        x,y=pt(cx,cy,r,deg)
        if shape=='rect': o+=f'<rect x="{x-150:.0f}" y="{y-80:.0f}" width="300" height="160" rx="24" fill="{fill}" stroke="{INK}" stroke-width="3"/>'+lab(x,y-8,a,b,46)
        else: o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="138" fill="{fill}" stroke="{INK}" stroke-width="3"/>'+lab(x,y-8,a,b,42)
    for i,l in enumerate(center): o+=tx(cx,cy-20+i*50+(0 if len(center)>1 else 20),l,42,700,True)
    return o
# G01 the manifestation loop
page('G01','the manifestation <i>loop</i>','#fff',
     loop([('desire','(clarify)'),('imagine','(rehearse)'),('act','(participate)'),('evolve','(refine)')],['continuous','creation'])
     +tx(500,1385,'the new way of manifestation.',40,800))
# G02 the old way vs the issue11 way
old=["Visualize &amp; wait","All or nothing","“Be in alignment”","Perfect mindset","One-time manifestation"]
new=["Imagine + participate","Iterative &amp; adaptive","Aligned action","Human &amp; strategic","A continuous loop"]
rows=''.join(f'<div class="r"><span class="o">✕ {a}</span><span class="n">✓ {b}</span></div>' for a,b in zip(old,new))
P['G02']=doc('Graph 02 · old vs new',S+TT+f""".pin{{background:{PI}}}
.tb{{position:absolute;left:50px;right:50px;top:500px;background:#fff;border:3px solid {INK};border-radius:22px;overflow:hidden}}
.hd,.r{{display:flex}} .hd span,.r span{{flex:1;padding:36px 28px}}
.hd span{{font-weight:800;font-size:46px;letter-spacing:-.03em;border-bottom:3px solid {INK}}} .hd span+span{{background:{HL};border-left:3px solid {INK}}}
.r span{{font-size:40px;letter-spacing:-.02em;line-height:1.1}} .r span.o{{color:#8A837C}} .r span.n{{font-weight:700;border-left:3px solid {INK}}}
.r+.r span{{border-top:1px solid #E4DDD6}}""",
f"""{T()}<div class="t">the old way <i>vs</i> the ISSUE11 way</div><div class="tb"><div class="hd"><span>the old way</span><span>the ISSUE11 way</span></div>{rows}</div>{U(INK)}""")
# G03 from desire to reality (staircase)
st=[('1','desire','define it'),('2','imagine','rehearse it'),('3','act','make it real'),('4','evolve','adapt &amp; grow')]
o=f'<path d="M90 1380 C 520 1370, 840 1060, 950 520" fill="none" stroke="{PK}" stroke-width="5" marker-end="url(#ah)"/>'
for i,(n,a,b) in enumerate(st):
    x=50+i*225; y=1150-i*190
    o+=f'<rect x="{x}" y="{y}" width="225" height="210" rx="14" fill="{HL if i==3 else "#fff"}" stroke="{INK}" stroke-width="3"/>'+tx(x+112,y+72,n,64,900)+lab(x+112,y+132,a,b,40)
page('G03','from desire <i>to reality</i>',LI,o)
# G04 the reality creation map (3-circle venn)
A=(500,690);B=(360,930);C=(640,930);R=260
v=f'<clipPath id="cb"><circle cx="{B[0]}" cy="{B[1]}" r="{R}"/></clipPath><clipPath id="cc"><circle cx="{C[0]}" cy="{C[1]}" r="{R}"/></clipPath>'
v+=f'<g clip-path="url(#cb)"><g clip-path="url(#cc)"><circle cx="{A[0]}" cy="{A[1]}" r="{R}" fill="{HL}"/></g></g>'
v+=''.join(f'<circle cx="{x}" cy="{y}" r="{R}" fill="none" stroke="{INK}" stroke-width="3"/>' for x,y in (A,B,C))
v+=lab(500,590,'belief','(it’s possible)',46)+lab(275,1000,'identity','(i am her)',46)+lab(725,1000,'action','(i participate)',46)+lab(500,835,'reality','shift',38)
page('G04','the reality <i>creation map</i>','#fff',v)
# G05 the versions of you (nested circles)
v=''; base=1300
for r,f in ((450,'none'),(345,'none'),(240,'none'),(130,HL)):
    v+=f'<circle cx="500" cy="{base-r}" r="{r}" fill="{f}" stroke="{INK}" stroke-width="3"/>'
v+=f'<path d="M560 1120 L 860 560" fill="none" stroke="{PK}" stroke-width="5" marker-end="url(#ah)"/>'
v+=lab(500,480,'expanded you','(what’s next)',42)+lab(500,690,'evolving you','(in process)',42)+lab(500,895,'aligned you','(making it real)',42)+lab(500,1150,'current you','(the starting point)',38)
page('G05','the versions <i>of you</i>',PI,v)
# G06 create → test → learn → evolve
page('G06','create → test → <i>learn → evolve</i>',LI,
     loop([('create','(a plan /|experiment)'),('test','(in real life)'),('learn','(what works)'),('evolve','(adjust / level up)')],['the adaptive','loop'],shape='circle',r=330,cy=900))
# G07 the reality triangle
v=f'<path d="M500 580 L 140 1180 L 860 1180 Z" fill="{HL}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
v+=lab(500,480,'imagination','(create the vision)',48)+lab(500,960,'reality','creation',48)+lab(190,1260,'identity','(become her)',48)+lab(810,1260,'action','(participate)',48)
page('G07','the reality <i>triangle</i>','#fff',v)
# G08 the expansion cycle (infinity + checklist)
inf='M500 720 C 400 560, 130 560, 130 720 C 130 880, 400 880, 500 720 C 600 560, 870 560, 870 720 C 870 880, 600 880, 500 720'
v=f'<path d="{inf}" fill="none" stroke="{PK}" stroke-width="6"/>'
v+=f'<path d="M250 600 L 300 597" stroke="{PK}" stroke-width="6" marker-end="url(#ah)"/><path d="M750 840 L 700 843" stroke="{PK}" stroke-width="6" marker-end="url(#ah)"/>'
v+=lab(300,715,'experience','(live)',44)+lab(700,715,'evolve','(expand)',44)
for i,w in enumerate(['try','learn','adapt','level up','repeat']):
    y=990+i*80; v+=f'<rect x="360" y="{y-38}" width="46" height="46" rx="8" fill="#fff" stroke="{INK}" stroke-width="3"/>'+tx(436,y,w,46,700,a='start')
page('G08','the expansion <i>cycle</i>',PI,v)
# G09 self-concept → reality (2-circle venn)
L=(360,840);Rr=(640,840);R=300
v=f'<clipPath id="cr"><circle cx="{Rr[0]}" cy="{Rr[1]}" r="{R}"/></clipPath><g clip-path="url(#cr)"><circle cx="{L[0]}" cy="{L[1]}" r="{R}" fill="{HL}"/></g>'
v+=''.join(f'<circle cx="{x}" cy="{y}" r="{R}" fill="none" stroke="{INK}" stroke-width="3"/>' for x,y in (L,Rr))
v+=tx(215,800,'how you',36,800)+tx(215,842,'see yourself',36,800)+tx(215,884,'(identity)',30,500,True)
v+=tx(785,820,'how you act',36,800)+tx(785,862,'(behavior)',30,500,True)
v+=tx(500,800,'how',46,900)+tx(500,848,'you live',46,900)+tx(500,894,'(reality)',32,500,True)
v+=tx(500,1280,'self-concept → decisions → outcomes',42,800)
page('G09','self-concept <i>→ reality</i>',LI,v)
# G10 the reality upgrade (bars)
bars=[('clarity','(know what)',250),('capacity','(become who)',420),('consistency','(do the work)',590),('expansion','(sustain &amp; grow)',760)]
v=f'<path d="M70 850 C 380 800, 700 620, 945 420" fill="none" stroke="{PK}" stroke-width="5" marker-end="url(#ah)"/>'
for i,(a,b,h) in enumerate(bars):
    x=60+i*220; y=1340-h
    v+=f'<rect x="{x}" y="{y}" width="220" height="{h}" fill="{HL if i==3 else "#FBEAF2"}" stroke="{INK}" stroke-width="3"/>'+lab(x+110,y+64,a,b,38 if a!='consistency' else 32)
page('G10','the reality <i>upgrade</i>','#fff',v)
# G11 the new way of manifestation
page('G11','the new way <i>of manifestation</i>',PI,
     loop([('imagine','(create)'),('participate','(act)'),('adapt','(learn)'),('evolve','(expand)')],['a continuous','creation system'],cy=930))
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
