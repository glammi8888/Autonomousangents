// Render CAR16/CAR17 (Instagram 1080x1350) like render.js: swap /_blob ids for local img/<id>.jpg, load Inter Tight locally,
// write <slide>.png next to each .dc.html. Phone check sheets (390px, 236px) go to the dir given as SHEETS env (default: no sheets).
// Usage: node render34.js ../carousels/CAR16 ../carousels/CAR17
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');
const D=__dirname,R=path.join(D,'../../..'),LIB=path.join(R,'drafts/issue11-gift/rebrand-kit/img'),FONT=path.join(R,'drafts/issue11-gift/rebrand-kit/InterTight.ttf');
const src=id=>{if(id==='d196614efc6265e2205729134fb523b8')return LIB+'/logo-black.png';for(const e of ['jpg','webp','png']){const f=path.join(D,'img',id+'.'+e);if(fs.existsSync(f))return f;}throw new Error('missing blob '+id);};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});const all=[];
for(const dir of process.argv.slice(2)){const ad=path.resolve(dir);
 for(const f of fs.readdirSync(ad).filter(f=>f.endsWith('.dc.html')).sort((a,c)=>a.localeCompare(c,undefined,{numeric:true}))){
  let h=fs.readFileSync(path.join(ad,f),'utf8');
  h=h.replace('<script src="./support.js"></script>',`<style>@font-face{font-family:'Inter Tight';src:url(file://${FONT})}</style>`);
  h=h.replace(/\/_blob\/([0-9a-f]{32})/g,(s,id)=>'file://'+src(id));
  const tmp=path.join(ad,'_tmp.html');fs.writeFileSync(tmp,h);await p.goto('file://'+tmp);await p.waitForTimeout(500);
  const out=path.join(ad,f.replace('.dc.html','.png'));await p.screenshot({path:out,clip:{x:0,y:0,width:1080,height:1350}});fs.unlinkSync(tmp);all.push(out);}}
const S=process.env.SHEETS;if(S){fs.mkdirSync(S,{recursive:true});
 for(const w of [390,236]){const n=path.join(S,`sheet-${w}.html`);fs.writeFileSync(n,`<body style="margin:0;padding:12px;background:#ddd;display:flex;flex-wrap:wrap;gap:12px;width:${w*4+60}px">`+all.map(x=>`<img src="file://${x}" style="width:${w}px">`).join('')+'</body>');
  await p.setViewportSize({width:w*4+84,height:800});await p.goto('file://'+n);await p.waitForTimeout(400);await p.screenshot({path:n.replace('.html','.png'),fullPage:true});}}
await b.close();console.log('rendered',all.length);})();
