"""Clixite logo concepts, round 2: bolder, built on the trio turquoise-bleu / rose / signal."""
import math
from shapely.geometry import Point, Polygon, LineString, MultiPolygon
from shapely.ops import unary_union
from shapely import affinity
from typo import text_paths, load, metrics, glyph_bounds
from geom import glyph_polygon, geom_to_d, rounded_rect
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for

ROSE_DEEP = "#D81B60"


def scheme2(variant):
    if variant == "color":
        return dict(bg=PAPER, text=INK, t=TURQ, r=ROSE, y=SIGNAL, overlap=INK, sub=SLATE)
    if variant == "inverse":
        return dict(bg=INK, text=PAPER, t=TURQ, r=ROSE, y=SIGNAL, overlap=SIGNAL, sub=MIST)
    if variant == "mono":
        return dict(bg=PAPER, text=INK, t=INK, r=INK, y=INK, overlap=PAPER, sub=INK)
    if variant == "mono_inverse":
        return dict(bg=INK, text=PAPER, t=PAPER, r=PAPER, y=PAPER, overlap=INK, sub=PAPER)
    raise ValueError(variant)


def split_i(tt, gname):
    """Return (stem, dot) geometries of the glyph 'i' in font units."""
    g = glyph_polygon(tt, gname)
    parts = list(g.geoms) if isinstance(g, MultiPolygon) else [g]
    parts = sorted(parts, key=lambda p: p.bounds[1])  # by min y
    return parts[0], parts[-1]


# =============================================================================
# Concept E : VARIABLE  (le x devient une variable en italique serif, les points des i en rose et jaune)
# =============================================================================
def variable_pieces(wm_size, x0, baseline, italic=("fraunces-it", 600)):
    """Compose 'clixite' with Space Grotesk 600 and an italic serif x; returns svg parts and width."""
    tt, _, upem = load("space", 600)
    cmap = tt.getBestCmap()
    iname, xname = cmap[ord("i")], cmap[ord("x")]
    m = metrics("space", 600)
    xh = m["xh"] / upem * wm_size
    stem_i, dot_i = split_i(tt, iname)
    # italic x scaled so its height matches the sans x-height
    ttx, _, upx = load(*italic)
    xg = ttx.getBestCmap()[ord("x")]
    bx = glyph_bounds(ttx, xg)
    x_h_units = bx[3] - bx[1]
    sx = (xh * 1.04) / x_h_units  # px per italic font unit
    xgeom = glyph_polygon(ttx, xg)
    # shape left part, x, right part
    left, lw = text_paths("space", 600, "cli", wm_size, x0, baseline, tracking=-0.005)
    gap = wm_size * 0.03
    xx = x0 + lw + gap - bx[0] * sx
    x_adv = (bx[2] - bx[0]) * sx + gap
    right, rw = text_paths("space", 600, "ite", wm_size, x0 + lw + gap + x_adv, baseline, tracking=-0.005)
    s = wm_size / upem
    pieces = []  # (kind, d)
    i_count = 0
    for it in left + right:
        if it["g"] == iname:
            pieces.append(("stem", geom_to_d(stem_i, s, it["x"], baseline)))
            pieces.append(("dot1" if i_count == 0 else "dot2", geom_to_d(dot_i, s, it["x"], baseline)))
            i_count += 1
        else:
            pieces.append(("text", it["d"]))
    pieces.append(("x", geom_to_d(xgeom, sx, xx, baseline)))
    total_w = lw + gap + x_adv + rw
    return pieces, total_w, xh


def lockup_variable(variant="color", descriptor="Nous résolvons votre x."):
    sc = scheme2(variant)
    wm_size = 170.0
    pad = 44
    baseline = pad + 0.80 * wm_size
    pieces, width, xh = variable_pieces(wm_size, pad, baseline)
    colors = dict(text=sc["text"], stem=sc["text"], dot1=sc["r"], dot2=sc["y"], x=sc["t"])
    content = "".join(f'<path d="{d}" fill="{colors[k]}"/>' for k, d in pieces if d)
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 4, baseline + 60, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + max(width, d_width)
    H = baseline + 60 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_variable(variant="color", size=200.0):
    """The italic x with the two tittles as satellites (rose, signal)."""
    sc = scheme2(variant)
    ttx, _, upx = load("fraunces-it", 600)
    xg = ttx.getBestCmap()[ord("x")]
    bx = glyph_bounds(ttx, xg)
    xgeom = glyph_polygon(ttx, xg)
    gw, gh = bx[2] - bx[0], bx[3] - bx[1]
    target = size * 0.54
    s = target / gh
    cx = size / 2
    dx = cx - (bx[0] + gw / 2) * s
    dy = size * 0.76 + bx[1] * s
    r = size * 0.06
    top = size * 0.76 - target
    content = f'<path d="{geom_to_d(xgeom, s, dx, dy)}" fill="{sc["t"]}"/>'
    content += f'<circle cx="{cx - gw * s * 0.40:.2f}" cy="{top - r * 1.9:.2f}" r="{r:.2f}" fill="{sc["r"]}"/>'
    content += f'<circle cx="{cx + gw * s * 0.40:.2f}" cy="{top - r * 1.9:.2f}" r="{r:.2f}" fill="{sc["y"]}"/>'
    return svg_wrap(content, size, size, sc["bg"])


