"""X de construction pour le site : le hero (X Interférence en couches animables) et les quatre états de la méthode.

Même géométrie que le logo (logos10.py) : barre 0,20 de la boîte, chant 0,30 barre à 70°, joint 0,085,
10 traits par barre, champs à 8° au repos, décalage d'un demi-pas entre les champs.
Différence avec le fichier logo : les champs ne sont pas découpés en dur. Ils sont dessinés à 0° et
découpés par des clipPath, pour que le CSS puisse faire varier l'angle entre eux (seul mouvement autorisé
par la charte) sans redessiner le X.

Lancer depuis la racine du dépôt : python3 web/scripts/gen_x.py
"""
import math, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT); os.chdir(ROOT)
from shapely.geometry import box, LineString, Polygon
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, TURQ, ROSE, SIGNAL, PAPER, SLATE, MIST, paths_for
from logos7 import bar45
from logos9 import sweep_of
from logos10 import x_geoms, ext_vec, STEM, x_master
from logos2 import scheme2
from typo import text_paths, metrics

OUT = os.path.join(ROOT, "web", "src", "assets", "x"); os.makedirs(OUT, exist_ok=True)
PUB = os.path.join(ROOT, "web", "public", "brand"); os.makedirs(PUB, exist_ok=True)

S = 480.0                 # boîte du X
T = 0.20 * S              # épaisseur de barre (t_ratio 0,20 comme la marque seule)
D = 0.30 * T              # profondeur du chant
P = 72.0                  # marge pour les repères de construction
LINES = 10; PITCH = T / LINES; LW = PITCH / 2
dx, dy = ext_vec(D)       # repère y vers le haut : dx > 0, dy < 0 (vers le bas à droite)

a, b, c, joint = x_geoms(S, T)
fa, fb, fc, fj = (affinity.translate(g, -dx, -dy) for g in (a, b, c, joint))
front = unary_union([fa, fb]); sweep = sweep_of(front, dx, dy)
minx, miny, maxx, maxy = unary_union([front, sweep]).bounds
VW = (maxx - minx) + 2 * P; VH = (maxy - miny) + 2 * P
OX = P - minx; OY = P - miny       # translation de la géométrie dans la viewBox (repère y vers le haut)

def d(g):
    """chemin SVG dans la viewBox (y vers le bas)"""
    return geom_to_d(affinity.translate(g, OX, OY), 1.0, 0, VH)

CX = OX + S / 2 - dx / 2; CY_UP = OY + S / 2 - dy / 2  # centre de la face avant, repère y vers le haut
cx, cy = OX + (fc.centroid.x), VH - (OY + fc.centroid.y)   # centre de la lentille, repère écran

def field(offset=0.0, lw=LW):
    """traits verticaux couvrant largement la boîte (assez pour tourner de ±8°)"""
    n = int(S * 1.0 / PITCH) + 6
    x0 = fc.centroid.x + offset
    lines = [box(x0 + k * PITCH - lw / 2, -0.35 * S, x0 + k * PITCH + lw / 2, 1.35 * S) for k in range(-n, n + 1)]
    return unary_union(lines)

def f(x):
    return f"{x:.2f}"

