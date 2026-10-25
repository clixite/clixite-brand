// Gabarit PowerPoint Clixite : un thème, huit mises en page, des slides d'exemple à remplacer.
const pptxgen = require("pptxgenjs");
const path = require("path");
const { applyTheme } = require("/root/.claude/skills/synced/c12811fc-6372-468e-a4d3-c888b257d183_c185d6f6-3c2e-4bcd-a4c1-02bd3e93bf11/pptx/scripts/apply_theme.js");

const L = path.join(__dirname, "charte/downloads/logo");
const IMG = {
  reliefInverse: path.join(L, "clixite-relief-inverse-transparent-1600px.png"),
  reliefColor: path.join(L, "clixite-relief-color-transparent-1600px.png"),
  reliefMono: path.join(L, "clixite-relief-mono-transparent-1600px.png"),
  xReliefInverse: path.join(L, "x-relief-inverse-transparent-1024px.png"),
  xVivantInverse: path.join(L, "x-vivant-inverse-transparent-1024px.png"),
  xReliefColor: path.join(L, "x-relief-color-transparent-1024px.png"),
  xMono: path.join(L, "x-maitre-mono-transparent-1024px.png"),
};

const THEME = {
  name: "Clixite",
  headFontFace: "Space Grotesk",
  bodyFontFace: "Inter",
  colors: {
    dk1: "0B2239", lt1: "FFFFFF", dk2: "4B5A6B", lt2: "F6F5F0",
    accent1: "19B3D9", accent2: "FF4F8B", accent3: "FFD233", accent4: "0C7893", accent5: "193776", accent6: "CDD5DD",
    hlink: "0C7893", folHlink: "193776",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.author = "Clixite";
pres.company = "Clixite SRL";
pres.title = "Gabarit Clixite";
const C = pres.SchemeColor;
const W = 13.33, H = 7.5, M = 0.6;

// ---- Layouts ---------------------------------------------------------------
pres.defineSlideMaster({
  title: "COUVERTURE", background: { color: C.text1 },
  objects: [
    { image: { x: 8.1, y: 0.4, w: 5.0, h: 5.0, path: IMG.xVivantInverse } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.3, w: 7.2, h: 2.2, fontSize: 44, bold: true, align: "left", color: C.background2, valign: "bottom", margin: 0 }, text: "Titre de la présentation" } },
    { placeholder: { options: { name: "body", type: "body", x: M, y: 4.65, w: 7.2, h: 0.9, fontSize: 18, align: "left", color: "CDD5DD", margin: 0 }, text: "Sous-titre, client, date" } },
    { image: { x: M, y: 6.3, w: 2.6, h: 0.6, path: IMG.reliefInverse } },
    { text: { text: "ENTERPRISE & SOLUTION ARCHITECTURE", options: { x: 3.5, y: 6.42, w: 6, h: 0.4, fontSize: 9, color: C.accent1, charSpacing: 3, margin: 0 } } },
  ],
});
pres.defineSlideMaster({
  title: "SECTION", background: { color: C.text1 },
  objects: [
    { image: { x: 9.6, y: -0.9, w: 5.2, h: 5.2, path: IMG.xReliefInverse } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.6, w: 8.5, h: 1.8, fontSize: 40, bold: true, align: "left", color: C.background2, valign: "bottom", margin: 0 }, text: "Titre de section" } },
    { placeholder: { options: { name: "body", type: "body", x: M, y: 4.55, w: 8.5, h: 0.8, fontSize: 16, align: "left", color: "CDD5DD", margin: 0 }, text: "Une phrase qui dit ce que la section décide" } },
    { text: { text: "01", options: { name: "num", x: M, y: 1.2, w: 3, h: 1.2, fontSize: 56, bold: true, color: C.accent1, margin: 0, fontFace: "Space Grotesk" } } },
  ],
});
const footer = (dark) => [
  { image: { x: M, y: H - 0.62, w: 1.45, h: 0.33, path: dark ? IMG.reliefInverse : IMG.reliefMono } },
  { text: { text: "Confidentiel", options: { x: W - 4.6, y: H - 0.62, w: 3.0, h: 0.33, fontSize: 9, color: dark ? "CDD5DD" : C.text2, align: "right", margin: 0 } } },
];
const contentTitle = (dark) => ({ placeholder: { options: { name: "title", type: "title", x: M, y: 0.5, w: W - 2 * M, h: 1.0, fontSize: 30, bold: true, align: "left", color: dark ? C.background2 : C.text1, valign: "middle", margin: 0 }, text: "Titre de la slide" } });
pres.defineSlideMaster({
  title: "CONTENU", background: { color: C.background1 },
  objects: [contentTitle(false),
    { placeholder: { options: { name: "body", type: "body", x: M, y: 1.7, w: W - 2 * M, h: 4.9, fontSize: 16, color: C.text1, margin: 0, paraSpaceAfter: 8, valign: "top" }, text: "Texte" } },
    ...footer(false)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: C.text2, align: "right" },
});
pres.defineSlideMaster({
  title: "TITRE_SEUL", background: { color: C.background1 },
  objects: [contentTitle(false), ...footer(false)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: C.text2, align: "right" },
});
pres.defineSlideMaster({
  title: "TITRE_SEUL_SOMBRE", background: { color: C.text1 },
  objects: [contentTitle(true), ...footer(true)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: "CDD5DD", align: "right" },
});
pres.defineSlideMaster({
  title: "DEUX_COLONNES", background: { color: C.background1 },
  objects: [contentTitle(false),
    { placeholder: { options: { name: "body", type: "body", x: M, y: 1.7, w: 5.8, h: 4.9, fontSize: 16, color: C.text1, margin: 0, paraSpaceAfter: 8, valign: "top" }, text: "Colonne gauche" } },
    { placeholder: { options: { name: "body2", type: "body", x: 7.0, y: 1.7, w: 5.73, h: 4.9, fontSize: 16, color: C.text1, margin: 0, paraSpaceAfter: 8, valign: "top" }, text: "Colonne droite" } },
    ...footer(false)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: C.text2, align: "right" },
});
pres.defineSlideMaster({
  title: "GRAPHIQUE", background: { color: C.background1 },
  objects: [contentTitle(false),
    { placeholder: { options: { name: "chart", type: "chart", x: M, y: 1.7, w: 7.6, h: 4.9, color: C.text1 }, text: "Graphique" } },
    { placeholder: { options: { name: "body", type: "body", x: 8.6, y: 1.7, w: 4.13, h: 4.9, fontSize: 14, color: C.text1, margin: 0, paraSpaceAfter: 8, valign: "top" }, text: "Lecture du graphique" } },
    ...footer(false)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: C.text2, align: "right" },
});
pres.defineSlideMaster({
  title: "TABLEAU", background: { color: C.background1 }, margin: [0.5, 0.6, 1.0, 0.6],
  objects: [contentTitle(false),
    { placeholder: { options: { name: "table", type: "tbl", x: M, y: 1.7, w: W - 2 * M, h: 4.6, color: C.text1 }, text: "Tableau" } },
    ...footer(false)],
  slideNumber: { x: W - 1.3, y: H - 0.62, w: 0.7, h: 0.33, fontSize: 9, color: C.text2, align: "right" },
});
pres.defineSlideMaster({
  title: "CLOTURE", background: { color: C.text1 },
  objects: [
    { image: { x: 4.37, y: 1.1, w: 4.6, h: 4.6, path: IMG.xReliefInverse } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 5.6, w: W - 2 * M, h: 0.8, fontSize: 28, bold: true, color: C.background2, align: "center", margin: 0 }, text: "Merci" } },
    { placeholder: { options: { name: "body", type: "body", x: M, y: 6.4, w: W - 2 * M, h: 0.6, fontSize: 13, color: "CDD5DD", align: "center", margin: 0 }, text: "nicolas@clixite.be · clixite.be" } },
  ],
});

