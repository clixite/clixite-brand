"""Pack logo complet : SVG, PNG, favicons, réseaux. Rejouable à chaque changement du générateur."""
import os, re, subprocess, json
from PIL import Image
from logos10 import x_master, x_relief, x_vivant, x_solid, lockup_central, lockup_side, lockup_stacked, mark, tile
from logos2 import scheme2
from logos import INK, PAPER, TURQ, ROSE, SIGNAL, svg_wrap, paths_for
from typo import text_paths

OUT = "charte/downloads/logo"; FAV = "charte/downloads/favicons"; S = "charte/downloads/reseaux"
for d in (OUT, FAV, S): os.makedirs(d, exist_ok=True)
def save(name, svg): p = f"{OUT}/{name}.svg"; open(p, "w").write(svg); return p
def png(svgpath, pngpath, width): subprocess.run(["node", "render.js", svgpath, pngpath, str(width)], check=True, capture_output=True)
def strip_bg(svg): return re.sub(r'<rect width="100%" height="100%" fill="[^"]+"/>', '', svg)
def inner(p):
    s = open(p).read(); m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    return float(m.group(1)), float(m.group(2)), re.sub(r'^<svg[^>]*>', '', s).rsplit('</svg>', 1)[0]

files = {}
for skin, gen in (("relief", x_relief), ("vivant", x_vivant), ("maitre", x_master)):
    for v in ("color", "inverse", "mono"):
        svg, _ = lockup_central(gen, v); files[f"clixite-{skin}-{v}"] = save(f"clixite-{skin}-{v}", svg)
    svg, _ = lockup_side(gen, "color"); files[f"clixite-{skin}-symbole-gauche-color"] = save(f"clixite-{skin}-symbole-gauche-color", svg)
    for v in ("color", "inverse"):
        svg, _ = lockup_stacked(gen, v); files[f"clixite-{skin}-empile-{v}"] = save(f"clixite-{skin}-empile-{v}", svg)
    for v in ("color", "inverse", "mono"):
        files[f"x-{skin}-{v}"] = save(f"x-{skin}-{v}", mark(gen, v))
files["x-favicon-encre"] = save("x-favicon-encre", mark(x_solid, "mono"))
files["x-favicon-inverse"] = save("x-favicon-inverse", mark(x_solid, "inverse"))
files["x-app-tile"] = save("x-app-tile", tile(x_relief))
for k in list(files):
    if "tile" in k: continue
    s2 = strip_bg(open(files[k]).read()); p = f"{OUT}/{k}-transparent.svg"; open(p, "w").write(s2); files[k + "-transparent"] = p
for k, p in list(files.items()):
    if k.startswith("clixite-") and not k.endswith("transparent"):
        for w in (800, 1600, 3200): png(p, f"{OUT}/{k}-{w}px.png", w)
    if k.startswith("clixite-") and k.endswith("transparent"):
        for w in (800, 1600): png(p, f"{OUT}/{k}-{w}px.png", w)
    if k.startswith("x-") and k.endswith("transparent"):
        for w in (256, 1024): png(p, f"{OUT}/{k}-{w}px.png", w)
png(files["x-app-tile"], f"{OUT}/x-app-tile-1024px.png", 1024)
# favicons
for w in (16, 32, 48, 64, 180, 192, 512):
    png(files["x-favicon-encre"], f"{FAV}/favicon-{w}.png", w); png(files["x-app-tile"], f"{FAV}/app-icon-{w}.png", w)
