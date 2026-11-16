// Visual QA render for article pins: swaps /_blob ids for local copies (article-pins/img/<id>.webp, else the
// rebrand-kit library via the batch generators' id map), loads Inter Tight locally, screenshots 1000x1500,
// then builds phone-size contact sheets (390px and 236px feed width). Usage: node render.js [file.dc.html ...]
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');
const D=__dirname, R=path.join(D,'../../..'), LIB=path.join(R,'drafts/issue11-gift/rebrand-kit/img'), FONT=path.join(R,'drafts/issue11-gift/rebrand-kit/InterTight.ttf');
const map={};for(const g of ['batch1/generator-v6.py','batch2/generator-b2.py','batch3/generator-b3.py','styles/generator-styles.py']){const p=path.join(D,'..',g);if(fs.existsSync(p))for(const m of fs.readFileSync(p,'utf8').matchAll(/"(\w\d\d?)":"([0-9a-f]{32})"/g))map[m[2]]=m[1];}
const src=id=>{if(id==='d196614efc6265e2205729134fb523b8')return LIB+'/logo-black.png';for(const e of ['webp','jpg','png']){const f=path.join(D,'img',id+'.'+e);if(fs.existsSync(f))return f;}if(map[id])return LIB+'/'+map[id]+'.jpg';throw new Error('missing blob '+id);};
const OUT=path.join(D,'png');fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});
const pins=(process.argv.slice(2).length?process.argv.slice(2):fs.readdirSync(D).filter(f=>f.endsWith('.dc.html'))).map(f=>path.basename(f)).sort();
for(const f of pins){let h=fs.readFileSync(path.join(D,f),'utf8');
 h=h.replace('<script src="./support.js"></script>',`<style>@font-face{font-family:'Inter Tight';src:url(file://${FONT})}</style>`);
 h=h.replace(/\/_blob\/([0-9a-f]{32})/g,(s,id)=>'file://'+src(id));
 const tmp=path.join(OUT,'_'+f.replace('.dc',''));fs.writeFileSync(tmp,h);
 await p.goto('file://'+tmp);await p.waitForTimeout(600);
 await p.screenshot({path:path.join(OUT,f.replace('.dc.html','.png')),clip:{x:0,y:0,width:1000,height:1500}});fs.unlinkSync(tmp);}
const pngs=pins.map(f=>f.replace('.dc.html','.png'));
for(const [w,name] of [[390,'sheet-390.html'],[236,'sheet-236.html']]){
 fs.writeFileSync(path.join(OUT,name),`<body style="margin:0;padding:12px;background:#ddd;display:flex;flex-wrap:wrap;gap:12px;width:${w*5+72}px">`+pngs.map(x=>`<img src="${x}" style="width:${w}px">`).join('')+'</body>');
 await p.setViewportSize({width:w*5+96,height:800});await p.goto('file://'+path.join(OUT,name));await p.waitForTimeout(400);
 await p.screenshot({path:path.join(OUT,name.replace('.html','.png')),fullPage:true});fs.unlinkSync(path.join(OUT,name));}
await b.close();console.log('rendered',pins.length);})();
