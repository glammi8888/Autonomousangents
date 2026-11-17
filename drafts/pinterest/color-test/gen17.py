# Doll series round 1 (CT149–CT162), Nov 17. Megan's AI doll photos (Drive, "glammi_barbie_doll…") + her 18 viral caption picks (BANK, word for word).
# Megan: "Make sure every facial expression matches with the quote". Keyword: "funny quotes humor". Never "Barbie" on the pin (Mattel trademark).
# Skipped photos: readable Chanel logos, a "PNG" stock watermark, a Google Lens screenshot icon, cigarettes.
import gen9, gen8, gen13
from gen import doc, LOGO
from gen13 import S, A
D={'b01':'664d8387c676702cb5a15943ef0b7d10','b02':'911861befb1c376b5f6056218d090277','b03':'19a1c64e03796c962e2254a7da9e19eb','b04':'3ff6f7314e4ea254936e23072d93b81d','b05':'ac522a12f3d1282f26baad8eeaa5b423','b06':'03675ff91760e5ac37d6db3ed67ff8b0','b07':'6deebe525e257a8e87c6983eb6e7e9a5','b08':'77dfa097898e0f171145dbd128cfde65','b09':'f83e2683cf569ebed8b9dc9f5a0f3a4c','b10':'cda49a9bed2fee480707205f1f8b9657','b11':'9133bd21c0c7d450c6b0cee835de9186','b12':'cd3d36c640dc5e010d8a04eebab0200d','b13':'7a3aba3d4df516025cc7bfe31ed4fa09','b14':'2fd6cd5538605728a6e040cccbbfdedb'}
def s(k): return f'/_blob/{D[k]}'
T=lambda w='': f'<img class="tl {w}" src="{LOGO}" alt="ISSUE11">'
U=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
SH='<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.28) 0%,rgba(0,0,0,0) 16%,rgba(0,0,0,0) 58%,rgba(0,0,0,.72) 92%)"></div>'
P={}
# A · meme: pink caption band on top + photo (top viral "barbie quotes" format)
def meme(n,k,cap,pos='50% 30%',fs=50,band='#F9C9DC'):
    P[n]=doc(f'Color test {n[2:]} · doll meme · {cap[:40]}',S+f"""
.pin{{background:{band};color:#141414}}
.tl{{top:34px;height:62px}}
.cap{{position:absolute;left:60px;right:60px;top:120px;height:290px;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:600;font-size:{fs}px;line-height:1.18;letter-spacing:-.02em;text-wrap:balance}}
img.ph{{position:absolute;left:0;top:430px;width:100%;height:1070px;object-fit:cover;object-position:{pos}}}
""",f"""{T()}<div class="cap">{cap}</div><img class="ph" src="{s(k)}" {A}><div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.55))"></div>{U('#fff')}""")
# B · quote over full-bleed photo (CT139 style, text kept off the face)
def quote(n,k,lines,top=1080,fs=76,pos='50% 30%',col='#fff'):
    P[n]=doc(f'Color test {n[2:]} · doll quote · {lines[0][:40]}',S+f"""
.pin{{background:#222}}
.q{{position:absolute;left:60px;right:60px;top:{top}px;text-align:center;color:{col};font-weight:800;font-size:{fs}px;letter-spacing:-.04em;line-height:1.02;text-shadow:0 4px 24px rgba(0,0,0,.6);text-wrap:balance}}
""",f"""<img class="f full" src="{s(k)}" style="object-position:{pos}" {A}>{SH}{T('w')}<div class="q">{'<br>'.join(lines)}</div>{U('#fff')}""")
meme('CT149','b04',"My toxic trait is knowing the truth before I ask because I wanna see how good you lie",fs=46)          # suspicious squint
meme('CT150','b01',"i swear i'm such a sweet girl but y'all be testing my patience all the time",pos='50% 20%')             # eye-roll
meme('CT151','b03','me fighting the urge to say "move bitch" to the slow walkers in front of me',pos='50% 35%')             # furious scowl
meme('CT152','b02',"Me when someone is better than me at the only thing I'm good at",pos='50% 30%')                       # disgusted side-eye
meme('CT153','b05','Me when I say something with confidence but it was wrong',pos='50% 35%')                               # sulky pout, room on fire
meme('CT154','b06',"YOU DON'T HAVE TO BE EVERYONE'S CUP OF TEA. BE GASOLINE. SET THAT SHIT ON FIRE.",pos='50% 35%',fs=48,band='#FFD7C2')  # glare + fire
meme('CT155','b07','I am both dumber and smarter than you think. do not estimate me',pos='50% 15%',band='#F3E6DA')         # blank regal stare
quote('CT156','b08',['I am healthy','I am wealthy','I am rich','I am that bitch'],top=1060,fs=74)                           # tongue out, sparkles
meme('CT157','b09','Me after saying "who would I even tell?" Knowing exactly who I\'m gonna tell',pos='50% 25%',fs=48)     # laughing with champagne
quote('CT158','b10',['I love being me.','it pisses off all the right people'],top=1130,fs=66)                              # smug grin, pink glasses
quote('CT159','b11',['if u lock in like a delusional psychopath','u can actually get what u want sooner'],top=1150,fs=54)   # manic open mouth
quote('CT160','b12',['Chin up princess','or the crown slips'],top=1120,fs=80,pos='50% 20%')                                 # head tilted back
quote('CT161','b13',['Hating me only','boosts my ego'],top=1130,fs=84)                                                     # unbothered, adjusting glasses
quote('CT162','b14',["Me, weird?","Bitch, I'm limited edition."],top=1150,fs=74,pos='50% 20%')                             # hand on hip, black gown
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
