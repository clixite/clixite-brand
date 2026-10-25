// Contenu par audience. Le site s'adapte à l'acheteur : grand groupe régulé, PME, cabinet ou intermédiaire.
// Tout ce qui n'est pas confirmé par Nicolas porte av: true (surligné en prévisualisation).
export type AudKey = "groupe" | "pme" | "cabinet";

export const AUDIENCES: { key: AudKey; label: string; short: string; angle: number }[] = [
  { key: "groupe", label: "un grand groupe", short: "Grand groupe", angle: 4 },
  { key: "pme", label: "une PME", short: "PME", angle: 7.5 },
  { key: "cabinet", label: "un cabinet de conseil", short: "Cabinet", angle: 6 },
];

export const HERO: Record<AudKey, { sub: string; lead: string; cta: string; ctaSubject: string; second: { label: string; href: string } }> = {
  groupe: {
    sub: "Architecture, achats et conformité pour les groupes régulés, de la cible à la mise en production.",
    lead: "Missions de trois à dix-huit mois en architecture d'entreprise, transformation des achats, DORA, NIS2 et gestion des risques tiers. En direct ou via votre cabinet référencé, à Bruxelles comme à Luxembourg.",
    cta: "Vérifier ma disponibilité",
    ctaSubject: "Mission : vérifier la disponibilité de Nicolas Simon",
    second: { label: "Voir le profil", href: "/nicolas-simon/" },
  },
  pme: {
    sub: "L'architecture de votre croissance : des outils, des données, des achats et une IA qui tournent.",
    lead: "Un architecte et ingénieur qui s'installe chez vous à temps partagé : site et visibilité, CRM, automatisations, agents IA, achats et NIS2. Un périmètre court et un prix annoncé avant de commencer.",
    cta: "Réserver un diagnostic de 30 min",
    ctaSubject: "PME : diagnostic de 30 minutes",
    second: { label: "Voir les offres", href: "#offres" },
  },
  cabinet: {
    sub: "Un profil senior rare pour vos clients : architecture, achats, risques et IA dans la même personne.",
    lead: "Enterprise & Solution Architect, Procurement et TPRM Advisor, Program et Change Manager. Certifié PMP, PRINCE2, SAFe, ITIL et ADKAR. Mobile en Belgique et au Luxembourg, profil et CV sur demande.",
    cta: "Demander le CV",
    ctaSubject: "Cabinet : demande de CV et de disponibilité",
    second: { label: "Voir le profil détaillé", href: "/nicolas-simon/" },
  },
};

export const AVAILABILITY = { text: "Disponible pour une nouvelle mission à partir de novembre 2026.", av: true };

// ---- Offres par audience
export const OFFERS: Record<AudKey, { t: string; dur: string; d: string; g: string[]; cta: string }[]> = {
  groupe: [
    { t: "Mission de conseil", dur: "3 à 18 mois", d: "Un senior intégré à vos équipes sur un rôle clair : architecte, responsable de la transformation des achats, conseiller TPRM et DORA, ou pilote de programme.", g: ["Démarrage rapide, sur site 2 à 5 jours par semaine", "Livrables suivis en comité", "Transfert documenté à la fin"], cta: "Proposer une mission" },
    { t: "Diagnostic DORA des tiers", dur: "15 jours", d: "Votre registre d'information, vos prestataires TIC critiques et vos contrats passés au crible, avec un plan de remédiation priorisé.", g: ["Registre et cartographie des tiers", "Risques de concentration et plans de sortie", "Clauses contractuelles à renégocier"], cta: "Cadrer le diagnostic" },
    { t: "Revue d'architecture", dur: "5 jours", d: "Un regard indépendant sur un programme ou un choix de solution, avant qu'il ne coûte trop cher.", g: ["Lecture du dossier et entretiens", "Points de rupture et alternatives", "Avis écrit, présenté à votre comité"], cta: "Demander une revue" },
  ],
  pme: [
    { t: "Diagnostic d'architecture", dur: "10 jours", d: "Une photographie honnête de vos outils, de vos flux et de vos risques, et trois options chiffrées pour la suite.", g: ["Cartographie des outils et des données", "Gains rapides chiffrés", "Feuille de route sur douze mois"], cta: "Demander le diagnostic" },
    { t: "Accompagnement croissance", dur: "Lancement de 3 à 4 mois", d: "Site, visibilité dans Google et les moteurs IA, CRM, automatisations et agents IA, mis en place puis entretenus.", g: ["Lancement intensif, puis suivi mensuel", "Indicateurs suivis chaque mois", "Vous gardez les accès et le code"], cta: "Parler de votre croissance" },
    { t: "Direction des achats à temps partagé", dur: "1 à 2 jours par semaine", d: "Un CPO expérimenté, en trois temps : évaluer, construire, faire tourner. Vos achats et vos fournisseurs enfin pilotés.", g: ["Cartographie des dépenses et des fournisseurs", "Appels d'offres et contrats clés", "Processus et outils dimensionnés à votre taille"], cta: "Structurer vos achats" },
  ],
  cabinet: [
    { t: "Rôles proposés", dur: "Senior", d: "Enterprise ou Solution Architect, Procurement Transformation Lead, TPRM et DORA Advisor, Program ou Change Manager (ADKAR), responsable de la mise en production IA.", g: ["Grands comptes régulés et secteur public", "Banque, assurance, télécoms, médias", "Équipes en français, en anglais et en néerlandais"], cta: "Proposer un rôle" },
    { t: "Formats", dur: "Souples", d: "Régie à temps plein ou partiel, forfait à livrable, ou renfort ponctuel sur une phase critique.", g: ["Facturation par Clixite SRL", "Accord de confidentialité avant tout échange", "Démarrage sous deux semaines"], cta: "Discuter du format" },
    { t: "Dossier de candidature", dur: "Sous 24 h", d: "CV à jour, références joignables et réponses à vos grilles de compétences, adaptés au rôle de votre client.", g: ["CV en français ou en anglais", "Synthèse des missions comparables", "Disponibilité et conditions"], cta: "Demander le dossier" },
  ],
};
export const OFFERS_AV = true; // durées, formats et délais à confirmer

