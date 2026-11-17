# Redo of LG1–LG8 in the LG9 / LG10 family (NG1–NG8), Nov 17. Megan: "ok i like Graph mix 9 and 10" + "The other ones the font doesn't fit in the grahs" + "especially 3 4 6".
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
# Rule from LG9/LG10: bold 800 words + small italic subs sit in OPEN space, never inside circles/triangles; graph = hand-drawn arrows (#100 look);
# two looks only: black + white ink (LG9) or white + framed photo (LG10). Titles bold, centred, like LG9.
K='#111'; WH='#fff'
def pin(k,title,dark,body,photo=None,pos='50% 25%',box=(360,560,280,400)):
    ink=WH if dark else K
    ph=f'<img class="f" src="{s(photo)}" style="left:{box[0]}px;top:{box[1]}px;width:{box[2]}px;height:{box[3]}px;object-position:{pos}" {A}>' if photo else ''
    P[k]=doc(f'Graph v2 {k[2:]} · {title}',S+f'.pin{{background:{"#111" if dark else "#fff"}}}',f'{T("w" if dark else "")}{ph}{body}{U(ink)}')
TL=lambda t,ink,y=230: w(50,y,t,ink,800,72,'center',width=900)
# NG1 · old way → ISSUE11 way · black
old=["visualize &amp; wait","all or nothing","“be in alignment”","perfect mindset","one-time manifestation"]; new=["imagine + participate","iterative &amp; adaptive","aligned action","human &amp; strategic","a continuous loop"]
b=w(50,220,'the old way →<br>the ISSUE11 way',WH,800,66,'center',width=900); g=''
for i,(o,n) in enumerate(zip(old,new)):
    y=480+i*180
    b+=w(60,y,o,'#8C8C8C',700,36,width=330,extra='text-decoration:line-through;text-decoration-thickness:3px')+w(560,y,n,WH,800,44,width=400)
    g+=arr(400,y+28,460,y+4,525,y+28)
pin('NG1','old vs new',True,svg(g,WH,10)+b+SP(860,1340,'#E8A9D4',70))
# NG2 · from desire to reality · white + photo top right
pt=[(60,1220,'1 desire','define it'),(230,1010,'2 imagine','rehearse it'),(400,800,'3 act','make it real'),(560,590,'4 evolve','adapt &amp; grow')]
g=''; b=TL('from desire to reality',K,220)
for i,(x,y,t,sb) in enumerate(pt):
    b+=w(x,y,t,K,800,60)+sub(x,y+68,sb,K,30,'left')
    if i<3: nx,ny=pt[i+1][:2]; g+=arr(x+30,y-20,x+40,ny+40,nx-25,ny+36)
pin('NG2','desire to reality',False,svg(g,K,12)+b,photo='curls',pos='50% 30%',box=(660,880,280,400))
# NG3 · reality creation map · black: 3 words around, arrows pointing in to "reality shift"
g=arr(500,680,470,760,500,820)+arr(250,1110,330,1040,410,980)+arr(750,1110,670,1040,590,980)
b=TL('the reality creation map',WH)
b+=w(500,530,'belief',WH,800,72,'center')+sub(500,610,'(it’s possible)',WH,30)
b+=w(500,860,'reality shift',WH,800,62,'center','color:#F7B8D6')
b+=w(220,1140,'identity',WH,800,66,'center')+sub(220,1216,'(i am her)',WH,30)+w(780,1140,'action',WH,800,66,'center')+sub(780,1216,'(i participate)',WH,30)
pin('NG3','reality creation map',True,svg(g,WH,12)+b+SP(780,560,'#E8A9D4',80))
# NG4 · versions of you · white + photo: bottom→top with arrows
st=[(1190,'current you','(the starting point)'),(950,'aligned you','(making it real)'),(710,'evolving you','(in process)'),(470,'expanded you','(what’s next)')]
b=TL('the versions of you',K); g=''
for i,(y,a,c) in enumerate(st):
    x=80+i*70
    b+=w(x,y,a,K,800,58)+sub(x,y+64,c,K,30,'left')
    if i<3: g+=arr(x+60,y-14,x+40,y-90,x+110,st[i+1][0]+120)
