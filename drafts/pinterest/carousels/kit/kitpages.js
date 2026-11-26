// Render each page of the real rebrand kit (drafts/issue11-gift/rebrand-kit/kit.html) to PNG, for the kit carousel.
const {chromium} = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({deviceScaleFactor: 2, viewport: {width: 900, height: 1300}});
  await p.goto('file://' + path.resolve(__dirname, '../../../issue11-gift/rebrand-kit/kit.html'), {waitUntil: 'networkidle'});
  await p.waitForTimeout(1200);
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) {
    await pages[i].screenshot({path: path.join(__dirname, 'page-' + String(i + 1).padStart(2, '0') + '.png')});
  }
  console.log('pages', pages.length);
  await b.close();
})();
