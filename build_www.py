"""Page d'accueil www.clixite.be : « la table à dessin ». Produit www/ (autonome) et clixite-www.zip."""
import os, shutil, zipfile
W = "www"; shutil.rmtree(W, ignore_errors=True); os.makedirs(f"{W}/assets"); os.makedirs(f"{W}/fonts")
for f in ("ouverture3d.js", "scene.json"): shutil.copy(f"charte/assets/{f}", f"{W}/assets/{f}")
for f in ("space-grotesk-500-normal", "space-grotesk-700-normal", "inter-400-normal", "inter-500-normal", "fraunces-500-italic", "fraunces-600-italic", "jetbrains-mono-500-normal"):
    shutil.copy(f"charte/fonts/{f}.woff2", f"{W}/fonts/{f}.woff2")
for f in ("favicon.svg", "favicon.ico", "app-icon-180.png", "app-icon-192.png", "app-icon-512.png", "site.webmanifest"):
    shutil.copy(f"charte/downloads/favicons/{f}", f"{W}/{f}")
shutil.copy("charte/downloads/reseaux/og-image-1200x630.png", f"{W}/og-image-1200x630.png")
shutil.copy("charte/downloads/logo/clixite-relief-inverse-transparent.svg", f"{W}/assets/clixite.svg")
shutil.copy("charte/downloads/logo/clixite-maitre-inverse-transparent.svg", f"{W}/assets/clixite-petit.svg")
shutil.copy("charte/downloads/logo/x-relief-color-transparent.svg", f"{W}/assets/x.svg")
shutil.copy("charte/downloads/logo/x-relief-inverse-transparent.svg", f"{W}/assets/x-inverse.svg")

