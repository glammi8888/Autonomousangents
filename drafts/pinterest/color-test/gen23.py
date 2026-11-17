# Phone-notes variations (CT211–CT215), Nov 17. Megan: "the pin format we posted is working so we can use that as well, phone notes / Let's add that in the pin formats".
# Same notes() as the live pins (batch1/generator.py, Pin01/02/06 = the first pins with views). Topics = real Pinterest searches (../viral/2026-11-17-manifest-questions.md); educational lists, no promised results, no specific people.
src=open('../batch1/generator.py').read()
exec(src[src.index('B={'):src.index('# --- Format 2')])
P={
'CT211':("Manifestation tips for beginners · Notes",notes("November 17, 2026 at 22:14","manifestation tips for beginners 🫧",[("start here",["pick ONE thing you want this year","write it like it already happened","see it for 2 min a day (no scrolling)","then do one small thing toward it this week"]),("stop",["waiting for a sign before you take action","checking if it \"worked\" every hour"])],"Manifestation tips for beginners · free kit")),
'CT212':("Scripting manifestation example · Notes",notes("November 17, 2026 at 23:02","scripting example 📝",[("how",["write in past tense, like it's done","be specific: where, who, how it feels","short is fine. 5 lines is enough","do NOT use negative terms"]),("my script",["it's dec 2027 and my mornings are slow","I worked for myself and i'm booked and busy","i can afford anything I want","i saved the money for the solo trip","i feel calm when i check my bank app"])],"Scripting manifestation template · free")),
'CT213':("369 method example · Notes",notes("November 17, 2026 at 07:30","369 method example ✨",[("how it works",["morning: write it 3 times","afternoon: 6 times","night: 9 times","same sentence, present tense, for 21 days"]),("my sentence",["\"i wake up to money\""]),("tip",["pair it with one money action this week"])],"369 method template · free")),
'CT214':("How to manifest money · Notes",notes("November 17, 2026 at 21:40","how to manifest money (realistic) 💸",[("the mindset",["say the number out loud. know your rich af number","\"i make way more money than what i'm able to spend\""]),("the actions",["Open a HYSA account just for future you","raise your rates once this year (or ask for a raise)","invest your money","sell what you don't use so you have room for the *new* to enter your life"])],"Money affirmations + money moves · free")),
'CT215':("Journal prompts for manifesting your dream life · Notes",notes("November 17, 2026 at 22:58","dream life journal prompts 💌",[("tonight",["describe how your day would look like a year from now","what do you keep procrastinating? Later = never so act now","where do I set boundaries to protect myself and my future","what's something you can do now that only takes 20 mins?"])],"Dream life journal prompts · free")),
}
# Megan, Nov 17: "let's remove the white footer at the bottom. and maybe promote the website while keeping the same writing style (as if it was part of the notes)"
import re
PS={'CT211':'i keep my list on issue11.app so i actually see it','CT212':'my script lives on issue11.app 🫧','CT213':'tracking my 21 days on issue11.app','CT214':'my money moves + affirmations are on issue11.app','CT215':'answering these on issue11.app tonight 💌'}
for k,(t,(bg,inner)) in list(P.items()):
    inner=inner[:inner.index('<div style="position:absolute; left:0; right:0; bottom:0')]
    fs=int(re.search(r'padding-left:30px; font-size:(\d+)px',inner).group(1))
    # Megan, Nov 17: "could also just be  issue11.app"
    # Megan, Nov 17: "the issue11.app should be at the bottom of the pin"
    ps=f'<p style="position:absolute; left:64px; bottom:60px; margin:0; font-size:{fs}px; line-height:1.3">issue11.app</p>'
    inner=inner.rstrip()
    assert inner.endswith('</div>')
    P[k]=(t,(bg,inner[:-6]+ps+'</div>'))
for k,(t,(bg,inner)) in P.items(): open(f'{k}.dc.html','w').write(doc(f'Color test {k[2:]} · phone notes · {t}',inner,bg))
print(len(P))
