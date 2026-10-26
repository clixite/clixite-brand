// Gemeenschappelijke teksten voor alle pagina's (kop, voettekst, contact, samenwerkingsvormen, labels).
// Clixite-stijl: u-vorm, korte zinnen, geen gedachtestreepjes, geen cijfers, prijzen of looptijden.
import type { Common } from "../fr/common";
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("nl");
const a = anchorsFor("nl");

const common: Common = {
  lang: "nl",
  skip: "Naar de inhoud",
  ogAlt: "Wij lossen uw x op. Clixite: Forward Deployed Engineering, GEO, enterprise- en solution-architectuur, programmamanagement, digitalisering.",
  // scheidingsteken voor de dubbele punt (in het Nederlands zonder spatie)
  colon: ":",
  countries: { BE: "België", LU: "Luxemburg" } as Record<string, string>,
  country: "België",
  header: {
    home: "Clixite, home",
    main: "Hoofdnavigatie",
    mobile: "Mobiele navigatie",
    menu: "Menu",
    open: "Menu openen",
    cta: "Een gesprek aanvragen",
    ctaShort: "Contact",
    contact: "Contact",
    languages: "Taal",
    nav: [
      { href: r.fde, label: "Forward Deployed Engineering" },
      { href: r.geo, label: "GEO" },
      { href: r.expertises, label: "Expertises" },
      { href: `${r.home}#${a.method}`, label: "Werkwijze" },
      { href: `${r.home}#${a.refs}`, label: "Referenties" },
    ],
  },
  footer: {
    contact: "Contact",
    expertise: "Expertises",
    info: "Informatie",
    achats: "Aankooptransformatie",
    about: "Over Clixite",
    contactPage: "Contact",
    legal: "Juridische informatie en privacy",
    charte: "Huisstijl",
    llms: "Samenvatting voor AI-assistenten",
    legalLine: "besloten vennootschap. Zetel:",
    vat: "KBO en btw",
    rpm: "RPR Waals-Brabant",
    since: "© 2005 tot",
  },
  crumbs: { label: "Kruimelpad", home: "Home", expertises: "Expertises" },
  faqTitle: "Veelgestelde vragen.",
  others: "Onze andere expertises",
  deliverable: "Oplevering",
  updated: "Bijgewerkt op 26 oktober 2026",
  cta: "Een gesprek aanvragen",
  sources: "Bronnen",
  source: "Bron",
  copy: { copy: "E-mailadres kopiëren", ok: "E-mailadres gekopieerd", sel: "E-mailadres geselecteerd" },
  booking: {
    subject: "Eerste gesprek met Clixite",
    body: "Goedendag,\n\nOnze uitdaging, in twee zinnen:\n\n\nBeschikbaarheid:\n",
  },
  final: {
    title: ["Wat is uw ", "x", "?"],
    lead: "Een eerste gesprek volstaat om hem te benoemen. U krijgt een eerste aanzet mee, ook als we niet samenwerken.",
    mail: "Of schrijf rechtstreeks naar",
    tel: "Of bel",
    meet: "Afspraak in Waver, bij u of via videogesprek.",
  },
  formats: {
    title: "Samenwerken.",
    lead: "Scope, looptijd en budget leggen we samen vast na een eerste gesprek. In België en Luxemburg, in het Nederlands, Frans of Engels.",
    cols: ["Formule", "Wat u krijgt", "Wanneer kiezen"],
    rows: [
      ["Consultancyopdracht", "Een duidelijke rol in uw teams, rechtstreeks of via een consultancybureau op uw leverancierslijst.", "Wanneer u expertise nodig hebt die langere tijd aanwezig blijft."],
      ["Vaste prijs per oplevering", "Een scope, een oplevering en een budget, goedgekeurd voor de start.", "Wanneer het doel helder is: een doelarchitectuur, een integratie, een oplossing in productie."],
      ["Programmaversterking", "Een kritieke fase die we samen met uw team in goede banen leiden, terwijl we mee bouwen.", "Om een programma over te nemen, in productie te gaan of de overdracht te organiseren."],
    ],
    terms: [
      ["Vertrouwelijkheid", "Op uw verzoek een geheimhoudingsovereenkomst, ondertekend voor het gesprek."],
      ["Continuïteit", "Doorlopende documentatie en een overdracht die van bij de start gepland is."],
      ["Eigendom", "Uw toegangsrechten, uw code en uw documentatie blijven bij u."],
    ],
  },
  quotesTitle: "Wat onze klanten zeggen.",
  film: { pause: "Pauzeren", play: "Afspelen", hint: " van de achtergrondfilm" },
  // beschrijving van het bedrijf in de gestructureerde data (JSON-LD), in de taal van de pagina
  orgDescription: "Consultancy- en engineeringbedrijf, opgericht in 2005 in Waver (België), actief in België en Luxemburg: Forward Deployed Engineering, GEO (vindbaarheid in AI-assistenten), enterprise- en solution-architectuur, programmamanagement en digitalisering, van doelarchitectuur tot productie, voor kmo's en grote groepen.",
  catalog: "Expertises van Clixite",
  slogan: "Wij lossen uw x op.",
  markdown: "Markdown-versie",
  notFound: {
    title: "Pagina niet gevonden | Clixite",
    description: "Deze pagina bestaat niet of niet meer.",
  },
};
export default common;
