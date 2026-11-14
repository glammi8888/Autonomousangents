import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-Autonomousangents/c1b1bd34-cf66-56f8-bc34-f80edec64abe/scratchpad")
from quotes_lib import *
Q=[
 (["2027 IS","THE YEAR","I BECOME","ME."],"Future you is already on her way."),
 (["I'M NOT","WAITING","FOR 2027.","I'M PRACTICING","FOR IT."],"One small move today."),
 (["MY FUTURE","SELF","IS TAKING","NOTES."],"Write it like it's already yours."),
 (["SOFT","VOICE.","RADICAL","MIND."],"Become your own dream girl."),
 (["ROMANTICIZE","THE","PRACTICE."],"Not just the outcome."),
 (["I DON'T","NEED TO","SEE IT","TO START IT."],"Participate in your own life."),
 (["DREAM","BOLDLY.","MOVE","DELIBERATELY."],"Your vision, your issue."),
 (["NEW YEAR,","SAME ME,","BETTER","HABITS."],"Your true self is built, not found."),
]
import os
OUTD="/home/user/Autonomousangents/drafts/pinterest/quotes/"
for i,(l,sub) in enumerate(Q,1):
    make_quote(l,sub,f"ISSUE11 · NOTE TO SELF · {i:02d} / 11",OUTD+f"quote-{i:02d}.jpg")
print(len(Q))
