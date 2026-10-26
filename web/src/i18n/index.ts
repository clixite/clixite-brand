// Contenu du site par langue. Chaque langue a les mêmes modules, de même forme que le français (vérifié par astro check).
import type { Lang } from "./routes";
import frCommon from "./fr/common"; import nlCommon from "./nl/common"; import enCommon from "./en/common";
import frHome from "./fr/home"; import nlHome from "./nl/home"; import enHome from "./en/home";
import frMetiers from "./fr/metiers"; import nlMetiers from "./nl/metiers"; import enMetiers from "./en/metiers";
import frFde from "./fr/fde"; import nlFde from "./nl/fde"; import enFde from "./en/fde";
import frPages from "./fr/pages"; import nlPages from "./nl/pages"; import enPages from "./en/pages";
import frAutres from "./fr/pages-autres"; import nlAutres from "./nl/pages-autres"; import enAutres from "./en/pages-autres";
import frPhotos from "./fr/photos"; import nlPhotos from "./nl/photos"; import enPhotos from "./en/photos";

const T = {
  fr: { common: frCommon, home: frHome, metiers: frMetiers, fde: frFde, pages: frPages, autres: frAutres, photos: frPhotos },
  nl: { common: nlCommon, home: nlHome, metiers: nlMetiers, fde: nlFde, pages: nlPages, autres: nlAutres, photos: nlPhotos },
  en: { common: enCommon, home: enHome, metiers: enMetiers, fde: enFde, pages: enPages, autres: enAutres, photos: enPhotos },
};
export const t = (lang: Lang) => T[lang];
export * from "./routes";
export { SOURCES, UPDATED } from "./sources";
