// Home: film, logo's, Forward Deployed Engineering, GEO, expertises, werkwijze.
import type { Home } from "../fr/home";
import { routesFor } from "../routes";
const r = routesFor("nl");

const home: Home = {
  title: "Forward Deployed Engineering en GEO in België | Clixite",
  description: "Forward Deployed Engineering, GEO, architectuur, programma's en digitalisering: Clixite bouwt uw oplossingen in uw teams, in België en Luxemburg.",
  hero: {
    // hoofdstukken van de lus (11,5 s): de titels van de film, op het ritme van de shots
    story: [
      { t: "Uw architectuur begint op papier.", from: 0 },
      { t: "Ze krijgt diepte.", from: 2.5 },
      { t: "Ze landt bij u.", from: 5.5 },
      { t: "En ze draait.", from: 8.5 },
    ],
    h1: ["Wij lossen uw ", "x", " op."],
    sub: "Forward Deployed Engineering, GEO, enterprise- en solution-architectuur, programmamanagement, digitalisering. In uw teams, in België en Luxemburg, tot in productie.",
    cta2: { t: "Forward Deployed Engineering", href: r.fde },
  },
  refs: {
    title: "Waar we gewerkt hebben.",
    note: "Telecom, bankwezen, verzekeringen, bouw, makelaardij, kmo's: zeer verschillende omgevingen, in opdracht, als consultant of in vaste dienst. De projecten zelf blijven vertrouwelijk.",
  },
  fde: {
    title: "Forward Deployed Engineering.",
    lead: "Clixite gaat aan de slag in uw teams om uw integraties, automatiseringen en AI-agents te ontwerpen, te bouwen en in productie te brengen, en draagt de oplossing daarna aan u over. In België en Luxemburg, in het Nederlands, Frans of Engels.",
    btn: "Forward Deployed Engineering in detail",
    items: [
      { t: "In uw teams, niet ernaast.", d: "Ter plaatse of op afstand, in uw tools en in uw tempo. Beslissingen vallen waar het werk gebeurt." },
      { t: "In productie, niet in PowerPoint.", d: "De opdracht wordt afgemeten aan wat draait: een integratie, een geautomatiseerd proces, een AI-agent die op maandagochtend gebruikt wordt." },
      { t: "Onder uw controle, daarna bij u.", d: "Uw omgevingen, uw beveiligingsregels, persoonsgebonden toegangsrechten. Aan het einde blijven de code, de documentatie en de knowhow bij u." },
    ],
  },
  geo: {
    title: "GEO: het antwoord zijn dat AI-assistenten geven.",
    lead: "Uw klanten zoeken niet meer alleen op Google. Ze vragen ChatGPT, Claude, Perplexity, Gemini of Copilot wie hen kan helpen. Wij werken eraan dat de assistenten u vinden en u correct beschrijven.",
    btn: "GEO in detail",
    items: [
      { t: "Meten", d: "De vragen die uw klanten stellen, getest op de belangrijkste assistenten: wie wordt vermeld, en met welke informatie." },
      { t: "Structureren", d: "Een coherente entiteit, pagina's die antwoorden geven en gestructureerde data die klopt: uw site wordt citeerbaar." },
      { t: "Publiceren en opvolgen", d: "Bedrijfsfiches, profielen, open databanken, vermeldingen bij derden, en daarna regelmatige tests: de assistenten toetsen hun bronnen aan elkaar voor ze een bedrijf vermelden." },
    ],
  },
  expertises: {
    title: "Vijf expertises, één maatstaf: een resultaat dat draait.",
    lead: "Wij gaan aan de slag waar een strategie een werkend systeem moet worden, in een kmo net zo goed als in een gereguleerde groep.",
  },
  method: {
    title: "Van opmeting tot ingebruikname.",
    lead: "Vier stappen, elk met een oplevering die u behoudt, ook als u daar stopt. U beslist over de volgende stap op basis van wat op tafel ligt.",
    steps: [
      { t: "Opmeten", d: "Uw systemen, stromen, contracten en risico's in kaart gebracht. We meten voor we tekenen.", out: "Diagnose" },
      { t: "Ontwerpen", d: "De doelarchitectuur en de weg ernaartoe, in becijferde opties. Wat we behouden, wat we vervangen, wat we stopzetten.", out: "Doelarchitectuur en roadmap" },
      { t: "Bouwen", d: "Integraties, data, automatiseringen en AI, opgeleverd in korte incrementen die uw teams in de praktijk testen.", out: "Incrementen in productie" },
      { t: "In gebruik nemen", d: "Uitrol, adoptie en overdracht. Wij vertrekken wanneer uw teams de oplossing zelfstandig draaiende houden.", out: "Oplossing in gebruik en gedocumenteerd" },
    ],
  },
};
export default home;
