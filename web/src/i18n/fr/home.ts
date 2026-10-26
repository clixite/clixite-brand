// Accueil : film, logos, Forward Deployed Engineering, GEO, métiers, méthode.
import { routesFor } from "../routes";
const r = routesFor("fr");

const home = {
  title: "Forward Deployed Engineering et GEO en Belgique | Clixite",
  description: "Forward Deployed Engineering, GEO, architecture, programmes et digitalisation : Clixite construit vos solutions dans vos équipes, en Belgique et au Luxembourg.",
  hero: {
    // chapitres de la boucle (11,5 s) : les titres du film, au rythme des plans
    story: [
      { t: "Votre architecture commence sur papier.", from: 0 },
      { t: "Elle prend du relief.", from: 2.5 },
      { t: "Elle se pose chez vous.", from: 5.5 },
      { t: "Et elle tourne.", from: 8.5 },
    ],
    h1: ["Nous résolvons votre ", "x", "."],
    sub: "Forward Deployed Engineering, GEO, architecture d'entreprise et de solutions, pilotage de programmes, digitalisation. Dans vos équipes, en Belgique et au Luxembourg, jusqu'à la mise en production.",
    cta2: { t: "Le Forward Deployed Engineering", href: r.fde },
  },
  refs: {
    title: "Là où nous avons travaillé.",
    note: "Télécoms, banque, assurance, construction, courtage, PME : des environnements très différents, en mission, en conseil ou en poste. Les projets, eux, restent confidentiels.",
  },
  fde: {
    title: "Forward Deployed Engineering.",
    lead: "Clixite s'installe dans vos équipes pour concevoir, construire et mettre en production vos intégrations, vos automatisations et vos agents IA, puis vous transférer la solution. En Belgique et au Luxembourg, en français, en néerlandais ou en anglais.",
    btn: "Le Forward Deployed Engineering en détail",
    items: [
      { t: "Dans vos équipes, pas à côté.", d: "Sur site ou à distance, dans vos outils et à votre rythme. Les décisions se prennent là où le travail se fait." },
      { t: "En production, pas en PowerPoint.", d: "La mission se mesure à ce qui tourne : une intégration, un processus automatisé, un agent IA utilisé le lundi matin." },
      { t: "Sous votre contrôle, puis chez vous.", d: "Vos environnements, vos règles de sécurité, des accès nominatifs. À la fin, le code, la documentation et le savoir-faire restent chez vous." },
    ],
  },
  geo: {
    title: "GEO : être la réponse des assistants IA.",
    lead: "Vos clients ne cherchent plus seulement sur Google. Ils demandent à ChatGPT, Claude, Perplexity, Gemini ou Copilot qui peut les aider. Nous travaillons pour que les assistants vous trouvent et vous décrivent juste.",
    btn: "Le GEO en détail",
    items: [
      { t: "Mesurer", d: "Les questions que posent vos clients, testées sur les principaux assistants : qui est cité, et avec quelles informations." },
      { t: "Structurer", d: "Une entité cohérente, des pages qui répondent et des données structurées fidèles : votre site devient citable." },
      { t: "Publier et suivre", d: "Fiches d'entreprise, profils, bases ouvertes, mentions tierces, puis des tests réguliers : les assistants croisent leurs sources avant de citer." },
    ],
  },
  expertises: {
    title: "Cinq métiers, une même exigence : un résultat qui tourne.",
    lead: "Nous intervenons là où une stratégie doit devenir un système qui fonctionne, dans une PME comme dans un groupe régulé.",
  },
  method: {
    title: "Du relevé à la mise en service.",
    lead: "Quatre étapes, chacune avec un livrable que vous gardez, même si vous arrêtez là. Vous décidez de la suivante sur pièces.",
    steps: [
      { t: "Relever", d: "Cartographie de vos systèmes, de vos flux, de vos contrats et de vos risques. On mesure avant de dessiner.", out: "Diagnostic" },
      { t: "Concevoir", d: "L'architecture cible et le chemin pour y aller, en options chiffrées. Ce qu'on garde, ce qu'on remplace, ce qu'on arrête.", out: "Cible et feuille de route" },
      { t: "Construire", d: "Intégrations, données, automatisations et IA, livrées par incréments courts que vos équipes testent en conditions réelles.", out: "Incréments en production" },
      { t: "Mettre en service", d: "Déploiement, adoption et transfert. Nous partons quand vos équipes tiennent la solution seules.", out: "Solution exploitée et documentée" },
    ],
  },
};
export type Home = typeof home;
export default home;
