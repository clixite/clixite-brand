# Clixite Design System 2.0

Le système qui fait tourner www.clixite.be (refonte 2030) et, à terme, charte.clixite.be. Il prolonge la charte (`DESIGN.md`) sans la contredire : mêmes couleurs, mêmes polices, même X. Ce qui change, c'est la forme : des tokens standardisés, des contrastes vérifiés à chaque build et des composants documentés.

## Tokens

- Format **W3C Design Tokens (DTCG)** : `ds/tokens/primitives.tokens.json` (valeurs brutes) et `ds/tokens/themes.tokens.json` (rôles sémantiques, typographie fluide, mise en page).
- Compilation : `node ds/build-tokens.mjs` produit `ds/dist/tokens.css` (variables `--clx-*`), `ds/dist/tokens.json` et `ds/dist/contrast.json`.
- **Garde-fou de contraste** : 14 paires texte et fond contrôlées dans chaque thème (WCAG 2.2 AA : 4,5:1 pour le texte, 3:1 pour le focus et les bordures fortes). Si une paire échoue, le build s'arrête. Le site ne peut donc pas partir en ligne avec un contraste insuffisant.
- Deux thèmes : `papier` (défaut) et `encre` (bandes sombres, pied de page). `data-theme="auto"` suit le réglage du système.

| Rôle | Papier | Encre |
|---|---|---|
| fond / texte | Papier #F6F5F0 / Encre #0B2239 (14,8:1) | Encre / Papier |
| texte secondaire | Ardoise #4B5A6B | Brume #CDD5DD |
| accent (boutons) | Turquoise #19B3D9, texte Encre | idem |
| lien | Turquoise-texte #0C7893 | Turquoise #19B3D9 |
| focus | Turquoise-texte | Signal #FFD233 |

## Typographie

Échelle fluide en `clamp()`, aucune rupture brutale entre mobile et grand écran : display (3 à 7 rem), h1, h2, h3, lead, body 17 px, small, citation (Fraunces italique), données (JetBrains Mono, chiffres tabulaires), chiffre clé (Fraunces italique). Polices auto-hébergées, sous-ensemble latin, `font-display: swap` et **polices de repli ajustées** (`size-adjust`, `ascent-override`, `descent-override`) : aucun saut de mise en page au chargement (CLS mesuré : 0).

## Composants (prototype Astro, `web/src/components/`)

| Composant | Rôle | États et règles |
|---|---|---|
| Header | logo, navigation, bouton de réservation | collant, filet qui apparaît au défilement (CSS `animation-timeline`, sans JavaScript), menu mobile en `details` natif |
| Hero | promesse, offre, appel à l'action, X en construction | ouverture orchestrée 2,4 s, puis seul l'angle entre les champs vit (4° à 6°, jusqu'à 8° près du pointeur). Écrans tactiles : pas de boucle. `prefers-reduced-motion` : X au repos à 8° |
| ClientLogos | références | fichiers officiels uniquement (registre `web/src/data/clients.registry.json`), teinte par masque CSS, équilibrage optique par surface et densité d'encre mesurées au build |
| Gap, Profile, Method, Expertises, Offers, Proofs, FinalCta | sections de la page d'accueil | une idée par section, titres sur deux lignes au plus, panneaux selon la charte (blanc, Brume 1 px, rayon 10, sans ombre) |
| Boutons | principal (turquoise, texte Encre), secondaire (contour) | 48 px de haut (44 px en petit), pression `scale(.97)` en 160 ms, focus visible 3 px |
| FAQ | questions fréquentes | `details` natif, balisage `FAQPage` |
| Sélecteur d'audience | grand groupe, PME, cabinet | boutons radio natifs ; le contenu `[data-aud]` s'adapte en CSS (`:has`), avec repli par attribut `data-audience` ; lien `?pour=groupe|pme|cabinet` pour la prospection ; l'angle des champs du X suit le choix (4°, 7°, 5,5°) |
| Solveur | qualification en trois questions | règles explicites (pas d'IA), recommandation rendue côté serveur puis mise à jour en direct, courriel prérempli avec les réponses, rien n'est envoyé sans clic |
| Parcours en X | deux trajectoires qui se croisent | SVG monochrome, traits perpendiculaires (pas de points reliés), liste accessible et version mobile en deux colonnes |
| Boîte à outils | six familles de compétences | ordre des familles selon l'audience (`order` en CSS) |

## Mouvement

Une courbe (`cubic-bezier(.2, .8, .2, 1)`), des durées en tokens (160, 240, 450, 600, 2 400 ms), uniquement `transform` et `opacity` (et l'angle des champs, une propriété CSS enregistrée `--hx-a`). Une seule séquence orchestrée par page. Aucune apparition en fondu section par section.

## Logos clients

1. Déposer le fichier SVG officiel dans `web/src/assets/clients/source/`.
2. L'inscrire dans `clients.registry.json` (nom, groupe `missions` ou `parcours`, source, accord du client).
3. `npm run clients` recadre la viewBox sur l'encre réelle, retire les métadonnées et mesure la densité. Rien n'est redessiné.

## Prévisualisation et contenus à valider

Tout contenu non confirmé porte la classe `av`. Le build de prévisualisation (`PUBLIC_REVIEW=1`) les surligne et ajoute `noindex`. Le build de production les affiche normalement : on ne publie qu'après validation.

## Icônes

Lucide (licence ISC), trait 1,75 px, 24 px, en Encre ou Ardoise, importées en SVG statique. Pas de tuile d'icône au-dessus des titres.
