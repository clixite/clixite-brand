"""Assets du site charte.clixite.be : X vivant interactif, diagrammes de construction,
interdits, aperçus Office, polices auto-hébergées, archives zip. Rejouable."""
import os, re, json, shutil, subprocess, zipfile, glob
from shapely.ops import unary_union
from shapely import affinity
from geom import geom_to_d
from logos import INK, PAPER, TURQ, TURQ_DEEP, ROSE, SIGNAL, MIST, SLATE, INK_TINT, svg_wrap, paths_for
from logos10 import x_geoms, x_relief, x_master, STEM, sweep_of, ext_vec, lockup_central, mark
from logos2 import scheme2
from typo import text_paths, metrics

SITE = "charte"; A = f"{SITE}/assets"; os.makedirs(A, exist_ok=True)
SC = "/tmp/claude-0/-home-claude/082fa878-b318-5a61-a8c6-40d163cb8592/scratchpad"

# ---------------------------------------------------------------- X vivant interactif
def living_x(size=400.0, lines=10, variant="inverse", t_ratio=0.185, depth_ratio=0.30, id_prefix="hx"):
    """SVG fragment in the silhouette frame: face at (0,0), extrusion to (edx, edy). Fields are rotated by JS."""
    t = t_ratio * size; d = depth_ratio * t
    edx, edy = ext_vec(d); edy = -edy            # screen: right, down
    a, b, c, joint = x_geoms(size, t)
    to = lambda g: geom_to_d(g, 1.0, 0, size)   # y-up box -> screen box
    sweep = sweep_of(unary_union([a, b]), edx, -edy)
    face = INK if variant == "inverse" else PAPER
    side = INK_TINT if variant == "inverse" else INK
    pitch = t / lines; lw = pitch / 2
    n = int(size * 1.8 / pitch)
    def lines_group(color, cls, offset=0.0):
        out = []
        for k in range(-n, n + 1):
            x = size / 2 + k * pitch + offset
            out.append(f'<rect x="{x - lw/2:.2f}" y="{-size:.1f}" width="{lw:.2f}" height="{3*size:.1f}" fill="{color}"/>')
        return f'<g class="{cls}" data-origin="{size/2:.1f} {size/2:.1f}">{"".join(out)}</g>'
    W = size + edx; H = size + edy
    frag = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" class="living-x" data-size="{size:.0f}" aria-hidden="true">
