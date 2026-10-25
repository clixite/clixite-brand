// Données de référence du site. Tout ce qui n'est pas confirmé par Nicolas porte `aValider: true`
// et s'affiche surligné dans la prévisualisation (PUBLIC_REVIEW=1), jamais en production.
export const SITE = {
  name: "Clixite",
  legalName: "Clixite SRL",
  url: "https://www.clixite.be",
  locale: "fr-BE",
  email: "nicolas@clixite.be",
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

export const bookingHref = () =>
  SITE.bookingsUrl ||
  `mailto:${SITE.email}?subject=${encodeURIComponent("Échange de 30 minutes avec Clixite")}&body=${encodeURIComponent("Bonjour Nicolas,\n\nNotre x, en deux phrases :\n\n\nDisponibilités :\n")}`;

export const KNOWS_ABOUT = [
  "Architecture d'entreprise", "Architecture de solutions", "Forward Deployed Engineering", "Transformation des achats",
  "Source-to-Pay", "SAP Ariba", "Fractional CPO", "Gestion des risques tiers (TPRM)", "DORA", "NIS2", "RGPD", "AI Act",
  "Industrialisation de l'intelligence artificielle", "Pilotage de programmes", "Conduite du changement",
];
