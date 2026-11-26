// KITE-1..5: free 2027 glow up kit carousel, CAR5 editorial style (Megan Nov 26: "Im tired of the notes app one").
// Format borrowed from the viral watch ("I made an entire ___ system (FREE)"); content is ours: real kit pages
// (page-XX.png, rendered from drafts/issue11-gift/rebrand-kit/kit.html by kitpages.js) and real prompt titles.
// Cover hook by Megan: "See others living their best lives while you're falling behind? read this" (lowercased).
const {chromium} = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const D = __dirname, KIT = path.resolve(D, '../../../issue11-gift/rebrand-kit');
const F = 'file://' + KIT + '/InterTight.ttf';
const img = n => 'file://' + path.join(D, 'page-' + n + '.png');
const LOGO_B = 'file://' + KIT + '/logo-black.png', LOGO_W = 'file://' + KIT + '/img/logo-white.png';
const PINK = '#E0217F';
const css = `@font-face{font-family:IT;src:url(${F})}
*{box-sizing:border-box;margin:0;padding:0}
.pin{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:IT,system-ui,sans-serif;color:#0D0D0D;background:#fff}
.logo{position:absolute;left:50%;top:46px;height:74px;transform:translateX(-50%)}
.num{position:absolute;right:60px;top:70px;font-weight:600;font-size:28px;letter-spacing:.08em}
.url{position:absolute;left:0;right:0;bottom:54px;text-align:center;font-weight:700;font-size:28px}
.pill{display:inline-block;background:${PINK};color:#fff;font-weight:800;font-size:24px;letter-spacing:.14em;padding:12px 20px;text-transform:uppercase}
.lab{font-weight:800;font-size:24px;letter-spacing:.2em;color:${PINK};text-transform:uppercase}
.page{position:absolute;box-shadow:0 24px 60px rgba(0,0,0,.28);border:1px solid #e6e6e6}`;
const shell = (n, body, dark) => `<html><head><style>${css}</style></head><body><div class="pin" style="${dark ? 'background:#0D0D0D;color:#fff' : ''}">
<img class="logo" src="${dark ? LOGO_W : LOGO_B}"><div class="num">${n} / 5</div>${body}<div class="url">issue11.app</div></div></body></html>`;
const S = [];
// 1 · cover: Megan's hook
S.push(shell(1, `
<div style="position:absolute;left:60px;top:200px;right:60px"><span class="pill">free 2027 glow up kit</span></div>
<div style="position:absolute;left:60px;right:60px;top:290px;font-weight:900;font-size:104px;line-height:.98;letter-spacing:-.045em">see others living their best lives while you're falling behind?</div>
<div style="position:absolute;left:60px;top:800px;font-weight:800;font-size:56px;color:${PINK};letter-spacing:-.02em">read this →</div>
<img class="page" src="${img('01')}" style="right:80px;top:900px;width:320px;transform:rotate(5deg)">`));
// 2 · what's inside (real pages)
S.push(shell(2, `
<div style="position:absolute;left:60px;top:200px" class="lab">what's inside</div>
<div style="position:absolute;left:60px;right:60px;top:250px;font-weight:900;font-size:78px;line-height:.98;letter-spacing:-.045em">the free 2027 glow up kit</div>
<img class="page" src="${img('01')}" style="left:60px;top:560px;width:300px;transform:rotate(-4deg)">
<img class="page" src="${img('03')}" style="left:350px;top:540px;width:300px;transform:rotate(1deg)">
<img class="page" src="${img('10')}" style="left:640px;top:560px;width:300px;transform:rotate(4deg)">
<div style="position:absolute;left:60px;right:60px;top:1060px;display:flex;justify-content:space-between;font-weight:700;font-size:30px;line-height:1.2;text-align:center">
<div style="width:280px">30 chatgpt prompts</div><div style="width:280px">my 2027 list</div><div style="width:280px">a 30-day future self challenge</div></div>`));
// 3 · six areas + real prompt titles
S.push(shell(3, `
<div style="position:absolute;left:0;right:0;top:220px;text-align:center" class="lab">6 areas · 5 prompts each</div>
<div style="position:absolute;left:60px;right:60px;top:300px;text-align:center;font-weight:300;font-size:118px;line-height:1.02;letter-spacing:-.05em">body<br>money<br>love<br>style<br>beauty<br>savings</div>
<div style="position:absolute;left:90px;right:90px;top:1110px;text-align:center;font-weight:500;font-size:36px;line-height:1.35;letter-spacing:-.015em">
<b>"my 5-minute glow up morning."</b><br><b>"ask for more, no 3-paragraph apology."</b></div>`));
// 4 · the method (real chapter page)
S.push(shell(4, `
<div style="position:absolute;inset:0;background:#EFEAFB"></div>
<img class="logo" src="${LOGO_B}"><div class="num">4 / 5</div>
<img class="page" src="${img('04')}" style="left:190px;top:170px;width:620px;transform:rotate(-2deg)">
<div style="position:absolute;left:70px;right:70px;top:1100px;text-align:center;font-style:italic;font-weight:500;font-size:52px;line-height:1.15;letter-spacing:-.02em">real methods, not "believe harder."</div>
<div style="position:absolute;left:70px;right:70px;top:1250px;text-align:center;font-weight:700;font-size:32px">habit stacking · tiny habits · woop</div>`));
// 5 · get it
S.push(shell(5, `
<div style="position:absolute;left:60px;top:220px" class="lab">it's free</div>
<div style="position:absolute;left:60px;right:60px;top:270px;font-weight:900;font-size:150px;line-height:.92;letter-spacing:-.055em">get your kit.</div>
<div style="position:absolute;left:60px;right:60px;top:600px;font-weight:600;font-size:40px;line-height:1.35">tap the link on this pin<br>or go to <span style="color:${PINK}">issue11.app/rebrand&#8209;kit</span></div>
<img class="page" src="${img('03')}" style="left:110px;top:800px;width:380px;transform:rotate(-4deg)">
<img class="page" src="${img('10')}" style="left:510px;top:780px;width:380px;transform:rotate(3deg)">`));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1000, height: 1500}});
  for (let i = 0; i < S.length; i++) {
    const f = path.join(D, 'KITE-' + (i + 1) + '.html'); require('fs').writeFileSync(f, S[i]);
    await p.goto('file://' + f); await p.waitForTimeout(500);
    await p.screenshot({path: path.join(D, 'KITE-' + (i + 1) + '.png')});
  }
  await b.close(); console.log('ok', S.length);
})();
