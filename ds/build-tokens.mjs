// Clixite Design System 2.0 : compile les tokens DTCG en variables CSS et contrôle les contrastes.
// Usage : node ds/build-tokens.mjs  (échoue avec le code 1 si une paire texte/fond passe sous WCAG AA)
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const read = (f) => JSON.parse(readFileSync(join(here, "tokens", f), "utf8"));
const prim = read("primitives.tokens.json");
const themes = read("themes.tokens.json");
const tree = { ...prim, ...themes };

const get = (path) => path.split(".").reduce((o, k) => (o ? o[k] : undefined), tree);
const resolve = (v) => {
  if (typeof v === "string" && /^\{[^}]+\}$/.test(v)) {
    const t = get(v.slice(1, -1));
    if (!t) throw new Error(`Alias introuvable : ${v}`);
    return resolve(t.$value);
  }
  return v;
};
const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
const css = (type, v) => {
  v = resolve(v);
  if (type === "fontFamily") return v.map((f) => (/\s/.test(f) ? `"${f}"` : f)).join(", ");
  if (type === "cubicBezier") return `cubic-bezier(${v.join(", ")})`;
  return String(v);
};

const lines = [];
const walk = (node, prefix, out) => {
  for (const [k, v] of Object.entries(node)) {
    if (k.startsWith("$")) continue;
    const name = prefix ? `${prefix}-${k}` : k;
    if (v && typeof v === "object" && "$value" in v) {
      if (v.$type === "typography") {
        for (const [p, pv] of Object.entries(v.$value)) out.push([`${name}-${kebab(p)}`, css(p === "fontFamily" ? "fontFamily" : "x", pv)]);
      } else out.push([name, css(v.$type, v.$value)]);
    } else if (v && typeof v === "object") walk(v, name, out);
  }
};

const root = [];
for (const key of ["color", "font", "space", "radius", "duration", "easing", "dataviz", "type", "layout"]) {
  const node = tree[key];
  if (node) walk(node, key === "color" ? "color" : key, root);
}
const themeVars = {};
for (const [name, node] of Object.entries(tree.theme)) { themeVars[name] = []; walk(node, "", themeVars[name]); }

const decl = (pairs, indent = "  ") => pairs.map(([n, v]) => `${indent}--clx-${n}: ${v};`).join("\n");
lines.push("/* Clixite Design System 2.0 : fichier généré par ds/build-tokens.mjs, ne pas éditer. */");
lines.push(`:root {\n${decl(root)}\n}`);
lines.push(`:root, [data-theme="papier"] {\n  color-scheme: light;\n${decl(themeVars.papier)}\n}`);
lines.push(`[data-theme="encre"] {\n  color-scheme: dark;\n${decl(themeVars.encre)}\n}`);
lines.push(`@media (prefers-color-scheme: dark) {\n  [data-theme="auto"] {\n    color-scheme: dark;\n${decl(themeVars.encre, "    ")}\n  }\n}`);

mkdirSync(join(here, "dist"), { recursive: true });
writeFileSync(join(here, "dist", "tokens.css"), lines.join("\n\n") + "\n");

// --- contraste WCAG 2.2 ---------------------------------------------------
const lum = (hex) => {
  const n = hex.replace("#", "");
  const [r, g, b] = [0, 2, 4].map((i) => parseInt(n.slice(i, i + 2), 16) / 255).map((c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
const pairs = [
  ["text", "bg", 4.5], ["text", "bg-alt", 4.5], ["text", "surface", 4.5],
  ["text-muted", "bg", 4.5], ["text-muted", "bg-alt", 4.5], ["text-muted", "surface", 4.5],
  ["link", "bg", 4.5], ["link", "surface", 4.5], ["link-hover", "bg", 4.5],
  ["on-accent", "accent", 4.5], ["on-accent", "accent-hover", 4.5],
  ["focus", "bg", 3], ["border-strong", "bg", 3], ["danger", "bg", 4.5],
];
const report = []; let failures = 0;
for (const [theme, node] of Object.entries(tree.theme)) {
  for (const [fg, bg, min] of pairs) {
    const a = resolve(node[fg].$value), b = resolve(node[bg].$value);
    const r = Math.round(ratio(a, b) * 100) / 100;
    const ok = r >= min; if (!ok) failures++;
    report.push({ theme, fg, bg, fgHex: a, bgHex: b, ratio: r, min, ok });
  }
}
writeFileSync(join(here, "dist", "contrast.json"), JSON.stringify(report, null, 2));
const flat = Object.fromEntries(root.concat(...Object.entries(themeVars).map(([t, p]) => p.map(([n, v]) => [`theme-${t}-${n}`, v]))));
writeFileSync(join(here, "dist", "tokens.json"), JSON.stringify(flat, null, 2));
for (const r of report.filter((x) => !x.ok)) console.error(`ÉCHEC ${r.theme} ${r.fg}/${r.bg} ${r.ratio}:1 < ${r.min}:1`);
console.log(`tokens ok : ${root.length} variables globales, ${Object.keys(themeVars).length} thèmes, ${report.length} paires contrôlées, ${failures} échec(s)`);
process.exit(failures ? 1 : 0);
