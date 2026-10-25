"""Raffinement O1 Relief et O3 Interférence, plus un hybride."""
import math
from shapely.geometry import box, Point, LineString
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, TURQ, TURQ_DEEP, PAPER, SIGNAL, ROSE, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos2 import scheme2
from logos7 import bar45, flip, lockup_central, lockup_side, mark
from logos8 import INDIGO, ROSE_DEEP

def sweep_of(shape, dx, dy, steps=48):
    return unary_union([affinity.translate(shape, dx * k / steps, dy * k / steps) for k in range(steps + 1)])

# ---- RELIEF variants ------------------------------------------------------
def relief(sc, size, variant="color", t=23.0, depth=11.0, cut="flat", side="indigo", key=True, direction=(1, -1), corner=0.0):
    t = t * size / 100; d = depth * size / 100
    a = bar45(size, t, 1, cut, r=corner * size / 100); b = bar45(size, t, -1, cut, r=corner * size / 100)
    dx, dy = direction[0] * d * 0.5, direction[1] * d * 0.5   # extrusion vector in y-up units (dy negative = down on screen)
    lift = (-dx, -dy)
    fa = affinity.translate(a, *lift); fb = affinity.translate(b, *lift)
    front = unary_union([fa, fb]); ov = fa.intersection(fb)
    if variant in ("mono", "mono_inverse"):
        sw = sweep_of(front, dx, dy)
        face = PAPER if variant == "mono" else INK
        return (f'<path d="{flip(sw, size)}" fill="{sc["text"]}"/>'
                f'<path d="{flip(front, size)}" fill="{face}"/>'
                f'<path d="{flip(front.buffer(-t*0.13, join_style=2), size)}" fill="{sc["text"]}"/>')
    if side == "indigo":
        sw = sweep_of(front, dx, dy)
        out = f'<path d="{flip(sw, size)}" fill="{INDIGO if variant == "color" else INK_TINT}"/>'
    else:  # per-bar deep tones
        swa = sweep_of(fa, dx, dy); swb = sweep_of(fb, dx, dy)
        out = f'<path d="{flip(swb, size)}" fill="{ROSE_DEEP}"/><path d="{flip(swa.difference(fb), size)}" fill="{TURQ_DEEP}"/>'
    out += f'<path d="{flip(fa, size)}" fill="{sc["t"]}"/><path d="{flip(fb.difference(fa), size)}" fill="{sc["r"]}"/>'
    if key:
        out += f'<path d="{flip(ov, size)}" fill="{sc["y"]}"/>'
    return out

# ---- INTERFERENCE variants ------------------------------------------------
def field(size, pitch, lw, rot):
    lines = []
    n = int(size * 1.6 / pitch)
    for k in range(-n, n + 1):
        x = size / 2 + k * pitch
        lines.append(box(x - lw / 2, -size, x + lw / 2, 2 * size))
    return affinity.rotate(unary_union(lines), rot, origin=(size / 2, size / 2))

def interference(sc, size, variant="color", t=30.0, pitch=3.0, lw=1.5, angle=6.0, cut="perp", lens=None, colors=("t", "r"), corner=0.0):
    t = t * size / 100; pitch = pitch * size / 100; lw = lw * size / 100
    a = bar45(size, t, 1, cut, r=corner * size / 100); b = bar45(size, t, -1, cut, r=corner * size / 100)
    if variant in ("mono", "mono_inverse"):
        ca = cb = sc["text"]
    else:
        ca, cb = sc[colors[0]], sc[colors[1]]
    out = ""
    if lens == "signal" and variant in ("color", "inverse"):
        out += f'<path d="{flip(a.intersection(b), size)}" fill="{sc["y"]}"/>'
    if lens == "ink":
        out += f'<path d="{flip(a.intersection(b), size)}" fill="{sc["text"]}"/>'
    fa = field(size, pitch, lw, -angle / 2).intersection(a); fb = field(size, pitch, lw, angle / 2).intersection(b)
    out += f'<path d="{flip(fa, size)}" fill="{ca}"/><path d="{flip(fb, size)}" fill="{cb}"/>'
    return out

