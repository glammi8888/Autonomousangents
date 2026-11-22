# CT62 ("$10,000 a month with ease", doing well, Megan Nov 22) remade with new amounts (M15K … M100K).
# Megan: "The $10,000 a month with ease pin is doing well so we redo it with different amounts such as 15,000 20,000 25,000 30,000 40,000 50,000 100,000".
import gen6
from gen6 import doc, S, src, TOP, URL
P={}
for amt in ['15,000','20,000','25,000','30,000','40,000','50,000','100,000']:
    fs=214 if len(amt)<=6 else 188
    k='M'+amt.replace(',000','K')
    P[k]=doc(f'Money amount · ${amt} a month with ease (CT62 style)',S+f"""
.pin{{background:#0E0E0E}}
.ko{{position:absolute;left:0;right:0;top:{410 if fs==214 else 425}px;font-weight:900;font-size:{fs}px;line-height:.85;letter-spacing:-.07em;text-align:center;background:url('KO2') 50% 50%/cover;-webkit-background-clip:text;background-clip:text;color:transparent}}
.big{{position:absolute;left:60px;right:60px;top:760px;text-align:center;color:#D9B3FF;font-weight:900;font-size:100px;line-height:.9;letter-spacing:-.05em;text-transform:uppercase}}
.big i{{font-weight:300}}
""".replace('KO2',src('cashpile')),f"""{TOP('w')}<div class="ko">${amt}</div><div class="big">a month <i>with ease</i></div>{URL('#D9B3FF')}""")
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(list(P))
