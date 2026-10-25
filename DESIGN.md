---
name: Clixite
description: Marque d'un cabinet d'architecture de solutions et d'entreprise. Encre et Papier comme socle, un trio turquoise bleu, rose et Signal qui ne vit que dans le X et les moments de signature. Précis, direct, calme, belge.
version: 1.0 (25 octobre 2026)
source_of_truth: https://charte.clixite.be/ et charte/downloads/clixite-tokens.json

colors:
  # Socle
  encre: "#0B2239"            # fond des couvertures, slides de titre, écran ; texte sur fond clair
  papier: "#F6F5F0"           # fond de page par défaut, chaud, jamais blanc clinique
  blanc: "#FFFFFF"            # panneaux et spécimens posés sur Papier
  # Signature (jamais de texte dessus sur fond clair, sauf les versions « texte »)
  turquoise: "#19B3D9"        # la marque : symbole, boutons principaux (texte Encre dessus), surfaces
  turquoise-texte: "#0C7893"  # liens, descripteurs, chiffres clés sur fond clair (4,7:1 sur Papier)
  turquoise-doux: "#D6F1F8"   # fonds de badge, sélection de texte
  rose: "#FF4F8B"             # seconde barre du X, pastilles, surlignages ; jamais en texte
  rose-texte: "#D81B60"       # accent texte sur fond clair (4,5:1 sur Papier)
  signal: "#FFD233"           # pièce centrale du X, lentille, un repère par support ; ne porte jamais de texte
  indigo: "#193776"           # turquoise multiplié par rose : le chevauchement en data viz et en motion
  # Neutres (toujours teintés d'Encre, jamais de gris pur)
  ardoise: "#4B5A6B"          # texte secondaire, légendes, icônes
  brume: "#CDD5DD"            # filets, bordures, en-têtes de tableau ; texte secondaire sur Encre
  encre-teintee: "#1F3A5A"    # chant du X sur fond Encre, surfaces relevées du thème sombre
  surface-sombre: "#122D4A"   # cartes et champs du thème sombre
  # États (toujours accompagnés d'un libellé ou d'une icône, jamais seulement par la teinte)
  succes: "#0C7893"
  danger: "#D81B60"

typography:
  display: "Space Grotesk"    # titres, mot-marque, chiffres clés ; graisses 500 à 700
  sans: "Inter"               # texte courant, interfaces, mails, Office ; graisses 400 à 600, jamais plus
  editorial: "Fraunces"       # italique uniquement, graisses 500 et 600 : citations, chiffres clés, le x variable
  mono: "JetBrains Mono"      # données, références, identifiants, mesures ; graisse 500
  scale:
    display-1: { size: 56, weight: 700, line: 1.0, tracking: -0.02em, family: display }
    h1: { size: 40, weight: 600, line: 1.05, tracking: -0.015em, family: display }
    h2: { size: 28, weight: 600, line: 1.15, family: display }
    h3: { size: 20, weight: 600, line: 1.25, family: display }
    quote: { size: 26, weight: 500, line: 1.3, family: editorial, style: italic }
    body: { size: 16, weight: 400, line: 1.5, family: sans }
    small: { size: 13, weight: 400, line: 1.45, family: sans }
    label: { size: 12, weight: 500, tracking: 0.08em, transform: uppercase, family: mono }
    data: { size: 14, weight: 500, family: mono, numerals: tabular }
  measure: "45 à 66 caractères pour le texte courant"
  loading: "auto-hébergées (woff2, font-display swap) ou Google Fonts ; licence OFL"

spacing:
  base: 8
  page-margin: { desktop: 64, mobile: 16 }
  card-padding: 24
  section-gap: 88

radius:
  sm: 6
  md: 10
  pill: 999

motion:
  ease-out: "cubic-bezier(.2, .8, .2, 1)"   # la courbe unique de la marque ; jamais de rebond ni d'élastique
  element: 450ms
  block: 600ms
  press: "160ms, transform scale(.97)"
  opening: "3,5 s, une seule séquence orchestrée par page ou par vidéo (moteur WebGL charte/assets/ouverture3d.js)"
  reduced-motion: "le logo s'affiche directement au repos ; les fondus restent, les déplacements disparaissent"
---

