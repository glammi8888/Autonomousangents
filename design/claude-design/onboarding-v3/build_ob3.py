import html
E=html.escape
N=32
def top(i):
    return f'<div class="bar"><i style="width:{i/N*100:.0f}%"></i></div><div class="tl"><span>ISSUE11</span><span>{"SKIP" if i>3 else ""}</span></div>'
def h(t): return f'<div class="h">{t}</div>'
def sub(t): return f'<div class="sub">{t}</div>'
def opts(items,sel=()):
    return '<div class="opts">'+''.join(f'<div class="opt{" on" if k in sel else ""}">{E(t)}<b></b></div>' for k,t in enumerate(items))+'</div>'
def chips(items,sel=()):
    return '<div class="chips">'+''.join(f'<span class="chip{" on" if t in sel else ""}">{E(t)}</span>' for t in items)+'</div>'
def field(ph,mic=False):
    return f'<div class="field">{E(ph)}{"<span class=mic></span>" if mic else ""}</div>'
def btn(t="CONTINUE",ghost=None):
    g=f'<div class="ghost">{E(ghost)}</div>' if ghost else ''
    return f'<div class="foot">{g}<div class="btn">{E(t)}</div></div>'
def stmt(t,small=""):
    return f'<div class="stmt"><div class="sh">{t}</div>{f"<div class=sub>{small}</div>" if small else ""}</div>'
def cover(name="MEGAN",line="HOW MEGAN BUILT A LIFE BY THE SEA",style="red",small=False):
    return f'<div class="cover {style}{" sm" if small else ""}"><div class="mast">ISSUE11</div><div class="cd">MARCH 2027 ISSUE</div><div class="cn">{name}</div><div class="cl">{line}</div></div>'
