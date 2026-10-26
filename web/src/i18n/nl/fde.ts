// Pijlerpagina Forward Deployed Engineering. U-vorm, geen cijfers of projectdetails, geen onverifieerbare
// beloften; bronnen vermeld voor de oorsprong van het model. Dezelfde structuur in de drie talen.
import type { Fde } from "../fr/fde";
import { SOURCES } from "../sources";

const fde: Fde = {
  title: "Forward Deployed Engineering in België en Luxemburg | Clixite",
  description: "Ingenieurs in uw teams ontwerpen uw integraties, automatiseringen en AI-agents, brengen ze in productie en dragen alles aan u over. In België en Luxemburg.",
  h1: ["Forward Deployed Engineering: ", "bouwen in uw teams, tot in productie."],
  chapo: "Forward Deployed Engineering (FDE) is een werkwijze waarbij ingenieurs in de teams van een klant een oplossing op diens systemen ontwerpen, bouwen en in productie brengen, en die daarna aan de klant overdragen. In België en Luxemburg past Clixite dit model toe op integraties, automatisering en AI, binnen het kader van DORA, NIS2, de GDPR en de AI Act.",
  cta: "Een gesprek aanvragen", cta2: "De werkwijze bekijken", updated: "Bijgewerkt op 26 oktober 2026",
  what: {
    h: "Wat is Forward Deployed Engineering?",
    p: [
      "Een Forward Deployed Engineer is een ingenieur die bij de klant werkt, zo dicht mogelijk bij de mensen die het systeem gebruiken. Hij begrijpt de business, ontwerpt, codeert, integreert en rolt uit, en draagt daarna over wat hij gebouwd heeft. De term blijft Engels, in het Nederlands net als in het Frans; soms spreekt men van een ingenieur die bij de klant wordt ingezet.",
      "Het is geen consultancy die ophoudt bij een aanbeveling, en ook geen regie die taken uitvoert: de Forward Deployed Engineer staat in voor een resultaat dat samen met u is vastgelegd, een oplossing die draait in uw omgeving.",
    ],
  },
  origin: {
    h: "Waar het model vandaan komt",
    p: "Het model werd geformaliseerd door Palantir, dat zijn productontwikkelaars onderscheidt van zijn ingenieurs die bij de klant worden ingezet, samengevat in één formule: één klant, veel capaciteiten. Sindsdien hebben AI-bedrijven het overgenomen om hun klanten van prototype naar productie te brengen, tot het een van de meest gezochte profielen in de sector werd.",
    src: [{ t: "Palantir, “Dev versus Delta”", href: SOURCES.palantir }, { t: "TechCrunch, 30 juli 2026", href: SOURCES.techcrunch }],
    srcLabel: "Bronnen",
  },
  when: {
    h: "Wanneer u een Forward Deployed Engineer inschakelt",
    items: [
      "Een AI-prototype werkt in een demo, maar is nooit in productie gegaan.",
      "Uw systemen praten niet met elkaar: ERP, CRM, aankooptool en bedrijfsdata moeten betrouwbaar gekoppeld worden.",
      "Een proces dat nog manueel verloopt, moet geautomatiseerd worden zonder te breken wat draait.",
      "Een programma loopt achter en er zijn evenveel handen nodig als stuurcomités.",
      "Uw omgeving is gereguleerd en niets mag uw organisatie verlaten.",
      "Uw team moet groeien in competenties, tot het een eigen FDE-capaciteit kan opbouwen.",
    ],
  },
  method: {
    h: "Onze werkwijze, in vier stappen",
    lead: "Elke stap levert iets op dat u behoudt. U beslist over de volgende op basis van wat op tafel ligt.",
    steps: [
      { t: "Instappen", d: "Toegangsrechten, omgevingen, beveiligingsregels en aanspreekpunten: wij werken van bij de start in uw tools en met uw teams.", out: "Gevalideerd werkkader" },
      { t: "Bouwen", d: "Een prototype op uw echte data, getest met wie het zal gebruiken en verbeterd in korte incrementen.", out: "Bewezen prototype" },
      { t: "In productie brengen", d: "Beveiliging, monitoring, documentatie en beheerprocedures: de oplossing gaat in productie volgens uw regels.", out: "Oplossing in productie" },
      { t: "Overdragen", d: "Code, toegangsrechten, documentatie en opleiding: wij vertrekken wanneer uw teams de oplossing zelfstandig beheren en verder ontwikkelen.", out: "Zelfstandige teams" },
    ],
    outLabel: "Oplevering",
  },
  compare: {
    h: "FDE, consultancy of regie: wat is het verschil?",
    cols: ["", "Rol", "Wat u krijgt", "Einde van de opdracht"],
    rows: [
      ["Forward Deployed Engineering", "Bouwt en brengt in productie, in uw teams.", "Een oplossing in productie, gedocumenteerd en overgedragen.", "Wanneer uw teams ze zelfstandig beheren."],
      ["Klassieke consultancy", "Analyseert en adviseert.", "Een rapport, een doelarchitectuur, een roadmap.", "Zodra de oplevering overhandigd is."],
      ["IT-dienstverlener of regie", "Voert de taken uit die u aanstuurt.", "Tijd, met een middelenverbintenis.", "Op de einddatum van het contract; een overdracht is niet automatisch inbegrepen."],
    ],
    note: "Het verschil zit in het mandaat, niet in het contract: een Forward Deployed Engineer kan zowel via een consultancyopdracht als tegen een vaste prijs ingezet worden.",
  },
  regulated: {
    h: "Forward Deployed Engineering in een gereguleerde omgeving",
    lead: "Banken, verzekeraars, essentiële entiteiten: DORA, NIS2, de GDPR en de AI Act gelden ook voor wat men bouwt. Het kader wordt van bij de start vastgelegd.",
    items: [
      { t: "Uw omgevingen", d: "Niets wordt buiten uw perimeter gebouwd zonder schriftelijk akkoord." },
      { t: "Persoonsgebonden toegangsrechten", d: "Traceerbaar, beperkt tot het nodige, ingetrokken op het einde van de opdracht." },
      { t: "Uw gegevens blijven bij u", d: "Over het gebruik van AI-tools beslissen we samen met u, tool per tool." },
      { t: "Documentatie klaar voor de audit", d: "Architectuur, keuzes, risico's, beheerprocedures." },
      { t: "AI onder menselijk toezicht", d: "Supervisie, logging en documentatie, zoals de AI Act eist voor de betrokken systemen." },
    ],
  },
  keep: {
    h: "Wat u behoudt",
    p: "De code, de toegangsrechten, de documentatie en opgeleide teams. En als u dat wenst, de opbouw van uw eigen interne FDE-team: rollen, methodes, rekrutering.",
  },
  faqTitle: "Veelgestelde vragen over Forward Deployed Engineering.",
  faq: [
    { q: "Wat is een Forward Deployed Engineer?", a: "Een Forward Deployed Engineer is een ingenieur die in de teams van een klant werkt en een behoefte omzet in een oplossing die in gebruik is. Hij begrijpt de business, ontwerpt, codeert, integreert, rolt uit en draagt daarna over. Het model werd geformaliseerd door Palantir." },
    { q: "Wat is het verschil met een consultant?", a: "De consultant adviseert, de Forward Deployed Engineer bouwt. Zijn opdracht eindigt wanneer uw teams de oplossing beheren, niet bij de overhandiging van een rapport." },
    { q: "Is het regie onder een andere naam?", a: "Nee. In regie stuurt u een resource taak per taak aan. De Forward Deployed Engineer staat in voor een resultaat dat samen met u is vastgelegd: een oplossing in productie, gedocumenteerd en overgedragen." },
    { q: "Moet het om een AI-project gaan?", a: "Nee. Het model werkt ook om systemen te koppelen, een proces te automatiseren of een programma over te nemen. AI is slechts een van de meest voorkomende toepassingen." },
    { q: "Is dit verenigbaar met DORA, NIS2, de GDPR en de AI Act?", a: "Ja, als het kader van bij de start vastligt: uw omgevingen, uw beveiligingsregels, persoonsgebonden toegangsrechten en gegevens die bij u blijven." },
    { q: "Wat behoudt de onderneming op het einde?", a: "De code, de toegangsrechten, de documentatie en teams die opgeleid zijn om de oplossing te beheren en verder te ontwikkelen." },
    { q: "Waar en in welke talen werkt u?", a: "In België en Luxemburg, in het Nederlands, Frans of Engels, ter plaatse of op afstand." },
  ],
  schema: {
    alternateName: ["FDE", "Forward Deployed Engineer", "Ingenieur ingezet bij de klant"],
    serviceType: ["Forward Deployed Engineering", "Systeemintegratie", "Procesautomatisering", "AI in productie brengen", "AI-agents"],
    term: "Engineeringmodel waarbij ingenieurs in de teams van een klant een oplossing op diens systemen ontwerpen, bouwen en in productie brengen, en die daarna aan de klant overdragen.",
  },
};
export default fde;
