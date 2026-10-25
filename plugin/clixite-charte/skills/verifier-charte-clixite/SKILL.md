---
name: verifier-charte-clixite
description: "Contrôle un contenu Clixite (texte, HTML, CSS, Word, PowerPoint, Excel) contre la charte graphique et la voix de la marque, avec un score sur 100 et la liste des corrections. À utiliser quand l'utilisateur demande de « vérifier la charte », « contrôler avant envoi », « relire aux normes Clixite », « est-ce conforme », et systématiquement avant de livrer un document, une présentation, une page web ou un post produit pour Clixite, Vidango ou CyGap."
metadata:
  version: "1.0.0"
---

# Vérifier un contenu contre la charte Clixite

## Étape 1 · Contrôle automatique

Lancer le vérificateur fourni avec cette compétence sur chaque fichier à livrer (texte, Markdown, HTML, CSS, .docx, .dotx, .pptx, .potx, .xlsx) :

```bash
python <dossier de cette compétence>/scripts/verifier_charte.py chemin/du/fichier [--langue fr|nl|en] [--interne] [--json]
```

Pour un texte collé, l'envoyer sur l'entrée standard avec `-` comme fichier. `--interne` pour un document interne (le tutoiement n'est alors pas signalé).

Le vérificateur classe chaque écart :
- **Bloquant** (−10) : tiret long ou demi-cadratin, double tiret ou double souligné dans un texte, émoji, descripteur traduit.
- **À corriger** (−4) : buzzwords et promesses vagues (synergies, disruption, transformation digitale, de bout en bout, partenaire de confiance, n'hésitez pas, propulsé par l'IA, leader, superlatifs), point d'exclamation, nombre sans séparateur de milliers, € avant le montant, unité collée, tutoiement en externe, titre en capitales, couleur hors palette, police hors charte, dégradé, ombre portée, bordure colorée à gauche, easing à rebond.
- **Conseil** (−1) : typographie française (espace avant ; : ?, guillemets « »), plus de trois hashtags, phrase de plus de 35 mots, « unique », « ia » en minuscules.

Corriger tous les bloquants et tous les points à corriger, puis relancer jusqu'à obtenir « aucun point bloquant ni à corriger ». Viser un score d'au moins 95. Un contre-exemple cité volontairement se met entre `~~` pour être ignoré.

## Étape 2 · Contrôle visuel (non automatisable)

Regarder le rendu (image de la page, de la slide ou du document) et vérifier :
1. Le logo est un des fichiers officiels, intact, à sa zone de protection (la hauteur du X), au bon niveau de taille : Interférence à 200 px et plus, Relief ou Interférence simplifiée de 48 à 200 px, X maître plat sous 48 px, X plein sous 24 px. Descripteur en anglais.
2. Un seul moment de signature (turquoise, rose et Signal ensemble) par support ; dans le corps, un seul accent, turquoise par défaut. Le Signal ne porte aucun texte. Aucun gris ni noir pur.
3. Contraste AA sur chaque paire texte et fond (turquoise et rose purs jamais en texte sur fond clair).
4. Pas de dégradé, pas d'ombre, pas de carte dans une carte, pas d'étiquette-chapeau au-dessus d'un titre, pas d'émoji, pas de mono pour du texte courant.
5. Les chiffres, références clients, dates et citations viennent d'une source réelle ; tout chiffre non sourcé est signalé à l'utilisateur comme champ à compléter.
6. Le mouvement, s'il y en a : une seule séquence, courbe de la charte, rien ne rebondit, reduced-motion respecté.
7. Les trois langues, si présentes, ont la même structure ; le *x* est en italique Fraunces.

## Étape 3 · Compte rendu

Donner à l'utilisateur le score, les corrections faites et les points qui restent à sa décision (chiffre à confirmer, exception à la charte, photo à remplacer). Ne jamais déclarer conforme un contenu qui n'a pas passé l'étape 1.