# Clixite

Clixite est le cabinet d'architecture de solutions de Nicolas Simon (Wavre, depuis 2005). Il relie la stratégie, les systèmes et la conformité pour des grands comptes régulés (banque, assurance, télécom) et pour des PME en croissance, puis livre. La marque doit ressembler à ce métier : un plan d'architecte, pas une plaquette. Lire ce fichier avant de produire un support Clixite, qu'il soit imprimé, à l'écran ou en mouvement. La référence complète, avec tous les fichiers, est sur https://charte.clixite.be/.

## 1. Étoile polaire

**L'architecte qui relie la stratégie, les systèmes et la conformité. Nous résolvons votre *x*.**

Le *x* est l'inconnue du client. Il vit dans les textes, en italique Fraunces, et nulle part ailleurs : le logo porte seulement le X. Personnalité : l'Architecte, sage et créateur. Précis, direct, exigeant, calme, humain, avec un brin d'humour belge. Chiffres et faits avant adjectifs.

Ce que la marque doit évoquer : la structure (une grille, des filets de mesure, un relief net), la clarté (Papier chaud, beaucoup d'air, une seule idée par écran), et un seul moment de signature par support où le trio turquoise, rose et Signal apparaît.

## 2. Logo

Le mot-marque s'écrit **CLI X ITE** en capitales Space Grotesk Bold, approche +6 %, avec le X comme symbole central. Descripteur sous le mot, toujours en anglais : **ENTERPRISE & SOLUTION ARCHITECTURE**, Space Grotesk Medium, capitales espacées, calé sur la largeur du mot.

- **X maître** : deux barres au poids des capitales (1,08 fût), turquoise par-dessus rose, pièce centrale Signal détachée par un joint fin, dépassement de 5 % au-dessus et au-dessous des capitales.
- **Peau Relief** (marque de référence, impression, dépôt) : X extrudé de 0,30 barre à 70°, chant Encre.
- **Peau Interférence** (écran, grands formats, mouvement) : deux champs de lignes turquoise et rose à 8° l'un de l'autre, lentille Signal au croisement, chant Encre.
- **Niveaux** : Interférence à 200 px et plus ; Interférence simplifiée (6 traits) ou Relief de 48 à 200 px ; X maître plat sous 48 px ; X plein Encre sous 24 px (favicon).
- **Zone de protection** : la hauteur du X sur les quatre côtés. Taille minimale du mot-marque : 96 px à l'écran, 24 mm imprimé.
- Sur Papier ou blanc : version couleur. Sur Encre : version inversée. Sur photo ou fond coloré : monochrome Encre ou Papier.
- Ne jamais : étirer, inverser l'ordre des couleurs, poser le logo sur du turquoise, du rose ou du Signal, ajouter une ombre ou un contour, incliner, réécrire le descripteur dans une autre police, intégrer un descripteur d'offre au fichier du logo.

Fichiers : `charte/downloads/logo/` (les « transparent » sont ceux à utiliser dans un document). Le logo est généré par `logos10.py` ; ne jamais le redessiner à la main.

## 3. Couleurs

L'Encre domine (45 %), le Papier respire (25 %), le turquoise signe (15 %), le rose et le Signal ponctuent (8 % et 7 %). Dans le corps d'un document, un seul accent à la fois, turquoise par défaut.

- Texte sur fond clair : Encre ou Ardoise ; accents en turquoise-texte ou rose-texte. Jamais de turquoise, rose ou Signal pur en texte sur fond clair.
- Sur Encre : Papier pour le texte, Brume pour le secondaire (jamais de gris neutre), turquoise et Signal comme accents (6,5:1 et 11,1:1).
- Le Signal ne porte jamais de texte. Un seul losange Signal par support.
- Deux séries qui se chevauchent prennent l'Indigo. Jamais de vert et rouge seuls pour distinguer deux états.
- Contrastes vérifiés AA : Encre sur Papier 14,8:1 ; turquoise-texte sur Papier 4,7:1 ; rose-texte sur Papier 4,5:1 ; Ardoise sur Papier 6,5:1.

## 4. Typographie

Quatre familles, chacune avec un rôle et jamais en concurrence. Space Grotesk porte le caractère (titres, mot-marque), Inter fait le travail (texte, interfaces, Office), Fraunces Italic apporte la voix (citations, chiffres clés, le *x*), JetBrains Mono tient les chiffres (données, références, mesures, étiquettes). Le mono n'est jamais un costume « technique » : il sert aux données, au code et aux mesures.

- Corps 16 px minimum à l'écran, interligne 1,5, 45 à 66 caractères par ligne. Titres avec `text-wrap: balance`, paragraphes avec `text-wrap: pretty`.
- Texte clair sur Encre : un peu plus d'interligne (1,55 à 1,6) et d'approche (+0,5 %).
- Chiffres tabulaires (`font-variant-numeric: tabular-nums`) dans les tableaux et les données.
- Pas d'étiquette en capitales au-dessus d'un titre ; le titre se suffit. Les numéros de chapitre s'écrivent dans le titre, en mono, pas au-dessus.
- Dans Office : Space Grotesk et Inter installées depuis `charte/downloads/fonts/`. Sans elles, Arial et Calibri sont tolérées pour un document de travail, pas pour une offre.

## 5. Mise en page, surfaces et composants

- Grille de 8 px. Marges de page 64 px sur grand écran, 16 px sur mobile.
- Fond Papier pour le contenu ; Encre pour les couvertures, héros, slides de titre, pieds de page.
- Panneaux : blanc, bordure 1 px Brume, rayon 10 px, padding 24 px. Pas d'ombre portée, pas de bordure colorée à gauche, pas de carte dans une carte, pas de page faite de cartes identiques « icône, titre, texte ».
- Boutons : principal fond turquoise et texte Encre ; secondaire bordure Brume et texte Encre ; lien en turquoise-texte. Hauteur 44 px minimum, forme pilule, retour de pression `scale(.97)` en 160 ms.
- Tableaux : en-tête Papier, chiffres mono alignés à droite, filets Brume.
- Icônes : trait 1,75 px, coins arrondis, 24 px, en Encre ou Ardoise, dessinées en SVG. Pas d'émoji dans les supports de marque.
- Surfaces du navigateur : sélection en turquoise-doux (Encre teintée sur fond sombre), curseur en turquoise-texte, barre de défilement Brume sur Papier, soulignement des liens décalé de 3 px.
- Trois motifs sortent du logo et suffisent : la lentille (un losange Signal, un seul par support), les champs (deux champs de lignes à 8°, en fond de couverture ou en masque, jamais sous du texte courant), le chant (extrusion à 70° en Encre, une seule épaisseur de 0,30).
- Photos : lieux et gens réels, lumière naturelle, légère dominante froide. Jamais de banque d'images « poignée de main ».

## 6. Mouvement

Une seule courbe, `cubic-bezier(.2, .8, .2, 1)`, un fort ease-out. Rien ne rebondit, rien n'élastique. Durées : 450 ms pour un élément, 600 ms pour un bloc, 3 s pour l'ouverture complète ; les interactions courantes restent sous 300 ms. Une seule séquence orchestrée par page ou par vidéo ; pas d'apparition en fondu section par section, pas d'animation sur ce qui se répète. Le X ne tourne jamais sur lui-même : seul l'angle entre les champs change (8° au repos, respiration entre 4° et 6° après l'ouverture, qui le résout de 14° vers 4°). À l'écran, le mot-marque entier en relief peut suivre le curseur de quelques degrés (7° au plus), jamais le X seul. Animer uniquement `transform` et `opacity`. Interactions au curseur interpolées avec inertie, jamais liées directement à la position. `prefers-reduced-motion` : le logo s'affiche au repos, les fondus restent, les déplacements disparaissent.

