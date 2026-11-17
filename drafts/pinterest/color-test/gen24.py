# CT216–CT217 (Nov 17): Megan: "Oh we could do a quote pin that is  Later = Never so act now". Two loved layouts (45 huge type over photo, 138 spaced caps on cream).
import gen9, gen8, gen13
import gen18
from gen18 import f45, P as P18
from gen import doc
from gen13 import S, T, U
P18.clear()
f45('CT216','orange','50% 0%','Later = Never <i>so act now</i>','rgba(120,45,0,.9)',top=1120)
P18['CT217']=doc('Color test 217 · spaced caps on cream · Later = Never',S+""".pin{background:#FAF6EE;color:#1A1A1A}
.q{position:absolute;left:0;right:0;top:470px;text-align:center;font-weight:300;font-size:72px;line-height:1.9;letter-spacing:.3em}
.q b{font-weight:800}""",f"""{T()}<div class="q"><b>LATER</b><br>=<br><b>NEVER</b><br>SO ACT NOW</div>{U('#1A1A1A')}""")
for k,v in P18.items(): open(f'{k}.dc.html','w').write(v)
print(list(P18))
