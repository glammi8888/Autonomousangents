# G01–G11 with colour: brand palette (design/claude-design/V4-TOKENS.md + landing notes), Nov 17.
# Megan: "Ok but let's add some colors! and our brand colors". Same layouts as graphs_v2_gen.py (LG9/LG10 look, #100 hand arrows, words in open space).
# Palette: ink #0D0D0D · white · pink #F65AAD · blush #FCD2DD · cream #F5EEE0 · cover red #D40806 · small pink text #C2207E.
import graphmix2_gen as m
from graphmix2_gen import w, sub, arr, head, svg, SP, ARW, s, A, T, U, S, doc
INK='#0D0D0D'; WH='#fff'; PP='#F8DCEB'; LI='#F1EBFF';  # pastel pink + lilac: Megan "I like the pastel pink and pastel purple you added too"
PK='#F65AAD'; BL='#FCD2DD'; CR='#F5EEE0'; RD='#D40806'; TP='#C2207E'
P={}
def pin(k,title,bg,ink,body,photo=None,pos='50% 25%',box=(360,560,280,400)):
    dark=bg in (INK,RD)
    ph=f'<img class="f" src="{s(photo)}" style="left:{box[0]}px;top:{box[1]}px;width:{box[2]}px;height:{box[3]}px;object-position:{pos}" {A}>' if photo else ''
    P[k]=doc(f'Graph {k[1:]} · {title} · colour',S+f'.pin{{background:{bg}}}',f'{T("w" if dark else "")}{ph}{body}{U(ink)}')
TL=lambda t,ink,y=230,fs=72: w(50,y,t,ink,800,fs,'center',width=900)
def loop4(words,ink,mid,acc_word=None):
    (a,a2),(r,r2),(bt,b2),(l,l2)=words
    b=w(500,300,a,acc_word or ink,800,72,'center')+sub(500,382,a2,ink,30)+w(70,650,l,ink,800,72)+sub(180,735,l2,ink,28)+w(70,650,r,ink,800,72 if len(r)<9 else 54,'right')+sub(820,735,r2,ink,28)+w(500,1150,bt,ink,800,72,'center')+sub(500,1232,b2,ink,30)
    return b+w(500,860,mid,ink,500,40,'center','font-style:italic')
# G01 · manifestation loop · hot pink bg, black words, white arrows
b=loop4([('desire','(clarify)'),('imagine','(rehearse)'),('act','(participate)'),('evolve','(refine)')],INK,'continuous<br>creation')+w(50,1310,'the new way of manifestation.',INK,800,40,'center',width=900)
pin('G01','manifestation loop',PK,INK,svg(ARW,WH,14)+b+SP(470,560,WH,90))
# G02 · old vs new · black, pink arrows, blush new words
old=["visualize &amp; wait","all or nothing","“be in alignment”","perfect mindset","one-time manifestation"]; new=["imagine + participate","iterative &amp; adaptive","aligned action","human &amp; strategic","a continuous loop"]
b=w(50,210,'old way of manifestation<br>vs the <span style="color:'+PK+'">new way</span>',WH,800,64,'center',width=900); g=''
for i,(o,n) in enumerate(zip(old,new)):
    y=520+i*175
    b+=w(60,y,o,'#8C8C8C',700,36,width=330,extra='text-decoration:line-through;text-decoration-thickness:3px')+w(560,y,n,WH,800,44,width=400)
    g+=arr(400,y+28,460,y+4,525,y+28)
pin('G02','old vs new',INK,WH,svg(g,PK,10)+b+SP(860,1340,PK,70))
# G03 · desire to reality · cream, red arrows, step 4 red
pt=[(60,1220,'1 desire','define it'),(230,1010,'2 imagine','rehearse it'),(400,800,'3 act','make it real'),(560,590,'4 evolve','adapt &amp; grow')]
g=''; b=TL('from desire to <span style="color:'+RD+'">reality</span>',INK,220)
for i,(x,y,t,sb) in enumerate(pt):
    b+=w(x,y,t,RD if i==3 else INK,800,60)+sub(x,y+68,sb,INK,30,'left')
    if i<3: nx,ny=pt[i+1][:2]; g+=arr(x+30,y-20,x+40,ny+40,nx-25,ny+36)
pin('G03','desire to reality',CR,INK,svg(g,RD,12)+b,photo='curls',pos='50% 30%',box=(660,880,280,400))
# G04 · reality creation map · red bg, white words, blush arrows + highlight
g=arr(500,680,470,760,500,820)+arr(250,1110,330,1040,410,980)+arr(750,1110,670,1040,590,980)
b=TL('the reality creation map',WH)+w(500,530,'belief',WH,800,72,'center')+sub(500,610,'(it’s possible)',WH,30)
b+=w(500,860,'reality shift',BL,800,64,'center')
b+=w(220,1140,'identity',WH,800,66,'center')+sub(220,1216,'(i am her)',WH,30)+w(780,1140,'action',WH,800,66,'center')+sub(780,1216,'(i participate)',WH,30)
pin('G04','reality creation map',RD,WH,svg(g,BL,12)+b+SP(780,560,BL,80))
# G05 · versions of you · blush bg, pink arrows, top step text-pink
st=[(1190,'current you','(the starting point)'),(950,'aligned you','(making it real)'),(710,'evolving you','(in process)'),(470,'expanded you','(what’s next)')]
b=TL('the versions of you',INK); g=''
for i,(y,a,c) in enumerate(st):
    x=80+i*70
    b+=w(x,y,a,TP if i==3 else INK,800,58)+sub(x,y+64,c,INK,30,'left')
    if i<3: g+=arr(x+60,y-14,x+40,y-90,x+110,st[i+1][0]+120)
