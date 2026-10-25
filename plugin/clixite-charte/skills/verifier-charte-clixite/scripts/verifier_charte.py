#!/usr/bin/env python3
"""Vérificateur de charte Clixite.

Contrôle un ou plusieurs fichiers (texte, Markdown, HTML, CSS, .docx, .pptx, .xlsx) ou l'entrée standard,
et affiche un score sur 100 avec les corrections à faire.

Le texte entre accents graves (`code`), barré (~~contre-exemple~~), les adresses web, les courriels,
les codes couleur et le bloc d'en-tête YAML ne sont pas contrôlés comme de la prose.

Usage :
  python verifier_charte.py fichier.md [autre.html ...] [--langue fr|nl|en] [--interne] [--json]
  echo "texte" | python verifier_charte.py - --langue fr

--interne : document interne (le tutoiement n'est pas signalé).
"""
import json, re, sys, zipfile, html as htmlmod

PALETTE = set('''0b2239 f6f5f0 ffffff 19b3d9 0c7893 d6f1f8 ff4f8b d81b60 ffd233 193776 4b5a6b cdd5dd 1f3a5a 122d4a 3fc3e3 000000'''.split())
# Design System 2.0 : teintes dérivées de la palette (fonds, survols, états), générées par ds/build-tokens.mjs
PALETTE |= set('''071827 2a4a6e 095e73 8c99a8 edebe3 ffe3ec fff4cc'''.split())
POLICES_OK = re.compile(r'^(space grotesk fallback|inter fallback|sfmono-regular|space grotesk|inter|fraunces|jetbrains mono|arial|calibri|georgia|system-ui|sans-serif|serif|monospace|ui-monospace|menlo|-apple-system|segoe ui|roboto|helvetica neue|helvetica|courier new|courier|symbol|wingdings|times new roman)$', re.I)
SIGLES = set('''HTVA TVA WCAG RGPD GDPR DORA NIS2 EBA SRL SPRL BCE PMP PRINCE2 SAFE ITIL ADKAR CPO CTO CIO CEO KBC VOS SAAS API HTML JSON SVG PDF URL HTTPS MCP GEO SEO
CMJN CMYK RVB RGB PNG MP4 GIF WEBM IA AI ERP CRM SAP ARIBA S2P P2P KPI SLA RFP RFI RFQ NDA ISO OFL UE EU BE ENTERPRISE SOLUTION ARCHITECTURE CLIXITE CLI ITE X'''.split())
LEXIQUE = [
    (r'\bsynergies?\b', 'Nommer ce qui est relié : « relier les achats, l’IT et la conformité autour d’un seul processus ».'),
    (r'\bdisrupt\w*|\bgame[- ]?changer\b|\br[ée]volution\w*|\bdisruptie\w*', 'Dire ce qui change, avec un chiffre.'),
    (r'\b[ée]cosyst[èe]me\b|\bholistique\b|\bholistic\b', 'Donner le périmètre exact : les outils, les équipes, les processus concernés.'),
    (r'\bbest[- ]in[- ]class\b|\bleader\b|\bn°\s?1\b|\bnum[ée]ro un\b|\bmarktleider\b', 'Pas d’autoproclamation : citer une référence vérifiable (KBC, Proximus, P&V, Tero, Design Plus).'),
    (r'\bexceptionnel\w*|\bincroyable\w*|\bextraordinaire\w*|\bexceptional\b|\bongelooflijk\b', 'Supprimer le superlatif, donner un fait ou un chiffre.'),
    (r'propuls[ée]e? par l.ia\b|powered by ai\b|\bl.ia va tout changer\b|\bai[- ]powered\b|\bai[- ]driven\b', 'L’IA est un levier, pas le produit : dire ce qu’elle fait gagner et où elle ne sert pas.'),
    (r'transformation digitale|digital transformation|digitale transformatie', 'Nommer le livrable : « votre policy achats en production en douze semaines ».'),
    (r'de bout en bout|end[- ]to[- ]end|van a tot z', 'Promesse vague : dire les trois étapes (cadrer, construire, livrer) et le délai.'),
    (r'partenaire de confiance|trusted partner|vertrouwde partner', 'Préférer un fait : « l’architecte qui dessine, puis construit ».'),
    (r"n.h[ée]sitez pas|don.t hesitate|aarzel niet", 'Invitation concrète : « un premier échange de trente minutes suffit pour cadrer votre x ».'),
    (r'\bpassionn[ée]s?\b|\bpassionate\b|\bgepassioneerd\b', 'Clixite livre ; la passion ne se dit pas, elle se voit.'),
    (r'\boptimis(er|ez|ation)\b vos? performances?|\bbooste[rz]?\b|\bboost your\b', 'Donner le résultat chiffré plutôt que le verbe magique.'),
    (r'\bagile\b(?! \(|,? m[ée]thode| framework|pm\b)', 'Agile en adjectif creux : dire ce qui est itératif et à quel rythme.'),
]
EMOJI = re.compile('[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U0001F900-\U0001F9FF]')
MAX_PAR_REGLE = 8


