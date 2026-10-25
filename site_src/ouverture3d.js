/* Clixite, ouverture 3D du mot-marque. WebGL2 sans dépendance.
   Géométrie : charte/assets/scene.json (exportée par build_scene.py depuis le générateur du logo).
   Usage : const o = new ClixiteOuverture(canvas, scene, { theme: 'encre' | 'papier', follow: true });
           o.play(); o.replay(); o.setTime(t); o.render(); */
(function (global) {
  'use strict';
  var COL = {
    encre: [0.043, 0.133, 0.224], papier: [0.965, 0.961, 0.941], turquoise: [0.098, 0.702, 0.851],
    rose: [1.0, 0.310, 0.545], signal: [1.0, 0.824, 0.2], brume: [0.804, 0.835, 0.867],
    encreTeintee: [0.122, 0.227, 0.353], chantClair: [0.165, 0.290, 0.439], turquoiseTexte: [0.047, 0.471, 0.576], ardoise: [0.294, 0.353, 0.420]
  };
  var EASE = function (x) { return 1 - Math.pow(1 - x, 3); };          // ease-out cubique, proche de cubic-bezier(.2,.8,.2,1)
  var EXPO = function (x) { return x >= 1 ? 1 : 1 - Math.pow(2, -10 * x); };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var seg = function (t, a, b) { return clamp((t - a) / (b - a), 0, 1); };

  var VS = [
    '#version 300 es', 'precision highp float;',
    'in vec3 aPos; in vec3 aNrm;',
    'uniform mat3 uRot; uniform vec2 uCentre; uniform vec2 uExt; uniform float uChant; uniform vec2 uScale; uniform vec2 uOffset; uniform vec2 uShift; uniform vec2 uPivot; uniform float uPivotScale;',
    'out vec3 vWorld; out vec3 vNrm;',
    'void main(){',
    '  vec3 p = aPos + vec3(uShift, 0.0);',
    '  p.xy = uPivot + (p.xy - uPivot) * uPivotScale;',
    '  vec3 c = vec3(uCentre, 0.0);',
    '  vec3 r = uRot * (p - c) + c;',              // parallaxe : rotation légère autour du centre du mot
    '  vWorld = aPos; vNrm = uRot * aNrm;',
    '  vec2 s = r.xy - r.z * uExt * uChant;',       // projection oblique : z négatif file vers le bas-droite (le chant)
    '  vec2 clip = (s - uOffset) * uScale;',
    '  gl_Position = vec4(clip.x, -clip.y, -r.z * 0.0005, 1.0);',
    '}'].join('\n');

  var FS_FLAT = [
    '#version 300 es', 'precision highp float;',
    'in vec3 vWorld; in vec3 vNrm; uniform vec3 uColor; uniform float uAlpha; out vec4 o;',
    'void main(){ o = vec4(uColor, uAlpha); }'].join('\n');

  var FS_GLOW = [
    '#version 300 es', 'precision highp float;',
    'in vec3 vWorld; in vec3 vNrm; uniform vec2 uXC; uniform float uT; uniform vec3 uColor; uniform float uAlpha; out vec4 o;',
    'void main(){',
    '  vec2 q = vWorld.xy - uXC; float dd = (abs(q.x) + abs(q.y)) / (uT * 0.70710678);',
    '  float a = (1.0 - smoothstep(0.85, 2.2, dd)) * (1.0 - smoothstep(0.85, 2.2, dd));',
    '  o = vec4(uColor, a * uAlpha);',
    '}'].join('\n');

  var FS_SIDE = [
    '#version 300 es', 'precision highp float;',
    'in vec3 vWorld; in vec3 vNrm; uniform vec3 uColor; uniform vec3 uColor2; uniform float uSweep; uniform vec2 uBox; uniform float uAlpha; out vec4 o;',
    'void main(){',
    '  vec3 L = normalize(vec3(-0.45, -0.75, 0.5));',
    '  float d = max(0.0, dot(normalize(vNrm), L));',
    '  vec3 c = mix(uColor, uColor2, d * 0.9);',
    '  float sx = uBox.x + (uBox.y - uBox.x) * uSweep;',               // balayage de lumière le long du chant
    '  float band = 1.0 - smoothstep(0.0, uBox.y * 0.0 + 90.0, abs(vWorld.x - vWorld.y * 0.35 - sx));',
    '  c = mix(c, uColor2 * 1.35, band * 0.6 * step(0.001, uSweep) * step(uSweep, 0.999));',
    '  o = vec4(c, uAlpha);',
    '}'].join('\n');

  var FS_FACE = [
    '#version 300 es', 'precision highp float;',
    'in vec3 vWorld; in vec3 vNrm; out vec4 o;',
    'uniform vec2 uXC; uniform float uT; uniform float uPitch; uniform float uAngle; uniform float uSlide; uniform float uFields; uniform float uLens; uniform float uGlow;',
    'uniform vec3 uFace; uniform vec3 uTurq; uniform vec3 uRose; uniform vec3 uSignal;',
    'float lineMask(vec2 q, float rot, float off, float lw){',
    '  float cr = cos(rot), sr = sin(rot);',
    '  float x = q.x * cr + q.y * sr + off;',                            // rotation de -rot (repère y vers le haut)
    '  float m = mod(x + uPitch * 0.5, uPitch) - uPitch * 0.5;',
    '  float aa = fwidth(x) * 0.8;',
    '  return 1.0 - smoothstep(lw * 0.5 - aa, lw * 0.5 + aa, abs(m));',
    '}',
    'void main(){',
    '  vec2 q = vec2(vWorld.x - uXC.x, -(vWorld.y - uXC.y));',          // repère y vers le haut, centré sur le X
    '  float dA = abs(q.x - q.y) * 0.70710678;',                        // barre turquoise : bas-gauche vers haut-droite (ligne y = x, y vers le haut)
    '  float dB = abs(q.x + q.y) * 0.70710678;',                        // barre rose : haut-gauche vers bas-droite (ligne y = -x)
    '  float inA = step(dA, uT * 0.5), inB = step(dB, uT * 0.5);',
    '  float both = inA * inB;',
    '  float lw = uPitch * 0.5;',
    '  float ha = radians(uAngle) * 0.5;',
    '  float off = uSlide * uT * 4.0;',
    '  vec2 qa = q + vec2(off, off); vec2 qb = q - vec2(off, off);',   // les champs arrivent des coins
    '  float mA = lineMask(qa, -ha, 0.0, lw) * inA;',
    '  float mB = lineMask(qb, ha, uPitch * 0.5, lw * mix(1.0, 0.7, both)) * inB;',
    '  vec3 base = mix(uFace, uSignal, both * uLens);',
    '  base += uSignal * both * uGlow * 0.25;',
    '  vec3 c = mix(base, uTurq, mA * uFields);',
    '  c = mix(c, uRose, mB * uFields);',
    '  o = vec4(c, 1.0);',
    '}'].join('\n');

  function compile(gl, type, src) {
    var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    return s;
  }
  function program(gl, fs) {
    var p = gl.createProgram(); gl.attachShader(p, compile(gl, gl.VERTEX_SHADER, VS)); gl.attachShader(p, compile(gl, gl.FRAGMENT_SHADER, fs)); gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    var u = {}; var n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
    for (var i = 0; i < n; i++) { var info = gl.getActiveUniform(p, i); u[info.name] = gl.getUniformLocation(p, info.name); }
    return { p: p, u: u };
  }
  function mesh(gl, pos, idx, nrm, stride) {
    var vao = gl.createVertexArray(); gl.bindVertexArray(vao);
    var pb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, pb); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(pos), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, stride, gl.FLOAT, false, 0, 0);
    if (nrm) { var nb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, nb); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(nrm), gl.STATIC_DRAW); gl.enableVertexAttribArray(1); gl.vertexAttribPointer(1, 3, gl.FLOAT, false, 0, 0); }
    else { gl.disableVertexAttribArray(1); gl.vertexAttrib3f(1, 0, 0, 1); }
    var ib = gl.createBuffer(); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint32Array(idx), gl.STATIC_DRAW);
    gl.bindVertexArray(null);
    return { vao: vao, n: idx.length };
  }

  function ClixiteOuverture(canvas, scene, opts) {
    opts = opts || {};
    this.canvas = canvas; this.scene = scene; this.theme = opts.theme || 'encre';
    this.follow = opts.follow !== false; this.loop = opts.loop !== false;
    this.reduce = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var gl = this.gl = canvas.getContext('webgl2', { antialias: true, alpha: false, preserveDrawingBuffer: !!opts.preserve, premultipliedAlpha: false });
    if (!gl) throw new Error('WebGL2 indisponible');
    this.progFlat = program(gl, FS_FLAT); this.progSide = program(gl, FS_SIDE); this.progFace = program(gl, FS_FACE); this.progGlow = program(gl, FS_GLOW);
    var s = scene;
    this.m = {
      left: mesh(gl, s.left.pos, s.left.idx, null, 2), right: mesh(gl, s.right.pos, s.right.idx, null, 2), desc: mesh(gl, s.desc.pos, s.desc.idx, null, 2),
      face: mesh(gl, s.face.pos, s.face.idx, null, 2), lens: mesh(gl, s.lens.pos, s.lens.idx, null, 2), sides: mesh(gl, s.sides.pos, s.sides.idx, s.sides.nrm, 3)
    };
    var gc = s.x.centre, gr = s.x.t * 2.0;
    this.m.glow = mesh(gl, [gc[0] - gr, gc[1] - gr, gc[0] + gr, gc[1] - gr, gc[0] + gr, gc[1] + gr, gc[0] - gr, gc[1] + gr], [0, 1, 2, 0, 2, 3], null, 2);
    this.pointer = null; this.rx = 0; this.ry = 0; this.t = 0; this.playing = false; this.t0 = 0; this.phaseCb = opts.onPhase || null;
    this.margin = opts.margin || 0.12;
    var self = this;
    if (this.follow) {
      var host = opts.host || canvas;
      host.addEventListener('pointermove', function (e) { var r = host.getBoundingClientRect(); self.pointer = [clamp(((e.clientX - r.left) / r.width - 0.5) * 2, -1, 1), clamp(((e.clientY - r.top) / r.height - 0.5) * 2, -1, 1)]; });
      host.addEventListener('pointerleave', function () { self.pointer = null; });
    }
    this.resize();
    if (global.ResizeObserver) new ResizeObserver(function () { self.resize(); if (!self.playing) self.render(); }).observe(canvas);
  }
  ClixiteOuverture.prototype.resize = function () {
    var dpr = Math.min(global.devicePixelRatio || 1, 2);
    var w = Math.max(1, Math.round(this.canvas.clientWidth * dpr)), h = Math.max(1, Math.round(this.canvas.clientHeight * dpr));
    if (this.canvas.width !== w || this.canvas.height !== h) { this.canvas.width = w; this.canvas.height = h; }
    this.gl.viewport(0, 0, w, h);
    // ajuster le mot-marque dans le canevas, en gardant la marge ; unités scène -> clip
    var s = this.scene, aspect = w / h, W = s.width, H = s.height;
    var fitW = (1 - this.margin * 2) * 2, fitH = (1 - this.margin * 2) * 2;
    var k = Math.min(fitW / W, fitH / (H * aspect));            // clip units per scene unit (x)
    this.scale = [k, k * aspect]; this.offset = [W / 2, H / 2];
  };
  /* ---- chronologie (secondes) ---- */
  ClixiteOuverture.prototype.state = function (t) {
    var st = {};
    var slide = 1 - EXPO(seg(t, 0.0, 0.9));
    st.slide = slide; st.fields = EASE(seg(t, 0.0, 0.5));
    var ang = 14 - 10 * EASE(seg(t, 0.7, 2.0));
    if (t > 3.2) ang = 4 + 1.0 * (1 - Math.cos((t - 3.2) / 6 * Math.PI * 2)) / 2 * 2;   // respiration 4° à 6°
    st.angle = ang;
    st.lens = EASE(seg(t, 1.2, 1.9));
    st.glow = t > 1.2 ? (0.6 * (1 - EASE(seg(t, 1.9, 2.6))) + 0.08 * (1 + Math.sin(t * 1.3)) * EASE(seg(t, 2.6, 3.2))) : 0;
    st.chant = EASE(seg(t, 2.0, 2.6));
    st.sweep = seg(t, 2.05, 2.9);
    st.letters = EASE(seg(t, 2.7, 3.2));
    st.desc = EASE(seg(t, 3.15, 3.65));
    st.zoomP = EASE(seg(t, 2.3, 3.1));              // zoom arrière : du X seul vers le mot-marque
    return st;
  };
  ClixiteOuverture.prototype.setTime = function (t) { this.t = t; };
  ClixiteOuverture.prototype.render = function (t) {
    if (t !== undefined) this.t = t;
    var gl = this.gl, s = this.scene, st = this.reduce ? this.state(10) : this.state(this.t);
    if (this.reduce) st.angle = 8;
    // parallaxe au pointeur, interpolée avec inertie
    var tx = this.pointer ? this.pointer[1] * 5 : 0, ty = this.pointer ? -this.pointer[0] * 7 : 0;
    if (this.reduce) { tx = 0; ty = 0; }
    this.rx += (tx - this.rx) * 0.06; this.ry += (ty - this.ry) * 0.06;
    var rx = this.rx * Math.PI / 180, ry = this.ry * Math.PI / 180;
    var cx = Math.cos(rx), sx = Math.sin(rx), cy = Math.cos(ry), sy = Math.sin(ry);
    // Ry * Rx, colonne-major
    var rot = [cy, 0, -sy, sx * sy, cx, sx * cy, cx * sy, -sx, cx * cy];
    var dark = this.theme === 'encre';
    var bg = dark ? COL.encre : COL.papier;
    gl.clearColor(bg[0], bg[1], bg[2], 1); gl.enable(gl.DEPTH_TEST); gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    var ext = [s.x.ext[0] / s.x.depth, s.x.ext[1] / s.x.depth];
    var self = this;
    var zoom = 1 + 1.8 * (1 - st.zoomP);
    var off = [s.x.centre[0] + (s.width / 2 - s.x.centre[0]) * st.zoomP, s.x.centre[1] + (s.height / 2 - s.x.centre[1]) * st.zoomP];
    var scl = [this.scale[0] * zoom, this.scale[1] * zoom];
    function common(pr, shift) {
      gl.useProgram(pr.p);
      gl.uniformMatrix3fv(pr.u.uRot, false, rot); gl.uniform2f(pr.u.uCentre, s.width / 2, s.height / 2);
      gl.uniform2f(pr.u.uExt, ext[0], ext[1]); gl.uniform1f(pr.u.uChant, st.chant);
      gl.uniform2f(pr.u.uScale, scl[0], scl[1]); gl.uniform2f(pr.u.uOffset, off[0], off[1]);
      gl.uniform2f(pr.u.uShift, shift ? shift[0] : 0, shift ? shift[1] : 0);
      gl.uniform2f(pr.u.uPivot, s.x.centre[0], s.x.centre[1]); gl.uniform1f(pr.u.uPivotScale, 1.0);
    }
    function draw(m) { gl.bindVertexArray(m.vao); gl.drawElements(gl.TRIANGLES, m.n, gl.UNSIGNED_INT, 0); }
    // lettres
    var ink = dark ? COL.papier : COL.encre, pf = this.progFlat;
    common(pf, [-(1 - st.letters) * 140, 0]); gl.uniform3fv(pf.u.uColor, ink); gl.uniform1f(pf.u.uAlpha, st.letters); if (st.letters > 0) draw(this.m.left);
    common(pf, [(1 - st.letters) * 140, 0]); if (st.letters > 0) draw(this.m.right);
    common(pf, [0, 0]); gl.uniform3fv(pf.u.uColor, dark ? COL.turquoise : COL.turquoiseTexte); gl.uniform1f(pf.u.uAlpha, st.desc); if (st.desc > 0) draw(this.m.desc);
    // chant
    var ps = this.progSide; common(ps, [0, 0]);
    gl.uniform3fv(ps.u.uColor, dark ? COL.encreTeintee : COL.encre); gl.uniform3fv(ps.u.uColor2, dark ? COL.chantClair : COL.encreTeintee);
    gl.uniform1f(ps.u.uSweep, st.sweep); gl.uniform2f(ps.u.uBox, s.x.box[0], s.x.box[0] + s.x.box[2]); gl.uniform1f(ps.u.uAlpha, 1.0);
    if (st.chant > 0.001) draw(this.m.sides);
    // face du X
    var pfc = this.progFace; common(pfc, [0, 0]);
    gl.uniform2f(pfc.u.uXC, s.x.centre[0], s.x.centre[1]); gl.uniform1f(pfc.u.uT, s.x.t); gl.uniform1f(pfc.u.uPitch, s.x.pitch);
    gl.uniform1f(pfc.u.uAngle, st.angle); gl.uniform1f(pfc.u.uSlide, st.slide); gl.uniform1f(pfc.u.uFields, st.fields);
    gl.uniform1f(pfc.u.uLens, st.lens); gl.uniform1f(pfc.u.uGlow, st.glow);
    gl.uniform3fv(pfc.u.uFace, dark ? COL.encre : COL.papier); gl.uniform3fv(pfc.u.uTurq, COL.turquoise); gl.uniform3fv(pfc.u.uRose, COL.rose); gl.uniform3fv(pfc.u.uSignal, COL.signal);
    draw(this.m.face);
    // halo de la lentille : la pièce Signal, agrandie, en fondu additif, le temps de l'allumage
    if (st.glow > 0.02) {
      var pg = this.progGlow; gl.depthMask(false); gl.blendFunc(gl.SRC_ALPHA, gl.ONE);
      common(pg, [0, 0]); gl.uniform2f(pg.u.uXC, s.x.centre[0], s.x.centre[1]); gl.uniform1f(pg.u.uT, s.x.t);
      gl.uniform3fv(pg.u.uColor, COL.signal); gl.uniform1f(pg.u.uAlpha, st.glow * (dark ? 0.55 : 0.35)); draw(this.m.glow);
      gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA); gl.depthMask(true);
    }
    if (this.phaseCb) this.phaseCb(this.t, st);
  };
  ClixiteOuverture.prototype.play = function () {
    var self = this; this.playing = true; this.t0 = performance.now() - this.t * 1000;
    function frame(now) {
      if (!self.playing) return;
      self.t = (now - self.t0) / 1000; self.render();
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  };
  ClixiteOuverture.prototype.replay = function () { this.t = 0; this.t0 = performance.now(); if (!this.playing) this.play(); };
  ClixiteOuverture.prototype.stop = function () { this.playing = false; };
  global.ClixiteOuverture = ClixiteOuverture;
})(window);
