// PROVISOIRE : copie du français, à traduire.
// Contenu des pages métiers (GEO, architecture, pilotage, digitalisation), rendues par components/MetierPage.astro.
// Vouvoiement, aucun chiffre, prix, durée ni détail de projet ; rien d'invérifiable. Les FAQ visibles alimentent le balisage FAQPage.
import type { PageMetier } from "../fr/pages";
import { routesFor } from "../routes";
import { SOURCES } from "../sources";
const r = routesFor("en");

const pages: PageMetier[] = [
  {
    slug: "geo", key: "geo", path: r.geo, crumb: "GEO",
    title: "GEO : référencement dans ChatGPT et les assistants IA | Clixite",
    description: "Le GEO rend votre entreprise compréhensible et citable par ChatGPT, Claude, Perplexity et Google : audit, structuration et suivi, en Belgique et au Luxembourg.",
    h1: ["GEO : ", "être la réponse que donnent les assistants IA."],
    chapo: "Le GEO (Generative Engine Optimization) consiste à rendre une entreprise compréhensible, vérifiable et citable par les moteurs de réponse : ChatGPT, Claude, Perplexity, Gemini, Copilot et les aperçus IA de Google. Clixite mesure votre visibilité, structure vos contenus et vos données, et corrige ce qui empêche les assistants de vous citer, en Belgique et au Luxembourg.",
    photo: "archives-45",
    alternateName: ["Generative Engine Optimization", "Référencement IA", "Optimisation pour les moteurs génératifs"],
    serviceType: ["Generative Engine Optimization", "Référencement naturel", "Données structurées", "Audit de visibilité dans les assistants IA"],
    blocs: [
      { id: "geo-seo", h: "GEO et SEO : quelle différence ?", kind: "prose", p: [
        "Le SEO vise une position dans une liste de liens. Le GEO vise une place dans la réponse que rédige l'assistant, avec une citation de votre site.",
        "Les deux se complètent. Les moteurs de réponse s'appuient largement sur des pages déjà bien référencées, mais ils lisent autrement : ils cherchent des définitions nettes, des faits vérifiables et des sources qui se confirment entre elles.",
      ], src: [{ t: "Aggarwal et al., « GEO: Generative Engine Optimization », 2023", href: SOURCES.geoPaper }] },
      { id: "geo-criteres", h: "Ce qui fait qu'un assistant vous cite", kind: "defs", band: true, lead: "Ce que l'on sait aujourd'hui, et que nous mesurons pour chaque client.", defs: [
        { t: "Une entité sans ambiguïté", d: "Le même nom, la même adresse, les mêmes métiers partout : registre des entreprises, site, LinkedIn, annuaires, Wikidata." },
        { t: "Des pages qui répondent", d: "Une définition en quelques phrases, des questions fréquentes visibles, des comparaisons honnêtes, des pages datées." },
        { t: "Des données structurées fidèles", d: "Un balisage schema.org qui décrit exactement ce que la page affiche, et un site lisible par les robots des assistants." },
        { t: "Des mentions ailleurs que chez vous", d: "Presse, annuaires professionnels, bases ouvertes : les assistants croisent leurs sources avant de citer." },
      ] },
      { id: "geo-methode", h: "Notre démarche, en quatre temps", kind: "steps", lead: "Chaque temps livre quelque chose que vous gardez.", steps: [
        { t: "Mesurer", d: "Les questions que posent vos clients, testées sur les principaux assistants : qui est cité, avec quelles informations, venues d'où.", out: "Audit de visibilité IA" },
        { t: "Structurer", d: "Entité, données structurées, pages définitionnelles, questions fréquentes, règles pour les robots : le site devient lisible et citable.", out: "Site prêt pour les moteurs de réponse" },
        { t: "Publier", d: "Contenus de référence, fiches d'entreprise, profils professionnels, Wikidata : votre présence hors site se met en cohérence.", out: "Présence tierce alignée" },
        { t: "Suivre", d: "Search Console, Bing Webmaster Tools et tests réguliers des assistants : on mesure les citations et on corrige.", out: "Tableau de suivi" },
      ] },
      { id: "geo-garantie", h: "Ce que personne ne peut garantir", kind: "note", encre: true, p: [
        "Aucun prestataire ne peut garantir une position dans Google ni une citation par un assistant : les modèles changent, leurs sources aussi.",
        "Ce à quoi nous nous engageons, c'est un travail mesurable : un site explorable, des données valides et cohérentes, une présence alignée, et des tests réguliers pour voir ce qui bouge. Ce site en est l'application : entité décrite en données structurées, pages définitionnelles, questions fréquentes visibles, résumé pour les assistants.",
      ] },
      { id: "geo-pour-qui", h: "Pour qui", kind: "list", items: [
        "Les PME et les cabinets dont les clients se renseignent seuls avant d'appeler.",
        "Les groupes qui veulent que les assistants décrivent correctement leurs offres, leurs marques et leurs obligations.",
        "Les éditeurs de logiciels et de services dont le nom doit sortir quand on demande une solution à un assistant.",
        "Toute entreprise présente en plusieurs langues : les assistants répondent dans la langue de la question.",
      ] },
    ],
    faq: [
      { q: "Qu'est-ce que le GEO ?", a: "Le Generative Engine Optimization rend une entreprise compréhensible, vérifiable et citable par les moteurs de réponse, comme ChatGPT, Claude, Perplexity, Gemini, Copilot et les aperçus IA de Google." },
      { q: "Le SEO est-il encore utile ?", a: "Oui. Les moteurs de réponse s'appuient en grande partie sur l'index des moteurs de recherche. Un bon référencement reste la base ; le GEO ajoute ce qui rend un contenu citable." },
      { q: "Peut-on garantir d'être cité par ChatGPT ?", a: "Non, et méfiez-vous de qui le promet. On peut en revanche mesurer votre visibilité, corriger ce qui vous dessert et suivre l'évolution des citations." },
      { q: "Le fichier llms.txt suffit-il ?", a: "Non. Il aide certains outils à résumer un site, mais les principaux assistants le lisent peu à ce jour. Nous le mettons en place sans en attendre de miracle." },
      { q: "Faut-il refaire son site ?", a: "Rarement. La plupart des corrections portent sur le contenu, les données structurées et la présence hors site." },
      { q: "En quelles langues travaillez-vous ?", a: "En français, en néerlandais et en anglais. Les assistants répondent dans la langue de la question : il faut exister dans chacune." },
    ],
  },
  {
    slug: "architecture-entreprise-solutions", key: "archi", path: r.archi, crumb: "Architecture d'entreprise et de solutions",
    title: "Architecture d'entreprise et de solutions | Clixite",
    description: "Cartographie du système d'information, architecture cible, trajectoire en options et choix de solutions, jusqu'à la mise en production. Belgique et Luxembourg.",
    h1: ["Architecture d'entreprise et de solutions : ", "décider où va votre système d'information."],
    chapo: "L'architecture d'entreprise relie la stratégie au système d'information : ce que vous avez, ce que vous visez et le chemin entre les deux. L'architecture de solutions choisit et dessine les outils qui y mènent. Clixite fait les deux, de la cartographie à la mise en production, pour les PME comme pour les groupes régulés, en Belgique et au Luxembourg.",
    photo: "aiguillage-45",
    serviceType: ["Architecture d'entreprise", "Architecture de solutions", "Cartographie du système d'information", "Revue d'architecture"],
    blocs: [
      { id: "archi-quand", h: "Quand faire appel à nous", kind: "list", items: [
        "Vos applications se sont empilées et plus personne n'a la vue d'ensemble.",
        "Un grand choix approche : ERP, CRM, outil achats, cloud, plateforme de données.",
        "Une fusion, une scission ou une réorganisation rebat les cartes.",
        "Un régulateur ou un auditeur demande une vue claire de vos systèmes et de vos fournisseurs critiques.",
        "Un projet d'IA doit trouver sa place dans l'existant.",
      ] },
      { id: "archi-obtenez", h: "Ce que vous obtenez", kind: "defs", band: true, defs: [
        { t: "Une cartographie", d: "Applications, données, flux, contrats et fournisseurs critiques, sur une carte que vos équipes savent lire." },
        { t: "Une architecture cible", d: "Principes, briques, intégrations et sécurité : ce vers quoi vous allez, et pourquoi." },
        { t: "Une trajectoire en options", d: "Ce qu'on garde, ce qu'on remplace, ce qu'on arrête ; chaque option avec ses coûts, ses risques et ses dépendances." },
        { t: "Des revues d'architecture extérieures", d: "Un regard extérieur et argumenté sur un choix de solution ou un dossier d'architecture, avant que la décision ne coûte cher." },
      ] },
      { id: "archi-suite", h: "De la cible à la mise en production", kind: "prose", p: [
        "Une cible n'a de valeur que si elle se construit. Quand elle est validée, nous pouvons la mettre en œuvre avec vos équipes, en Forward Deployed Engineering, et piloter le programme qui la porte.",
      ], link: { t: "Le Forward Deployed Engineering", href: r.fde } },
    ],
    faq: [
      { q: "Quelle différence entre architecture d'entreprise et architecture de solutions ?", a: "La première décide de l'ensemble : métiers, données, applications, technologies, et la trajectoire entre aujourd'hui et la cible. La seconde conçoit une solution précise dans ce cadre, jusqu'aux intégrations et à la sécurité." },
      { q: "Une PME a-t-elle besoin d'architecture d'entreprise ?", a: "Oui, à sa mesure. Une carte claire de vos outils et de vos flux évite les achats redondants et prépare la croissance. Pour une PME, l'exercice tient en quelques livrables courts." },
      { q: "Suivez-vous un cadre méthodologique ?", a: "Nous reprenons les notions des cadres reconnus quand elles servent, sans imposer de formalisme lourd : un livrable d'architecture doit être lu et utilisé par vos équipes." },
      { q: "Pouvez-vous aussi construire la cible ?", a: "Oui, en Forward Deployed Engineering : nous intégrons vos équipes pour mettre en production ce qui a été décidé, puis nous transférons." },
    ],
  },
  {
    slug: "pilotage-de-programmes", key: "pilotage", path: r.pilotage, crumb: "Pilotage de programmes",
    title: "Pilotage de programmes et conduite du changement | Clixite",
    description: "Gouvernance, planning, budget, risques et adoption : vos programmes multi-équipes tenus jusqu'à la mise en service, en Belgique et au Luxembourg.",
    h1: ["Pilotage de programmes : ", "des programmes multi-équipes tenus jusqu'à la mise en service."],
    chapo: "Le pilotage de programmes coordonne plusieurs projets qui servent un même objectif : gouvernance, planning, budget, risques et conduite du changement. Clixite lance ou reprend vos programmes de transformation, en Belgique et au Luxembourg, avec des référentiels reconnus (PMP, PRINCE2, SAFe, Scrum, ADKAR) et une règle : les décisions se prennent sur pièces.",
    photo: "salle-45",
    serviceType: ["Pilotage de programmes", "Gestion de projets", "Conduite du changement", "Reprise de programme"],
    blocs: [
      { id: "prog-quand", h: "Quand faire appel à nous", kind: "list", items: [
        "Un programme a pris du retard ou son budget dérive.",
        "Plusieurs équipes et plusieurs fournisseurs doivent avancer au même rythme.",
        "Les comités se réunissent mais ne décident pas.",
        "Une mise en production critique approche.",
        "Les utilisateurs n'adoptent pas ce qui a été livré.",
      ] },
      { id: "prog-obtenez", h: "Ce que vous obtenez", kind: "defs", band: true, defs: [
        { t: "Un diagnostic de reprise", d: "Où en est vraiment le programme : périmètre, planning, budget, risques et dépendances." },
        { t: "Une gouvernance qui décide", d: "Des comités, des rôles et des règles d'arbitrage clairs, des tableaux de bord qui servent la décision." },
        { t: "Un plan tenu", d: "Des jalons, des dépendances et des risques suivis de près, avec chaque équipe et chaque fournisseur." },
        { t: "Un changement mesuré", d: "Formation, communication et adoption suivies avec des indicateurs définis au départ." },
      ] },
    ],
    faq: [
      { q: "Pouvez-vous reprendre un programme en cours ?", a: "Oui, c'est fréquent : un diagnostic, un plan de reprise et des arbitrages clairs, puis un pilotage au plus près des équipes." },
      { q: "Méthodes itératives ou cycle en V ?", a: "Les deux, selon la nature du programme et vos contraintes : SAFe et Scrum pour le produit et le logiciel, PRINCE2 ou PMP pour les programmes très gouvernés, souvent un mélange assumé." },
      { q: "Travaillez-vous avec nos fournisseurs et nos intégrateurs ?", a: "Oui. Nous coordonnons les équipes internes et les fournisseurs, avec des engagements clairs pour chacun." },
      { q: "Comment mesurez-vous l'adoption ?", a: "Avec des indicateurs définis au départ : usage réel, demandes de support, qualité des données saisies, retours des utilisateurs." },
    ],
  },
  {
    slug: "digitalisation", key: "digit", path: r.digit, crumb: "Digitalisation",
    title: "Digitalisation des processus et automatisation | Clixite",
    description: "Processus simplifiés puis outillés, flux automatisés, données reliées et IA appliquée, de la PME au grand groupe, en Belgique et au Luxembourg.",
    h1: ["Digitalisation des processus : ", "du papier et des doubles saisies à des outils reliés."],
    chapo: "La digitalisation des processus remplace le papier, les fichiers éparpillés et les doubles saisies par des flux outillés et des données reliées. Clixite cartographie et simplifie vos processus avant de les automatiser, puis les met en production avec vos équipes, des PME aux grands groupes, en Belgique et au Luxembourg.",
    photo: "fibres-45",
    serviceType: ["Digitalisation des processus", "Automatisation", "Intégration CRM et ERP", "IA appliquée"],
    blocs: [
      { id: "digit-quand", h: "Quand faire appel à nous", kind: "list", items: [
        "Un processus tourne encore sur papier, sur Excel ou par courriel.",
        "Les mêmes données sont saisies plusieurs fois dans plusieurs outils.",
        "Les validations se perdent entre les boîtes de réception.",
        "Les tableaux de bord existent mais personne ne s'en sert.",
        "Vous voulez utiliser l'IA sans savoir par où commencer.",
      ] },
      { id: "digit-obtenez", h: "Ce que vous obtenez", kind: "defs", band: true, defs: [
        { t: "Des processus simplifiés", d: "Cartographiés, débarrassés des étapes inutiles, avec des règles claires, avant d'être outillés." },
        { t: "Des flux automatisés", d: "Formulaires, validations, notifications et intégrations avec votre CRM et votre ERP." },
        { t: "Des données reliées", d: "Une seule saisie, des référentiels propres et des tableaux de bord utilisés." },
        { t: "De l'IA appliquée", d: "Là où elle fait gagner du temps, sous contrôle humain et dans le respect du RGPD." },
      ] },
    ],
    faq: [
      { q: "Par où commencer ?", a: "Par le processus le plus pénible et le plus fréquent. On le simplifie avant de l'outiller : automatiser un processus confus ne fait que l'accélérer." },
      { q: "Faut-il changer d'outils ?", a: "Pas forcément. Nous exploitons d'abord ce que vous avez ; un nouvel outil ne se justifie que s'il fait mieux à un coût raisonnable." },
      { q: "Quelle place pour l'IA ?", a: "Lire des documents, classer des demandes, préparer des réponses : l'IA rend de vrais services, sous contrôle humain et dans le respect du RGPD." },
      { q: "Vos équipes pourront-elles faire évoluer les flux ?", a: "Oui. La documentation et la formation font partie de chaque mission, pour que vos équipes restent autonomes." },
    ],
  },
];
export default pages;