// ---- Preuves par audience
export const CASES: Record<AudKey, { c: string; d: string; g: string }[]> = {
  groupe: [
    { c: "KBC", d: "Politique achats v2.0 (politique, standards, playbooks) alignée sur DORA, l'EBA, NIS2 et la CSRD. Circuit d'achats tactiques en production depuis janvier 2026 sur SAP Ariba.", g: "Mission Clixite, 18 mois auprès du CPO" },
    { c: "Groupe P&V", d: "Direction des achats par intérim pour P&V Assurances et Vivium, de janvier à mi-2025.", g: "Mission Clixite" },
    { c: "Proximus", d: "Procurement Lead sur un périmètre d'environ 800 M€, puis Senior Program Manager du domaine TV.", g: "Parcours du fondateur, 2018 à 2024" },
  ],
  pme: [
    { c: "Design Plus", d: "Nouvelle charte graphique, refonte du site, visibilité dans les moteurs IA et prospection outillée dans HubSpot.", g: "Mission Clixite, en cours" },
    { c: "Tero", d: "Refonte du site et d'un back-office moderne pour le groupe, et site du Tero Padel Club.", g: "Mission Clixite, en cours" },
    { c: "Logiciels maison", d: "Une plateforme de conformité NIS2 et CyFun pour PME, et une plateforme de gestion des risques tiers orchestrée par agents IA.", g: "Produits Clixite" },
  ],
  cabinet: [
    { c: "KBC", d: "18 mois comme Expert Procurement et TPRM Advisor auprès du CPO : politique v2.0 et circuit d'achats tactiques sur SAP Ariba.", g: "Mission Clixite, terminée en septembre 2026" },
    { c: "Groupe P&V", d: "Head of Procurement par intérim, P&V Assurances et Vivium.", g: "Mission Clixite, 2025" },
    { c: "Proximus", d: "Procurement Lead (environ 800 M€) et Senior Program Manager TV.", g: "Salarié, 2018 à 2024" },
  ],
};

