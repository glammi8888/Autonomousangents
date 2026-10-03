import re,os
B='/home/user/Autonomousangents/design/claude-design/'
def art(path):
    s=open(B+path).read()
    a=s.index('<div style="position: relative; width: 390px'); b=s.rindex('</x-dc>')
    h=s[a:b].strip()
    h=re.sub(r'width: 390px; height: \d+px; box-sizing: border-box; overflow: hidden;','width: 100%; height: 100%; box-sizing: border-box; overflow-y: auto; overflow-x: hidden; scrollbar-width: none;',h,count=1)
    h=h.replace('./assets/','assets/')
    return h
def strip_nav(h):
    return re.sub(r'<nav style="position: absolute;.*?</nav>','',h,flags=re.S)
home=open(B+'v4-home-html/V4Home.dc.html').read()
nav=re.search(r'<nav style="position: absolute;.*?</nav>',home,re.S).group(0).replace('./assets/','assets/')
nav=nav.replace('<nav style="position: absolute;','<nav id="tabbar" style="position: absolute; z-index: 5;',1)
nav=nav.replace('<button type="button" aria-label="Lucky Star — tap to speak or write" style="','<button type="button" id="eleven" aria-label="Lucky Star" style="cursor: pointer; ',1)
S={
 'launch':art('v3-launch/V3Launch.dc.html'),
 'welcome':art('v5-onboarding-01-welcome/V5Welcome.dc.html'),
 'becoming':art('v3-onboarding/V3Onboarding.dc.html'),
 'vision':art('v5-onboarding-07-your-one-year-vision/V5Vision.dc.html'),
 'building':art('v5-onboarding-building-your-issue/V5Building.dc.html'),
 'signin':art('v2-sign-in/V2SignIn.dc.html'),
 'home':strip_nav(art('v4-home-html/V4Home.dc.html')),
 'player':art('v4-immersive-player-video-live-words/V4Immersive.dc.html'),
 'eyes':art('v4-eyes-closed-mode/V4EyesClosed.dc.html'),
 'world':art('v2-in-frame/V2InFrame.dc.html'),
 'scribe':strip_nav(art('v4-notes-to-self/V4Notes.dc.html')),
 'issue':strip_nav(art('v4-my-issue-progress-first/V4Issue.dc.html')),
 'aura':art('lucky-star-aura-html/LSQ6AuraChat.dc.html'),
 'streak':art('12-streak-calendar-with-logo-tiles/Idea12Streak.dc.html'),
 'board':art('14-vision-board/Idea14Collect.dc.html'),
 'icons':art('07-app-icon-picker/IdeaAppIcons.dc.html'),
 'launchRed':art('11-cream-on-red-full-bleed/Eleven03RedBleed.dc.html'),
 'launchNoir':art('11-small-cream-on-black/Eleven04Noir.dc.html'),
 'launchPhoto':art('11-white-over-photo/Eleven05Photo.dc.html'),
}
# Adaptations (functionality + locked architecture names)
S['launch']=re.sub(r'<div style="position: absolute; left: 70px; right: 70px; bottom: 80px;.*?</div></div></div>','',S['launch'],flags=re.S)
S['home']=S['home'].replace('>Listen</span>','>Audio</span>').replace('>Script</span>','>Scribe</span>').replace('>Curate</span>','>Your world</span>').replace('4 TO PRINT','4 TO GO')
S['scribe']=S['scribe'].replace('>01 / Writing<','>Scribe<')
S['world']=S['world'].replace('>02 / Image<','>Your world<')
S['issue']=S['issue'].replace('>4 to print<','>4 to go<').replace('FINISH 4 PAGES TO PRINT','FINISH MY ISSUE')
S['becoming']=S['becoming'].replace('>Step 2 of 4<','>Question 02<')
S['signin']=S['signin'].replace('BY CONTINUING YOU AGREE TO THE TERMS','SAVE YOUR ISSUE · BY CONTINUING YOU AGREE TO THE TERMS &amp; PRIVACY POLICY')
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'gaps.py')).read(),G:={})
S.update(G['S'])
secs='\n'.join(f'<section class="scr" id="s-{k}" data-name="{k}">{v}</section>' for k,v in S.items())
page='''<title>ISSUE11 V1 Prototype</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo+Narrow:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{--ground:#e9e6e1;--ink:#0d0d0d;--pink:#F65AAD;color-scheme:light}
html,body{background:var(--ground);color:var(--ink)}
body{margin:0;padding-inline:16px;padding-block:24px;display:flex;flex-direction:column;align-items:center;gap:14px;font-family:'Archivo Narrow',sans-serif}
a{color:inherit}
.fit{position:relative;width:390px;height:844px;flex-shrink:0}
.frame{position:absolute;left:0;top:0;width:390px;height:844px;transform-origin:0 0;border-radius:36px;overflow:hidden;box-shadow:0 0 0 8px #111,0 30px 60px rgba(0,0,0,.25);background:#fff}
.frame img{max-width:none}
.scr{position:absolute;inset:0;display:none}
.scr.on{display:block;animation:fade .25s ease}
@keyframes fade{from{opacity:.4}to{opacity:1}}
.scr>div::-webkit-scrollbar{display:none}
.m11{-webkit-mask-image:url(assets/599dae8c7a4a4bf4fde1c1f1e6037191.png);mask-image:url(assets/599dae8c7a4a4bf4fde1c1f1e6037191.png);-webkit-mask-size:contain;mask-size:contain;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-position:center;mask-position:center}
#tabbar{display:none!important}
.frame.tabs #tabbar{display:flex!important}
[data-go],[data-act],#eleven{cursor:pointer}
.toast{position:absolute;left:50%;top:18px;transform:translate(-50%,-140%);z-index:20;background:#0d0d0d;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.03em;padding:10px 14px;border-radius:18px;transition:transform .3s;max-width:85%;text-align:center}
.toast.show{transform:translate(-50%,0)}
.crumbs{font-family:'IBM Plex Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:#555;display:flex;gap:10px;flex-wrap:wrap;justify-content:center;max-width:390px}
.crumbs button{font:inherit;text-transform:inherit;border:1px solid #0d0d0d;background:transparent;border-radius:14px;padding:5px 10px;cursor:pointer;color:#0d0d0d}
.crumbs button.cur{background:#0d0d0d;color:#fff}
.sel{outline:3px solid #0d0d0d!important;outline-offset:3px}
@media (max-width:500px){html,body{background:#0d0d0d}body{padding:0;gap:10px}.crumbs{color:#aaa}.crumbs button{border-color:#555;color:#ddd}.frame{border-radius:0;box-shadow:none}}
@media (prefers-reduced-motion:reduce){.scr.on{animation:none}.toast{transition:none}}
</style>
<div class="fit" id="fit"><div class="frame" id="frame">
'''+secs+'\n'+nav+'''
<div class="toast" id="toast"></div>
</div></div>
<div class="crumbs" id="crumbs"></div>
<script>
const F=document.getElementById('frame'),T=document.getElementById('toast'),FIT=document.getElementById('fit');
function fit(){const phone=innerWidth<=500;const pad=phone?0:32;const sc=Math.min((innerWidth-pad)/390,(innerHeight-(phone?0:48))/844,phone?10:1);F.style.transform='scale('+sc+')';FIT.style.width=(390*sc)+'px';FIT.style.height=(844*sc)+'px'}
addEventListener('resize',fit);fit();
const ORDER=[['launch','Launch'],['welcome','Welcome'],['how','How it works'],['q01','Q01'],['becoming','Q02'],['q03','Q03'],['q04','Q04'],['q05','Q05'],['q06','Q06'],['vision','Q07'],['q08','Q08'],['q09','Q09'],['meet','Meet Lucky Star'],['building','Building'],['reveal','Reveal'],['notif','Notifications'],['paywall','Paywall'],['signin','Save issue'],['home','Home'],['player','Audio'],['eyes','Eyes closed'],['scribe','Scribe'],['write','Write'],['board','Your world'],['world','In frame'],['issue','Issue'],['page','Page'],['proof','Add proof'],['proofdone','Proof!'],['streak','Streak'],['you','You'],['icons','App icon'],['delete','Delete account'],['aura','Lucky Star'],['launchRed','Launch red'],['launchNoir','Launch noir'],['launchPhoto','Launch photo']];
const TABS=['home','scribe','issue','board','you'];let cur='launch',hist=[];
function go(n,back){if(n===cur)return;if(!back)hist.push(cur);document.querySelectorAll('.scr').forEach(s=>s.classList.toggle('on',s.dataset.name===n));cur=n;F.classList.toggle('tabs',TABS.includes(n));
 const d=document.querySelector('#s-'+n+'>div');if(d)d.scrollTop=0;
 document.querySelectorAll('#tabbar a').forEach((a,i)=>{const dot=a.querySelector('span+span');if(dot)dot.style.background=((i===0&&n==='home')||(i===2&&n==='issue'))?'#F65AAD':'transparent'});
 drawCrumbs();if(n==='building')runBuild();if(n==='launch')setTimeout(()=>cur==='launch'&&go('welcome'),1600)}
function back(){const p=hist.pop();if(p)go(p,true)}
function toast(m){T.textContent=m;T.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(()=>T.classList.remove('show'),2200)}
function drawCrumbs(){document.getElementById('crumbs').innerHTML=ORDER.map(([k,l])=>'<button data-c="'+k+'" class="'+(k===cur?'cur':'')+'">'+l+'</button>').join('')}
document.getElementById('crumbs').onclick=e=>{const b=e.target.closest('button');if(b){hist=[];go(b.dataset.c,true)}};
function $s(n){return document.getElementById('s-'+n)}
function byText(n,sel,txt){return [...$s(n).querySelectorAll(sel)].find(e=>e.textContent.trim().toUpperCase().startsWith(txt.toUpperCase()))}
function wire(n,sel,txt,fn){const el=byText(n,sel,txt);if(el){el.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();fn(el)})}}
// prevent all dead # links from jumping
document.addEventListener('click',e=>{const a=e.target.closest('a[href="#"]');if(a)e.preventDefault()});
// Launch
$s('launch').onclick=()=>go('welcome');
// Welcome
wire('welcome','a','BEGIN',()=>go('how'));
wire('welcome','div','I ALREADY HAVE',()=>go('signin'));
// Q02 select cards
const cards=[...$s('becoming').querySelectorAll('a[style*="height: 200px"]')];
function count(){const c=cards.filter(x=>x.dataset.on==='1').length;const b=byText('becoming','a','CONTINUE');if(b)b.firstChild.textContent='CONTINUE · '+c+' SELECTED ';}
cards.forEach(c=>{const chk=c.querySelector('span[style*="border-radius: 50%"]');c.dataset.on=chk?'1':'0';c.addEventListener('click',e=>{e.preventDefault();const on=c.dataset.on!=='1';c.dataset.on=on?'1':'0';c.style.outline=on?'3px solid #0d0d0d':'none';c.style.outlineOffset='3px';let k=c.querySelector('.chk')||chk;if(!k){k=document.createElement('span');k.className='chk';k.textContent='✓';k.style.cssText='position:absolute;right:10px;top:10px;width:28px;height:28px;border-radius:50%;background:#fff;color:#0d0d0d;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700';c.appendChild(k)}k.style.display=on?'flex':'none';count()})});
wire('becoming','a','CONTINUE',()=>go('q03'));
// Q07
wire('vision','a[aria-label="Back"]','',()=>back());
wire('vision','a','NEXT',()=>go('q08'));
wire('vision','a','SAY IT INSTEAD',()=>toast('Voice answer · uses iOS dictation'));
// Building animation
function runBuild(){const rows=[...$s('building').querySelectorAll('div[style*="padding: 10px 0"]')];const ok='width: 24px; height: 24px; border-radius: 50%; background: #FFFFFF; color: #0d0d0d; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700';
 rows.forEach((r,i)=>{const d=r.querySelector('span');if(i>=2){d.textContent='';d.style.cssText='width:24px;height:24px;border-radius:50%;border:1.5px solid rgba(255,255,255,.4)';r.style.opacity=.5}});
 [2,3].forEach((i,j)=>setTimeout(()=>{if(cur!=='building')return;const r=rows[i];const d=r.querySelector('span');d.textContent='✓';d.style.cssText=ok;r.style.opacity=1},900*(j+1)));
 setTimeout(()=>cur==='building'&&go('reveal'),2900)}
// Sign in
wire('signin','a','CONTINUE WITH APPLE',()=>go('home'));
wire('signin','a','CONTINUE WITH EMAIL',()=>go('home'));
// Home
wire('home','a','THE',()=>go('issue'));
wire('home','a[aria-label^="Resume"]','',()=>go('player'));
wire('home','a','LISTEN',()=>go('player'));
wire('home','a','ADD PROOF',()=>go('proof'));
wire('home','a','NOT YET',()=>toast('Lucky Star will ask again later'));
wire('home','a','LOG A SIGN',()=>toast('Sign saved to Scribe'));
['01','02','03','04'].forEach((num,i)=>{const t=[...$s('home').querySelectorAll('a')].find(a=>a.textContent.trim().startsWith(num));if(t)t.addEventListener('click',e=>{e.preventDefault();go(['player','scribe','board','issue'][i])})});
// Player
let playing=true;const pb=$s('player').querySelector('button[aria-label="Pause"]');
if(pb)pb.addEventListener('click',()=>{playing=!playing;pb.innerHTML=playing?'<svg width="20" height="22" viewBox="0 0 20 22"><rect x="3" y="2" width="4.5" height="18" rx="1" fill="currentColor"/><rect x="12.5" y="2" width="4.5" height="18" rx="1" fill="currentColor"/></svg>':'<svg width="20" height="22" viewBox="0 0 20 22"><path d="M4 2l14 9-14 9z" fill="currentColor"/></svg>'});
const mb=$s('player').querySelector('button[aria-label="Minimize"]');if(mb)mb.onclick=()=>back();
wire('player','span','EYES CLOSED',()=>go('eyes'));
const sv=$s('player').querySelector('button[aria-label="Save to my issue"]');if(sv)sv.onclick=()=>toast('Saved to your Issue ✦');
const cc=$s('player').querySelector('button[aria-label="Captions"]');if(cc)cc.onclick=()=>toast('Live words on / off');
// Eyes closed
$s('eyes').onclick=()=>back();
const breaths=['Breathe in for four.','Hold for four.','Breathe out for six.','See her clearly.'];let bi=0;setInterval(()=>{if(cur!=='eyes')return;const el=byText('eyes','div','');const t=[...$s('eyes').querySelectorAll('div')].find(d=>/Breathe|Hold|See her/.test(d.textContent)&&d.children.length===0);if(t){bi=(bi+1)%breaths.length;t.textContent=breaths[bi]}},2500);
// Scribe
wire('scribe','a[aria-label="Back"]','',()=>back());
wire('scribe','a','START WRITING',()=>go('write'));
// World
wire('world','a[aria-label="Back"]','',()=>back());
wire('world','a','+ ADD IMAGE',()=>toast('Opens the photo picker'));
// Issue
wire('issue','span','EDIT COVER',()=>go('page'));
wire('issue','a','FINISH MY ISSUE',()=>go('write'));
// Aura
const ax=$s('aura').querySelector('a[aria-label="Close"]');if(ax)ax.addEventListener('click',e=>{e.preventDefault();back()});
wire('aura','a','START',()=>go('player'));
['a[aria-label="Send"]','a[aria-label="Hold to talk"]'].forEach(q=>{const b=$s('aura').querySelector(q);if(b)b.addEventListener('click',e=>{e.preventDefault();toast('Talking to Lucky Star · V2')})});
// Vibes screens
['launchRed','launchNoir','launchPhoto'].forEach(n=>$s(n).onclick=()=>go('welcome'));
const hs=byText('home','div','12 DAY STREAK');if(hs){hs.style.cursor='pointer';hs.addEventListener('click',()=>go('streak'))}
[...$s('streak').querySelectorAll('a')].forEach(a=>a.addEventListener('click',e=>{e.preventDefault();if(/WRITE ONE LINE/.test(a.textContent)||a.getAttribute('aria-label')==='Write today')go('scribe');else if(a.getAttribute('aria-label')==='Back')back()}));
const wb=byText('streak','*','WRITE ONE LINE');if(wb&&wb.tagName!=='A'){wb.style.cursor='pointer';wb.addEventListener('click',()=>go('scribe'))}
[...$s('board').querySelectorAll('a[aria-label="Back"]')].forEach(a=>a.addEventListener('click',()=>back()));
const icons=[...$s('icons').querySelectorAll('a')].filter(a=>a.querySelector('div[style*="100px"]'));
icons.forEach(a=>a.addEventListener('click',()=>{icons.forEach(b=>{const t=b.querySelector('div');t.style.outline='none'});const t=a.querySelector('div');t.style.outline='3px solid #F65AAD';t.style.outlineOffset='4px'}));
wire('icons','a','SET ICON',()=>toast('App icon changed ✦'));
// ===== Gap screens (Design Room) =====
const NEXT={q01:'becoming',q03:'q04',q04:'q05',q05:'q06',q06:'vision',q08:'q09',q09:'meet',how:'q01'};
Object.entries(NEXT).forEach(([n,to])=>[...$s(n).querySelectorAll('[data-b]')].forEach(b=>{if(/NEXT|BUILD|START/.test(b.dataset.b))b.addEventListener('click',e=>{e.preventDefault();go(to)})}));
document.querySelectorAll('.scr').forEach(sc=>{sc.querySelectorAll('a[aria-label="Back"]').forEach(a=>{if(!a.dataset.w){a.dataset.w=1;a.addEventListener('click',e=>{e.preventDefault();back()})}});
 const opts=[...sc.querySelectorAll('[data-opt]')];opts.forEach(o=>o.addEventListener('click',e=>{e.preventDefault();opts.forEach(x=>x.querySelector('.dot').style.background='transparent');o.querySelector('.dot').style.background='#0d0d0d'}));
 sc.querySelectorAll('[data-chip]').forEach(c=>c.addEventListener('click',()=>{const on=c.style.color!=='rgb(255, 255, 255)';const pink=sc.dataset.name==='q06';c.style.background=on?(pink?'#F65AAD':'#0d0d0d'):'#F2F2F2';c.style.color=on?'#FFFFFF':'#0d0d0d'}));
 const picks=[...sc.querySelectorAll('[data-pick]')];picks.forEach(p=>p.addEventListener('click',e=>{e.preventDefault();p.dataset.on=p.style.outlineStyle==='solid'?'':'1';p.style.outline=p.dataset.on?'3px solid #0d0d0d':'none';p.style.outlineOffset='2px';const n=picks.filter(x=>x.style.outlineStyle==='solid').length;const b=sc.querySelector('[data-b^="NEXT"]');if(b)b.firstChild.textContent='NEXT · '+n+' PICKED '}));
 const plans=[...sc.querySelectorAll('[data-plan]')];plans.forEach(p=>p.addEventListener('click',e=>{e.preventDefault();plans.forEach(x=>x.style.border='1px solid rgba(13,13,13,0.2)');p.style.border='3px solid #0d0d0d'}))});
function onB(n,label,fn){[...$s(n).querySelectorAll('[data-b]')].filter(b=>b.dataset.b.startsWith(label)).forEach(b=>b.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();fn()}))}
onB('meet',"I'M IN",()=>{if(!document.getElementById('consent').checked){toast('AI is off · your Issue uses a simple template');}go('building')});
onB('meet','PRIVACY',()=>toast('Opens the privacy policy'));
onB('reveal','OPEN MY ISSUE',()=>go('notif'));
onB('notif','YES',()=>{toast('iOS asks for permission now');go('paywall')});onB('notif','NOT NOW',()=>go('paywall'));
onB('paywall','CONTINUE',()=>{toast('Apple payment sheet · then save your issue');go('signin')});onB('paywall','CLOSE',()=>go('signin'));onB('paywall','RESTORE',()=>toast('Restoring purchases…'));
onB('write','SAVE',()=>{toast('Saved to Scribe · page 08 ✦');back()});onB('write','SAY IT',()=>toast('iOS dictation'));
onB('proof','PHOTO',()=>toast('Opens the photo picker'));onB('proof','ADD PROOF',()=>go('proofdone'));
onB('proofdone','SEE IT',()=>{hist=[];go('issue')});
onB('page','APPLY',()=>{const i=document.getElementById('pageprompt');toast(i.value?'Lucky Star is updating this page…':'Type what to change first');i.value=''});
onB('delete','DELETE',()=>{toast('Account deleted');hist=[];setTimeout(()=>go('launch'),900)});onB('delete','KEEP',()=>back());
[...$s('you').querySelectorAll('[data-go2]')].forEach(a=>a.addEventListener('click',e=>{e.preventDefault();a.dataset.go2?go(a.dataset.go2):toast(a.textContent.replace('→','').trim())}));
[...$s('issue').querySelectorAll('div[style*="height: 140px"]')].forEach((t,i)=>{t.style.cursor='pointer';t.addEventListener('click',()=>i<7?go('page'):go('write'))});
[...$s('board').querySelectorAll('img')].forEach(im=>{const box=im.parentElement;box.style.cursor='pointer';box.addEventListener('click',()=>go('world'))});
// Tab bar
const tl=[...document.querySelectorAll('#tabbar a')];
tl[0]&&tl[0].addEventListener('click',()=>go('home'));
tl[1]&&tl[1].addEventListener('click',()=>toast('Explore · not designed yet'));
tl[2]&&tl[2].addEventListener('click',()=>go('issue'));
tl[3]&&tl[3].addEventListener('click',()=>go('you'));
document.getElementById('eleven').addEventListener('click',()=>go('aura'));
document.querySelectorAll('.scr').forEach(s=>s.classList.toggle('on',s.dataset.name==='launch'));drawCrumbs();setTimeout(()=>cur==='launch'&&go('welcome'),1600);
</script>
'''
open(B+'v1-prototype/index.html','w').write(page)
print(len(page))
