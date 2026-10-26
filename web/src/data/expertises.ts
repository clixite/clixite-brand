// Les cinq métiers de Clixite, le Forward Deployed Engineering et le GEO en tête (les plus demandés).
// Source unique pour l'accueil, le hub /expertises/, les pages métiers, le JSON-LD et llms.txt.
import { FDE_PATH, GEO_PATH } from "./site";

export interface Metier {
  slug: string;
  href: string;
  t: string;          // nom du métier
  court: string;      // nom court (navigation, fil d'Ariane)
  d: string;          // description courte (accueil, hub)
  g: string[];        // ce que vous obtenez
  k: string;          // mots clés visibles
  photo: string;      // slug du registre photo
  photoAlt: string;
}

export const METIERS: Metier[] = [
  {
    slug: "forward-deployed-engineering", href: FDE_PATH, t: "Forward Deployed Engineering", court: "Forward Deployed Engineering",
    d: "Nous nous installons dans vos équipes pour concevoir, construire et mettre en production l'intégration, l'automatisation ou l'agent IA dont vous avez besoin, sur vos outils et selon vos règles de sécurité. Nous partons quand vos équipes exploitent la solution seules.",
    g: ["Un prototype éprouvé sur vos données réelles", "Une solution en production, surveillée et documentée", "Un transfert complet : code, accès, documentation, équipes formées"],
    k: "Intégration, automatisation, agents IA, mise en production, transfert",
    photo: "ingenieurs", photoAlt: "Trois ingénieurs penchés sur un ordinateur portable, au milieu d'un banc d'essai en atelier.",
  },
  {
    slug: "geo", href: GEO_PATH, t: "GEO : référencement dans les assistants IA", court: "GEO",
    d: "Quand vos clients demandent à ChatGPT, Claude, Perplexity, Gemini ou Copilot qui peut les aider, votre entreprise doit faire partie de la réponse. Nous rendons votre offre compréhensible, vérifiable et citable par les moteurs de réponse comme par Google.",
    g: ["Un audit de votre visibilité dans les assistants IA, question par question", "Des pages, des données structurées et une entité cohérentes, que les moteurs comprennent", "Une présence hors site alignée et un suivi des citations"],
    k: "GEO, SEO, données structurées, Wikidata, Search Console, Bing Webmaster Tools",
    photo: "archives", photoAlt: "Une longue allée de rayonnages chargés de dossiers et de reliures.",
  },
  {
    slug: "architecture-entreprise-solutions", href: "/expertises/architecture-entreprise-solutions/", t: "Architecture d'entreprise et de solutions", court: "Architecture",
    d: "Savoir ce que vous avez, décider où vous allez et choisir les solutions qui vous y mènent, sans empiler les outils.",
    g: ["Cartographie des applications, des données et des flux", "Architecture cible et trajectoire en options chiffrées", "Choix de solutions et revues d'architecture extérieures"],
    k: "Cartographie, architecture cible, intégration, cloud",
    photo: "aiguillage", photoAlt: "Deux voies ferrées qui se croisent en X, vues d'en haut.",
  },
  {
    slug: "pilotage-de-programmes", href: "/expertises/pilotage-de-programmes/", t: "Pilotage de programmes", court: "Pilotage de programmes",
    d: "Des programmes multi-équipes cadrés et tenus : une gouvernance claire, des risques suivis, des comités qui décident, des utilisateurs embarqués dès le premier jour.",
    g: ["Plan, budget et risques repris en main", "Gouvernance et comités qui tranchent", "Conduite du changement mesurée"],
    k: "PMP, PRINCE2, SAFe, Scrum, ADKAR",
    photo: "salle", photoAlt: "Une salle de réunion vide, une longue table face à une baie vitrée.",
  },
  {
    slug: "digitalisation", href: "/expertises/digitalisation/", t: "Digitalisation", court: "Digitalisation",
    d: "Les processus papier, les doubles saisies et les fichiers éparpillés deviennent des outils reliés qui travaillent pour vos équipes.",
    g: ["Processus cartographiés et simplifiés avant d'être outillés", "Formulaires, flux et validations automatisés", "Données reliées entre vos outils, tableaux de bord utilisés"],
    k: "Automatisation, CRM et ERP, données, IA appliquée",
    photo: "fibres", photoAlt: "Des fibres optiques jaunes raccordées une à une sur un panneau de brassage.",
  },
];

// domaines d'application : chacun avec une phrase et la page qui le traite
export const DOMAINES = [
  { t: "Achats et Source-to-Pay", sub: "Fractional CPO, intérim, risques tiers",
    d: "Du besoin au paiement : des processus outillés, des risques fournisseurs maîtrisés, une direction des achats à temps partagé ou par intérim.",
    href: "/expertises/transformation-achats/", l: "La transformation des achats" },
  { t: "Risques et conformité", sub: "DORA, NIS2, RGPD, AI Act",
    d: "Des obligations traduites en processus, en responsables et en preuves, dans ce que vous construisez comme dans ce que vous achetez.",
    href: `${FDE_PATH}#environnement-regule`, l: "Le FDE en environnement régulé" },
  { t: "IA en production", sub: "Agents, automatisations, intégrations",
    d: "Du prototype qui convainc en démonstration à l'agent IA qui tourne sur vos systèmes, sous contrôle humain.",
    href: FDE_PATH, l: "Le Forward Deployed Engineering" },
  { t: "Produits numériques et SaaS", sub: "Architecture, intégrations, lancement",
    d: "L'architecture, les intégrations et la mise en production d'un produit numérique, jusqu'à ce que votre équipe le fasse évoluer seule.",
    href: "/expertises/architecture-entreprise-solutions/", l: "L'architecture de solutions" },
];
