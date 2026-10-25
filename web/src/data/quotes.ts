// Recommandations clients, publiées seulement avec l'accord écrit de leur auteur.
// Tant que la liste est vide, la section n'apparaît pas sur le site.
import type { AudKey } from "./audiences";
export const QUOTES: { q: string; who: string; role: string; org: string; aud: AudKey[] }[] = [];
