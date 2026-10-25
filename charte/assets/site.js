/* charte.clixite.be : X vivant, navigation, copie des valeurs. Aucun framework, aucune dépendance. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- X vivant : angle d'interférence piloté par le curseur ---------- */
  function LivingX(svg, opts) {
    opts = opts || {};
    this.svg = svg;
    this.fa = svg.querySelector('.lx-field-a');
    this.fb = svg.querySelector('.lx-field-b');
    var o = (this.fa.getAttribute('data-origin') || '200 200').split(' ');
    this.cx = parseFloat(o[0]); this.cy = parseFloat(o[1]);
    this.rest = opts.rest || 8;          // angle au repos, en degrés
    this.angle = reduce ? this.rest : 14; // angle de départ (séquence d'ouverture)
    this.target = this.rest;
    this.manual = null;                   // angle imposé par un curseur (atelier)
    this.pointer = null;                  // influence du pointeur, -1..1
    this.t0 = performance.now();
    this.apply(this.angle);
    var self = this;
    if (reduce) { svg.classList.add('is-still'); }
    else { requestAnimationFrame(function () { svg.classList.add('is-on'); }); }
    var host = opts.host || svg;
    if (opts.follow !== false) {
      host.addEventListener('pointermove', function (e) {
        var r = host.getBoundingClientRect();
        self.pointer = Math.max(-1, Math.min(1, ((e.clientX - r.left) / r.width - 0.5) * 2));
      });
      host.addEventListener('pointerleave', function () { self.pointer = null; });
    }
    this.loop();
  }
  LivingX.prototype.apply = function (a) {
    this.fa.setAttribute('transform', 'rotate(' + (-a / 2).toFixed(3) + ' ' + this.cx + ' ' + this.cy + ')');
    this.fb.setAttribute('transform', 'rotate(' + (a / 2).toFixed(3) + ' ' + this.cx + ' ' + this.cy + ')');
  };
  LivingX.prototype.loop = function () {
    var self = this;
    function frame(now) {
      var t = (now - self.t0) / 1000;
      var target;
      if (self.manual !== null) target = self.manual;
      else if (self.pointer !== null) target = self.rest + self.pointer * 9;
      else target = self.rest + (reduce ? 0 : Math.sin(t / 6 * Math.PI * 2) * 1.2);
      if (!reduce && t < 1.6 && self.manual === null) target = 14 - (14 - self.rest) * ease(Math.min(1, Math.max(0, (t - 0.4) / 1.2)));
      self.angle += (target - self.angle) * (self.manual !== null ? 0.25 : 0.08);
      self.apply(self.angle);
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  };
  function ease(x) { return 1 - Math.pow(1 - x, 3); }

  /* ---------- ouverture 3D (hero et chapitre Animation) ---------- */
  function boot3d(scene) {
    var heroC = document.getElementById('hero-3d'), animC = document.getElementById('anim-3d');
    var heroO = null, animO = null;
    try {
      if (heroC) {
        heroO = new ClixiteOuverture(heroC, scene, { theme: 'encre', host: document.getElementById('hero'), margin: 0.05 });
        heroO.play();
        var hr = document.getElementById('hero-replay'); if (hr) hr.addEventListener('click', function () { heroO.replay(); });
      }
    } catch (e) {
      if (heroC) { heroC.hidden = true; var fb = document.querySelector('.o3d-fallback'); if (fb) fb.hidden = false; }
    }
    try {
      if (animC) {
        animO = new ClixiteOuverture(animC, scene, { theme: 'encre', margin: 0.1 });
        animO.setTime(0); animO.render();
        var seen = false, io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting && !seen) { seen = true; animO.replay(); } }); }, { threshold: 0.4 });
        io.observe(animC);
        animC.addEventListener('click', function () { animO.replay(); });
        var rb = document.getElementById('replay'); if (rb) rb.addEventListener('click', function () { animO.replay(); });
        var tb = document.getElementById('anim-theme');
        if (tb) tb.addEventListener('click', function () {
          var dark = animO.theme === 'encre'; animO.theme = dark ? 'papier' : 'encre';
          document.getElementById('anim-stage').style.background = dark ? '#F6F5F0' : '#0B2239';
          tb.textContent = dark ? 'Voir sur Encre' : 'Voir sur Papier'; animO.replay();
        });
      }
    } catch (e) { if (animC) animC.hidden = true; }
  }
  if (window.ClixiteOuverture && (document.getElementById('hero-3d') || document.getElementById('anim-3d'))) {
    fetch('assets/scene.json').then(function (r) { return r.json(); }).then(boot3d).catch(function () {
      var heroC = document.getElementById('hero-3d'); if (heroC) { heroC.hidden = true; var fb = document.querySelector('.o3d-fallback'); if (fb) fb.hidden = false; }
    });
  }
  var play = document.querySelector('.atelier .living-x');
  if (play) {
    var lx = new LivingX(play, { follow: false, rest: 8 });
    var range = document.getElementById('angle'), out = document.getElementById('angle-out');
    function setAngle(v) { lx.manual = parseFloat(v); out.textContent = String(v).replace('.', ',') + '°'; }
    range.addEventListener('input', function () { setAngle(range.value); });
    document.getElementById('angle-reset').addEventListener('click', function () { range.value = 8; setAngle(8); });
    document.getElementById('angle-free').addEventListener('click', function () { lx.manual = null; out.textContent = 'respiration'; });
    setAngle(8);
  }

  /* ---------- navigation : chapitre actif ---------- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.sidenav a[href^="#"], .mobilenav a[href^="#"]'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('section.chapter[id]'));
  function spy() {
    var y = window.scrollY + 140, cur = sections[0] && sections[0].id;
    for (var i = 0; i < sections.length; i++) if (sections[i].offsetTop <= y) cur = sections[i].id;
    links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + cur); });
    var act = document.querySelector('.mobilenav a.active');
    if (act && act.scrollIntoView) act.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
  }
  window.addEventListener('scroll', spy, { passive: true }); spy();

  /* ---------- copie dans le presse-papier ---------- */
  var toast = document.getElementById('toast'), toastT;
  function say(msg) { toast.textContent = msg; toast.classList.add('show'); clearTimeout(toastT); toastT = setTimeout(function () { toast.classList.remove('show'); }, 1600); }
  function copy(text, label) {
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () { say(label + ' copié'); }, function () { say('Copie impossible dans ce navigateur'); });
    else say('Copie impossible dans ce navigateur');
  }
  document.querySelectorAll('.swatch').forEach(function (b) {
    b.addEventListener('click', function () { copy(b.getAttribute('data-hex'), b.getAttribute('data-hex')); });
  });
  document.querySelectorAll('.codeblock .copy').forEach(function (b) {
    b.addEventListener('click', function () { copy(b.parentNode.querySelector('code').textContent, 'Code'); });
  });

})();
