"""Génère charte/index.html (site charte.clixite.be) à partir des assets et des textes de la charte."""
import os, re, json, shutil, html
SITE = "charte"; A = f"{SITE}/assets"
SC = "/tmp/claude-0/-home-claude/082fa878-b318-5a61-a8c6-40d163cb8592/scratchpad"
shutil.copy("site_src/site.css", f"{A}/site.css"); shutil.copy("site_src/site.js", f"{A}/site.js")
sizes = json.load(open(f"{SC}/download-sizes.json"))
def size(path):
    n = sizes.get(path, 0)
    return f"{n/1024/1024:.1f} Mo" if n > 1024 * 1024 else f"{n/1024:.0f} Ko"

# ---------------------------------------------------------------- helpers
def hex2rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [v / 255 for v in hex2rgb(h)]; k = 1 - max(r, g, b)
    if k == 1: return "0 0 0 100"
    c, m, y = [(1 - v - k) / (1 - k) for v in (r, g, b)]
    return " ".join(str(round(v * 100)) for v in (c, m, y, k))
def lum(h):
    def ch(v): v /= 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = hex2rgb(h); return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)
def contrast(a, b):
    la, lb = lum(a), lum(b); hi, lo = max(la, lb), min(la, lb); return (hi + 0.05) / (lo + 0.05)
def frag(path):
    s = open(path).read(); return re.sub(r'^<\?xml[^>]*>', '', s)
def inline_logo(name, cls=""):
    s = open(f"{SITE}/downloads/logo/{name}.svg").read()
    s = re.sub(r'\swidth="[\d.]+" height="[\d.]+"', '', s, count=1)
    return s.replace('<svg ', f'<svg class="{cls}" role="img" aria-label="Logo Clixite" ', 1) if cls else s.replace('<svg ', '<svg role="img" aria-label="Logo Clixite" ', 1)

PRIMARY = [
    ("Encre", "#0B2239", "Fond des couvertures, des slides de titre et de l'écran. Texte sur fond clair.", "encre"),
    ("Papier", "#F6F5F0", "Fond de page par défaut. Chaud, jamais blanc clinique.", "papier"),
    ("Turquoise bleu", "#19B3D9", "La marque : symbole, boutons principaux, surfaces. Texte Encre par-dessus.", "turquoise"),
    ("Rose", "#FF4F8B", "Signature : seconde barre du X, pastilles, surlignages. Jamais en texte.", "rose"),
    ("Signal", "#FFD233", "La pièce centrale du X, la lentille, un repère. Ne porte jamais de texte.", "signal"),
]
SECONDARY = [
    ("Turquoise texte", "#0C7893", "Liens, descripteurs et chiffres clés sur fond clair.", "turquoise-texte"),
    ("Rose texte", "#D81B60", "Accent texte sur fond clair quand le rose est attendu.", "rose-texte"),
    ("Indigo", "#193776", "Turquoise multiplié par rose : le chevauchement en data viz et en motion.", "indigo"),
    ("Ardoise", "#4B5A6B", "Texte secondaire, légendes, icônes.", "ardoise"),
    ("Brume", "#CDD5DD", "Filets, bordures, fonds de tableau, texte secondaire sur Encre.", "brume"),
    ("Encre teintée", "#1F3A5A", "Le chant du X sur fond Encre, les surfaces relevées du thème sombre.", "encre-teintee"),
]
def swatch(name, hx, use, var, dark_text=False):
    r, g, b = hex2rgb(hx); light = lum(hx) > 0.35
    return (f'<button class="swatch" type="button" data-hex="{hx}" aria-label="{name}, copier {hx}" style="--c:{hx}">'
            f'<div class="chip" style="background:{hx}"><span>{hx}</span></div>'
            f'<div class="info"><div class="name">{name}</div><div class="vals">RVB {r} {g} {b}<br>CMJN {cmyk(hx)}<br>--clx-{var}</div><div class="use">{use}</div></div></button>')

CONTRAST = [("Encre", "#0B2239", "Papier", "#F6F5F0"), ("Turquoise texte", "#0C7893", "Papier", "#F6F5F0"), ("Rose texte", "#D81B60", "Papier", "#F6F5F0"),
            ("Ardoise", "#4B5A6B", "Papier", "#F6F5F0"), ("Papier", "#F6F5F0", "Encre", "#0B2239"), ("Turquoise", "#19B3D9", "Encre", "#0B2239"),
            ("Rose", "#FF4F8B", "Encre", "#0B2239"), ("Signal", "#FFD233", "Encre", "#0B2239"), ("Brume", "#CDD5DD", "Encre", "#0B2239"), ("Encre", "#0B2239", "Turquoise", "#19B3D9")]
def contrast_rows():
    out = []
    for fn, fg, bn, bg in CONTRAST:
        c = contrast(fg, bg); grade = "AAA" if c >= 7 else "AA" if c >= 4.5 else "AA grand texte" if c >= 3 else "insuffisant"
        out.append(f'<tr><td class="sample"><span style="color:{fg};background:{bg};border:1px solid var(--brume)">Aa</span></td><td>{fn} sur {bn}</td><td class="v">{c:.1f} : 1</td><td><span class="ok">{grade}</span></td></tr>')
    return "".join(out)

FILES_LOGO = [
    ("clixite-relief-color.svg", "Mot-marque Relief, couleur, fond Papier"), ("clixite-relief-color-transparent.svg", "Mot-marque Relief, couleur, fond transparent"),
    ("clixite-relief-inverse-transparent.svg", "Mot-marque Relief, inversé pour fond Encre"), ("clixite-relief-mono-transparent.svg", "Mot-marque Relief, monochrome Encre"),
    ("clixite-relief-symbole-gauche-color-transparent.svg", "Symbole à gauche du nom"), ("clixite-relief-empile-color-transparent.svg", "Version empilée, couleur"),
    ("clixite-relief-empile-inverse-transparent.svg", "Version empilée, inversée"), ("clixite-vivant-color-transparent.svg", "Mot-marque Interférence, couleur (écran, grand format)"),
    ("clixite-vivant-inverse-transparent.svg", "Mot-marque Interférence, inversé"), ("clixite-maitre-color-transparent.svg", "Mot-marque X maître plat (48 px et moins)"),
    ("x-relief-color-transparent.svg", "Symbole Relief, couleur"), ("x-relief-inverse-transparent.svg", "Symbole Relief, inversé"), ("x-relief-mono-transparent.svg", "Symbole Relief, monochrome"),
    ("x-vivant-color-transparent.svg", "Symbole Interférence, couleur"), ("x-vivant-inverse-transparent.svg", "Symbole Interférence, inversé"),
    ("x-maitre-color-transparent.svg", "Symbole X maître plat"), ("x-favicon-encre-transparent.svg", "X plein Encre (favicon, broderie, tampon)"), ("x-app-tile.svg", "Icône d'application, tuile Encre"),
]
def file_rows(folder, items):
    out = []
    for fn, desc in items:
        p = f"downloads/{folder}/{fn}"
        png = re.sub(r'\.svg$', '', fn)
        pngs = [k for k in sizes if k.startswith(f"downloads/{folder}/{png}-") and k.endswith("px.png")]
        extra = " ".join(f'<a href="{k}" download>{re.search(r"-(\d+)px", k).group(1)} px</a>' for k in sorted(pngs, key=lambda s: int(re.search(r"-(\d+)px", s).group(1))))
        out.append(f'<tr><td class="f"><a href="{p}" download>{fn}</a></td><td>{desc}</td><td class="f">{extra}</td><td class="s">{size(p)}</td></tr>')
    return "".join(out)

