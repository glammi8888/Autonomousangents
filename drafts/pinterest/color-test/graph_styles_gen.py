# More STYLES for Megan's 11 graphs, layouts unchanged (GS01–GS11), Nov 17. Megan: "okayyyy, i need more styles too".
# Rule (Nov 17): "keep the graphs … As they were, just changing the style" -> each GSxx = the G file with a new theme (colours / title font), mixed across the set.
import re
G='#0D0D0D'
TH={ # name: bg, ink (text+lines), node fill, highlight (#F65AAD), blush, title italic colour, dark logo, extra css
 'night':   dict(bg='#0D0D0D', ink='#FFFFFF', fill='#1C1C1C', hl='#F65AAD', bl='#3A1F2E', ti='#F65AAD', dark=True),
 'cover':   dict(bg='#D40806', ink='#FFFFFF', fill='#D40806', hl='#0D0D0D', bl='#B00705', ti='#FCD2DD', dark=True),
 'hotpink': dict(bg='#F65AAD', ink='#0D0D0D', fill='#FFFFFF', hl='#FFFFFF', bl='#FCD2DD', ti='#FFFFFF', dark=False),
 'editorial':dict(bg='#F5EEE0', ink='#0D0D0D', fill='#FFFFFF', hl='#D40806', bl='#F2C9C4', ti='#D40806', dark=False,
             css=".t{text-transform:uppercase;font-family:'Archivo Black',sans-serif!important;font-weight:400!important;letter-spacing:-.04em!important;line-height:.9!important}.t i{font-style:normal;font-weight:400}"),
 'tonal':   dict(bg='#FCD2DD', ink='#C2207E', fill='#FFF5F9', hl='#F65AAD', bl='#F9BFD6', ti='#0D0D0D', dark=False),
 'pastel':  dict(bg='linear-gradient(165deg,#F8DCEB 0%,#F1EBFF 100%)', ink='#0D0D0D', fill='#FFFFFF', hl='#F65AAD', bl='#E9DDFB', ti='#C2207E', dark=False),
}
MIX={'01':'night','02':'editorial','03':'hotpink','04':'cover','05':'tonal','06':'pastel','07':'editorial','08':'night','09':'hotpink','10':'tonal','11':'pastel'}
for n,th in MIX.items():
    t=TH[th]; h=open(f'G{n}.dc.html').read()
    for a,b in [(G,'@INK@'),('#0d0d0d','@INK@'),('#111','@INK@'),('#fff"','@FILL@"'),('#fff;','@FILL@;'),('#fff}','@FILL@}'),('#F65AAD','@HL@'),('#FCD2DD','@BL@'),('#C2207E','@TI@')]: h=h.replace(a,b)
    h=h.replace('@INK@',t['ink']).replace('@FILL@',t['fill']).replace('@HL@',t['hl']).replace('@BL@',t['bl']).replace('@TI@',t['ti'])
    h=re.sub(r'\.pin\{background:[^}]*\}',f'.pin{{background:{t["bg"]}}}',h)  # after colour swaps
    if t['dark']: h=h.replace('class="tl "','class="tl w"')
    if t.get('css'):
        h=h.replace('family=Inter+Tight','family=Archivo+Black&amp;family=Inter+Tight',1)
        h=h.replace('</style>',t['css']+'</style>',1)
    h=h.replace(f'<title>Graph',f'<title>Graph style {th} ·',1)
    open(f'GS{n}.dc.html','w').write(h); open(f'../carousels/GS{n}.dc.html','w').write(h)
print(len(MIX))
