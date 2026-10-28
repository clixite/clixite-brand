// Transitions entre pages (View Transitions API) : sens du relevé et glissement des éléments marqués.
// Extrait du layout pour permettre une CSP script-src 'self' sans 'unsafe-inline'.

type VT = { types: { add: (name: string) => void }; finished: Promise<void> };
type Activation = { entry?: { url: string } | null; from?: { url: string } | null } | null;

const depth = (u: string) => new URL(u).pathname.split("/").filter(Boolean).length;

const visible = (el: HTMLElement) => {
  const r = el.getBoundingClientRect();
  return r.height > 0 && r.bottom > 0 && r.top < innerHeight;
};

const mark = (path: string) => {
  const used = new Set<string>();
  document.querySelectorAll<HTMLElement>('[data-vt-href="' + path + '"]').forEach((el) => {
    const n = el.dataset.vt;
    if (!n || used.has(n) || !visible(el)) return;
    used.add(n);
    el.style.viewTransitionName = n;
    el.style.viewTransitionClass = el.dataset.vtClass || "";
  });
};

const clear = () => document.querySelectorAll<HTMLElement>("[data-vt]").forEach((el) => {
  el.style.viewTransitionName = "";
  el.style.viewTransitionClass = "";
});

addEventListener("pageswap", (e) => {
  const ev = e as Event & { viewTransition?: VT | null; activation?: Activation };
  const entry = ev.activation?.entry;
  if (!ev.viewTransition || !entry) return;
  mark(new URL(entry.url).pathname);
});

addEventListener("pagereveal", (e) => {
  const ev = e as Event & { viewTransition?: VT | null };
  const vt = ev.viewTransition;
  if (!vt) return;
  const nav = (window as Window & { navigation?: { activation?: Activation } }).navigation;
  const a = nav?.activation;
  if (a?.from && a.entry) {
    if (depth(a.entry.url) < depth(a.from.url)) vt.types.add("remonte");
    mark(new URL(a.from.url).pathname);
  }
  vt.finished.finally(clear);
});

addEventListener("pageshow", clear);

export {};
