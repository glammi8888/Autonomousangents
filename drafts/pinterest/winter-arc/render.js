// Visual QA render for the winter arc pins: 1000x1500 PNGs + phone-size contact sheets (390px and the ~236px feed).
// Usage: node render.js   (after python3 -I gen_winter_arc.py)
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');
const D=__dirname, OUT=path.join(D,'png');fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1500}});
const pins=fs.readdirSync(D).filter(f=>/^WA\d+\.html$/.test(f)).sort((a,c)=>parseInt(a.slice(2))-parseInt(c.slice(2)));
for(const f of pins){await p.goto('file://'+path.join(D,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 await p.screenshot({path:path.join(OUT,f.replace('.html','.png')),clip:{x:0,y:0,width:1000,height:1500}});}
const pngs=pins.map(f=>f.replace('.html','.png'));
for(const [w,name] of [[390,'sheet-390.html'],[236,'sheet-236.html']]){
 fs.writeFileSync(path.join(OUT,name),`<body style="margin:0;padding:12px;background:#ddd;display:flex;flex-wrap:wrap;gap:12px;width:${w*3+48}px">`+pngs.map(x=>`<img src="${x}" style="width:${w}px">`).join('')+'</body>');
 await p.setViewportSize({width:w*3+72,height:600});await p.goto('file://'+path.join(OUT,name));await p.waitForTimeout(400);
 await p.screenshot({path:path.join(OUT,name.replace('.html','.png')),fullPage:true});fs.unlinkSync(path.join(OUT,name));}
await b.close();console.log('rendered',pins.length);})();
