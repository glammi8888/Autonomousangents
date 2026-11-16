# Covers round (CT64–CT67), Nov 16: Megan "ohhh the magazine covers are amazing". Same cover format as CT51–CT53, new Drive photos.
import gen4
gen4.B.update({'shoulder':'68963da8e26c9286d2fba8b5c3edb3bb','sleepcash':'62bbca5a42743009b5377360d4ed86d7','earring':'860f329959c42e11a32a5dcb35db8203','wethair':'a5d556e3904ad3660587c191ff3898c6'})
from gen5 import cover
P={}
P['CT64']=cover('CT64','shoulder','100% 20%','Self love','#FF8FB1','I love my hot bod',[('60','self love affirmations'),('8','glow up checklist steps'),('9','ways to stop overthinking')],'linear-gradient(180deg,rgba(0,0,0,0) 48%,rgba(60,25,15,.75) 100%)',date=False)
P['CT65']=cover('CT65','sleepcash','40% 30%','Sleep','#9DF2C8',"I'm making money in my sleep",[('40','money affirmations'),('9','ways to stop overthinking'),('120','words of the year')],'linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 50%,rgba(5,30,15,.75) 100%)')
P['CT66']=cover('CT66','earring','50% 20%','Business','#F3D9A4','My business is bringing sooooo much money',[('40','money affirmations'),('120','words of the year'),('60','self love affirmations')],'linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(20,14,6,.7) 100%)',date=False)
P['CT67']=cover('CT67','wethair','50% 25%','Worthy','#B9A2FF','I am worthy of love, respect, and everything I desire',[('60','self love affirmations'),('40','new year journal prompts'),('8','glow up checklist steps')],'linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(25,15,40,.88) 100%)')
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
