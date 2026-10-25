---
name: charte-clixite
description: "Applique la charte graphique officielle de Clixite (architecture de solutions et d'entreprise, Wavre) à toute production : présentation PowerPoint, document Word, offre, lettre, tableau Excel, page web, artefact HTML, post LinkedIn, visuel, graphique, signature de courriel, animation. À utiliser dès que l'utilisateur mentionne Clixite, clixite.be, « ma charte », « aux couleurs de Clixite », « le modèle Clixite », « by Clixite », ou demande un livrable pour Clixite, Vidango ou CyGap."
metadata:
  version: "1.0.0"
  source: https://charte.clixite.be/
---

# Appliquer la charte Clixite

Produire chaque livrable Clixite en suivant la charte. Le référentiel complet est `references/regles.md` ; `references/DESIGN.md` en est la version pour agents (jetons en en-tête YAML). Lire `regles.md` avant toute production non triviale. En cas de doute, choisir l'option la plus sobre : Encre, Papier, un accent.

## Règles non négociables

1. **Logo intact.** Utiliser uniquement les fichiers de `references/logos/` : `clixite-relief-color-transparent.svg` sur fond clair, `clixite-relief-inverse-transparent.svg` sur Encre, `clixite-relief-mono-transparent.svg` sur photo ou fond coloré ; `x-relief-*.svg` pour le symbole seul ; `x-maitre-color-transparent.svg` sous 48 px ; `x-favicon-encre-transparent.svg` sous 24 px. Ne jamais le redessiner, le recolorer, l'étirer, l'incliner, l'ombrer, lui ajouter un contour ni le poser sur du turquoise, du rose ou du Signal. Zone de protection : la hauteur du X sur les quatre côtés. Le descripteur reste ENTERPRISE & SOLUTION ARCHITECTURE, en anglais.
2. **Couleurs.** Encre #0B2239 et Papier #F6F5F0 comme socle. Turquoise #19B3D9 pour la marque (symbole, bouton principal avec texte Encre, surfaces), rose #FF4F8B et Signal #FFD233 en ponctuation seulement. Pour du texte sur fond clair : turquoise texte #0C7893 ou rose texte #D81B60, jamais les teintes pures. Le Signal ne porte jamais de texte. Neutres teintés : Ardoise #4B5A6B, Brume #CDD5DD, Encre teintée #1F3A5A ; jamais de gris ni de noir pur. Le trio turquoise, rose, Signal n'apparaît ensemble que dans le X et dans un seul moment de signature par support.
3. **Polices.** Space Grotesk 500 à 700 pour les titres, Inter 400 à 600 pour le texte, Fraunces Italic pour les citations et le *x* variable, JetBrains Mono pour les données, mesures et étiquettes. Pas de mono pour du texte courant, pas d'étiquette en capitales au-dessus d'un titre.
4. **Formes.** Grille de 8 px, panneaux blancs à bordure 1 px Brume et rayon 10 px, boutons pilule de 44 px, filets Brume. Aucun dégradé, aucune ombre portée, aucune bordure colorée à gauche, aucune carte dans une carte, aucun émoji.
5. **Voix.** Vouvoiement en externe, phrases courtes, chiffres avant adjectifs, français de Belgique. Jamais de tiret long ni de double tiret, jamais de buzzword, de hype IA ni de promesse vague.
6. **Mouvement.** Une courbe `cubic-bezier(.2, .8, .2, 1)`, 450 ms par élément, 600 ms par bloc, une seule séquence orchestrée par page. Rien ne rebondit. Le X ne tourne jamais sur lui-même.
7. **Faits.** Ne jamais inventer un chiffre, une référence client, une date ou une citation. Preuves établies dans `regles.md` (section marque) ; tout le reste est un champ à compléter, signalé à l'utilisateur.

## Dispositifs signature

