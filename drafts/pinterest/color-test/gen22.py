# Favourites variations · batch 1 (CT201–CT210), Nov 17. Megan: "now you can simply reproduce and create varieties of the ones we have approved". Approved layouts only, new photo + BANK line pairs.
import gen9, gen8, gen13
from gen4 import B
import gen18, gen17
from gen18 import f42, f45, f95, f122, fang, P as P18
from gen17 import quote, P as P17
from gen5 import cover
P18.clear(); P17.clear()
G=lambda c:f'linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 50%,{c} 100%)'
M=[('40','money affirmations'),('8','glow up checklist steps'),('60','self love affirmations')]
O=[('60','self love affirmations'),('9','ways to stop overthinking'),('24','journaling prompts')]
C={}
C['CT201']=cover('CT201','redhair','50% 20%','Hot','#FFB38A','Hot and Rich all 2027',M,G('rgba(60,10,5,.78)'))
C['CT202']=cover('CT202','pink','50% 20%','Pretty','#FF9EC4','i only get richer and prettier',O,G('rgba(60,15,35,.78)'))
C['CT203']=cover('CT203','bobcash','50% 25%','Lucky','#F3D9A4',"I'm the luckiest girl on the planet",M,G('rgba(25,20,10,.8)'))
f45('CT204','pinkgloss','50% 0%','I am my own <i>dream girl</i>','rgba(110,30,60,.88)',top=1160)
f42('CT205','#E9E2FF','blueclose','50% 30%','My nervous system is calm')
f122('CT206','flying','50% 30%','money','I wake up to money','#7CF0A8')
fang('CT207','earring','50% 25%','1111','AWAKENING',"this is not a coincidence. you're close ✨")
quote('CT208','b10',["babe, you're a big deal.","act like it."],top=1130,fs=70)
quote('CT209','b13',['Never let a loser make you','question your worth'],top=1140,fs=62)
f95('CT210','iconic','I am iconic',[('blue','Blue'),('red','Red'),('pinkgloss','Pink'),('orange','Orange')],fs=230)
C.update(P18); C.update(P17)
for k,v in C.items(): open(f'{k}.dc.html','w').write(v)
print(sorted(C))
