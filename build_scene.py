"""Exporte la géométrie 3D du mot-marque (lettres, X en relief, descripteur) pour le moteur WebGL
charte/assets/ouverture3d.js. Même métriques que lockup_central (logos10) : coordonnées écran (y vers le bas),
unités = 1/1000 de la taille du mot-marque (wm_size = 1000)."""
import json, math
import numpy as np
import mapbox_earcut as earcut
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
from shapely import affinity
from geom import glyph_polygon
from logos10 import x_geoms, STEM, ext_vec, EXTRUDE_DEG
from typo import load, shape, metrics

WM = 1000.0
tt, font, upem = load("space", 700)
m = metrics("space", 700); cap = m["cap"] / upem * WM
over = 0.05; xs = cap * (1 + 2 * over); stem = STEM * WM; t_ratio = 1.08 * stem / xs; t = t_ratio * xs
d = 0.30 * t; edx, edy = ext_vec(d); edy = -edy          # screen: right, down
shx, shy = edx / 2, edy / 2                               # silhouette centring (box nudged right and down)
gap = 0.035 * WM; tr = 0.06
baseline = xs - over * cap                                 # origin: top-left of the lockup content box
sc = WM / upem

def text_polys(text, fam, w, size, x0, base, tracking):
    """list of (shapely polygon, screen coords) for each glyph."""
    ttf, _, up = load(fam, w)
    glyphs, width, _ = shape(fam, w, text, tracking)
    s = size / up; out = []
    for gname, gx, gy, adv in glyphs:
        g = glyph_polygon(ttf, gname)
        if g.is_empty: continue
        g = affinity.affine_transform(g, [s, 0, 0, -s, x0 + gx * s, base - gy * s])  # flip y, translate
        out.append(g)
    return out, width * s

left, lw = text_polys("CLI", "space", 700, WM, 0.0, baseline, tr)
x_x = lw + gap + shx; x_y = baseline - cap - over * cap + shy
right, rw = text_polys("ITE", "space", 700, WM, x_x + xs + gap - shx, baseline, tr)
width = x_x + xs + gap - shx + rw
# descriptor fitted to the wordmark width (same rule as lockup_central: 24/150 of wm, then scaled)
d_size = 24.0 / 150 * WM
_, d_w = text_polys("ENTERPRISE & SOLUTION ARCHITECTURE", "space", 500, d_size, 0, 0, 0.2)
d_size *= width / d_w
desc, d_w = text_polys("ENTERPRISE & SOLUTION ARCHITECTURE", "space", 500, d_size, 0.0, baseline + 40 / 150 * WM + d_size, 0.2)
H = baseline + 40 / 150 * WM + d_size

# X face polygon in screen coords: box at (x_x, x_y), face lifted by (-edx, -edy)
a, b, c, joint = x_geoms(xs, t)
def box_to_screen(g):  # y-up box -> screen
    return affinity.affine_transform(g, [1, 0, 0, -1, x_x - edx, x_y - edy + xs])
face = box_to_screen(unary_union([a, b]))
lens = box_to_screen(c)

def tri(geom):
    """earcut a (multi)polygon -> positions [[x,y],...], indices"""
    polys = list(geom.geoms) if isinstance(geom, MultiPolygon) else [geom]
    P, I, base_i = [], [], 0
    for poly in polys:
        poly = poly.simplify(0.15)
        rings = [list(poly.exterior.coords)[:-1]] + [list(r.coords)[:-1] for r in poly.interiors]
        verts = np.array([p for r in rings for p in r], dtype=np.float64)
        ring_ends = np.cumsum([len(r) for r in rings]).astype(np.uint32)
        idx = earcut.triangulate_float64(verts, ring_ends)
        P += verts.round(2).tolist(); I += (idx + base_i).tolist(); base_i += len(verts)
    return P, I

def group(polys):
    P, I = [], []
    for g in polys:
        p, i = tri(g); off = len(P); P += p; I += [k + off for k in i]
    return {"pos": [v for xy in P for v in xy], "idx": I}

# sides of the X: one quad per exterior edge, with its outward normal (2D), extruded along z by -d
ring = list(face.exterior.coords)[:-1]
# ensure clockwise in screen coords (y down) so outward normals are consistent
area = sum(ring[i][0] * ring[(i + 1) % len(ring)][1] - ring[(i + 1) % len(ring)][0] * ring[i][1] for i in range(len(ring)))
if area > 0: ring = ring[::-1]
sides = {"pos": [], "nrm": [], "idx": []}
for i in range(len(ring)):
    (x1, y1), (x2, y2) = ring[i], ring[(i + 1) % len(ring)]
    ex, ey = x2 - x1, y2 - y1; L = math.hypot(ex, ey)
    if L < 1e-6: continue
    nx, ny = ey / L, -ex / L   # outward normal for clockwise ring in y-down coords
    base_i = len(sides["pos"]) // 3
    for (x, y, z) in ((x1, y1, 0), (x2, y2, 0), (x2, y2, -d), (x1, y1, -d)):
        sides["pos"] += [round(x, 2), round(y, 2), round(z, 2)]; sides["nrm"] += [round(nx, 4), round(ny, 4), 0.0]
    sides["idx"] += [base_i, base_i + 1, base_i + 2, base_i, base_i + 2, base_i + 3]

scene = {
    "units": WM, "width": round(width, 2), "height": round(H, 2),
    "x": {"box": [round(x_x - edx, 2), round(x_y - edy, 2), round(xs, 2)], "t": round(t, 2), "depth": round(d, 2),
          "ext": [round(edx, 2), round(edy, 2)], "ext_deg": EXTRUDE_DEG, "pitch": round(t / 10, 2),
          "centre": [round(x_x - edx + xs / 2, 2), round(x_y - edy + xs / 2, 2)]},
    "left": group(left), "right": group(right), "desc": group(desc),
    "face": group([face]), "lens": group([lens]), "sides": sides,
    "cap": round(cap, 2), "baseline": round(baseline, 2),
}
json.dump(scene, open("charte/assets/scene.json", "w"), separators=(",", ":"))
n = sum(len(scene[k]["idx"]) for k in ("left", "right", "desc", "face", "lens", "sides"))
print(f"scene ok: {n//3} triangles, width {width:.0f}, height {H:.0f}, X box {xs:.0f}, t {t:.1f}, depth {d:.1f}, ext ({edx:.1f},{edy:.1f})")