// ---- Example slides ------------------------------------------------------
pres.addSection({ title: "Ouverture" });
let s = pres.addSlide({ masterName: "COUVERTURE", sectionTitle: "Ouverture" });
s.addText("Tactical Sourcing : passer en production", { placeholder: "title" });
s.addText("Comité de pilotage · Nom du client · 25 octobre 2026", { placeholder: "body" });
s.addNotes("Couverture : le titre dit la décision attendue. Remplacer le sous-titre par client et date. Ne jamais changer la position du X.");

s = pres.addSlide({ masterName: "SECTION", sectionTitle: "Ouverture" });
s.addText("Où nous en sommes", { placeholder: "title" });
s.addText("Trois faits, aucune opinion", { placeholder: "body" });
s.addNotes("Section : numéro en haut à gauche (modifier le texte 01, 02...). Une phrase sous le titre, jamais un paragraphe.");

pres.addSection({ title: "Contenu" });
s = pres.addSlide({ masterName: "CONTENU", sectionTitle: "Contenu" });
s.addText("Ce que nous avons livré ce trimestre", { placeholder: "title" });
s.addText([
  { text: "Policy achats v2.0 en production, alignée DORA, EBA et NIS2", options: { bullet: true, breakLine: true } },
  { text: "Light track IT tiers 4 et 5 sous SAP Ariba, délai moyen 9 jours", options: { bullet: true, breakLine: true } },
  { text: "Trois playbooks fournisseurs rédigés et validés par le risque", options: { bullet: true, breakLine: true } },
  { text: "Reste à faire : intégration World-Check au flux de qualification", options: { bullet: true } },
], { placeholder: "body" });
s.addNotes("Contenu : quatre puces maximum, verbes d'action, chiffres. Sinon, passer en deux colonnes ou en cartes.");

