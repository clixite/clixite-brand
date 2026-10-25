"""Clixite logo concepts, generated as clean vector SVG."""
import math
from shapely.geometry import Point, Polygon, LineString
from shapely.ops import unary_union
from shapely import affinity
from typo import text_paths, load, metrics
from geom import glyph_polygon, geom_to_d, band, chevron, rounded_rect

# ---- Palette -------------------------------------------------------------
INK = "#0B2239"        # Encre : fond sombre, texte
TURQ = "#19B3D9"       # Turquoise Clixite
TURQ_DEEP = "#0C7893"  # Turquoise profond : texte sur fond clair
PAPER = "#F6F5F0"      # Papier : fond clair
SIGNAL = "#FFD233"     # Jaune signal : accent, CTA
ROSE = "#FF4F8B"       # Rose : accent secondaire (écosystème)
MIST = "#CDD5DD"       # Brume : gris clair
SLATE = "#4B5A6B"      # Ardoise : texte secondaire
INK_TINT = "#1F3A5A"   # Encre teintée : modules secondaires sur fond sombre


def svg_wrap(content, w, h, bg=None, pad=0):
    bgrect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" '
            f'width="{w:.1f}" height="{h:.1f}">{bgrect}{content}</svg>')


def paths_for(items, fill):
    return "".join(f'<path d="{it["d"]}" fill="{fill}"/>' for it in items if it["d"])


# ---- Scheme helper: picks colours per variant ------------------------------
def scheme(variant):
    """variant: color | inverse | mono | mono_inverse"""
    if variant == "color":
        return dict(bg=PAPER, text=INK, primary=TURQ, secondary=INK, accent=SIGNAL, muted=MIST, sub=TURQ_DEEP)
    if variant == "inverse":
        return dict(bg=INK, text=PAPER, primary=TURQ, secondary=PAPER, accent=SIGNAL, muted=INK_TINT, sub=TURQ)
    if variant == "mono":
        return dict(bg=PAPER, text=INK, primary=INK, secondary=INK, accent=PAPER, muted=MIST, sub=INK)
    if variant == "mono_inverse":
        return dict(bg=INK, text=PAPER, primary=PAPER, secondary=PAPER, accent=INK, muted=INK_TINT, sub=PAPER)
    raise ValueError(variant)


# =============================================================================
# Concept A : CARREFOUR  (évolution du X historique : deux chevrons qui se croisent)
# =============================================================================
def mark_carrefour(sc, size=100.0):
    """Returns svg content for a size x size mark at origin."""
    s = size / 100.0
    hw = 10.5 * s  # half stroke width
    left = chevron([(13 * s, 12 * s), (56 * s, 50 * s), (13 * s, 88 * s)], hw)
    right = chevron([(87 * s, 12 * s), (44 * s, 50 * s), (87 * s, 88 * s)], hw)
    overlap = left.intersection(right)
    out = []
    out.append(f'<path d="{geom_to_d(left, flip=False)}" fill="{sc["primary"]}"/>')
    out.append(f'<path d="{geom_to_d(right.difference(left), flip=False)}" fill="{sc["secondary"]}"/>')
    out.append(f'<path d="{geom_to_d(overlap, flip=False)}" fill="{sc["accent"]}"/>')
    return "".join(out)


def lockup_carrefour(variant="color", descriptor="SOLUTIONS & ENTERPRISE ARCHITECTURE"):
    sc = scheme(variant)
    size = 180.0
    wm_size = 150.0
    m = metrics("space", 700)
    cap = m["cap"] / m["upem"] * wm_size
    mark_h = cap * 1.25
    pad = 40
    mark_x, mark_y = pad, pad
    # wordmark
    wm_x = mark_x + mark_h + 36
    baseline = mark_y + (mark_h + cap) / 2
    items, width = text_paths("space", 700, "CLIXITE", wm_size, wm_x, baseline, tracking=0.05)
    # descriptor sized to the wordmark width
    d_size = 28.0
    d_items, d_width = text_paths("space", 500, descriptor, d_size, wm_x, baseline + 44, tracking=0.19)
    # rescale descriptor to match wordmark width
    k = width / d_width
    d_size2 = d_size * k
    d_items, d_width = text_paths("space", 500, descriptor, d_size2, wm_x, baseline + 36 + d_size2, tracking=0.19)
    W = wm_x + width + pad
    H = baseline + 36 + d_size2 + pad * 0.9
    content = f'<g transform="translate({mark_x},{mark_y})">{mark_carrefour(sc, mark_h)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"])
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_carrefour(variant="color", size=200.0):
    sc = scheme(variant)
    pad = size * 0.18
    inner = size - 2 * pad
    content = f'<g transform="translate({pad},{pad})">{mark_carrefour(sc, inner)}</g>'
    return svg_wrap(content, size, size, sc["bg"])


