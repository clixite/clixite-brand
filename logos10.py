"""Piste P : le logo du comité. Un X maître au poids des lettres, une peau Relief (marque déposée), une peau Interférence (expression vivante)."""
import math
from shapely.geometry import box
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from logos7 import bar45, flip
from logos9 import sweep_of, field
from typo import text_paths, metrics, load, glyph_bounds

STEM = 132 / 1000          # Space Grotesk Bold capital stem, em units
EXTRUDE_DEG = 70.0         # extrusion direction, degrees below the horizontal (90 = straight down)
def ext_vec(d):
    return d * math.cos(math.radians(EXTRUDE_DEG)), -d * math.sin(math.radians(EXTRUDE_DEG))
T_RATIO = None             # computed per lockup: X bar thickness / box size

def x_geoms(size, t, gap_ratio=0.085):
    a = bar45(size, t, 1, "flat"); b = bar45(size, t, -1, "flat")
    centre = a.intersection(b)
    joint = centre.buffer(t * gap_ratio, join_style=2)
    return a, b, centre, joint

# P0 : maître plat
def x_master(sc, size, variant="color", t_ratio=0.185, key=True):
    t = t_ratio * size
    a, b, c, joint = x_geoms(size, t)
    if variant in ("mono", "mono_inverse"):
        return f'<path d="{flip(unary_union([a, b]).difference(joint), size)}" fill="{sc["text"]}"/><path d="{flip(c, size)}" fill="{sc["text"]}"/>'
    out = f'<path d="{flip(a.difference(joint), size)}" fill="{sc["t"]}"/><path d="{flip(b.difference(unary_union([a, joint])), size)}" fill="{sc["r"]}"/>'
    out += f'<path d="{flip(c, size)}" fill="{sc["y"] if key else sc["t"]}"/>'
    return out

def x_solid(sc, size, variant="color", t_ratio=0.185):
    """favicon : un seul X plein"""
    t = t_ratio * size
    a, b, c, joint = x_geoms(size, t)
    col = sc["text"] if variant in ("mono", "mono_inverse") else (sc["t"] if variant == "inverse" else sc["text"])
    return f'<path d="{flip(unary_union([a, b]), size)}" fill="{col}"/>'

# P1 : peau Relief (marque déposée)
def x_relief(sc, size, variant="color", t_ratio=0.185, depth_ratio=0.30, key=True):
    t = t_ratio * size; d = depth_ratio * t
    a, b, c, joint = x_geoms(size, t)
    dx, dy = ext_vec(d)
    lift = (-dx, -dy)
    fa, fb, fc, fj = (affinity.translate(g, *lift) for g in (a, b, c, joint))
    front = unary_union([fa, fb])
    sw = sweep_of(front, dx, dy)
    side = sc["text"] if variant in ("color", "mono") else INK_TINT if variant == "inverse" else PAPER
    if variant in ("mono", "mono_inverse"):
        face = PAPER if variant == "mono" else INK
        return (f'<path d="{flip(sw, size)}" fill="{sc["text"]}"/><path d="{flip(front, size)}" fill="{face}"/>'
                f'<path d="{flip(front.buffer(-t*0.14, join_style=2), size)}" fill="{sc["text"]}"/>')
    out = f'<path d="{flip(sw, size)}" fill="{side}"/>'
    out += f'<path d="{flip(fa.difference(fj), size)}" fill="{sc["t"]}"/><path d="{flip(fb.difference(unary_union([fa, fj])), size)}" fill="{sc["r"]}"/>'
    out += f'<path d="{flip(fc, size)}" fill="{sc["y"] if key else sc["t"]}"/>'
    return out

