// Contenu par audience. Le site s'adapte à l'acheteur : grand groupe régulé, PME, cabinet ou intermédiaire.
// Version prudente validée par Nicolas le 25 octobre 2026 : ni prix, ni durées, ni date de disponibilité en ligne.
export type AudKey = "groupe" | "pme" | "cabinet";

export const AUDIENCES: { key: AudKey; label: string; short: string; angle: number }[] = [
  { key: "groupe", label: "un grand groupe", short: "Grand groupe", angle: 4 },
  { key: "pme", label: "une PME", short: "PME", angle: 7.5 },
  { key: "cabinet", label: "un cabinet ou un intermédiaire", short: "Cabinet", angle: 6 },
];

export const HERO: Record<AudKey, { sub: string; lead: string; cta: string; ctaSubject: string; second: { label: string; href: string } }> = {
  groupe: {
    sub: "Transformation des achats, risques tiers et conformité, avec un regard d'architecte, de la cible à la mise en production.",
    lead: "Missions de conseil, revues et programmes : transformation des achats, DORA, NIS2, gestion des risques tiers et architecture de solutions. En direct ou via votre cabinet référencé, à Bruxelles comme à Luxembourg.",
    cta: "Proposer une mission",
    ctaSubject: "Mission : premier échange avec Nicolas Simon",
    second: { label: "Voir le profil", href: "/nicolas-simon/" },
  },
  pme: {
    sub: "L'architecture de votre croissance : des outils, des données, des achats et une IA qui tournent.",
    lead: "Un architecte de solutions qui construit aussi, installé chez vous à temps partagé : site et visibilité, CRM, automatisations, agents IA, achats et NIS2. Un périmètre court et un budget validé avant de commencer.",
    cta: "Demander un diagnostic de 30 min",
    ctaSubject: "PME : diagnostic de 30 minutes",
    second: { label: "Voir les offres", href: "#offres" },
  },
  cabinet: {
    sub: "Un profil senior rare pour vos clients : architecture, achats, risques et IA dans la même personne.",
    lead: "Interim Head of Procurement, TPRM et DORA Advisor, DORA Program Manager, Enterprise ou Solution Architect, Change Manager ADKAR. Mobile en Belgique et au Luxembourg, fiche profil et CV sur demande.",
    cta: "Demander le CV",
    ctaSubject: "Cabinet : demande de CV et de disponibilité",
    second: { label: "Voir le profil détaillé", href: "/nicolas-simon/" },
  },
};

// Pas de date de disponibilité en ligne (version prudente) : la ligne d'identité nomme la personne.
export const IDENTITY = "Nicolas Simon, Enterprise & Solution Architect et Forward Deployed Engineer. Clixite, à Wavre depuis 2005.";

