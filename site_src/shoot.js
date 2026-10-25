// Captures du site pour la revue visuelle : node site_src/shoot.js <outdir>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2];
  const url = 'http://127.0.0.1:8765/index.html';
  const browser = await chromium.launch();
  for (const [name, w, h] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2600);
    await page.screenshot({ path: path.join(out, `${name}-hero.png`) });
    // scroll through the page so lazy images and iframes load, then back to top
    const total = await page.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < total; y += h * 0.8) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(120); }
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(800);
    await page.screenshot({ path: path.join(out, `${name}-full.png`), fullPage: true });
    const H = await page.evaluate(() => document.documentElement.scrollHeight);
    console.log(name, 'height', H, 'errors', errors);
    await page.close();
  }
  await browser.close();
})();
