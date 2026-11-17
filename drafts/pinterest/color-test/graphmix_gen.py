# Megan's 10 other framework graphs, each drawn in the pin #100 look and each in a DIFFERENT pin style (LG1–LG10), Nov 17.
# Megan: "I want the graphs to keep the look of pin # 100" + "Yes but I need you to mix and match the content of the pins too".
# #100 look = thick round hand-drawn arrows/lines, bold floating words, no boxes. Wording = her graphs, word for word (lowercased). No eyebrow labels.
import math, gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
A='alt="Editorial photo (AI-generated)"'
def head(x2,y2,cx,cy,L=42):
    a=math.atan2(y2-cy,x2-cx); o=''
    for d in (2.6,-2.6):
        o+=f'<path d="M{x2:.0f} {y2:.0f} L{x2+L*math.cos(a+d):.0f} {y2+L*math.sin(a+d):.0f}"/>'
    return o
def arr(x1,y1,cx,cy,x2,y2,hd=True):  # quadratic hand arrow
    return f'<path d="M{x1} {y1} Q{cx} {cy} {x2} {y2}"/>'+(head(x2,y2,cx,cy) if hd else '')
def svg(inner,ink,sw): return f'<svg viewBox="0 0 1000 1500" style="position:absolute;inset:0"><g fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{inner}</g></svg>'
def w(x,y,t,ink,fw=800,fs=70,al='left',extra='',width=None):
    pos=f'left:{x}px;' if al=='left' else (f'right:{x}px;' if al=='right' else f'left:{x-300}px;width:600px;')
    if width: pos=f'left:{x}px;width:{width}px;'
    return f'<div style="position:absolute;{pos}top:{y}px;text-align:{"center" if al=="center" else al};font-weight:{fw};font-size:{fs}px;letter-spacing:-.03em;line-height:1.02;color:{ink};{extra}">{t}</div>'
def sub(x,y,t,ink,fs=34,al='center',extra=''): return w(x,y,t,ink,500,fs,al,'font-style:italic;letter-spacing:-.01em;'+extra)
SP=lambda x,y,c,f=100: f'<div style="position:absolute;left:{x}px;top:{y}px;color:{c};font-size:{f}px">✦</div>'
P={}
def pin(k,title,bg,body,url='#111',logo=''):
    P[k]=doc(f'Graph mix {k[2:]} · {title}',S+f'.pin{{background:{bg}}}',f'{T(logo)}{body}{U(url)}')
# LG1 · old way vs issue11 way · cream letter (110)
ink='#2A211A'; old=["visualize &amp; wait","all or nothing","“be in alignment”","perfect mindset","one-time manifestation"]; new=["imagine + participate","iterative &amp; adaptive","aligned action","human &amp; strategic","a continuous loop"]
b=w(70,200,'the old way <i style="font-weight:300">→</i><br>the ISSUE11 way',ink,800,70,width=860); g=''
for i,(o,n) in enumerate(zip(old,new)):
    y=520+i*175
    b+=w(70,y,o,'#9A8E82',400,38,width=330,extra='text-decoration:line-through;text-decoration-thickness:2px')+w(560,y,n,ink,800,42,width=380)
    g+=arr(410,y+26,470,y+6,530,y+26)
pin('LG1','old vs new','#FBF3EA',svg(g,ink,9)+b,ink)
# LG2 · from desire to reality · loud poster (101)
pt=[(60,1240,'1 desire','define it'),(270,1020,'2 imagine','rehearse it'),(500,800,'3 act','make it real'),(660,580,'4 evolve','adapt &amp; grow')]
g=''; b='<div style="position:absolute;left:44px;right:44px;top:190px;text-transform:uppercase;line-height:.86;letter-spacing:-.05em;font-weight:900;font-size:120px;color:#0D0D0D">from desire<br>to reality</div>'
for i,(x,y,t,sb) in enumerate(pt):
    b+=w(x,y,t,'#0D0D0D',800,62)+w(x,y+70,sb,'#0D0D0D',500,32,extra='font-style:italic')
    if i<3: nx,ny=pt[i+1][0],pt[i+1][1]; g+=arr(x+30,y-20,x+40,ny+40,nx-25,ny+36)