html = r'''<!doctype html>
<html lang="fr-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clixite</title>
<meta name="description" content="Clixite, Enterprise & Solution Architecture. Nicolas Simon, Wavre. Nous résolvons votre x : la structure d'abord, puis ce qui tourne.">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.ico" sizes="any"><link rel="apple-touch-icon" href="app-icon-180.png"><link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#0B2239">
<meta property="og:title" content="Clixite"><meta property="og:description" content="Enterprise & Solution Architecture. Nous résolvons votre x."><meta property="og:image" content="https://www.clixite.be/og-image-1200x630.png"><meta property="og:url" content="https://www.clixite.be/"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Clixite SRL","alternateName":"Clixite","url":"https://www.clixite.be/","logo":"https://www.clixite.be/og-image-1200x630.png","description":"Enterprise & Solution Architecture pour les organisations régulées et les PME en croissance.","founder":{"@type":"Person","name":"Nicolas Simon","jobTitle":"Solutions & Enterprise Architect","sameAs":"https://www.linkedin.com/in/nicolassim/"},"address":{"@type":"PostalAddress","streetAddress":"Avenue Reine Astrid 53","postalCode":"1300","addressLocality":"Wavre","addressCountry":"BE"},"vatID":"BE0871430776","email":"nicolas@clixite.be","foundingDate":"2005","sameAs":["https://www.linkedin.com/in/nicolassim/"]}</script>
<style>
@font-face{font-family:'Space Grotesk';font-weight:500;font-display:swap;src:url(fonts/space-grotesk-500-normal.woff2) format('woff2')}
@font-face{font-family:'Space Grotesk';font-weight:700;font-display:swap;src:url(fonts/space-grotesk-700-normal.woff2) format('woff2')}
@font-face{font-family:'Inter';font-weight:400;font-display:swap;src:url(fonts/inter-400-normal.woff2) format('woff2')}
@font-face{font-family:'Inter';font-weight:500;font-display:swap;src:url(fonts/inter-500-normal.woff2) format('woff2')}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:500;font-display:swap;src:url(fonts/fraunces-500-italic.woff2) format('woff2')}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:600;font-display:swap;src:url(fonts/fraunces-600-italic.woff2) format('woff2')}
@font-face{font-family:'JetBrains Mono';font-weight:500;font-display:swap;src:url(fonts/jetbrains-mono-500-normal.woff2) format('woff2')}
:root{--encre:#0B2239;--papier:#F6F5F0;--turquoise:#19B3D9;--turquoise-texte:#0C7893;--rose:#FF4F8B;--signal:#FFD233;--brume:#CDD5DD;--ardoise:#4B5A6B;--encre-teintee:#1F3A5A;--surface:#122D4A;--ease:cubic-bezier(.2,.8,.2,1);--g:clamp(20px,5vw,80px);--mx:50vw;--my:40vh}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--encre);color:var(--papier);font-family:Inter,system-ui,sans-serif;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
::selection{background:var(--encre-teintee);color:var(--papier)}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:5px;text-decoration-color:var(--turquoise)}
:focus-visible{outline:2px solid var(--turquoise);outline-offset:4px;border-radius:4px}
h1,h2{margin:0;font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-.02em;line-height:1.02;text-wrap:balance}
p{margin:0 0 1em;max-width:58ch;text-wrap:pretty}
.mono{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.06em;color:var(--brume)}
/* la table : grille de plan et lampe qui suit le curseur */
.table{position:fixed;inset:0;z-index:0;pointer-events:none;background-image:linear-gradient(rgba(205,213,221,.075) 1px,transparent 1px),linear-gradient(90deg,rgba(205,213,221,.075) 1px,transparent 1px),linear-gradient(rgba(205,213,221,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(205,213,221,.04) 1px,transparent 1px);background-size:160px 160px,160px 160px,32px 32px,32px 32px;background-position:-1px -1px}
.table::after{content:"";position:absolute;inset:0;background:radial-gradient(520px circle at var(--mx) var(--my),rgba(25,179,217,.13),rgba(25,179,217,.04) 40%,transparent 70%);transition:opacity .4s ease}
.page{position:relative;z-index:1}
/* en-tête */
.top{position:sticky;top:0;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:18px var(--g);backdrop-filter:blur(6px);background:linear-gradient(rgba(11,34,57,.85),rgba(11,34,57,0))}
.top img{height:26px;width:auto}
.top nav{display:flex;gap:26px;font-size:14px}
.top nav a{text-decoration:none;color:var(--brume);padding:6px 0;border-bottom:1px solid transparent;transition:color .2s ease,border-color .2s ease}
@media (hover:hover){.top nav a:hover{color:var(--papier);border-color:var(--turquoise)}}
@media (max-width:720px){.top nav a:not(.keep){display:none}}
/* feuilles */
.sheet{position:relative;padding:calc(var(--g) * 1.2) var(--g);max-width:1440px;margin:0 auto}
.cote{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.cote .n{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;color:var(--turquoise)}
.cote .l{flex:0 0 auto;width:0;height:1px;background:var(--turquoise);transition:width 1.2s var(--ease)}
.cote .l::before,.cote .l::after{content:"";position:absolute;width:1px;height:9px;background:var(--turquoise);margin-top:-4px}
.cote .l::after{right:0}
.sheet.on .cote .l{width:120px}
.cote .t{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;color:var(--ardoise)}
/* 01 ouverture */
.hero{min-height:calc(100vh - 62px);display:grid;grid-template-rows:auto 1fr auto;padding-top:8px}
.o3d-wrap{width:min(100%,1120px);margin:0 auto;cursor:crosshair;position:relative}
canvas.o3d{display:block;width:100%;aspect-ratio:3/1;touch-action:none}
.o3d-fallback{width:min(100%,720px);margin:0 auto}
[hidden]{display:none!important}
.claim{align-self:end;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:32px 56px;align-items:end;padding-bottom:12px}
.claim h1{font-family:Fraunces,Georgia,serif;font-style:italic;font-weight:500;font-size:clamp(40px,6.2vw,92px);letter-spacing:-.01em;line-height:1.02}
.claim h1 .x{position:relative;display:inline-block;color:var(--signal);font:inherit;font-weight:600;background:none;border:0;padding:0;margin:0;cursor:pointer;white-space:nowrap;transition:opacity .22s ease}
.claim h1 .x.swap{opacity:0}
.claim h1 .x::after{content:"";position:absolute;left:0;right:0;bottom:-.06em;height:2px;background:var(--signal);opacity:.0;transition:opacity .3s ease}
@media (hover:hover){.claim h1 .x:hover::after{opacity:.6}}
.claim .side{font-size:17px;color:var(--brume);max-width:40ch;padding-bottom:.6em}
.claim .side b{display:block;color:var(--papier);font-family:'Space Grotesk',sans-serif;font-weight:500;font-size:19px;margin-bottom:8px;letter-spacing:-.01em}
.claim .side .mono{display:block;margin-top:14px}
.scrollhint{display:flex;justify-content:center;padding:18px 0 0}
.scrollhint span{width:1px;height:34px;background:linear-gradient(var(--turquoise),transparent)}
@media (max-width:860px){.claim{grid-template-columns:1fr}.claim .side{padding-bottom:0}}
/* 02 terrains : comparateur à glisser */
.terrains{margin-top:12px}
.compare{position:relative;height:clamp(420px,62vh,620px);border-radius:14px;overflow:hidden;border:1px solid var(--encre-teintee);user-select:none;touch-action:pan-y}
.pane{position:absolute;inset:0;padding:clamp(24px,4vw,56px);display:flex;flex-direction:column;justify-content:flex-end}
.pane h2{font-size:clamp(26px,3vw,44px);margin-bottom:14px;max-width:min(46%,16ch)}
.pane p{font-size:17px;max-width:min(46%,40ch);margin-bottom:12px}
.pane .tags{max-width:46%}
.pane.pme h2,.pane.pme p,.pane.pme .tags{margin-left:auto}
.pane .tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.pane .tags span{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding:6px 10px;border-radius:999px;border:1px solid currentColor;opacity:.8}
.pane.regule{background:var(--surface);color:var(--papier)}
.pane.regule .tags span{color:var(--turquoise)}
.pane.pme{background:var(--papier);color:var(--encre);clip-path:inset(0 0 0 var(--cut,50%));align-items:flex-end;text-align:right}
.pane.pme .tags{justify-content:flex-end}
.pane.pme .tags span{color:var(--turquoise-texte)}
.pane .k{position:absolute;top:clamp(20px,3vw,40px);font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em}
.pane.regule .k{left:clamp(24px,4vw,56px);color:var(--turquoise)}
.pane.pme .k{right:clamp(24px,4vw,56px);color:var(--turquoise-texte)}
.handle{position:absolute;top:0;bottom:0;left:var(--cut,50%);width:0;z-index:3}
.handle::before{content:"";position:absolute;top:0;bottom:0;left:-1px;width:2px;background:var(--signal)}
.handle .knob{position:absolute;top:50%;left:0;transform:translate(-50%,-50%);width:56px;height:56px;border-radius:50%;background:var(--encre);border:2px solid var(--signal);display:flex;align-items:center;justify-content:center;cursor:ew-resize;box-shadow:none;transition:transform 160ms var(--ease)}
.handle .knob:active{transform:translate(-50%,-50%) scale(.95)}
.handle .knob img{width:26px;height:26px}
.compare .note{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);z-index:4;font-size:12px;color:var(--brume);background:rgba(11,34,57,.7);padding:6px 12px;border-radius:999px;pointer-events:none;transition:opacity .4s ease}
.compare.moved .note{opacity:0}
@media (max-width:720px){.compare{height:auto;min-height:0}.pane{position:relative;clip-path:none!important;padding:24px 20px 28px}.pane h2,.pane p{max-width:100%;font-size:24px}.pane p{font-size:15px}.pane.pme h2,.pane.pme p{text-align:left;margin-left:0}.pane.pme{align-items:flex-start;text-align:left}.pane .tags{display:none}.pane .k{position:static;display:block;margin-bottom:60px}.handle,.compare .note{display:none}}
/* 03 preuves */
.proof{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--encre-teintee);border:1px solid var(--encre-teintee);border-radius:14px;overflow:hidden}
.proof > div{background:var(--encre);padding:clamp(22px,3vw,40px) clamp(20px,2.6vw,32px);min-height:220px;display:flex;flex-direction:column;justify-content:space-between;gap:24px}
.proof .big{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:clamp(40px,4.6vw,64px);letter-spacing:-.03em;line-height:1;font-variant-numeric:tabular-nums}
.proof .big small{display:block;font-family:Inter,sans-serif;font-weight:400;font-size:15px;letter-spacing:0;color:var(--brume);margin-top:10px;line-height:1.4}
.proof .big .lens{display:inline-block;width:.32em;height:.32em;background:var(--signal);transform:rotate(45deg);margin-right:.22em;vertical-align:.08em}
.proof .who{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.06em;color:var(--ardoise);line-height:1.7}
@media (max-width:980px){.proof{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.proof{grid-template-columns:1fr}.proof > div{min-height:0}}
/* 04 contact */
.contact{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:40px 64px;align-items:start}
.contact h2{font-size:clamp(34px,4.6vw,64px);margin-bottom:22px}
.contact p{color:var(--brume)}
.contact .card{border:1px solid var(--encre-teintee);border-radius:14px;padding:clamp(22px,3vw,36px);display:grid;gap:22px;position:relative;overflow:hidden}
.contact .card img.x{position:absolute;right:-18px;top:-18px;width:120px;opacity:.9}
.contact .card b{display:block;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:22px;letter-spacing:-.01em;margin-bottom:4px}
.contact address{font-style:normal;color:var(--brume);line-height:1.6}
.contact .mono{display:block;margin-top:4px}
.in{display:inline-flex;align-items:center;gap:12px;height:52px;padding:0 24px;border-radius:999px;background:var(--turquoise);color:var(--encre);font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:16px;text-decoration:none;will-change:transform;transition:background .2s ease}
.in svg{width:18px;height:18px;fill:currentColor}
.in:active{transform:scale(.97)!important}
@media (hover:hover) and (pointer:fine){.in:hover{background:#3FC3E3;color:var(--encre)}}
.links{display:flex;flex-wrap:wrap;gap:14px 26px;align-items:center;font-size:15px}
@media (max-width:860px){.contact{grid-template-columns:1fr}}
@media (max-width:520px){.contact .card img.x{width:72px;right:-10px;top:-10px;opacity:.6}.cote .t{display:none}}
/* pied */
.foot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;padding:28px var(--g) 34px;border-top:1px solid var(--encre-teintee);max-width:1440px;margin:40px auto 0;color:var(--ardoise);font-size:13px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.cote .l{transition:none;width:120px}.claim h1 .x{transition:none}.table::after{display:none}}
</style>
</head>
<body>
<div class="table" aria-hidden="true"></div>
<div class="page">
<header class="top"><a href="#top" aria-label="Clixite"><img src="assets/clixite-petit.svg" alt="Clixite" width="94" height="26"></a><nav><a href="#terrains">Deux terrains</a><a href="#preuves">Preuves</a><a href="#contact" class="keep">Contact</a><a href="https://charte.clixite.be/" class="keep">La charte</a></nav></header>

<section class="sheet hero on" id="top">
  <div class="cote"><span class="n">FEUILLE 01</span><span class="l"></span><span class="t">ENTERPRISE &amp; SOLUTION ARCHITECTURE · WAVRE</span></div>
  <div class="o3d-wrap" id="stage"><canvas class="o3d" id="o3d" aria-label="Clixite, mot-marque en relief"></canvas><img class="o3d-fallback" src="assets/clixite.svg" alt="Clixite" hidden></div>
  <div class="claim">
    <h1>Nous résolvons votre <button class="x" id="x" type="button" aria-label="Votre x : cliquer pour voir des exemples">x</button>.</h1>
    <div class="side"><b>Le x, c'est l'inconnue de votre organisation.</b>Une policy achats qui ne tient pas l'audit, un back-office qui ne suit plus, une exigence DORA à traduire en preuves. Clixite dessine la structure, puis construit ce qui tourne.<span class="mono">DEPUIS 2005 · NICOLAS SIMON · <span id="hint">CLIQUEZ SUR LE X</span></span></div>
  </div>
  <div class="scrollhint" aria-hidden="true"><span></span></div>
</section>

<section class="sheet terrains" id="terrains">
  <div class="cote"><span class="n">FEUILLE 02</span><span class="l"></span><span class="t">DEUX TERRAINS, UN MÊME MÉTIER · GLISSEZ</span></div>
  <div class="compare" id="compare">
    <div class="pane regule"><span class="k">GRANDS COMPTES RÉGULÉS</span><h2>La conformité qui tient à l'audit.</h2><p>Banque, assurance, télécom. Procurement, conformité, architecture d'entreprise : des exigences traduites en processus, en responsables et en preuves.</p><div class="tags"><span>Procurement</span><span>DORA · NIS2</span><span>Source-to-Pay</span><span>Fractional CPO</span></div></div>
    <div class="pane pme"><span class="k">PME EN CROISSANCE</span><h2>La croissance qui ne casse pas l'outil.</h2><p>Audit, choix et connexion des outils existants, automatisation, IA là où elle fait gagner du temps. Architecturer la croissance avec ce qui existe déjà.</p><div class="tags"><span>Back-office</span><span>Automatisation</span><span>Agents IA</span><span>Build</span></div></div>
    <div class="handle" id="handle"><button class="knob" type="button" aria-label="Glisser pour comparer les deux terrains"><img src="assets/x-inverse.svg" alt=""></button></div>
    <div class="note">Glissez le X</div>
  </div>
</section>

<section class="sheet" id="preuves">
  <div class="cote"><span class="n">FEUILLE 03</span><span class="l"></span><span class="t">PREUVES, PAS ADJECTIFS</span></div>
  <div class="proof">
    <div><div class="big"><span class="lens"></span>800 M€<small>d'achats pilotés, policy et sourcing en production</small></div><div class="who">PROXIMUS</div></div>
    <div><div class="big">v2.0<small>Procurement Policy et Tactical Sourcing Light Track, en production</small></div><div class="who">KBC</div></div>
    <div><div class="big">2005<small>vingt et un ans de structure, de l'agence à l'architecture</small></div><div class="who">CLIXITE · WAVRE</div></div>
    <div><div class="big">4<small>produits et plateformes conçus et codés</small></div><div class="who">TERO · DESIGN PLUS<br>CYGAP · VIDANGO</div></div>
  </div>
</section>

<section class="sheet contact" id="contact">
  <div>
    <div class="cote"><span class="n">FEUILLE 04</span><span class="l"></span><span class="t">UN PREMIER ÉCHANGE</span></div>
    <h2>Trente minutes suffisent pour cadrer votre <em style="font-family:Fraunces,serif;font-style:italic;font-weight:600;color:var(--signal)">x</em>.</h2>
    <p>Pas de slides pour les slides. On regarde votre situation, on nomme l'inconnue, on dit ce qui est faisable en douze semaines.</p>
    <div class="links"><a class="in" id="in" href="https://www.linkedin.com/in/nicolassim/" rel="me noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>Nicolas Simon sur LinkedIn</a><a href="mailto:nicolas@clixite.be">nicolas@clixite.be</a></div>
  </div>
  <div class="card"><img class="x" src="assets/x.svg" alt="">
    <div><b>Nicolas Simon</b>Solutions &amp; Enterprise Architect<span class="mono">PMP · PRINCE2 · SAFe · ITIL</span></div>
    <address><b>Clixite SRL</b>Avenue Reine Astrid 53<br>1300 Wavre, Belgique<span class="mono">BE 0871.430.776</span></address>
    <div><a href="https://charte.clixite.be/">La charte graphique Clixite</a></div>
  </div>
</section>

<footer class="foot"><span>Clixite SRL · Wavre · depuis 2005</span><span>Enterprise &amp; Solution Architecture</span></footer>
</div>
<script src="assets/ouverture3d.js" defer></script>
<script>
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches, fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  // lampe d'architecte : suit le curseur
  if (fine && !reduce) document.addEventListener('pointermove', function (e) { document.documentElement.style.setProperty('--mx', e.clientX + 'px'); document.documentElement.style.setProperty('--my', e.clientY + 'px'); }, { passive: true });
  // le x : les inconnues que Clixite résout
  var xs = ['policy achats', 'conformité DORA', 'back-office', 'Source-to-Pay', 'architecture', 'croissance', 'exigence NIS2', 'dette d’outils', 'audit', 'x'];
  var i = -1, x = document.getElementById('x'), hint = document.getElementById('hint'), busy = false;
  x.addEventListener('click', function () {
    if (busy) return; busy = true; i = (i + 1) % xs.length; var v = xs[i];
    x.classList.add('swap'); setTimeout(function () { x.textContent = v; x.classList.remove('swap'); busy = false; }, reduce ? 0 : 200);
    hint.textContent = v === 'x' ? 'ET LE VÔTRE ?' : 'ENCORE';
  });
  // cotes qui se tracent une fois, à l'entrée de chaque feuille
  var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('on'); io.unobserve(en.target); } }); }, { threshold: 0.25 });
  document.querySelectorAll('.sheet:not(.on)').forEach(function (s) { io.observe(s); });
  // comparateur : glisser le X
  var cmp = document.getElementById('compare'), handle = document.getElementById('handle'), drag = false;
  function setCut(px) { var r = cmp.getBoundingClientRect(); var p = Math.max(6, Math.min(94, (px - r.left) / r.width * 100)); cmp.style.setProperty('--cut', p + '%'); cmp.classList.add('moved'); }
  handle.addEventListener('pointerdown', function (e) { drag = true; handle.setPointerCapture(e.pointerId); e.preventDefault(); });
  handle.addEventListener('pointermove', function (e) { if (drag) setCut(e.clientX); });
  handle.addEventListener('pointerup', function () { drag = false; }); handle.addEventListener('pointercancel', function () { drag = false; });
  cmp.addEventListener('click', function (e) { if (e.target.closest('.knob')) return; setCut(e.clientX); });
  handle.querySelector('.knob').addEventListener('keydown', function (e) { var cur = parseFloat(getComputedStyle(cmp).getPropertyValue('--cut')) || 50; if (e.key === 'ArrowLeft') { cmp.style.setProperty('--cut', Math.max(6, cur - 5) + '%'); cmp.classList.add('moved'); } if (e.key === 'ArrowRight') { cmp.style.setProperty('--cut', Math.min(94, cur + 5) + '%'); cmp.classList.add('moved'); } });
  // bouton magnétique
  var btn = document.getElementById('in');
  if (fine && !reduce) {
    btn.addEventListener('pointermove', function (e) { var r = btn.getBoundingClientRect(); var dx = (e.clientX - (r.left + r.width / 2)) / r.width, dy = (e.clientY - (r.top + r.height / 2)) / r.height; btn.style.transform = 'translate(' + (dx * 10) + 'px,' + (dy * 8) + 'px)'; });
    btn.addEventListener('pointerleave', function () { btn.style.transition = 'transform .5s cubic-bezier(.2,.8,.2,1), background .2s ease'; btn.style.transform = ''; setTimeout(function () { btn.style.transition = 'background .2s ease'; }, 500); });
  }
  // ouverture 3D
  function fallback() { var c = document.getElementById('o3d'); c.hidden = true; document.querySelector('.o3d-fallback').hidden = false; }
  function boot(scene) { try { var o = new ClixiteOuverture(document.getElementById('o3d'), scene, { theme: 'encre', host: document.getElementById('stage'), margin: 0.04 }); o.play(); document.getElementById('o3d').addEventListener('dblclick', function () { o.replay(); }); } catch (e) { fallback(); } }
  function start() { if (!window.ClixiteOuverture) return fallback(); fetch('assets/scene.json').then(function (r) { return r.json(); }).then(boot).catch(fallback); }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
</script>
</body>
</html>
'''
open(f"{W}/index.html", "w").write(html)
open(f"{W}/.htaccess", "w").write("AddType image/svg+xml .svg\nAddType font/woff2 .woff2\nAddType application/manifest+json .webmanifest\n<IfModule mod_deflate.c>\n  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/json\n</IfModule>\n<IfModule mod_expires.c>\n  ExpiresActive On\n  ExpiresByType font/woff2 \"access plus 30 days\"\n  ExpiresByType image/png \"access plus 7 days\"\n  ExpiresByType image/svg+xml \"access plus 7 days\"\n</IfModule>\n")
open(f"{W}/robots.txt", "w").write("User-agent: *\nAllow: /\n")
with zipfile.ZipFile("clixite-www.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(W):
        for fn in files: p = os.path.join(root, fn); z.write(p, os.path.relpath(p, W))
print("www ok", sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(W) for f in fs) // 1024, "Ko")