# P2 : peau Interférence (hybride : chant Encre, face vivante)
def x_vivant(sc, size, variant="color", t_ratio=0.185, depth_ratio=0.30, lines=10, angle=8.0, lens=True, lighten_overlap=True):
    t = t_ratio * size; d = depth_ratio * t
    a, b, c, joint = x_geoms(size, t)
    dx, dy = ext_vec(d)
    fa, fb, fc = (affinity.translate(g, -dx, -dy) for g in (a, b, c))
    front = unary_union([fa, fb]); sw = sweep_of(front, dx, dy)
    pitch = t / lines; lw = pitch / 2
    face = sc["bg"] if variant in ("color", "mono") else INK
    side = sc["text"] if variant in ("color", "mono") else INK_TINT if variant == "inverse" else PAPER
    out = f'<path d="{flip(sw, size)}" fill="{side}"/><path d="{flip(front, size)}" fill="{face}"/>'
    if lens and variant in ("color", "inverse"):
        out += f'<path d="{flip(fc, size)}" fill="{sc["y"]}"/>'
    ca, cb = (sc["text"], sc["text"]) if variant in ("mono", "mono_inverse") else (sc["t"], sc["r"])
    # half-step offset between the two fields (typographer), lighter strokes in the overlap
    Fa = affinity.translate(field(size, pitch, lw, -angle / 2), -dx, -dy).intersection(fa)
    Fb = affinity.translate(field(size, pitch, lw, angle / 2), -dx + pitch / 2, -dy).intersection(fb)
    if lighten_overlap:
        Fb_in = Fb.intersection(fc); Fb_out = Fb.difference(fc)
        out += f'<path d="{flip(Fa, size)}" fill="{ca}"/><path d="{flip(Fb_out, size)}" fill="{cb}"/>'
        out += f'<path d="{flip(Fb_in.buffer(-lw*0.15), size)}" fill="{cb}"/>'
    else:
        out += f'<path d="{flip(Fa, size)}" fill="{ca}"/><path d="{flip(Fb, size)}" fill="{cb}"/>'
    return out

# ---- lockups with the committee's metrics ---------------------------------
def lockup_central(gen, variant="color", descriptor="ENTERPRISE & SOLUTION ARCHITECTURE", wm_size=150.0, overshoot=0.05, gap_em=0.035):
    sc = scheme2(variant); pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * (1 + 2 * overshoot)
    stem = STEM * wm_size
    t_ratio = 1.08 * stem / xs
    tr = 0.06
    baseline = pad + xs - overshoot * cap
    left, lw = text_paths("space", 700, "CLI", wm_size, pad, baseline, tracking=tr)
    gap_px = gap_em * wm_size
    # symmetric blanks: the I sidebearings (66/1000 em each side) plus gap_px on each side of the X box;
    # the relief extrudes down-right, so the box is nudged left by a quarter of the depth for optical centring
    # the relief lifts the face up-left by (dx, dy) and extrudes back to the box: the silhouette spans
    # [x_x - dx, x_x + xs] horizontally and [x_y - dy, x_y + xs] vertically. Centre the silhouette, not the box.
    t_px = t_ratio * xs; d_px = 0.30 * t_px; edx, edy = ext_vec(d_px)
    flat = gen in (x_master, x_solid)
    shx = 0.0 if flat else edx / 2; shy = 0.0 if flat else -edy / 2
    x_x = pad + lw + gap_px + shx
    x_y = baseline - cap - overshoot * cap + shy
    right, rw = text_paths("space", 700, "ITE", wm_size, x_x + xs + gap_px - shx, baseline, tracking=tr)
    width = (x_x + xs + gap_px + rw) - pad
    content = paths_for(left, sc["text"]) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{gen(sc, xs, variant, t_ratio=t_ratio)}</g>' + paths_for(right, sc["text"])
    d_size = 24.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    k = width / d_w; d_size *= k
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    content += paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = pad * 2 + width; H = baseline + 40 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def lockup_side(gen, variant="color", descriptor="ENTERPRISE & SOLUTION ARCHITECTURE", wm_size=150.0):
    sc = scheme2(variant); pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * 1.28
    stem = STEM * wm_size; t_ratio = 1.08 * stem / xs * 1.12
    mark_x, mark_y = pad, pad
    wm_x = mark_x + xs + 36
    baseline = mark_y + (xs + cap) / 2
    items, width = text_paths("space", 700, "CLIXITE", wm_size, wm_x, baseline, tracking=0.06)
    d_size = 24.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.2)
    k = width / d_w; d_size *= k
    d_items, d_w = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.2)
    edx, edy = ext_vec(0.30 * t_ratio * xs); flat = gen in (x_master, x_solid)
    shx = 0.0 if flat else edx / 2; shy = 0.0 if flat else -edy / 2
    content = f'<g transform="translate({mark_x + shx:.2f},{mark_y + shy:.2f})">{gen(sc, xs, variant, t_ratio=t_ratio)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = wm_x + width + pad; H = baseline + 36 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def lockup_stacked(gen, variant="color", descriptor="ENTERPRISE & SOLUTION ARCHITECTURE"):
    sc = scheme2(variant); pad = 56; xs = 220.0; wm_size = 92.0; tr = 0.12
    items, width = text_paths("space", 700, "CLIXITE", wm_size, 0, 0, tracking=tr)
    W = max(width, xs) + pad * 2
    x_x = (W - xs) / 2
    t_ratio = 1.08 * STEM * wm_size / (0.7 * wm_size * 1.1) * 1.0
    edx, edy = ext_vec(0.30 * 0.2 * xs); flat = gen in (x_master, x_solid)
    shx = 0.0 if flat else edx / 2; shy = 0.0 if flat else -edy / 2
    content = f'<g transform="translate({x_x + shx:.2f},{pad + shy:.2f})">{gen(sc, xs, variant, t_ratio=0.2)}</g>'
    baseline = pad + xs + 44 + 0.7 * wm_size
    items, width = text_paths("space", 700, "CLIXITE", wm_size, (W - width) / 2, baseline, tracking=tr)
    content += paths_for(items, sc["text"])
    d_items, d_w = text_paths("space", 500, descriptor, 15.0, 0, 0, tracking=0.22)
    d_items, d_w = text_paths("space", 500, descriptor, 15.0, (W - d_w) / 2, baseline + 34, tracking=0.22)
    content += paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    H = baseline + 34 + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def lockup_wordmark(gen, variant="color", wm_size=150.0, overshoot=0.05, gap_em=0.035):
    """Mot-marque seul (Design System 2.0) : pour les usages sous 240 px de large, en-têtes d'interface et barres
    de navigation, où le descripteur deviendrait illisible. Mêmes métriques que lockup_central, sans descripteur."""
    sc = scheme2(variant); pad = 0.0
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * (1 + 2 * overshoot); stem = STEM * wm_size; t_ratio = 1.08 * stem / xs; tr = 0.06
    baseline = xs - overshoot * cap
    left, lw = text_paths("space", 700, "CLI", wm_size, pad, baseline, tracking=tr)
    gap_px = gap_em * wm_size
    t_px = t_ratio * xs; d_px = 0.30 * t_px; edx, edy = ext_vec(d_px)
    flat = gen in (x_master, x_solid)
    shx = 0.0 if flat else edx / 2; shy = 0.0 if flat else -edy / 2
    x_x = pad + lw + gap_px + shx; x_y = baseline - cap - overshoot * cap + shy
    right, rw = text_paths("space", 700, "ITE", wm_size, x_x + xs + gap_px - shx, baseline, tracking=tr)
    W = (x_x + xs + gap_px + rw); H = xs + (0.0 if flat else -edy)
    content = paths_for(left, sc["text"]) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{gen(sc, xs, variant, t_ratio=t_ratio)}</g>' + paths_for(right, sc["text"])
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def mark(gen, variant="color", size=200.0, t_ratio=0.2):
    sc = scheme2(variant); pad = size * 0.17; inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{gen(sc, inner, variant, t_ratio=t_ratio)}</g>', size, size, sc["bg"])

