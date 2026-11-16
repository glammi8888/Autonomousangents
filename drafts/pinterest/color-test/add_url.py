# Megan, Nov 16: "Website should be on it too, or linked to every single pin" / "Or both actually".
# Idempotent post-process: puts a small "issue11.app" next to the ISSUE11 logo on any pin that doesn't show the site yet.
import re,sys,glob
files=sys.argv[1:] or sorted(glob.glob('CT*.dc.html'))+sorted(glob.glob('../article-pins/ArticlePin*.dc.html'))
n=0
for p in files:
    t=open(p).read()
    if 'issue11.app' in t: continue
    m=re.search(r'<img class="logo( w)?"[^>]*>',t)
    if not m: print('no logo',p); continue
    tag=m.group(0); white=bool(m.group(1)) or 'invert' in tag
    col='#fff' if white else '#0D0D0D'
    art='ArticlePin' in p
    if art: css=f'position:absolute;left:170px;top:70px;font-weight:600;font-size:19px;color:{col}'
    else:
        sty=re.search(r'style="([^"]*)"',tag); s=sty.group(1) if sty else ''
        if 'right:52px' in s and 'left:auto' in s: css=f'position:absolute;right:190px;bottom:72px;font-weight:600;font-size:19px;color:{col}'
        elif 'top:' in s and 'bottom:auto' in s:
            top=int(re.search(r'top:(\d+)px',s).group(1)); css=f'position:absolute;left:180px;top:{top+30}px;font-weight:600;font-size:19px;color:{col}'
        else: css=f'position:absolute;left:180px;bottom:74px;font-weight:600;font-size:19px;color:{col}'
    t=t.replace(tag,tag+f'<div class="siteurl" style="{css};z-index:6;text-shadow:{"0 2px 10px rgba(0,0,0,.4)" if white else "none"}">issue11.app</div>',1)
    open(p,'w').write(t); n+=1
print('added',n)
