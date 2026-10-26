// Forward Deployed Engineering pillar page, in English (British spelling). Same structure as ../fr/fde.ts.
import type { Fde } from "../fr/fde";
import { SOURCES } from "../sources";

const fde: Fde = {
  title: "Forward Deployed Engineering, Belgium and Luxembourg | Clixite",
  description: "Engineers embedded in your teams design, build and ship your integrations, automations and AI agents to production, then hand everything over to you.",
  h1: ["Forward Deployed Engineering: ", "building inside your teams, all the way to production."],
  chapo: "Forward Deployed Engineering (FDE) means placing engineers inside a client's teams to design, build and ship a solution to production on the client's own systems, then hand it over. In Belgium and Luxembourg, Clixite applies this model to integrations, automation and AI, within the frameworks of DORA, NIS2, the GDPR and the AI Act.",
  cta: "Request a conversation", cta2: "See how we work", updated: "Updated 26 October 2026",
  what: {
    h: "What is Forward Deployed Engineering?",
    p: [
      "A Forward Deployed Engineer is an engineer placed with the client, close to the people who use the system. They understand the business, design, code, integrate and deploy, then hand over what they built.",
      "It is neither consulting that stops at a recommendation nor staffing that executes tasks: the Forward Deployed Engineer owns an outcome defined with you, a solution running in your environment.",
    ],
  },
  origin: {
    h: "Where the model comes from",
    p: "The model was formalised by Palantir, which distinguishes its product developers from the engineers it deploys with customers, summed up in the phrase “one customer, many capabilities”. AI companies have since adopted it to take their customers from prototype to production, to the point of making it one of the most sought-after profiles in the industry.",
    src: [{ t: "Palantir, “Dev versus Delta”", href: SOURCES.palantir }, { t: "TechCrunch, 30 July 2026", href: SOURCES.techcrunch }],
    srcLabel: "Sources",
  },
  when: {
    h: "When to bring in a Forward Deployed Engineer",
    items: [
      "An AI prototype works in a demo but has never reached production.",
      "Your systems do not talk to each other: ERP, CRM, procurement tools and business data need reliable connections.",
      "A manual process must be automated without breaking what already runs.",
      "A programme is late and needs hands as much as steering committees.",
      "Your environment is regulated and nothing may leave your premises.",
      "Your team needs to build skills, up to creating its own FDE capability.",
    ],
  },
  method: {
    h: "How we work, in four stages",
    lead: "Each stage delivers something you keep. You decide on the next one based on evidence.",
    steps: [
      { t: "Settle in", d: "Access, environments, security rules and contacts: we work in your tools and with your teams from the start.", out: "Agreed working framework" },
      { t: "Build", d: "A prototype on your real data, tested with the people who will use it and improved in short increments.", out: "Proven prototype" },
      { t: "Go to production", d: "Security, monitoring, documentation and runbooks: the solution goes live according to your rules.", out: "Solution in production" },
      { t: "Hand over", d: "Code, access, documentation and training: we leave when your teams run and evolve the solution on their own.", out: "Self-sufficient teams" },
    ],
    outLabel: "Deliverable",
  },
  compare: {
    h: "FDE, consulting or staffing: what is the difference?",
    cols: ["", "Role", "What you receive", "End of the assignment"],
    rows: [
      ["Forward Deployed Engineering", "Builds and ships to production inside your teams.", "A solution in production, documented and handed over.", "When your teams run it on their own."],
      ["Traditional consulting", "Analyses and recommends.", "A report, a target, a roadmap.", "When the deliverable is handed in."],
      ["IT services or staffing", "Executes the tasks you direct.", "Time, on a best-efforts basis.", "When the contract ends; handover is not built in."],
    ],
    note: "The difference lies in the mandate, not the contract: a Forward Deployed Engineer can be engaged on a time-and-materials or a fixed-scope basis.",
  },
  regulated: {
    h: "Forward Deployed Engineering in regulated environments",
    lead: "Banks, insurers, essential entities: DORA, NIS2, the GDPR and the AI Act also apply to what gets built. The framework is set from the start.",
    items: [
      { t: "Your environments", d: "Nothing is built outside your perimeter without written agreement." },
      { t: "Named access", d: "Logged, limited to what is needed, removed at the end of the assignment." },
      { t: "Your data stays with you", d: "The use of AI tools is decided with you, tool by tool." },
      { t: "Audit-ready documentation", d: "Architecture, decisions, risks, operating procedures." },
      { t: "AI under human oversight", d: "Oversight, logging and documentation, as the AI Act requires for the systems in scope." },
    ],
  },
  keep: {
    h: "What you keep",
    p: "The code, the access, the documentation and trained teams. And if you wish, the set-up of your own internal FDE team: roles, methods, hiring.",
  },
  faqTitle: "Frequently asked questions about Forward Deployed Engineering.",
  faq: [
    { q: "What is a Forward Deployed Engineer?", a: "An engineer embedded in a client's teams who turns a need into a working service. They understand the business, design, code, integrate, deploy, then hand over. The model was formalised by Palantir." },
    { q: "How is it different from a consultant?", a: "A consultant recommends; a Forward Deployed Engineer builds. The assignment ends when your teams run the solution, not when a report is delivered." },
    { q: "Is it staffing under another name?", a: "No. With staffing, you direct a resource task by task. A Forward Deployed Engineer owns an outcome defined with you: a solution in production, documented and handed over." },
    { q: "Do I need an artificial intelligence project?", a: "No. The model also works for connecting systems, automating a process or recovering a programme. AI is simply one of the most common cases." },
    { q: "Is it compatible with DORA, NIS2, the GDPR and the AI Act?", a: "Yes, provided the framework is set from the start: your environments, your security rules, named access and data that stays with you." },
    { q: "What does the company keep at the end?", a: "The code, the access, the documentation and teams trained to run and evolve the solution." },
    { q: "Where and in which languages do you work?", a: "In Belgium and Luxembourg, in English, French or Dutch, on site or remotely." },
  ],
  schema: {
    alternateName: ["FDE", "Forward Deployed Engineer"],
    serviceType: ["Forward Deployed Engineering", "Systems integration", "Process automation", "AI in production", "AI agents"],
    term: "An engineering model that places engineers inside a client's teams to design, build and ship a solution to production on the client's own systems, then hand it over.",
  },
};
export default fde;
