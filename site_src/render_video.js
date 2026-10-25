// Rendu image par image de l'ouverture 3D : node site_src/render_video.js <page.html> <dossier> <fps> <durée s>
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const [page, out, fpsS, durS] = process.argv.slice(2);
  const fps = parseInt(fpsS, 10) || 30, dur = parseFloat(durS) || 4.8, n = Math.round(fps * dur);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.error('pageerror', e.message));
  await p.goto('file://' + path.resolve(page) + '?capture=1'); await p.waitForFunction(() => window.__ready);
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    const t = i / fps;
    const data = await p.evaluate(t => { window.__o.render(t); return document.getElementById('c').toDataURL('image/png'); }, t);
    fs.writeFileSync(path.join(out, `f${String(i).padStart(4, '0')}.png`), Buffer.from(data.split(',')[1], 'base64'));
    if (i % 30 === 0) console.log(`frame ${i}/${n}`);
  }
  console.log(`${n} frames in ${((Date.now() - t0) / 1000).toFixed(1)} s`);
  await b.close();
})();