def hero():
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(VW)} {f(VH)}" class="hx" role="img" aria-labelledby="hx-title">')
    out.append('<title id="hx-title">Le X de Clixite en construction : repères, tracé, chant, champs de lignes et lentille</title>')
    # clips : barre A entière, barre B hors lentille, lentille
    out.append("<defs>")
    out.append(f'<clipPath id="hx-ca"><path d="{d(fa)}"/></clipPath>')
    out.append(f'<clipPath id="hx-cb"><path d="{d(fb.difference(fc))}"/></clipPath>')
    out.append(f'<clipPath id="hx-cc"><path d="{d(fc)}"/></clipPath>')
    out.append("</defs>")
    # 1. repères : boîte, axes, diagonales des barres, cote du chant
    bx0, by0 = OX - dx, VH - (OY - dy + S)      # boîte de la face avant, coin haut gauche (écran)
    g = []
    g.append(f'<rect x="{f(bx0)}" y="{f(by0)}" width="{f(S)}" height="{f(S)}"/>')
    g.append(f'<line x1="{f(bx0 + S/2)}" y1="{f(by0 - 36)}" x2="{f(bx0 + S/2)}" y2="{f(by0 + S + 36)}"/>')
    g.append(f'<line x1="{f(bx0 - 36)}" y1="{f(by0 + S/2)}" x2="{f(bx0 + S + 36)}" y2="{f(by0 + S/2)}"/>')
    th = T * math.sqrt(2) / 2
    g.append(f'<line x1="{f(bx0 + th)}" y1="{f(by0 + S)}" x2="{f(bx0 + S - th)}" y2="{f(by0)}"/>')
    g.append(f'<line x1="{f(bx0 + th)}" y1="{f(by0)}" x2="{f(bx0 + S - th)}" y2="{f(by0 + S)}"/>')
    # cote de l'épaisseur de barre sous la boîte
    yb = by0 + S + 28
    g.append(f'<line x1="{f(bx0)}" y1="{f(yb)}" x2="{f(bx0 + T*math.sqrt(2))}" y2="{f(yb)}"/>')
    g.append(f'<line x1="{f(bx0)}" y1="{f(yb-6)}" x2="{f(bx0)}" y2="{f(yb+6)}"/><line x1="{f(bx0 + T*math.sqrt(2))}" y1="{f(yb-6)}" x2="{f(bx0 + T*math.sqrt(2))}" y2="{f(yb+6)}"/>')
    # direction du chant : 70°
    ex, ey = bx0 + S, by0 + S
    g.append(f'<line x1="{f(ex)}" y1="{f(ey)}" x2="{f(ex + 54*math.cos(math.radians(70)))}" y2="{f(ey + 54*math.sin(math.radians(70)))}"/>')
    g.append(f'<line x1="{f(ex)}" y1="{f(ey)}" x2="{f(ex + 54)}" y2="{f(ey)}"/>')
    out.append(f'<g class="hx-guides" fill="none" stroke="currentColor" stroke-width="1" vector-effect="non-scaling-stroke">{"".join(g)}</g>')
    # 2. légendes de mesure (données : JetBrains Mono, rendues en chemins pour ne dépendre d'aucune police)
    lab = []
    items, w = text_paths("mono", 500, "0,20", 13, bx0, yb + 20); lab.append(paths_for(items, "currentColor"))
    items, w = text_paths("mono", 500, "70°", 13, ex + 22, ey + 34); lab.append(paths_for(items, "currentColor"))
    items, w = text_paths("mono", 500, "+5 %", 13, bx0 + S/2 + 8, by0 - 22); lab.append(paths_for(items, "currentColor"))
    out.append(f'<g class="hx-labels">{"".join(lab)}</g>')
    # 3. chant, 4. face, 5. lentille
    out.append(f'<path class="hx-chant" d="{d(sweep.difference(front))}" fill="{INK}"/>')
    out.append(f'<path class="hx-face" d="{d(front)}" fill="{PAPER}"/>')
    out.append(f'<path class="hx-lens" d="{d(fc)}" fill="{SIGNAL}"/>')
    # 6. champs : rotation pilotée par CSS autour du centre de la lentille
    fA = field(0.0); fB = field(PITCH / 2); fBt = field(PITCH / 2, LW * 0.7)
    out.append(f'<g clip-path="url(#hx-ca)"><g class="hx-field hx-field-a"><path d="{d(fA)}" fill="{TURQ}"/></g></g>')
    out.append(f'<g clip-path="url(#hx-cb)"><g class="hx-field hx-field-b"><path d="{d(fB)}" fill="{ROSE}"/></g></g>')
    out.append(f'<g clip-path="url(#hx-cc)"><g class="hx-field hx-field-b"><path d="{d(fBt)}" fill="{ROSE}"/></g></g>')
    # 7. tracé du contour (dessiné au départ, puis s'efface sous les champs)
    out.append(f'<path class="hx-outline" d="{d(front)}" fill="none" stroke="{INK}" stroke-width="1.5" pathLength="1" vector-effect="non-scaling-stroke"/>')
    out.append("</svg>")
    return "".join(out), (cx, cy)