# =============================================================================
# Concept B : JONCTION  (mot-symbole, le x devient une jonction de deux tracés)
# =============================================================================
def split_x(tt, gname, gap_ratio=0.22):
    """Split the real 'x' glyph into slash (/) and backslash (\\) parts, with a bridge gap."""
    g = glyph_polygon(tt, gname)
    minx, miny, maxx, maxy = g.bounds
    # terminal centres: sample at bottom and top
    def centres(y):
        line = LineString([(minx - 10, y), (maxx + 10, y)])
        inter = g.intersection(line)
        segs = list(inter.geoms) if hasattr(inter, "geoms") else [inter]
        segs = sorted(segs, key=lambda s: s.bounds[0])
        return [((s.bounds[0] + s.bounds[2]) / 2, y) for s in segs], [(s.bounds[2] - s.bounds[0]) for s in segs]
    (bl, br), bw = centres(miny + 2)
    (tl, tr), tw = centres(maxy - 2)
    slash_line = (bl, tr)
    back_line = (br, tl)
    # stroke thickness perpendicular: horizontal terminal width * sin(angle)
    ang = math.atan2(tr[1] - bl[1], tr[0] - bl[0])
    thick = bw[0] * math.sin(ang)
    hw = thick / 2
    slash_band = band(slash_line[0], slash_line[1], hw * 1.02)
    back_band = band(back_line[0], back_line[1], hw * 1.02)
    slash = g.intersection(slash_band)
    gap = slash_band.buffer(thick * gap_ratio)
    back = g.intersection(back_band).difference(gap)
    # the crossing centre for a node
    cx = (bl[0] + tr[0]) / 2
    cy = (bl[1] + tr[1]) / 2
    return slash, back, (cx, cy), thick


def lockup_jonction(variant="color", descriptor="Architecture de solutions · depuis 2005", node=False):
    sc = scheme(variant)
    wm_size = 170.0
    pad = 44
    tt, _, upem = load("space", 600)
    cmap = tt.getBestCmap()
    xname = cmap[ord("x")]
    m = metrics("space", 600)
    asc = m["asc"] / upem * wm_size
    baseline = pad + 0.80 * wm_size
    items, width = text_paths("space", 600, "clixite", wm_size, pad, baseline, tracking=-0.005, skip={xname})
    s = wm_size / upem
    content = paths_for(items, sc["text"])
    for it in items:
        if it["g"] == xname:
            slash, back, (cx, cy), thick = split_x(tt, xname)
            content += f'<path d="{geom_to_d(slash, s, it["x"], baseline)}" fill="{sc["primary"]}"/>'
            content += f'<path d="{geom_to_d(back, s, it["x"], baseline)}" fill="{sc["secondary"]}"/>'
            if node:
                r = thick * 0.26 * s
                content += f'<circle cx="{it["x"] + cx * s:.2f}" cy="{baseline - cy * s:.2f}" r="{r:.2f}" fill="{sc["accent"]}"/>'
    # descriptor
    d_size = 30.0
    d_items, d_width = text_paths("space", 500, descriptor, d_size, pad + 4, baseline + 62, tracking=0.02)
    content += paths_for(d_items, sc["sub"])
    W = pad * 2 + width
    H = baseline + 62 + pad * 0.75
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_jonction(variant="color", size=200.0, node=False):
    """The junction x alone, as a square mark."""
    sc = scheme(variant)
    tt, _, upem = load("space", 600)
    xname = tt.getBestCmap()[ord("x")]
    slash, back, (cx, cy), thick = split_x(tt, xname)
    g = unary_union([slash, back])
    minx, miny, maxx, maxy = g.bounds
    gw, gh = maxx - minx, maxy - miny
    target = size * 0.62
    s = target / max(gw, gh)
    dx = (size - gw * s) / 2 - minx * s
    dy = (size + gh * s) / 2 + miny * s
    content = f'<path d="{geom_to_d(slash, s, dx, dy)}" fill="{sc["primary"]}"/>'
    content += f'<path d="{geom_to_d(back, s, dx, dy)}" fill="{sc["secondary"]}"/>'
    if node:
        content += f'<circle cx="{dx + cx * s:.2f}" cy="{dy - cy * s:.2f}" r="{thick * 0.26 * s:.2f}" fill="{sc["accent"]}"/>'
    return svg_wrap(content, size, size, sc["bg"])


# =============================================================================
# Concept C : TRAME  (grille 3x3 de modules, le X est tracé dans la trame)
# =============================================================================
def mark_trame(sc, size=100.0):
    s = size / 100.0
    mod, gap = 26.0 * s, 11.0 * s
    r = 5.0 * s
    out = []
    for row in range(3):
        for col in range(3):
            x = col * (mod + gap)
            y = row * (mod + gap)
            on_x = (row == col) or (row + col == 2)
            fill = sc["primary"] if on_x else sc["muted"]
            if row == 1 and col == 1:
                fill = sc["accent"] if sc["accent"] not in (PAPER, INK) else sc["primary"]
            out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{mod:.2f}" height="{mod:.2f}" rx="{r:.2f}" fill="{fill}"/>')
    return "".join(out)


