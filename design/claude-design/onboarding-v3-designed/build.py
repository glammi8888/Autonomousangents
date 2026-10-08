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
t = open(os.path.join(here, 'template.html')).read().replace('/*ASSETS*/{}', json.dumps(A))
open(os.path.join(here, 'index.html'), 'w').write(t)
print('index.html', len(t)//1024, 'KB')
