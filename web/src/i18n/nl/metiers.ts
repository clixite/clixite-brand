// De vijf expertises van Clixite, met Forward Deployed Engineering en GEO voorop (het meest gevraagd),
// daarna de toepassingsdomeinen. Eén bron voor de home, de hub, de expertisepagina's, de JSON-LD en llms.txt.
import type { Metiers } from "../fr/metiers";
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("nl");
const a = anchorsFor("nl");

const metiers: Metiers = {
  list: [
    {
      slug: "forward-deployed-engineering", key: "fde", href: r.fde, t: "Forward Deployed Engineering", court: "Forward Deployed Engineering",
      d: "Wij gaan aan de slag in uw teams om de integratie, de automatisering of de AI-agent die u nodig hebt te ontwerpen, te bouwen en in productie te brengen, op uw tools en volgens uw beveiligingsregels. Wij vertrekken wanneer uw teams de oplossing zelfstandig beheren.",
      g: ["Een prototype dat zich bewezen heeft op uw echte data", "Een oplossing in productie, bewaakt en gedocumenteerd", "Een volledige overdracht: code, toegangsrechten, documentatie, opgeleide teams"],
      k: "Integratie, automatisering, AI-agents, in productie brengen, overdracht",
      photo: "ingenieurs",
    },
    {
      slug: "geo", key: "geo", href: r.geo, t: "GEO: vindbaarheid in AI-assistenten", court: "GEO",
      d: "Wanneer uw klanten ChatGPT, Claude, Perplexity, Gemini of Copilot vragen wie hen kan helpen, moet uw bedrijf deel uitmaken van het antwoord. Wij maken uw aanbod begrijpelijk, verifieerbaar en citeerbaar voor antwoordmachines en voor Google.",
      g: ["Een audit van uw zichtbaarheid in AI-assistenten, vraag per vraag", "Pagina's, gestructureerde data en een entiteit die op elkaar aansluiten en die zoekmachines begrijpen", "Een afgestemde aanwezigheid buiten uw site en opvolging van de vermeldingen"],
      k: "GEO, SEO, gestructureerde data, Wikidata, Search Console, Bing Webmaster Tools",
      photo: "archives",
    },
    {
      slug: "architecture-entreprise-solutions", key: "archi", href: r.archi, t: "Enterprise- en solution-architectuur", court: "Architectuur",
      d: "Weten wat u hebt, beslissen waar u naartoe gaat en de oplossingen kiezen die u daar brengen, zonder tools op te stapelen.",
      g: ["Uw applicaties, data en stromen in kaart gebracht", "Doelarchitectuur en traject in becijferde opties", "Keuze van oplossingen en externe architectuurreviews"],
      k: "Landschapskaart, doelarchitectuur, integratie, cloud",
      photo: "aiguillage",
    },
    {
      slug: "pilotage-de-programmes", key: "pilotage", href: r.pilotage, t: "Programmamanagement", court: "Programmamanagement",
      d: "Programma's met meerdere teams, goed afgebakend en in de hand gehouden: een duidelijke governance, opgevolgde risico's, stuurcomités die beslissen, gebruikers die vanaf dag één mee aan boord zijn.",
      g: ["Planning, budget en risico's opnieuw onder controle", "Governance en stuurcomités die knopen doorhakken", "Gemeten verandermanagement"],
      k: "PMP, PRINCE2, SAFe, Scrum, ADKAR",
      photo: "salle",
    },
    {
      slug: "digitalisation", key: "digit", href: r.digit, t: "Digitalisering", court: "Digitalisering",
      d: "Papieren processen, dubbele invoer en verspreide bestanden worden gekoppelde tools die voor uw teams werken.",
      g: ["Processen in kaart gebracht en vereenvoudigd, voordat ze digitaal ondersteund worden", "Formulieren, stromen en goedkeuringen geautomatiseerd", "Data gekoppeld tussen uw tools, dashboards die gebruikt worden"],
      k: "Automatisering, CRM en ERP, data, toegepaste AI",
      photo: "fibres",
    },
  ],
  // toepassingsdomeinen: elk met een zin en de pagina die het behandelt
  domaines: {
    title: "Waar onze expertises van toepassing zijn.",
    lead: "Dezelfde methodes, op de onderwerpen die het zwaarst wegen in gereguleerde ondernemingen en in kmo's.",
    items: [
      { t: "Aankoop en Source-to-Pay", sub: "Fractional CPO, interim, risico's van derden",
        d: "Van behoefte tot betaling: digitaal ondersteunde processen, beheerste leveranciersrisico's, een aankoopdirectie in deeltijd of ad interim.",
        href: r.achats, l: "Aankooptransformatie" },
      { t: "Risico's en compliance", sub: "DORA, NIS2, GDPR, AI Act",
        d: "Verplichtingen vertaald naar processen, verantwoordelijken en bewijzen, in wat u bouwt en in wat u aankoopt.",
        href: `${r.fde}#${a.fdeRegulated}`, l: "FDE in een gereguleerde omgeving" },
      { t: "AI in productie", sub: "Agents, automatiseringen, integraties",
        d: "Van het prototype dat overtuigt in een demo tot de AI-agent die op uw systemen draait, onder menselijk toezicht.",
        href: r.fde, l: "Forward Deployed Engineering" },
      { t: "Digitale producten en SaaS", sub: "Architectuur, integraties, lancering",
        d: "De architectuur, de integraties en het in productie brengen van een digitaal product, tot uw team het zelfstandig verder ontwikkelt.",
        href: r.archi, l: "Solution-architectuur" },
    ],
  },
};
export default metiers;