S=[]
def add(part,title,body,cap,src): S.append((part,title,body,cap,src))
P1,P2,P3,P4,P5="Hello","Desire","The pain, then the answer","Build her Issue","Reveal, then pay"
add(P1,"Welcome",h("TURN YOUR DREAMS INTO YOUR OWN MAGAZINE.")+sub("And become the woman who makes them real. About 3 minutes.")+'<div class="q">Where are you with manifesting?</div>'+opts(["Just curious","Tried it, nothing changed yet","Sometimes","It's part of my life"]),"The USP in one line, then an easy question. (Megan, Oct 7)","Headway · HeyCatch")
add(P1,"Name",h("WHAT SHOULD WE CALL OUR COVER STAR?")+field("Megan")+sub("It goes on the cover of your Issue.")+btn(),"Her name is used from here on.","I am · our Q01")
add(P1,"Reward",'<div class="cwrap">'+cover(line="",style="blank")+'<span class="stk">HI MEGAN.</span></div>'+stmt("","Your cover's waiting.")+btn(),"A small reward after the first answer.","Headway reward screen")
add(P1,"Age",h("HOW OLD ARE YOU?")+sub("So your Issue speaks your language.")+opts(["18–24","25–34","35–44","45+"],(1,)),"Easy, one tap. Optional (question for Megan).","I am · Headway")
add(P2,"Topic",h("WHAT'S YOUR FIRST ISSUE ABOUT?")+chips(["Love","Money & freedom","My own thing","A home I love","Glow-up","Peace","Travel","Help me choose"],("My own thing","A home I love"))+btn(),"Sets her cover headline and World.","HeyCatch · our Q03")
add(P2,"Sneak peek",h("THIS IS WHAT A REAL ISSUE LOOKS LIKE.")+'<div class="peek">'+cover(line="HER OWN STUDIO, HER OWN RULES",style="noir",small=True)+'<div class="spread"><div class="ph"></div><div class="ln"></div><div class="ln s"></div></div></div><div class="sess">5 MIN · YOUR MORNING, AS HER</div>'+btn(),"Curiosity, no feature list.","Headway curiosity gap")
add(P2,"Feel",h("HOW DO YOU WANT TO FEEL EVERY DAY?")+chips(["Unbothered","Rich","Chosen","Free","Powerful","Soft","Seen","Calm","Magnetic"],("Unbothered","Free","Magnetic"))+btn(),"Feeds affirmations and Audio.","our Q06")
add(P2,"Inspiration",h("WHOSE LIFE INSPIRES YOUR ISSUE?")+sub("Pick any. Names only.")+chips(["Rihanna","Oprah","Zendaya","Beyoncé","Serena","Someone else"],("Rihanna",))+btn(),"Implied authority, never claimed.","Headway · Sep 24")
add(P2,"Dreamer or doer",h("ARE YOU A DREAMER OR A DOER?")+opts(["A dreamer","A doer"],(0,)),"Labeling: she starts acting like her answer.","Headway · Sep 24")
add(P2,"Reply",stmt("DREAMERS SEE IT FIRST.","Your Issue makes it real.")+btn(),"Changes with her answer.","Headway feedback")
add(P3,"Clear vision?",h("DO YOU HAVE A CLEAR PICTURE OF THE LIFE YOU WANT?")+opts(["Yes","Working on it","One day at a time","Not really"],(1,)),"Gentle start to the pain block.","I am")
yn='<div class="yn"><span>NO</span><span class="on">YES</span></div>'
add(P3,"Pain card 1",'<div class="card">"I start strong… then stop after a few days."</div><div class="q c">Does this sound like you?</div>'+yn,"Reply: “Most people do. That's why your Issue meets you every day.” (pain 1)","Megan's pain points · Headway")
add(P3,"Pain card 2",'<div class="card">"I make vision boards or write goals… then forget them."</div><div class="q c">Does this sound like you?</div>'+yn,"Reply: “A board you forget isn't a vision. An Issue you open every day is.” (pain 6)","Megan's pain points · HeyCatch")
add(P3,"Pain card 3",'<div class="card">"Some manifestation content makes me feel delusional."</div><div class="q c">Does this sound like you?</div>'+yn,"Reply: “Fair. No ‘I'm a millionaire’ here. We rehearse becoming her.” (pain 5)","Megan's pain points")
add(P3,"What gets in the way",h("WHAT SOUNDS MOST LIKE YOU?")+opts(["I don't know what to actually do","I'm too focused on when it'll happen","Generic affirmations don't feel like me","I can't tell if I'm progressing","I watch content instead of changing"],(1,2))+btn(),"Pains 2, 4, 7, 8, 9. Lucky Star will know this (real context).","Megan's pain points")
add(P3,"Mirror",stmt("YOU KNOW THE LIFE YOU WANT.","The hard part is becoming her. That's what ISSUE11 is for.")+btn(),"The core pain (10), as a calm breather.","Megan's pain points · I am rhythm")
add(P3,"How it works",h("DON'T JUST VISUALIZE THE OUTCOME. REHEARSE BECOMING HER.")+'<div class="steps"><div><b>YOUR ISSUE</b>makes it visible</div><div><b>AUDIO</b>rehearses your days as her</div><div><b>ONE MOVE A WEEK</b>makes it real</div><div><b>PROOF</b>shows it’s happening</div></div>'+btn(),"Megan's philosophy line. Loop stays invisible.","our 02b")
tiles=''.join(f'<i class="t t{k}{" on" if k in (0,2,4) else ""}"></i>' for k in range(9))
add(P4,"What feels like her",h("PICK WHAT FEELS LIKE HER.")+f'<div class="tiles">{tiles}</div>'+btn(),"Picks fill Your World (Megan's images).","I am themes · our Q04")
add(P4,"Pick your cover",h("PICK YOUR COVER.")+'<div class="covers">'+cover(line="",style="red",small=True)+cover(line="",style="noir",small=True)+cover(line="",style="photo",small=True)+'</div>'+btn(),"Megan's 3 cover styles from Claude Design.","I am theme pick · HeyCatch")
add(P4,"Dream sentence",h("DESCRIBE YOUR DREAM LIFE IN ONE SENTENCE.")+field("I run my own studio by the sea…",mic=True)+sub("This becomes your cover story.")+btn(),"The one effortful input. Mic = iOS dictation.","I am · HeyCatch")
add(P4,"First proof",h("NAME ONE THING YOU ALREADY MADE HAPPEN.")+field("I moved cities on my own.")+sub("Your first proof. It opens your Issue.")+btn(),"Skip allowed.","our Q08")
add(P4,"Practice",h("HOW DO YOU WANT TO PRACTICE?")+opts(["Listen","Watch","Both"],(2,))+'<div class="q">How long?</div>'+chips(["5 min","10 min","15 min"],("5 min",))+btn(),"Sets her Audio.","I am · our Q05")
add(P4,"First move",h("ONE SMALL STEP THIS WEEK?")+field("Book a viewing for a place by the sea.")+sub("This becomes your first move.")+btn(),"Seeds the weekly Next Move.","our Q09")
days=''.join(f'<span class="d{" on" if k==0 else ""}"><em>{d}</em><b></b></span>' for k,d in enumerate(["WE","TH","FR","SA","SU","MO","TU"]))
add(P4,"Day 1",'<div class="big1">1</div>'+stmt("YOUR ISSUE STARTS TODAY.")+f'<div class="week">{days}</div>'+btn(),"She's on day 1 before she's in the app.","I am")
icons=''.join(f'<i class="ic ic{k}{" on" if k==0 else ""}">11</i>' for k in range(6))
add(P4,"Pick your icon",h("PICK YOUR ICON.")+sub("It sits on your Home Screen.")+f'<div class="icons">{icons}</div>'+btn(),"Megan's icon picker (07).","I am")
add(P4,"Notifications",h("YOUR ISSUE, THROUGHOUT THE DAY.")+'<div class="notif"><span class="ni">11</span><div><b>ISSUE11</b><br>I’m the woman who shares her work.</div></div><div class="rows"><div>How many <span>3×</span></div><div>From <span>8:00</span></div><div>To <span>21:00</span></div></div>'+btn("ALLOW"),"Live preview, then the iOS prompt.","I am · HeyCatch")
add(P4,"Meet Lucky Star",'<div class="ls"><span>11</span></div>'+h("MEET LUCKY STAR ★")+sub("Your AI guide. It helps you build your Issue and decide what’s next. Nothing changes unless you keep it.")+btn("SOUNDS GOOD"),"The one place we say “AI”, plainly. Consent.","our 09b")
add(P5,"Printing",h("PRINTING YOUR FIRST ISSUE…")+'<div class="check"><div class="ok">Writing your headlines</div><div class="ok">Designing your cover</div><div class="run">Composing your soundtrack</div><div>Binding your issue</div></div><div class="mini">Want to hear your vision read aloud?<span>YES</span><span>LATER</span></div><div class="rev">“Real beta review goes here.”</div>',"Never an empty loader.","Headway · HeyCatch")
add(P5,"The Reveal",'<div class="mono c">MEGAN, YOUR FIRST ISSUE IS READY.</div>'+cover()+btn("OPEN MY ISSUE","Share"),"Her cover, her style, her words.","HeyCatch")
add(P5,"Your future",h("YOUR ISSUE STARTS NOW.")+'<div class="tline"><div><b>TODAY</b>Your first Issue</div><div><b>THIS WEEK</b>Book a viewing by the sea</div><div><b>SOON</b>Your first proof</div></div>'+sub("No promises. A practice.")+btn(),"Her timeline. No outcome guarantees.","Headway “your future”")
add(P5,"Save your Issue",h("SAVE YOUR ISSUE.")+cover(line="",small=True,style="red")+'<div class="foot"><div class="btn">  SIGN IN WITH APPLE</div><div class="ghost">Use email instead</div></div>',"Account after value.","HeyCatch")
add(P5,"Paywall",'<div class="btn top">START MY ISSUE</div>'+h("KEEP YOUR ISSUE ALIVE.")+'<div class="ben"><div>Your dreams as a magazine you open every day</div><div>Audio that rehearses becoming her, made from your words</div><div>One small move a week, no pressure</div><div>Proof you’re becoming her</div></div><div class="price">PRICE TBD · intro offer TBD</div><div class="mono c">Cancel anytime · Restore · Terms · Privacy</div>',"Buy first, then benefits, reviews, FAQ. Prices = Megan + Revenue.","Headway · I am")

