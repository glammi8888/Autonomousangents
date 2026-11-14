import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
Q=[
 (["2027.","I am","becoming me."],"Same girl, bigger dreams."),
 (["I’m in my","building era."],"One small action. Then rest."),
 (["Your future","is not a","spectator sport."],"You’re the visionary."),
 (["A soft voice.","A radical mind."],"The new way of manifestation."),
 (["Become your","own dream girl."],"It’s giving future you."),
 (["You can be","manifesting","something long","before you","possess it."],"One line is enough."),
 (["Art direct","your life."],"You’re the cover star."),
 (["It’s not","too late."],"I let today be enough."),
]
import os
OUTD="/home/user/Autonomousangents/drafts/pinterest/quotes/"
for i,(l,sub) in enumerate(Q,1):
    make_quote(l,sub,f"ISSUE11 · NOTE TO SELF · {i:02d} / 11",OUTD+f"quote-{i:02d}.jpg")
print(len(Q))
