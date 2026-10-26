"""Reconstruit les archives de téléchargement de la charte (office, signature, kit complet) après une modification de fichiers,
sans régénérer les visuels. Même logique que la section « zips » de build_site_assets.py."""
import os, zipfile

SITE = "charte"
D = f"{SITE}/downloads"

def zipdir(folder, out, prefix):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(folder):
            for fn in sorted(files):
                if fn.endswith(".zip"):
                    continue
                p = os.path.join(root, fn)
                z.write(p, os.path.join(prefix, os.path.relpath(p, folder)))

zipdir(f"{D}/office", f"{D}/clixite-office.zip", "clixite-office")
zipdir(f"{D}/signature", f"{D}/clixite-signature.zip", "clixite-signature")
with zipfile.ZipFile(f"{D}/clixite-kit-complet.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(D):
        for fn in sorted(files):
            if fn.endswith(".zip"):
                continue
            p = os.path.join(root, fn)
            z.write(p, os.path.join("clixite-kit", os.path.relpath(p, D)))
    for fn in os.listdir(f"{SITE}/animation"):
        z.write(f"{SITE}/animation/{fn}", f"clixite-kit/animation/{fn}")
print("archives ok")
