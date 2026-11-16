# Round 5 (CT41–CT50), Nov 16: Megan's favourite style (huge clean type, roman + italic, logo small on top, issue11.app at the bottom) WITH her Drive photos.
import gen
from gen import doc, LOGO
from gen4 import B
def bg(k,pos): return f'<img class="bg" src="/_blob/{B[k]}" style="object-position:{pos}" alt="Editorial photo (AI-generated)">'
def ph(k,pos,css): return f'<img src="/_blob/{B[k]}" style="position:absolute;object-fit:cover;object-position:{pos};{css}" alt="Editorial photo (AI-generated)">'
TOP=lambda inv='': f'<img class="tl {inv}" src="{LOGO}" alt="ISSUE11">'
URL=lambda c: f'<div class="url" style="color:{c}">issue11.app</div>'
S="""
.tl{position:absolute;left:50%;top:44px;height:76px;transform:translateX(-50%)}
.url{position:absolute;left:0;right:0;bottom:56px;text-align:center;font-weight:700;font-size:28px;letter-spacing:-.01em}
.big{position:absolute;left:44px;right:44px;font-weight:900;letter-spacing:-.055em;line-height:.86}
.big i{font-weight:300;letter-spacing:-.04em}
.shade{position:absolute;inset:0}
"""
P={}
P['CT41']=doc('Color test 41 · black + lilac · photo',S+"""
.pin{background:#0E0E0E}
.big{top:1050px;color:#D9B3FF;font-size:116px;text-transform:uppercase;text-align:center}
.shade{background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 55%,rgba(10,10,10,.92) 75%)}
""",f"""{bg('bobcash','45% 20%')}<div class="shade"></div>
{TOP('w')}<div class="big">I'm making money in my sleep</div>{URL('#D9B3FF')}""")
P['CT42']=doc('Color test 42 · lavender · italic + photo',S+"""
.pin{background:#F1EBFF}
.it{position:absolute;left:0;right:0;top:1050px;text-align:center;font-style:italic;font-weight:400;font-size:64px;letter-spacing:-.03em;color:#111}
""",f"""{ph('curls','55% 30%','left:250px;top:200px;width:500px;height:760px')}
{TOP()}<div class="it">I am my own dream girl</div>{URL('#111')}""")
P['CT43']=doc('Color test 43 · white · roman + italic stack + photo',S+"""
.pin{background:#fff}
.big{top:150px;color:#0E0E0E;font-size:150px}
.tl{left:52px;transform:none}
.url{text-align:left;left:52px}
""",f"""{TOP()}<div class="big">My <i>face card</i> is <i>absolutely</i> lethal</div>
{ph('pink','50% 40%','left:430px;top:860px;width:518px;height:560px')}{URL('#0E0E0E')}""")
P['CT44']=doc('Color test 44 · white · lowercase + photo',S+"""
.pin{background:#fff}
.big{color:#fff;font-size:112px;text-transform:lowercase;text-align:center}
.shade{background:linear-gradient(180deg,rgba(10,30,90,.55) 0%,rgba(10,30,90,0) 30%,rgba(0,0,0,0) 70%,rgba(10,30,90,.6) 100%)}
""",f"""{bg('sky','50% 0%')}<div class="shade"></div>{TOP('w')}<div class="big" style="top:1150px">i wake up to <i>stripe</i> notifications</div>{URL('#fff')}""")
P['CT45']=doc('Color test 45 · full-bleed red · huge type',S+"""
.pin{background:#C8322B}
.shade{background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 62%,rgba(110,10,10,.88) 84%)}
.big{top:1080px;color:#fff;font-size:132px;text-transform:uppercase;text-align:center}
""",f"""{bg('red','50% 22%')}<div class="shade"></div>{TOP('w')}<div class="big">I am the prize, <i>always</i></div>{URL('#fff')}""")
P['CT46']=doc('Color test 46 · full-bleed orange · roman + italic',S+"""
.pin{background:#E2531F}
.shade{background:linear-gradient(180deg,rgba(0,0,0,0) 62%,rgba(150,45,10,.9) 80%)}
.big{top:1150px;color:#FFE7D6;font-size:88px}
""",f"""{bg('orange','45% 10%')}<div class="shade"></div>{TOP()}<div class="big">Get up girl, <i>you got people</i> to prove wrong</div>{URL('#FFE7D6')}""")
P['CT47']=doc('Color test 47 · photo top + lavender · huge type',S+"""
.pin{background:#DCE6F2}
.big{top:1170px;color:#DCE6F2;font-size:104px;text-align:center}
.shade{background:linear-gradient(180deg,rgba(0,0,0,0) 66%,rgba(20,40,80,.9) 82%)}
""",f"""{bg('blue','50% 0%')}<div class="shade"></div>{TOP()}<div class="big">My nervous system is <i>calm</i></div>{URL('#DCE6F2')}""")
P['CT48']=doc('Color test 48 · black + lilac · photo strip',S+"""
.pin{background:#0E0E0E}
.big{top:960px;color:#D9B3FF;font-size:120px;text-transform:uppercase;text-align:center}
.shade{background:linear-gradient(180deg,rgba(0,0,0,.3) 0%,rgba(0,0,0,0) 15%,rgba(0,0,0,0) 50%,rgba(10,10,10,.9) 68%)}
""",f"""{bg('cashpile','50% 25%')}<div class="shade"></div>{TOP('w')}<div class="big">I make $10,000 a month with ease</div>{URL('#D9B3FF')}""")
P['CT49']=doc('Color test 49 · full-bleed champagne · lilac type',S+"""
.pin{background:#1A140C}
.shade{background:linear-gradient(180deg,rgba(20,12,4,.35) 0%,rgba(20,12,4,0) 22%,rgba(20,12,4,0) 60%,rgba(20,12,4,.92) 80%)}
.big{top:1080px;color:#F3D9A4;font-size:96px;text-transform:uppercase;text-align:center}
""",f"""{bg('cashface','50% 35%')}<div class="shade"></div>{TOP('w')}<div class="big">My business is bringing <i>sooooo</i> much money</div>{URL('#F3D9A4')}""")
P['CT50']=doc('Color test 50 · full-bleed hair · white stack',S+"""
.pin{background:#2A2622}
.shade{background:linear-gradient(180deg,rgba(0,0,0,0) 48%,rgba(30,26,22,.9) 76%)}
.big{top:940px;color:#fff;font-size:112px}
""",f"""{bg('hair','50% 18%')}<div class="shade"></div>{TOP('w')}<div class="big">I glowed up so hard <i>now my ex is crying</i></div>{URL('#fff')}""")

