// Logos clients : prépare les fichiers officiels pour le bandeau de références.
// On ne redessine rien. Le script retire seulement l'en-tête XML, les commentaires et les métadonnées,
// recadre la viewBox sur l'encre réelle du logo, puis mesure sa densité pour l'équilibrage optique.
// Le composant ClientLogos.astro teinte ensuite chaque fichier par masque CSS (couleur du thème).
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { Resvg } from "@resvg/resvg-js";

const here = dirname(fileURLToPath(import.meta.url));
const SRC = join(here, "..", "src", "assets", "clients", "source");
const OUT = join(here, "..", "public", "clients");
const DATA = join(here, "..", "src", "data", "clients.json");
mkdirSync(OUT, { recursive: true });

// Registre : provenance et groupe. Un logo absent du registre n'est pas publié.
const registry = JSON.parse(readFileSync(join(here, "..", "src", "data", "clients.registry.json"), "utf8"));

const clean = (svg) => svg
  .replace(/<\?xml[^>]*\?>\s*/g, "")
  .replace(/<!--[\s\S]*?-->/g, "")
  .replace(/<metadata[\s\S]*?<\/metadata>/g, "")
  .replace(/\s(width|height)="[^"]*"(?=[^>]*>)/, (m) => m) // conservé puis retiré plus bas sur la racine seulement
  .trim();

const out = [];
for (const entry of registry.logos) {
  const raw = readFileSync(join(SRC, entry.file), "utf8");
  const sha = createHash("sha256").update(raw.replace(/\s+/g, "")).digest("hex");
  let svg = clean(raw);
  const vb = svg.match(/viewBox="([-\d.\s]+)"/);
  if (!vb) throw new Error(`${entry.file} : pas de viewBox`);
  const [vx, vy, vw, vh] = vb[1].trim().split(/\s+/).map(Number);
  // rendu pour mesurer l'encre (toutes couleurs confondues : on lit l'alpha)
  const W = 1600;
  const r = new Resvg(svg, { fitTo: { mode: "width", value: W }, background: "rgba(0,0,0,0)" }).render();
  const px = r.pixels; const w = r.width, h = r.height;
  let x0 = w, y0 = h, x1 = -1, y1 = -1, ink = 0;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const a = px[(y * w + x) * 4 + 3];
    if (a > 24) { ink += a / 255; if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
  }
  const k = vw / w; // unités viewBox par pixel
  const pad = 0.5 * k;
  const nx = vx + x0 * k - pad, ny = vy + y0 * k - pad, nw = (x1 - x0 + 1) * k + 2 * pad, nh = (y1 - y0 + 1) * k + 2 * pad;
  const density = ink / ((x1 - x0 + 1) * (y1 - y0 + 1));
  const f = (n) => Number(n.toFixed(3));
  svg = svg.replace(/<svg\b[^>]*>/, (tag) => tag
    .replace(/\sviewBox="[^"]*"/, ` viewBox="${f(nx)} ${f(ny)} ${f(nw)} ${f(nh)}"`)
    .replace(/\s(width|height)="[^"]*"/g, "")
    .replace(/\s(id|data-name|role|aria-labelledby)="[^"]*"/g, "")
    .replace(/\sxmlns:c2pa="[^"]*"/g, ""));
  writeFileSync(join(OUT, `${entry.id}.svg`), svg + "\n");
  out.push({ ...entry, aspect: f(nw / nh), density: f(density), sha256Source: sha, bytes: Buffer.byteLength(svg) });
}
writeFileSync(DATA, JSON.stringify(out, null, 2) + "\n");
for (const o of out) console.log(`${o.id.padEnd(16)} ratio ${String(o.aspect).padEnd(6)} densité ${String(o.density).padEnd(6)} ${o.bytes} o  ${o.group}`);
