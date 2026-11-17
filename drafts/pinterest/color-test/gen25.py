# CT218–CT224 (Nov 17): "Later = Never so act now" in Megan's picked styles. Megan: "especially in the 110 111 113 114 115 118 125 styles".
import gen9, gen8
from gen import doc
from gen12 import S, T, U
P={}
L='When manifesting<br>later = never<br>so act now'
P['CT218']=doc('Color test 218 · like 110 · letter + send this to yourself',S+""".pin{background:#FBF3EA;color:#2A211A}
.q{position:absolute;left:70px;right:90px;top:340px;font-weight:400;font-size:96px;line-height:1.02;letter-spacing:-.04em}
.k{position:absolute;left:70px;top:1120px;font-weight:600;font-size:18px;letter-spacing:.24em;text-transform:uppercase}""",f"""{T()}<div class="q">When manifesting, later = never so act now. Send this to yourself.</div><div class="k">Save · send · act</div>{U('#2A211A')}""")
P['CT219']=doc('Color test 219 · like 111 · orange + blue italic',S+""".pin{background:#FF6533}
.q{position:absolute;left:60px;right:60px;top:470px;text-align:center;color:#24409A;font-style:italic;font-weight:400;font-size:124px;line-height:1;letter-spacing:-.05em}""",f"""{T()}<div class="q">{L}</div>{U('#24409A')}""")
P['CT220']=doc('Color test 220 · like 113 · stacked lines',S+""".pin{background:#FCECEF;color:#1A1A1A}
.st{position:absolute;left:60px;right:40px;top:220px;font-size:112px;line-height:1.02;letter-spacing:-.05em}
.st i{font-weight:300}.st b{font-weight:800}""",f"""{T()}<div class="st"><i>When manifesting,</i><br><b>Later</b> <i>= never,</i><br><b>Later</b> <i>= never,</i><br><b>Later</b> <i>= never,</i><br><b>so act</b><br><b>now.</b></div>{U('#1A1A1A')}""")
P['CT221']=doc('Color test 221 · like 114 · pink centred quote',S+""".pin{background:#FCD4DA}
.q{position:absolute;left:110px;right:110px;top:480px;text-align:center;color:#2A0F18;font-weight:700;font-size:96px;line-height:1.35;letter-spacing:-.02em}""",f"""{T()}<div class="q">{L}</div>{U('#2A0F18')}""")
P['CT222']=doc('Color test 222 · like 115 · spaced words',S+""".pin{background:#fff}
.q{position:absolute;left:70px;right:70px;top:480px;color:#111;font-weight:400;font-size:100px;line-height:1.08;letter-spacing:-.03em;text-align:justify;text-align-last:justify;word-spacing:.2em}""",f"""{T()}<div class="q">when manifesting<br>later = never<br>so act now</div>{U('#111')}""")
rep=''.join('<div>When manifesting later = Never so act now.</div>' for _ in range(7))+'<div class="hi">When manifesting later = Never so act now.</div>'+''.join('<div>When manifesting later = Never so act now.</div>' for _ in range(7))
P['CT223']=doc('Color test 223 · like 118 · repeated line',S+""".pin{background:#FEFBF4}
.rep{position:absolute;left:90px;top:225px;color:#6A625A;font-weight:300;font-size:44px;line-height:1.28;letter-spacing:-.02em}
.rep .hi{color:#C2207E;font-weight:700}""",f"""{T()}<div class="rep">{rep}</div>{U('#6A625A')}""")
P['CT224']=doc('Color test 224 · like 125 · aura gradient',S+""".pin{background:radial-gradient(circle at 50% 52%,#FFE2C2 0%,#FFC7A8 18%,#F7A38C 38%,#E9877A 60%,#C9686A 100%)}
.q{position:absolute;left:150px;right:150px;top:700px;text-align:center;color:#3A1815;font-weight:400;font-size:52px;letter-spacing:-.01em;line-height:1.2}""",f"""{T()}<div class="q">when manifesting<br>later = never so act now</div>{U('#3A1815')}""")
P['CT225']=doc('Color test 225 · like 137 · big pink spaced text',S+""".pin{background:#F7F5F6}
.q{position:absolute;left:80px;right:80px;top:260px;text-align:center;color:#FF6FB5;font-weight:300;font-size:128px;line-height:1.28;letter-spacing:.01em}""",f"""{T()}<div class="q"><span style="font-size:76px">when manifesting</span><br>later<br>=<br>never<br>so act now</div>{U('#C2207E')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
