// Render a notes pin as a real phone screen (tall, full-bleed) for onscreen.py. Same HTML as the pin, just a
// phone-shaped viewport, status bar beside the notch, no carousel "swipe" cue.
// Usage: node screen_render.js <pin.dc.html> <out.png> <width> <height> <topPad> [sidePad] [bottomPad]
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');const path=require('path');
const [f,out,W,H,TP,SP=56,BP=60,TS=0]=process.argv.slice(2);const FONT=path.resolve(__dirname,'../../issue11-gift/rebrand-kit/InterTight.ttf');
let h=fs.readFileSync(f,'utf8').replace('<script src="./support.js"></script>',`<style>@font-face{font-family:'Inter Tight';src:url(file://${FONT})}</style>`)
 .replace('width:1000px; height:1500px',`width:${W}px; height:${H}px`).replace('padding:40px 64px',`padding:${TP}px ${SP}px`).replace('left:64px; bottom:60px',`left:${SP}px; bottom:${BP}px`)
 .replace(/\d\/5 · /,'').replace(/year(<svg[^]*?<\/svg>)/,'<span style="white-space:nowrap">year$1</span>').replace(/font-size:\d+px; font-weight:800/,m=>+TS?`font-size:${TS}px; font-weight:800`:m).replace(/<p style="position:absolute; right:64px[^<]*swipe[^<]*<\/p>/,'');
const tmp=path.join(path.dirname(path.resolve(out)),'_screen.html');fs.writeFileSync(tmp,h);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+W,height:+H}});await p.goto('file://'+tmp);await p.waitForTimeout(500);
await p.screenshot({path:out});await b.close();fs.unlinkSync(tmp);console.log('ok',out);})();
