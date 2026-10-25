"""Animation d'ouverture 3D : page HTML autonome (moteur et géométrie inclus) et rendu vidéo image par image
(Playwright + ffmpeg) : MP4 1080p, WebM, GIF 800 px, affiche. Usage : python3 build_anim.py [--video]"""
import os, sys, json, subprocess, shutil
A = "charte/assets"; OUT = "charte/animation"; os.makedirs(OUT, exist_ok=True)
engine = open("site_src/ouverture3d.js").read()
scene = open(f"{A}/scene.json").read()
html = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clixite, ouverture</title>
<style>
  html,body{{margin:0;height:100%;background:#0B2239;overflow:hidden}}
  body.papier{{background:#F6F5F0}}
  canvas{{display:block;width:100vw;height:100vh;cursor:pointer}}
  .note{{position:fixed;left:16px;bottom:12px;font:12px/1.4 Inter,system-ui,sans-serif;color:#4B5A6B;opacity:.8}}
</style></head>
<body>
<canvas id="c" aria-label="Clixite, Enterprise and Solution Architecture"></canvas>
<div class="note">Clic : rejouer. Touche P : fond Papier ou Encre. Paramètres : ?theme=papier, ?t=2.6 (image fixe), ?loop=0.</div>
<script>{engine}</script>
<script>
(function(){{
  var scene = {scene};
  var q = new URLSearchParams(location.search), theme = q.get('theme') === 'papier' ? 'papier' : 'encre';
  if (theme === 'papier') document.body.classList.add('papier');
  var o = new ClixiteOuverture(document.getElementById('c'), scene, {{ theme: theme, margin: 0.1, preserve: q.has('capture'), follow: !q.has('capture') }});
  window.__o = o;
  if (q.has('t')) {{ o.render(parseFloat(q.get('t'))); }}
  else if (!q.has('capture')) {{ o.play(); }}
  document.getElementById('c').addEventListener('click', function () {{ o.replay(); }});
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'p' || e.key === 'P') {{ o.theme = o.theme === 'encre' ? 'papier' : 'encre'; document.body.classList.toggle('papier', o.theme === 'papier'); o.replay(); }}
    if (e.key === ' ') {{ o.replay(); e.preventDefault(); }}
  }});
  window.__ready = true;
}})();
</script>
</body></html>'''
open(f"{OUT}/clixite-ouverture.html", "w").write(html)
print("html ok", len(html) // 1024, "Ko")

if "--video" in sys.argv:
    frames = "frames3d"; shutil.rmtree(frames, ignore_errors=True); os.makedirs(frames)
    subprocess.run(["node", "site_src/render_video.js", f"{OUT}/clixite-ouverture.html", frames, "30", "4.8"], check=True)
    fps = "30"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", fps, "-i", f"{frames}/f%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "slow", "-movflags", "+faststart", f"{OUT}/clixite-ouverture-1080p.mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", fps, "-i", f"{frames}/f%04d.png", "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "28", "-pix_fmt", "yuv420p", f"{OUT}/clixite-ouverture-1080p.webm"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", fps, "-i", f"{frames}/f%04d.png", "-vf", "fps=20,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=96[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4", f"{OUT}/clixite-ouverture-800.gif"], check=True)
    last = sorted(os.listdir(frames))[-1]
    shutil.copy(f"{frames}/{last}", f"{OUT}/clixite-ouverture-poster.png")
    for f in os.listdir(OUT): print(f, os.path.getsize(f"{OUT}/{f}") // 1024, "Ko")
