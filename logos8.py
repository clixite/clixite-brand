"""Piste O : le X artistique. Cinq natures de X, toujours central."""
import math, random
from shapely.geometry import Polygon, LineString, MultiPoint, Point, box
from shapely.ops import unary_union, triangulate
from shapely import affinity
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from logos7 import bar45, flip, lockup_central, lockup_side, mark
from typo import text_paths, metrics

INDIGO = "#193776"; ROSE_DEEP = "#D81B60"; TURQ_LIGHT = "#7FD6EA"; ROSE_LIGHT = "#FF9BBF"; SIGNAL_DEEP = "#E6B800"

def mix(h1, h2, k):
    a = [int(h1[i:i+2], 16) for i in (1, 3, 5)]; b = [int(h2[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02X%02X%02X" % tuple(int(x + (y - x) * k) for x, y in zip(a, b))

# ---------------------------------------------------------------------------
# O1 RELIEF : the X as one solid, extruded in isometric; the front face carries the trio.
# ---------------------------------------------------------------------------
def x_relief(sc, size, variant="color", t=23.0, depth=11.0):
    t = t * size / 100; d = depth * size / 100
    a = bar45(size, t, 1, "flat"); b = bar45(size, t, -1, "flat")
    solid = unary_union([a, b])
    front = affinity.translate(solid, -d * 0.5, d * 0.5)   # lifted up-left so the extrusion goes down-right
    steps = 40
    sweep = unary_union([affinity.translate(front, d * 0.5 * k / steps, -d * 0.5 * k / steps) for k in range(steps + 1)])
    fa = affinity.translate(a, -d * 0.5, d * 0.5); fb = affinity.translate(b, -d * 0.5, d * 0.5)
    ov = fa.intersection(fb)
    if variant in ("mono", "mono_inverse"):
        side = sc["text"]; ca = cb = sc["bg"] if False else (PAPER if variant == "mono" else INK); cc = ca
        out = f'<path d="{flip(sweep, size)}" fill="{side}"/>'
        out += f'<path d="{flip(front.buffer(-t*0.09), size)}" fill="{ca}"/>'
        out += f'<path d="{flip(front.buffer(-t*0.09).buffer(-t*0.1), size)}" fill="{side}"/>'
        return out
    side = INDIGO if variant == "color" else INK_TINT
    out = f'<path d="{flip(sweep, size)}" fill="{side}"/>'
    out += f'<path d="{flip(fa, size)}" fill="{sc["t"]}"/>'
    out += f'<path d="{flip(fb.difference(fa), size)}" fill="{sc["r"]}"/>'
    out += f'<path d="{flip(ov, size)}" fill="{sc["y"]}"/>'
    return out

# ---------------------------------------------------------------------------
# O2 MOIRÉ : each bar is a bundle of fine lines along its axis; the crossing weaves a lattice.
# ---------------------------------------------------------------------------
def x_moire(sc, size, variant="color", t=30.0, n=8, lw=1.9):
    t = t * size / 100; lw = lw * size / 100
    out = ""
    ca, cb = (sc["text"], sc["text"]) if variant in ("mono", "mono_inverse") else (sc["t"], sc["r"])
    for direction, col in ((1, ca), (-1, cb)):
        bar = bar45(size, t, direction, "perp")
        lines = []
        for k in range(n):
            off = -t / 2 + lw / 2 + k * (t - lw) / (n - 1)
            if direction == 1:
                p0 = (0 - off / math.sqrt(2), 0 + off / math.sqrt(2)); p1 = (size - off / math.sqrt(2), size + off / math.sqrt(2))
            else:
                p0 = (0 - off / math.sqrt(2), size - off / math.sqrt(2)); p1 = (size - off / math.sqrt(2), 0 - off / math.sqrt(2))
            lines.append(LineString([p0, p1]).buffer(lw / 2, cap_style=1).intersection(bar))
        out += f'<path d="{flip(unary_union(lines), size)}" fill="{col}"/>'
    if variant == "color" or variant == "inverse":
        c = Point(size / 2, size / 2).buffer(t * 0.16, quad_segs=24)
        out += f'<path d="{flip(c, size)}" fill="{sc["y"]}"/>'
    return out

# ---------------------------------------------------------------------------
# O3 FACETTES : the X as a cut mineral; triangular facets in tints, hairline joints.
# ---------------------------------------------------------------------------
def x_facettes(sc, size, variant="color", t=26.0, seed=7):
    t = t * size / 100
    a = bar45(size, t, 1, "perp"); b = bar45(size, t, -1, "perp")
    solid = unary_union([a, b])
    pts = list(solid.exterior.coords)[:-1]
    rnd = random.Random(seed)
    extra = [(size / 2, size / 2)]
    for cx, cy in [(size * 0.25, size * 0.25), (size * 0.75, size * 0.75), (size * 0.25, size * 0.75), (size * 0.75, size * 0.25)]:
        extra.append((cx + rnd.uniform(-3, 3) * size / 100, cy + rnd.uniform(-3, 3) * size / 100))
    tris = triangulate(MultiPoint(pts + extra))
    out = ""
    centre_r = t * 0.55
    for tri in tris:
        piece = tri.intersection(solid)
        if piece.is_empty or piece.area < 1e-3: continue
        c = piece.centroid
        d_c = math.hypot(c.x - size / 2, c.y - size / 2)
        # which arm: distance to the two axes
        da = abs((c.x - c.y)) / math.sqrt(2); db = abs((c.x + c.y - size)) / math.sqrt(2)
        shade = rnd.choice([0.0, 0.18, 0.36])
        if variant in ("mono", "mono_inverse"):
            base = sc["text"]; col = mix(base, PAPER if variant == "mono" else INK, shade * 0.9)
        elif d_c < centre_r:
            col = mix(sc["y"], SIGNAL_DEEP, shade)
        elif da < db:
            col = mix(sc["t"], TURQ_DEEP if shade < 0.3 else TURQ_LIGHT, shade if shade < 0.3 else 0.6)
        else:
            col = mix(sc["r"], ROSE_DEEP if shade < 0.3 else ROSE_LIGHT, shade if shade < 0.3 else 0.6)
        piece = piece.buffer(-size * 0.006, join_style=2)
        if piece.is_empty: continue
        out += f'<path d="{flip(piece, size)}" fill="{col}"/>'
    return out

# ---------------------------------------------------------------------------
# O4 FLUIDE : two capsules that fuse like liquid at the crossing.
# ---------------------------------------------------------------------------
def x_fluide(sc, size, variant="color", t=24.0, fillet=9.0):
    t = t * size / 100; f = fillet * size / 100
    inset = t / 2
    a = LineString([(inset, inset), (size - inset, size - inset)]).buffer(t / 2, cap_style=1, quad_segs=32)
    b = LineString([(inset, size - inset), (size - inset, inset)]).buffer(t / 2, cap_style=1, quad_segs=32)
    body = unary_union([a, b]).buffer(f, join_style=1, quad_segs=32).buffer(-f, join_style=1, quad_segs=32)
    if variant in ("mono", "mono_inverse"):
        return f'<path d="{flip(body, size)}" fill="{sc["text"]}"/>'
    inner = body.buffer(-t * 0.14, join_style=1)
    out = f'<path d="{flip(body, size)}" fill="{sc["t"]}"/>'
    out += f'<path d="{flip(b.intersection(inner), size)}" fill="{sc["r"]}"/>'
    core = Point(size / 2, size / 2).buffer(t * 0.36, quad_segs=32)
    out += f'<path d="{flip(core, size)}" fill="{sc["y"]}"/>'
    return out

# ---------------------------------------------------------------------------
# O5 TRAIT : two brush strokes, thick to thin, slightly curved; the crossing deepens to indigo.
# ---------------------------------------------------------------------------
def brush(p0, p1, w0, w1, bend, steps=48):
    (x0, y0), (x1, y1) = p0, p1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy); nx, ny = -dy / L, dx / L
    cx, cy = mx + nx * bend, my + ny * bend
    left, right = [], []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        tx = 2 * (1 - u) * (cx - x0) + 2 * u * (x1 - cx); ty = 2 * (1 - u) * (cy - y0) + 2 * u * (y1 - cy)
        tl = math.hypot(tx, ty); ox, oy = -ty / tl, tx / tl
        w = w0 + (w1 - w0) * (u ** 1.3)
        w *= (0.55 + 0.45 * math.sin(math.pi * min(1, u * 1.15)) )  # soft entry
        left.append((x + ox * w / 2, y + oy * w / 2)); right.append((x - ox * w / 2, y - oy * w / 2))
    return Polygon(left + right[::-1]).buffer(0)

def x_trait(sc, size, variant="color"):
    s = size / 100
    a = brush((6 * s, 92 * s), (94 * s, 8 * s), 30 * s, 6 * s, -7 * s)    # "/" from bottom-left, pulled up-right
    b = brush((8 * s, 8 * s), (92 * s, 92 * s), 30 * s, 6 * s, 7 * s)     # "\" from top-left, pulled down-right
    ov = a.intersection(b)
    if variant in ("mono", "mono_inverse"):
        return f'<path d="{flip(unary_union([a, b]), size)}" fill="{sc["text"]}"/>'
    out = f'<path d="{flip(a, size)}" fill="{sc["t"]}"/><path d="{flip(b, size)}" fill="{sc["r"]}"/>'
    out += f'<path d="{flip(ov, size)}" fill="{INDIGO if variant == "color" else sc["y"]}"/>'
    return out

VARIANTS = {"o1-relief": x_relief, "o2-moire": x_moire, "o3-facettes": x_facettes, "o4-fluide": x_fluide, "o5-trait": x_trait}

if __name__ == "__main__":
    import os
    os.makedirs("out8", exist_ok=True)
    for key, gen in VARIANTS.items():
        for v in ["color", "inverse", "mono"]:
            open(f"out8/{key}-mark-{v}.svg", "w").write(mark(gen, v))
            svg, _ = lockup_central(gen, v); open(f"out8/{key}-central-{v}.svg", "w").write(svg)
    print("done")

# ---------------------------------------------------------------------------
# O2b INTERFÉRENCE : a line field under each bar, the second rotated a few degrees; the crossing produces true moiré.
# ---------------------------------------------------------------------------
def x_interference(sc, size, variant="color", t=30.0, pitch=3.0, lw=1.5, angle=6.0):
    t = t * size / 100; pitch = pitch * size / 100; lw = lw * size / 100
    a = bar45(size, t, 1, "perp"); b = bar45(size, t, -1, "perp")
    def field(rot):
        lines = []
        n = int(size * 1.6 / pitch)
        for k in range(-n, n + 1):
            x = size / 2 + k * pitch
            lines.append(box(x - lw / 2, -size, x + lw / 2, 2 * size))
        f = unary_union(lines)
        return affinity.rotate(f, rot, origin=(size / 2, size / 2))
    ca, cb = (sc["text"], sc["text"]) if variant in ("mono", "mono_inverse") else (sc["t"], sc["r"])
    fa = field(-angle / 2).intersection(a); fb = field(angle / 2).intersection(b)
    out = f'<path d="{flip(fa, size)}" fill="{ca}"/><path d="{flip(fb, size)}" fill="{cb}"/>'
    return out

VARIANTS["o6-interference"] = x_interference