s = pres.addSlide({ masterName: "TITRE_SEUL", sectionTitle: "Contenu" });
s.addText("Trois chiffres qui comptent", { placeholder: "title" });
const stats = [["9 j", "délai moyen de qualification", C.accent1], ["800 M€", "d'achats sous contrôle", C.accent2], ["100 %", "des fournisseurs critiques évalués", C.accent4]];
stats.forEach(([n, l, col], i) => {
  const x = M + i * 4.1;
  s.addShape(pres.ShapeType.roundRect, { x, y: 2.0, w: 3.75, h: 3.6, fill: { color: C.background2 }, line: { color: C.background2 }, rectRadius: 0.12, objectName: `carte-${i + 1}` });
  s.addText(n, { x: x + 0.35, y: 2.4, w: 3.1, h: 1.4, fontSize: 54, bold: true, color: col, margin: 0, isTextBox: true, fontFace: "Space Grotesk", objectName: `chiffre-${i + 1}` });
  s.addText(l, { x: x + 0.35, y: 3.9, w: 3.1, h: 1.2, fontSize: 15, color: C.text2, margin: 0, isTextBox: true, objectName: `libelle-${i + 1}` });
});
s.addNotes("Cartes KPI : trois chiffres, un accent par carte (turquoise, rose, turquoise profond). Jamais plus de trois.");

s = pres.addSlide({ masterName: "DEUX_COLONNES", sectionTitle: "Contenu" });
s.addText("Option A ou option B", { placeholder: "title" });
s.addText([{ text: "Option A : conserver l'outil actuel", options: { bold: true, breakLine: true } }, { text: "Coût stable, aucune migration, dette technique qui grandit", options: { bullet: true, breakLine: true } }, { text: "Risque : non-conformité DORA au 1er janvier", options: { bullet: true } }], { placeholder: "body" });
s.addText([{ text: "Option B : migrer en douze semaines", options: { bold: true, breakLine: true } }, { text: "Investissement initial, conformité acquise, équipe à former", options: { bullet: true, breakLine: true } }, { text: "Recommandation : B, avec un pilote sur un périmètre", options: { bullet: true } }], { placeholder: "body2" });
s.addNotes("Deux colonnes : comparer, puis recommander dans la dernière puce de droite.");

