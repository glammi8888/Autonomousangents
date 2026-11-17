# Magazine cover batch (CT191–CT200), Nov 17. Megan: "I think we should do magazine cover styles like 87, 86, 51, 52, 64". Approved cover() template from gen5, new photo + BANK line pairs; cover lines = real article counts.
import gen9, gen8, gen13
from gen4 import B
B.update({'s1':'0bc23b41da2e3dfdeb2d5e202cf73263','s2':'1bbdd0bf5cdc7f980f3968816cf5962b','s3':'cb42026166e754aa61015533d682c479','s4':'187c62db4887a4edac6fed1a8aaf04ee','s5':'e497cf9d0ab5de779ac0933248b44fb7','b08':'77dfa097898e0f171145dbd128cfde65'})
from gen5 import cover
G=lambda c:f'linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 50%,{c} 100%)'
M=[('40','money affirmations'),('8','glow up checklist steps'),('60','self love affirmations')]
N=[('50','new year affirmations'),('40','new year journal prompts'),('120','words of the year')]
O=[('60','self love affirmations'),('9','ways to stop overthinking'),('24','journaling prompts')]
P={}
P['CT191']=cover('CT191','s5','50% 30%','Luxury','#F3D9A4','I deserve luxury',M,G('rgba(40,25,10,.78)'))
P['CT192']=cover('CT192','s2','50% 30%','Soft life','#FFC9D6','I can give myself the soft life',O,'linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 40%,rgba(60,30,30,.78) 66%,rgba(60,30,30,.85) 100%)')
P['CT193']=cover('CT193','s1','50% 30%','Afford','#F5C9A0','I can afford anything',M,G('rgba(50,30,15,.78)'))
P['CT194']=cover('CT194','s3','50% 30%','Money','#E8B07A','Nothing feels better than having money',M,G('rgba(20,15,10,.8)'))
P['CT195']=cover('CT195','s4','50% 30%','Shopping','#F3E3C0','Unlimited shopping budget for meeee babyyyy',N,'linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 38%,rgba(15,15,20,.82) 62%,rgba(15,15,20,.9) 100%)')
P['CT196']=cover('CT196','cashface','50% 25%','Rich','#FFD24A','Rich &amp; Stylish 2027',N,G('rgba(30,20,5,.78)'))
P['CT197']=cover('CT197','earring','50% 20%','Spoiled','#FF9EC4','Spoiled by the Universe ⭐',O,G('rgba(40,10,25,.78)'))
P['CT198']=cover('CT198','b08','50% 30%','Wealthy','#FFB3D9','I am healthy I am wealthy I am rich I am that bitch',M,G('rgba(30,40,70,.8)'),date=False)
P['CT199']=cover('CT199','blue','50% 10%','Iconic','#B9CCFF','I am iconic',O,G('rgba(10,25,90,.8)'))
P['CT200']=cover('CT200','hair','45% 15%','Long hair','#F2C9A0','I love my long hair',[('8','glow up checklist steps'),('60','self love affirmations'),('40','new year journal prompts')],G('rgba(20,15,10,.75)'))
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
