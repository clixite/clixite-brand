// Données de référence du site. Tout ce qui n'est pas confirmé par Nicolas porte `aValider: true`
// et s'affiche surligné dans la prévisualisation (PUBLIC_REVIEW=1), jamais en production.
export const SITE = {
  name: "Clixite",
  legalName: "Clixite SRL",
  url: "https://www.clixite.be",
  locale: "fr-BE",
  email: "nicolas@clixite.be",
  // numéros communiqués par Nicolas Simon le 26 octobre 2026 ; `tel` au format E.164 pour les liens et les données structurées
  phones: [
    { country: "BE", label: "Belgique", display: "+32 10 31 10 00", tel: "+3210311000" },
    { country: "LU", label: "Luxembourg", display: "+352 20 42 02 02", tel: "+35220420202" },
  ],
  vat: "BE 0871.430.776",
  vatId: "BE0871430776",
  founded: "2005",
  address: { street: "Avenue Reine Astrid 53", postalCode: "1300", city: "Wavre", region: "Brabant wallon", country: "BE" },
  linkedin: "https://www.linkedin.com/in/nicolassim/",
  charte: "https://charte.clixite.be/",
  descriptor: "ENTERPRISE & SOLUTION ARCHITECTURE",
  founder: {
    name: "Nicolas Simon",
    jobTitle: "Enterprise & Solution Architect, Forward Deployed Engineer",
    certifications: ["PMP", "PRINCE2", "AgilePM", "SAFe", "Scrum", "ITIL v3", "ADKAR"],
    languages: ["fr", "en", "nl"],
  },
  // Microsoft Bookings : lien public de réservation à fournir par Nicolas. Sans lien, le bouton ouvre un courriel prérempli.
  bookingsUrl: "" as string,
} as const;

export const REVIEW = import.meta.env.PUBLIC_REVIEW === "1";

// page pilier du Forward Deployed Engineering, premier métier mis en avant (à la racine : c'est l'offre principale)
export const FDE_PATH = "/forward-deployed-engineering/";
export const FDE_PATH_EN = "/en/forward-deployed-engineering/";
// GEO (Generative Engine Optimization) : deuxième métier mis en avant
export const GEO_PATH = "/geo-referencement-ia/";

export const NAV = [
  { href: FDE_PATH, label: "Forward Deployed Engineering" },
  { href: GEO_PATH, label: "GEO" },
  { href: "/expertises/", label: "Expertises" },
  { href: "/#methode", label: "Méthode" },
  { href: "/#references", label: "Références" },
];

export const bookingHref = (lang: "fr" | "en" = "fr") =>
  SITE.bookingsUrl ||
  (lang === "en"
    ? `mailto:${SITE.email}?subject=${encodeURIComponent("First conversation with Clixite")}&body=${encodeURIComponent("Hello,\n\nOur challenge, in two sentences:\n\n\nAvailability:\n")}`
    : `mailto:${SITE.email}?subject=${encodeURIComponent("Premier échange avec Clixite")}&body=${encodeURIComponent("Bonjour,\n\nNotre enjeu, en deux phrases :\n\n\nDisponibilités :\n")}`);

// thèmes de compétence (JSON-LD knowsAbout) : le FDE en tête ; les règlements européens pointent vers leur texte officiel
export const KNOWS_ABOUT: (string | Record<string, string>)[] = [
  "Forward Deployed Engineering", "Generative Engine Optimization (GEO)", "Référencement naturel (SEO)", "Données structurées schema.org", "Architecture d'entreprise", "Architecture de solutions", "Pilotage de programmes", "Digitalisation des processus",
  "Mise en production de l'intelligence artificielle", "Agents IA", "Intégration de systèmes", "Conduite du changement", "Transformation des achats",
  "Source-to-Pay", "SAP Ariba", "Fractional CPO", "Gestion des risques tiers (TPRM)",
  { "@type": "Thing", name: "DORA (règlement (UE) 2022/2554)", sameAs: "https://eur-lex.europa.eu/eli/reg/2022/2554/oj" },
  { "@type": "Thing", name: "NIS2 (directive (UE) 2022/2555)", sameAs: "https://eur-lex.europa.eu/eli/dir/2022/2555/oj" },
  { "@type": "Thing", name: "AI Act (règlement (UE) 2024/1689)", sameAs: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj" },
  "RGPD",
];
