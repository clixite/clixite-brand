"""Animation d'ouverture du X Clixite (3 s) : HTML/SVG autonome + frames pour MP4/GIF."""
import math, os, subprocess
from shapely.geometry import box
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, PAPER, TURQ, ROSE, SIGNAL, INK_TINT
from logos10 import x_geoms, STEM, sweep_of, field, ext_vec
from logos7 import flip
from typo import text_paths, metrics

# ---- shared geometry (one wordmark at 1280x720, dark background) -------------
WM = 190.0
PAD_X = 120.0
m = metrics("space", 700); CAP = m["cap"] / m["upem"] * WM
OVER = 0.05; XS = CAP * (1 + 2 * OVER); STEMPX = STEM * WM; T = 1.08 * STEMPX; GAP = 0.035 * WM
D = 0.30 * T; _ex, _ey = ext_vec(D); DX, DY = _ex, -_ey  # screen: right, down
SHX, SHY = DX / 2, DY / 2
BASE = 300.0 + CAP  # baseline y
LEFT, LW = text_paths("space", 700, "CLI", WM, PAD_X, BASE, tracking=0.06)
X_X = PAD_X + LW + GAP + SHX
X_Y = BASE - CAP - OVER * CAP + SHY
RIGHT, RW = text_paths("space", 700, "ITE", WM, X_X + XS + GAP - SHX, BASE, tracking=0.06)
TOTAL_W = X_X + XS + GAP - SHX + RW - PAD_X
OFFSET_X = (1280 - TOTAL_W) / 2 - PAD_X  # centre the lockup

a_geom, b_geom, centre, joint = x_geoms(XS, T)  # y-up in an XS box
def to_screen(g):  # y-up box coords -> svg (y down) inside the X box, then lift by (-DX,-DY) for the face
    return geom_to_d(g, 1.0, 0, XS)
FACE_A = affinity.translate(a_geom, 0, 0); FACE_B = b_geom
SWEEP = sweep_of(unary_union([a_geom, b_geom]), DX, -DY)  # extrusion down-right in y-up terms
PITCH = T / 10; LWID = PITCH / 2

def desc_paths():
    d_items, d_w = text_paths("space", 500, "ENTERPRISE & SOLUTION ARCHITECTURE", 24.0, PAD_X, BASE + 52 + 24, tracking=0.2)
    k = TOTAL_W / d_w
    d_items, d_w = text_paths("space", 500, "ENTERPRISE & SOLUTION ARCHITECTURE", 24.0 * k, PAD_X, BASE + 52 + 24 * k, tracking=0.2)
    return d_items

def lines_group(color, cls):
    """vertical lines covering the X box generously, to be rotated/clipped."""
    n = int(XS * 1.8 / PITCH)
    out = []
    for k in range(-n, n + 1):
        x = XS / 2 + k * PITCH
        out.append(f'<rect x="{x - LWID/2:.2f}" y="{-XS:.1f}" width="{LWID:.2f}" height="{3*XS:.1f}" fill="{color}"/>')
    return f'<g class="{cls}">{"".join(out)}</g>'

def build_html(path):
    paths = lambda items, col: "".join(f'<path d="{it["d"]}" fill="{col}"/>' for it in items)
    face_a = to_screen(a_geom); face_b = to_screen(b_geom); lens = to_screen(centre); sweep = to_screen(SWEEP)
    html = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Clixite · ouverture</title>