def tile(gen, size=200.0):
    sc = scheme2("inverse"); pad = size * 0.22; inner = size - 2 * pad
    return svg_wrap(f'<rect width="{size}" height="{size}" rx="{size*0.22:.1f}" fill="{INK}"/><g transform="translate({pad},{pad})">{gen(sc, inner, "inverse", t_ratio=0.2)}</g>', size, size, None)

GENS = {
    "p0-maitre": x_master,
    "p1-relief": x_relief,
    "p2-vivant": x_vivant,
    "p2-vivant-simple": lambda sc, s, v="color", t_ratio=0.2: x_vivant(sc, s, v, t_ratio=t_ratio, lines=6, angle=8.0),
    "p2-vivant-sobre": lambda sc, s, v="color", t_ratio=0.2: x_vivant(sc, s, v, t_ratio=t_ratio, lines=10, angle=8.0),
}

if __name__ == "__main__":
    import os
    os.makedirs("out10", exist_ok=True)
    for key, gen in GENS.items():
        for v in ["color", "inverse", "mono"]:
            open(f"out10/{key}-mark-{v}.svg", "w").write(mark(gen, v))
            svg, _ = lockup_central(gen, v); open(f"out10/{key}-central-{v}.svg", "w").write(svg)
        svg, _ = lockup_side(gen, "color"); open(f"out10/{key}-side-color.svg", "w").write(svg)
        svg, _ = lockup_stacked(gen, "color"); open(f"out10/{key}-stacked-color.svg", "w").write(svg)
        svg, _ = lockup_stacked(gen, "inverse"); open(f"out10/{key}-stacked-inverse.svg", "w").write(svg)
    open("out10/p-favicon-ink.svg", "w").write(mark(x_solid, "mono"))
    open("out10/p-favicon-inverse.svg", "w").write(mark(x_solid, "inverse"))
    open("out10/p1-tile.svg", "w").write(tile(x_relief))
    print("done")
