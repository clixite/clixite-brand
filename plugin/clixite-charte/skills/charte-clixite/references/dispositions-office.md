# Dispositions PowerPoint, styles Word et styles Excel Clixite

Les modèles sont dans ce dossier `modeles/`. Ils embarquent les polices Space Grotesk et Inter par leur nom : si elles ne sont pas installées sur le poste, Office retombe sur Arial et Calibri (acceptable pour un document de travail, pas pour une offre). Les polices se téléchargent sur https://charte.clixite.be/downloads/fonts/clixite-polices.zip.

## PowerPoint · Clixite-Presentation-2026.potx (16:9, 13,333 × 7,5 pouces)

Thème : dk1 Encre `0B2239`, lt1 blanc, dk2 Ardoise `4B5A6B`, lt2 Papier `F6F5F0`, accent1 turquoise `19B3D9`, accent2 rose `FF4F8B`, accent3 Signal `FFD233`, accent4 turquoise texte `0C7893`, accent5 Indigo `193776`, accent6 Brume `CDD5DD`. Police de titre Space Grotesk, police de corps Inter. Utiliser les couleurs du thème, jamais des hexadécimaux posés à la main : une présentation reste rethémable.

| Disposition | Fond | Espaces réservés | Usage |
| --- | --- | --- | --- |
| COUVERTURE | Encre | `title`, `body` (sous-titre) ; symbole X couleur en haut à droite | Première slide. Titre en Space Grotesk 44, sous-titre en Brume. |
| SECTION | Encre | `num` (numéro, turquoise, 56), `title`, `body` | Intercalaire. Un seul mot ou une phrase. |
| CONTENU | Papier | `title`, `body` (puces) | Slide à puces, 5 puces au plus, une idée par slide. |
| TITRE_SEUL | Papier | `title` | Composition libre : cartes, chiffres clés, schéma. La plupart des slides de contenu. |
| TITRE_SEUL_SOMBRE | Encre | `title` | Même usage, sur Encre, pour un visuel plein cadre ou la peau Interférence. |
| DEUX_COLONNES | Papier | `title`, `body`, `body2` | Comparaison, avant et après, deux listes. |
| GRAPHIQUE | Papier | `title`, `chart` | Un graphique natif PowerPoint ; séries turquoise, rose, Signal, Ardoise, Indigo. |
| TABLEAU | Papier | `title`, `table` | Tableau natif ; en-tête Papier, chiffres à droite en JetBrains Mono. |
| CLOTURE | Encre | `title`, `body` (coordonnées) | Dernière slide : « Nous résolvons votre x. », coordonnées, symbole couleur. |

Pied de page sur chaque disposition : symbole X monochrome à gauche, « Clixite · Enterprise & Solution Architecture » et numéro de slide en JetBrains Mono.

Avec python-pptx : copier le `.potx` sous un nom `.pptx`, remplacer dans `[Content_Types].xml` le type `presentationml.template.main+xml` par `presentationml.presentation.main+xml`, puis ouvrir ; utiliser `prs.slide_layouts` par nom. Avec pptxgenjs : reprendre le fichier `build_pptx.js` du dépôt `clixite/clixite-brand` (thème, 9 dispositions et exemple commenté) ; les placeholders se remplissent par nom.

Exemple commenté avec notes de l'orateur : `Clixite-Presentation-Exemple-2026.pptx`.

## Word · Clixite-Lettre-2026.dotx et Clixite-Offre-2026.dotx (A4, marges 22 mm, en-tête 32 mm)

En-tête : logo Relief couleur (42 mm) à gauche. Pied : « Clixite SRL · Avenue Reine Astrid 53, 1300 Wavre · BE 0871.430.776 · nicolas@clixite.be · clixite.be » en Inter 8, puis ENTERPRISE & SOLUTION ARCHITECTURE en Space Grotesk 7,5 turquoise texte.

| Style | Police | Usage |
| --- | --- | --- |
| Normal | Inter 10,5, interligne 1,3, Encre | Texte courant. |
| Titre (Title) | Space Grotesk 30 gras | Titre de couverture d'une offre. |
| Titre 1 / 2 / 3 | Space Grotesk 22 / 15 / 12 gras (Titre 3 en turquoise texte) | Chapitres, sections, étapes. |
| Étiquette Clixite | JetBrains Mono 8 gras, capitales, turquoise texte | Surtitre, date, « Proposition de services », références. |
| Citation Clixite | Fraunces 15 italique, retrait 8 mm | Citation du client, chiffre clé en phrase, le *x*. |
| Chiffre Clixite | Space Grotesk 28 gras | Chiffre clé isolé (suivi d'un libellé en Normal ou Étiquette). |
| Liste à puces (List Bullet) | Inter | Listes courtes, trois à cinq points. |

Tableaux : première ligne fond Papier et texte Space Grotesk gras, filets Brume 0,5 pt, chiffres alignés à droite. Avec python-docx : `doc.add_paragraph(texte, style="Étiquette Clixite")`. Ne jamais mettre en forme à la main ce qu'un style couvre.

Le modèle d'offre contient : couverture (X, étiquette, titre, client et version), sommaire, 1 Contexte et enjeu, 2 Ce que nous proposons (Cadrer, Construire, Livrer), 3 Livrables (tableau), 4 Planning, 5 Équipe, 6 Budget (tableau, HTVA), 7 Conditions, bloc de signature.

## Excel · Clixite-Suivi-2026.xltx

Feuille « Suivi » : logo, titre Space Grotesk 18, ligne d'étiquette turquoise, tableau avec les styles nommés `Clixite en-tête` (Space Grotesk gras, fond Papier, filet Encre), `Clixite corps` (Inter 10) et `Clixite nombre` (JetBrains Mono, aligné à droite, format `# ##0,00 "€"`) ; mise en forme conditionnelle sur la colonne Statut (À faire, En cours, Fait). Feuille « KPI » pour les indicateurs, feuille « Palette » avec les couleurs de la charte. Appliquer un style : `cell.style = "Clixite nombre"`.
