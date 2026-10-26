// Les cinq métiers de Clixite, le Forward Deployed Engineering et le GEO en tête (les plus demandés),
// puis les domaines d'application. Source unique pour l'accueil, le hub, les pages métiers, le JSON-LD et llms.txt.
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("fr");
const a = anchorsFor("fr");

const metiers = {
  list: [
    {
      slug: "forward-deployed-engineering", key: "fde", href: r.fde, t: "Forward Deployed Engineering", court: "Forward Deployed Engineering",
      d: "Nous nous installons dans vos équipes pour concevoir, construire et mettre en production l'intégration, l'automatisation ou l'agent IA dont vous avez besoin, sur vos outils et selon vos règles de sécurité. Nous partons quand vos équipes exploitent la solution seules.",
      g: ["Un prototype éprouvé sur vos données réelles", "Une solution en production, surveillée et documentée", "Un transfert complet : code, accès, documentation, équipes formées"],
      k: "Intégration, automatisation, agents IA, mise en production, transfert",
      photo: "ingenieurs",
    },
    {
      slug: "geo", key: "geo", href: r.geo, t: "GEO : référencement dans les assistants IA", court: "GEO",
      d: "Quand vos clients demandent à ChatGPT, Claude, Perplexity, Gemini ou Copilot qui peut les aider, votre entreprise doit faire partie de la réponse. Nous rendons votre offre compréhensible, vérifiable et citable par les moteurs de réponse comme par Google.",
      g: ["Un audit de votre visibilité dans les assistants IA, question par question", "Des pages, des données structurées et une entité cohérentes, que les moteurs comprennent", "Une présence hors site alignée et un suivi des citations"],
      k: "GEO, SEO, données structurées, Wikidata, Search Console, Bing Webmaster Tools",
      photo: "archives",
    },
    {
      slug: "architecture-entreprise-solutions", key: "archi", href: r.archi, t: "Architecture d'entreprise et de solutions", court: "Architecture",
      d: "Savoir ce que vous avez, décider où vous allez et choisir les solutions qui vous y mènent, sans empiler les outils.",
      g: ["Cartographie des applications, des données et des flux", "Architecture cible et trajectoire en options chiffrées", "Choix de solutions et revues d'architecture extérieures"],
      k: "Cartographie, architecture cible, intégration, cloud",
      photo: "aiguillage",
    },
    {
      slug: "pilotage-de-programmes", key: "pilotage", href: r.pilotage, t: "Pilotage de programmes", court: "Pilotage de programmes",
      d: "Des programmes multi-équipes cadrés et tenus : une gouvernance claire, des risques suivis, des comités qui décident, des utilisateurs embarqués dès le premier jour.",
      g: ["Plan, budget et risques repris en main", "Gouvernance et comités qui tranchent", "Conduite du changement mesurée"],
      k: "PMP, PRINCE2, SAFe, Scrum, ADKAR",
      photo: "salle",
    },
    {
      slug: "digitalisation", key: "digit", href: r.digit, t: "Digitalisation", court: "Digitalisation",
      d: "Les processus papier, les doubles saisies et les fichiers éparpillés deviennent des outils reliés qui travaillent pour vos équipes.",
      g: ["Processus cartographiés et simplifiés avant d'être outillés", "Formulaires, flux et validations automatisés", "Données reliées entre vos outils, tableaux de bord utilisés"],
      k: "Automatisation, CRM et ERP, données, IA appliquée",
      photo: "fibres",
    },
  ],
  // domaines d'application : chacun avec une phrase et la page qui le traite
  domaines: {
    title: "Là où nos métiers s'appliquent.",
    lead: "Les mêmes méthodes, sur les sujets qui pèsent le plus dans les entreprises régulées comme dans les PME.",
    items: [
      { t: "Achats et Source-to-Pay", sub: "Fractional CPO, intérim, risques tiers",
        d: "Du besoin au paiement : des processus outillés, des risques fournisseurs maîtrisés, une direction des achats à temps partagé ou par intérim.",
        href: r.achats, l: "La transformation des achats" },
      { t: "Risques et conformité", sub: "DORA, NIS2, RGPD, AI Act",
        d: "Des obligations traduites en processus, en responsables et en preuves, dans ce que vous construisez comme dans ce que vous achetez.",
        href: `${r.fde}#${a.fdeRegulated}`, l: "Le FDE en environnement régulé" },
      { t: "IA en production", sub: "Agents, automatisations, intégrations",
        d: "Du prototype qui convainc en démonstration à l'agent IA qui tourne sur vos systèmes, sous contrôle humain.",
        href: r.fde, l: "Le Forward Deployed Engineering" },
      { t: "Produits numériques et SaaS", sub: "Architecture, intégrations, lancement",
        d: "L'architecture, les intégrations et la mise en production d'un produit numérique, jusqu'à ce que votre équipe le fasse évoluer seule.",
        href: r.archi, l: "L'architecture de solutions" },
    ],
  },
};
export type Metiers = typeof metiers;
export default metiers;