// ---- Solveur : questions et recommandations
export const SOLVER: Record<AudKey, { x: { id: string; label: string; rec: { title: string; first: string[]; deliverable: string; duration: string; proof: string } }[]; formats: string[] }> = {
  groupe: {
    x: [
      { id: "dora", label: "DORA et risques tiers", rec: { title: "Diagnostic DORA des tiers, puis mission de remédiation", first: ["Relire le registre d'information et les contrats des prestataires critiques", "Mesurer les risques de concentration et les plans de sortie", "Prioriser les remédiations avec la deuxième ligne"], deliverable: "Registre fiabilisé et plan de remédiation chiffré", duration: "15 jours, puis 3 à 6 mois", proof: "KBC : politique achats alignée sur DORA et l'EBA" } },
      { id: "achats", label: "Achats à transformer", rec: { title: "Transformation des achats, de la politique au Source-to-Pay", first: ["Cartographier les dépenses et les circuits d'achat", "Réécrire la politique en politique, standards et playbooks", "Mettre en production un circuit d'achats tactiques"], deliverable: "Politique, processus et outil en production", duration: "6 à 18 mois", proof: "KBC : circuit tactique en production sur SAP Ariba" } },
      { id: "archi", label: "Architecture à rationaliser", rec: { title: "Revue puis architecture cible", first: ["Cartographier les applications et les flux", "Identifier doublons, dette et risques", "Dessiner la cible et la trajectoire en options chiffrées"], deliverable: "Architecture cible et feuille de route", duration: "5 jours de revue, puis 1 à 3 mois", proof: "Plus de quinze ans dans la banque, l'assurance et les télécoms" } },
      { id: "programme", label: "Programme NIS2 ou transformation à piloter", rec: { title: "Pilotage de programme et conduite du changement", first: ["Reprendre le plan, les risques et la gouvernance", "Aligner les métiers avec la méthode ADKAR", "Installer un comité qui décide"], deliverable: "Programme remis sur les rails, adoption mesurée", duration: "6 à 16 mois", proof: "Proximus : Senior Program Manager du domaine TV" } },
      { id: "ia", label: "IA à mettre en production", rec: { title: "IA en production, en Forward Deployed Engineer", first: ["Choisir un cas d'usage mesurable et ses données", "Construire avec garde-fous, traçabilité et AI Act", "Mettre en service et transférer"], deliverable: "Un cas d'usage IA en production", duration: "4 à 8 semaines", proof: "Plateformes maison orchestrées par agents IA" } },
    ],
    formats: ["Mission sur site", "Forfait à livrable", "Avis ponctuel"],
  },
  pme: {
    x: [
      { id: "croissance", label: "Croissance : site, visibilité, CRM", rec: { title: "Accompagnement croissance", first: ["Auditer le site, la visibilité Google et IA, le CRM", "Refaire ce qui freine, outiller la prospection", "Mesurer chaque mois et ajuster"], deliverable: "Site, CRM et prospection qui tournent", duration: "Lancement de 3 à 4 mois, puis suivi", proof: "Design Plus : charte, site, moteurs IA et HubSpot" } },
      { id: "outils", label: "Des outils qui ne se parlent pas", rec: { title: "Diagnostic d'architecture, puis intégrations", first: ["Lister les outils, les exports et les doubles saisies", "Choisir ce qu'on garde, relie ou remplace", "Automatiser les flux qui coûtent le plus"], deliverable: "Outils reliés, saisies divisées", duration: "10 jours, puis 1 à 3 mois", proof: "Tero : site et back-office modernisés" } },
      { id: "achats", label: "Achats et fournisseurs à structurer", rec: { title: "Direction des achats à temps partagé", first: ["Cartographier les dépenses et les fournisseurs", "Renégocier les contrats qui pèsent le plus", "Installer des processus simples et un outil adapté"], deliverable: "Achats pilotés, économies documentées", duration: "1 à 2 jours par semaine, 6 mois et plus", proof: "Proximus : environ 800 M€ d'achats couverts" } },
      { id: "nis2", label: "NIS2 et cybersécurité", rec: { title: "Mise en conformité NIS2 et CyFun", first: ["Vérifier si vous êtes concerné et à quel niveau", "Évaluer l'écart avec le référentiel CyFun", "Prioriser les mesures et la documentation"], deliverable: "Écart mesuré et plan de conformité", duration: "10 jours, puis suivi", proof: "Plateforme de conformité NIS2 pour PME" } },
      { id: "ia", label: "IA à mettre au travail", rec: { title: "IA en production", first: ["Choisir la tâche répétitive qui coûte le plus", "Construire l'agent avec vos données et vos règles", "Mesurer le temps gagné"], deliverable: "Un agent IA en service", duration: "4 semaines", proof: "Agents IA conçus et exploités en interne" } },
    ],
    formats: ["Temps partagé", "Forfait", "Atelier d'une journée"],
  },
  cabinet: {
    x: [
      { id: "archi", label: "Mission en architecture", rec: { title: "Enterprise ou Solution Architect", first: ["Lecture du rôle et du contexte client", "CV ciblé et références comparables", "Entretien sous 48 heures"], deliverable: "Dossier de candidature complet", duration: "Réponse sous 24 heures", proof: "Architecture d'entreprise et de solutions, grands comptes et PME" } },
      { id: "achats", label: "Mission achats ou TPRM", rec: { title: "Procurement Transformation Lead ou TPRM Advisor", first: ["Lecture du rôle et du contexte client", "CV ciblé et références comparables", "Entretien sous 48 heures"], deliverable: "Dossier de candidature complet", duration: "Réponse sous 24 heures", proof: "KBC, Groupe P&V et Proximus" } },
      { id: "risques", label: "Mission DORA, NIS2 ou risques", rec: { title: "DORA ou NIS2 Program Manager, Risk Program Manager", first: ["Lecture du rôle et du contexte client", "CV ciblé et références comparables", "Entretien sous 48 heures"], deliverable: "Dossier de candidature complet", duration: "Réponse sous 24 heures", proof: "Politique achats KBC alignée sur DORA, NIS2 et l'EBA" } },
      { id: "changement", label: "Mission programme ou changement", rec: { title: "Program Manager ou Change Manager ADKAR", first: ["Lecture du rôle et du contexte client", "CV ciblé et références comparables", "Entretien sous 48 heures"], deliverable: "Dossier de candidature complet", duration: "Réponse sous 24 heures", proof: "PMP, PRINCE2, SAFe et ADKAR" } },
      { id: "ia", label: "Mission IA", rec: { title: "Responsable de la mise en production IA", first: ["Lecture du rôle et du contexte client", "CV ciblé et démonstrations", "Entretien sous 48 heures"], deliverable: "Dossier de candidature complet", duration: "Réponse sous 24 heures", proof: "Agents et plateformes IA construits en production" } },
    ],
    formats: ["Régie à temps plein", "Régie à temps partiel", "Forfait"],
  },
};
export const URGENCY = ["Ce mois-ci", "Ce trimestre", "Plus tard"];
