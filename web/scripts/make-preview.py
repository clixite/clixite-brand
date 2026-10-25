"""Prépare une copie autonome du build de prévisualisation (dist-review) pour la publier comme artefact privé :
chemins absolus réécrits en chemins relatifs, liens de pages vers index.html explicites.
Usage : python3 web/scripts/make-preview.py <dossier_source> <dossier_cible>"""
import os, re, shutil, sys

src, dst = sys.argv[1], sys.argv[2]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)

def rewrite(html, depth):
    up = "../" * depth if depth else "./"
    def page_link(m):
        attr, path, frag = m.group(1), m.group(2), m.group(3) or ""
        if path == "" or path.endswith("/"):
            path += "index.html"
        return f'{attr}="{up}{path}{frag}"'
    # liens de pages et ressources : href="/..." et src="/..." (jamais //)
    html = re.sub(r'(href|src)="/(?!/)([^"#]*)(#[^"]*)?"', page_link, html)
    html = re.sub(r'url\(/(?!/)', f"url({up}", html)
    return html

for root, _, files in os.walk(dst):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            depth = os.path.relpath(p, dst).count(os.sep)
            s = open(p, encoding="utf-8").read()
            open(p, "w", encoding="utf-8").write(rewrite(s, depth))
print("prévisualisation prête :", dst)