def cover(pid,k,pos,mast,mcol,story,lines,shade,date=True):
    ls='<br>'.join(f'<b>{n}</b> {x}' for n,x in lines)
    return doc(f'Color test {pid[2:]} · magazine cover · {mast.lower()}',"""
.pin{background:#222}
.dg{position:absolute;left:36px;right:36px;top:40px;font-weight:900;font-size:150px;line-height:.78;letter-spacing:-.07em;text-transform:uppercase;white-space:nowrap;word-spacing:.12em;text-shadow:0 4px 30px rgba(0,0,0,.3)}
.date{position:absolute;right:44px;top:300px;writing-mode:vertical-rl;color:#fff;font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase}
.story{position:absolute;left:52px;bottom:300px;color:#fff;font-weight:900;font-size:76px;line-height:.92;letter-spacing:-.045em;max-width:640px;text-shadow:0 4px 24px rgba(0,0,0,.35)}
.story i{display:block;font-weight:600;font-size:30px;letter-spacing:.12em;text-transform:uppercase;font-style:normal;margin-bottom:12px;text-shadow:none}
.lines{position:absolute;right:48px;bottom:150px;text-align:right;color:#fff;font-weight:800;font-size:30px;line-height:1.25;text-shadow:0 2px 14px rgba(0,0,0,.45)}
.bar{position:absolute;right:48px;bottom:44px;background:transparent;padding:8px 10px 4px;display:flex;flex-direction:column;align-items:center}
.bar span{font-weight:600;font-size:13px;letter-spacing:.16em;color:#fff;margin-top:2px}
.site{position:absolute;left:0;right:0;bottom:62px;text-align:center;color:#fff;font-weight:600;font-size:19px;letter-spacing:.02em;text-shadow:0 2px 12px rgba(0,0,0,.45)}
.shade{position:absolute;inset:0}
""",f'''{bg(k,pos)}<div class="shade" style="background:{shade}"></div>
<div class="dg" style="color:{mcol}">{mast}</div>{'<div class="date">The 2027 issue</div>' if date else ''}
<div class="story"><i style="color:{mcol}">Cover story</i>{story}</div>
<div class="lines">{ls.replace('<b>',f'<b style="color:{mcol}">')}</div>
<img class="logo w" src="{LOGO}" alt="ISSUE11"><div class="site">issue11.app</div><div class="bar"><svg viewBox="0 0 200 60" width="168" height="50" fill="#fff"><rect x="4.0" y="0" width="3" height="58"/><rect x="10.0" y="0" width="3" height="50"/><rect x="15.0" y="0" width="4.5" height="50"/><rect x="22.5" y="0" width="1.5" height="50"/><rect x="25.5" y="0" width="4.5" height="50"/><rect x="32.0" y="0" width="4.5" height="50"/><rect x="38.0" y="0" width="1.5" height="50"/><rect x="41.5" y="0" width="2" height="50"/><rect x="45.0" y="0" width="1.5" height="50"/><rect x="49.5" y="0" width="1.5" height="50"/><rect x="54.0" y="0" width="3" height="50"/><rect x="59.0" y="0" width="4.5" height="50"/><rect x="66.5" y="0" width="1.5" height="50"/><rect x="71.0" y="0" width="1.5" height="50"/><rect x="75.5" y="0" width="1.5" height="50"/><rect x="78.5" y="0" width="1.5" height="50"/><rect x="81.5" y="0" width="1.5" height="50"/><rect x="86.0" y="0" width="1.5" height="50"/><rect x="89.5" y="0" width="2" height="50"/><rect x="93.5" y="0" width="4.5" height="50"/><rect x="99.5" y="0" width="4.5" height="58"/><rect x="105.5" y="0" width="2" height="50"/><rect x="109.5" y="0" width="1.5" height="50"/><rect x="114.0" y="0" width="1.5" height="50"/><rect x="117.5" y="0" width="2" height="50"/><rect x="121.5" y="0" width="4.5" height="50"/><rect x="127.5" y="0" width="2" height="50"/><rect x="131.5" y="0" width="1.5" height="50"/><rect x="136.0" y="0" width="2" height="50"/><rect x="139.5" y="0" width="1.5" height="50"/><rect x="144.0" y="0" width="1.5" height="50"/><rect x="147.5" y="0" width="1.5" height="50"/><rect x="151.0" y="0" width="3" height="50"/><rect x="155.5" y="0" width="1.5" height="50"/><rect x="160.0" y="0" width="1.5" height="50"/><rect x="163.0" y="0" width="1.5" height="50"/><rect x="166.0" y="0" width="3" height="50"/><rect x="171.0" y="0" width="3" height="50"/><rect x="176.0" y="0" width="1.5" height="50"/><rect x="180.5" y="0" width="1.5" height="50"/><rect x="185.0" y="0" width="2" height="50"/><rect x="189.0" y="0" width="1.5" height="50"/><rect x="192.5" y="0" width="2" height="58"/></svg><span>8 88888 888 8888</span></div>''')
P['CT51']=cover('CT51','red','50% 22%','The prize','#FFC2B8','I am the prize, always',[('60','self love affirmations'),('9','ways to stop overthinking'),('120','words of the year')],'linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(90,0,0,.6) 100%)')
P['CT52']=cover('CT52','hair','50% 15%','Glow up','#F2C9A0','I glowed up so hard now my enemies are crying',[('8','glow up checklist steps'),('40','new year journal prompts'),('60','self love affirmations')],'linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(20,15,10,.7) 100%)')
P['CT53']=cover('CT53','sky','50% 18%','Money','#7FD3FF','I wake up to money',[('40','money affirmations'),('9','ways to stop overthinking'),('120','words of the year')],'linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(5,20,60,.7) 100%)')
for k,v in P.items(): open(f'{k}.dc.html','w').write(v)
print(len(P))
