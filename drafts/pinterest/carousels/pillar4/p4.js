// P4-1..5: pillar 4 "a setback isn't a verdict" carousel, CAR5 editorial style, Pinterest 5-slide cut.
// Copy: C3 v3 (drafts/social/2026-11-17-informative-carousels.md, rewritten to the Brand Voice Guide) + Megan's
// picked hook (C3 v2: "it didn't manifest. and no, you didn't block it"). Lowercase, one idea per slide.
// Megan Nov 26: "Perfect so now we are creating content from there" (POV approved, start with pillars 1 + 4).
// Link: issue11.app/blog/does-manifestation-work
const {chromium} = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'); const fs = require('fs');
const D = __dirname, KIT = path.resolve(D, '../../../issue11-gift/rebrand-kit');
const F = 'file://' + KIT + '/InterTight.ttf';
const LOGO = 'file://' + KIT + '/logo-black.png';
const PHOTO = 'file://' + KIT + '/img/e27.jpg';
const PINK = '#E0217F';
const css = `@font-face{font-family:IT;src:url(${F})}
*{box-sizing:border-box;margin:0;padding:0}
.pin{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:IT,system-ui,sans-serif;color:#0D0D0D;background:#fff}
.logo{position:absolute;left:50%;top:46px;height:74px;transform:translateX(-50%);z-index:3}
.num{position:absolute;right:60px;top:70px;font-weight:600;font-size:28px;letter-spacing:.08em;z-index:3}
.url{position:absolute;left:0;right:0;bottom:54px;text-align:center;font-weight:700;font-size:28px;z-index:3}
.big{position:absolute;left:60px;right:60px;font-weight:900;letter-spacing:-.045em;line-height:.98}
.mid{position:absolute;left:80px;right:80px;text-align:center;font-weight:500;letter-spacing:-.03em;line-height:1.12}
.lab{position:absolute;left:0;right:0;text-align:center;font-weight:800;font-size:24px;letter-spacing:.2em;color:${PINK};text-transform:uppercase}`;
const shell = (n, body, bg) => `<html><head><style>${css}</style></head><body><div class="pin" style="${bg ? 'background:' + bg : ''}">
<img class="logo" src="${LOGO}"><div class="num">${n} / 5</div>${body}<div class="url">issue11.app</div></div></body></html>`;
const S = [];
// 1 · cover (Megan's picked hook)
S.push(shell(1, `<div class="big" style="top:300px;font-size:128px">it didn't manifest.</div>
<div class="big" style="top:640px;font-size:128px;color:${PINK}">and no, you didn't block it.</div>`));
// 2 · the advice she got (their words, quoted to question it)
S.push(shell(2, `<div class="mid" style="top:520px;font-size:76px">they told you not to react to the 3d.</div>
<div class="mid" style="top:860px;font-size:44px;font-weight:600;color:#555">so you stopped opening the bank app.</div>`));
// 3 · the turn (registry line) + framed photo
S.push(shell(3, `<div style="position:absolute;inset:0;background:#EFEAFB"></div>
<img src="${PHOTO}" style="position:absolute;left:250px;top:190px;width:500px;height:620px;object-fit:cover;object-position:50% 20%">
<div class="mid" style="top:880px;font-size:66px;font-style:italic">your mind is powerful.<br>it's just not the whole universe.</div>`));
// 4 · conceptual model: the month you pictured vs the month you had
S.push(shell(4, `<div class="lab" style="top:230px">not real data. just real life.</div>
<svg style="position:absolute;left:100px;top:330px" width="800" height="620" viewBox="0 0 800 620">
<line x1="40" y1="580" x2="780" y2="580" stroke="#0D0D0D" stroke-width="3"/>
<line x1="40" y1="580" x2="40" y2="20" stroke="#0D0D0D" stroke-width="3"/>
<path d="M40 560 L760 60" stroke="#BDBDBD" stroke-width="10" fill="none" stroke-dasharray="22 16" stroke-linecap="round"/>
<path d="M40 560 C150 430 210 420 280 420 S390 440 440 470 S540 330 600 260 S700 170 760 150" stroke="${PINK}" stroke-width="12" fill="none" stroke-linecap="round"/>
</svg>
<div style="position:absolute;left:110px;top:1010px;font-weight:700;font-size:38px;color:#9A9A9A">- - what you pictured</div>
<div style="position:absolute;left:110px;top:1070px;font-weight:700;font-size:38px;color:${PINK}">— what actually happened</div>
<div class="mid" style="top:1180px;font-size:44px;font-weight:600">still going up though.</div>`));
// 5 · the decision + next step
S.push(shell(5, `<div class="big" style="top:250px;font-size:112px">one slow month doesn't mean it's over.</div>
<div style="position:absolute;left:60px;right:60px;top:700px;font-weight:700;font-size:56px;line-height:1.35">keep going.<br>change the plan.<br>take a break.<br>try a smaller step.<br><span style="color:${PINK}">your call.</span></div>
<div style="position:absolute;left:60px;right:60px;top:1150px;font-weight:600;font-size:38px">save this for month two.</div>`));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1000, height: 1500}});
  for (let i = 0; i < S.length; i++) {
    const f = path.join(D, 'P4-' + (i + 1) + '.html'); fs.writeFileSync(f, S[i]);
    await p.goto('file://' + f); await p.waitForTimeout(500);
    await p.screenshot({path: path.join(D, 'P4-' + (i + 1) + '.png')});
  }
  await b.close(); console.log('ok', S.length);
})();
