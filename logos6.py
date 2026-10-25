"""Piste N : LE X. The X is the symbol, central, assembled from four arms and a centre piece."""
import math
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from typo import text_paths, metrics

def x_parts(size=100.0, t=23.0, gap=2.4):
    th = t * math.sqrt(2)  # horizontal width of a 45-degree bar's terminal
    S = size
    A = Polygon([(0, 0), (th, 0), (S, S), (S - th, S)])          # bottom-left to top-right
    B = Polygon([(S, 0), (S - th, 0), (0, S), (th, S)])          # top-left to bottom-right
    centre = A.intersection(B)
    hole = centre.buffer(gap, join_style=2)
    a_arms = A.difference(hole)
    b_arms = B.difference(hole)
    return a_arms, b_arms, centre

def x_svg(sc, size=100.0, variant="color", t=23.0, gap=2.4):
    a, b, c = x_parts(size, t * size / 100.0, gap * size / 100.0)
    if variant in ("mono", "mono_inverse"):
        ca, cb, cc = sc["text"], sc["text"], sc["text"]
    else:
        ca, cb, cc = sc["t"], sc["r"], sc["y"]
    # geometry is y-up in a size box; flip to SVG
    out = f'<path d="{geom_to_d(a, 1.0, 0, size)}" fill="{ca}"/>'
    out += f'<path d="{geom_to_d(b, 1.0, 0, size)}" fill="{cb}"/>'
    out += f'<path d="{geom_to_d(c, 1.0, 0, size)}" fill="{cc}"/>'
    return out

def lockup_x(variant="color", descriptor="NOUS RÉSOLVONS VOTRE X", overshoot=1.14):
    sc = scheme2(variant)
    wm_size = 150.0; pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm_size
    xs = cap * overshoot
    tr = 0.06
    left, lw = text_paths("space", 700, "CLI", wm_size, pad, 0, tracking=tr)
    baseline = pad + xs - (xs - cap) / 2
    left, lw = text_paths("space", 700, "CLI", wm_size, pad, baseline, tracking=tr)
    gap_px = wm_size * 0.09
    x_x = pad + lw + gap_px
    x_y = baseline - cap - (xs - cap) / 2
    right, rw = text_paths("space", 700, "ITE", wm_size, x_x + xs + gap_px, baseline, tracking=tr)
    width = (x_x + xs + gap_px + rw) - pad
    content = paths_for(left, sc["text"]) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{x_svg(sc, xs, variant)}</g>' + paths_for(right, sc["text"])
    # descriptor spread to the wordmark width
    d_size = 24.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    k = width / d_w; d_size *= k
    d_items, d_w = text_paths("space", 500, descriptor, d_size, pad, baseline + 40 + d_size, tracking=0.2)
    content += paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    W = pad * 2 + width; H = baseline + 40 + d_size + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def lockup_x_stacked(variant="color", descriptor="NOUS RÉSOLVONS VOTRE X"):
    sc = scheme2(variant)
    pad = 56; xs = 220.0
    wm_size = 96.0; tr = 0.12
    items, width = text_paths("space", 700, "CLIXITE", wm_size, 0, 0, tracking=tr)
    W = max(width, xs) + pad * 2
    x_x = (W - xs) / 2
    content = f'<g transform="translate({x_x:.2f},{pad})">{x_svg(sc, xs, variant)}</g>'
    baseline = pad + xs + 44 + metrics("space", 700)["cap"] / 1000 * wm_size
    items, width = text_paths("space", 700, "CLIXITE", wm_size, (W - width) / 2, baseline, tracking=tr)
    content += paths_for(items, sc["text"])
    d_size = 16.0
    d_items, d_w = text_paths("space", 500, descriptor, d_size, 0, 0, tracking=0.22)
    d_items, d_w = text_paths("space", 500, descriptor, d_size, (W - d_w) / 2, baseline + 34, tracking=0.22)
    content += paths_for(d_items, sc["sub"] if variant != "color" else TURQ_DEEP)
    H = baseline + 34 + pad * 0.9
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def mark_x(variant="color", size=200.0):
    sc = scheme2(variant); pad = size * 0.17; inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{x_svg(sc, inner, variant)}</g>', size, size, sc["bg"])

def mark_x_tile(variant="color", size=200.0):
    """App-icon tile: ink rounded square, X inside."""
    sc = scheme2(variant); pad = size * 0.22; inner = size - 2 * pad
    bg = INK if variant in ("color", "inverse") else sc["bg"]
    scheme_in = scheme2("inverse") if variant in ("color", "inverse") else sc
    c = f'<rect width="{size}" height="{size}" rx="{size*0.22:.1f}" fill="{bg}"/>'
    c += f'<g transform="translate({pad},{pad})">{x_svg(scheme_in, inner, "color" if variant in ("color","inverse") else variant)}</g>'
    return svg_wrap(c, size, size, None)

if __name__ == "__main__":
    import os
    os.makedirs("out6", exist_ok=True)
    for v in ["color", "inverse", "mono", "mono_inverse"]:
        svg, _ = lockup_x(v); open(f"out6/n-x-lockup-{v}.svg", "w").write(svg)
        svg, _ = lockup_x_stacked(v); open(f"out6/n-x-stacked-{v}.svg", "w").write(svg)
        open(f"out6/n-x-mark-{v}.svg", "w").write(mark_x(v))
    open("out6/n-x-tile.svg", "w").write(mark_x_tile("color"))
    print("done")
