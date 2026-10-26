// Typographie française sur le HTML construit (après astro build) : espaces insécables et apostrophes typographiques.
// Ne touche qu'au texte entre les balises, jamais aux attributs, aux scripts, aux styles ni aux SVG.
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const NBSP = " ", NNBSP = " ";
const fixText = (t) => t
  .replace(/&#39;|&#x27;/g, "'")
  .replace(/'/g, "’")
  .replace(/[  ]+([:])/g, NBSP + "$1")
  .replace(/[   ]+([;!?])/g, NNBSP + "$1")
  .replace(/«[  ]*/g, "«" + NBSP)
  .replace(/[  ]*»/g, NBSP + "»")
  .replace(/≈ /g, "≈" + NBSP)
  .replace(/(\d) (M€|€|%|min\b|jours?\b|semaines?\b|personnes\b|ans\b)/g, "$1" + NBSP + "$2")
  .replace(/(\d) (\d{3})\b/g, "$1" + NNBSP + "$2");

export function typo(html) {
  // On avance balise par balise ; les blocs script, style, svg, code, pre et textarea sont recopiés tels quels
  // jusqu'à leur balise fermante (le CSS minifié contient des « < » dans les requêtes média).
  const out = []; let i = 0;
  const re = /<[^>]+>/g; let m;
  while ((m = re.exec(html))) {
    out.push(fixText(html.slice(i, m.index)));
    const tag = m[0]; const open = /^<(script|style|svg|code|pre|textarea)\b/i.exec(tag);
    if (open && !tag.endsWith("/>")) {
      const name = open[1].toLowerCase();
      const endIdx = html.toLowerCase().indexOf(`</${name}`, re.lastIndex);
      const stop = endIdx === -1 ? html.length : html.indexOf(">", endIdx) + 1;
      out.push(html.slice(m.index, stop)); re.lastIndex = stop; i = stop; continue;
    }
    out.push(tag); i = re.lastIndex;
  }
  out.push(fixText(html.slice(i)));
  return out.join("");
}

const walk = (d) => readdirSync(d).flatMap((f) => { const p = join(d, f); return statSync(p).isDirectory() ? walk(p) : p.endsWith(".html") ? [p] : []; });
const dir = process.argv[2] || "dist";   // un dossier (site construit) ou un seul fichier .html (charte)
let n = 0;
for (const f of dir.endsWith(".html") ? [dir] : walk(dir)) { const s = readFileSync(f, "utf8"); if (!/<html[^>]*\blang="fr/i.test(s)) continue; const t = typo(s); if (t !== s) { writeFileSync(f, t); n++; } }
console.log(`typo-fr : ${n} page(s) corrigée(s) dans ${dir}`);
