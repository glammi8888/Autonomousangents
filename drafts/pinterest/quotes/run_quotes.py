import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
Q=[
 (["2027","I AM","BECOMING","ME"],"same girl, bigger dreams"),
 (["I'M IN MY","BUILDING","ERA"],"one small action. then rest"),
 (["YOUR FUTURE","IS NOT A","SPECTATOR","SPORT"],"you're the visionary"),
 (["A SOFT VOICE","A RADICAL","MIND"],"the new way of manifestation"),
 (["BECOME","YOUR OWN","DREAM GIRL"],"it's giving future you"),
 (["YOU CAN BE","MANIFESTING","SOMETHING","LONG BEFORE","YOU POSSESS IT"],"one line is enough"),
 (["ART DIRECT","YOUR LIFE"],"you're the cover star"),
 (["IT'S NOT","TOO LATE"],"i let today be enough"),
]
import os
OUTD="/home/user/Autonomousangents/drafts/pinterest/quotes/"
for i,(l,sub) in enumerate(Q,1):
    make_quote(l,sub,f"ISSUE11 · NOTE TO SELF · {i:02d} / 11",OUTD+f"quote-{i:02d}.jpg")
print(len(Q))