# =============================================================================
# Concept F : INTERSECTION  (deux pilules qui se croisent, l'intersection prend la couleur du fond ou du signal)
# =============================================================================
def pill(cx, cy, length, width, angle_deg):
    half = (length - width) / 2
    ls = LineString([(-half, 0), (half, 0)]).buffer(width / 2, quad_segs=48)
    ls = affinity.rotate(ls, angle_deg, origin=(0, 0))
    return affinity.translate(ls, cx, cy)


def mark_intersection(sc, size=100.0):
    s = size / 100.0
    a = pill(50 * s, 50 * s, 92 * s, 27 * s, 45)
    b = pill(50 * s, 50 * s, 92 * s, 27 * s, -45)
    ov = a.intersection(b)
    out = [f'<path d="{geom_to_d(a, flip=False)}" fill="{sc["t"]}"/>',
           f'<path d="{geom_to_d(b.difference(a), flip=False)}" fill="{sc["r"]}"/>',
           f'<path d="{geom_to_d(ov, flip=False)}" fill="{sc["overlap"]}"/>']
    return "".join(out)


def lockup_intersection(variant="color", descriptor="ARCHITECTURE · PROCUREMENT · CONFORMITÉ"):
    sc = scheme2(variant)
    wm_size = 150.0
    pad = 40
    m = metrics("space", 700)
    cap = m["cap"] / m["upem"] * wm_size
    mark_h = cap * 1.3
    mark_x, mark_y = pad, pad
    wm_x = mark_x + mark_h + 34
    baseline = mark_y + (mark_h + cap) / 2
    items, width = text_paths("space", 700, "CLIXITE", wm_size, wm_x, baseline, tracking=0.05)
    d_size = 24.0
    d_items, d_width = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.19)
    k = width / d_width
    d_size *= k
    d_items, d_width = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 36 + d_size, tracking=0.19)
    content = f'<g transform="translate({mark_x},{mark_y})">{mark_intersection(sc, mark_h)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = wm_x + width + pad
    H = baseline + 36 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_intersection(variant="color", size=200.0):
    sc = scheme2(variant)
    pad = size * 0.17
    inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{mark_intersection(sc, inner)}</g>', size, size, sc["bg"])


# =============================================================================
# Concept G : ASTÉRISQUE  (trois barres, trois couleurs ; le joker, la note de bas de page, le détail qui compte)
# =============================================================================
def mark_asterisque(sc, size=100.0, center=None):
    s = size / 100.0
    bars = []
    for ang, col in [(90, sc["t"]), (30, sc["r"]), (150, sc["y"])]:
        b = pill(50 * s, 50 * s, 96 * s, 24 * s, ang)
        bars.append((b, col))
    out = []
    for b, col in bars:
        out.append(f'<path d="{geom_to_d(b, flip=False)}" fill="{col}"/>')
    centre = bars[0][0].intersection(bars[1][0]).intersection(bars[2][0])
    ccol = center or (PAPER if sc["t"] == INK else INK)
    out.append(f'<path d="{geom_to_d(centre, flip=False)}" fill="{ccol}"/>')
    return "".join(out)


def lockup_asterisque(variant="color", descriptor="Architecture de solutions"):
    sc = scheme2(variant)
    wm_size = 170.0
    pad = 44
    baseline = pad + 0.80 * wm_size
    items, width = text_paths("space", 600, "clixite", wm_size, pad, baseline, tracking=-0.005)
    m = metrics("space", 600)
    asc = m["asc"] / m["upem"] * wm_size
    ast = wm_size * 0.42
    ax = pad + width + wm_size * 0.05
    ay = baseline - 0.74 * wm_size
    content = paths_for(items, sc["text"])
    content += f'<g transform="translate({ax},{ay})">{mark_asterisque(sc, ast)}</g>'
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 4, baseline + 60, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = ax + ast + pad
    H = baseline + 60 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_asterisque(variant="color", size=200.0):
    sc = scheme2(variant)
    pad = size * 0.16
    inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{mark_asterisque(sc, inner)}</g>', size, size, sc["bg"])


CONCEPTS2 = {
    "e-variable": (lockup_variable, mark_only_variable),
    "f-intersection": (lockup_intersection, mark_only_intersection),
    "g-asterisque": (lockup_asterisque, mark_only_asterisque),
}

if __name__ == "__main__":
    import os
    os.makedirs("out2", exist_ok=True)
    for key, (lock, mark) in CONCEPTS2.items():
        for v in ["color", "inverse", "mono", "mono_inverse"]:
            svg, dims = lock(v)
            open(f"out2/{key}-lockup-{v}.svg", "w").write(svg)
            open(f"out2/{key}-mark-{v}.svg", "w").write(mark(v))
    print("done")
