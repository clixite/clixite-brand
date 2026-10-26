// PROVISOIRE : copie du français, à traduire.
// Textes communs à toutes les pages (en-tête, pied de page, contact, formats de collaboration, libellés).
// Rédaction Clixite : vouvoiement, phrases courtes, aucun tiret long, aucun chiffre ni prix ni durée.
import type { Common } from "../fr/common";
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("en");
const a = anchorsFor("en");

const common: Common = {
  lang: "en",
  skip: "Aller au contenu",
  ogAlt: "Nous résolvons votre x. Clixite : Forward Deployed Engineering, GEO, architecture d’entreprise et de solutions, pilotage de programmes, digitalisation.",
  // séparateur avant les deux-points (espace insécable en français)
  colon: " :",
  countries: { BE: "Belgique", LU: "Luxembourg" } as Record<string, string>,
  country: "Belgique",
  header: {
    home: "Clixite, accueil",
    main: "Navigation principale",
    mobile: "Navigation mobile",
    menu: "Menu",
    open: "Ouvrir le menu",
    cta: "Demander un échange",
    ctaShort: "Contact",
    contact: "Contact",
    languages: "Langue",
    nav: [
      { href: r.fde, label: "Forward Deployed Engineering" },
      { href: r.geo, label: "GEO" },
      { href: r.expertises, label: "Expertises" },
      { href: `${r.home}#${a.method}`, label: "Méthode" },
      { href: `${r.home}#${a.refs}`, label: "Références" },
    ],
  },
  footer: {
    contact: "Contact",
    expertise: "Expertises",
    info: "Informations",
    achats: "Transformation des achats",
    about: "À propos de Clixite",
    contactPage: "Contact",
    legal: "Mentions légales et confidentialité",
    charte: "Charte graphique",
    llms: "Résumé pour les assistants IA",
    legalLine: "société à responsabilité limitée. Siège :",
    vat: "BCE et TVA",
    rpm: "RPM Brabant wallon",
    since: "© 2005 à",
  },
  crumbs: { label: "Fil d'Ariane", home: "Accueil", expertises: "Expertises" },
  faqTitle: "Questions fréquentes.",
  others: "Nos autres métiers",
  deliverable: "Livrable",
  updated: "Mis à jour le 26 octobre 2026",
  cta: "Demander un échange",
  sources: "Sources",
  source: "Source",
  copy: { copy: "Copier l'adresse", ok: "Adresse copiée", sel: "Adresse sélectionnée" },
  booking: {
    subject: "Premier échange avec Clixite",
    body: "Bonjour,\n\nNotre enjeu, en deux phrases :\n\n\nDisponibilités :\n",
  },
  final: {
    title: ["Quel est votre ", "x", " ?"],
    lead: "Un premier échange suffit pour le nommer. Vous repartez avec une première piste, même si nous ne travaillons pas ensemble.",
    mail: "Ou écrivez directement à",
    tel: "Ou appelez",
    meet: "Rendez-vous à Wavre, chez vous ou en visio.",
  },
  formats: {
    title: "Travailler ensemble.",
    lead: "Le périmètre, la durée et le budget se fixent ensemble après un premier échange. En Belgique et au Luxembourg, en français, en néerlandais ou en anglais.",
    cols: ["Format", "Ce que vous obtenez", "Quand le choisir"],
    rows: [
      ["Mission de conseil", "Un rôle clair au sein de vos équipes, en direct ou via votre cabinet référencé.", "Quand il faut une expertise présente dans la durée."],
      ["Forfait à livrable", "Un périmètre, un livrable et un budget validés avant de commencer.", "Quand l'objectif est net : une cible, une intégration, une mise en production."],
      ["Renfort de programme", "Une phase critique tenue avec votre équipe, en construisant avec elle.", "Pour reprendre un programme, passer en production ou organiser le transfert."],
    ],
    terms: [
      ["Confidentialité", "Accord de confidentialité signé avant l'échange si vous le souhaitez."],
      ["Continuité", "Documentation au fil de l'eau et transfert prévu dès le départ."],
      ["Propriété", "Vos accès, votre code et votre documentation restent chez vous."],
    ],
  },
  quotesTitle: "Ce qu'en disent nos clients.",
  film: { pause: "Pause", play: "Lecture", hint: " du film de fond" },
  // description de l'entreprise dans les données structurées (JSON-LD), dans la langue de la page
  orgDescription: "Société de conseil et d'ingénierie fondée en 2005 à Wavre (Belgique), active en Belgique et au Luxembourg : Forward Deployed Engineering, GEO (référencement dans les assistants IA), architecture d'entreprise et de solutions, pilotage de programmes et digitalisation, de la cible à la mise en production, pour les PME et les grands groupes.",
  catalog: "Métiers de Clixite",
  slogan: "Nous résolvons votre x.",
  markdown: "Version Markdown",
  notFound: {
    title: "Page introuvable | Clixite",
    description: "Cette page n'existe pas ou plus.",
  },
};
export default common;
