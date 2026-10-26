// Contenu de la page pilier Forward Deployed Engineering, en français et en anglais (même structure, même balisage).
// Rédaction : vouvoiement, aucun chiffre ni détail de projet, aucune promesse invérifiable ; sources citées pour l'origine du modèle.
export const FDE_UPDATED = "2026-10-26";

export const SOURCES = {
  palantir: "https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87",
  techcrunch: "https://techcrunch.com/2026/07/30/forward-deployed-engineers-are-the-AI-industrys-latest-talent-obsession/",
};

export const FDE = {
  fr: {
    title: "Forward Deployed Engineering, Belgique et Luxembourg | Clixite",
    description: "Des ingénieurs intégrés à vos équipes conçoivent et mettent en production vos intégrations, automatisations et agents IA, puis vous transfèrent tout.",
    crumbs: [{ name: "Accueil", href: "/" }, { name: "Forward Deployed Engineering", href: "/forward-deployed-engineering/" }],
    h1: ["Forward Deployed Engineering : ", "construire dans vos équipes, jusqu'à la production."],
    chapo: "Le Forward Deployed Engineering (FDE) consiste à installer des ingénieurs dans les équipes d'un client pour concevoir, construire et mettre en production une solution sur ses systèmes, puis la lui transférer. En Belgique et au Luxembourg, Clixite applique ce modèle aux intégrations, aux automatisations et à l'IA, dans le cadre de DORA, NIS2, du RGPD et de l'AI Act.",
    cta: "Demander un échange", cta2: "Voir la méthode", updated: "Mis à jour le 26 octobre 2026",
    what: {
      h: "Qu'est-ce que le Forward Deployed Engineering ?",
      p: [
        "Un Forward Deployed Engineer est un ingénieur placé chez le client, au plus près de ceux qui utilisent le système. Il comprend le métier, conçoit, code, intègre et déploie, puis transfère ce qu'il a construit. Le terme reste en anglais, en français comme en néerlandais ; on parle parfois d'ingénieur déployé chez le client.",
        "Ce n'est ni un conseil qui s'arrête à la recommandation, ni une régie qui exécute des tâches : le Forward Deployed Engineer porte un résultat défini avec vous, une solution qui tourne dans votre environnement.",
      ],
    },
    origin: {
      h: "D'où vient le modèle",
      p: "Le modèle a été formalisé par Palantir, qui distingue ses développeurs produit de ses ingénieurs déployés chez le client, résumés par une formule : un client, de nombreuses capacités. Depuis, les acteurs de l'intelligence artificielle l'ont repris pour faire passer leurs clients du prototype à la production, au point d'en faire l'un des profils les plus recherchés du secteur.",
      src: [{ t: "Palantir, « Dev versus Delta »", href: SOURCES.palantir }, { t: "TechCrunch, 30 juillet 2026", href: SOURCES.techcrunch }],
      srcLabel: "Sources",
    },
    when: {
      h: "Quand faire appel à un Forward Deployed Engineer",
      items: [
        "Un prototype d'IA fonctionne en démonstration mais n'est jamais passé en production.",
        "Vos systèmes ne se parlent pas : ERP, CRM, outil achats et données métier sont à relier de façon fiable.",
        "Un processus encore manuel doit être automatisé sans casser ce qui tourne.",
        "Un programme a pris du retard et il faut des mains autant que des comités.",
        "Votre environnement est régulé et rien ne doit sortir de chez vous.",
        "Votre équipe doit monter en compétence, jusqu'à créer sa propre capacité FDE.",
      ],
    },
    method: {
      h: "Notre méthode, en quatre temps",
      lead: "Chaque temps livre quelque chose que vous gardez. Vous décidez du suivant sur pièces.",
      steps: [
        { t: "S'installer", d: "Accès, environnements, règles de sécurité et interlocuteurs : nous travaillons dans vos outils et avec vos équipes dès le départ.", out: "Cadre de travail validé" },
        { t: "Construire", d: "Un prototype sur vos données réelles, testé avec ceux qui l'utiliseront et amélioré par incréments courts.", out: "Prototype éprouvé" },
        { t: "Mettre en production", d: "Sécurité, surveillance, documentation et procédures d'exploitation : la solution entre en production selon vos règles.", out: "Solution en production" },
        { t: "Transférer", d: "Code, accès, documentation et formation : nous partons quand vos équipes exploitent et font évoluer la solution seules.", out: "Équipes autonomes" },
      ],
      outLabel: "Livrable",
    },
    compare: {
      h: "FDE, conseil ou régie : quelle différence ?",
      cols: ["", "Rôle", "Ce que vous recevez", "Fin de la mission"],
      rows: [
        ["Forward Deployed Engineering", "Construit et met en production dans vos équipes.", "Une solution en production, documentée et transférée.", "Quand vos équipes l'exploitent seules."],
        ["Conseil classique", "Analyse et recommande.", "Un rapport, une cible, une feuille de route.", "À la remise du livrable."],
        ["ESN ou régie", "Exécute les tâches que vous dirigez.", "Du temps, en obligation de moyens.", "À l'échéance du contrat ; le transfert n'est pas prévu d'office."],
      ],
      note: "La différence tient au mandat, pas au contrat : un Forward Deployed Engineer peut être engagé en mission comme au forfait.",
    },
    regulated: {
      h: "Le Forward Deployed Engineering en environnement régulé",
      lead: "Banques, assurances, entités essentielles : DORA, NIS2, le RGPD et l'AI Act s'appliquent aussi à ce que l'on construit. Le cadre se pose dès le départ.",
      items: [
        { t: "Vos environnements", d: "Rien n'est construit hors de votre périmètre sans accord écrit." },
        { t: "Des accès nominatifs", d: "Tracés, limités au nécessaire, retirés à la fin de la mission." },
        { t: "Vos données restent chez vous", d: "L'usage d'outils d'IA se décide avec vous, outil par outil." },
        { t: "Une documentation prête pour l'audit", d: "Architecture, choix, risques, procédures d'exploitation." },
        { t: "L'IA sous contrôle humain", d: "Supervision, journalisation et documentation, comme l'exige l'AI Act pour les systèmes concernés." },
      ],
    },
    keep: {
      h: "Ce que vous gardez",
      p: "Le code, les accès, la documentation et des équipes formées. Et si vous le souhaitez, l'organisation de votre propre équipe FDE interne : rôles, méthodes, recrutement.",
    },
    faqTitle: "Questions fréquentes sur le Forward Deployed Engineering.",
    faq: [
      { q: "Qu'est-ce qu'un Forward Deployed Engineer ?", a: "Un ingénieur intégré aux équipes d'un client, qui transforme un besoin en solution en service. Il comprend le métier, conçoit, code, intègre, déploie, puis transfère. Le modèle a été formalisé par Palantir." },
      { q: "Quelle différence avec un consultant ?", a: "Le consultant recommande, le Forward Deployed Engineer construit. Sa mission se termine quand vos équipes exploitent la solution, pas à la remise d'un rapport." },
      { q: "Est-ce de la régie sous un autre nom ?", a: "Non. En régie, vous dirigez une ressource tâche par tâche. Le Forward Deployed Engineer porte un résultat défini avec vous : une solution en production, documentée et transférée." },
      { q: "Faut-il un projet d'intelligence artificielle ?", a: "Non. Le modèle vaut aussi pour relier des systèmes, automatiser un processus ou reprendre un programme. L'IA n'est qu'un des cas les plus fréquents." },
      { q: "Est-ce compatible avec DORA, NIS2, le RGPD et l'AI Act ?", a: "Oui, si le cadre est posé au départ : vos environnements, vos règles de sécurité, des accès nominatifs et des données qui restent chez vous." },
      { q: "Que garde l'entreprise à la fin ?", a: "Le code, les accès, la documentation et des équipes formées pour exploiter et faire évoluer la solution." },
      { q: "Où et en quelles langues intervenez-vous ?", a: "En Belgique et au Luxembourg, en français, en néerlandais ou en anglais, sur site ou à distance." },
    ],
    others: "Nos autres métiers",
  },
  en: {
    title: "Forward Deployed Engineering, Belgium and Luxembourg | Clixite",
    description: "Engineers embedded in your teams design, build and ship your integrations, automations and AI agents to production, then hand everything over to you.",
    crumbs: [{ name: "Clixite", href: "/" }, { name: "Forward Deployed Engineering", href: "/en/forward-deployed-engineering/" }],
    h1: ["Forward Deployed Engineering: ", "building inside your teams, all the way to production."],
    chapo: "Forward Deployed Engineering (FDE) means placing engineers inside a client's teams to design, build and ship a solution to production on the client's own systems, then hand it over. In Belgium and Luxembourg, Clixite applies this model to integrations, automation and AI, within the frameworks of DORA, NIS2, the GDPR and the AI Act.",
    cta: "Request a conversation", cta2: "See how we work", updated: "Updated 26 October 2026",
    what: {
      h: "What is Forward Deployed Engineering?",
      p: [
        "A Forward Deployed Engineer is an engineer placed with the client, close to the people who use the system. They understand the business, design, code, integrate and deploy, then hand over what they built.",
        "It is neither consulting that stops at a recommendation nor staffing that executes tasks: the Forward Deployed Engineer owns an outcome defined with you, a solution running in your environment.",
      ],
    },
    origin: {
      h: "Where the model comes from",
      p: "The model was formalised by Palantir, which distinguishes its product developers from the engineers it deploys with customers, summed up as one customer, many capabilities. AI companies have since adopted it to take their customers from prototype to production, to the point of making it one of the most sought-after profiles in the industry.",
      src: [{ t: "Palantir, “Dev versus Delta”", href: SOURCES.palantir }, { t: "TechCrunch, 30 July 2026", href: SOURCES.techcrunch }],
      srcLabel: "Sources",
    },
    when: {
      h: "When to bring in a Forward Deployed Engineer",
      items: [
        "An AI prototype works in a demo but has never reached production.",
        "Your systems do not talk to each other: ERP, CRM, procurement tools and business data need reliable connections.",
        "A manual process must be automated without breaking what already runs.",
        "A programme is late and needs hands as much as steering committees.",
        "Your environment is regulated and nothing may leave your premises.",
        "Your team needs to build skills, up to creating its own FDE capability.",
      ],
    },
    method: {
      h: "How we work, in four stages",
      lead: "Each stage delivers something you keep. You decide on the next one based on evidence.",
      steps: [
        { t: "Settle in", d: "Access, environments, security rules and contacts: we work in your tools and with your teams from the start.", out: "Agreed working framework" },
        { t: "Build", d: "A prototype on your real data, tested with the people who will use it and improved in short increments.", out: "Proven prototype" },
        { t: "Go to production", d: "Security, monitoring, documentation and runbooks: the solution goes live according to your rules.", out: "Solution in production" },
        { t: "Hand over", d: "Code, access, documentation and training: we leave when your teams run and evolve the solution on their own.", out: "Self-sufficient teams" },
      ],
      outLabel: "Deliverable",
    },
    compare: {
      h: "FDE, consulting or staffing: what is the difference?",
      cols: ["", "Role", "What you receive", "End of the assignment"],
      rows: [
        ["Forward Deployed Engineering", "Builds and ships to production inside your teams.", "A solution in production, documented and handed over.", "When your teams run it on their own."],
        ["Traditional consulting", "Analyses and recommends.", "A report, a target, a roadmap.", "When the deliverable is handed in."],
        ["IT services or staffing", "Executes the tasks you direct.", "Time, on a best-efforts basis.", "When the contract ends; handover is not built in."],
      ],
      note: "The difference lies in the mandate, not the contract: a Forward Deployed Engineer can be engaged on a time-and-materials or a fixed-scope basis.",
    },
    regulated: {
      h: "Forward Deployed Engineering in regulated environments",
      lead: "Banks, insurers, essential entities: DORA, NIS2, the GDPR and the AI Act also apply to what gets built. The framework is set from the start.",
      items: [
        { t: "Your environments", d: "Nothing is built outside your perimeter without written agreement." },
        { t: "Named access", d: "Logged, limited to what is needed, removed at the end of the assignment." },
        { t: "Your data stays with you", d: "The use of AI tools is decided with you, tool by tool." },
        { t: "Audit-ready documentation", d: "Architecture, decisions, risks, operating procedures." },
        { t: "AI under human oversight", d: "Oversight, logging and documentation, as the AI Act requires for the systems in scope." },
      ],
    },
    keep: {
      h: "What you keep",
      p: "The code, the access, the documentation and trained teams. And if you wish, the set-up of your own internal FDE team: roles, methods, hiring.",
    },
    faqTitle: "Frequently asked questions about Forward Deployed Engineering.",
    faq: [
      { q: "What is a Forward Deployed Engineer?", a: "An engineer embedded in a client's teams who turns a need into a working service. They understand the business, design, code, integrate, deploy, then hand over. The model was formalised by Palantir." },
      { q: "How is it different from a consultant?", a: "A consultant recommends; a Forward Deployed Engineer builds. The assignment ends when your teams run the solution, not when a report is delivered." },
      { q: "Is it staffing under another name?", a: "No. With staffing, you direct a resource task by task. A Forward Deployed Engineer owns an outcome defined with you: a solution in production, documented and handed over." },
      { q: "Do I need an artificial intelligence project?", a: "No. The model also works for connecting systems, automating a process or recovering a programme. AI is simply one of the most common cases." },
      { q: "Is it compatible with DORA, NIS2, the GDPR and the AI Act?", a: "Yes, provided the framework is set from the start: your environments, your security rules, named access and data that stays with you." },
      { q: "What does the company keep at the end?", a: "The code, the access, the documentation and teams trained to run and evolve the solution." },
      { q: "Where and in which languages do you work?", a: "In Belgium and Luxembourg, in English, French or Dutch, on site or remotely." },
    ],
    others: "Our other services (in French)",
  },
};
