"""Round 4: 'Je connecte les dots'. Nodes and links."""
import math
from shapely.geometry import Point, LineString, box
from shapely.ops import unary_union
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2, split_i
from typo import text_paths, load, metrics

QS = 48

# ---------------------------------------------------------------------------
# J : CONSTELLATION. The X as five nodes and four links; the centre is Clixite.
# ---------------------------------------------------------------------------
def constellation_svg(sc, size=100.0, node_r=9.0, link_w=5.0, centre_r=13.0, corner_colors=None):
    s = size / 100.0
    c = (50 * s, 50 * s)
    corners = [(14 * s, 14 * s), (86 * s, 14 * s), (14 * s, 86 * s), (86 * s, 86 * s)]
    cols = corner_colors or [sc["r"], sc["y"], sc["text"], sc["text"]]
    out = []
    for p in corners:
        out.append(f'<line x1="{p[0]:.2f}" y1="{p[1]:.2f}" x2="{c[0]:.2f}" y2="{c[1]:.2f}" stroke="{sc["t"]}" stroke-width="{link_w*s:.2f}" stroke-linecap="round"/>')
    for p, col in zip(corners, cols):
        out.append(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{node_r*s:.2f}" fill="{col}"/>')
    out.append(f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{centre_r*s:.2f}" fill="{sc["t"]}"/>')
    return "".join(out)

def lockup_constellation(variant="color", descriptor="Solutions & Enterprise Architecture", word="clixite"):
    sc = scheme2(variant)
    wm_size = 160.0; pad = 44
    m = metrics("space", 600); xh = m["xh"] / m["upem"] * wm_size; asc = 0.74 * wm_size
    mark_h = asc * 1.0
    mark_x, mark_y = pad, pad
    wm_x = mark_x + mark_h + 36
    baseline = mark_y + mark_h
    items, width = text_paths("space", 600, word, wm_size, wm_x, baseline, tracking=-0.005)
    content = f'<g transform="translate({mark_x},{mark_y})">{constellation_svg(sc, mark_h)}</g>'
    content += paths_for(items, sc["text"])
    d_items, d_width = text_paths("space", 500, descriptor, 28.0, wm_x + 4, baseline + 54, tracking=0.03)
    content += paths_for(d_items, sc["sub"])
    W = wm_x + max(width, d_width) + pad; H = baseline + 54 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

def mark_only_constellation(variant="color", size=200.0):
    sc = scheme2(variant); pad = size * 0.16; inner = size - 2 * pad
    return svg_wrap(f'<g transform="translate({pad},{pad})">{constellation_svg(sc, inner)}</g>', size, size, sc["bg"])

# ---------------------------------------------------------------------------
# L : POINTS RELIÉS. In the word, each i-dot is linked to the foot of the other i; the links cross and draw the x.
# ---------------------------------------------------------------------------
def lockup_points_relies(variant="color", descriptor="Je connecte les points.", link_w=None, node=True):
    sc = scheme2(variant)
    wm_size = 170.0; pad = 44
    tt, _, upem = load("space", 600); cmap = tt.getBestCmap()
    iname, xname = cmap[ord("i")], cmap[ord("x")]
    baseline = pad + 0.80 * wm_size
    s = wm_size / upem
    stem_i, dot_i = split_i(tt, iname)
    sb = stem_i.bounds; db = dot_i.bounds
    t = (sb[2] - sb[0]) * s
    # shape the word without the x glyph drawn, keep its advance
    items, width = text_paths("space", 600, "clixite", wm_size, pad, baseline, tracking=-0.005, skip={xname})
    content = ""
    i_items = [it for it in items if it["g"] == iname]
    dots = []
    for k, it in enumerate(items):
        if it["g"] == iname:
            content += f'<path d="{geom_to_d(stem_i, s, it["x"], baseline)}" fill="{sc["text"]}"/>'
            dcx = it["x"] + (db[0] + db[2]) / 2 * s; dcy = baseline - (db[1] + db[3]) / 2 * s
            dots.append((dcx, dcy, it["x"]))
        elif it["g"] != xname:
            content += f'<path d="{it["d"]}" fill="{sc["text"]}"/>'
    (d1x, d1y, i1x), (d2x, d2y, i2x) = dots
    lw = link_w or t * 0.5
    # feet: bottom centre of each stem
    f1 = (i1x + (sb[0] + sb[2]) / 2 * s, baseline - lw / 2)
    f2 = (i2x + (sb[0] + sb[2]) / 2 * s, baseline - lw / 2)
    links = f'<line x1="{d1x:.2f}" y1="{d1y:.2f}" x2="{f2[0]:.2f}" y2="{f2[1]:.2f}" stroke="{sc["t"]}" stroke-width="{lw:.2f}" stroke-linecap="round"/>'
    links += f'<line x1="{d2x:.2f}" y1="{d2y:.2f}" x2="{f1[0]:.2f}" y2="{f1[1]:.2f}" stroke="{sc["t"]}" stroke-width="{lw:.2f}" stroke-linecap="round"/>'
    content = links + content  # links behind letters
    # dots on top
    content += f'<path d="{geom_to_d(dot_i, s, i1x, baseline)}" fill="{sc["r"]}"/>'
    content += f'<path d="{geom_to_d(dot_i, s, i2x, baseline)}" fill="{sc["y"]}"/>'
    if node:
        # crossing point
        cx = (d1x + f2[0]) / 2 ; cy = (d1y + f2[1]) / 2
        content += f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{lw*0.95:.2f}" fill="{sc["t"]}"/>'
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 4, baseline + 60, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + max(width, d_width); H = baseline + 60 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

# ---------------------------------------------------------------------------
# K : RÉSEAU. The whole word drawn as nodes and links (a graph), on the monoline module.
# ---------------------------------------------------------------------------
XH = 100.0; ASC = 142.0; R = 50.0
def arc_nodes(cx, cy, r, angles):
    return [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in angles]

def graph_word():
    """Returns nodes list [(x,y,kind)], edges [(i,j)] in units, y up."""
    nodes = []; edges = []
    def add(p, kind="n"):
        nodes.append((p[0], p[1], kind)); return len(nodes) - 1
    x = 0.0
    # c : open arc of 7 nodes
    ids = [add(p) for p in arc_nodes(x + R, R, R, [42, 90, 138, 186, 234, 282, 318])]
    edges += [(ids[k], ids[k + 1]) for k in range(len(ids) - 1)]
    x += 2 * R * 0.95 + 18
    # l
    a = add((x, 0)); b = add((x, ASC)); edges.append((a, b)); x += 34
    # i 1
    a = add((x, 0)); b = add((x, XH)); edges.append((a, b)); d1 = add((x, XH + 26), "dot1")
    x += 36
    # x : 5 nodes
    xs = XH * 0.92
    tl = add((x, XH)); tr = add((x + xs, XH)); bl = add((x, 0)); br = add((x + xs, 0)); c = add((x + xs / 2, XH / 2), "centre")
    edges += [(tl, c), (tr, c), (bl, c), (br, c)]
    x += xs + 36
    # i 2
    a = add((x, 0)); b = add((x, XH)); edges.append((a, b)); d2 = add((x, XH + 26), "dot2")
    x += 40
    # t
    top = add((x, ASC * 0.86)); mid = add((x, XH)); base = add((x, 0)); lft = add((x - 26, XH)); rgt = add((x + 30, XH))
    edges += [(top, mid), (mid, base), (lft, mid), (mid, rgt)]
    x += 30 + 26
    # e
    cx, cy = x + R, R
    ring = [add(p) for p in arc_nodes(cx, cy, R, [0, 60, 120, 180, 240, 300, 330])]
    edges += [(ring[k], ring[k + 1]) for k in range(len(ring) - 1)]
    edges.append((ring[0], ring[3]))  # the bar
    x += 2 * R
    return nodes, edges, x

def lockup_reseau(variant="color", scale=1.55, pad=48, descriptor="Je connecte les points.", node_r=11.0, link_w=5.5):
    sc = scheme2(variant)
    nodes, edges, w_units = graph_word()
    baseline = pad + (ASC + 30) * scale
    def P(n): return (pad + n[0] * scale, baseline - n[1] * scale)
    content = ""
    for i, j in edges:
        a, b = P(nodes[i]), P(nodes[j])
        content += f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{sc["t"] if variant not in ("mono","mono_inverse") else sc["text"]}" stroke-width="{link_w*scale:.2f}" stroke-linecap="round"/>'
    for n in nodes:
        p = P(n)
        col = sc["text"]; r = node_r
        if n[2] == "dot1": col = sc["r"]; r = node_r * 1.25
        if n[2] == "dot2": col = sc["y"]; r = node_r * 1.25
        if n[2] == "centre": col = sc["t"]; r = node_r * 1.35
        if variant in ("mono", "mono_inverse"): col = sc["text"]
        content += f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r*scale:.2f}" fill="{col}"/>'
    d_items, d_width = text_paths("space", 500, descriptor, 30.0, pad + 2, baseline + 62, tracking=0.01)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + max(w_units * scale, d_width); H = baseline + 62 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), (W, H)

if __name__ == "__main__":
    import os
    os.makedirs("out5", exist_ok=True)
    for v in ["color", "inverse", "mono"]:
        svg, _ = lockup_constellation(v); open(f"out5/j-constellation-lockup-{v}.svg", "w").write(svg)
        open(f"out5/j-constellation-mark-{v}.svg", "w").write(mark_only_constellation(v))
        svg, _ = lockup_points_relies(v); open(f"out5/l-points-lockup-{v}.svg", "w").write(svg)
        svg, _ = lockup_reseau(v); open(f"out5/k-reseau-lockup-{v}.svg", "w").write(svg)
    print("done")
