// 3D motion pin sample (Megan Nov 23: "3D effects ... to stand out" / "Like a movement").
// A phone showing a pin floats and turns slowly in 3D on pastel pink while a glossy heart drifts in front (parallax).
// Seamless 6s loop, 1000x1500 (2:3), 30fps -> MP4. Usage: node motion3d.js <screen.png> <out.mp4>
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');const {execSync}=require('child_process');
const [scr,out]=process.argv.slice(2);const FR=path.join(__dirname,'_frames');fs.rmSync(FR,{recursive:true,force:true});fs.mkdirSync(FR);
const HEART=`<svg viewBox="0 0 64 58"><defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB4D9"/><stop offset="1" stop-color="#F27BB7"/></linearGradient></defs><path d="M32 56C14 43 2 32 2 18 2 8.6 9.6 2 18.5 2 24.6 2 29.4 5.2 32 10 34.6 5.2 39.4 2 45.5 2 54.4 2 62 8.6 62 18 62 32 50 43 32 56Z" fill="url(#hg)"/><ellipse cx="17" cy="14" rx="6.5" ry="4.2" fill="#fff" opacity=".6" transform="rotate(-30 17 14)"/></svg>`;
const html=`<body style="margin:0;width:1000px;height:1500px;overflow:hidden;background:radial-gradient(circle at 50% 40%,#FFE3F1,#F7C6DF 70%,#EFB3D3);perspective:1800px">
<div id="sh" style="position:absolute;left:50%;top:1330px;width:560px;height:60px;margin-left:-280px;border-radius:50%;background:rgba(150,40,95,.28);filter:blur(28px)"></div>
<div id="ph" style="position:absolute;left:50%;top:50%;width:600px;height:1220px;margin:-630px 0 0 -300px;border-radius:84px;background:#111;box-shadow:inset 0 0 0 4px #2a2a2a,0 40px 80px rgba(120,30,80,.35);transform-style:preserve-3d">
 <div style="position:absolute;inset:22px;border-radius:64px;overflow:hidden;background:#000"><img src="file://${path.resolve(scr)}" style="width:100%;height:100%;object-fit:contain;object-position:center"></div>
 <div id="gl" style="position:absolute;inset:22px;border-radius:64px;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.16) 45%,transparent 60%);background-size:300% 100%"></div></div>
<div id="ht" style="position:absolute;left:740px;top:170px;width:200px;filter:drop-shadow(0 24px 22px rgba(180,40,110,.35))">${HEART}</div></body>`;
fs.writeFileSync(path.join(FR,'p.html'),html);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});await p.goto('file://'+path.join(FR,'p.html'));await p.waitForTimeout(500);
const N=180;for(let i=0;i<N;i++){const t=i/N*2*Math.PI;
 await p.evaluate(([t])=>{const s=Math.sin(t),c=Math.cos(t);
  ph.style.transform=`translateY(${s*-22}px) rotateY(${s*14}deg) rotateX(${c*5}deg) rotateZ(${s*-1.5}deg)`;
  gl.style.backgroundPosition=`${50+s*50}% 0`;
  sh.style.transform=`scaleX(${1+s*.08})`;sh.style.opacity=.85-s*.15;
  ht.style.transform=`translate(${c*-18}px,${Math.sin(t*2)*-26}px) rotate(${s*12}deg) scale(${1+Math.sin(t*2)*.05})`;},[t]);
 await p.screenshot({path:path.join(FR,String(i).padStart(4,'0')+'.png')});}
await b.close();
execSync(`ffmpeg -y -loglevel error -framerate 30 -i ${FR}/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart ${out}`);
execSync(`ffmpeg -y -loglevel error -ss 1.5 -i ${out} -frames:v 1 ${out.replace('.mp4','-still.png')}`);
fs.rmSync(FR,{recursive:true,force:true});console.log('ok',out);})();
