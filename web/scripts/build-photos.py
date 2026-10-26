"""Photos du site : recadrage et traitement Clixite à partir des originaux libres de droits (Unsplash).

Entrées : src/assets/photos/source/<fichier> (originaux, non versionnés : voir l'adresse dans le registre)
et src/data/photos.registry.json (provenance, licence, recadrages, traitement).
Sorties : src/assets/photos/<slug>-<variante>.jpg, que <Picture> d'Astro décline en AVIF et WebP.

Deux traitements, définis avec la direction artistique (DESIGN.md §5 et §9) :
- « lumiere » (photos posées sur Papier) : couleurs gardées à 55 %, balance froide, courbe en S douce,
  noirs ramenés à l'Encre et blancs au Papier, grain fin monochrome pondéré dans les tons moyens ;
- « tirage » (photos posées sur Encre) : tirage de plan, la luminance projetée sur Encre, Encre 600,
  un bleu de Brume teinté de turquoise et Papier ; les ombres valent exactement l'Encre, la photo se fond dans la bande.
Pas de voile, pas de dégradé ajouté, pas de texte sur l'image.
Usage (depuis web/) : python3 scripts/build-photos.py
"""
import json, os, sys, zlib
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "src/assets/photos/source")
OUT = os.path.join(ROOT, "src/assets/photos")
REG = os.path.join(ROOT, "src/data/photos.registry.json")

def rgb(h):
    h = h.lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255

ENCRE, ENCRE6, BRUME, PAPIER, TURQ6 = (rgb(h) for h in ("#0B2239", "#2A4A6E", "#CDD5DD", "#F6F5F0", "#0C7893"))

def lum(c): return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]

def levels(c, lo, hi):
    L = lum(c); a, b = np.percentile(L, lo), np.percentile(L, hi)
    return np.clip((c - a) / max(b - a, 1e-3), 0, 1)

def grain(shape, amount, L, seed):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, shape[:2]).astype(np.float32)
    im = Image.fromarray((n * 40 + 128).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    n = (np.asarray(im).astype(np.float32) - 128) / 40
    return (n * amount * (0.35 + 2.6 * L * (1 - L)))[..., None]

def lumiere(c, p, seed):
    c = levels(c, 0.5, 99.5)
    L = lum(c)[..., None]
    c = L + p.get("saturation", 0.55) * (c - L)
    c = np.clip(c * np.array(p.get("gains", (0.95, 1.0, 1.06)), np.float32), 0, 1)
    s = p.get("courbe", 0.30); c = c + s * (c * c * (3 - 2 * c) - c)
    c = ENCRE + c * (PAPIER - ENCRE)
    return np.clip(c + grain(c.shape, p.get("grain", 0.024), lum(c), seed), 0, 1)

def tirage(c, p, seed):
    c = levels(c, 1, 99)
    L = lum(c) ** p.get("gamma", 1.08)
    stops = [(0.0, ENCRE), (0.45, ENCRE6), (0.80, TURQ6 * 0.35 + BRUME * 0.65), (1.0, PAPIER)]
    o = np.zeros(L.shape + (3,), np.float32)
    for ch in range(3): o[..., ch] = np.interp(L, [s[0] for s in stops], [s[1][ch] for s in stops])
    return np.clip(o + grain(o.shape, p.get("grain", 0.022), L, seed), 0, 1)

def crop(im, c):
    """c : {"ratio": "4:5", "x": 0..1, "y": 0..1} : centre du recadrage, en proportion de l'image."""
    rw, rh = (float(v) for v in c["ratio"].split(":"))
    W, H = im.size
    if W / H > rw / rh: h, w = H, round(H * rw / rh)
    else: w, h = W, round(W * rh / rw)
    cx, cy = c.get("x", 0.5) * W, c.get("y", 0.5) * H
    left = int(min(max(cx - w / 2, 0), W - w)); top = int(min(max(cy - h / 2, 0), H - h))
    return im.crop((left, top, left + w, top + h))

def main():
    reg = json.load(open(REG))
    os.makedirs(OUT, exist_ok=True)
    for ph in reg["photos"]:
        im = Image.open(os.path.join(SRC, ph["fichier"])).convert("RGB")
        for name, c in ph["variantes"].items():
            out = crop(im, c)
            maxw = c.get("largeurMax", 1600)
            if out.width > maxw: out = out.resize((maxw, round(out.height * maxw / out.width)), Image.LANCZOS)
            # dimensions multiples de 8 (grille)
            out = out.crop((0, 0, out.width // 8 * 8, out.height // 8 * 8))
            a = np.asarray(out, np.float32) / 255
            seed = zlib.crc32(f"{ph['slug']}-{name}".encode())
            a = (lumiere if ph["traitement"] == "lumiere" else tirage)(a, ph.get("reglages", {}), seed)
            path = os.path.join(OUT, f"{ph['slug']}-{name}.jpg")
            Image.fromarray((a * 255 + 0.5).astype(np.uint8)).save(path, quality=90, optimize=True, progressive=True)
            print("ok", os.path.basename(path), out.size)

if __name__ == "__main__":
    sys.exit(main())
