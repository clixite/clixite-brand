// Clixite's five services, Forward Deployed Engineering and GEO first (the most requested),
// then the application areas. Single source for the home page, the hub, the service pages, the JSON-LD and llms.txt.
import type { Metiers } from "../fr/metiers";
import { routesFor, anchorsFor } from "../routes";
const r = routesFor("en");
const a = anchorsFor("en");

const metiers: Metiers = {
  list: [
    {
      slug: "forward-deployed-engineering", key: "fde", href: r.fde, t: "Forward Deployed Engineering", court: "Forward Deployed Engineering",
      d: "We join your teams to design and build the integration, automation or AI agent you need and take it into production, using your tools and following your security rules. We leave when your teams run the solution on their own.",
      g: ["A prototype proven on your real data", "A solution in production, monitored and documented", "A complete handover: code, access, documentation, trained teams"],
      k: "Systems integration, process automation, AI agents, go-live, handover",
      photo: "ingenieurs",
    },
    {
      slug: "geo", key: "geo", href: r.geo, t: "GEO: visibility in AI assistants", court: "GEO",
      d: "When your clients ask ChatGPT, Claude, Perplexity, Gemini or Copilot who can help them, your company needs to be part of the answer. We make your offering understandable, verifiable and citable by answer engines as well as by Google.",
      g: ["An audit of your visibility in AI assistants, question by question", "Consistent pages, structured data and entity details that engines understand", "An aligned off-site presence and citation tracking"],
      k: "GEO, SEO, structured data, Wikidata, Search Console, Bing Webmaster Tools",
      photo: "archives",
    },
    {
      slug: "architecture-entreprise-solutions", key: "archi", href: r.archi, t: "Enterprise and solution architecture", court: "Architecture",
      d: "Know what you have, decide where you are going and choose the solutions that take you there, without piling up tools.",
      g: ["Mapping of applications, data and flows", "Target architecture and roadmap, as costed options", "Solution selection and external architecture reviews"],
      k: "IT landscape mapping, target architecture, integration, cloud",
      photo: "aiguillage",
    },
    {
      slug: "pilotage-de-programmes", key: "pilotage", href: r.pilotage, t: "Programme management", court: "Programme management",
      d: "Multi-team programmes scoped and kept on track: clear governance, risks tracked, committees that decide, users on board from day one.",
      g: ["Plan, budget and risks back under control", "Governance and committees that make decisions", "Change management you can measure"],
      k: "PMP, PRINCE2, SAFe, Scrum, ADKAR",
      photo: "salle",
    },
    {
      slug: "digitalisation", key: "digit", href: r.digit, t: "Digitalisation", court: "Digitalisation",
      d: "Paper processes, double data entry and scattered files become connected tools that work for your teams.",
      g: ["Processes mapped and simplified before any tool is added", "Automated forms, workflows and approvals", "Data connected across your tools, dashboards that get used"],
      k: "Process automation, CRM and ERP, data, applied AI",
      photo: "fibres",
    },
  ],
  // application areas: each with one sentence and the page that covers it
  domaines: {
    title: "Where our services apply.",
    lead: "The same methods, on the topics that matter most in regulated enterprises and SMEs alike.",
    items: [
      { t: "Procurement and Source-to-Pay", sub: "Fractional CPO, interim management, third-party risk",
        d: "From need to payment: processes backed by the right tools, supplier risk under control, procurement leadership on a fractional or interim basis.",
        href: r.achats, l: "Procurement transformation" },
      { t: "Risk and compliance", sub: "DORA, NIS2, GDPR, AI Act",
        d: "Obligations translated into processes, owners and evidence, in what you build as well as in what you buy.",
        href: `${r.fde}#${a.fdeRegulated}`, l: "FDE in regulated environments" },
      { t: "AI in production", sub: "Agents, automations, integrations",
        d: "From a prototype that looks convincing in a demo to an AI agent that runs on your systems, under human oversight.",
        href: r.fde, l: "Forward Deployed Engineering" },
      { t: "Digital products and SaaS", sub: "Architecture, integrations, launch",
        d: "The architecture, integrations and go-live of a digital product, until your team can develop it further on its own.",
        href: r.archi, l: "Solution architecture" },
    ],
  },
};
export default metiers;