pin('G05','versions of you',LI,INK,svg(g,PK,12)+b,photo='pinkgloss',pos='50% 30%',box=(640,700,300,430))
# G06 · adaptive loop · black, pink arrows
b=loop4([('create','(a plan / experiment)'),('test','(in real life)'),('learn','(what works)'),('evolve','(adjust / level up)')],WH,'the adaptive<br>loop',acc_word=PK)
pin('G06','adaptive loop',INK,WH,svg(ARW,PK,14)+b+SP(470,560,BL,90))
# G07 · reality triangle · cream, pink arrows, text-pink centre line
g=arr(400,560,250,700,190,880)+arr(250,1180,500,1260,750,1180)+arr(810,880,750,700,600,560)
b=w(500,430,'imagination',INK,800,66,'center')+sub(500,502,'(create the vision)',INK,30)
b+=w(170,1060,'identity',INK,800,62,'center')+sub(170,1132,'(become her)',INK,30)+w(830,1060,'action',INK,800,62,'center')+sub(830,1132,'(participate)',INK,30)
b+=w(500,1290,'reality creation',TP,700,44,'center','font-style:italic')+TL('the reality triangle',INK,230)
pin('G07','reality triangle',PP,INK,svg(g,PK,12)+b,photo='blue',pos='50% 25%',box=(405,690,190,280))
# G08 · expansion cycle · hot pink bg, white infinity, black words
g='<path d="M500 760 C 400 600, 140 600, 140 760 C 140 920, 400 920, 500 760 C 600 600, 860 600, 860 760 C 860 920, 600 920, 500 760"/>'+head(330,640,250,625)+head(670,880,750,895)
b=TL('the expansion cycle',INK)+w(300,500,'experience',INK,800,60,'center')+sub(300,568,'(live)',INK,30)+w(700,500,'evolve',INK,800,60,'center')+sub(700,568,'(expand)',INK,30)
bx=''
for i,t in enumerate(['try','learn','adapt','level up','repeat']):
    y=1000+i*74; bx+=f'<rect x="380" y="{y-4}" width="44" height="44" rx="10" fill="#fff" stroke="{INK}" stroke-width="5"/>'; b+=w(450,y-8,t,INK,800,46)
pin('G08','expansion cycle',PK,INK,svg(g,WH,14)+f'<svg viewBox="0 0 1000 1500" style="position:absolute;inset:0">{bx}</svg>'+b+SP(830,400,WH,70))
# G09 · self-concept → reality · white, red arrows, red key words (matches the red photo)
g=arr(230,640,250,780,350,800)+arr(770,640,750,780,650,800)
b=TL('self-concept → <span style="color:'+RD+'">reality</span>',INK)+w(230,470,'how you<br>see yourself',INK,800,46,'center')+sub(230,580,'(identity)',INK,30)+w(770,500,'how you act',INK,800,46,'center')+sub(770,560,'(behavior)',INK,30)
b+=w(500,1110,'how you live',RD,800,64,'center')+sub(500,1184,'(reality)',INK,30)+w(500,1290,'self-concept → decisions → outcomes',INK,500,36,'center','font-style:italic')
pin('G09','self-concept to reality','#fff',INK,svg(g,RD,12)+b,photo='red',pos='50% 25%',box=(380,640,240,420))
# G10 · reality upgrade · black, pink arrow, expansion in pink
g=arr(60,1340,880,1330,950,600)
st=[(60,1180,'clarity','(know what)'),(250,1010,'capacity','(become who)'),(430,840,'consistency','(do the work)'),(600,670,'expansion','(sustain &amp; grow)')]
b=''.join(w(x,y,a,PK if a=='expansion' else WH,800,58)+w(x,y+64,c,WH,500,30,extra='font-style:italic') for x,y,a,c in st)
b+=w(50,250,'the reality<br><span style="color:'+PK+'">upgrade</span>',WH,800,74,'center',width=900)
pin('G10','reality upgrade',INK,WH,svg(g,PK,12)+b+SP(820,420,BL,90))
# G11 · new way of manifestation · blush... white? -> cream bg, pink arrows, photo
b=loop4([('imagine','(create)'),('participate','(act)'),('adapt','(learn)'),('evolve','(expand)')],INK,'',acc_word=TP)
b=b.replace(w(500,860,'',INK,500,40,'center','font-style:italic'),'')
b+=f'<img class="f" src="{s("sky")}" style="left:360px;top:520px;width:280px;height:400px;object-position:50% 25%" {A}>'+w(500,950,'a continuous<br>creation system',INK,500,34,'center','font-style:italic')
pin('G11','new way of manifestation',LI,INK,svg(ARW,PK,14)+b)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
