# Shopping series (CT185–CT190), Nov 17. Megan's fur-coat shopping photos (pasted in chat; every Dior/Chanel logo cropped out) + her lines (BANK, word for word). Style = her liked quote over full-bleed photo (156/158/160–162).
import gen9, gen8, gen13
from gen import doc, LOGO
from gen13 import S, A
# Megan, Nov 17: "the logos don't need to be cropped out" -> full photos, bags + logos visible; text sits on the coat between face and bags.
D={'s1':'0bc23b41da2e3dfdeb2d5e202cf73263','s2':'1bbdd0bf5cdc7f980f3968816cf5962b','s3':'cb42026166e754aa61015533d682c479','s4':'187c62db4887a4edac6fed1a8aaf04ee','s5':'e497cf9d0ab5de779ac0933248b44fb7'}
T=lambda: f'<img class="tl w" src="{LOGO}" alt="ISSUE11">'
SH='<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 14%,rgba(0,0,0,0) 40%,rgba(0,0,0,.45) 55%,rgba(0,0,0,.45) 66%,rgba(0,0,0,0) 80%,rgba(0,0,0,0) 90%,rgba(0,0,0,.45) 100%)"></div>'
P={}
def q(n,k,lines,top=770,fs=84,it=None):
    P[n]=doc(f'Color test {n[2:]} · shopping · {lines[0][:36]}',S+f""".q{{position:absolute;left:60px;right:60px;top:{top}px;text-align:center;color:#fff;font-weight:800;font-size:{fs}px;letter-spacing:-.04em;line-height:1.02;text-shadow:0 4px 24px rgba(0,0,0,.55);text-wrap:balance}}
.q i{{font-weight:300}}""",f"""<img class="f full" src="/_blob/{D[k]}" style="object-position:50% 50%" {A}>{SH}{T()}<div class="q">{'<br>'.join(lines)}</div><div class="url" style="color:#fff">issue11.app</div>""")
q('CT185','s1',['I can afford','<i>anything</i>'],top=770,fs=104)                                  # arms full of bags, level stare
q('CT186','s2',['I can give myself','<i>the soft life</i>'],top=770,fs=96)                         # pink fur, sunshine, sunglasses
q('CT187','s3',['Nothing feels better','than having money'],top=770,fs=88)                         # holding her coat open, night street
q('CT188','s4',['Unlimited shopping budget','for meeee babyyyy'],top=770,fs=80)                    # white fur, bags in hand, pout
q('CT189','s5',['I deserve','<i>luxury</i>'],top=770,fs=110)                                       # camel fur against the car
q('CT190','s1',['I am healthy, I am wealthy,','I am rich, I am that bitch'],top=770,fs=72)          # Megan sent it again for this series
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