def texte_office(chemin):
    """Extrait le texte d'un .docx, .pptx, .xlsx (et de leurs modèles)."""
    z = zipfile.ZipFile(chemin)
    parties = [n for n in z.namelist() if re.match(r'word/(document|header\d*|footer\d*)\.xml$|ppt/slides/slide\d+\.xml$|xl/sharedStrings\.xml$', n)]
    morceaux = []
    for n in sorted(parties):
        x = z.read(n).decode('utf8', 'ignore')
        x = re.sub(r'</w:p>|</a:p>|</si>', '\n', x)
        morceaux.append(htmlmod.unescape(re.sub(r'<[^>]+>', '', x)))
    polices = set()
    for n in z.namelist():
        if n.endswith('.xml') and 'theme' not in n and ('styles' in n or 'slide' in n or 'document' in n or 'header' in n or 'footer' in n):
            x = z.read(n).decode('utf8', 'ignore')
            polices |= set(re.findall(r'typeface="([^"]+)"', x)) | set(re.findall(r'w:ascii="([^"]+)"', x))
    return '\n'.join(morceaux), polices


def nettoyer(texte):
    """Retire ce qui n'est pas de la prose : code, contre-exemples, URL, courriels, couleurs, en-tête YAML."""
    t = re.sub(r'^---\n[\s\S]*?\n---\n', '', texte)
    t = re.sub(r'```[\s\S]*?```', ' ', t)
    t = re.sub(r'`[^`\n]*`', ' ', t)
    t = re.sub(r'~~[^~\n]*~~', ' ', t)
    t = re.sub(r'https?://\S+|www\.\S+|\S+@\S+\.\S+', ' ', t)
    t = re.sub(r'#[0-9a-fA-F]{3,8}\b', ' ', t)
    return t