pin('NG4','versions of you',False,svg(g,K,12)+b,photo='pinkgloss',pos='50% 30%',box=(640,700,300,430))
# NG5 · adaptive loop · black, #100 loop in white (LG10 layout)
ARW='<path d="M190 600 C150 460 220 380 330 360"/><path d="M300 330 l40 30 -40 35"/><path d="M700 380 C860 400 900 520 860 640"/><path d="M820 610 l40 40 45 -45"/><path d="M860 960 C860 1080 780 1150 680 1170"/><path d="M710 1130 l-40 40 45 35"/><path d="M260 1110 C160 1040 140 920 180 830"/><path d="M150 870 l30 -45 40 40"/>'
b=w(500,300,'create',WH,800,72,'center')+sub(500,382,'(a plan / experiment)',WH,30)+w(70,650,'evolve',WH,800,72)+sub(180,735,'(adjust / level up)',WH,28)+w(70,650,'test',WH,800,72,'right')+sub(820,735,'(in real life)',WH,28)+w(500,1150,'learn',WH,800,72,'center')+sub(500,1232,'(what works)',WH,30)
b+=w(500,860,'the adaptive<br>loop',WH,500,40,'center','font-style:italic')
pin('NG5','adaptive loop',True,svg(ARW,WH,14)+b+SP(470,560,'#E8A9D4',90))
# NG6 · reality triangle · white + photo in the middle, corners linked by arrows
g=arr(400,560,250,700,190,880)+arr(250,1180,500,1260,750,1180)+arr(810,880,750,700,600,560)
b=w(500,430,'imagination',K,800,66,'center')+sub(500,502,'(create the vision)',K,30)
b+=w(170,1060,'identity',K,800,62,'center')+sub(170,1132,'(become her)',K,30)+w(830,1060,'action',K,800,62,'center')+sub(830,1132,'(participate)',K,30)
b+=w(500,1290,'reality creation',K,500,40,'center','font-style:italic')+TL('the reality triangle',K,230)
pin('NG6','reality triangle',False,svg(g,K,12)+b,photo='blue',pos='50% 25%',box=(405,690,190,280))
# NG7 · expansion cycle · black
g='<path d="M500 760 C 400 600, 140 600, 140 760 C 140 920, 400 920, 500 760 C 600 600, 860 600, 860 760 C 860 920, 600 920, 500 760"/>'+head(330,640,250,625)+head(670,880,750,895)
b=TL('the expansion cycle',WH)+w(300,500,'experience',WH,800,60,'center')+sub(300,568,'(live)',WH,30)+w(700,500,'evolve',WH,800,60,'center')+sub(700,568,'(expand)',WH,30)
for i,tx_ in enumerate(['try','learn','adapt','level up','repeat']):
    y=1000+i*74; g+=f'<rect x="380" y="{y-4}" width="44" height="44" rx="10" stroke-width="6"/>'; b+=w(450,y-8,tx_,WH,800,46)
pin('NG7','expansion cycle',True,svg(g,WH,14)+b+SP(830,400,'#E8A9D4',70))
# NG8 · self-concept → reality · white + photo, two words flowing into it
g=arr(230,640,250,780,350,800)+arr(770,640,750,780,650,800)
b=TL('self-concept → reality',K)+w(230,470,'how you<br>see yourself',K,800,46,'center')+sub(230,580,'(identity)',K,30)+w(770,500,'how you act',K,800,46,'center')+sub(770,560,'(behavior)',K,30)
b+=w(500,1110,'how you live',K,800,64,'center','color:#C2207E')+sub(500,1184,'(reality)',K,30)+w(500,1290,'self-concept → decisions → outcomes',K,500,36,'center','font-style:italic')
pin('NG8','self-concept to reality',False,svg(g,K,12)+b,photo='red',pos='50% 25%',box=(380,640,240,420))
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