def etape(n):
    """quatre états monochromes pour la méthode (un seul moment de couleur par page : le hero)"""
    pad = 36; s = 200.0; t = 0.2 * s; dd = 0.30 * t
    ddx, ddy = ext_vec(dd)
    A, B, C, J = x_geoms(s, t)
    FA, FB, FC = (affinity.translate(g, -ddx, -ddy) for g in (A, B, C))
    FR = unary_union([FA, FB]); SW = sweep_of(FR, ddx, ddy)
    mnx, mny, mxx, mxy = unary_union([FR, SW]).bounds
    vw, vh = (mxx - mnx) + 2 * pad, (mxy - mny) + 2 * pad
    ox, oy = pad - mnx, pad - mny
    dd_ = lambda g: geom_to_d(affinity.translate(g, ox, oy), 1.0, 0, vh)
    bx, by = ox - ddx, vh - (oy - ddy + s)
    body = []
    guides = (f'<g fill="none" stroke="currentColor" stroke-width="1" vector-effect="non-scaling-stroke" opacity="{1 if n == 1 else .35}">'
              f'<rect x="{f(bx)}" y="{f(by)}" width="{f(s)}" height="{f(s)}"/>'
              f'<line x1="{f(bx + s/2)}" y1="{f(by - 16)}" x2="{f(bx + s/2)}" y2="{f(by + s + 16)}"/>'
              f'<line x1="{f(bx - 16)}" y1="{f(by + s/2)}" x2="{f(bx + s + 16)}" y2="{f(by + s/2)}"/>'
              f'<line x1="{f(bx)}" y1="{f(by + s)}" x2="{f(bx + s)}" y2="{f(by)}"/><line x1="{f(bx)}" y1="{f(by)}" x2="{f(bx + s)}" y2="{f(by + s)}"/></g>')
    body.append(guides)
    if n == 2:
        body.append(f'<path d="{dd_(FR)}" fill="none" stroke="currentColor" stroke-width="1.5" vector-effect="non-scaling-stroke"/>')
    if n == 3:
        body.append(f'<path d="{dd_(unary_union([FA, FB]).difference(affinity.translate(J, -ddx, -ddy)))}" fill="currentColor"/><path d="{dd_(FC)}" fill="currentColor"/>')
    if n == 4:
        body.append(f'<path d="{dd_(SW.difference(FR))}" fill="currentColor"/>')
        body.append(f'<path d="{dd_(unary_union([FA, FB]).difference(affinity.translate(J, -ddx, -ddy)))}" fill="currentColor" opacity=".18"/>')
        body.append(f'<path d="{dd_(FR)}" fill="none" stroke="currentColor" stroke-width="1.5" vector-effect="non-scaling-stroke"/>')
        body.append(f'<path d="{dd_(FC)}" fill="currentColor"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(vw)} {f(vh)}" aria-hidden="true" focusable="false">{"".join(body)}</svg>'

def wordmark(variant="color"):
    """mot-marque officiel sans descripteur (logos10.lockup_wordmark), fond transparent, sans dimensions fixes"""
    from logos10 import lockup_wordmark
    import re
    svg, _ = lockup_wordmark(x_master, variant)
    svg = re.sub(r'<rect width="100%" height="100%" fill="[^"]+"/>', "", svg)
    svg = re.sub(r'\s(width|height)="[^"]*"', "", svg, count=2)
    return re.sub(r"(\d+\.\d{2})\d+", r"\1", svg)   # 2 décimales suffisent à l'écran

if __name__ == "__main__":
    svg, centre = hero()
    open(os.path.join(OUT, "hero.svg"), "w").write(svg)
    open(os.path.join(OUT, "hero.json"), "w").write('{"cx": %.2f, "cy": %.2f, "vw": %.2f, "vh": %.2f}\n' % (centre[0], centre[1], VW, VH))
    for n in (1, 2, 3, 4):
        open(os.path.join(OUT, f"etape-{n}.svg"), "w").write(etape(n))
    open(os.path.join(OUT, "wordmark.svg"), "w").write(wordmark("color"))
    print(f"x ok hero {VW:.0f}x{VH:.0f} {len(svg)//1024} Ko, lentille ({centre[0]:.1f}, {centre[1]:.1f})")
