// Accueil : film, logos, Forward Deployed Engineering, GEO, expertises, méthode, preuves.
import { routesFor } from "../routes";
const r = routesFor("fr");

const home = {
  title: "Clixite, conseil et ingénierie à Wavre depuis 2005",
  description: "Conseil et ingénierie à Wavre depuis 2005. Clixite conçoit, construit et met en production les systèmes des entreprises belges et luxembourgeoises.",
  hero: {
    // chapitres de la boucle (11,5 s) : la signature ouvre, puis les titres du film au rythme des plans
    story: [
      { t: "Nous résolvons votre x.", from: 0 },
      { t: "Votre architecture commence sur papier.", from: 2 },
      { t: "Elle prend du relief.", from: 4.5 },
      { t: "Elle se pose chez vous.", from: 7 },
      { t: "Et elle tourne.", from: 9.5 },
    ],
    // le titre principal dit ce que nous faisons ; le « x » reste la signature du site (chapitres du film, clôture)
    h1: ["Nous construisons votre ", "solution", " dans vos équipes, jusqu'en production."],
    sub: "Conseil et ingénierie depuis 2005. Nous concevons, construisons et mettons en production vos systèmes, dans vos équipes, en Belgique et au Luxembourg.",
    cta2: { t: "Le Forward Deployed Engineering", href: r.fde },
  },
  refs: {
    title: "Là où nous avons travaillé.",
    note: "Télécoms, banque, assurance, industrie pharmaceutique, construction, aviation, distribution, loisirs, PME : des environnements très différents, en mission, en conseil ou en poste. Les projets, eux, restent confidentiels.",
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
    title: "Cinq expertises, une même exigence : un résultat qui tourne.",
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
  // Bloc « Preuves » (HomeView) : uniquement des faits vérifiables. Les 7 certifications viennent de
  // SITE.founder.certifications (site.ts) et les 14 logos affichés de data/clients.json.
  // TODO(contenu) : publier des cas clients anonymisés et des citations avec accord écrit, puis des chiffres de résultat vérifiables.
  // Aucun cas client, aucun témoignage et aucun pourcentage ne sont inventés ici.
  proofs: {
    title: "Ce qui est vérifiable.",
    lead: "Les projets restent confidentiels. Voici les faits que vous pouvez vérifier, et les engagements que nous prenons par écrit.",
    facts: {
      founded: "Fondée en",
      foundedValue: "2005, soit {years} ans d'activité.",
      certifications: "Sept certifications du fondateur",
      certificationsValue: "PMP, PRINCE2, AgilePM, SAFe, Scrum, ITIL v3, ADKAR.",
      logos: "Organisations citées",
      logosValue: "Quatorze organisations dont les logos sont affichés sur cette page, en mission, en conseil ou en poste.",
      languages: "Langues de travail",
      languagesValue: "Français, néerlandais, anglais.",
      area: "Zone d'intervention",
      areaValue: "Belgique et Luxembourg.",
      commitments: "Engagements",
      commitmentsValue: "Accord de confidentialité avant l'échange si vous le souhaitez, documentation au fil de l'eau, et le code, les accès et la documentation restent chez vous.",
    },
  },
};
export type Home = typeof home;
export default home;