L'ouverture de référence : `charte/animation/clixite-ouverture.html`, rendue en 3D depuis la géométrie exacte du logo (0 à 0,9 s les champs arrivent, 0,7 à 2 s l'angle se résout et la lentille s'allume, 2 à 2,6 s le chant tombe sous un balayage de lumière, 2,3 à 3,2 s recul de la caméra et les lettres se posent, 3,15 à 3,65 s le descripteur).

## 7. Voix

Phrases courtes, verbes d'action, chiffres avant adjectifs. Vouvoiement en externe. Français de Belgique, anglais et néerlandais écrits dans la langue du lecteur, jamais traduits mot à mot. Jamais de buzzwords, de hype IA ou de promesse vague. Pas de tirets longs : une virgule, un point ou deux points font le travail. Une note d'humour sec quand elle détend sans décrédibiliser. Les contrôles nomment leur action (« Télécharger le kit », pas « Soumettre ») ; une erreur nomme le problème et la sortie.

## 8. À faire et à ne pas faire

### À faire

- Un seul moment de signature par support, où le trio turquoise, rose et Signal apparaît ensemble ; partout ailleurs, Encre, Papier et un accent.
- Prendre les fichiers du logo dans `charte/downloads/`, jamais une copie recolorée.
- Vérifier le contraste de chaque paire texte et fond (AA minimum) et l'état clavier de chaque contrôle.
- Laisser de l'air : plus d'espace au-dessus d'un titre qu'en dessous, groupes serrés, séparations généreuses.
- Mettre le X vivant (Interférence) seulement là où il a la place de vivre : hero, couverture, bannière, animation.

