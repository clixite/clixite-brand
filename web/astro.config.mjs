// www.clixite.be, refonte 2030 : site statique Astro, servi par nginx sur le VPS.
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import { keyOf, alternatesOf, ROUTES, X_DEFAULT } from "./src/i18n/routes.ts";

const SITE = "https://www.clixite.be";

export default defineConfig({
  site: SITE,
  trailingSlash: "always",
  build: { format: "directory", inlineStylesheets: "always" },
  integrations: [sitemap({
    // chaque adresse avec ses versions en français, néerlandais et anglais (slugs traduits : table src/i18n/routes.ts)
    serialize(item) {
      const path = new URL(item.url).pathname;
      const key = keyOf(path);
      if (key) item.links = [...alternatesOf(key).map((a) => ({ lang: a.lang, url: SITE + a.path })), { lang: "x-default", url: SITE + ROUTES[key][X_DEFAULT] }];
      return item;
    },
    // date de la dernière révision du contenu : à avancer à chaque mise à jour réelle des textes
    lastmod: new Date("2026-10-26"),
  })],
  compressHTML: true,
  prefetch: false,
});
