# "Which The Body girl are you?" carousel (TBC1-1..5), Nov 20. Megan: "you can also use their characters ... for carousels and apply their philosophy or characteristics into content".
# Character traits from cast guides (Marie Claire, DMTalkies, Nov 2026). Show stills/actors' faces NOT used (Netflix copyright + actors' likeness on a commercial pin): our library photos in the show's dark academia grade.
# Lines = BANK.md word for word. Audience: Gen Z + millennials (Megan, Nov 20). No "becoming her".
import gen9, gen8, gen13
from gen4 import B
from gen import doc, LOGO
from gen11 import S, T, U, s
from thebody_gen import GRADE, GRAIN, FONTS, BL
A='alt="Editorial photo (AI-generated)"'
P={}
N=lambda i: f'<div style="position:absolute;right:60px;top:64px;font-weight:700;font-size:24px;letter-spacing:.16em;color:#f3e6dc;z-index:6">{i} / 5</div>'
CSS=""".pin{background:#1a0f0c}
.nm{position:absolute;left:60px;right:60px;text-align:center;color:#ff9ccf;font-family:'UnifrakturMaguntia',serif;line-height:1;text-shadow:0 3px 18px rgba(0,0,0,.7)}
.t{position:absolute;left:80px;right:80px;text-align:center;color:#f3e6dc;font-weight:600;font-size:36px;line-height:1.3;text-shadow:0 2px 12px rgba(0,0,0,.85)}
.t i{font-weight:400}
.q{position:absolute;left:80px;right:80px;text-align:center;color:#fff;font-weight:800;font-size:46px;line-height:1.15;letter-spacing:-.02em;text-shadow:0 2px 14px rgba(0,0,0,.85)}
.mv{position:absolute;left:80px;right:80px;text-align:center;color:#ff9ccf;font-weight:700;font-size:32px;text-shadow:0 2px 10px rgba(0,0,0,.85)}"""
def slide(k,i,photo,pos,body):
    P[k]=doc(f'The Body carousel · slide {i}',S+CSS,f'<img class="f full" src="{s(photo)}" style="object-position:{pos};{GRADE}" {A}>{GRAIN}{T("w")}{N(i)}{body}{U("#f3e6dc")}').replace('family=Inter+Tight',FONTS,1)
slide('TBC1-1',1,'bighair','50% 30%','<div class="nm" style="top:820px;font-size:118px">which the body girl are you?</div><div class="t" style="top:1130px">manifestation edition ♱ save this</div>')
def char(k,i,photo,name,who,principle,line,move,fs=46):
    slide(k,i,photo,'50% 25%',f'<div class="nm" style="top:800px;font-size:112px">{name}</div><div class="t" style="top:940px"><i>{who}</i><br>{principle}</div><div class="q" style="top:1090px;font-size:{fs}px">“{line}”</div><div class="mv" style="top:1320px">{move}</div>')
char('TBC1-2',2,'curls','Lisbeth energy','smart. a little weird. starting over.','reinvent yourself, then act first.',"Me, weird? Bitch, I'm limited edition.",'this week: one thing before you feel ready')
char('TBC1-3',3,'wethair','Anya energy','the captain hiding who she really is.','stop performing for status.',"I am no longer proving my worth to someone. You either value me or you're OUT!",'this week: say no to one thing you do for approval',40)
char('TBC1-4',4,'hair','Elise energy','loyal. ride or die.','be real and your people find you.','The right people, places, and moments find me','this week: text the friend who gets you')
char('TBC1-5',5,'earring','Grace energy','the new girl everyone talks about.','main character, quietly.','I am iconic','this week: walk in like you belong',60)
for k,v in P.items(): open(f'{k}.dc.html','w').write(v); open(f'../carousels/{k}.dc.html','w').write(v)
print(len(P))
