# Déployer charte.clixite.be et www.clixite.be

## Ce que l'on a constaté le 25 octobre 2026

- clixite.be (76.13.46.55) n'est pas un hébergement mutualisé mais le **VPS Hostinger srv1352234** (Ubuntu 24.04, KVM 8, Paris). Il n'y a ni sous-domaine, ni gestionnaire de fichiers, ni SSL « en un clic » : tout passe par Docker (hPanel > VPS > Gestionnaire Docker) et par **Traefik v3.3** (projet `traefik-svsx`, provider fichier `/docker/traefik-svsx/config/*.yml`, résolveur TLS `le`, réseau `proxy`).
- La zone DNS de clixite.be est servie par **Microsoft 365** (`ns1-4.bdm.microsoftonline.com`), pas par OVH ; l'enregistrement A `charte` y a été ajouté par Nicolas.

## Déploiement retenu : projet Docker `clixite-sites` (deploy/)

`deploy/docker-compose.yml` crée deux conteneurs : `clixite-sync` (alpine) qui, toutes les cinq minutes, télécharge les branches `site` (charte) et `www` (accueil) du dépôt public et dépose `nginx.conf` et le routage Traefik ; `clixite-web` (nginx) qui sert les deux sites. Le dépôt doit être **public** pour que le VPS le lise sans clé (le contenu est de toute façon un site web). Mise en place, une fois : hPanel > VPS > Gestionnaire Docker > Composer, nom `clixite-sites`, coller le YAML, Déployer. Ensuite, chaque push sur `main` est en ligne dans les cinq minutes.

Les anciennes instructions ci-dessous (hébergement mutualisé) sont conservées pour mémoire.

---

Le site est statique : un dossier `charte/` à copier tel quel dans le dossier web du sous-domaine. Trois façons de le faire, de la plus simple à la plus autonome.

## 0. Créer le sous-domaine (une fois)

1. hPanel, Sites web, clixite.be, Domaines, Sous-domaines : créer `charte`. Hostinger propose un dossier ; garder la valeur par défaut (`public_html/charte` ou `domains/charte.clixite.be/public_html` selon le plan) et la noter : c'est le **dossier cible**.
2. DNS : les serveurs de noms de clixite.be sont ceux de **Microsoft 365** (`ns1.bdm.microsoftonline.com` à `ns4`), constaté le 25 octobre 2026. La zone active se gère donc dans le centre d'administration Microsoft 365 (https://admin.microsoft.com/#/Domains, clixite.be, Enregistrements DNS) : ajouter un enregistrement **A, nom d'hôte `charte`, adresse 76.13.46.55** (l'IP de www.clixite.be chez Hostinger), TTL 1 heure. La zone OVH du domaine existe toujours (le workflow DNS de ce dépôt la gère) mais elle n'est pas servie tant que les serveurs de noms restent chez Microsoft. Propagation : quelques minutes à une heure.
3. SSL : hPanel, Sécurité, SSL, installer le certificat gratuit sur charte.clixite.be, puis forcer HTTPS.

## 1. À la main (gestionnaire de fichiers)

Télécharger `clixite-charte-site.zip` (fourni dans la conversation, ou le produire avec `cd charte && zip -r ../clixite-charte-site.zip .`), hPanel, Fichiers, Gestionnaire de fichiers, aller dans le dossier cible, Importer, puis Extraire l'archive à la racine du dossier. Vérifier que `index.html` est bien directement dans le dossier cible, pas dans un sous-dossier.

## 2. Autonome, sans identifiant partagé : Git sur Hostinger (recommandé)

Le dépôt GitHub `clixite/clixite-brand` publie automatiquement le contenu de `charte/` sur une branche `site` à chaque push sur `main`. Hostinger sait suivre une branche Git.

1. hPanel, Sites web, clixite.be, Avancé, **Git**.
2. Si le dépôt est privé : copier la clé SSH publique affichée par hPanel (« Générer une clé SSH » si besoin), puis GitHub, dépôt clixite-brand, Settings, Deploy keys, Add deploy key, coller, lecture seule.
3. Créer le dépôt dans hPanel : adresse `git@github.com:clixite/clixite-brand.git`, branche **`site`**, répertoire d'installation : le dossier cible du sous-domaine (vide au moment de la création).
4. Dans la ligne du dépôt, activer **Déploiement automatique** : hPanel donne une URL de webhook. GitHub, Settings, Webhooks, Add webhook : coller l'URL, Content type `application/json`, événement « Just the push event ».
5. Cliquer « Déployer » une première fois.

À partir de là, chaque mise à jour de la charte poussée sur GitHub est en ligne en moins d'une minute, sans que personne ne manipule un mot de passe. Claude peut pousser sur `main` depuis ses sessions ; Hostinger fait le reste.

## 3. Autonome par FTPS (si la route Git n'est pas disponible sur le plan)

1. hPanel, Fichiers, Comptes FTP : créer un compte dédié `charte@clixite.be` limité au dossier cible.
2. GitHub, dépôt clixite-brand, Settings, Secrets and variables, Actions :
   - secrets `FTP_SERVER` (ex. `ftp.clixite.be` ou l'IP donnée par hPanel), `FTP_USERNAME`, `FTP_PASSWORD` ;
   - variable `FTP_SERVER_DIR` = chemin du dossier cible vu depuis le compte FTP (par exemple `/` si le compte est limité au dossier, sinon `/public_html/charte/`).
3. Le workflow `.github/workflows/deploy.yml` détecte les secrets et envoie `charte/` par FTPS à chaque push. Sans secrets, cette étape est simplement ignorée.

Les identifiants restent dans les secrets GitHub : ni dans le dépôt, ni dans les conversations.

## Vérifier

- https://charte.clixite.be/ affiche le X animé et le menu des onze chapitres.
- https://charte.clixite.be/downloads/clixite-kit-complet.zip se télécharge (environ 7 Mo).
- https://charte.clixite.be/animation/clixite-ouverture.html joue l'ouverture.
- La signature mail charge son image depuis https://charte.clixite.be/downloads/logo/x-relief-color-transparent-256px.png.

## OVH

La zone OVH n'est utile que si les serveurs de noms de clixite.be reviennent un jour chez OVH (étape 0.2) ; dans ce cas le workflow `DNS OVH clixite.be` du dépôt gère les enregistrements. Dans ce cas, plutôt qu'un accès au compte, créer une clé API OVH limitée (https://www.ovh.com/auth/api/createToken) avec les droits `GET/POST/PUT/DELETE /domain/zone/clixite.be/*` uniquement, et la stocker en secret GitHub (`OVH_APP_KEY`, `OVH_APP_SECRET`, `OVH_CONSUMER_KEY`) : un petit workflow peut alors gérer les enregistrements sans jamais voir le mot de passe du compte.
