"""Concept H : JOINTURE. In 'clixite', the x spans exactly between the two i stems: i x i becomes |><| , the bowtie,
the relational JOIN operator and a bridge truss. The two enclosed counters carry rose and signal."""
import math
from shapely.geometry import Polygon, LineString, box, MultiPolygon
from shapely.ops import unary_union
from typo import text_paths, load, metrics, glyph_bounds
from geom import glyph_polygon, geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2, split_i

def bowtie_parts(W, H, t):
    """Bars and counters inside a W x H box (font units, y up). Returns (bars_geom, left_tri, right_tri)."""
    rect = box(0, 0, W, H)
    a = LineString([(0, 0), (W, H)]).buffer(t / 2, cap_style=2, join_style=2)
    b = LineString([(0, H), (W, 0)]).buffer(t / 2, cap_style=2, join_style=2)
    bars = unary_union([a, b]).intersection(rect)
    rest = rect.difference(bars)
    pieces = list(rest.geoms) if isinstance(rest, MultiPolygon) else [rest]
    pieces = sorted(pieces, key=lambda p: p.centroid.x)
    left = pieces[0]; right = pieces[-1]
    return bars, left, right

def jointure_pieces(wm_size, x0, baseline, stem_gap=None):
    tt, _, upem = load("space", 600)
    cmap = tt.getBestCmap()
    iname, xname = cmap[ord("i")], cmap[ord("x")]
    m = metrics("space", 600)
    xh = m["xh"]  # 486 units
    stem_i, dot_i = split_i(tt, iname)
    sb = stem_i.bounds  # stem bounds in units: (xmin, ymin, xmax, ymax)
    t = sb[2] - sb[0]   # stem width in units
    W = stem_gap or xh  # bowtie width between stems = x-height -> 45 degrees
    s = wm_size / upem
    # layout: 'cl' then i then bowtie then i then 'te'
    left, lw = text_paths("space", 600, "cl", wm_size, x0, baseline, tracking=-0.005)
    # first i placed right after 'cl' with normal advance
    cl_adv = lw
    i1_x = x0 + cl_adv + (-0.005 * upem) * s + 0  # continue tracking
    # use natural pair spacing: shape 'cli' to get the i offset
    cli, cli_w = text_paths("space", 600, "cli", wm_size, x0, baseline, tracking=-0.005)
    i1_x = cli[-1]["x"]
    stem_right = i1_x + sb[2] * s          # right edge of first stem (px)
    bow_x0 = stem_right                     # bowtie starts flush at the stem edge
    bow_x1 = bow_x0 + W * s
    i2_x = bow_x1 - sb[0] * s               # second i so its stem left edge is flush with bowtie end
    # 'te' after second i with natural 'ite' spacing: measure 'it' pair offset
    ite, _ = text_paths("space", 600, "ite", wm_size, 0, baseline, tracking=-0.005)
    t_off = ite[1]["x"] - ite[0]["x"]
    e_off = ite[2]["x"] - ite[0]["x"]
    te, _ = text_paths("space", 600, "te", wm_size, i2_x + t_off, baseline, tracking=-0.005)
    pieces = []
    for it in left:
        pieces.append(("text", it["d"]))
    for k, ix in enumerate([i1_x, i2_x]):
        pieces.append(("stem", geom_to_d(stem_i, s, ix, baseline)))
        pieces.append(("dot1" if k == 0 else "dot2", geom_to_d(dot_i, s, ix, baseline)))
    bars, ltri, rtri = bowtie_parts(W, xh, t)
    pieces.append(("x", geom_to_d(bars, s, bow_x0, baseline)))
    pieces.append(("ltri", geom_to_d(ltri, s, bow_x0, baseline)))
    pieces.append(("rtri", geom_to_d(rtri, s, bow_x0, baseline)))
    for it in te:
        pieces.append(("text", it["d"]))
    total_w = (te[-1]["x"] + te[-1]["adv"]) - x0
    return pieces, total_w

def lockup_jointure(variant="color", descriptor="Architecture de solutions", fill_counters=True, dots_colored=True):
    sc = scheme2(variant)
    wm_size = 170.0
    pad = 44
    baseline = pad + 0.80 * wm_size
    pieces, width = jointure_pieces(wm_size, pad, baseline)
    colors = dict(text=sc["text"], stem=sc["text"], x=sc["t"],
                  dot1=sc["r"] if dots_colored else sc["text"], dot2=sc["y"] if dots_colored else sc["text"],
                  ltri=sc["r"] if fill_counters else "none", rtri=sc["y"] if fill_counters else "none")
    if variant in ("mono", "mono_inverse"):
        colors.update(ltri="none", rtri="none", dot1=sc["text"], dot2=sc["text"])
    content = "".join(f'<path d="{d}" fill="{colors[k]}"/>' for k, d in pieces if d and colors[k] != "none")
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 4, baseline + 60, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + max(width, d_width)
    H = baseline + 60 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)

def mark_only_jointure(variant="color", size=200.0, with_dots=False):
    """|><| : the two stems and the bowtie, counters in rose and signal."""
    sc = scheme2(variant)
    tt, _, upem = load("space", 600)
    iname = tt.getBestCmap()[ord("i")]
    stem_i, dot_i = split_i(tt, iname)
    sb = stem_i.bounds; t = sb[2] - sb[0]
    m = metrics("space", 600); xh = m["xh"]
    W = xh
    total_w = t + W + t
    target = size * 0.62
    s = target / total_w
    x0 = (size - total_w * s) / 2
    base = size / 2 + xh * s / 2
    bars, ltri, rtri = bowtie_parts(W, xh, t)
    stem = box(0, 0, t, xh)
    content = f'<path d="{geom_to_d(stem, s, x0, base)}" fill="{sc["text"]}"/>'
    content += f'<path d="{geom_to_d(stem, s, x0 + (t + W) * s, base)}" fill="{sc["text"]}"/>'
    content += f'<path d="{geom_to_d(bars, s, x0 + t * s, base)}" fill="{sc["t"]}"/>'
    if variant not in ("mono", "mono_inverse"):
        content += f'<path d="{geom_to_d(ltri, s, x0 + t * s, base)}" fill="{sc["r"]}"/>'
        content += f'<path d="{geom_to_d(rtri, s, x0 + t * s, base)}" fill="{sc["y"]}"/>'
    return svg_wrap(content, size, size, sc["bg"])

if __name__ == "__main__":
    import os
    os.makedirs("out3", exist_ok=True)
    for v in ["color", "inverse", "mono", "mono_inverse"]:
        svg, d = lockup_jointure(v); open(f"out3/h-jointure-lockup-{v}.svg", "w").write(svg)
        open(f"out3/h-jointure-mark-{v}.svg", "w").write(mark_only_jointure(v))
    svg, d = lockup_jointure("color", fill_counters=False); open("out3/h-jointure-lockup-color-open.svg", "w").write(svg)
    print("done")
