// Inhoud van de expertisepagina's (GEO, architectuur, programmamanagement, digitalisering), weergegeven door components/MetierPage.astro.
// U-vorm; geen prijzen, looptijden of projectdetails; alleen verifieerbare feiten (data, certificeringen, bronnen). De zichtbare FAQ voeden de FAQPage-markup.
import type { PageMetier } from "../fr/pages";
import { routesFor } from "../routes";
import { SOURCES } from "../sources";
const r = routesFor("nl");

const pages: PageMetier[] = [
  {
    slug: "geo", key: "geo", path: r.geo, crumb: "GEO",
    title: "GEO: vindbaar in ChatGPT en andere AI-assistenten | Clixite",
    description: "GEO maakt uw bedrijf begrijpelijk en citeerbaar voor ChatGPT, Claude, Perplexity en Google: audit, structurering en opvolging, in België en Luxemburg.",
    h1: ["GEO: ", "het antwoord zijn dat AI-assistenten geven."],
    chapo: "GEO (Generative Engine Optimization) is een werkwijze om een bedrijf begrijpelijk, verifieerbaar en citeerbaar te maken voor antwoordmachines: ChatGPT, Claude, Perplexity, Gemini, Copilot en de AI-overzichten van Google. Clixite meet uw zichtbaarheid, structureert uw inhoud en uw data, en verhelpt wat assistenten ervan weerhoudt u te vermelden, in België en Luxemburg.",
    photo: "archives-45",
    alternateName: ["Generative Engine Optimization", "Vindbaarheid in AI-assistenten", "Optimalisatie voor generatieve zoekmachines"],
    serviceType: ["Generative Engine Optimization", "Zoekmachineoptimalisatie", "Gestructureerde data", "Audit van de zichtbaarheid in AI-assistenten"],
    blocs: [
      { id: "geo-seo", h: "GEO en SEO: wat is het verschil?", kind: "prose", p: [
        "SEO mikt op een positie in een lijst met links. GEO mikt op een plaats in het antwoord dat de assistent opstelt, met uw site als bron.",
        "De twee vullen elkaar aan. Antwoordmachines steunen grotendeels op pagina's die al goed vindbaar zijn in zoekmachines, maar ze lezen anders: ze zoeken heldere definities, verifieerbare feiten en bronnen die elkaar bevestigen.",
      ], src: [{ t: "Aggarwal et al., “GEO: Generative Engine Optimization”, 2023", href: SOURCES.geoPaper }] },
      { id: "geo-criteres", h: "Wat ervoor zorgt dat een assistent u vermeldt", kind: "defs", band: true, lead: "Wat we vandaag weten, en wat we voor elke klant meten.", defs: [
        { t: "Een eenduidige entiteit", d: "Dezelfde naam, hetzelfde adres, dezelfde expertises overal: ondernemingsregister, website, LinkedIn, bedrijvengidsen, Wikidata." },
        { t: "Pagina's die antwoorden", d: "Een definitie in enkele zinnen, zichtbare veelgestelde vragen, eerlijke vergelijkingen, gedateerde pagina's." },
        { t: "Gestructureerde data die klopt", d: "Een schema.org-markup die precies beschrijft wat de pagina toont, en een site die leesbaar is voor de crawlers van de assistenten." },
        { t: "Vermeldingen buiten uw eigen site", d: "Pers, vakgidsen, open databanken: de assistenten toetsen hun bronnen aan elkaar voor ze een bedrijf vermelden." },
      ] },
      { id: "geo-methode", h: "Onze aanpak, in vier stappen", kind: "steps", lead: "Elke stap levert iets op dat u behoudt.", steps: [
        { t: "Meten", d: "De vragen die uw klanten stellen, getest op de belangrijkste assistenten: wie wordt vermeld, met welke informatie, en uit welke bron.", out: "Audit van uw AI-zichtbaarheid" },
        { t: "Structureren", d: "Entiteit, gestructureerde data, definitiepagina's, veelgestelde vragen, regels voor crawlers: de site wordt leesbaar en citeerbaar.", out: "Site klaar voor antwoordmachines" },
        { t: "Publiceren", d: "Referentie-inhoud, bedrijfsfiches, professionele profielen, Wikidata: uw aanwezigheid buiten uw site wordt op één lijn gebracht.", out: "Afgestemde aanwezigheid bij derden" },
        { t: "Opvolgen", d: "Search Console, Bing Webmaster Tools en regelmatige tests van de assistenten: we meten de vermeldingen en sturen bij.", out: "Opvolgingsdashboard" },
      ] },
      { id: "geo-garantie", h: "Wat niemand kan garanderen", kind: "note", encre: true, p: [
        "Geen enkele dienstverlener kan een positie in Google of een vermelding door een assistent garanderen: de modellen veranderen, hun bronnen ook.",
        "Waar wij ons wel toe verbinden, is meetbaar werk: een site die crawlbaar is, geldige en coherente data, een afgestemde aanwezigheid en regelmatige tests om te zien wat beweegt. Deze site past dat zelf toe: een entiteit beschreven in gestructureerde data, definitiepagina's, zichtbare veelgestelde vragen, een samenvatting voor de assistenten.",
      ] },
      { id: "geo-pour-qui", h: "Voor wie", kind: "list", items: [
        "Kmo's en vrije beroepen waarvan de klanten zich eerst zelf informeren voor ze bellen.",
        "Groepen die willen dat de assistenten hun aanbod, hun merken en hun verplichtingen correct beschrijven.",
        "Software- en dienstenbedrijven waarvan de naam moet opduiken wanneer iemand een assistent om een oplossing vraagt.",
        "Elk bedrijf dat in meerdere talen actief is: de assistenten antwoorden in de taal van de vraag.",
      ] },
    ],
    faq: [
      { q: "Wat is GEO?", a: "Generative Engine Optimization (GEO) maakt een bedrijf begrijpelijk, verifieerbaar en citeerbaar voor antwoordmachines, zoals ChatGPT, Claude, Perplexity, Gemini, Copilot en de AI-overzichten van Google." },
      { q: "Is SEO nog nuttig?", a: "Ja. Antwoordmachines steunen grotendeels op de index van de zoekmachines. Goede SEO blijft de basis; GEO voegt toe wat inhoud citeerbaar maakt." },
      { q: "Kan een vermelding door ChatGPT gegarandeerd worden?", a: "Nee. Niemand kan een vermelding door ChatGPT garanderen: wees op uw hoede voor wie dat belooft. Wat wel kan: uw zichtbaarheid meten, verhelpen wat in uw nadeel speelt en de evolutie van de vermeldingen opvolgen." },
      { q: "Volstaat een llms.txt-bestand?", a: "Nee. Een llms.txt-bestand helpt sommige tools om een site samen te vatten, maar de belangrijkste assistenten lezen het vandaag weinig. Wij zetten het op zonder er wonderen van te verwachten." },
      { q: "Moet u uw website herbouwen?", a: "Zelden. De meeste GEO-correcties gaan over de inhoud, de gestructureerde data en de aanwezigheid buiten de site." },
      { q: "In welke talen werkt u?", a: "Clixite werkt in het Nederlands, het Frans en het Engels. De assistenten antwoorden in de taal van de vraag: u moet in elke taal aanwezig zijn." },
    ],
  },
  {
    slug: "architecture-entreprise-solutions", key: "archi", path: r.archi, crumb: "Enterprise- en solution-architectuur",
    title: "Enterprise- en solution-architectuur in België | Clixite",
    description: "Uw informatiesysteem in kaart, een doelarchitectuur, een traject in opties en de keuze van oplossingen, tot in productie. In België en Luxemburg.",
    h1: ["Enterprise- en solution-architectuur: ", "beslissen waar uw informatiesysteem naartoe gaat."],
    chapo: "Enterprise-architectuur verbindt de strategie met het informatiesysteem: wat u hebt, wat u nastreeft en de weg daartussen. Solution-architectuur kiest en ontwerpt de tools die u daar brengen. Clixite doet beide, van het in kaart brengen tot de ingebruikname, voor kmo's en voor gereguleerde groepen, in België en Luxemburg.",
    photo: "aiguillage-45",
    serviceType: ["Enterprise-architectuur", "Solution-architectuur", "In kaart brengen van het informatiesysteem", "Architectuurreview"],
    blocs: [
      { id: "archi-quand", h: "Wanneer u ons inschakelt", kind: "list", items: [
        "Uw applicaties hebben zich opgestapeld en niemand heeft nog het overzicht.",
        "Er staat een grote keuze voor de deur: ERP, CRM, aankooptool, cloud, dataplatform.",
        "Een fusie, een splitsing of een reorganisatie schudt de kaarten opnieuw.",
        "Een toezichthouder of een auditor vraagt een helder overzicht van uw systemen en uw kritieke leveranciers.",
        "Een AI-project moet zijn plaats vinden in het bestaande landschap.",
      ] },
      { id: "archi-obtenez", h: "Wat u krijgt", kind: "defs", band: true, defs: [
        { t: "Een kaart van uw IT-landschap", d: "Applicaties, data, stromen, contracten en kritieke leveranciers, op een kaart die uw teams kunnen lezen." },
        { t: "Een doelarchitectuur", d: "Principes, bouwstenen, integraties en beveiliging: waar u naartoe gaat, en waarom." },
        { t: "Een traject in opties", d: "Wat we behouden, wat we vervangen, wat we stopzetten; elke optie met haar kosten, risico's en afhankelijkheden." },
        { t: "Externe architectuurreviews", d: "Een externe, onderbouwde blik op een oplossingskeuze of een architectuurdossier, voor de beslissing duur uitvalt." },
      ] },
      { id: "archi-suite", h: "Van doelarchitectuur tot productie", kind: "prose", p: [
        "Een doelarchitectuur heeft pas waarde als ze gebouwd wordt. Zodra ze gevalideerd is, kunnen wij ze met uw teams realiseren, via Forward Deployed Engineering, en het programma leiden dat erbij hoort.",
      ], link: { t: "Forward Deployed Engineering", href: r.fde } },
    ],
    faq: [
      { q: "Wat is het verschil tussen enterprise-architectuur en solution-architectuur?", a: "Enterprise-architectuur beslist over het geheel: business, data, applicaties, technologie, en het traject tussen vandaag en de doelarchitectuur. Solution-architectuur ontwerpt een concrete oplossing binnen dat kader, tot en met de integraties en de beveiliging." },
      { q: "Heeft een kmo enterprise-architectuur nodig?", a: "Ja, op haar eigen schaal. Een duidelijke kaart van uw tools en uw stromen voorkomt overbodige aankopen en bereidt de groei voor. Voor een kmo blijft het werk beperkt tot enkele korte opleveringen." },
      { q: "Volgt u een methodologisch kader?", a: "Wij gebruiken de begrippen uit erkende kaders wanneer ze nuttig zijn, zonder zwaar formalisme op te leggen: wat wij aan architectuur opleveren, moet door uw teams gelezen en gebruikt worden." },
      { q: "Kunt u de doelarchitectuur ook bouwen?", a: "Ja, via Forward Deployed Engineering: wij gaan aan de slag in uw teams om in productie te brengen wat beslist is, en dragen het daarna over." },
    ],
  },
  {
    slug: "pilotage-de-programmes", key: "pilotage", path: r.pilotage, crumb: "Programmamanagement",
    title: "Programmamanagement en verandermanagement | Clixite",
    description: "Governance, planning, budget, risico's en adoptie: uw programma's met meerdere teams strak geleid tot de ingebruikname, in België en Luxemburg.",
    h1: ["Programmamanagement: ", "programma's met meerdere teams, strak geleid tot de ingebruikname."],
    chapo: "Programmamanagement coördineert meerdere projecten die eenzelfde doel dienen: governance, planning, budget, risico's en verandermanagement. Clixite zet uw transformatieprogramma's op of neemt ze over, in België en Luxemburg, met erkende referentiekaders (PMP, PRINCE2, SAFe, Scrum, ADKAR) en één regel: beslissingen worden genomen op basis van feiten.",
    photo: "salle-45",
    serviceType: ["Programmamanagement", "Projectmanagement", "Verandermanagement", "Overname van lopende programma's"],
    blocs: [
      { id: "prog-quand", h: "Wanneer u ons inschakelt", kind: "list", items: [
        "Een programma loopt vertraging op of het budget ontspoort.",
        "Meerdere teams en meerdere leveranciers moeten in hetzelfde tempo vooruitgaan.",
        "De stuurcomités vergaderen, maar beslissen niet.",
        "Een kritieke overgang naar productie nadert.",
        "De gebruikers omarmen niet wat opgeleverd werd.",
      ] },
      { id: "prog-obtenez", h: "Wat u krijgt", kind: "defs", band: true, defs: [
        { t: "Een diagnose bij overname", d: "Waar het programma echt staat: scope, planning, budget, risico's en afhankelijkheden." },
        { t: "Een governance die beslist", d: "Stuurcomités, rollen en duidelijke beslisregels, dashboards die de besluitvorming ondersteunen." },
        { t: "Een plan dat standhoudt", d: "Mijlpalen, afhankelijkheden en risico's die op de voet gevolgd worden, met elk team en elke leverancier." },
        { t: "Meetbare verandering", d: "Opleiding, communicatie en adoptie, opgevolgd met indicatoren die bij de start zijn vastgelegd." },
      ] },
    ],
    faq: [
      { q: "Kunt u een lopend programma overnemen?", a: "Ja, dat komt vaak voor: een diagnose, een herstelplan en duidelijke keuzes, daarna aansturing dicht bij de teams." },
      { q: "Iteratieve methodes of V-model?", a: "Allebei, afhankelijk van de aard van het programma en uw randvoorwaarden: SAFe en Scrum voor product en software, PRINCE2 of PMP voor programma's met een zware governance, vaak een bewuste combinatie." },
      { q: "Werkt u samen met onze leveranciers en integratoren?", a: "Ja. Wij coördineren de interne teams en de leveranciers, met duidelijke afspraken voor elk van hen." },
      { q: "Hoe meet u de adoptie?", a: "Met indicatoren die bij de start zijn vastgelegd: werkelijk gebruik, supportaanvragen, kwaliteit van de ingevoerde gegevens, feedback van de gebruikers." },
    ],
  },
  {
    slug: "digitalisation", key: "digit", path: r.digit, crumb: "Digitalisering",
    title: "Digitalisering van processen en procesautomatisering | Clixite",
    description: "Eerst vereenvoudigen, dan digitaliseren: geautomatiseerde stromen, gekoppelde data en toegepaste AI, van kmo tot grote groep, in België en Luxemburg.",
    h1: ["Digitalisering van processen: ", "van papier en dubbele invoer naar gekoppelde tools."],
    chapo: "Digitalisering van processen vervangt papier, verspreide bestanden en dubbele invoer door digitale werkstromen en gekoppelde data. Clixite brengt uw processen in kaart en vereenvoudigt ze voor ze geautomatiseerd worden, en neemt ze daarna samen met uw teams in productie, van kmo's tot grote groepen, in België en Luxemburg.",
    photo: "fibres-45",
    serviceType: ["Digitalisering van processen", "Procesautomatisering", "CRM- en ERP-integratie", "Toegepaste AI"],
    blocs: [
      { id: "digit-quand", h: "Wanneer u ons inschakelt", kind: "list", items: [
        "Een proces draait nog op papier, in Excel of via e-mail.",
        "Dezelfde gegevens worden meermaals ingevoerd, in verschillende tools.",
        "Goedkeuringen raken zoek tussen mailboxen.",
        "De dashboards bestaan, maar niemand gebruikt ze.",
        "U wilt AI gebruiken, maar weet niet waar u moet beginnen.",
      ] },
      { id: "digit-obtenez", h: "Wat u krijgt", kind: "defs", band: true, defs: [
        { t: "Vereenvoudigde processen", d: "In kaart gebracht, ontdaan van overbodige stappen, met duidelijke regels, voordat ze digitaal ondersteund worden." },
        { t: "Geautomatiseerde stromen", d: "Formulieren, goedkeuringen, meldingen en integraties met uw CRM en uw ERP." },
        { t: "Gekoppelde data", d: "Eén keer invoeren, correcte referentiedata en dashboards die gebruikt worden." },
        { t: "Toegepaste AI", d: "Waar ze tijd bespaart, onder menselijk toezicht en conform de GDPR." },
      ] },
    ],
    faq: [
      { q: "Waar begint u het best?", a: "Bij het proces dat het lastigst is en het vaakst terugkomt. We vereenvoudigen het voor we het digitaal ondersteunen: een warrig proces automatiseren versnelt alleen de warboel." },
      { q: "Moet u van tools veranderen?", a: "Niet altijd. We benutten eerst wat u al hebt; een nieuwe tool is alleen verantwoord als hij beter werkt tegen redelijke kosten." },
      { q: "Welke plaats krijgt AI?", a: "Documenten lezen, aanvragen sorteren, antwoorden voorbereiden: daar bewijst AI goede diensten, onder menselijk toezicht en conform de GDPR." },
      { q: "Kunnen uw teams de werkstromen daarna zelf aanpassen?", a: "Ja. Documentatie en opleiding maken deel uit van elke opdracht, zodat uw teams zelfstandig blijven." },
    ],
  },
];
export default pages;