s = pres.addSlide({ masterName: "GRAPHIQUE", sectionTitle: "Contenu" });
s.addText("Délai de qualification fournisseur, en jours", { placeholder: "title" });
s.addChart(pres.ChartType.bar, [{ name: "Jours", labels: ["T1", "T2", "T3", "T4"], values: [21, 17, 12, 9] }], {
  placeholder: "chart", barDir: "col", chartColors: [THEME.colors.accent1], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: THEME.colors.dk1, dataLabelFontFace: "+mn-lt", dataLabelFontSize: 12,
  catAxisLabelColor: THEME.colors.dk2, valAxisLabelColor: THEME.colors.dk2, catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", valGridLine: { color: THEME.colors.accent6, size: 0.5 }, catGridLine: { style: "none" }, showLegend: false, showTitle: false, valAxisMinVal: 0,
});
s.addText([{ text: "Lecture", options: { bold: true, breakLine: true } }, { text: "Le délai a été divisé par deux en trois trimestres grâce au light track.", options: { breakLine: true } }, { text: "L'objectif de 7 jours est atteignable au T2 avec l'intégration World-Check.", options: {} }], { placeholder: "body" });
s.addNotes("Graphique : une série, une couleur, étiquettes de valeur. Deux séries : turquoise puis rose. La lecture tient en deux phrases.");

s = pres.addSlide({ masterName: "TABLEAU", sectionTitle: "Contenu" });
s.addText("Plan d'actions", { placeholder: "title" });
s.addTable([
  [{ text: "Action", options: { bold: true, color: THEME.colors.dk1, fill: { color: THEME.colors.lt2 } } }, { text: "Responsable", options: { bold: true, color: THEME.colors.dk1, fill: { color: THEME.colors.lt2 } } }, { text: "Échéance", options: { bold: true, color: THEME.colors.dk1, fill: { color: THEME.colors.lt2 } } }, { text: "Statut", options: { bold: true, color: THEME.colors.dk1, fill: { color: THEME.colors.lt2 } } }],
  ["Intégrer World-Check au flux", "Nicolas Simon", "15 novembre", "En cours"],
  ["Former l'équipe achats au light track", "Responsable achats", "30 novembre", "À planifier"],
  ["Valider les playbooks avec le risque", "CRO", "10 décembre", "Fait"],
], { placeholder: "table", x: M, y: 1.7, w: W - 2 * M, autoPageSlideStartY: 1.7, colW: [5.2, 2.8, 2.1, 2.03], fontSize: 13, color: THEME.colors.dk1, border: { type: "solid", color: THEME.colors.accent6, pt: 0.5 }, rowH: 0.5, valign: "middle" });
s.addNotes("Tableau : en-tête sur fond Papier, filets Brume, pas de zébrage. Les statuts en texte, pas en couleur seule.");

s = pres.addSlide({ masterName: "TITRE_SEUL_SOMBRE", sectionTitle: "Contenu" });
s.addText("Décision demandée aujourd'hui", { placeholder: "title" });
s.addShape(pres.ShapeType.roundRect, { x: M, y: 1.9, w: W - 2 * M, h: 3.6, fill: { color: "122D4A" }, line: { color: "122D4A" }, rectRadius: 0.12, objectName: "cadre-decision" });
s.addText("Lancer la migration en option B, avec un pilote sur le périmètre IT tiers 4 et 5 dès le 1er décembre.", { x: M + 0.5, y: 2.3, w: W - 2 * M - 1.0, h: 1.6, fontSize: 26, bold: true, color: THEME.colors.lt2, margin: 0, isTextBox: true, fontFace: "Space Grotesk", objectName: "decision" });
s.addText("Budget : 48 k€ · Durée : 12 semaines · Risque principal : disponibilité de l'équipe achats en décembre", { x: M + 0.5, y: 4.1, w: W - 2 * M - 1.0, h: 1.0, fontSize: 15, color: "CDD5DD", margin: 0, isTextBox: true, objectName: "decision-detail" });
s.addNotes("Slide sombre : réservée au moment clé (décision, chiffre choc). Une par deck.");

pres.addSection({ title: "Clôture" });
s = pres.addSlide({ masterName: "CLOTURE", sectionTitle: "Clôture" });
s.addText("Merci", { placeholder: "title" });
s.addText("Nicolas Simon · nicolas@clixite.be · clixite.be", { placeholder: "body" });
s.addNotes("Clôture : le X en couleur revient. Contacts en une ligne.");

(async () => {
  const out = path.join(__dirname, "charte/downloads/office/Clixite-gabarit-presentation.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("written", out);
})();
