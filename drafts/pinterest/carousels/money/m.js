// M-1..5: pillar 4 (money + soft life) · belief 2 (process, not outcome). CAR5 editorial style, 5 slides.
// Megan Nov 26: "Sure" (money carousel next). Hook pattern Megan liked: "...? this is for you".
// Links to issue11.app/blog/money-affirmations ("Money Affirmations: 40 for Abundance That Feel True";
// sections: what they can and can't do · how to manifest money, realistically · affirmation vs action vs both).
// Moves on slide 4 are real prompt titles from the free kit (drafts/issue11-gift/rebrand-kit/prompts.json).
// Humanized, lowercase, one idea per slide, no money promised by a date.
const {chromium} = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'); const fs = require('fs');
const D = __dirname, KIT = path.resolve(D, '../../../issue11-gift/rebrand-kit');
const F = 'file://' + KIT + '/InterTight.ttf';
const LOGO = 'file://' + KIT + '/logo-black.png';
const PHOTO = 'file://' + KIT + '/img/e19.jpg';
const PINK = '#E0217F';
const css = `@font-face{font-family:IT;src:url(${F})}
*{box-sizing:border-box;margin:0;padding:0}
.pin{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:IT,system-ui,sans-serif;color:#0D0D0D;background:#fff}
.logo{position:absolute;left:50%;top:46px;height:74px;transform:translateX(-50%);z-index:3}
.num{position:absolute;right:60px;top:70px;font-weight:600;font-size:28px;letter-spacing:.08em;z-index:3}
.url{position:absolute;left:0;right:0;bottom:54px;text-align:center;font-weight:700;font-size:28px;z-index:3}
.big{position:absolute;left:60px;right:60px;font-weight:900;letter-spacing:-.045em;line-height:.98}
.mid{position:absolute;left:80px;right:80px;text-align:center;font-weight:500;letter-spacing:-.03em;line-height:1.12}`;
const shell = (n, body) => `<html><head><style>${css}</style></head><body><div class="pin">
<img class="logo" src="${LOGO}"><div class="num">${n} / 5</div>${body}<div class="url">issue11.app</div></div></body></html>`;
const S = [];
// 1 · cover
S.push(shell(1, `<div class="big" style="top:280px;font-size:112px">manifesting money but your bank account didn't get the memo?</div>
<div class="big" style="top:1010px;font-size:112px;color:${PINK}">this is for you.</div>`));
// 2 · the relatable moment (framed photo)
S.push(shell(2, `<div style="position:absolute;inset:0;background:#EFEAFB"></div>
<img src="${PHOTO}" style="position:absolute;left:250px;top:180px;width:500px;height:620px;object-fit:cover;object-position:50% 0%">
<div class="mid" style="top:870px;font-size:62px;font-style:italic">saying "i'm a millionaire"<br>while checking your balance<br>with one eye open.</div>`));
// 3 · why it doesn't stick
S.push(shell(3, `<div class="mid" style="top:470px;font-size:84px;font-weight:700">your brain knows it's not true yet.</div>
<div class="mid" style="top:820px;font-size:48px;font-weight:600;color:#555">so pick a line you'd actually believe.</div>`));
// 4 · pair it with one move (real kit prompts)
S.push(shell(4, `<div class="big" style="top:230px;font-size:104px">then pair it with one move.</div>
<div style="position:absolute;left:60px;right:60px;top:600px;font-weight:700;font-size:44px;line-height:1.55">put a real number on "rich af".<br>ask for more, no 3-paragraph apology.<br>plan one money date.</div>`));
// 5 · close + where to go
S.push(shell(5, `<div class="big" style="top:300px;font-size:124px">say it.<br><span style="color:${PINK}">then do<br>one thing.</span></div>
<div style="position:absolute;left:60px;right:60px;top:900px;font-weight:600;font-size:44px;line-height:1.35">40 money affirmations that feel true<br>→ link on this pin</div>
<div style="position:absolute;left:60px;right:60px;top:1150px;font-weight:600;font-size:38px">save this for payday.</div>`));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1000, height: 1500}});
  for (let i = 0; i < S.length; i++) {
    const f = path.join(D, 'M-' + (i + 1) + '.html'); fs.writeFileSync(f, S[i]);
    await p.goto('file://' + f); await p.waitForTimeout(500);
    await p.screenshot({path: path.join(D, 'M-' + (i + 1) + '.png')});
  }
  await b.close(); console.log('ok', S.length);
})();