### À ne pas faire

- Pas de dégradés, pas de texte en dégradé, pas de verre dépoli, pas de lueur « outil IA », pas de violet.
- Pas de gris neutre ni de noir pur : les neutres sont teintés d'Encre.
- Pas de tuile d'icône arrondie au-dessus de chaque titre, pas d'étiquette-chapeau, pas de flèche « → » collée aux liens.
- Pas de mono partout pour « faire technique ».
- Pas de rebond, pas d'élastique, pas d'animation d'entrée sur chaque section.
- Pas de slogan dans le logo ; « nous résolvons votre *x* » reste dans le texte.

## 9. Design System 2.0 (refonte 2030)

Le site www.clixite.be est construit sur le Design System 2.0 (`ds/`, documentation dans `ds/README.md`) : tokens au format W3C, contrastes contrôlés à chaque build, composants Astro dans `web/`. Quatre ajouts à la charte, décidés pour l'écran :

- **Mot-marque sans descripteur** : sous 240 px de large (en-têtes d'interface, barres de navigation), utiliser `clixite-maitre-motmarque-*`, généré par `logos10.lockup_wordmark`. Au-dessus, le descripteur reste obligatoire.
- **Ouverture web en 2,4 s** : sur un site, le X se construit en 2,4 s (repères, tracé, chant, champs, lentille), puis seul l'angle entre les champs respire entre 4° et 6°. Exception documentée à la règle « transform et opacité » : le tracé des repères (`stroke-dashoffset`), pendant l'ouverture uniquement. Sur écran tactile, pas de boucle.
- **Film en fond de hero** (www.clixite.be, depuis octobre 2026) : la boucle du film de lancement, plein cadre, sans titres ni logo (le logo est déjà dans l'en-tête), remplace le X construit dans le hero de l'accueil. Le texte se pose sur une plaque Encre à 92 % (rayon 10 px, filet turquoise de 44 × 4 px, comme les titres du film) ; aucun voile ni dégradé sur l'image. Les quatre phrases du film défilent au-dessus de la promesse, au rythme des plans. Boucle de 11,5 s sans coupure visible, chargée après l'affichage, jamais en mouvement réduit ni en économie de données, avec un bouton Pause visible (WCAG 2.2.2). Le X construit reste la règle pour les autres pages, couvertures et bannières.
- **Le *x* en deux endroits par page** au plus : le titre d'ouverture et l'appel final.
- **Un site par acheteur** : l'accueil s'adapte au visiteur (grand groupe, PME, cabinet ou intermédiaire). Le sous-titre, l'appel à l'action, les offres, les conditions, les preuves, l'ordre des logos et les compétences mises en avant suivent ce choix. Là où le X construit est affiché, l'angle entre ses champs suit aussi l'acheteur : 4° pour les groupes régulés, 6° pour les cabinets, 7,5° pour les PME (valeurs de `web/src/data/audiences.ts`).
- **Logos clients** : fichiers officiels uniquement, inscrits au registre `web/src/data/clients.registry.json` avec leur source, teintés par masque CSS, jamais redessinés. La publication est décidée par Nicolas Simon et tracée dans le registre ; l'accord écrit du client est archivé dès qu'il est obtenu.