parts=[P1,P2,P3,P4,P5]
secs=[]
n=0
for p in parts:
    cards=[]
    for (pp,t,b,c,s) in S:
        if pp!=p: continue
        n+=1
        cards.append(f'<figure class="cell"><div class="phone">{top(n)}<div class="scr">{b}</div></div><figcaption><span class="num">{n:02d}</span><strong>{E(t)}</strong><span class="cap">{E(c)}</span><span class="src">From {E(s)}</span></figcaption></figure>')
    cnt=len(cards)
    secs.append(f'<section><header class="ph-h"><h2>{E(p)}</h2><span>{cnt} screens</span></header><div class="grid">{"".join(cards)}</div></section>')
css=open('ob3.css').read()
out=f'''<title>ISSUE11 Onboarding v3</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo+Narrow:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{css}</style>
<main>
<header class="top"><div class="eyebrow">ISSUE11 · DESIGN ROOM · DRAFT FOR MEGAN</div><h1>Onboarding v3</h1>
<p>32 screens. Every answer builds her magazine, so the Reveal shows <em>her</em> Issue. Megan’s pain points, Headway’s structure, I am’s calm rhythm. <em>Don’t just visualize the outcome. Rehearse becoming her.</em></p>
<div class="flow"><span>Hello</span><span>Desire</span><span>The pain, then the answer</span><span>Build her Issue</span><span>Reveal, then pay</span></div></header>
{"".join(secs)}
<footer class="note">Draft · not built into the app yet · prices, trial and discounts are decided by Megan + Revenue · social proof only from real data.</footer>
</main>'''
open('index.html','w').write(out)
print(n)