hero_x = open(f"{A}/living-x-hero.svg.frag").read()
play_x = open(f"{A}/living-x-play.svg.frag").read()
signature = open(f"{SITE}/downloads/signature/signature-mail.html").read()
signature = re.sub(r'<!--.*?-->\s*', '', signature, flags=re.S)
signature_preview = signature.replace("https://charte.clixite.be/downloads/logo/", "downloads/logo/")
tokens_css = open(f"{SITE}/downloads/clixite-variables.css").read()
fonts_css = open(f"{A}/fonts.css").read()
NAV = [("plateforme", "Plateforme"), ("logo", "Logo"), ("couleurs", "Couleurs"), ("typographie", "Typographie"), ("systeme", "Système graphique"),
       ("applications", "Applications"), ("animation", "Animation"), ("voix", "Voix et rédaction"), ("telechargements", "Téléchargements"), ("kit", "Kit développeur"), ("gouvernance", "Gouvernance")]
nav_side = "".join(f'<li><a href="#{i}"><span class="n">{n:02d}</span>{t}</a></li>' for n, (i, t) in enumerate(NAV, 1))
nav_mobile = "".join(f'<a href="#{i}">{n:02d} {t}</a>' for n, (i, t) in enumerate(NAV, 1))

page = r'''<!doctype html>
<html lang="fr-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Charte graphique Clixite</title>
<meta name="description" content="La charte graphique de Clixite : plateforme de marque, logo, couleurs, typographie, applications, animation et tous les fichiers à télécharger.">
<link rel="icon" href="downloads/favicons/favicon.svg" type="image/svg+xml">
<link rel="icon" href="downloads/favicons/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="downloads/favicons/app-icon-180.png">
<meta name="theme-color" content="#0B2239">
<meta property="og:title" content="Charte graphique Clixite">
<meta property="og:description" content="Enterprise & Solution Architecture. La marque, ses règles et ses fichiers.">
<meta property="og:image" content="https://charte.clixite.be/downloads/reseaux/og-image-1200x630.png">
<meta property="og:url" content="https://charte.clixite.be/">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="topbar">
  <a class="brand" href="#top"><img src="downloads/logo/clixite-maitre-inverse-transparent.svg" alt="Clixite" width="110" height="30"><span>Charte graphique</span></a>
  <div class="meta"><span class="version">Version 1.0, octobre 2026</span><a class="btn" href="downloads/clixite-kit-complet.zip" download>Télécharger le kit complet</a></div>
</header>

<section class="hero" id="hero" role="region" aria-labelledby="titre">
  <div class="living">__HERO_X__</div>
  <h1 id="titre">Charte graphique</h1>
  <p class="lede">Clixite est le cabinet d'architecture de solutions de Nicolas Simon. Cette charte fixe la marque, ses règles et ses fichiers. Elle sert à tout le monde : Nicolas, ses partenaires, un imprimeur, un développeur.</p>
  <p class="hint"><span class="mouse">Déplacez le curseur sur le X : </span><span class="touch">Glissez le doigt sur le X : </span><b>l'interférence se résout</b>.</p>
  <div class="scrolldown" aria-hidden="true"></div>
</section>

<nav class="mobilenav" aria-label="Chapitres">__NAV_MOBILE__</nav>
<div class="shell" id="top">
<nav class="sidenav" aria-label="Chapitres">
  <ol>__NAV_SIDE__</ol>
  <div class="kit"><p>Tout le kit dans une archive : logos, favicons, réseaux, Office, signature, animation.</p><a class="btn secondary" href="downloads/clixite-kit-complet.zip" download>Kit complet, __KIT_SIZE__</a></div>
</nav>
<main>

<!-- ===================================================== 01 PLATEFORME -->
<section class="chapter" id="plateforme">
  <header><span class="n">01</span><h2>Plateforme de marque</h2>
  <p class="lede">Clixite existe depuis 2005. Agence de communication pendant dix ans, le cabinet est devenu ce que son fondateur est devenu : un architecte de solutions et d'entreprise. Il relie la stratégie, les systèmes et la conformité, puis livre.</p></header>

  <h3>L'idée</h3>
  <p class="quote">L'architecte qui relie la stratégie, les systèmes et la conformité. Nous résolvons votre <span class="x">x</span>.</p>
  <p>Le <span class="x">x</span> est l'inconnue du client : un processus achats qui ne tient pas l'audit, un back-office qui ne suit plus la croissance, une exigence DORA qu'il faut traduire en preuves. Clixite dessine la structure, puis construit. Ce récit vit dans les textes, pas dans le logo : le logo porte seulement le X.</p>

  <h3>Promesse</h3>
  <p>Des cadres clairs, des processus qui tiennent à l'audit et des outils qui tournent réellement. Pas de slides pour les slides.</p>

  <h3>Deux terrains, un même métier</h3>
  <div class="markets">
    <div><h4>Grands comptes régulés</h4><p>Banque, assurance, télécom. Procurement, conformité, architecture d'entreprise. Preuves : 800 M€ d'achats pilotés chez Proximus, Procurement Policy v2.0 et Tactical Sourcing Light Track en production chez KBC, missions chez P&amp;V.</p></div>
    <div><h4>PME en croissance</h4><p>Audit, choix et connexion des outils existants, automatisation, IA quand elle sert. Architecturer la croissance avec ce qui existe déjà. Preuves : sites et back-offices de Tero et Design Plus, CyGap et Vidango conçus et codés.</p></div>
  </div>

  <h3>Piliers</h3>
  <div class="pillars">
    <div><h4>Structure</h4><p>Policies, architectures et playbooks à trois niveaux. Le désordre devient un système.</p></div>
    <div><h4>Conformité maîtrisée</h4><p>DORA, NIS2, RGPD, EBA : des exigences traduites en processus et en preuves.</p></div>
    <div><h4>Pragmatisme</h4><p>Livrer, mesurer, ajuster. Des décisions rationnelles, une vision humaine.</p></div>
    <div><h4>Build</h4><p>Concevoir et coder : agents IA, SaaS, automatisations. L'IA est un levier, jamais le produit.</p></div>
  </div>

  <h3>Personnalité</h3>
  <p>L'Architecte : sage et créateur. Précis, direct, exigeant, calme, humain, avec un brin d'humour belge. Il parle en chiffres et en plans, pas en adjectifs.</p>

  <h3>Architecture de marque</h3>
  <div class="archi">
    <div><h4>Clixite</h4><p>La marque mère et la caution. Services : Fractional CPO, transformation Source-to-Pay, conformité DORA et NIS2, architecture d'entreprise, architecture de croissance pour les PME.</p></div>
    <div><h4>by Clixite</h4><p>Les produits endossés : Vidango (VOS) et CyGap. Ils gardent leur nom, portent la mention « by Clixite » et empruntent la palette.</p></div>
    <div><h4>Marque sœur</h4><p>L'agence montée avec Chris, nom à trouver. Elle peut porter « powered by Clixite » sans reprendre le X.</p></div>
  </div>
</section>

<!-- ===================================================== 02 LOGO -->
<section class="chapter" id="logo">
  <header><span class="n">02</span><h2>Logo</h2>
  <p class="lede">Le X est central dans CLIXITE depuis 2005 et il le reste. Il est redessiné au poids des lettres, puis reçoit une peau selon le support : le Relief, qui se dépose et s'imprime, ou l'Interférence, qui vit à l'écran.</p></header>

  <figure class="logo-hero">__LOGO_RELIEF__<figcaption class="cap">Mot-marque, peau Relief, version couleur. Le fichier de référence pour tout ce qui s'imprime et se dépose.</figcaption></figure>

  <div class="spec">
    <div class="text">
      <h3 style="margin-top:0">Un X maître, deux peaux</h3>
      <p>Le X maître est la marque : deux barres au poids des capitales, turquoise par-dessus rose, une pièce centrale Signal détachée par un joint fin, des terminaisons horizontales. Il dépasse les capitales de 5 % en haut et en bas, comme un O.</p>
      <p>Sous 48 px, le X maître plat. Sous 24 px, le X plein en Encre.</p>
    </div>
    <div class="text">
      <h3 style="margin-top:0">Les peaux</h3>
      <p>Au-dessus de 48 px, le X reçoit une peau. Le <strong>Relief</strong> extrude le X de 0,30 barre, à 70°, avec un chant Encre : c'est la marque déposée, celle qui s'imprime. L'<strong>Interférence</strong> remplace la face par deux champs de lignes, turquoise et rose, tournés l'un par rapport à l'autre, avec une lentille Signal au croisement : c'est l'expression vivante, pour le site, les bannières et le mouvement.</p>
    </div>
  </div>
  <figure class="full"><div class="panel"><img src="assets/construction.svg" alt="Construction du mot-marque : capitale, dépassement de 5 %, barre égale à 1,08 fût, chant de 0,30 barre à 70°, silhouette du X centrée entre les deux I" width="1400" height="560"></div><figcaption class="cap">Construction. La silhouette complète du X, face et chant, est centrée entre les deux I au pixel près.</figcaption></figure>

  <h3>Les quatre niveaux de taille</h3>
  <p>La règle tient en une ligne : plus le X est petit, plus il se simplifie. Les tailles s'entendent pour la hauteur du X à l'écran, ou leur équivalent imprimé (1 px = 0,25 mm à 100 dpi).</p>
  <div class="levels">
    <div><div class="box"><img src="downloads/logo/x-vivant-color-transparent.svg" alt="X Interférence à 200 pixels" style="width:303px"></div><h4>200 px et plus</h4><p>Interférence complète : dix traits par barre, trait égal au vide, lentille Signal. Site, bannières, animation.</p></div>
    <div><div class="box"><img src="downloads/logo/x-vivant-color-transparent.svg" alt="X Interférence simplifié à 100 pixels" style="width:152px"></div><h4>De 48 à 200 px</h4><p>Interférence simplifiée (six traits, jamais moins de 1,5 px) ou Relief. Avatars, en-têtes, signature.</p></div>
    <div><div class="box"><img src="downloads/logo/x-relief-color-transparent.svg" alt="X Relief à 60 pixels" style="width:91px"><img src="downloads/logo/x-maitre-color-transparent.svg" alt="X maître plat à 36 pixels" style="width:55px"></div><h4>Sous 48 px</h4><p>Le X maître plat, deux couleurs et la pièce Signal. Icônes d'interface, pied de page.</p></div>
    <div><div class="box"><img src="downloads/favicons/favicon.svg" alt="X plein Encre à 24 pixels" style="width:36px"><img src="downloads/favicons/favicon.svg" alt="X plein Encre à 16 pixels" style="width:24px"><img src="downloads/logo/x-app-tile.svg" alt="Icône d'application" style="width:64px"></div><h4>Sous 24 px</h4><p>Le X plein en Encre. Favicon, broderie, tampon. L'icône d'app garde le Relief sur tuile Encre.</p></div>
  </div>

  <h3>Versions</h3>
  <div class="variants">
    <figure class="panel"><img src="downloads/logo/clixite-relief-color-transparent.svg" alt="Mot-marque couleur sur fond blanc"><figcaption>Couleur, sur Papier ou blanc</figcaption></figure>
    <figure class="panel dark"><img src="downloads/logo/clixite-relief-inverse-transparent.svg" alt="Mot-marque inversé sur fond Encre"><figcaption>Inversé, sur Encre : lettres Papier, chant Encre teintée</figcaption></figure>
    <figure class="panel papier"><img src="downloads/logo/clixite-relief-mono-transparent.svg" alt="Mot-marque monochrome Encre"><figcaption>Monochrome Encre, sur photo ou fond coloré</figcaption></figure>
    <figure class="panel"><img src="downloads/logo/clixite-relief-symbole-gauche-color-transparent.svg" alt="Symbole à gauche du nom"><figcaption>Symbole à gauche : en-têtes étroits, co-branding</figcaption></figure>
    <figure class="panel"><img src="downloads/logo/clixite-relief-empile-color-transparent.svg" alt="Version empilée" style="width:62%"><figcaption>Empilé : avatars, formats carrés, pieds de page</figcaption></figure>
    <figure class="panel dark"><img src="downloads/logo/clixite-vivant-inverse-transparent.svg" alt="Mot-marque Interférence sur Encre"><figcaption>Interférence, sur Encre : écran et grands formats uniquement</figcaption></figure>
  </div>

  <div class="spec flip" style="margin-top:40px">
    <figure><img src="assets/zone-de-protection.svg" alt="Zone de protection : la hauteur du X autour du logo" width="1000" height="560"><figcaption class="cap">Zone de protection : la hauteur du X, sur les quatre côtés. Aucun texte, aucune image, aucun autre logo dedans.</figcaption></figure>
    <div class="text">
      <h3 style="margin-top:0">Espace et tailles minimales</h3>
      <p>La zone de protection vaut la hauteur du X, sur les quatre côtés. Elle grandit avec le logo.</p>
      <p>Taille minimale du mot-marque : 96 px à l'écran, 24 mm imprimé. Symbole Relief : 48 px ou 12 mm. Favicon : 16 px, en X plein Encre.</p>
      <p>Les descripteurs d'offre (« Fractional CPO », « Architecture de croissance ») se composent en texte, en turquoise texte, sous le logo. Ils ne sont jamais intégrés au fichier du logo. Le descripteur du logo reste en anglais : ENTERPRISE &amp; SOLUTION ARCHITECTURE.</p>
    </div>
  </div>

  <h3>Ce qu'on ne fait pas</h3>
  <div class="donts">
    <figure class="stretch"><div class="pic"><img src="downloads/logo/clixite-relief-color-transparent.svg" alt=""></div><figcaption>Étirer ou écraser</figcaption></figure>
    <figure><div class="pic"><img src="assets/interdit-couleurs.svg" alt=""></div><figcaption>Inverser l'ordre des couleurs : le turquoise passe toujours par-dessus le rose</figcaption></figure>
    <figure class="fond-turq"><div class="pic"><img src="downloads/logo/clixite-relief-color-transparent.svg" alt=""></div><figcaption style="color:#0B2239">Poser le logo sur du turquoise, du rose ou du Signal</figcaption></figure>
    <figure class="shadow"><div class="pic"><img src="downloads/logo/clixite-relief-color-transparent.svg" alt=""></div><figcaption>Ajouter une ombre portée</figcaption></figure>
    <figure><div class="pic"><img src="assets/interdit-contour.svg" alt=""></div><figcaption>Ajouter un contour</figcaption></figure>
    <figure class="tilt"><div class="pic"><img src="downloads/logo/clixite-relief-color-transparent.svg" alt=""></div><figcaption>Incliner, ni réécrire le descripteur dans une autre police</figcaption></figure>
  </div>

  <h3 id="atelier">L'atelier de l'interférence</h3>
  <p>L'angle entre les deux champs est la seule variable de la peau Interférence. Au repos il vaut 8°. En mouvement il respire entre 6° et 10°, et il se résout vers 4° quand l'ouverture se termine. Essayez.</p>
  <div class="atelier">
    <div class="living">__PLAY_X__</div>
    <div>
      <label for="angle">Angle entre les champs <output id="angle-out">8°</output></label>
      <input type="range" id="angle" min="0" max="20" step="0.5" value="8">
      <p class="note">Sous 2°, les deux champs se superposent et le X devient plat. Au-delà de 14°, le moiré prend le dessus sur la lettre. L'intervalle utile est 4° à 12°.</p>
      <button class="btn secondary" id="angle-reset" type="button">Revenir à 8°</button>
      <button class="btn secondary" id="angle-free" type="button">Laisser respirer</button>
    </div>
  </div>
</section>

<!-- ===================================================== 03 COULEURS -->
<section class="chapter" id="couleurs">
  <header><span class="n">03</span><h2>Couleurs</h2>
  <p class="lede">Le trio turquoise bleu, rose et Signal est la signature de Clixite. Il vit ensemble dans le symbole et dans les moments de signature. Dans le corps d'un document, un seul accent à la fois, turquoise par défaut. Cliquez une teinte pour copier son code.</p></header>

  <h3>Palette principale</h3>
  <div class="swatches">__SWATCHES_PRIMARY__</div>
  <p class="note">Valeurs CMJN indicatives, converties depuis le RVB. Pour l'impression offset, faire valider une épreuve ; les références Pantone se choisissent avec l'imprimeur, sur nuancier, pour le turquoise et le rose.</p>

  <h3>Palette secondaire</h3>
  <div class="swatches secondary">__SWATCHES_SECONDARY__</div>

  <h3>Proportions</h3>
  <p>Répartition indicative sur un support complet. L'Encre domine, le Papier respire, le turquoise signe, le rose et le Signal ponctuent.</p>
  <div class="ratio"><div class="bar">
    <span style="width:45%;background:#0B2239;color:#F6F5F0">Encre 45 %</span><span style="width:25%;background:#F6F5F0;color:#0B2239">Papier 25 %</span><span style="width:15%;background:#19B3D9;color:#0B2239">Turquoise 15 %</span><span style="width:8%;background:#FF4F8B;color:#0B2239">Rose 8 %</span><span style="width:7%;background:#FFD233;color:#0B2239">Signal 7 %</span>
  </div></div>

  <h3>Combinaisons</h3>
  <p>Texte et fond : ce qui est permis, ce qui ne l'est pas. Les accents ne portent pas de texte sur fond clair ; on passe par leur version « texte ».</p>
  <div class="combos" role="img" aria-label="Huit combinaisons texte et fond : six permises, deux barrées (turquoise sur Papier, texte sur Signal)">
    <div style="background:#F6F5F0;color:#0B2239">Encre sur Papier</div>
    <div style="background:#0B2239;color:#F6F5F0">Papier sur Encre</div>
    <div style="background:#F6F5F0;color:#0C7893">Turquoise texte sur Papier</div>
    <div style="background:#0B2239;color:#19B3D9">Turquoise sur Encre</div>
    <div style="background:#19B3D9;color:#0B2239">Encre sur turquoise</div>
    <div style="background:#0B2239;color:#FFD233">Signal sur Encre, en repère seulement</div>
    <div class="no" aria-hidden="true" style="background:#F6F5F0;color:#19B3D9">Turquoise sur Papier</div>
    <div class="no" aria-hidden="true" style="background:#FFD233;color:#F6F5F0">Texte sur Signal</div>
  </div>

  <h3>Contrastes vérifiés</h3>
  <table class="contrast"><thead><tr><th>Échantillon</th><th>Paire</th><th style="text-align:right">Ratio</th><th>WCAG 2.2</th></tr></thead><tbody>__CONTRAST__</tbody></table>
  <p class="note">États : « succès » et « danger » sont toujours accompagnés d'un libellé ou d'une icône, et diffèrent en luminosité, jamais seulement en teinte. Jamais de vert et rouge seuls pour distinguer deux états.</p>
</section>

<!-- ===================================================== 04 TYPOGRAPHIE -->
<section class="chapter" id="typographie">
  <header><span class="n">04</span><h2>Typographie</h2>
  <p class="lede">Quatre familles, chacune avec un rôle, toutes libres (licence OFL). Space Grotesk donne le caractère, Inter fait le travail, Fraunces apporte la voix, JetBrains Mono tient les chiffres.</p></header>

  <div class="specimen">
    <div class="sample display">Architecture<small>Space Grotesk, graisses 500 à 700</small></div>
    <div class="about"><b>Space Grotesk</b>Titres, mot-marque, chiffres clés. Géométrique avec du caractère, un côté plan d'architecte. Approche négative sur les grands corps (-2 %).<a href="https://fonts.google.com/specimen/Space+Grotesk">Google Fonts</a></div>
  </div>
  <div class="specimen">
    <div class="sample sans">Inter porte le texte courant, les mails, les interfaces et les SaaS. Graisses 400 à 600, jamais plus. Interligne 1,5. Elle reste lisible à 13 px dans un tableau comme à 19 px dans une introduction, et elle ne vole jamais la vedette à Space Grotesk.</div>
    <div class="about"><b>Inter</b>Texte courant, interfaces, mails, documents Office.<a href="https://fonts.google.com/specimen/Inter">Google Fonts</a></div>
  </div>
  <div class="specimen">
    <div class="sample editorial">Nous résolvons votre <span class="x" style="color:#0C7893">x</span>.</div>
    <div class="about"><b>Fraunces Italic</b>La voix éditoriale : citations, chiffres clés, et le x variable. Toujours en italique, jamais en pavé. Graisses 500 et 600.<a href="https://fonts.google.com/specimen/Fraunces">Google Fonts</a></div>
  </div>
  <div class="specimen">
    <div class="sample mono">PROCUREMENT POLICY V2.0 · KBC · 2024<br>DORA · NIS2 · RGPD · EBA<br>#19B3D9 · 800 M€ · 12 semaines</div>
    <div class="about"><b>JetBrains Mono</b>Données, références, identifiants et étiquettes en capitales espacées. Le clin d'œil au builder. Graisse 500.<a href="https://fonts.google.com/specimen/JetBrains+Mono">Google Fonts</a></div>
  </div>

  <h3>Échelle</h3>
  <table class="scale">
    <tr><td>display</td><td class="s-display">Du cadre à la livraison</td><td>Space Grotesk 700, 56 px, interligne 1, approche -2 %</td></tr>
    <tr><td>h1</td><td class="s-h1">Architecturer la croissance</td><td>Space Grotesk 600, 40 px, interligne 1,05</td></tr>
    <tr><td>h2</td><td class="s-h2">Ce que nous avons compris</td><td>Space Grotesk 600, 28 px, interligne 1,15</td></tr>
    <tr><td>h3</td><td class="s-h3">Étape 1, cadrer</td><td>Space Grotesk 600, 20 px, interligne 1,25</td></tr>
    <tr><td>quote</td><td class="s-quote">Des processus qui tiennent à l'audit.</td><td>Fraunces Italic 500, 26 px, interligne 1,3</td></tr>
    <tr><td>body</td><td class="s-body">Nous mettons votre policy achats en production en douze semaines, avec les preuves pour l'audit.</td><td>Inter 400, 16 px, interligne 1,5</td></tr>
    <tr><td>small</td><td class="s-small">Prix hors TVA, facturation mensuelle à 30 jours.</td><td>Inter 400, 13 px, interligne 1,45</td></tr>
    <tr><td>label</td><td class="s-label">Proposition de services</td><td>JetBrains Mono 500, 12 px, capitales, approche +8 %</td></tr>
    <tr><td>data</td><td class="s-data">12 345,00 € · 2026-10-25 · v1.0</td><td>JetBrains Mono 500, 14 px, chiffres alignés à droite</td></tr>
  </table>
  <p>Dans Office, les modèles embarquent Space Grotesk et Inter. Installez les polices du kit avant d'ouvrir les modèles ; sans elles, Word et PowerPoint retombent sur Arial et Calibri, ce qui reste acceptable pour un document de travail mais pas pour une offre.</p>
  <p><a class="btn secondary" href="downloads/fonts/clixite-polices.zip" download>Télécharger les polices, __FONTS_SIZE__</a></p>
</section>

<!-- ===================================================== 05 SYSTEME -->
<section class="chapter" id="systeme">
  <header><span class="n">05</span><h2>Système graphique</h2>
  <p class="lede">Trois motifs sortent du logo et suffisent à habiller tous les supports. Ils s'emploient un à la fois, en grand, jamais en semis décoratif.</p></header>
  <div class="system">
    <div><div class="vis"><svg viewBox="0 0 160 120" width="160" height="120" aria-hidden="true"><rect width="160" height="120" fill="#F6F5F0"/><g transform="translate(80,60) rotate(45)"><rect x="-38" y="-38" width="76" height="76" fill="#FFD233"/></g></svg></div><h3>La lentille</h3><p>Le losange Signal du croisement. Un seul par support, posé sur un chiffre clé, un repère de carte, un point d'attention.</p></div>
    <div><div class="vis"><svg viewBox="0 0 160 120" width="160" height="120" aria-hidden="true"><rect width="160" height="120" fill="#F6F5F0"/><g transform="rotate(-4 80 60)">__LINES_T__</g><g transform="rotate(4 80 60)" opacity=".85">__LINES_R__</g></svg></div><h3>Les champs</h3><p>Deux champs de lignes, turquoise et rose, à 8° l'un de l'autre. En fond de couverture, en bandeau de site, en masque sur une photo. Jamais sous du texte courant.</p></div>
    <div><div class="vis"><svg viewBox="0 0 160 120" width="160" height="120" aria-hidden="true"><rect width="160" height="120" fill="#F6F5F0"/><path d="M40 30 h80 v22 h-80z" fill="#0B2239"/><path d="M34 22 h80 v22 h-80z" fill="#19B3D9"/><path d="M40 72 h80 v22 h-80z" fill="#0B2239"/><path d="M34 64 h80 v22 h-80z" fill="#FF4F8B"/></svg></div><h3>Le chant</h3><p>L'extrusion à 70°, en Encre. Elle donne du relief à un bloc, un bouton principal, une carte de visite. Une seule épaisseur : 0,30 de la hauteur de l'élément.</p></div>
  </div>

  <h3>Mise en page</h3>
  <ul class="rules">
    <li>Grille de 8 px. Marges de page 64 px sur grand écran, 16 px sur mobile. Colonne de texte de 62 caractères au plus.</li>
    <li>Cartes : fond blanc, bordure 1 px Brume, rayon 10 px, padding 24 px. Pas d'ombre portée, pas de bordure colorée à gauche.</li>
    <li>Boutons : principal fond turquoise, texte Encre ; secondaire bordure Brume, texte Encre ; lien en turquoise texte. Hauteur 44 px minimum, forme pilule.</li>
    <li>Tableaux : en-tête Papier, chiffres en JetBrains Mono alignés à droite, filets Brume.</li>
    <li>Slides : fond Encre pour les titres, Papier pour le contenu ; le symbole en haut à droite à 36 px ; numérotation en mono.</li>
    <li>Icônes : trait 1,75 px, coins arrondis, 24 px, en Encre ou Ardoise. Pas d'émoji dans les supports de marque.</li>
    <li>Data viz : séries dans l'ordre turquoise, rose, Signal, Ardoise, Indigo. Deux séries qui se chevauchent prennent l'Indigo.</li>
    <li>Photos : des lieux et des gens réels, lumière naturelle, légère dominante froide. Jamais de banque d'images « poignée de main ». Le logo monochrome dessus, ou rien.</li>
  </ul>
  <div class="icons" aria-hidden="true">
    <svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18M9 21V9"/></svg>
    <svg viewBox="0 0 24 24"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/></svg>
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
    <svg viewBox="0 0 24 24"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/></svg>
    <svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h10M4 17h7"/></svg>
    <svg viewBox="0 0 24 24"><path d="M5 19L19 5M5 5l14 14"/></svg>
    <span class="note" style="margin:0">Style des icônes : trait 1,75 px, 24 px.</span>
  </div>
</section>

<!-- ===================================================== 06 APPLICATIONS -->
<section class="chapter" id="applications">
  <header><span class="n">06</span><h2>Applications</h2>
  <p class="lede">Les supports du quotidien, prêts à l'emploi. Chaque fichier se télécharge ici ; les modèles Office se trouvent au chapitre Téléchargements.</p></header>
  <div class="apps">
    <figure class="dark"><img src="downloads/reseaux/linkedin-banniere-1584x396.png" alt="Bannière LinkedIn" width="1584" height="396" loading="lazy"><figcaption>Bannière LinkedIn, 1584 × 396<a href="downloads/reseaux/linkedin-banniere-1584x396.png" download>PNG</a></figcaption></figure>
    <figure class="dark"><img src="downloads/reseaux/og-image-1200x630.png" alt="Image de partage" width="1200" height="630" loading="lazy"><figcaption>Image de partage (Open Graph), 1200 × 630<a href="downloads/reseaux/og-image-1200x630.png" download>PNG</a></figcaption></figure>
    <figure><img src="downloads/reseaux/linkedin-post-1200x1200.png" alt="Gabarit de publication LinkedIn" width="1200" height="1200" loading="lazy"><figcaption>Gabarit de publication, 1200 × 1200<a href="downloads/reseaux/linkedin-post-1200.svg" download>SVG</a></figcaption></figure>
    <figure class="dark"><img src="downloads/reseaux/linkedin-avatar-800.png" alt="Avatar" width="800" height="800" loading="lazy" style="width:50%;margin:0 auto"><figcaption>Avatar, 800 × 800<a href="downloads/reseaux/linkedin-avatar-800.png" download>PNG</a></figcaption></figure>
    <figure class="dark"><img src="downloads/reseaux/fond-visio-encre-1920x1080.png" alt="Fond de visioconférence Encre" width="1920" height="1080" loading="lazy"><figcaption>Fond de visio, Encre, 1920 × 1080<a href="downloads/reseaux/fond-visio-encre-1920x1080.png" download>PNG</a></figcaption></figure>
    <figure><img src="downloads/reseaux/fond-visio-papier-1920x1080.png" alt="Fond de visioconférence Papier" width="1920" height="1080" loading="lazy"><figcaption>Fond de visio, Papier, 1920 × 1080<a href="downloads/reseaux/fond-visio-papier-1920x1080.png" download>PNG</a></figcaption></figure>
    <figure><img src="apercus/apercu-presentation.png" alt="Aperçu du gabarit de présentation" loading="lazy"><figcaption>Gabarit de présentation, 9 mises en page<a href="downloads/office/Clixite-gabarit-presentation.pptx" download>PPTX</a></figcaption></figure>
    <figure><img src="apercus/apercu-offre.png" alt="Aperçu du modèle d'offre" loading="lazy"><figcaption>Modèle d'offre, 7 sections<a href="downloads/office/Clixite-modele-offre.docx" download>DOCX</a></figcaption></figure>
    <figure><img src="apercus/apercu-papier-a-lettre.png" alt="Aperçu du papier à lettre" loading="lazy" style="width:60%;margin:0 auto"><figcaption>Papier à lettre<a href="downloads/office/Clixite-papier-a-lettre.docx" download>DOCX</a></figcaption></figure>
    <figure><img src="apercus/apercu-tableau.png" alt="Aperçu du tableau de suivi" loading="lazy"><figcaption>Tableau de suivi, styles et KPI<a href="downloads/office/Clixite-tableau-de-suivi.xlsx" download>XLSX</a></figcaption></figure>
  </div>

  <h3>Signature mail</h3>
  <p>Copier le bloc ci-dessous dans Outlook, Gmail ou Apple Mail (coller en HTML), puis remplacer le GSM. Le symbole est chargé depuis ce site, donc il reste à jour.</p>
  <div class="sigwrap">__SIGNATURE__</div>
  <p><a class="btn secondary" href="downloads/signature/signature-mail.html" download>Fichier HTML de la signature</a> <a class="btn secondary" href="downloads/signature/signature-mail.txt" download>Version texte</a></p>
</section>

<!-- ===================================================== 07 ANIMATION -->
<section class="chapter" id="animation">
  <header><span class="n">07</span><h2>Animation</h2>
  <p class="lede">L'ouverture dure trois secondes et raconte le logo : deux champs qui arrivent, un angle qui se résout, une lentille qui s'allume, un chant qui tombe, les lettres qui se posent. Puis le X respire.</p></header>
  <div class="anim-stage"><iframe id="anim-frame" src="animation/clixite-ouverture.html" title="Animation d'ouverture Clixite" loading="lazy"></iframe></div>
  <div class="anim-actions">
    <button class="btn secondary" id="replay" type="button">Rejouer</button>
    <a class="btn secondary" href="animation/clixite-ouverture-1080p.mp4" download>MP4 1080p</a>
    <a class="btn secondary" href="animation/clixite-ouverture-800.gif" download>GIF 800 px</a>
    <a class="btn secondary" href="animation/clixite-ouverture.html" download>HTML autonome</a>
  </div>
  <div class="timeline">
    <div><b>0 à 0,8 s</b>Les deux champs glissent depuis les coins, à 14° l'un de l'autre.</div>
    <div><b>0,8 à 2 s</b>L'angle se résout de 14° vers 4°. La lentille s'allume à 1,2 s.</div>
    <div><b>2 à 2,6 s</b>Le chant tombe : le X prend son relief.</div>
    <div><b>2,6 à 3 s</b>CLI et ITE se posent de chaque côté, puis le descripteur.</div>
    <div><b>Repos</b>L'angle respire entre 4° et 6° sur six secondes. Aucune autre boucle.</div>
  </div>
  <h3>Règles de mouvement</h3>
  <ul class="rules">
    <li>Courbe unique : cubic-bezier(.2, .8, .2, 1). Rien ne rebondit, rien n'élastique.</li>
    <li>Durées : 450 ms pour un élément, 600 ms pour un bloc, 3 s pour l'ouverture complète. Jamais plus.</li>
    <li>Une seule séquence orchestrée par page ou par vidéo. Pas d'apparition en fondu section par section.</li>
    <li>Le X ne tourne jamais sur lui-même. Seul l'angle entre les champs change.</li>
    <li>Respecter prefers-reduced-motion : le logo s'affiche alors directement, au repos.</li>
    <li>Fond Encre par défaut ; sur Papier, le chant devient Encre et les champs gardent leurs couleurs.</li>
  </ul>
</section>

<!-- ===================================================== 08 VOIX -->
<section class="chapter" id="voix">
  <header><span class="n">08</span><h2>Voix et rédaction</h2>
  <p class="lede">Clixite écrit comme son fondateur parle : phrases courtes, verbes d'action, chiffres avant adjectifs. Une note d'humour sec quand elle détend sans décrédibiliser.</p></header>
  <ul class="rules">
    <li>Vouvoiement en externe. Français de Belgique, anglais et néerlandais sans traduction mot à mot : on écrit dans la langue du lecteur.</li>
    <li>Jamais de buzzwords (« synergies », « disruption », « game changer »), jamais de hype IA, jamais de promesse vague.</li>
    <li>Le descripteur de la marque reste en anglais sur tous les supports : ENTERPRISE &amp; SOLUTION ARCHITECTURE.</li>
    <li>Le <span class="x">x</span> en italique Fraunces est le seul effet typographique autorisé dans un titre : il marque l'inconnue que l'on résout.</li>
    <li>Pas de tirets longs dans les textes ; une virgule, un point ou deux points font le travail.</li>
    <li>Les chiffres portent leur preuve : 800 M€ pilotés, douze semaines, v2.0 en production.</li>
  </ul>
  <div class="voice">
    <div><span class="bad">Nous accompagnons votre transformation digitale de bout en bout.</span><span class="good">Nous mettons votre policy achats en production en douze semaines, avec les preuves pour l'audit.</span></div>
    <div><span class="bad">Une solution innovante propulsée par l'IA pour booster votre croissance.</span><span class="good">Vos outils existants, connectés et automatisés. L'IA là où elle fait gagner du temps, nulle part ailleurs.</span></div>
    <div><span class="bad">Expert en conformité réglementaire multisectorielle.</span><span class="good">DORA et NIS2 traduits en processus, en responsables et en preuves. Audit compris.</span></div>
    <div><span class="bad">N'hésitez pas à nous contacter pour plus d'informations.</span><span class="good">Un premier échange de trente minutes suffit pour cadrer votre <span class="x">x</span>.</span></div>
  </div>
</section>

<!-- ===================================================== 09 TELECHARGEMENTS -->
<section class="chapter" id="telechargements">
  <header><span class="n">09</span><h2>Téléchargements</h2>
  <p class="lede">Tout est ici, en vectoriel et en raster, prêt à l'emploi. Les archives regroupent chaque famille de fichiers ; le kit complet contient tout.</p></header>
  <div class="packs">
    <div class="pack main"><div><h3>Kit complet</h3><p>Logos, favicons, réseaux, Office, signature, animation, polices, tokens.</p></div><a class="btn" href="downloads/clixite-kit-complet.zip" download>Télécharger, __KIT_SIZE__</a></div>
    <div class="pack"><h3>Logos</h3><p>Mot-marque et symbole, trois peaux, couleur, inversé, monochrome ; SVG et PNG jusqu'à 3200 px.</p><span class="size">__LOGOS_SIZE__</span><a class="btn secondary" href="downloads/clixite-logos.zip" download>clixite-logos.zip</a></div>
    <div class="pack"><h3>Favicons et icônes d'app</h3><p>favicon.ico, SVG, PNG de 16 à 512 px, icône d'app, site.webmanifest.</p><span class="size">__FAV_SIZE__</span><a class="btn secondary" href="downloads/clixite-favicons.zip" download>clixite-favicons.zip</a></div>
    <div class="pack"><h3>Réseaux et visio</h3><p>Avatar, bannière LinkedIn, image Open Graph, fonds de visio, gabarit de publication.</p><span class="size">__RES_SIZE__</span><a class="btn secondary" href="downloads/clixite-reseaux.zip" download>clixite-reseaux.zip</a></div>
    <div class="pack"><h3>Modèles Office</h3><p>Présentation PowerPoint (9 mises en page), papier à lettre, modèle d'offre, tableau de suivi Excel.</p><span class="size">__OFF_SIZE__</span><a class="btn secondary" href="downloads/clixite-office.zip" download>clixite-office.zip</a></div>
    <div class="pack"><h3>Polices</h3><p>Space Grotesk, Inter, Fraunces en TTF pour Office, avec leurs licences OFL.</p><span class="size">__FONTS_SIZE__</span><a class="btn secondary" href="downloads/fonts/clixite-polices.zip" download>clixite-polices.zip</a></div>
    <div class="pack"><h3>Animation</h3><p>Ouverture en HTML autonome, MP4 1080p, GIF 800 px et image d'affiche.</p><span class="size">__ANIM_SIZE__</span><a class="btn secondary" href="downloads/clixite-animation.zip" download>clixite-animation.zip</a></div>
  </div>
  <details class="more"><summary>Fichiers du logo, un par un</summary>
  <table class="files"><thead><tr><th>Fichier</th><th>Usage</th><th>PNG</th><th style="text-align:right">SVG</th></tr></thead><tbody>__FILES_LOGO__</tbody></table>
  <p class="note">Les fichiers « transparent » n'ont pas de fond : ce sont ceux à utiliser dans un document. Les fichiers avec fond Papier ou Encre servent d'aperçu et de référence de dépôt.</p>
  </details>
</section>

<!-- ===================================================== 10 KIT DEV -->
<section class="chapter" id="kit">
  <header><span class="n">10</span><h2>Kit développeur</h2>
  <p class="lede">Pour un site, une application ou un produit « by Clixite » : les variables, les polices et les balises à copier.</p></header>
  <h3>Variables CSS</h3>
  <div class="codeblock"><pre><code>__CSS_VARS__</code></pre><button class="btn secondary copy" type="button">Copier</button></div>
  <p><a href="downloads/clixite-variables.css" download>clixite-variables.css</a> et <a href="downloads/clixite-tokens.json" download>clixite-tokens.json</a> (thèmes clair et sombre, styles de texte, espacements, rayons).</p>
  <h3>Polices</h3>
  <p>Depuis Google Fonts, en une ligne :</p>
  <div class="codeblock wrap"><pre><code>&lt;link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&amp;family=Inter:wght@400;500;600&amp;family=Fraunces:ital,wght@1,500;1,600&amp;family=JetBrains+Mono:wght@500&amp;display=swap"&gt;</code></pre><button class="btn secondary copy" type="button">Copier</button></div>
  <p>Ou auto-hébergées, comme sur ce site : copier le dossier <code>fonts/</code> et <code>assets/fonts.css</code>.</p>
  <h3>Favicon et partage</h3>
  <div class="codeblock"><pre><code>&lt;link rel="icon" href="/favicon.svg" type="image/svg+xml"&gt;
&lt;link rel="icon" href="/favicon.ico" sizes="any"&gt;
&lt;link rel="apple-touch-icon" href="/app-icon-180.png"&gt;
&lt;link rel="manifest" href="/site.webmanifest"&gt;
&lt;meta name="theme-color" content="#0B2239"&gt;
&lt;meta property="og:image" content="https://clixite.be/og-image-1200x630.png"&gt;</code></pre><button class="btn secondary copy" type="button">Copier</button></div>
  <h3>Le X en code</h3>
  <p>Le logo est généré par un script (Python, fontTools et shapely) : chaque fichier de cette charte sort du même générateur, ce qui garantit que le X est identique partout, au pixel. Le dépôt <code>clixite/clixite-brand</code> sur GitHub contient les sources, ce site et les modèles.</p>
  <dl class="kv">
    <dt>Barre du X</dt><dd>1,08 × le fût des capitales Space Grotesk Bold</dd>
    <dt>Dépassement</dt><dd>5 % de la hauteur de capitale, en haut et en bas</dd>
    <dt>Joint central</dt><dd>0,085 × la barre, autour de la pièce Signal</dd>
    <dt>Chant (Relief)</dt><dd>0,30 × la barre, extrudé à 70° sous l'horizontale</dd>
    <dt>Champs (Interférence)</dt><dd>10 traits par barre (6 sous 200 px), trait égal au vide, décalage d'un demi-pas entre les deux champs, angle 8° au repos</dd>
    <dt>Approche du mot</dt><dd>+6 % ; blancs symétriques de 0,035 em entre les I et la silhouette du X</dd>
  </dl>
</section>

<!-- ===================================================== 11 GOUVERNANCE -->
<section class="chapter" id="gouvernance">
  <header><span class="n">11</span><h2>Gouvernance</h2>
  <p class="lede">Une marque tient si une seule personne en répond. Pour Clixite, c'est Nicolas Simon.</p></header>
  <dl class="kv">
    <dt>Version</dt><dd>1.0, publiée le 25 octobre 2026. Les fichiers de cette page sont la référence ; un fichier qui ne vient pas d'ici n'est pas à jour.</dd>
    <dt>Demandes</dt><dd>Un nouveau support, une exception, un co-branding : écrire à <a href="mailto:nicolas@clixite.be">nicolas@clixite.be</a>. Réponse sous deux jours ouvrables.</dd>
    <dt>Dépôt de marque</dt><dd>Conseil du comité : marque verbale CLIXITE dans l'Union européenne (classes 35 et 42), symbole Relief en figuratif couleur, et un dessin ou modèle de l'Union à vues multiples pour les variantes d'angle de l'Interférence, après recherche d'antériorités en classe de Vienne 27.5.</dd>
    <dt>Licences</dt><dd>Polices sous licence OFL. Le logo, les couleurs et les textes de cette charte appartiennent à Clixite SRL.</dd>
    <dt>Historique</dt><dd>2005, agence de communication, premier X. 2015, bascule vers l'architecture de solutions. 2026, cette charte : X maître, peaux Relief et Interférence, descripteur ENTERPRISE &amp; SOLUTION ARCHITECTURE.</dd>
  </dl>
</section>

</main>
</div>

<footer>
  <div class="inner">
    <div><img src="downloads/logo/clixite-relief-empile-inverse-transparent.svg" alt="Clixite" width="60" height="56"><p>Clixite SRL, Avenue Reine Astrid 53, 1300 Wavre, Belgique. BE 0871.430.776.</p><p><a href="https://clixite.be">clixite.be</a> · <a href="mailto:nicolas@clixite.be">nicolas@clixite.be</a></p></div>
    <div class="right">Charte graphique v1.0<br>25 octobre 2026</div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''

lines_t = "".join(f'<rect x="{x}" y="-60" width="3" height="240" fill="#19B3D9"/>' for x in range(-40, 220, 6))
lines_r = "".join(f'<rect x="{x}" y="-60" width="3" height="240" fill="#FF4F8B"/>' for x in range(-37, 220, 6))
reps = {
    "__HERO_X__": hero_x, "__PLAY_X__": play_x, "__NAV_SIDE__": nav_side, "__NAV_MOBILE__": nav_mobile,
    "__LOGO_RELIEF__": inline_logo("clixite-relief-color-transparent"),
    "__SWATCHES_PRIMARY__": "".join(swatch(*s) for s in PRIMARY), "__SWATCHES_SECONDARY__": "".join(swatch(*s) for s in SECONDARY),
    "__CONTRAST__": contrast_rows(), "__FILES_LOGO__": file_rows("logo", FILES_LOGO), "__SIGNATURE__": signature_preview,
    "__CSS_VARS__": html.escape(tokens_css.strip()), "__LINES_T__": lines_t, "__LINES_R__": lines_r,
    "__KIT_SIZE__": size("downloads/clixite-kit-complet.zip"), "__LOGOS_SIZE__": size("downloads/clixite-logos.zip"), "__FAV_SIZE__": size("downloads/clixite-favicons.zip"),
    "__RES_SIZE__": size("downloads/clixite-reseaux.zip"), "__OFF_SIZE__": size("downloads/clixite-office.zip"), "__FONTS_SIZE__": size("downloads/fonts/clixite-polices.zip"),
    "__ANIM_SIZE__": size("downloads/clixite-animation.zip"),
}
for k, v in reps.items(): page = page.replace(k, v)
assert "__" not in re.sub(r'__(?!\w+__)', '', page) or True
leftover = re.findall(r'__[A-Z_]+__', page); assert not leftover, leftover
open(f"{SITE}/index.html", "w").write(page)
open(f"{SITE}/.htaccess", "w").write("""# charte.clixite.be
AddType image/svg+xml .svg
AddType font/woff2 .woff2
AddType application/manifest+json .webmanifest
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/svg+xml "access plus 7 days"
  ExpiresByType image/png "access plus 7 days"
  ExpiresByType font/woff2 "access plus 30 days"
  ExpiresByType text/css "access plus 1 day"
  ExpiresByType application/javascript "access plus 1 day"
</IfModule>
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/json
</IfModule>
<FilesMatch "\\.(zip|pptx|docx|xlsx|mp4|gif|ttf)$">
  Header set Content-Disposition attachment
</FilesMatch>
""")
open(f"{SITE}/robots.txt", "w").write("User-agent: *\nAllow: /\n")
print("site ok:", len(page) // 1024, "Ko")
