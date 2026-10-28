// Langues et adresses du site. Une page = une clé ; chaque langue a son adresse, traduite (mots-clés dans l'URL).
// Le français reste à la racine (adresses publiées depuis l'origine) ; le néerlandais sous /nl/, l'anglais sous /en/.
export type Lang = "fr" | "nl" | "en";
export const LANGS: Lang[] = ["fr", "nl", "en"];

// codes hreflang et html lang : français et néerlandais de Belgique, anglais international
export const HREFLANG: Record<Lang, string> = { fr: "fr-BE", nl: "nl-BE", en: "en" };
export const OG_LOCALE: Record<Lang, string> = { fr: "fr_BE", nl: "nl_BE", en: "en_GB" };
// version proposée aux langues que le site ne couvre pas
export const X_DEFAULT: Lang = "fr";

export type RouteKey = "home" | "fde" | "geo" | "expertises" | "archi" | "pilotage" | "digit" | "achats" | "about" | "contact" | "legal";

export const ROUTES: Record<RouteKey, Record<Lang, string>> = {
  home: { fr: "/", nl: "/nl/", en: "/en/" },
  fde: { fr: "/forward-deployed-engineering/", nl: "/nl/forward-deployed-engineering/", en: "/en/forward-deployed-engineering/" },
  geo: { fr: "/geo-referencement-ia/", nl: "/nl/geo-vindbaarheid-ai/", en: "/en/generative-engine-optimization/" },
  expertises: { fr: "/expertises/", nl: "/nl/expertises/", en: "/en/expertise/" },
  archi: { fr: "/expertises/architecture-entreprise-solutions/", nl: "/nl/expertises/enterprise-en-solution-architectuur/", en: "/en/expertise/enterprise-solution-architecture/" },
  pilotage: { fr: "/expertises/pilotage-de-programmes/", nl: "/nl/expertises/programmamanagement/", en: "/en/expertise/programme-management/" },
  digit: { fr: "/expertises/digitalisation/", nl: "/nl/expertises/digitalisering/", en: "/en/expertise/digitalisation/" },
  achats: { fr: "/expertises/transformation-achats/", nl: "/nl/expertises/aankooptransformatie/", en: "/en/expertise/procurement-transformation/" },
  about: { fr: "/a-propos/", nl: "/nl/over-clixite/", en: "/en/about/" },
  contact: { fr: "/contact/", nl: "/nl/contact/", en: "/en/contact/" },
  legal: { fr: "/mentions-legales/", nl: "/nl/juridische-informatie/", en: "/en/legal-notice/" },
};

// ancres partagées entre pages (une ancre se traduit aussi : elle apparaît dans l'adresse)
export const ANCHORS = {
  method: { fr: "methode", nl: "werkwijze", en: "method" },
  refs: { fr: "references", nl: "referenties", en: "references" },
  fdeMethod: { fr: "methode-fde", nl: "werkwijze-fde", en: "how" },
  fdeRegulated: { fr: "environnement-regule", nl: "gereguleerde-omgeving", en: "regulated-environments" },
  achatsOffers: { fr: "offres-achats", nl: "formules-aankoop", en: "procurement-offers" },
} satisfies Record<string, Record<Lang, string>>;
export type AnchorKey = keyof typeof ANCHORS;

// adresses et ancres d'une langue, pour les fichiers de contenu : r.fde, r.geo, a.method…
export const routesFor = (lang: Lang) =>
  Object.fromEntries(Object.entries(ROUTES).map(([k, v]) => [k, v[lang]])) as Record<RouteKey, string>;
export const anchorsFor = (lang: Lang) =>
  Object.fromEntries(Object.entries(ANCHORS).map(([k, v]) => [k, v[lang]])) as Record<AnchorKey, string>;

export const langOf = (pathname: string): Lang => (/^\/nl(\/|$)/.test(pathname) ? "nl" : /^\/en(\/|$)/.test(pathname) ? "en" : "fr");
export const keyOf = (pathname: string): RouteKey | undefined => {
  const p = pathname.endsWith("/") ? pathname : pathname + "/";
  return (Object.keys(ROUTES) as RouteKey[]).find((k) => LANGS.some((l) => ROUTES[k][l] === p));
};
// versions linguistiques d'une page, pour hreflang (la page elle-même comprise)
export const alternatesOf = (key: RouteKey) => LANGS.map((l) => ({ lang: HREFLANG[l], path: ROUTES[key][l], code: l }));

export const LANG_NAMES: Record<Lang, { short: string; name: string }> = {
  fr: { short: "FR", name: "Français" },
  nl: { short: "NL", name: "Nederlands" },
  en: { short: "EN", name: "English" },
};
