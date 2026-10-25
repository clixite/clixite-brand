# clixite-brand

La marque Clixite, en code. Ce dépôt contient le générateur du logo, le kit de marque complet et le site de la charte publié sur https://charte.clixite.be/.

Le logo n'est pas dessiné à la main : chaque fichier (SVG, PNG, favicons, bannières, modèles Office, animation) sort du même générateur Python. Changer une valeur dans `logos10.py` et relancer `npm run all` régénère tout, au pixel.

## Structure

| Dossier ou fichier | Rôle |
| --- | --- |
| `charte/` | Le site statique déployé sur charte.clixite.be, avec tous les téléchargements (`charte/downloads/`), l'animation (`charte/animation/`) et les polices auto-hébergées (`charte/fonts/`). |
| `logos10.py` | Le logo final (piste P) : X maître, peau Relief, peau Interférence, mots-marques central, symbole à gauche, empilé. Les constantes de construction sont en tête de fichier (`STEM`, `EXTRUDE_DEG`). |
| `typo.py`, `geom.py` | Mise en forme des glyphes (fontTools + HarfBuzz) et géométrie (shapely). |
| `logos.py` à `logos9.py` | Les pistes explorées avant la piste P (A à O). Conservées pour l'historique ; `logos.py` porte aussi la palette et `logos2.py` les schémas de couleur. |
| `build_pack.py` | Pack logo : SVG, PNG 800 à 3200 px, favicons, icône d'app, avatar, bannière LinkedIn, image Open Graph, fonds de visio, gabarit de post. |
| `build_pptx.js`, `build_docx.py`, `build_xlsx.py` | Modèles Office : présentation (9 mises en page), papier à lettre, modèle d'offre, tableau de suivi. |
| `anim.py` | Animation d'ouverture : HTML autonome, frames, MP4 1080p, GIF. |
| `build_site_assets.py`, `build_site.py`, `site_src/` | Le site de la charte : diagrammes, X vivant interactif, archives zip, `index.html`. |
| `render.js` | Rendu SVG vers PNG (resvg). |
| `DESIGN.md` | La charte résumée pour les agents IA et les développeurs : à lire avant de produire un support Clixite. |
| `.github/workflows/deploy.yml` | Déploiement : publie `charte/` sur la branche `site` (suivie par Hostinger) et, si les secrets existent, par FTPS. |

## Régénérer

```bash
npm install
pip install -r requirements.txt
npm run all        # pack logo, Office, animation, site
npm run preview    # http://localhost:8765
```

Étapes séparées : `npm run pack`, `npm run office`, `npm run anim`, `npm run site`. Les PNG passent par `node render.js in.svg out.png largeur`. La conversion des modèles Office en aperçus utilise LibreOffice et pdftoppm, présents sur la machine de build.

## Déployer

Voir `DEPLOIEMENT.md`. En résumé : un push sur `main` met à jour la branche `site` ; Hostinger (hPanel, Avancé, Git) suit cette branche et publie le site dans le dossier de charte.clixite.be. Aucune clé ni mot de passe dans ce dépôt.

## Règles essentielles

- Le X est central dans CLIXITE et le reste. Le récit « nous résolvons votre x » vit dans les textes, jamais dans le logo.
- Descripteur : ENTERPRISE & SOLUTION ARCHITECTURE, en anglais, sur tous les supports.
- Quatre niveaux : Interférence à 200 px et plus, Interférence simplifiée ou Relief de 48 à 200 px, X maître plat sous 48 px, X plein Encre sous 24 px.
- Le turquoise passe toujours par-dessus le rose. Le Signal ne porte jamais de texte.

Version 1.0, 25 octobre 2026. Clixite SRL, Wavre.
