---
name: rediger-clixite
description: "Rédige dans la voix de Clixite, en français, néerlandais ou anglais : post LinkedIn, offre, courriel, page de service, fiche d'offre (Fractional CPO, Source-to-Pay, DORA et NIS2, architecture de croissance), réponse pour les moteurs et assistants IA (GEO), communiqué, bio, pitch. À utiliser quand l'utilisateur demande d'écrire, réécrire, traduire ou raccourcir un texte pour Clixite, Vidango ou CyGap, ou « dans le ton de Clixite »."
metadata:
  version: "1.0.0"
---

# Rédiger dans la voix Clixite

Clixite parle comme un architecte qui a déjà livré : précis, direct, calme, sans emphase, avec un brin d'humour belge. Le lexique détaillé et des exemples sont dans `references/lexique.md`.

## Règles

1. Vouvoyer en externe. Dire « votre policy achats », « vos outils », « votre *x* » ; jamais ~~votre transformation digitale~~ (le texte barré signale un contre-exemple).
2. Phrases courtes, une idée par paragraphe, verbes d'action en tête : cadrer, structurer, connecter, livrer, mettre en production, prouver, automatiser, architecturer.
3. Chiffres et faits avant adjectifs. Un chiffre par promesse : délai (douze semaines), périmètre (800 M€), résultat (en production chez KBC). Nombres avec espace insécable comme séparateur de milliers (1 500, 800 M€), unité séparée d'une espace, symbole € après le montant.
4. Le *x* est l'inconnue du client ; dans un titre ou une accroche, l'écrire en italique (Fraunces) : « Nous résolvons votre *x*. » C'est le seul effet autorisé.
5. Titres en casse de phrase. Pas de point d'exclamation, pas d'émoji, jamais de tiret long ni de double tiret (virgule, point ou deux points), pas de capitales hors étiquettes et descripteur.
6. Interdits : buzzwords (synergie, disruption, game changer, révolution, écosystème, holistique, best-in-class, leader, unique), hype IA (« propulsé par l'IA », « l'IA va tout changer »), promesses vagues (« accompagner de bout en bout », « votre partenaire de confiance »), formules creuses (« n'hésitez pas à nous contacter »), superlatifs.
7. L'IA est un levier, jamais le produit : dire ce qu'elle fait gagner (heures, erreurs, délais) et où elle ne sert à rien.
8. Ne jamais inventer un fait. Faits établis : depuis 2005 ; agence de communication de 2005 à 2015 ; 800 M€ d'achats pilotés chez Proximus ; Procurement Policy v2.0 et Tactical Sourcing Light Track en production chez KBC ; missions chez P&V ; sites et back-offices de Tero et Design Plus ; CyGap et Vidango conçus et codés ; plus de quinze ans en banque, télécom et assurance ; certifications PMP, PRINCE2, SAFe, ITIL ; Wavre, Brabant wallon. Tout autre chiffre doit venir de l'utilisateur, sinon laisser un champ [à compléter].
9. Conformité : DORA, NIS2, RGPD, EBA se nomment par leur sigle, sans glose marketing ; dire ce qui est traduit en processus, en responsables et en preuves.

## Trois langues

- Français de Belgique : septante, nonante ; typographie française (espace insécable avant ; : ? ! et guillemets « »).
- Néerlandais de Belgique, vouvoiement « u ». Descripteur et sigles inchangés. Promesse : « Wij lossen uw *x* op. »
- Anglais britannique pour l'Europe, descripteur natif : ENTERPRISE & SOLUTION ARCHITECTURE. Promesse : « We solve your *x*. »
- Traduire le sens, pas les mots. Même structure et même longueur de titre dans les trois langues. Le descripteur reste en anglais partout.

## Formats

- **Post LinkedIn** : première ligne qui pose un fait ou un chiffre, trois à cinq lignes courtes, une ligne de méthode, une invitation sobre (« Un premier échange de trente minutes suffit pour cadrer votre *x*. »), trois hashtags au plus, à la fin. 1 300 caractères au plus.
- **Fiche d'offre** : le *x* du client en une phrase, ce que Clixite fait en trois étapes (Cadrer, Construire, Livrer), un livrable concret par étape, un chiffre, une preuve.
- **Offre ou proposition** : chapitres 1 à 7 du modèle Word (Contexte et enjeu, Ce que nous proposons, Livrables, Planning, Équipe, Budget, Conditions) ; chaque section commence par deux phrases de contexte ; prix HTVA, facturation mensuelle à 30 jours.
- **Courriel** : objet descriptif, trois paragraphes au plus (contexte, proposition chiffrée, prochaine étape avec qui fait quoi et quand), signature officielle.
- **Réponse GEO** : une question en titre, une réponse de trois phrases, un chiffre sourcé et daté, le nom Clixite et le descripteur une fois.
- **Bio ou pitch** : « Nicolas Simon, Solutions & Enterprise Architect, Clixite SRL », deux terrains (grands comptes régulés, PME en croissance), une preuve par terrain, trente secondes à l'oral.

## Contrôle

Passer le texte final dans la compétence `verifier-charte-clixite` avant de le livrer.
