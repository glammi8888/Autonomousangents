"""Build the designed ISSUE11 onboarding (locked flow, Megan's V5 Claude Design). Run: python3 build.py"""
import base64, json, os
here = os.path.dirname(os.path.abspath(__file__))
files = {'pcover':'photo-cover.jpg','pwelcome':'photo-welcome.jpg','p3':'photo-3.jpg','p4':'photo-4.jpg','p5':'photo-5.jpg','p6':'photo-6.jpg','p7':'photo-7.jpg','psignin':'photo-signin.jpg',
         'mwhite':'masthead-white.png','mblack':'masthead-black.png','mcream':'masthead-cream.png',
         'e11pink':'eleven-pink.png','e11black':'eleven-black.png','e11cream':'eleven-cream.png','e11white':'eleven-white.png'}
A = {}
for k, f in files.items():
    mime = 'image/png' if f.endswith('.png') else 'image/jpeg'
    A[k] = 'data:%s;base64,%s' % (mime, base64.b64encode(open(os.path.join(here, 'assets', f), 'rb').read()).decode())
def font(f):
    return 'data:font/woff2;base64,' + base64.b64encode(open(os.path.join(here, 'assets', f), 'rb').read()).decode()
# Fonts are embedded (SIL Open Font License) so titles always render in Archivo Black, even if Google Fonts can't load.
FONTS = ("@font-face{font-family:'Archivo Black';font-weight:400;font-display:block;src:url(%s) format('woff2')}"
         "@font-face{font-family:'Archivo Narrow';font-weight:400 700;font-display:block;src:url(%s) format('woff2')}"
         "@font-face{font-family:'IBM Plex Mono';font-weight:400;font-display:block;src:url(%s) format('woff2')}"
         "@font-face{font-family:'IBM Plex Mono';font-weight:500;font-display:block;src:url(%s) format('woff2')}") % (
         font('font-archivo-black.woff2'), font('font-archivo-narrow.woff2'), font('font-plex-mono-400.woff2'), font('font-plex-mono-500.woff2'))
t = open(os.path.join(here, 'template.html')).read().replace('/*ASSETS*/{}', json.dumps(A)).replace('/*FONTS*/', FONTS)
open(os.path.join(here, 'index.html'), 'w').write(t)
print('index.html', len(t)//1024, 'KB')
