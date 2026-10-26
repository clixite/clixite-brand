// www.clixite.be, refonte 2030 : site statique Astro, servi par nginx sur le VPS.
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://www.clixite.be",
  trailingSlash: "always",
  build: { format: "directory", inlineStylesheets: "always" },
  integrations: [sitemap({ i18n: { defaultLocale: "fr", locales: { fr: "fr-BE", en: "en" } } })],
  compressHTML: true,
  prefetch: false,
});
