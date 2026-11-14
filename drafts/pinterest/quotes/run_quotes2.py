import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
Q=[
 (["It’s never","too late for","your dreams."],"I let today be enough."),
 (["Become your","own dream girl."],"It’s giving future you."),
 (["Art direct","your life","like a pro."],"You’re the cover star."),
 (["Manifestation","doesn’t mean","instant","gratification."],"The path counts as much as the cover."),
 (["Rebrand","yourself."],"One small action. Then rest."),
 (["Rebrand","your life."],"Same girl, bigger dreams."),
 (["Your 2027","rebrand."],"One line is enough."),
 (["What if you","achieved all","your wildest","goals in 2027?"],"Your future is not a spectator sport."),
 (["ISSUE11","for your","2027 rebrand."],"A magazine by you."),
]
OUTD="/home/user/Autonomousangents/drafts/pinterest/quotes/set2/"
import os; os.makedirs(OUTD,exist_ok=True)
for i,(l,sub) in enumerate(Q,1):
    make_quote(l,sub,f"ISSUE11 · NOTE TO SELF · {i:02d} / 11",OUTD+f"megan-{i:02d}.jpg")
from PIL import Image
s=Image.new('RGB',(5*260+60,2*390+30),(255,255,255))
for i in range(9):
    t=Image.open(OUTD+f'megan-{i+1:02d}.jpg').resize((250,375)); s.paste(t,(10+(i%5)*260,10+(i//5)*390))
s.save(OUTD+'preview-set2.jpg',quality=85)
print(len(Q))
