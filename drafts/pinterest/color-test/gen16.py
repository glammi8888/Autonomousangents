# CT147 (Nov 16): CT128 vision board redo. Megan: "I do like 128 but the visionboard is cut off so if we can elongate the pin or find a way to make the pictures full format within the pin that would be great". Photos are 3:4, so a 3x3 grid of 3:4 cells fits the 2:3 pin with no cropping.
import gen9, gen8, gen13
from gen import doc
from gen13 import S, T, U, A, s
ks=['hair','cashpile','sky','suit',None,'pinkgloss','flying','earring','bedcash']
cells=''.join(f'<img src="{s(k)}" {A}>' if k else '<div class="tc"><em>Rich &amp; Stylish</em><div>2027</div><span>vision board</span></div>' for k in ks)
P={'CT147':doc('Color test 147 · vision board grid, full photos (128 redo)',S+"""
.pin{background:#F7F2EA}
.tl{top:14px;height:58px}
.g{position:absolute;left:0;right:0;top:84px;display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
.g img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}
.tc{aspect-ratio:3/4;background:#F7F2EA;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#1A1A1A}
.tc div{font-weight:800;font-size:110px;letter-spacing:-.05em;line-height:1}
.tc em{font-style:italic;font-weight:600;font-size:44px;letter-spacing:-.02em;margin-bottom:6px}
.tc span{font-size:34px !important;margin-top:6px;font-style:italic;font-weight:400;font-size:46px;letter-spacing:-.02em}
.url{bottom:22px}
""",f"""{T()}<div class="g">{cells}</div>{U('#1A1A1A')}""")}
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