def lockup_trame(variant="color", descriptor="Architecture & transformation"):
    sc = scheme(variant)
    wm_size = 160.0
    pad = 44
    m = metrics("space", 600)
    cap = m["cap"] / m["upem"] * wm_size
    mark_h = cap * 1.12
    mark_x, mark_y = pad, pad
    wm_x = mark_x + mark_h + 34
    baseline = mark_y + (mark_h + cap) / 2
    items, width = text_paths("space", 600, "Clixite", wm_size, wm_x, baseline, tracking=-0.01)
    d_size = 30.0
    d_items, d_width = text_paths("space", 400, descriptor, d_size, wm_x + 6, baseline + 56, tracking=0.01)
    content = f'<g transform="translate({mark_x},{mark_y})">{mark_trame(sc, mark_h)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"])
    W = wm_x + max(width, d_width) + pad
    H = baseline + 56 + pad * 0.8
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_trame(variant="color", size=200.0):
    sc = scheme(variant)
    pad = size * 0.2
    inner = size - 2 * pad
    content = f'<g transform="translate({pad},{pad})">{mark_trame(sc, inner)}</g>'
    return svg_wrap(content, size, size, sc["bg"])


# =============================================================================
# Concept D : CONNECTEUR  (un C en anneau épais, ouvert, et un module qui s'y branche)
# =============================================================================
def mark_connecteur(sc, size=100.0):
    s = size / 100.0
    cx, cy = 50 * s, 50 * s
    R, w = 40 * s, 19 * s
    ring = Point(cx, cy).buffer(R + w / 2, quad_segs=64).difference(Point(cx, cy).buffer(R - w / 2, quad_segs=64))
    # opening on the right, +/- 42 degrees
    a = math.radians(42)
    far = 200 * s
    wedge = Polygon([(cx, cy), (cx + far * math.cos(a), cy - far * math.sin(a)), (cx + far, cy - far * math.sin(a)),
                     (cx + far, cy + far * math.sin(a)), (cx + far * math.cos(a), cy + far * math.sin(a))])
    c_shape = ring.difference(wedge)
    # the plug: a rounded module sitting in the opening, on the ring's radius
    msz = w * 1.18
    plug = rounded_rect(cx + R - msz / 2, cy - msz / 2, msz, msz, 4.5 * s)
    out = [f'<path d="{geom_to_d(c_shape, flip=False)}" fill="{sc["secondary"]}"/>',
           f'<path d="{geom_to_d(plug, flip=False)}" fill="{sc["primary"]}"/>']
    return "".join(out)


def lockup_connecteur(variant="color", descriptor="Procurement · Compliance · Architecture"):
    sc = scheme(variant)
    wm_size = 160.0
    pad = 44
    m = metrics("space", 500)
    xh = m["xh"] / m["upem"] * wm_size
    asc = 0.72 * wm_size
    mark_h = asc * 1.02
    mark_x, mark_y = pad, pad
    wm_x = mark_x + mark_h + 30
    baseline = mark_y + mark_h - (mark_h - asc) / 2
    items, width = text_paths("space", 500, "clixite", wm_size, wm_x, baseline, tracking=-0.005)
    d_size = 28.0
    d_items, d_width = text_paths("space", 500, descriptor, d_size, wm_x + 4, baseline + 54, tracking=0.04)
    content = f'<g transform="translate({mark_x},{mark_y})">{mark_connecteur(sc, mark_h)}</g>'
    content += paths_for(items, sc["text"]) + paths_for(d_items, sc["sub"])
    W = wm_x + max(width, d_width) + pad
    H = baseline + 54 + pad * 0.8
    return svg_wrap(content, W, H, sc["bg"]), dict(W=W, H=H)


def mark_only_connecteur(variant="color", size=200.0):
    sc = scheme(variant)
    pad = size * 0.16
    inner = size - 2 * pad
    content = f'<g transform="translate({pad},{pad})">{mark_connecteur(sc, inner)}</g>'
    return svg_wrap(content, size, size, sc["bg"])


CONCEPTS = {
    "a-carrefour": (lockup_carrefour, mark_only_carrefour),
    "b-jonction": (lockup_jonction, mark_only_jonction),
    "c-trame": (lockup_trame, mark_only_trame),
    "d-connecteur": (lockup_connecteur, mark_only_connecteur),
}

if __name__ == "__main__":
    import os
    os.makedirs("out", exist_ok=True)
    for key, (lock, mark) in CONCEPTS.items():
        for v in ["color", "inverse", "mono", "mono_inverse"]:
            svg, dims = lock(v)
            open(f"out/{key}-lockup-{v}.svg", "w").write(svg)
            open(f"out/{key}-mark-{v}.svg", "w").write(mark(v))
    print("done")
