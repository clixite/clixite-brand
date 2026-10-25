"""Variations du X (piste N) : cinq constructions du symbole, même lockup."""
import math
from shapely.geometry import Polygon, LineString, box, Point
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d, chevron
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from logos6 import x_svg as x_assembled
from typo import text_paths, metrics

INDIGO = "#193776"

def bar45(size, t, direction=1, cut="perp", r=0.0):
    """A diagonal bar across a size box. direction 1 = '/', -1 = '\\'. cut: 'perp' (45-degree ends) or 'flat' (horizontal terminals)."""
    S = size
    if cut == "flat":
        th = t * math.sqrt(2)
        if direction == 1:
            poly = Polygon([(0, 0), (th, 0), (S, S), (S - th, S)])
        else:
            poly = Polygon([(S, 0), (S - th, 0), (0, S), (th, S)])
    else:
        inset = t / 2 * math.sqrt(2) / 2
        p0, p1 = ((inset, inset), (S - inset, S - inset)) if direction == 1 else ((inset, S - inset), (S - inset, inset))
        poly = LineString([p0, p1]).buffer(t / 2, cap_style=2, join_style=2)
    if r > 0:
        poly = poly.buffer(-r, join_style=1).buffer(r, join_style=1, quad_segs=12)
    return poly

def flip(g, size):
    return geom_to_d(g, 1.0, 0, size)

# N2 : CROISÉ. 45-degree cut ends, turquoise over rose, overlap in indigo (turquoise x rose).
def x_croise(sc, size, variant="color", t=24.0, centre=None):
    t = t * size / 100
    a = bar45(size, t, 1, "perp", r=t * 0.12)
    b = bar45(size, t, -1, "perp", r=t * 0.12)
    ov = a.intersection(b)
    if variant in ("mono", "mono_inverse"):
        ca = cb = sc["text"]; cc = sc["bg"] if variant == "mono" else INK
        cc = PAPER if variant == "mono" else INK
    else:
        ca, cb, cc = sc["t"], sc["r"], (centre or INDIGO)
    out = f'<path d="{flip(a, size)}" fill="{ca}"/>'
    out += f'<path d="{flip(b.difference(a), size)}" fill="{cb}"/>'
    out += f'<path d="{flip(ov, size)}" fill="{cc}"/>'
    return out

# N3 : TRESSÉ. Rounded bars; the turquoise passes over the rose, which is interrupted at the crossing.
def x_tresse(sc, size, variant="color", t=24.0):
    t = t * size / 100
    inset = t / 2
    a = LineString([(inset, inset), (size - inset, size - inset)]).buffer(t / 2, cap_style=1, quad_segs=24)
    b = LineString([(inset, size - inset), (size - inset, inset)]).buffer(t / 2, cap_style=1, quad_segs=24)
    gap = a.buffer(t * 0.16)
    b2 = b.difference(gap)
    ca, cb = (sc["text"], sc["text"]) if variant in ("mono", "mono_inverse") else (sc["t"], sc["r"])
    return f'<path d="{flip(b2, size)}" fill="{cb}"/><path d="{flip(a, size)}" fill="{ca}"/>'

# N4 : MONOLITHE. One solid x, the centre piece in signal with a fine joint.
def x_monolithe(sc, size, variant="color", t=25.0, gap=2.2):
    t = t * size / 100; gap = gap * size / 100
    a = bar45(size, t, 1, "perp"); b = bar45(size, t, -1, "perp")
    whole = unary_union([a, b])
    centre = a.intersection(b)
    body = whole.difference(centre.buffer(gap, join_style=2))
    cbody = sc["text"] if variant in ("mono", "mono_inverse") else sc["t"]
    cc = (PAPER if variant == "mono" else INK) if variant in ("mono", "mono_inverse") else sc["y"]
    return f'<path d="{flip(body, size)}" fill="{cbody}"/><path d="{flip(centre, size)}" fill="{cc}"/>'

