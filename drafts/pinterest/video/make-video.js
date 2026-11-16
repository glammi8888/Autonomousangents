// Video pin sample: takes a color-test pin, adds CSS animations, steps them frame by frame with the Web
// Animations API and pipes PNG frames to ffmpeg (H.264 MP4, 1000x1500 2:3, 30fps). Free, local.
// Usage: node make-video.js CT144 out.mp4 [seconds]
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');const {spawn}=require('child_process');
const [pin,out,secs='8']=process.argv.slice(2);const D=path.join(__dirname,'../color-test'),R=path.join(D,'../../..');
const LIB=path.join(R,'drafts/issue11-gift/rebrand-kit/img'),FONT=path.join(R,'drafts/issue11-gift/rebrand-kit/InterTight.ttf');
const src=id=>{if(id==='d196614efc6265e2205729134fb523b8')return LIB+'/logo-black.png';for(const e of ['webp','jpg','png']){const f=path.join(D,'img',id+'.'+e);if(fs.existsSync(f))return f;}throw new Error('missing '+id);};
const ANIM=`<style>
@keyframes zoom{from{transform:scale(1)}to{transform:scale(1.09)}}
@keyframes rise{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
img.f{animation:zoom ${secs}s linear both}
.n{animation:rise 1s cubic-bezier(.2,.7,.2,1) .5s both}
.k{animation:fade .7s ease 1.7s both}
.l{animation:rise .9s cubic-bezier(.2,.7,.2,1) 2.4s both}
</style>`;
(async()=>{let h=fs.readFileSync(path.join(D,pin+'.dc.html'),'utf8');
h=h.replace('<script src="./support.js"></script>',`<style>@font-face{font-family:'Inter Tight';src:url(file://${FONT})}</style>`).replace(/\/_blob\/([0-9a-f]{32})/g,(s,id)=>'file://'+src(id)).replace('</head>',ANIM+'</head>');
const tmp=path.join(__dirname,'_tmp.html');fs.writeFileSync(tmp,h);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});await p.goto('file://'+tmp);await p.waitForTimeout(800);
await p.evaluate(()=>document.getAnimations().forEach(a=>a.pause()));
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart',out]);
const N=Math.round(+secs*30);
for(let i=0;i<N;i++){await p.evaluate(t=>document.getAnimations().forEach(a=>a.currentTime=t),i*1000/30);ff.stdin.write(await p.screenshot({clip:{x:0,y:0,width:1000,height:1500}}));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();fs.unlinkSync(tmp);console.log('wrote',out,N,'frames');})();
