// Text shared by every page (header, footer, contact, ways of working, labels), in British English.
// Clixite voice: address the reader as "you", short sentences, no long dashes, no figures, prices or durations.
import type { Common } from "../fr/common";
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("en");
const a = anchorsFor("en");

const common: Common = {
  lang: "en",
  skip: "Skip to content",
  ogAlt: "We solve your x. Clixite: Forward Deployed Engineering, GEO, enterprise and solution architecture, programme management, digitalisation.",
  // separator before a colon (no space in English)
  colon: ":",
  countries: { BE: "Belgium", LU: "Luxembourg" } as Record<string, string>,
  country: "Belgium",
  header: {
    home: "Clixite, home",
    main: "Main navigation",
    mobile: "Mobile navigation",
    menu: "Menu",
    open: "Open the menu",
    cta: "Request a conversation",
    ctaShort: "Contact",
    contact: "Contact",
    languages: "Language",
    nav: [
      { href: r.fde, label: "Forward Deployed Engineering" },
      { href: r.geo, label: "GEO" },
      { href: r.expertises, label: "Expertise" },
      { href: `${r.home}#${a.method}`, label: "Method" },
      { href: `${r.home}#${a.refs}`, label: "References" },
    ],
  },
  footer: {
    contact: "Contact",
    expertise: "Expertise",
    info: "Information",
    achats: "Procurement transformation",
    about: "About Clixite",
    contactPage: "Contact",
    legal: "Legal notice and privacy",
    charte: "Brand guidelines",
    llms: "Summary for AI assistants",
    legalLine: "private limited company. Registered office:",
    vat: "Company and VAT number",
    rpm: "RLE Walloon Brabant",
    since: "© 2005 to",
  },
  crumbs: { label: "Breadcrumb", home: "Home", expertises: "Expertise" },
  faqTitle: "Frequently asked questions.",
  others: "Our other services",
  deliverable: "Deliverable",
  updated: "Updated 26 October 2026",
  cta: "Request a conversation",
  sources: "Sources",
  source: "Source",
  copy: { copy: "Copy address", ok: "Address copied", sel: "Address selected" },
  booking: {
    subject: "First conversation with Clixite",
    body: "Hello,\n\nOur challenge, in two sentences:\n\n\nAvailability:\n",
  },
  final: {
    title: ["What is your ", "x", "?"],
    lead: "One conversation is enough to name it. You leave with a first way forward, even if we do not end up working together.",
    mail: "Or write directly to",
    tel: "Or call",
    meet: "We meet in Wavre, at your premises or by video call.",
  },
  formats: {
    title: "Working together.",
    lead: "Scope, duration and budget are set together after a first conversation. In Belgium and Luxembourg, in English, French or Dutch.",
    cols: ["Format", "What you get", "When to choose it"],
    rows: [
      ["Consulting assignment", "A clear role inside your teams, directly or through your preferred supplier.", "When you need expertise on hand over time."],
      ["Fixed-scope delivery", "A scope, a deliverable and a budget agreed before we start.", "When the goal is clear: a target architecture, an integration, a go-live."],
      ["Programme reinforcement", "A critical phase held together with your team, building alongside it.", "To recover a programme, go to production or organise the handover."],
    ],
    terms: [
      ["Confidentiality", "A non-disclosure agreement signed before we talk, if you wish."],
      ["Continuity", "Documentation as we go and a handover planned from day one."],
      ["Ownership", "Your access, your code and your documentation stay with you."],
    ],
  },
  quotesTitle: "What our clients say.",
  film: { pause: "Pause", play: "Play", hint: " the background video" },
  // company description in the structured data (JSON-LD), in the language of the page
  orgDescription: "Consulting and engineering company founded in 2005 in Wavre (Belgium), working in Belgium and Luxembourg: Forward Deployed Engineering, GEO (visibility in AI assistants), enterprise and solution architecture, programme management and digitalisation, from target to production, for SMEs and large enterprises.",
  catalog: "Clixite services",
  slogan: "We solve your x.",
  markdown: "Markdown version",
  notFound: {
    title: "Page not found | Clixite",
    description: "This page does not exist, or no longer does.",
  },
};
export default common;
