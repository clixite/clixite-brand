// Versions Markdown du site pour les moteurs et assistants IA (proposition llmstxt.org), après astro build et typo-fr :
// - <page>/index.html.md : le contenu principal de chaque page (<main>), en Markdown propre, liens absolus ;
// - llms-full.txt : toutes les pages à la suite, chacune précédée de son adresse canonique.
// Le texte est celui de la page construite, mot pour mot : aucune divergence possible entre le HTML et le Markdown.
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join, relative } from "node:path";
import { NodeHtmlMarkdown } from "node-html-markdown";

const DIST = process.argv[2] || "dist";
const SITE = "https://www.clixite.be";
// ordre de lecture de llms-full.txt : les métiers d'abord, le FDE et le GEO en tête
const ORDER = [
  "/", "/forward-deployed-engineering/", "/geo-referencement-ia/", "/expertises/architecture-entreprise-solutions/",
  "/expertises/pilotage-de-programmes/", "/expertises/digitalisation/", "/expertises/transformation-achats/",
  "/expertises/", "/a-propos/", "/contact/", "/en/forward-deployed-engineering/", "/mentions-legales/",
];

const walk = (d) => readdirSync(d).flatMap((f) => { const p = join(d, f); return statSync(p).isDirectory() ? walk(p) : f === "index.html" ? [p] : []; });
const pick = (re, s) => (re.exec(s) || [])[1] || "";
const decode = (s) => s.replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;|&#x27;/g, "’").replace(/&lt;/g, "<").replace(/&gt;/g, ">");

// éléments sans valeur pour un lecteur de texte : décor, médias, boutons, film, X animé, fil d'Ariane
const DROP = [
  /<script\b[\s\S]*?<\/script>/gi, /<style\b[\s\S]*?<\/style>/gi, /<svg\b[\s\S]*?<\/svg>/gi, /<picture\b[\s\S]*?<\/picture>/gi,
  /<video\b[\s\S]*?<\/video>/gi, /<button\b[\s\S]*?<\/button>/gi, /<img\b[^>]*>/gi, /<source\b[^>]*>/gi,
];
function clean(html, canonical, en) {
  for (const re of DROP) html = html.replace(re, "");
  // blocs masqués aux lecteurs d'écran (film, phrases du film, X vivant, champs) : masqués ici aussi
  for (let i = 0; i < 5; i++) html = html.replace(/<(div|p|span|nav)\b[^>]*aria-hidden="true"[^>]*>(?:(?!<\1\b)[\s\S])*?<\/\1>/gi, "");
  html = html.replace(/<nav\b[^>]*class="[^"]*crumbs[^"]*"[^>]*>[\s\S]*?<\/nav>/gi, "");
  html = html.replace(/<span class="visually-hidden"[^>]*>[\s\S]*?<\/span>/gi, "");
  // boutons d'action (« Demander un échange », « Voir la méthode ») : du bruit pour un lecteur de texte
  html = html.replace(/<a\b[^>]*class="btn[^"]*"[^>]*>[\s\S]*?<\/a>/gi, "");
  // logos « Là où nous avons travaillé » : leur nom accessible devient une liste lisible
  html = html.replace(/<span class="refs__logo"[^>]*aria-label="([^"]+)"[^>]*>\s*<\/span>/gi, "$1");
  // titres de cartes dans des listes : en gras, au début de l'élément (pas de titre Markdown dans une puce)
  html = html.replace(/(<li\b[^>]*>)\s*(?:<div\b[^>]*>\s*<\/div>\s*)?<h3\b[^>]*>([\s\S]*?)<\/h3>/gi, "$1<strong>$2</strong><br>");
  // « Livrable » suivi de sa valeur
  html = html.replace(/(<p class="[^"]*(?:method__meta|fp-step__out|mp-step__out)[^"]*"[^>]*>)\s*<span[^>]*>([^<]+)<\/span>/gi, `$1<span>$2${en ? ":" : "\u00a0:"} </span>`);
  // listes de définitions (formats, questions fréquentes, faits) : le terme en gras, la définition dessous
  html = html.replace(/<dt\b[^>]*>([\s\S]*?)<\/dt>\s*<dd\b[^>]*>([\s\S]*?)<\/dd>/gi, "<p><strong>$1</strong><br>$2</p>");
  // liens absolus, ancres comprises
  html = html.replace(/href="\/(?!\/)/g, `href="${SITE}/`).replace(/href="#/g, `href="${canonical}#`);
  return html;
}

const nhm = new NodeHtmlMarkdown({ bulletMarker: "-", useInlineLinks: true, maxConsecutiveNewlines: 2, keepDataImages: false });
const pages = new Map();
for (const file of walk(DIST)) {
  const html = readFileSync(file, "utf8");
  if (/<meta name="robots" content="noindex/.test(html)) continue;
  const canonical = pick(/<link rel="canonical" href="([^"]+)"/, html);
  const path = new URL(canonical).pathname;
  const lang = pick(/<html lang="([^"]+)"/, html) || "fr-BE";
  const en = lang.startsWith("en");
  const title = decode(pick(/<title>([^<]+)<\/title>/, html));
  const description = decode(pick(/<meta name="description" content="([^"]+)"/, html));
  const modified = pick(/"dateModified":"([^"]+)"/, html) || "2026-10-26";
  const main = pick(/<main\b[^>]*>([\s\S]*)<\/main>/, html);
  let md = nhm.translate(clean(main, canonical, en)).trim();
  md = md.replace(/\n{3,}/g, "\n\n").replace(/[ \t]+\n/g, "\n");
  const head = en
    ? `Title: ${title}\nSource: ${canonical}\nLanguage: English\nUpdated: ${modified}\nPublisher: Clixite SRL, Wavre, Belgium (company number 0871.430.776)\nSummary: ${description}`
    : `Titre : ${title}\nSource : ${canonical}\nLangue : français (Belgique)\nMise à jour : ${modified}\nÉditeur : Clixite SRL, Wavre, Belgique (BCE 0871.430.776)\nRésumé : ${description}`;
  const out = `${head}\n\n${md}\n`;
  writeFileSync(file + ".md", out);
  pages.set(path, { out, title, canonical });
}

const ordered = [...ORDER.filter((p) => pages.has(p)), ...[...pages.keys()].filter((p) => !ORDER.includes(p)).sort()];
const full = [
  "# Clixite : contenu complet du site www.clixite.be",
  "",
  "> Toutes les pages de www.clixite.be, en Markdown, dans l'ordre de lecture conseillé. Chaque page commence par son adresse canonique : citez cette adresse. Le sommaire est dans https://www.clixite.be/llms.txt.",
  "",
  ...ordered.flatMap((p) => ["* * *", "", pages.get(p).out]),
].join("\n");
writeFileSync(join(DIST, "llms-full.txt"), full);
console.log(`llms : ${pages.size} page(s) en Markdown, llms-full.txt ${Math.round(full.length / 1024)} Ko (${relative(process.cwd(), DIST)})`);
