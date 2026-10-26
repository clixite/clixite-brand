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
| Header | logo, navigation, bouton d'échange | collant, filet qui apparaît au défilement (CSS `animation-timeline`, sans JavaScript) ; filet turquoise sous la page courante, qui glisse d'un lien à l'autre pendant le changement de page ; menu mobile en `popover` natif (Échap et clic extérieur le ferment), lien vers l'autre langue quand la page existe en deux langues |
| Hero | promesse, métiers, appel à l'action, film | film de lancement en boucle plein cadre (sans titres ni logo), affiche prise à 3,8 s, promesse sur une plaque Encre à 92 % avec le filet turquoise des titres du film, quatre phrases du film synchronisées avec les plans ; film chargé après l'affichage, jamais en mouvement réduit ni en économie de données, bouton Pause visible |
| ClientLogos | « Là où nous avons travaillé » | fichiers officiels ou repris de duonexia.com, vérifiés par empreinte (registre `web/src/data/clients.registry.json`), teinte par masque CSS, équilibrage optique par surface et densité d'encre mesurées au build ; aucun projet détaillé |
| FdeBand | le Forward Deployed Engineering sur l'accueil | bande Encre, photo « tirage de plan », champs du X sur le dernier tiers de la photo (traits Encre à -4°, turquoise filaire à +4°) dont l'angle se referme au défilement ; trois engagements |
| GeoBand | le GEO sur l'accueil | bande Papier, photo « lumière » avec volet qui se retire, trois temps (mesurer, structurer, publier et suivre) ; aucun faux écran d'assistant |
| Expertises | les cinq métiers et leurs domaines | données dans `web/src/data/expertises.ts` ; le FDE et le GEO en tête avec un filet turquoise, chaque titre mène à sa page |
| Photo | photo traitée, responsive | `web/scripts/build-photos.py` (traitements « lumière » et « tirage de plan ») puis AVIF et WebP à plusieurs largeurs ; variante mobile possible ; cadre `.ph` au ratio fixe, parallaxe (`.ph--parallax`) réservée aux bandes pleine largeur, volet (`data-reveal`) pour une seule photo par page |
| LivingX | le X Interférence vivant | se construit à son entrée à l'écran (2,4 s), puis respire entre 4° et 6° ; au repos à 8° en mouvement réduit et sur écran tactile ; une seule instance par page |
| FdePage, MetierPage | pages métiers | chapo définitionnel citable, sections statiques, méthode en quatre X, questions fréquentes visibles, date de mise à jour, `Service`, `BreadcrumbList` et `FAQPage` en JSON-LD fidèles au texte visible |
| Method, Formats, FinalCta | sections de la page d'accueil | une idée par section ; les quatre X de la méthode se construisent au défilement ; les formats en tableau à filets (aucun prix ni aucune durée) ; l'appel final avec les deux téléphones et le X vivant |
| Boutons | principal (turquoise, texte Encre), secondaire (contour) | 48 px de haut (44 px en petit), pression `scale(.97)` en 160 ms, focus visible 3 px |
| CopyMail | adresse en clair et bouton Copier | pour qui n'a qu'une messagerie en ligne ; repli par sélection du texte si le presse-papiers est refusé |
| Faq | questions fréquentes | réponses toujours visibles (aucun accordéon), balisage `FAQPage` |
| Quotes | recommandations clients | n'apparaît que si `web/src/data/quotes.ts` contient au moins une citation, publiée avec l'accord de son auteur |

Le site ne contient aucun élément interactif de contenu : pas de sélecteur, pas de questionnaire, pas de contenu qui change selon le visiteur.

## Mouvement

Une courbe (`cubic-bezier(.2, .8, .2, 1)`), des durées en tokens (160, 240, 450, 600, 2 400 ms), uniquement `transform` et `opacity`. Une seule séquence orchestrée par page. Aucune apparition en fondu section par section.

## Logos clients

1. Déposer le fichier SVG officiel dans `web/src/assets/clients/source/`.
2. L'inscrire dans `clients.registry.json` (nom, groupe `references`, source, décision de publication).
3. `npm run clients` recadre la viewBox sur l'encre réelle, retire les métadonnées et mesure la densité. Rien n'est redessiné.

## Prévisualisation et contenus à valider

Tout contenu non confirmé porte la classe `av`. Le build de prévisualisation (`PUBLIC_REVIEW=1`) les surligne et ajoute `noindex`. Le build de production les affiche normalement : on ne publie qu'après validation.

## Icônes

Lucide (licence ISC), trait 1,75 px, 24 px, en Encre ou Ardoise, importées en SVG statique. Pas de tuile d'icône au-dessus des titres.