# N5 : CHEVRONS. Heritage: a > and a < that cross, rounded corners, signal diamond where they meet.
def x_chevrons(sc, size, variant="color", t=22.0):
    s = size / 100
    hw = t * s / 2
    left = chevron([(12 * s, 10 * s), (57 * s, 50 * s), (12 * s, 90 * s)], hw)
    right = chevron([(88 * s, 10 * s), (43 * s, 50 * s), (88 * s, 90 * s)], hw)
    r = hw * 0.35
    left = left.buffer(-r, join_style=1).buffer(r, join_style=1, quad_segs=12)
    right = right.buffer(-r, join_style=1).buffer(r, join_style=1, quad_segs=12)
    ov = left.intersection(right)
    if variant in ("mono", "mono_inverse"):
        cl = cr = sc["text"]; cc = PAPER if variant == "mono" else INK
    else:
        cl, cr, cc = sc["t"], sc["r"], sc["y"]
    out = f'<path d="{geom_to_d(left, flip=False)}" fill="{cl}"/>'
    out += f'<path d="{geom_to_d(right.difference(left), flip=False)}" fill="{cr}"/>'
    out += f'<path d="{geom_to_d(ov, flip=False)}" fill="{cc}"/>'
    return out

VARIANTS = {
    "n1-assemble": lambda sc, size, v: x_assembled(sc, size, v),
    "n2-croise": x_croise,
    "n3-tresse": x_tresse,
    "n4-monolithe": x_monolithe,
    "n5-chevrons": x_chevrons,
}

def lockup_side(gen, variant="color", descriptor="ENTERPRISE & SOLUTION ARCHITECTURE", word="CLIXITE"):
    """Symbol on the left, wordmark on the right, descriptor under the wordmark."""
    sc = scheme2(variant)
    wm_size = 150.0; pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * 1.3
    mark_x, mark_y = pad, pad
    wm_x = mark_x + xs + 40
    baseline = mark_y + (xs + cap) / 2
    items, width = text_paths("space", 700, word, wm_size, wm_x, baseline, tracking=0.06)
    d_size = 24.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.2)
    k = width / d_w; d_size *= k
    d_items, d_w = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.2)
    content = f'<g transform="translate({mark_x},{mark_y})">{gen(sc, xs, variant)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = wm_x + width + pad; H = baseline + 36 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def lockup_central(gen, variant="color", descriptor="ENTERPRISE & SOLUTION ARCHITECTURE"):
    sc = scheme2(variant)
    wm_size = 150.0; pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * 1.14; tr = 0.06
    baseline = pad + xs - (xs - cap) / 2
    left, lw = text_paths("space", 700, "CLI", wm_size, pad, baseline, tracking=tr)
    gap_px = wm_size * 0.09
    x_x = pad + lw + gap_px; x_y = baseline - cap - (xs - cap) / 2
    right, rw = text_paths("space", 700, "ITE", wm_size, x_x + xs + gap_px, baseline, tracking=tr)
    width = (x_x + xs + gap_px + rw) - pad
    content = paths_for(left, sc["text"]) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{gen(sc, xs, variant)}</g>' + paths_for(right, sc["text"])
    d_size = 24.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    k = width / d_w; d_size *= k
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    content += paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = pad * 2 + width; H = baseline + 40 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def mark(gen, variant="color", size=200.0):
    sc = scheme2(variant); pad = size * 0.17; inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{gen(sc, inner, variant)}</g>', size, size, sc["bg"])

if __name__ == "__main__":
    import os
    os.makedirs("out7", exist_ok=True)
    for key, gen in VARIANTS.items():
        for v in ["color", "inverse", "mono"]:
            open(f"out7/{key}-mark-{v}.svg", "w").write(mark(gen, v))
            svg, _ = lockup_side(gen, v); open(f"out7/{key}-side-{v}.svg", "w").write(svg)
            svg, _ = lockup_central(gen, v); open(f"out7/{key}-central-{v}.svg", "w").write(svg)
    print("done")
