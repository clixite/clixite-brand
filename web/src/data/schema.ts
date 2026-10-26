// Fabriques JSON-LD partagées par les pages (le graphe de l'organisation est dans layouts/Base.astro).
import { SITE } from "./site";

const abs = (path: string) => new URL(path, SITE.url).href;

export const breadcrumb = (items: { name: string; href: string }[]) => ({
  "@type": "BreadcrumbList",
  itemListElement: items.map((c, i) => ({ "@type": "ListItem", position: i + 1, name: c.name, item: abs(c.href) })),
});

// la FAQ balisée reprend mot pour mot le texte visible de la page
export const faqPage = (items: { q: string; a: string }[], lang = "fr-BE") => ({
  "@type": "FAQPage",
  inLanguage: lang,
  mainEntity: items.map((f) => ({ "@type": "Question", name: f.q, acceptedAnswer: { "@type": "Answer", text: f.a } })),
});

export const service = (o: { path: string; name: string; description: string; serviceType: string[]; alternateName?: string[]; lang?: string; areas?: Record<string, string> }) => ({
  "@type": "Service",
  "@id": `${abs(o.path)}#service`,
  name: o.name,
  ...(o.alternateName ? { alternateName: o.alternateName } : {}),
  description: o.description,
  serviceType: o.serviceType,
  provider: { "@id": `${SITE.url}/#org` },
  areaServed: [{ "@type": "Country", name: o.areas?.BE ?? "Belgique", identifier: "BE" }, { "@type": "Country", name: o.areas?.LU ?? "Luxembourg", identifier: "LU" }],
  availableLanguage: ["fr", "nl", "en"],
  url: abs(o.path),
  ...(o.lang ? { inLanguage: o.lang } : {}),
});