def controler(brut, nom, langue='fr', interne=False):
    pts = []
    def add(niveau, regle, msg, extraits):
        if extraits:
            pts.append({'niveau': niveau, 'regle': regle, 'message': msg, 'extraits': extraits[:MAX_PAR_REGLE], 'nombre': len(extraits)})
    est_html = bool(re.search(r'<(html|body|div|p|h[1-6]|section)\b', brut, re.I))
    est_css = ('{' in brut and ':' in brut and not est_html and bool(re.search(r'[a-z-]+\s*:\s*[^;]+;', brut)))
    polices_office = set()
    if nom.lower().endswith(('.docx', '.dotx', '.pptx', '.potx', '.xlsx', '.xltx')):
        brut, polices_office = texte_office(nom)
    prose = brut
    if est_html:
        prose = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', brut, flags=re.I)
        prose = htmlmod.unescape(re.sub(r'<[^>]+>', ' ', prose))
    if est_css:
        prose = ''
    prose = nettoyer(prose)
    lignes = [l for l in prose.split('\n')]

    # ---- bloquants
    add('bloquant', 'tiret-long', 'Tiret long ou demi-cadratin : remplacer par une virgule, un point ou deux points.', re.findall(r'[^\n]{0,30}[—–][^\n]{0,30}', prose))
    add('bloquant', 'double-tiret', 'Double tiret ou double souligné : interdits dans un texte Clixite.', re.findall(r'[^\n]{0,30}(?:--(?![a-zA-Z])|__)[^\n]{0,30}', prose))
    add('bloquant', 'emoji', 'Émoji : aucun dans un support de marque.', [m.group(0) for m in EMOJI.finditer(prose)])
    add('bloquant', 'descripteur', 'Le descripteur reste en anglais : ENTERPRISE & SOLUTION ARCHITECTURE.', re.findall(r'[^\n]{0,20}(?:ARCHITECTURE D.ENTREPRISE (?:&|ET) DE SOLUTIONS?|ENTERPRISE (?:&|AND) SOLUTIONS? ARCHITECTE)[^\n]{0,20}', prose))  # 2.0 : seul le descripteur en capitales est visé, le nom du métier en français reste permis

    # ---- à corriger
    for motif, conseil in LEXIQUE:
        add('corriger', 'lexique', conseil, re.findall(r'[^\n]{0,25}(?:' + motif + r')[^\n]{0,25}', prose, re.I))
    add('corriger', 'exclamation', 'Point d’exclamation : la marque n’en utilise pas.', re.findall(r'[^\n]{0,30}![^\n]{0,10}', prose))
    add('corriger', 'milliers', 'Nombre sans séparateur de milliers (espace insécable) : 1 500, 12 000.', re.findall(r'(?<![\d.,])\d{5,}(?![\d.,:])', prose))
    add('corriger', 'euro-avant', 'Le symbole € se place après le montant : 1 200 €.', re.findall(r'€\s?\d', prose))
    add('corriger', 'unite-collee', 'Séparer le nombre et l’unité : 12 semaines, 800 M€, 4,5:1.', re.findall(r'\b\d+(?:€|M€|k€|j\b|h\b|sem\b)', prose))
    if not interne and langue == 'fr':
        add('corriger', 'tutoiement', 'Vouvoiement en externe.', re.findall(r'[^\n]{0,20}\b(?:tu|te|toi|ton|ta|tes)\b[^\n]{0,20}', prose))
    titres = [l.strip() for l in lignes if l.strip() and len(l.strip()) < 90 and l.strip().isupper() and len(re.findall(r'[A-ZÀ-Ý]{3,}', l)) >= 2 and not set(re.findall(r'[A-ZÀ-Ý0-9]+', l.strip())) <= SIGLES]
    add('corriger', 'capitales', 'Titre en capitales : casse de phrase (capitales réservées aux étiquettes, sigles et descripteur).', titres)
    if est_html or est_css or nom.lower().endswith(('.css', '.html', '.htm', '.svg')):
        couleurs = set(c.lower() for c in re.findall(r'#([0-9a-fA-F]{6})\b', brut))
        add('corriger', 'couleur', 'Couleur hors palette Clixite.', sorted('#' + c for c in couleurs if c not in PALETTE))
        familles = set()
        for fam in re.findall(r'font-family\s*:\s*([^;}]+)', brut, re.I):
            for f in fam.split(','):
                f = f.strip().strip('\'"').strip()
                if f and not f.startswith('var(') and not POLICES_OK.match(f): familles.add(f)
        add('corriger', 'police', 'Police hors charte (Space Grotesk, Inter, Fraunces, JetBrains Mono).', sorted(familles))
        # seule exception : le voile de lisibilité sur photo ou vidéo, Encre vers Encre transparente (DESIGN.md)
        def voile_encre(g):
            cols = re.findall(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\btransparent\b', g)
            ok = lambda c: c.lower() in ('transparent', '#0000', '#00000000') or c.lower().startswith('#0b2239') or re.match(r'rgba?\(\s*11[\s,]+34[\s,]+57\b', c)
            return bool(cols) and all(ok(c) for c in cols)
        degrades = [g[:40] for g in re.findall(r'[a-z-]*gradient\((?:[^()]|\([^()]*\))*\)', brut) if not voile_encre(g)]
        add('corriger', 'degrade', 'Dégradé : interdit (fond uni, Encre ou Papier ; seul le voile Encre sur image est admis).', degrades)
        add('corriger', 'ombre', 'Ombre portée : aucune ombre au repos.', re.findall(r'(?:box|text)-shadow\s*:\s*[^;]{0,40}', brut))
        add('corriger', 'bordure-gauche', 'Bordure colorée à gauche : interdite sur les cartes et encadrés.', [m for m in re.findall(r'border-left\s*:\s*[^;]{0,40}', brut) if not re.search(r'\b(0|1px)\b', m)])
        add('corriger', 'rebond', 'Easing élastique ou rebond : une seule courbe, cubic-bezier(.2, .8, .2, 1).', re.findall(r'cubic-bezier\(\s*[^)]*(?:-\d|1\.\d{2,}|2\.)[^)]*\)|ease-in-out-back|bounce|elastic', brut))
    if polices_office:
        add('corriger', 'police', 'Police hors charte dans le document Office.', sorted(f for f in polices_office if not POLICES_OK.match(f) and not f.startswith('+') and 'Symbol' not in f and 'Wingdings' not in f and 'Times' not in f))

    # ---- conseils
    if langue == 'fr':
        add('conseil', 'typo-fr', 'Typographie française : espace insécable avant ; : ? et guillemets « ».', re.findall(r'\w[;?]|\w:\s(?=[A-Za-zÀ-ÿ])|"[^"\n]{3,80}"', prose)[:MAX_PAR_REGLE])
    add('conseil', 'hashtags', 'Trois hashtags au plus, à la fin.', ['#' * 1 + str(len(re.findall(r'(?<!\w)#\w+', prose))) + ' hashtags'] if len(re.findall(r'(?<!\w)#\w+', prose)) > 3 else [])
    longues = [l[:60] + '…' for l in lignes if len(l) > 0 and not est_html and len(re.findall(r'\w+', l)) > 0 and max((len(s.split()) for s in re.split(r'[.!?]\s', l)), default=0) > 35]
    add('conseil', 'phrase-longue', 'Phrase de plus de 35 mots : couper. Une idée par phrase.', longues)
    add('conseil', 'unique', '« Unique » est souvent un superlatif déguisé : préférer « un seul », ou un fait.', re.findall(r'[^\n]{0,25}\bunique\b[^\n]{0,25}', prose, re.I))
    add('conseil', 'ia-majuscule', 'Écrire « IA » en capitales (sigle), « intelligence artificielle » en toutes lettres sinon.', re.findall(r'\b[Ii]a\b(?= [a-zé])', prose))

    score = 100 - sum({'bloquant': 10, 'corriger': 4, 'conseil': 1}[p['niveau']] * min(p['nombre'], 3) for p in pts)
    return {'fichier': nom, 'score': max(0, score), 'points': pts}


def afficher(res):
    print(f"\n{res['fichier']} : score {res['score']}/100")
    for niveau, libelle in (('bloquant', 'BLOQUANT'), ('corriger', 'À CORRIGER'), ('conseil', 'CONSEIL')):
        for p in [p for p in res['points'] if p['niveau'] == niveau]:
            print(f"  [{libelle}] {p['regle']} ({p['nombre']}) : {p['message']}")
            for e in p['extraits']:
                print(f"      · {str(e).strip()[:100]}")
    if not res['points']:
        print("  aucun point : conforme à la charte Clixite (contrôle visuel encore à faire).")
    elif not any(p['niveau'] in ('bloquant', 'corriger') for p in res['points']):
        print("  aucun point bloquant ni à corriger.")


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    langue = 'fr'; interne = '--interne' in sys.argv; as_json = '--json' in sys.argv
    if '--langue' in sys.argv:
        langue = sys.argv[sys.argv.index('--langue') + 1]; args = [a for a in args if a != langue]
    if not args:
        sys.exit(__doc__)
    resultats = []
    for a in args:
        if a == '-':
            resultats.append(controler(sys.stdin.read(), 'entrée standard', langue, interne))
        elif a.lower().endswith(('.docx', '.dotx', '.pptx', '.potx', '.xlsx', '.xltx')):
            resultats.append(controler('', a, langue, interne))
        else:
            resultats.append(controler(open(a, encoding='utf8', errors='ignore').read(), a, langue, interne))
    if as_json:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
    else:
        for r in resultats: afficher(r)
    sys.exit(0 if all(not any(p['niveau'] in ('bloquant', 'corriger') for p in r['points']) for r in resultats) else 1)
