#!/bin/sh
# Synchronise les branches `site` et `www` du dépôt public clixite/clixite-brand vers /www/<branche>,
# et dépose la configuration nginx et Traefik. Tourne dans le conteneur clixite-sync (alpine).
set -e
REPO="clixite/clixite-brand"
# les fichiers de configuration sont lus via l'API GitHub (contenu brut) :
# raw.githubusercontent.com peut servir une version en cache plusieurs minutes après un push.
API="https://api.github.com/repos/$REPO/contents/deploy"
mkdir -p /www /state
for b in site www; do
  head=$(curl -fsSL -H "Accept: application/vnd.github.sha" "https://api.github.com/repos/$REPO/commits/$b" 2>/dev/null || true)
  if [ -z "$head" ]; then echo "[$b] HEAD inconnu (API indisponible), on réessaie plus tard"; continue; fi
  if [ -f /state/$b.sha ] && [ "$(cat /state/$b.sha)" = "$head" ] && [ -d /www/$b ]; then echo "[$b] à jour ($head)"; continue; fi
  echo "[$b] mise à jour vers $head"
  rm -rf /tmp/$b /tmp/$b.zip; mkdir -p /tmp/$b
  curl -fsSL -o /tmp/$b.zip "https://codeload.github.com/$REPO/zip/$head"
  unzip -q /tmp/$b.zip -d /tmp/$b
  src=$(find /tmp/$b -maxdepth 1 -mindepth 1 -type d | head -1)
  rm -rf /www/$b.new; mkdir -p /www/$b.new; cp -a "$src"/. /www/$b.new/
  rm -rf /www/$b.old; [ -d /www/$b ] && mv /www/$b /www/$b.old; mv /www/$b.new /www/$b; rm -rf /www/$b.old
  echo "$head" > /state/$b.sha
  rm -rf /tmp/$b /tmp/$b.zip
done
[ -d /stack/nginx.conf ] && rm -rf /stack/nginx.conf   # reliquat du premier déploiement (Docker avait créé un dossier)
mkdir -p /stack/conf.d
curl -fsSL -H "Accept: application/vnd.github.raw" -o /stack/conf.d/clixite.conf.new "$API/nginx.conf?ref=main&v=$(date +%s)" && mv /stack/conf.d/clixite.conf.new /stack/conf.d/clixite.conf
curl -fsSL -H "Accept: application/vnd.github.raw" -o /traefik-config/clixite-sites.yml.new "$API/traefik-clixite.yml?ref=main&v=$(date +%s)" && mv /traefik-config/clixite-sites.yml.new /traefik-config/clixite-sites.yml
echo "sync ok $(date -u +%FT%TZ)"