pin('LG2','desire to reality','#fff',svg(g,'#0D0D0D',12)+b+SP(860,470,'#E8A9D4',90))
# LG3 · reality creation map · plain white light (103)
g=''.join(f'<circle cx="{x}" cy="{y}" r="250"/>' for x,y in ((500,700),(360,940),(640,940)))
b=w(500,520,'belief','#111',400,76,'center')+sub(500,605,'(it’s possible)','#111')+w(240,960,'identity','#111',400,70,'center')+sub(240,1040,'(i am her)','#111')+w(760,960,'action','#111',400,70,'center')+sub(760,1040,'(i participate)','#111')
b+=w(500,800,'reality<br>shift','#C2207E',800,46,'center')
pin('LG3','reality creation map','#fff',svg(g,'#111',8)+b)
# LG4 · versions of you · pink + magenta (114)
mk='#C2207E'; g=''.join(f'<circle cx="500" cy="{1300-r}" r="{r}"/>' for r in (450,340,235,125))+arr(560,1110,740,840,880,560)
b=w(500,420,'expanded you',mk,700,52,'center')+sub(500,480,'(what’s next)',mk,30)+w(500,640,'evolving you',mk,700,52,'center')+sub(500,700,'(in process)',mk,30)+w(500,850,'aligned you',mk,700,52,'center')+sub(500,910,'(making it real)',mk,30)+w(500,1120,'current you',mk,800,44,'center')+sub(500,1172,'(the starting point)',mk,26)
pin('LG4','versions of you','#FCD4DA',svg(g,mk,10)+b,'#2A0F18')
# LG5 · adaptive loop · aura (125) with #100 arrows
ARW='<path d="M190 600 C150 460 220 380 330 360"/><path d="M300 330 l40 30 -40 35"/><path d="M700 380 C860 400 900 520 860 640"/><path d="M820 610 l40 40 45 -45"/><path d="M860 960 C860 1080 780 1150 680 1170"/><path d="M710 1130 l-40 40 45 35"/><path d="M260 1110 C160 1040 140 920 180 830"/><path d="M150 870 l30 -45 40 40"/>'
gi='#2D3B22'
b=w(500,300,'create',gi,700,72,'center')+sub(500,382,'(a plan / experiment)',gi,30)+w(70,650,'evolve',gi,700,72)+sub(180,735,'(adjust / level up)',gi,28)+w(70,650,'test',gi,700,72,'right')+sub(820,735,'(in real life)',gi,28)+w(500,1150,'learn',gi,700,72,'center')+sub(500,1232,'(what works)',gi,30)
b+=w(500,880,'the adaptive<br>loop',gi,600,40,'center','font-style:italic')
pin('LG5','adaptive loop','radial-gradient(circle at 50% 52%,#FFF6C8 0%,#E9F2B8 18%,#B9D69A 38%,#8DB884 60%,#6E9A72 100%)',svg(ARW,gi,14)+b+SP(470,580,'#FFF6C8'),gi)
# LG6 · reality triangle · spaced caps (137)
cap='letter-spacing:.32em;'
g='<path d="M500 560 C 420 700, 260 960, 160 1140 C 400 1150, 640 1145, 840 1140 C 740 960, 590 710, 500 560"/>'
b=w(50,430,'I M A G I N A T I O N','#111',500,36,'center',cap,width=900)+sub(500,485,'(create the vision)','#111',30)
b+=w(500,920,'R E A L I T Y<br>C R E A T I O N','#111',600,34,'center','line-height:1.5;')
b+=w(230,1190,'I D E N T I T Y','#111',500,36,'center',cap)+sub(230,1240,'(become her)','#111',28)+w(770,1190,'A C T I O N','#111',500,36,'center',cap)+sub(770,1240,'(participate)','#111',28)
pin('LG6','reality triangle','#FAF6F0',svg(g,'#111',6)+b)
# LG7 · expansion cycle · #100 pink
g='<path d="M500 720 C 400 540, 120 540, 120 720 C 120 900, 400 900, 500 720 C 600 540, 880 540, 880 720 C 880 900, 600 900, 500 720"/>'+head(330,588,250,575)+head(670,852,750,865)
for i in range(5): y=1000+i*80; g+=f'<rect x="395" y="{y-6}" width="48" height="48" rx="10" stroke-width="6"/>'
b=w(300,690,'experience','#111',800,54,'center')+sub(300,752,'(live)','#111',30)+w(700,690,'evolve','#111',800,54,'center')+sub(700,752,'(expand)','#111',30)
b+=''.join(w(470,1000+i*80-6,t,'#111',700,46) for i,t in enumerate(['try','learn','adapt','level up','repeat']))
b+=w(50,300,'the expansion cycle','#111',800,66,'center',width=900)
pin('LG7','expansion cycle','#F8DCEB',svg(g,'#111',14)+b+SP(840,420,'#E8A9D4',70))
# LG8 · self-concept → reality · lilac (42 palette)
g='<circle cx="370" cy="820" r="290"/><circle cx="630" cy="820" r="290"/>'
b=w(200,740,'how you<br>see yourself','#111',800,40,'center')+sub(200,840,'(identity)','#111',28)+w(800,760,'how you act','#111',800,40,'center')+sub(800,812,'(behavior)','#111',28)
b+=w(500,740,'how<br>you live','#C2207E',800,52,'center')+sub(500,860,'(reality)','#C2207E',30)
b+=w(500,1230,'self-concept → decisions → outcomes','#111',600,38,'center','font-style:italic')
pin('LG8','self-concept to reality','#F1EBFF',svg(g,'#111',12)+b+SP(470,470,'#C9B8F0',80))
# LG9 · reality upgrade · full photo, white (133-style)
sh='text-shadow:0 2px 14px rgba(0,0,0,.8);'
g=arr(60,1340,880,1330,950,600)
st=[(60,1180,'clarity','(know what)'),(250,1010,'capacity','(become who)'),(430,840,'consistency','(do the work)'),(600,670,'expansion','(sustain &amp; grow)')]
b=''.join(w(x,y,a,'#fff',800,58,extra=sh)+w(x,y+64,c,'#fff',500,30,extra='font-style:italic;'+sh) for x,y,a,c in st)
b+=w(500,250,'the reality upgrade','#fff',800,74,'center',sh)
pin('LG9','reality upgrade','#111',SP(820,420,'#E8A9D4',90)+f'<svg viewBox="0 0 1000 1500" style="position:absolute;inset:0;filter:drop-shadow(0 2px 8px rgba(0,0,0,.6))"><g fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round">{g}</g></svg>'+b,'#fff','w')
# LG10 · the new way of manifestation · white + framed photo in the loop (42)
b=w(500,300,'imagine','#111',800,72,'center')+sub(500,382,'(create)','#111',30)+w(70,650,'evolve','#111',800,72)+sub(180,735,'(expand)','#111',28)+w(40,650,'participate','#111',800,64,'right')+sub(800,735,'(act)','#111',28)+w(500,1150,'adapt','#111',800,72,'center')+sub(500,1232,'(learn)','#111',30)
b+=f'<img class="f" src="{s("sky")}" style="left:360px;top:520px;width:280px;height:400px;object-position:50% 25%" {A}>'+w(500,950,'a continuous<br>creation system','#111',500,34,'center','font-style:italic')
pin('LG10','new way of manifestation','#fff',svg(ARW,'#111',14)+b)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