Trois motifs, un à la fois, en grand : la **lentille** (un losange Signal, un seul par support, sur un chiffre clé ou un repère), les **champs** (deux champs de lignes turquoise et rose à 8°, en fond de couverture ou en masque, jamais sous du texte), le **chant** (l'extrusion à 70° en Encre, une seule épaisseur). Le récit « nous résolvons votre *x* » vit dans les textes, avec le *x* en Fraunces italique, jamais dans le logo.

## Méthode par type de livrable

### Présentation PowerPoint
- Partir de `references/modeles/Clixite-Presentation-2026.potx` (16:9). Avec python-pptx : copier le fichier sous un nom `.pptx`, remplacer dans `[Content_Types].xml` le type `presentationml.template.main+xml` par `presentationml.presentation.main+xml`, puis utiliser les dispositions par nom. Avec pptxgenjs : reprendre `build_pptx.js` du dépôt `clixite/clixite-brand` (thème et 9 dispositions).
- Dispositions, espaces réservés et couleurs de thème : `references/dispositions-office.md`. Une idée par slide, Encre pour l'ouverture, les intercalaires et la clôture, Papier pour le contenu, chiffres clés en Space Grotesk 54, graphiques natifs avec les séries turquoise, rose, Signal, Ardoise, Indigo.
- Exemple commenté avec notes de l'orateur : `references/modeles/Clixite-Presentation-Exemple-2026.pptx`.

### Document Word
- Partir de `references/modeles/Clixite-Lettre-2026.dotx` (lettre) ou `Clixite-Offre-2026.dotx` (offre, rapport, proposition). Pour python-docx, convertir de la même façon (`wordprocessingml.template.main+xml` vers `wordprocessingml.document.main+xml`).
- Utiliser les styles nommés, jamais de mise en forme manuelle : Titre, Titre 1, Titre 2, Titre 3, Étiquette Clixite, Citation Clixite, Chiffre Clixite, Liste à puces. Tableaux à en-tête Papier et chiffres à droite.

### Tableau Excel
- Partir de `references/modeles/Clixite-Suivi-2026.xltx` ; styles nommés `Clixite en-tête`, `Clixite corps`, `Clixite nombre` ; chiffres en JetBrains Mono alignés à droite ; une feuille Palette est fournie.

### Page web, artefact HTML, visuel
- Inclure `references/tokens.css` puis `references/kit-html.css` (polices, jetons, composants `clx-`). Thème Papier par défaut, bloc Encre avec `data-theme="encre"` ou la classe `clx-encre`.
- Hiérarchie type : titre Space Grotesk, chapeau Inter 19 px, corps 16 px sur 66 caractères, données en mono. Un seul bouton principal par écran (fond turquoise, texte Encre). Focus visible, cibles de 44 px, contraste AA. Surfaces du navigateur thématisées (sélection, curseur, défilement).
- Pour un hero ou une couverture animée : le moteur `ouverture3d.js` et `scene.json` du site (https://charte.clixite.be/assets/), ou la page autonome `clixite-ouverture.html`. Pas d'autre animation sur la page.

### Post LinkedIn, réseaux
- Carré 1200 × 1200 ou 4:5. Papier avec un filet turquoise en haut et le X Relief en haut à droite, ou Encre avec le mot-marque inversé. Titre Space Grotesk 600 en deux lignes, un paragraphe Inter, un chiffre en Space Grotesk 700 si le post en porte un, logo en pied. Un seul moment de signature. Le texte suit la compétence `rediger-clixite`.

### Signature de courriel
- Reprendre le bloc HTML de https://charte.clixite.be/downloads/signature/signature-mail.html (table, symbole Relief 64 px depuis le site, nom en Space Grotesk, fonction, coordonnées, descripteur). Ne pas y ajouter d'image supplémentaire ni de citation.

### Graphiques
- Séries dans l'ordre turquoise #19B3D9, rose #FF4F8B, Signal #FFD233, Ardoise #4B5A6B, Indigo #193776 ; fond Papier, axes Brume, étiquettes mono ; étiquettes directes, pas de camembert 3D ni de quadrillage lourd ; source et date sous le graphique.

## Avant de livrer

Contrôler le résultat avec la compétence `verifier-charte-clixite` (script `verifier_charte.py` fourni), corriger tous les points bloquants et à corriger, puis vérifier visuellement : logo officiel intact à sa zone de protection, un seul moment de signature, contraste AA sur chaque paire texte et fond, aucun chiffre inventé, descripteur en anglais.

## Références

- `references/regles.md` : la charte complète, version texte.
- `references/DESIGN.md` : le système au format DESIGN.md (jetons YAML et règles) pour les agents.
- `references/tokens.css`, `references/tokens.json` : couleurs, polices, échelle, espacements, mouvement (thèmes Papier et Encre).
- `references/kit-html.css` : base prête à l'emploi pour toute sortie HTML.
- `references/dispositions-office.md` : dispositions PowerPoint, styles Word et Excel.
- `references/logos/` : fichiers officiels du logo. `references/modeles/` : modèles Office.
- https://charte.clixite.be/ : la charte en ligne, tous les téléchargements, l'animation.