// ---- Offres par audience
export const OFFERS: Record<AudKey, { t: string; d: string; g: string[]; cta: string }[]> = {
  groupe: [
    { t: "Mission de conseil", d: "Un senior intégré à vos équipes sur un rôle clair : responsable de la transformation des achats, conseiller TPRM et DORA, architecte ou pilote de programme.", g: ["Sur site ou à distance, au rythme de vos équipes", "Livrables suivis en comité", "Documentation au fil de l'eau, transfert à la fin"], cta: "Proposer une mission" },
    { t: "DORA, deuxième année", d: "Vos contrats TIC critiques, vos plans de sortie et votre sous-traitance relus au regard des articles 28 à 30, avec un plan de remédiation priorisé.", g: ["Contrats critiques et clauses manquantes", "Plans de sortie et risques de concentration", "Chaîne de sous-traitance à documenter"], cta: "Cadrer la revue" },
    { t: "Revue d'architecture", d: "Un regard indépendant sur un programme ou un choix de solution, avant qu'il ne coûte trop cher.", g: ["Lecture du dossier et entretiens", "Points de rupture et alternatives", "Avis écrit, présenté à votre comité"], cta: "Demander une revue" },
  ],
  pme: [
    { t: "Diagnostic d'architecture", d: "Une photographie honnête de vos outils, de vos flux et de vos risques, et trois options chiffrées pour la suite.", g: ["Cartographie des outils et des données", "Gains rapides chiffrés", "Feuille de route sur douze mois"], cta: "Demander le diagnostic" },
    { t: "Accompagnement croissance", d: "Site, visibilité dans Google et les moteurs IA, CRM, automatisations et agents IA, mis en place puis entretenus.", g: ["Lancement intensif, puis suivi mensuel", "Indicateurs suivis chaque mois", "Vous gardez les accès et le code"], cta: "Parler de votre croissance" },
    { t: "Direction des achats à temps partagé", d: "Un CPO expérimenté, en trois temps : évaluer, construire, faire tourner. Vos achats et vos fournisseurs pilotés.", g: ["Cartographie des dépenses et des fournisseurs", "Appels d'offres et contrats clés", "Processus et outils dimensionnés à votre taille"], cta: "Structurer vos achats" },
  ],
  cabinet: [
    { t: "Rôles proposés", d: "Interim Head of Procurement ou CPO, Procurement Transformation Lead, Third-Party Risk Manager, TPRM et DORA Advisor, DORA Program Manager, Enterprise ou Solution Architect, Change Manager ADKAR.", g: ["Grands comptes régulés", "Banque, assurance, télécoms, médias", "Équipes en français, en anglais et en néerlandais"], cta: "Proposer un rôle" },
    { t: "Formats", d: "Régie à temps plein ou partiel, forfait à livrable, ou renfort ponctuel sur une phase critique.", g: ["Facturation par Clixite SRL", "Accord de confidentialité dès qu'un dossier client est partagé", "Démarrage fixé avec votre client"], cta: "Discuter du format" },
    { t: "Dossier de candidature", d: "CV à jour, références joignables et réponses à vos grilles de compétences, adaptés au rôle de votre client.", g: ["CV en français ou en anglais", "Synthèse des missions comparables", "Disponibilité et conditions"], cta: "Demander le dossier" },
  ],
};

// ---- Preuves par audience
export const CASES: Record<AudKey, { c: string; d: string; g: string }[]> = {
  groupe: [
    { c: "KBC", d: "Politique achats refondue en trois niveaux et alignée sur DORA et les exigences de l'EBA. Circuit d'achats tactiques outillé et mis en production.", g: "Mission Clixite, 18 mois auprès du CPO" },
    { c: "Groupe P&V", d: "Direction des achats par intérim pour P&V Assurances et Vivium.", g: "Mission Clixite, 2025" },
    { c: "Proximus", d: "Senior Program Manager du domaine TV, puis Procurement Lead sur un périmètre d'environ 800 M€.", g: "Parcours du fondateur, 2018 à 2024" },
  ],
  pme: [
    { c: "Design Plus", d: "Nouvelle charte graphique, refonte du site, visibilité dans les moteurs IA et prospection outillée dans HubSpot.", g: "Mission Clixite, en cours" },
    { c: "Tero", d: "Refonte du site et d'un back-office moderne pour le groupe, et site du Tero Padel Club.", g: "Mission Clixite, en cours" },
    { c: "Logiciels maison", d: "Une plateforme de conformité NIS2 et CyFun pour PME, et une plateforme de gestion des risques tiers à base d'agents IA, en phase pilote.", g: "Produits Clixite" },
  ],
  cabinet: [
    { c: "KBC", d: "18 mois comme Expert Procurement et TPRM Advisor auprès du CPO : politique achats refondue, circuit d'achats tactiques en production.", g: "Mission Clixite, 18 mois" },
    { c: "Groupe P&V", d: "Head of Procurement par intérim, P&V Assurances et Vivium.", g: "Mission Clixite, 2025" },
    { c: "Proximus", d: "Senior Program Manager TV, puis Procurement Lead (environ 800 M€).", g: "Salarié, 2018 à 2024" },
  ],
};