# ---- HYBRID : relief whose front face is an interference surface ----------
def hybrid(sc, size, variant="color", t=26.0, depth=11.0, pitch=2.8, lw=1.3, angle=7.0):
    t_ = t * size / 100; d = depth * size / 100
    a = bar45(size, t_, 1, "perp"); b = bar45(size, t_, -1, "perp")
    dx, dy = d * 0.5, -d * 0.5
    fa = affinity.translate(a, -dx, -dy); fb = affinity.translate(b, -dx, -dy)
    front = unary_union([fa, fb])
    sw = sweep_of(front, dx, dy)
    if variant in ("mono", "mono_inverse"):
        face = PAPER if variant == "mono" else INK
        return (f'<path d="{flip(sw, size)}" fill="{sc["text"]}"/><path d="{flip(front, size)}" fill="{face}"/>'
                f'<path d="{flip(field(size, pitch*size/100, lw*size/100, -angle/2).intersection(fa), size)}" fill="{sc["text"]}"/>'
                f'<path d="{flip(field(size, pitch*size/100, lw*size/100, angle/2).intersection(fb), size)}" fill="{sc["text"]}"/>')
    out = f'<path d="{flip(sw, size)}" fill="{INK if variant == "color" else INK_TINT}"/>'
    out += f'<path d="{flip(front, size)}" fill="{sc["bg"] if variant == "color" else INK}"/>'
    ffa = field(size, pitch * size / 100, lw * size / 100, -angle / 2).intersection(fa)
    ffb = field(size, pitch * size / 100, lw * size / 100, angle / 2).intersection(fb)
    out += f'<path d="{flip(ffa, size)}" fill="{sc["t"]}"/><path d="{flip(ffb, size)}" fill="{sc["r"]}"/>'
    return out

RELIEF = {
    "r1-base":    lambda sc, s, v="color": relief(sc, s, v),
    "r2-tons":    lambda sc, s, v="color": relief(sc, s, v, depth=14.0, side="tones"),
    "r3-croix":   lambda sc, s, v="color": relief(sc, s, v, cut="perp", depth=12.0, corner=2.0),
    "r4-profond": lambda sc, s, v="color": relief(sc, s, v, depth=18.0, key=False),
}
INTERF = {
    "i1-base":    lambda sc, s, v="color": interference(sc, s, v),
    "i2-fin":     lambda sc, s, v="color": interference(sc, s, v, pitch=2.2, lw=1.0, angle=8.0),
    "i3-gras":    lambda sc, s, v="color": interference(sc, s, v, pitch=4.2, lw=2.5, angle=5.0, t=32.0),
    "i4-lentille":lambda sc, s, v="color": interference(sc, s, v, pitch=2.8, lw=1.4, angle=7.0, lens="signal"),
    "i5-encre":   lambda sc, s, v="color": interference(sc, s, v, pitch=2.8, lw=1.4, angle=7.0, colors=("t", "text")),
}
HYBRID = {"h1-hybride": lambda sc, s, v="color": hybrid(sc, s, v), "h2-hybride-gras": lambda sc, s, v="color": hybrid(sc, s, v, pitch=3.6, lw=1.9, angle=6.0, depth=13.0)}

if __name__ == "__main__":
    import os
    os.makedirs("out9", exist_ok=True)
    for key, gen in {**RELIEF, **INTERF, **HYBRID}.items():
        for v in ["color", "inverse", "mono"]:
            open(f"out9/{key}-mark-{v}.svg", "w").write(mark(gen, v))
        svg, _ = lockup_central(gen, "color"); open(f"out9/{key}-central-color.svg", "w").write(svg)
        svg, _ = lockup_central(gen, "inverse"); open(f"out9/{key}-central-inverse.svg", "w").write(svg)
    print("done")
