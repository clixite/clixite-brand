"""Concept I : CONSTRUIT. A fully custom geometric monoline wordmark drawn on one module:
circle = x-height, stroke = x-height/4.2, 45-degree bowtie between the two i stems."""
import math
from shapely.geometry import Polygon, LineString, box, Point, MultiPolygon
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from logos3 import bowtie_parts
from typo import text_paths

XH = 100.0            # x-height in units
T = XH / 4.4          # stroke
ASC = XH * 1.42       # ascender
R = XH / 2            # circle radius (outer)
QS = 64

def ring(cx, cy, r_out, r_in):
    return Point(cx, cy).buffer(r_out, quad_segs=QS).difference(Point(cx, cy).buffer(r_in, quad_segs=QS))

def wedge(cx, cy, a0, a1, far=400):
    a0, a1 = math.radians(a0), math.radians(a1)
    pts = [(cx, cy)] + [(cx + far * math.cos(a0 + (a1 - a0) * k / 24), cy + far * math.sin(a0 + (a1 - a0) * k / 24)) for k in range(25)]
    return Polygon(pts)

def letter_c(x):
    g = ring(x + R, R, R, R - T).difference(wedge(x + R, R, -38, 38))
    return g, 2 * R * 0.93   # advance (open right side: tighter)

def letter_l(x):
    return box(x, 0, x + T, ASC), T

def letter_i(x):
    stem = box(x, 0, x + T, XH)
    dot = Point(x + T / 2, XH + T * 0.95).buffer(T * 0.58, quad_segs=QS)
    return stem, dot, T

def letter_t(x):
    stem = box(x, 0, x + T, ASC * 0.86)
    bar = box(x - XH * 0.26, XH - T, x + T + XH * 0.30, XH)
    return unary_union([stem, bar]), T + XH * 0.30

def letter_e(x):
    g = ring(x + R, R, R, R - T).difference(wedge(x + R, R, -56, -4))
    bar = box(x + T * 0.55, R - T / 2, x + 2 * R + 5, R + T / 2).intersection(Point(x + R, R).buffer(R, quad_segs=QS))
    return unary_union([g, bar]), 2 * R

GAP = XH * 0.17

def construit_pieces(scale, x0, baseline):
    """Returns list of (kind, geom) in units and total width in units."""
    pieces = []
    x = 0.0
    g, adv = letter_c(x); pieces.append(("text", g)); x += adv + GAP * 0.55
    g, adv = letter_l(x); pieces.append(("text", g)); x += adv + GAP
    stem, dot, adv = letter_i(x); pieces.append(("stem", stem)); pieces.append(("dot1", dot)); x += adv
    bars, ltri, rtri = bowtie_parts(XH, XH, T)
    for k, gg in (("x", bars), ("ltri", ltri), ("rtri", rtri)):
        pieces.append((k, affinity.translate(gg, x, 0)))
    x += XH
    stem, dot, adv = letter_i(x); pieces.append(("stem", stem)); pieces.append(("dot2", dot)); x += adv + GAP
    g, adv = letter_t(x + XH * 0.26); pieces.append(("text", g)); x += adv + XH * 0.26 + GAP * 0.6
    g, adv = letter_e(x); pieces.append(("text", g)); x += adv
    return pieces, x