// ---- Solveur : questions et recommandations
export const SOLVER: Record<AudKey, { x: { id: string; label: string; rec: { title: string; first: string[]; deliverable: string; proof: string } }[]; formats: string[]; formatNotes: Record<string, string> }> = {
  groupe: {
    x: [
      { id: "dora", label: "DORA et risques tiers", rec: { title: "Diagnostic DORA des tiers, puis mission de remédiation", first: ["Relire le registre d'information et les contrats des prestataires critiques", "Mesurer les risques de concentration et les plans de sortie", "Prioriser les remédiations avec la deuxième ligne"], deliverable: "Registre fiabilisé et plan de remédiation chiffré", proof: "KBC : politique achats alignée sur DORA et l'EBA" } },
      { id: "achats", label: "Achats à transformer", rec: { title: "Transformation des achats, de la politique au Source-to-Pay", first: ["Cartographier les dépenses et les circuits d'achat", "Réécrire la politique en politique, standards et playbooks", "Mettre en production un circuit d'achats tactiques"], deliverable: "Politique, processus et outil en production", proof: "KBC : circuit d'achats tactiques en production" } },
      { id: "archi", label: "Architecture à rationaliser", rec: { title: "Revue puis architecture cible", first: ["Cartographier les applications et les flux", "Identifier doublons, dette et risques", "Dessiner la cible et la trajectoire en options chiffrées"], deliverable: "Architecture cible et feuille de route", proof: "Plus de quinze ans dans la banque, l'assurance et les télécoms" } },
      { id: "programme", label: "Programme NIS2 ou transformation à piloter", rec: { title: "Pilotage de programme et conduite du changement", first: ["Reprendre le plan, les risques et la gouvernance", "Aligner les métiers avec la méthode ADKAR", "Installer un comité qui décide"], deliverable: "Programme remis sur les rails, adoption mesurée", proof: "Proximus : Senior Program Manager du domaine TV" } },
      { id: "ia", label: "IA à mettre en production", rec: { title: "IA en production, par un Forward Deployed Engineer", first: ["Choisir un cas d'usage mesurable et ses données", "Construire avec garde-fous, traçabilité et AI Act", "Mettre en service et transférer"], deliverable: "Un cas d'usage IA en production", proof: "Deux plateformes maison à base d'agents IA, en phase pilote" } },
    ],
    formats: ["Mission sur site", "Forfait à livrable", "Avis ponctuel"],
    formatNotes: { "Mission sur site": "Un senior intégré à vos équipes, sur site ou à distance.", "Forfait à livrable": "Un livrable défini et un budget fixé avant de commencer.", "Avis ponctuel": "Un regard indépendant, rendu par écrit à votre comité." },
  },
  pme: {
    x: [
      { id: "croissance", label: "Croissance : site, visibilité, CRM", rec: { title: "Accompagnement croissance", first: ["Auditer le site, la visibilité Google et IA, le CRM", "Refaire ce qui freine, outiller la prospection", "Mesurer chaque mois et ajuster"], deliverable: "Site, CRM et prospection qui tournent", proof: "Design Plus : charte, site, moteurs IA et HubSpot" } },
      { id: "outils", label: "Des outils qui ne se parlent pas", rec: { title: "Diagnostic d'architecture, puis intégrations", first: ["Lister les outils, les exports et les doubles saisies", "Choisir ce qu'on garde, relie ou remplace", "Automatiser les flux qui coûtent le plus"], deliverable: "Outils reliés, moins de doubles saisies", proof: "Tero : site et back-office modernisés" } },
      { id: "achats", label: "Achats et fournisseurs à structurer", rec: { title: "Direction des achats à temps partagé", first: ["Cartographier les dépenses et les fournisseurs", "Renégocier les contrats qui pèsent le plus", "Installer des processus simples et un outil adapté"], deliverable: "Achats pilotés, économies documentées", proof: "Proximus : environ 800 M€ d'achats couverts" } },
      { id: "nis2", label: "NIS2 et cybersécurité", rec: { title: "Mise en conformité NIS2 et CyFun", first: ["Vérifier si vous êtes concerné et à quel niveau", "Évaluer l'écart avec le référentiel CyFun", "Prioriser les mesures et la documentation"], deliverable: "Écart mesuré et plan de conformité", proof: "Plateforme maison de conformité NIS2 pour PME, en phase pilote" } },
      { id: "ia", label: "IA à mettre au travail", rec: { title: "IA en production", first: ["Choisir la tâche répétitive qui coûte le plus", "Construire l'agent avec vos données et vos règles", "Mesurer le temps gagné"], deliverable: "Un agent IA en service", proof: "Agents IA conçus et exploités chez Clixite" } },
    ],
    formats: ["Temps partagé", "Forfait", "Atelier avec votre équipe"],
    formatNotes: { "Temps partagé": "Une présence régulière, au rythme de votre croissance.", "Forfait": "Un périmètre et un budget fixés avant de commencer.", "Atelier avec votre équipe": "Un atelier de travail avec votre équipe, et un plan d'action écrit." },
  },
  cabinet: {
    x: [
      { id: "archi", label: "Mission en architecture", rec: { title: "Enterprise ou Solution Architect", first: ["Lire le rôle, le paysage applicatif et les attentes du client", "Cibler le CV sur les chantiers d'architecture comparables", "Préparer l'entretien avec un premier avis sur le contexte"], deliverable: "Dossier de candidature ciblé", proof: "Tero et Design Plus : sites et back-offices livrés" } },
      { id: "achats", label: "Mission achats ou TPRM", rec: { title: "Procurement Transformation Lead ou TPRM Advisor", first: ["Lire le rôle, le périmètre de dépenses et l'outil en place", "Mettre en avant les missions comparables chez KBC, P&V et Proximus", "Préparer l'entretien avec une lecture de la maturité achats"], deliverable: "Dossier de candidature ciblé", proof: "Groupe P&V : direction des achats par intérim" } },
      { id: "risques", label: "Mission DORA, NIS2 ou risques", rec: { title: "DORA ou NIS2 Program Manager, Risk Program Manager", first: ["Lire le rôle et l'état du registre DORA ou du programme NIS2", "Cibler le CV sur les contrats TIC, la sous-traitance et la deuxième ligne", "Préparer l'entretien avec les points d'attention réglementaires"], deliverable: "Dossier de candidature ciblé", proof: "KBC : politique achats alignée sur DORA et l'EBA" } },
      { id: "changement", label: "Mission programme ou changement", rec: { title: "Program Manager ou Change Manager ADKAR", first: ["Lire le rôle, la gouvernance et le calendrier du programme", "Cibler le CV sur les programmes comparables et la méthode ADKAR", "Préparer l'entretien avec un premier regard sur l'adoption"], deliverable: "Dossier de candidature ciblé", proof: "Proximus : Senior Program Manager du domaine TV" } },
      { id: "ia", label: "Mission IA", rec: { title: "Responsable de la mise en production IA", first: ["Lire le rôle et le cas d'usage visé", "Joindre des démonstrations d'agents réellement exploités", "Préparer l'entretien avec les garde-fous et l'AI Act"], deliverable: "Dossier de candidature ciblé", proof: "Agents IA conçus et exploités chez Clixite" } },
    ],
    formats: ["Régie à temps plein", "Régie à temps partiel", "Forfait"],
    formatNotes: { "Régie à temps plein": "Présence à temps plein chez votre client, facturée par Clixite SRL.", "Régie à temps partiel": "Jours de présence fixés avec votre client.", "Forfait": "Un livrable défini, facturé par Clixite SRL." },
  },
};
export const URGENCY = ["Ce mois-ci", "Ce trimestre", "Plus tard"];
// ce que change l'échéance : le premier pas
export const URGENCY_NOTES: Record<string, string> = {
  "Ce mois-ci": "Un premier échange rapide pour cadrer l'urgence, puis un périmètre resserré sur ce qui ne peut pas attendre.",
  "Ce trimestre": "Un cadrage d'abord, puis un périmètre et un budget validés avant de commencer.",
  "Plus tard": "Un premier échange sans engagement pour préparer le dossier, le budget et le bon moment.",
};