<defs><clipPath id="{id_prefix}-a"><path d="{to(a)}"/></clipPath><clipPath id="{id_prefix}-b"><path d="{to(b)}"/></clipPath></defs>
<g class="lx-chant"><path d="{to(sweep)}" fill="{side}"/></g>
<g class="lx-face"><path d="{to(a)}" fill="{face}"/><path d="{to(b)}" fill="{face}"/></g>
<path class="lx-lens" d="{to(c)}" fill="{SIGNAL}"/>
<g clip-path="url(#{id_prefix}-a)"><g class="lx-slide lx-slide-a">{lines_group(TURQ, "lx-field lx-field-a")}</g></g>
<g clip-path="url(#{id_prefix}-b)"><g class="lx-slide lx-slide-b">{lines_group(ROSE, "lx-field lx-field-b", pitch / 2)}</g></g>
</svg>'''
    return frag, (W, H, edx, edy)

hero, dims = living_x(400, 10, "inverse", id_prefix="hx")
open(f"{A}/living-x-hero.svg.frag", "w").write(hero)
play, _ = living_x(400, 10, "color", id_prefix="px")
open(f"{A}/living-x-play.svg.frag", "w").write(play)

# ---------------------------------------------------------------- construction diagram
def construction_svg():
    wm = 200.0; pad = 70
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm
    over = 0.05; xs = cap * (1 + 2 * over); stem = STEM * wm; t_ratio = 1.08 * stem / xs; t = t_ratio * xs
    d = 0.30 * t; edx, edy = ext_vec(d); shx, shy = edx / 2, -edy / 2
    gap = 0.035 * wm; tr = 0.06
    baseline = pad + xs - over * cap + 60
    left, lw = text_paths("space", 700, "CLI", wm, pad, baseline, tracking=tr)
    x_x = pad + lw + gap + shx; x_y = baseline - cap - over * cap + shy
    right, rw = text_paths("space", 700, "ITE", wm, x_x + xs + gap - shx, baseline, tracking=tr)
    W = x_x + xs + gap - shx + rw + pad; H = baseline + 150
    sc = scheme2("color")
    g = f'<rect width="100%" height="100%" fill="#FFFFFF"/>'
    # guides
    guide = lambda x1, y1, x2, y2, col=MIST, dash="4 4": f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="1" stroke-dasharray="{dash}"/>'
    lab = lambda x, y, s, anchor="start", col=SLATE: f'<text x="{x:.1f}" y="{y:.1f}" font-family="JetBrains Mono, monospace" font-size="11" fill="{col}" text-anchor="{anchor}">{s}</text>'
    g += guide(pad - 30, baseline, W - pad + 30, baseline, SLATE, "none")                      # baseline
    g += guide(pad - 30, baseline - cap, W - pad + 30, baseline - cap)                          # cap height
    g += guide(pad - 30, baseline - cap - over * cap, W - pad + 30, baseline - cap - over * cap, ROSE)   # overshoot top
    g += guide(pad - 30, baseline + over * cap, W - pad + 30, baseline + over * cap, ROSE)             # overshoot bottom
    g += lab(W - pad + 34, baseline - 4, "ligne de base") + lab(W - pad + 34, baseline - cap + 14, "capitale")
    g += lab(W - pad + 34, baseline - cap - over * cap - 4, "+ 5 %", col="#D81B60") + lab(W - pad + 34, baseline + over * cap + 14, "+ 5 %", col="#D81B60")
    # X box
    g += f'<rect x="{x_x:.1f}" y="{x_y:.1f}" width="{xs:.1f}" height="{xs:.1f}" fill="none" stroke="{TURQ_DEEP}" stroke-width="1" stroke-dasharray="3 3"/>'
    # letters and X
    g += paths_for(left, INK) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{x_relief(sc, xs, "color", t_ratio=t_ratio)}</g>' + paths_for(right, INK)
    # symmetric blanks: vertical guides dropped from the I's advance edge and from the silhouette edges
    i_end = pad + lw; t_start = x_x + xs + gap - shx; sil_l = x_x - edx; sil_r = x_x + xs
    yb = baseline + 40
    for xg in (i_end, sil_l, sil_r, t_start):
        g += guide(xg, baseline + 14, xg, yb + 16, TURQ_DEEP, "2 3")
    for (xa, xb) in ((i_end, sil_l), (sil_r, t_start)):
        g += f'<line x1="{xa:.1f}" y1="{yb:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{TURQ_DEEP}" stroke-width="1"/>'
        g += lab((xa + xb) / 2, yb + 30, "a", "middle", TURQ_DEEP)
    g += lab(x_x + xs / 2, yb + 56, "a = a : la silhouette complète du X, face et chant, est centrée entre les deux I", "middle")
    # stem
    I = left[2]["bbox"]; g += f'<path d="M{I[0]:.1f} {baseline - cap - 30} v-6 M{I[2]:.1f} {baseline - cap - 30} v-6 M{I[0]:.1f} {baseline - cap - 36} H{I[2]:.1f}" stroke="{SLATE}" fill="none" stroke-width="1"/>'
    g += lab((I[0] + I[2]) / 2, baseline - cap - 44, "fût f", "middle")
    # bar thickness and extrusion
    g += lab(x_x + xs / 2, x_y - 44, "barre = 1,08 f", "middle", TURQ_DEEP)
    g += lab(x_x + xs + 26, x_y + xs + 36, "chant = 0,30 barre, extrudé à 70°", "start", TURQ_DEEP)
    g += f'<path d="M{x_x + xs + 10:.1f} {x_y + xs + 6:.1f} l{edx*4:.1f} {-edy*4:.1f}" stroke="{TURQ_DEEP}" stroke-width="1" marker-end="url(#arr)"/>'
    g += f'<defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{TURQ_DEEP}"/></marker></defs>'
    g += lab(pad, H - 16, "Mot-marque Space Grotesk Bold, approche + 6 %. Descripteur Space Grotesk Medium, capitales espacées, calé sur la largeur du mot.", "start")
    return svg_wrap(g, W + 130, H)
open(f"{A}/construction.svg", "w").write(construction_svg())

# ---------------------------------------------------------------- clear space diagram
def clearspace_svg():
    svg, (W, H) = lockup_central(x_relief, "color")
    inner = re.sub(r'^<svg[^>]*>', '', svg).rsplit('</svg>', 1)[0]
    inner = re.sub(r'<rect width="100%" height="100%" fill="[^"]+"/>', '', inner)
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * 150; xs = cap * 1.1
    # content bounds approx: pad 44 each side; descriptor bottom = H - 44*0.9
    pad = 44; X = xs
    # content bounds inside the lockup: [pad, W-pad] x [pad, H-0.9pad]; lockup is placed at (X, X)
    cx0, cy0, cx1, cy1 = X + pad, X + pad, X + W - pad, X + H - 0.9 * pad
    out = f'<rect width="100%" height="100%" fill="#FFFFFF"/>'
    out += f'<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="{MIST}" stroke-width="1"/></pattern></defs>'
    out += f'<rect x="{cx0 - X:.1f}" y="{cy0 - X:.1f}" width="{(cx1 - cx0) + 2*X:.1f}" height="{(cy1 - cy0) + 2*X:.1f}" fill="url(#hatch)" stroke="{SLATE}" stroke-width="1" stroke-dasharray="4 4"/>'
    out += f'<rect x="{cx0:.1f}" y="{cy0:.1f}" width="{cx1 - cx0:.1f}" height="{cy1 - cy0:.1f}" fill="#FFFFFF"/>'
    out += f'<g transform="translate({X:.1f},{X:.1f})">{inner}</g>'
    # X marker squares in two corners of the protection zone
    for (qx, qy) in ((cx0 - X, cy0 - X), (cx1, cy1)):
        out += f'<rect x="{qx:.1f}" y="{qy:.1f}" width="{X:.1f}" height="{X:.1f}" fill="#FFFFFF" stroke="{TURQ_DEEP}" stroke-width="1"/>'
        out += f'<text x="{qx + X/2:.1f}" y="{qy + X/2 + 5:.1f}" font-family="JetBrains Mono, monospace" font-size="14" fill="{TURQ_DEEP}" text-anchor="middle">X</text>'
    return svg_wrap(out, W + 2 * X, H + 2 * X)
open(f"{A}/zone-de-protection.svg", "w").write(clearspace_svg())

# ---------------------------------------------------------------- don'ts
sc_swapped = dict(bg=PAPER, text=INK, t=ROSE, r=TURQ, y=SIGNAL, overlap=INK, sub=SLATE)
def lockup_with_scheme(sc):
    """lockup central, colour, but with a custom scheme: re-render via x_relief + text paths (simplified copy)."""
    wm = 150.0; pad = 44
    m = metrics("space", 700); cap = m["cap"] / m["upem"] * wm; xs = cap * 1.1; stem = STEM * wm; t_ratio = 1.08 * stem / xs
    baseline = pad + xs - 0.05 * cap
    left, lw = text_paths("space", 700, "CLI", wm, pad, baseline, tracking=0.06)
    edx, edy = ext_vec(0.30 * t_ratio * xs); shx, shy = edx / 2, -edy / 2
    x_x = pad + lw + 0.035 * wm + shx; x_y = baseline - cap - 0.05 * cap + shy
    right, rw = text_paths("space", 700, "ITE", wm, x_x + xs + 0.035 * wm - shx, baseline, tracking=0.06)
    width = (x_x + xs + 0.035 * wm + rw) - pad
    content = paths_for(left, sc["text"]) + f'<g transform="translate({x_x:.2f},{x_y:.2f})">{x_relief(sc, xs, "color", t_ratio=t_ratio)}</g>' + paths_for(right, sc["text"])
    W = pad * 2 + width; H = baseline + pad * 0.9
    return svg_wrap(content, W, H)
open(f"{A}/interdit-couleurs.svg", "w").write(lockup_with_scheme(sc_swapped))
base = open(f"{SITE}/downloads/logo/clixite-relief-color-transparent.svg").read()
outlined = base.replace('<path d=', '<path stroke="#0B2239" stroke-width="3" d=')
open(f"{A}/interdit-contour.svg", "w").write(outlined)

# ---------------------------------------------------------------- office previews
P = f"{SITE}/apercus"; os.makedirs(P, exist_ok=True)
tmp = f"{SC}/apercus"; os.makedirs(tmp, exist_ok=True)
for f in ("Clixite-gabarit-presentation.pptx", "Clixite-papier-a-lettre.docx", "Clixite-modele-offre.docx", "Clixite-tableau-de-suivi.xlsx"):
    pdf = f"{tmp}/{os.path.splitext(f)[0]}.pdf"
    if not os.path.exists(pdf):
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, f"{SITE}/downloads/office/{f}"], check=True, capture_output=True, timeout=180)
    stem_ = os.path.splitext(f)[0]
    subprocess.run(["pdftoppm", "-png", "-r", "60", "-f", "1", "-l", "4", pdf, f"{tmp}/{stem_}"], check=True)
from PIL import Image
# montage of deck slides 1..4
def montage(files, cols, out, gap=12, bg=(246, 245, 240)):
    ims = [Image.open(f).convert("RGB") for f in files]
    w, h = ims[0].size; rows = (len(ims) + cols - 1) // cols
    M = Image.new("RGB", (cols * w + (cols + 1) * gap, rows * h + (rows + 1) * gap), bg)
    for i, im in enumerate(ims):
        M.paste(im.resize((w, h)), (gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap)))
    M.save(out, optimize=True)
deck = sorted(glob.glob(f"{tmp}/Clixite-gabarit-presentation-*.png"))[:4]
montage(deck, 2, f"{P}/apercu-presentation.png")
for stem_, outn in (("Clixite-papier-a-lettre", "apercu-papier-a-lettre"), ("Clixite-modele-offre", "apercu-offre"), ("Clixite-tableau-de-suivi", "apercu-tableau")):
    pages = sorted(glob.glob(f"{tmp}/{stem_}-*.png"))
    montage(pages[:2] if "offre" in stem_ else pages[:1], 2 if "offre" in stem_ else 1, f"{P}/{outn}.png")

# ---------------------------------------------------------------- fonts (self-hosted + pack)
F = f"{SITE}/fonts"; os.makedirs(F, exist_ok=True)
NM = "node_modules/@fontsource"
wanted = {"space-grotesk": ["500-normal", "600-normal", "700-normal"], "inter": ["400-normal", "500-normal", "600-normal", "400-italic"],
          "jetbrains-mono": ["500-normal"], "fraunces": ["500-italic", "600-italic"]}
css = []
fam_name = {"space-grotesk": "Space Grotesk", "inter": "Inter", "jetbrains-mono": "JetBrains Mono", "fraunces": "Fraunces"}
for fam, variants in wanted.items():
    for v in variants:
        src = f"{NM}/{fam}/files/{fam}-latin-{v}.woff2"; dst = f"{F}/{fam}-{v}.woff2"; shutil.copy(src, dst)
        w, style = v.split("-")
        css.append(f"@font-face{{font-family:'{fam_name[fam]}';font-style:{style};font-weight:{w};font-display:swap;src:url('../fonts/{fam}-{v}.woff2') format('woff2')}}")
    shutil.copy(f"{NM}/{fam}/LICENSE", f"{F}/LICENSE-{fam}.txt")
open(f"{A}/fonts.css", "w").write("\n".join(css) + "\n")
# TTF pack for Office (decompressed from woff2 by typo.load)
DF = f"{SITE}/downloads/fonts"; os.makedirs(DF, exist_ok=True)
ttf_map = {"space-500.ttf": "SpaceGrotesk-Medium.ttf", "space-600.ttf": "SpaceGrotesk-SemiBold.ttf", "space-700.ttf": "SpaceGrotesk-Bold.ttf",
           "inter-400.ttf": "Inter-Regular.ttf", "inter-600.ttf": "Inter-SemiBold.ttf", "inter-700.ttf": "Inter-Bold.ttf",
           "fraunces-it-500.ttf": "Fraunces-MediumItalic.ttf", "fraunces-it-600.ttf": "Fraunces-SemiBoldItalic.ttf"}
with zipfile.ZipFile(f"{DF}/clixite-polices.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for src, name in ttf_map.items():
        if os.path.exists(f"fonts/{src}"): z.write(f"fonts/{src}", name)
    for fam in wanted: z.write(f"{NM}/{fam}/LICENSE", f"LICENCES/OFL-{fam}.txt")
    z.writestr("LISEZ-MOI.txt", "Polices Clixite (licence OFL, libres).\nInstaller tous les fichiers .ttf (clic droit > Installer pour tous les utilisateurs sous Windows).\nSpace Grotesk : titres et mot-marque. Inter : texte courant. Fraunces Italic : voix éditoriale.\nJetBrains Mono (donnees et etiquettes) se telecharge sur https://www.jetbrains.com/lp/mono/ ou via Google Fonts.\n")

# ---------------------------------------------------------------- tokens for developers
tok_src = f"{SC}/clixite-ds/project/tokens.json"
if os.path.exists(tok_src): shutil.copy(tok_src, f"{SITE}/downloads/clixite-tokens.json")
css_vars = """:root{
  --clx-encre:#0B2239; --clx-papier:#F6F5F0; --clx-blanc:#FFFFFF;
  --clx-turquoise:#19B3D9; --clx-turquoise-texte:#0C7893; --clx-turquoise-doux:#D6F1F8;
  --clx-rose:#FF4F8B; --clx-rose-texte:#D81B60;
  --clx-signal:#FFD233; --clx-indigo:#193776;
  --clx-ardoise:#4B5A6B; --clx-brume:#CDD5DD; --clx-encre-teintee:#1F3A5A; --clx-surface-sombre:#122D4A;
  --clx-font-display:'Space Grotesk',system-ui,sans-serif; --clx-font-sans:'Inter',system-ui,sans-serif;
  --clx-font-editorial:'Fraunces',Georgia,serif; --clx-font-mono:'JetBrains Mono',ui-monospace,monospace;
  --clx-radius-sm:6px; --clx-radius-md:10px; --clx-radius-pill:999px;
}
"""
open(f"{SITE}/downloads/clixite-variables.css", "w").write(css_vars)

# ---------------------------------------------------------------- zips
D = f"{SITE}/downloads"
def zipdir(folder, out, prefix):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(folder):
            for fn in sorted(files):
                if fn.endswith(".zip"): continue
                p = os.path.join(root, fn); z.write(p, os.path.join(prefix, os.path.relpath(p, folder)))
zipdir(f"{D}/logo", f"{D}/clixite-logos.zip", "clixite-logos")
zipdir(f"{D}/favicons", f"{D}/clixite-favicons.zip", "clixite-favicons")
zipdir(f"{D}/reseaux", f"{D}/clixite-reseaux.zip", "clixite-reseaux")
zipdir(f"{D}/office", f"{D}/clixite-office.zip", "clixite-office")
zipdir(f"{D}/signature", f"{D}/clixite-signature.zip", "clixite-signature")
with zipfile.ZipFile(f"{D}/clixite-animation.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for fn in os.listdir(f"{SITE}/animation"): z.write(f"{SITE}/animation/{fn}", f"clixite-animation/{fn}")
with zipfile.ZipFile(f"{D}/clixite-kit-complet.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(D):
        for fn in sorted(files):
            if fn.endswith(".zip"): continue
            p = os.path.join(root, fn); z.write(p, os.path.join("clixite-kit", os.path.relpath(p, D)))
    for fn in os.listdir(f"{SITE}/animation"): z.write(f"{SITE}/animation/{fn}", f"clixite-kit/animation/{fn}")
sizes = {}
for p in glob.glob(f"{D}/**/*", recursive=True):
    if os.path.isfile(p): sizes[os.path.relpath(p, SITE)] = os.path.getsize(p)
json.dump(sizes, open(f"{SC}/download-sizes.json", "w"), indent=1)
print("assets ok", dims, len(sizes), "download files")