ico = [Image.open(f"{FAV}/favicon-{w}.png").convert("RGBA") for w in (16, 32, 48, 64)]
ico[0].save(f"{FAV}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)], append_images=ico[1:])
open(f"{FAV}/favicon.svg", "w").write(open(files["x-favicon-encre-transparent"]).read())
json.dump({"name": "Clixite", "short_name": "Clixite", "icons": [{"src": "app-icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "app-icon-512.png", "sizes": "512x512", "type": "image/png"}], "theme_color": "#0B2239", "background_color": "#F6F5F0", "display": "standalone"}, open(f"{FAV}/site.webmanifest", "w"), indent=2)

# social
sc = scheme2("inverse"); scp = scheme2("color")
av = f'<rect width="400" height="400" fill="{INK}"/><g transform="translate(70,70)">{x_relief(sc, 260, "inverse", t_ratio=0.2)}</g>'
open(f"{S}/linkedin-avatar.svg", "w").write(svg_wrap(av, 400, 400)); png(f"{S}/linkedin-avatar.svg", f"{S}/linkedin-avatar-400.png", 400); png(f"{S}/linkedin-avatar.svg", f"{S}/linkedin-avatar-800.png", 800)
w, h, b = inner(f"{OUT}/clixite-vivant-inverse-transparent.svg"); k = 560 / w
ban = f'<rect width="1584" height="396" fill="{INK}"/><g transform="translate(100,{(396-h*k)/2:.1f}) scale({k:.4f})">{b}</g>'
ban += f'<g transform="translate(1180,-60)">{x_vivant(sc, 520, "inverse", t_ratio=0.2, lines=14, angle=8)}</g><rect x="100" y="330" width="56" height="6" fill="{SIGNAL}"/>'
d_items, dw = text_paths("space", 500, "ENTERPRISE & SOLUTION ARCHITECTURE  ·  PROCUREMENT  ·  COMPLIANCE  ·  GROWTH", 18, 100, 356, tracking=0.18); ban += paths_for(d_items, "#CDD5DD")
open(f"{S}/linkedin-banniere.svg", "w").write(svg_wrap(ban, 1584, 396)); png(f"{S}/linkedin-banniere.svg", f"{S}/linkedin-banniere-1584x396.png", 1584)
w, h, b = inner(f"{OUT}/clixite-relief-empile-inverse-transparent.svg"); k = min(700 / w, 420 / h)
og = f'<rect width="1200" height="630" fill="{INK}"/><g transform="translate({(1200-w*k)/2:.1f},{(630-h*k)/2:.1f}) scale({k:.4f})">{b}</g>'
open(f"{S}/og-image.svg", "w").write(svg_wrap(og, 1200, 630)); png(f"{S}/og-image.svg", f"{S}/og-image-1200x630.png", 1200)
for name, bg, scm, v, lock in (("encre", INK, sc, "inverse", "clixite-relief-inverse-transparent"), ("papier", PAPER, scp, "color", "clixite-relief-color-transparent")):
    g = f'<rect width="1920" height="1080" fill="{bg}"/><g transform="translate(1160,40)" opacity="0.15">{x_vivant(scm, 1000, v, t_ratio=0.2, lines=16, angle=8, lens=False)}</g>'
    w, h, b = inner(f"{OUT}/{lock}.svg"); k = 380 / w
    g += f'<g transform="translate(80,{1080-h*k-60:.1f}) scale({k:.4f})">{b}</g>'
    open(f"{S}/fond-visio-{name}.svg", "w").write(svg_wrap(g, 1920, 1080)); png(f"{S}/fond-visio-{name}.svg", f"{S}/fond-visio-{name}-1920x1080.png", 1920)
post = f'<rect width="1200" height="1200" fill="{PAPER}"/><rect x="0" y="0" width="1200" height="14" fill="{TURQ}"/><g transform="translate(760,-40)">{x_relief(scp, 520, "color", t_ratio=0.2)}</g>'
t, _ = text_paths("space", 600, "Votre titre ici,", 72, 90, 420, tracking=-0.01); post += paths_for(t, INK)
t, _ = text_paths("space", 600, "en deux lignes.", 72, 90, 500, tracking=-0.01); post += paths_for(t, INK)
t, _ = text_paths("inter", 400, "Un paragraphe court, une idée, une preuve chiffrée.", 30, 90, 580); post += paths_for(t, "#4B5A6B")
w, h, b = inner(f"{OUT}/clixite-relief-color-transparent.svg"); k = 360 / w
post += f'<g transform="translate(90,{1200-h*k-80:.1f}) scale({k:.4f})">{b}</g>'
open(f"{S}/linkedin-post-1200.svg", "w").write(svg_wrap(post, 1200, 1200)); png(f"{S}/linkedin-post-1200.svg", f"{S}/linkedin-post-1200x1200.png", 1200)
print("pack ok:", len(os.listdir(OUT)), "logo files,", len(os.listdir(FAV)), "favicons,", len(os.listdir(S)), "social files")