def render_construit(variant="color", scale=1.6, pad=44, counters=True, colored_dots=False, descriptor="Architecture de solutions"):
    sc = scheme2(variant)
    pieces, w_units = construit_pieces(scale, 0, 0)
    baseline = pad + ASC * scale + 8
    colors = dict(text=sc["text"], stem=sc["text"], x=sc["t"],
                  dot1=sc["r"] if colored_dots else sc["text"], dot2=sc["y"] if colored_dots else sc["text"],
                  ltri=sc["r"] if counters else None, rtri=sc["y"] if counters else None)
    if variant in ("mono", "mono_inverse"):
        colors.update(ltri=None, rtri=None, dot1=sc["text"], dot2=sc["text"])
    content = ""
    for k, g in pieces:
        if colors[k] is None: continue
        content += f'<path d="{geom_to_d(g, scale, pad, baseline)}" fill="{colors[k]}"/>'
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 2, baseline + 58, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + max(w_units * scale, d_width)
    H = baseline + 58 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def render_blueprint(scale=1.6, pad=60):
    """Construction drawing: the wordmark in outline with its guides."""
    pieces, w_units = construit_pieces(scale, 0, 0)
    baseline = pad + ASC * scale + 40
    W = pad * 2 + w_units * scale
    H = baseline + pad * 1.3
    content = f'<rect width="100%" height="100%" fill="{PAPER}"/>'
    # guides: baseline, x-height, ascender, cap of dot
    for y, lab in ((0, "ligne de base"), (XH, "hauteur d'x"), (ASC, "ascendante")):
        yy = baseline - y * scale
        content += f'<line x1="{pad-30}" y1="{yy:.1f}" x2="{W-pad+30}" y2="{yy:.1f}" stroke="{TURQ}" stroke-width="1" stroke-dasharray="4 4"/>'
        content += f'<text x="{W-pad+34}" y="{yy+4:.1f}" font-family="JetBrains Mono, monospace" font-size="11" fill="{TURQ_DEEP}">{lab}</text>'
    # circles behind c and e, square behind the bowtie, 45 degree diagonals
    x = 0.0
    content += f'<circle cx="{pad + R*scale:.1f}" cy="{baseline - R*scale:.1f}" r="{R*scale:.1f}" fill="none" stroke="{ROSE}" stroke-width="1"/>'
    for k, g in pieces:
        if k == "x":
            b = g.bounds
            content += f'<rect x="{pad + b[0]*scale:.1f}" y="{baseline - b[3]*scale:.1f}" width="{(b[2]-b[0])*scale:.1f}" height="{(b[3]-b[1])*scale:.1f}" fill="none" stroke="{ROSE}" stroke-width="1"/>'
            content += f'<line x1="{pad + b[0]*scale:.1f}" y1="{baseline - b[1]*scale:.1f}" x2="{pad + b[2]*scale:.1f}" y2="{baseline - b[3]*scale:.1f}" stroke="{ROSE}" stroke-width="1" stroke-dasharray="3 3"/>'
            content += f'<line x1="{pad + b[0]*scale:.1f}" y1="{baseline - b[3]*scale:.1f}" x2="{pad + b[2]*scale:.1f}" y2="{baseline - b[1]*scale:.1f}" stroke="{ROSE}" stroke-width="1" stroke-dasharray="3 3"/>'
    # e circle: last piece
    eb = pieces[-1][1].bounds
    content += f'<circle cx="{pad + (eb[0]+R)*scale:.1f}" cy="{baseline - R*scale:.1f}" r="{R*scale:.1f}" fill="none" stroke="{ROSE}" stroke-width="1"/>'
    for k, g in pieces:
        if k in ("ltri", "rtri"): continue
        content += f'<path d="{geom_to_d(g, scale, pad, baseline)}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
    # stroke annotation
    content += f'<text x="{pad}" y="{H-18:.1f}" font-family="JetBrains Mono, monospace" font-size="11" fill="{SLATE}">module : cercle = hauteur d\'x · trait = x/4,4 · jointure à 45° · ascendante = 1,42 x</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.1f}" height="{H:.1f}">{content}</svg>'

def mark_construit(variant="color", size=200.0):
    sc = scheme2(variant)
    bars, ltri, rtri = bowtie_parts(XH, XH, T)
    total = T + XH + T
    s = size * 0.62 / total
    x0 = (size - total * s) / 2
    base = size / 2 + XH * s / 2
    stem = box(0, 0, T, XH)
    c = f'<path d="{geom_to_d(stem, s, x0, base)}" fill="{sc["text"]}"/>'
    c += f'<path d="{geom_to_d(stem, s, x0 + (T + XH) * s, base)}" fill="{sc["text"]}"/>'
    c += f'<path d="{geom_to_d(bars, s, x0 + T * s, base)}" fill="{sc["t"]}"/>'
    if variant not in ("mono", "mono_inverse"):
        c += f'<path d="{geom_to_d(ltri, s, x0 + T * s, base)}" fill="{sc["r"]}"/>'
        c += f'<path d="{geom_to_d(rtri, s, x0 + T * s, base)}" fill="{sc["y"]}"/>'
    return svg_wrap(c, size, size, sc["bg"])

if __name__ == "__main__":
    import os
    os.makedirs("out4", exist_ok=True)
    for v in ["color", "inverse", "mono", "mono_inverse"]:
        svg, d = render_construit(v); open(f"out4/i-construit-lockup-{v}.svg", "w").write(svg)
        open(f"out4/i-construit-mark-{v}.svg", "w").write(mark_construit(v))
    svg, d = render_construit("color", counters=False, colored_dots=True); open("out4/i-construit-lockup-color-open.svg", "w").write(svg)
    open("out4/i-construit-blueprint.svg", "w").write(render_blueprint())
    print("done")