<style>
  html,body{{margin:0;height:100%;background:{INK}}}
  .stage{{width:100%;height:100%;display:flex;align-items:center;justify-content:center}}
  svg{{width:min(100vw,177.8vh);height:auto}}
  /* séquence 3 s : 0 à 0,8 s les champs glissent ; 0,8 à 2 s l'angle se résout et la lentille s'allume ; 2 à 2,6 s le chant tombe ; 2,6 à 3 s les lettres se posent */
  .fieldA{{transform-origin:{XS/2:.1f}px {XS/2:.1f}px;animation:fa 2s cubic-bezier(.2,.8,.2,1) forwards}}
  .fieldB{{transform-origin:{XS/2:.1f}px {XS/2:.1f}px;animation:fb 2s cubic-bezier(.2,.8,.2,1) forwards}}
  @keyframes fa{{0%{{transform:translate(-{XS*1.2:.0f}px,{XS*1.2:.0f}px) rotate(-14deg);opacity:0}}20%{{opacity:1}}40%{{transform:translate(0,0) rotate(-14deg)}}100%{{transform:translate(0,0) rotate(-4deg)}}}}
  @keyframes fb{{0%{{transform:translate({XS*1.2:.0f}px,-{XS*1.2:.0f}px) rotate(14deg);opacity:0}}20%{{opacity:1}}40%{{transform:translate(0,0) rotate(14deg)}}100%{{transform:translate(0,0) rotate(4deg)}}}}
  .lens{{opacity:0;animation:lens .8s ease-out 1.2s forwards}}
  @keyframes lens{{to{{opacity:1}}}}
  .chant{{transform:translate(-{DX:.2f}px,-{DY:.2f}px);animation:chant .6s cubic-bezier(.2,.8,.2,1) 2s forwards}}
  @keyframes chant{{to{{transform:translate(0,0)}}}}
  .left{{opacity:0;transform:translate(-28px,0);animation:settle .45s cubic-bezier(.2,.8,.2,1) 2.6s forwards}}
  .right{{opacity:0;transform:translate(28px,0);animation:settle .45s cubic-bezier(.2,.8,.2,1) 2.6s forwards}}
  @keyframes settle{{to{{opacity:1;transform:translate(0,0)}}}}
  .desc{{opacity:0;animation:fade .5s ease-out 3s forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  /* repos : respiration lente de l'angle après l'ouverture */
  .breath .fieldA{{animation:fa 2s cubic-bezier(.2,.8,.2,1) forwards, breathA 6s ease-in-out 3.2s infinite}}
  .breath .fieldB{{animation:fb 2s cubic-bezier(.2,.8,.2,1) forwards, breathB 6s ease-in-out 3.2s infinite}}
  @keyframes breathA{{0%,100%{{transform:rotate(-4deg)}}50%{{transform:rotate(-6deg)}}}}
  @keyframes breathB{{0%,100%{{transform:rotate(4deg)}}50%{{transform:rotate(6deg)}}}}
  @media (prefers-reduced-motion: reduce){{.fieldA,.fieldB,.lens,.chant,.left,.right,.desc{{animation:none!important;opacity:1!important;transform:none!important}}}}
</style></head>
<body><div class="stage breath">
<svg viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Clixite, Enterprise and Solution Architecture">
  <defs>
    <clipPath id="clipA"><path d="{face_a}"/></clipPath>
    <clipPath id="clipB"><path d="{face_b}"/></clipPath>
  </defs>
  <rect width="1280" height="720" fill="{INK}"/>
  <g transform="translate({OFFSET_X:.1f},0)">
    <g class="left">{paths(LEFT, PAPER)}</g>
    <g class="right">{paths(RIGHT, PAPER)}</g>
    <g class="xwrap" transform="translate({X_X - DX:.2f},{X_Y - DY:.2f})">
      <g class="chant"><path d="{sweep}" fill="{INK_TINT}"/></g>
      <path d="{face_a}" fill="{INK}"/><path d="{face_b}" fill="{INK}"/>
      <path class="lens" d="{lens}" fill="{SIGNAL}"/>
      <g clip-path="url(#clipA)">{lines_group(TURQ, "fieldA")}</g>
      <g clip-path="url(#clipB)">{lines_group(ROSE, "fieldB")}</g>
    </g>
    <g class="desc">{paths(desc_paths(), TURQ)}</g>
  </g>
</svg></div></body></html>'''
    open(path, "w").write(html)

# ---- video frames ------------------------------------------------------------
def ease(t): return 1 - (1 - t) ** 3
def frame_svg(t):
    """t in seconds, 0..3.6"""
    paths = lambda items, col: "".join(f'<path d="{it["d"]}" fill="{col}"/>' for it in items)
    # fields: slide 0..0.8, angle 14 -> 4 over 0.8..2.0
    s = ease(min(1, t / 0.8)); off = (1 - s) * XS * 1.2
    ang = 14 - 10 * ease(max(0, min(1, (t - 0.8) / 1.2)))
    if t > 3.2:  # breathing
        ang = 4 + 1.0 * (1 - math.cos((t - 3.2) / 6 * 2 * math.pi)) / 2 * 2
    lens_o = ease(max(0, min(1, (t - 1.2) / 0.8)))
    chant_p = ease(max(0, min(1, (t - 2.0) / 0.6)))
    letters_p = ease(max(0, min(1, (t - 2.6) / 0.45)))
    desc_o = ease(max(0, min(1, (t - 3.0) / 0.5)))
    fa = affinity.translate(field(XS, PITCH, LWID, -ang / 2), -off, -off)   # y-up: down-left start
    fb = affinity.translate(field(XS, PITCH, LWID, ang / 2), off, off)
    fa = fa.intersection(a_geom); fb = fb.intersection(b_geom)
    sweep = sweep_of(unary_union([a_geom, b_geom]), DX * chant_p, -DY * chant_p)
    out = f'<rect width="1280" height="720" fill="{INK}"/><g transform="translate({OFFSET_X:.1f},0)">'
    out += f'<g opacity="{letters_p:.3f}" transform="translate({-28*(1-letters_p):.2f},0)">{paths(LEFT, PAPER)}</g>'
    out += f'<g opacity="{letters_p:.3f}" transform="translate({28*(1-letters_p):.2f},0)">{paths(RIGHT, PAPER)}</g>'
    out += f'<g transform="translate({X_X - DX:.2f},{X_Y - DY:.2f})">'
    out += f'<path d="{to_screen(sweep)}" fill="{INK_TINT}"/>'
    out += f'<path d="{to_screen(a_geom)}" fill="{INK}"/><path d="{to_screen(b_geom)}" fill="{INK}"/>'
    out += f'<path d="{to_screen(centre)}" fill="{SIGNAL}" opacity="{lens_o:.3f}"/>'
    out += f'<path d="{to_screen(fa)}" fill="{TURQ}" opacity="{min(1, s*3):.3f}"/><path d="{to_screen(fb)}" fill="{ROSE}" opacity="{min(1, s*3):.3f}"/>'
    out += '</g>'
    out += f'<g opacity="{desc_o:.3f}">{paths(desc_paths(), TURQ)}</g></g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">{out}</svg>'

if __name__ == "__main__":
    import sys
    os.makedirs("charte/animation", exist_ok=True)
    build_html("charte/animation/clixite-ouverture.html")
    if "--video" in sys.argv:
        fps = 30; dur = 4.0; n = int(fps * dur)
        os.makedirs("frames", exist_ok=True)
        for i in range(n):
            svg = frame_svg(i / fps); open(f"frames/f{i:03d}.svg", "w").write(svg)
            subprocess.run(["node", "render.js", f"frames/f{i:03d}.svg", f"frames/f{i:03d}.png", "1920"], check=True, capture_output=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", "frames/f%03d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", "charte/animation/clixite-ouverture-1080p.mp4"], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", "frames/f%03d.png", "-vf", "fps=20,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse=dither=bayer", "charte/animation/clixite-ouverture-800.gif"], check=True)
        # poster frame
        subprocess.run(["cp", f"frames/f{n-1:03d}.png", "charte/animation/clixite-ouverture-poster.png"])
    print("anim ok")
