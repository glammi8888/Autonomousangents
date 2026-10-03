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
MOVE='<div style="position: relative; flex-shrink: 0; width: 300px; height: 300px; padding: 20px; background: #F65AAD; color: #0d0d0d; box-sizing: border-box; display: flex; flex-direction: column"><span style="position: absolute; right: 14px; top: -22px; display: block; transform: rotate(-4deg)"><span style="position: relative; display: block; width: 56px; height: 56px; border-radius: 16px; overflow: hidden; background: #F5EEE0; border: 3px solid #FFFFFF; box-shadow: 0 6px 14px rgba(0,0,0,0.2)"><img src="assets/0bb93fbeaae4f5c1075c630112490891.png" alt="" style="position: absolute; left: 50%; top: 50%; height: 76%; width: auto; transform: translate(-50%,-50%)"></span></span><div style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.03em; text-transform: uppercase">Lucky Star · Your move this week</div><div style="margin-top: 14px; font-family: \'Archivo Black\', sans-serif; letter-spacing: -0.06em; font-size: 32px; line-height: 0.9; text-transform: uppercase">Share one piece of work before you feel ready.</div><div style="margin-top: auto; display: flex; gap: 8px"><a href="#" data-move style="display: inline-flex; align-items: center; height: 44px; padding: 0 18px; border-radius: 22px; background: #0d0d0d; color: #FFFFFF; text-decoration: none; font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.03em; text-transform: uppercase">KEEP MY MOVE</a></div></div>'
HOLD='<div style="margin: 30px 16px 0; padding: 20px; background: #0d0d0d; color: #F5EEE0; display: flex; align-items: center; gap: 16px"><button type="button" id="holdBtn" aria-label="Hold to log your win" style="position: relative; width: 84px; height: 84px; border-radius: 50%; border: 0; background: #F65AAD; color: #0d0d0d; flex-shrink: 0; cursor: pointer; touch-action: none; user-select: none; -webkit-user-select: none"><svg width="84" height="84" viewBox="0 0 84 84" style="position: absolute; inset: 0; transform: rotate(-90deg)"><circle cx="42" cy="42" r="38" fill="none" stroke="#F5EEE0" stroke-width="4" stroke-dasharray="239" stroke-dashoffset="239" id="holdRing"/></svg><span style="font-family: \'Archivo Black\', sans-serif; font-size: 26px">★</span></button><div><div style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.03em; text-transform: uppercase; opacity: .7">Big or small</div><div id="holdLabel" style="font-family: \'Archivo Black\', sans-serif; letter-spacing: -0.05em; font-size: 26px; line-height: .92; text-transform: uppercase; margin-top: 6px">Hold to log<br>your win</div></div></div>'
S['home']=S['home'].replace('padding: 28px 16px 0; overflow: hidden">','padding: 28px 16px 0; overflow-x: auto; scrollbar-width: none">'+MOVE,1)
S['home']=S['home'].replace('<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 34px 16px 12px">',HOLD+'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 34px 16px 12px">',1)
S['aura']=S['aura'].replace('<div style="position: absolute; left: 20px; right: 20px; top: 330px; text-align: center;','<div id="lsCenter" style="position: absolute; left: 20px; right: 20px; top: 330px; text-align: center;',1)
S['aura']=S['aura'].replace('<div style="flex: 1; font-size: 18px; color: #8A8A8A">Talk to Lucky Star…</div>','<input id="lsAsk" placeholder="Talk to Lucky Star…" autocomplete="off" aria-label="Talk to Lucky Star" style="flex: 1; min-width: 0; border: 0; outline: 0; background: transparent; font-family: \'Archivo Narrow\', sans-serif; font-size: 18px; color: #0d0d0d">',1)
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
.night .scr>div[style*="background: #FFFFFF"]{background:#0d0d0d!important;color:#F5EEE0!important}
.night .scr [style*="color: #0d0d0d"]:not([style*="background: #FFFFFF"]):not([style*="background: #F5EEE0"]):not([style*="background: #F65AAD"]):not([style*="background: #FCD2DD"]){color:#F5EEE0!important}
.night .scr a[style*="background: #0d0d0d"]{background:#F5EEE0!important;color:#0d0d0d!important}
.night .scr [style*="background: #F2F2F2"],.night .scr [style*="background: #F7F7F7"]{background:#1d1d1d!important;color:#F5EEE0!important}
.night .scr [style*="border-top: 1px solid #0d0d0d"]{border-color:#F5EEE0!important}
.night img[src*="047dac70"]{filter:invert(1)}
.night #tabbar{background:rgba(20,20,20,.94)!important}.night #tabbar a{color:#F5EEE0!important}
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
const ORDER=[['launch','Launch'],['welcome','Welcome'],['how','How it works'],['q01','Q01'],['becoming','Q02'],['q03','Q03'],['q04','Q04'],['q05','Q05'],['q06','Q06'],['vision','Q07'],['q08','Q08'],['q09','Q09'],['meet','Meet Lucky Star'],['building','Building'],['reveal','Reveal'],['notif','Notifications'],['paywall','Paywall'],['signin','Save issue'],['home','Home'],['player','Audio'],['eyes','Eyes closed'],['after','After session'],['explore','Explore'],['collection','Collection'],['scribe','Scribe'],['empty','Scribe empty'],['write','Write'],['board','Your world'],['world','In frame'],['issue','Issue'],['reader','Read issue'],['page','Page'],['edit','Edit page'],['proof','Add proof'],['proofdone','Proof!'],['proofs','Past proof'],['streak','Streak'],['you','You'],['icons','App icon'],['delete','Delete account'],['offline','Offline'],['aura','Lucky Star'],['launchRed','Launch red'],['launchNoir','Launch noir'],['launchPhoto','Launch photo']];
const TABS=['home','scribe','issue','board','you','explore'];let cur='launch',hist=[];
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
wire('home','a','THE',()=>go('reader'));
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
const LC=document.getElementById('lsCenter'),LA=document.getElementById('lsAsk');
const PLAY='<svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><path d="M1 1l10 6-10 6z" fill="currentColor"/></svg> ';
const pill=(t,a,w)=>'<a href="#" data-ls="'+a+'" style="display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 18px;border-radius:22px;background:'+(w?'#FFFFFF':'#0d0d0d')+';color:'+(w?'#0d0d0d':'#FFFFFF')+';'+(w?'border:1px solid rgba(13,13,13,.25);':'')+'text-decoration:none;font-family:IBM Plex Mono,monospace;font-size:11px;text-transform:uppercase">'+t+'</a>';
const H1=(t,sm)=>'<div style="font-family:Archivo Black,sans-serif;letter-spacing:-.06em;font-size:'+(sm?34:44)+'px;line-height:.88;text-transform:uppercase">'+t+'</div>';
const K=t=>'<div style="font-family:IBM Plex Mono,monospace;font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:#666">'+t+'</div>';
const B=t=>'<p style="margin:0;font-size:16px;line-height:1.35;max-width:30ch">'+t+'</p>';
const row=h=>'<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center">'+h+'</div>';
const ASSIST={scribe:[K('Scribe · Lucky Star'),H1('Want me to<br>make it more<br>specific?',1),row(pill('Make it specific','done:Rewritten · tap Undo if you prefer yours')+pill('Not now','close',1))],
 write:[K('Scribe · Lucky Star'),H1('Want me to<br>make it more<br>specific?',1),row(pill('Make it specific','done:Rewritten · tap Undo if you prefer yours')+pill('Not now','close',1))],
 board:[K('Your World · Lucky Star'),H1('Curate images<br>for “a home<br>by the sea”?',1),row(pill('Curate 6 images','done:6 images added to Your World')+pill('Not now','close',1))],
 world:[K('Your World · Lucky Star'),H1('Build a page<br>from this<br>image?',1),row(pill('Build the page','done:Page 09 added to your Issue')+pill('Not now','close',1))],
 player:[K('Audio · Lucky Star'),H1('Make this<br>session yours?',1),B('I’ll add your name and your home by the sea.'),row(pill('Personalize','done:Your version is ready')+pill('Not now','close',1))],
 explore:[K('Audio · Lucky Star'),H1('Find a session<br>for tonight?',1),row(pill(PLAY+'10 min · Receiving','go:player')+pill('Not now','close',1))],
 issue:[K('Publish · Lucky Star'),H1('Finish your<br>Issue with me?',1),B('4 pages to go. I’ll draft them from your Scribe and World.'),row(pill('Draft 4 pages','done:4 pages drafted · review them in your Issue')+pill('Not now','close',1))],
 reader:[K('Publish · Lucky Star'),H1('Make this page<br>more “me”?',1),row(pill('Make it me','done:Page updated · Undo anytime')+pill('Not now','close',1))],
 page:[K('Publish · Lucky Star'),H1('Make this page<br>more “me”?',1),row(pill('Make it me','done:Page updated · Undo anytime')+pill('Not now','close',1))]};
const GUIDE=[[K('Tonight · 5 min'),H1('You’re ready<br>to embody it.'),row(pill(PLAY+'Start','go:player'))],
 [K('Your move · this week'),H1('This week,<br>let’s practice<br>being her.',1),B('Share one piece of work before you feel completely ready.'),row(pill('Keep my move','done:Your move for this week ✦')+pill('Another one','next',1))],
 [K('Lucky Star · Proof'),H1('That’s<br>proof.',1),B('Something you wrote three months ago sounds a lot like what’s happening now.'),row(pill('Add proof','go:proof')+pill('Not yet','next',1))]];
let gi=0,from='home';
function lsShow(parts){LC.innerHTML=parts.join('')}
function lsGuide(){if(ASSIST[from])lsShow(ASSIST[from]);else lsShow(GUIDE[gi%GUIDE.length])}
function lsReply(t){const l=t.toLowerCase(),said='<div style="font-size:17px;font-style:italic;color:#555;max-width:30ch">“'+t.replace(/[<>&]/g,'')+'”</div>';
 if(/don.?t know|no idea|lost|confused/.test(l))return lsShow([said,K('Desire · let’s find it'),H1('What would make<br>this year feel rich?',1),B('Answer in one sentence. I’ll save it to Scribe if you want.'),row(pill('Save to Scribe','done:Saved to Scribe')+pill('Not now','close',1))]);
 if(/picture|imagine|see myself|visual/.test(l))return lsShow([said,K('5 min · Future self visualization'),H1('Let’s work<br>on that.',1),row(pill(PLAY+'Start session','go:player'))]);
 if(/happened|got it|came true|signed|moved|finally/.test(l))return lsShow([said,K('That’s proof'),H1('Want to<br>capture it?',1),B('It goes into your Issue.'),row(pill('Add proof','go:proof')+pill('Not yet','close',1))]);
 lsShow([said,K('Your move · this week'),H1('Let’s practice<br>being her.',1),B('Share one piece of work before you feel completely ready.'),row(pill('Keep my move','done:Your move for this week ✦')+pill('Another one','next',1))])}
LC.addEventListener('click',e=>{const a=e.target.closest('[data-ls]');if(!a)return;e.preventDefault();const [k,v]=a.dataset.ls.split(/:(.*)/);
 if(k==='go'){go(v)}else if(k==='close'){back()}else if(k==='next'){gi++;from='home';lsGuide()}else if(k==='done'){lsShow([K('Done ✦'),H1(v,1),row(pill('Undo','undo',1)+pill('Back','close'))])}else if(k==='undo'){toast('Undone');lsGuide()}});
wire('aura','a','START',()=>go('player'));
const LSF=$s('aura').querySelector('a[aria-label="Send"]'),LSM=$s('aura').querySelector('a[aria-label="Hold to talk"]');
LSF.addEventListener('click',e=>{e.preventDefault();const v=LA.value.trim();if(v){lsReply(v);LA.value=''}});
LA.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();LSF.click()}});
LSM.addEventListener('click',e=>{e.preventDefault();const said="I know what I want but I can't picture myself having it.";let i=0;LA.value='';LA.placeholder='Listening…';LSM.style.boxShadow='0 0 0 8px rgba(246,90,173,.25)';
 const t=setInterval(()=>{LA.value=said.slice(0,++i);if(i>=said.length){clearInterval(t);setTimeout(()=>{LSM.style.boxShadow='';LA.placeholder='Talk to Lucky Star…';lsReply(said);LA.value=''},450)}},30)});
// Tab bar
const tl=[...document.querySelectorAll('#tabbar a')];
tl[0]&&tl[0].addEventListener('click',()=>go('home'));
tl[1]&&tl[1].addEventListener('click',()=>go('explore'));
tl[2]&&tl[2].addEventListener('click',()=>go('issue'));
tl[3]&&tl[3].addEventListener('click',()=>go('you'));
document.getElementById('eleven').addEventListener('click',()=>{from=cur;go('aura');lsGuide()});
document.querySelectorAll('.scr').forEach(s=>s.classList.toggle('on',s.dataset.name==='launch'));drawCrumbs();setTimeout(()=>cur==='launch'&&go('welcome'),1600);
</script>
'''
open(B+'v1-prototype/index.html','w').write(page)
print(len(page))
