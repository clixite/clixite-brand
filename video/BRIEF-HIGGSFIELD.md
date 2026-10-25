# Teaser de lancement Clixite : brief pour ChatGPT + Higgsfield

Ce brief se colle tel quel dans ChatGPT (connecteur Higgsfield actif). ChatGPT génère les plans de coupe ; l'assemblage final (titres, étalonnage, plan de fin avec le vrai logo animé) se fait ensuite chez Claude, pour que la marque reste exacte.

## Pourquoi ce partage des rôles

- Un modèle vidéo ne sait pas reproduire un logo au millimètre : il déforme le X, invente des lettres, change les couleurs. Le logo n'apparaît donc **jamais** dans les plans générés. Le plan de fin utilise l'animation officielle `clixite-ouverture-1080p.mp4` (rendue depuis la géométrie exacte).
- Les textes générés dans une vidéo IA sont souvent illisibles ou faux. Tous les textes sont posés au montage, en Space Grotesk.
- Pas de visages : pas de faux clients, pas de « consultant souriant » de banque d'images, pas de risque d'uncanny valley.

## Le film

- **Usage** : annonce LinkedIn du nouveau site, puis en-tête de la page d'accueil de LinkedIn entreprise.
- **Durée** : 15 secondes. Quatre plans de 3 à 4 s, puis 3 s de plan de fin.
- **Formats livrés** : 4:5 (1080 × 1350) pour le fil LinkedIn, 16:9 (1920 × 1080), 9:16 (1080 × 1920).
- **Ton** : très corporate, calme, précis. Le « wow » vient de la transformation de la matière (un trait de plan devient une architecture qui tourne), pas d'effets.
- **Palette** : nuit bleu encre (#0B2239), papier chaud (#F6F5F0), une lumière turquoise (#19B3D9). Rose et jaune réservés au plan de fin (le logo).
- **Interdits** : violet, lueurs néon, cerveau numérique, réseau de points reliés, poignée de main, globe terrestre, code qui défile, robots, texte à l'écran, visages.

## Message à coller dans ChatGPT

> Tu vas générer avec Higgsfield quatre plans vidéo pour un teaser corporate de 15 secondes. Pour chaque plan : format 16:9 en 1080p (je recadrerai en 4:5 et 9:16, garde le sujet au centre), 4 secondes, mouvement de caméra lent et continu, aucun texte, aucun logo, aucun visage. Style : photographie d'architecture contemporaine, lumière naturelle froide, grain fin, profondeur de champ réduite, étalonnage sobre bleu nuit et papier chaud, une seule lumière d'accent turquoise. Génère deux variantes par plan et donne-moi les liens de téléchargement des MP4.
>
> **Plan 1, la table à dessin (0 à 4 s).** Prompt : *"Macro shot of an architect's drafting table at night, warm off-white paper with precise thin construction lines, a single cool desk lamp, ink-blue darkness around, slow dolly-in across the paper, the graphite lines catch a faint turquoise reflection, photorealistic, architectural photography, shallow depth of field, no text, no logo, no people."* Caméra : dolly in lent.
>
> **Plan 2, le plan prend du relief (4 à 8 s).** Prompt : *"The thin construction lines on the paper slowly lift off the sheet and become a precise three-dimensional architectural framework of light, clean orthogonal structure, like a building's steel frame made of thin turquoise light, deep ink-blue background, elegant, restrained, slow crane up, photorealistic render, no text, no glowing neon, no particles, no people."* Caméra : crane up.
>
> **Plan 3, l'architecture se pose dans le réel (8 à 12 s).** Prompt : *"Seamless transition: the light framework settles into a real contemporary European office at early morning, large windows, concrete and oak, a quiet open space with screens showing abstract charts, soft daylight, one subtle turquoise accent light, slow lateral tracking shot, photorealistic, architectural photography, no readable text, no faces, people only as soft out-of-focus silhouettes in the distance."* Caméra : travelling latéral.
>
> **Plan 4, ça tourne (12 à 15 s).** Prompt : *"Close-up of a minimalist server rack and network patch panel in a clean data room, status lights pulse calmly in turquoise, cool ink-blue ambience, very slow push-in, crisp details, photorealistic, no text, no logo, no people."* Caméra : push-in très lent.
>
> Prompt négatif pour tous les plans : *"text, letters, logo, watermark, faces, hands, purple, neon glow, lens flare, particles, globe, brain, robot, handshake, stock photo look, cartoon, oversaturated."*

## Montage (fait par Claude à réception des MP4)

1. Sélection de la meilleure variante par plan, étalonnage commun sur la palette Clixite.
2. Titres en Space Grotesk Bold, un par plan, en bas à gauche, apparition par fondu de 450 ms :
   - plan 1 : « Votre architecture commence sur papier. »
   - plan 2 : « Elle prend du relief. »
   - plan 3 : « Elle se pose chez vous. »
   - plan 4 : « Et elle tourne. »
3. Plan de fin (3 s) : animation officielle du logo, puis « Nous résolvons votre *x*. » et « clixite.be ».
4. Son : nappe minimale (piano et pulsation lente), libre de droits, sous-titres intégrés (LinkedIn se lit sans le son).
5. Exports 4:5, 16:9 et 9:16, H.264, moins de 8 Mo pour LinkedIn.

## À fournir par Nicolas

- Les MP4 téléchargés depuis ChatGPT (dans N:\dev ou en pièce jointe).
- Le choix de la musique, ou carte blanche.
