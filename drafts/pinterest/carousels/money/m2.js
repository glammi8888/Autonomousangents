// M2-1..5: pillar 4 (money + soft life) · beliefs 5 + 7 (become YOU; your dream life is yours, not theirs).
// Copy by Megan, Nov 26 (word for word, lowercased): "$10,000 a month isn't delulu" / "And if it's unrealistic for them" /
// "Doesn't mean that it is for you" / "Then an inspiring quote from Paris Hilton".
// Quote: "Always act like you're wearing an invisible crown." Paris Hilton, Confessions of an Heiress (2004), as reported
// by China Daily, Sept 21, 2004 (book excerpt). Text + attribution only, never her photo.
// Closer + link: issue11.app/blog/money-affirmations (process: one move).
const {chromium} = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'); const fs = require('fs');
const D = __dirname, KIT = path.resolve(D, '../../../issue11-gift/rebrand-kit');
const F = 'file://' + KIT + '/InterTight.ttf';
const LOGO = 'file://' + KIT + '/logo-black.png';
const PINK = '#E0217F';
const css = `@font-face{font-family:IT;src:url(${F})}
*{box-sizing:border-box;margin:0;padding:0}
.pin{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:IT,system-ui,sans-serif;color:#0D0D0D;background:#fff}
.logo{position:absolute;left:50%;top:46px;height:74px;transform:translateX(-50%);z-index:3}
.num{position:absolute;right:60px;top:70px;font-weight:600;font-size:28px;letter-spacing:.08em;z-index:3}
.url{position:absolute;left:0;right:0;bottom:54px;text-align:center;font-weight:700;font-size:28px;z-index:3}
.big{position:absolute;left:60px;right:60px;font-weight:900;letter-spacing:-.045em;line-height:.98}`;
const shell = (n, body, bg) => `<html><head><style>${css}</style></head><body><div class="pin" style="${bg ? 'background:' + bg : ''}">
<img class="logo" src="${LOGO}"><div class="num">${n} / 5</div>${body}<div class="url">issue11.app</div></div></body></html>`;
const S = [];
S.push(shell(1, `<div class="big" style="top:420px;font-size:150px">$10,000 a month isn't <span style="color:${PINK}">delulu.</span></div>`));
S.push(shell(2, `<div class="big" style="top:560px;font-size:120px">and if it's unrealistic for them,</div>`));
S.push(shell(3, `<div class="big" style="top:560px;font-size:120px;color:${PINK}">doesn't mean it is for you.</div>`));
S.push(shell(4, `<div class="big" style="top:420px;font-size:104px;font-style:italic;font-weight:800">"always act like you're wearing an invisible crown."</div>
<div style="position:absolute;left:60px;top:1010px;font-weight:700;font-size:40px">— paris hilton</div>`, '#FCD2DD'));
S.push(shell(5, `<div class="big" style="top:340px;font-size:128px">now give it<br><span style="color:${PINK}">one real move.</span></div>
<div style="position:absolute;left:60px;right:60px;top:860px;font-weight:600;font-size:44px;line-height:1.35">money affirmations that feel true<br>→ link on this pin</div>`));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1000, height: 1500}});
  for (let i = 0; i < S.length; i++) {
    const f = path.join(D, 'M2-' + (i + 1) + '.html'); fs.writeFileSync(f, S[i]);
    await p.goto('file://' + f); await p.waitForTimeout(500);
    await p.screenshot({path: path.join(D, 'M2-' + (i + 1) + '.png')});
  }
  await b.close(); console.log('ok', S.length);
})();
