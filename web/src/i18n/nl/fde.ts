// PROVISOIRE : copie du français, à traduire.
// Page pilier Forward Deployed Engineering. Vouvoiement, aucun chiffre ni détail de projet, aucune promesse
// invérifiable ; sources citées pour l'origine du modèle. Même structure dans les trois langues.
import type { Fde } from "../fr/fde";
import { SOURCES } from "../sources";

const fde: Fde = {
  title: "Forward Deployed Engineering, Belgique et Luxembourg | Clixite",
  description: "Des ingénieurs intégrés à vos équipes conçoivent et mettent en production vos intégrations, automatisations et agents IA, puis vous transfèrent tout.",
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
  schema: {
    alternateName: ["FDE", "Forward Deployed Engineer", "Ingénieur déployé chez le client"],
    serviceType: ["Forward Deployed Engineering", "Intégration de systèmes", "Automatisation des processus", "Mise en production de l'IA", "Agents IA"],
    term: "Modèle d'ingénierie qui installe des ingénieurs dans les équipes d'un client pour concevoir, construire et mettre en production une solution sur ses systèmes, puis la lui transférer.",
  },
};
export default fde;
