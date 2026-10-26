// Content of the service pages (GEO, architecture, programme management, digitalisation), rendered by components/MetierPage.astro.
// Address the reader as "you"; no figures, prices, durations or project details; nothing unverifiable. The visible FAQs feed the FAQPage markup.
import type { PageMetier } from "../fr/pages";
import { routesFor } from "../routes";
import { SOURCES } from "../sources";
const r = routesFor("en");

const pages: PageMetier[] = [
  {
    slug: "geo", key: "geo", path: r.geo, crumb: "GEO",
    title: "GEO: visibility in ChatGPT and AI assistants | Clixite",
    description: "GEO makes your company understandable and citable by ChatGPT, Claude, Perplexity and Google: audit, structuring and monitoring, in Belgium and Luxembourg.",
    h1: ["GEO: ", "be the answer AI assistants give."],
    chapo: "Generative Engine Optimization (GEO) means making a company understandable, verifiable and citable by answer engines: ChatGPT, Claude, Perplexity, Gemini, Copilot and Google's AI Overviews. Clixite measures your visibility, structures your content and data, and fixes what stops assistants from citing you, in Belgium and Luxembourg.",
    photo: "archives-45",
    alternateName: ["Generative Engine Optimization", "AI search optimisation", "Generative search optimisation"],
    serviceType: ["Generative Engine Optimization", "Search engine optimisation", "Structured data", "AI search visibility audit"],
    blocs: [
      { id: "geo-seo", h: "GEO and SEO: what is the difference?", kind: "prose", p: [
        "SEO aims for a position in a list of links. GEO aims for a place in the answer the assistant writes, with a citation of your site.",
        "The two complement each other. Answer engines rely heavily on pages that already rank well, but they read differently: they look for clear definitions, verifiable facts and sources that confirm one another.",
      ], src: [{ t: "Aggarwal et al., “GEO: Generative Engine Optimization”, 2023", href: SOURCES.geoPaper }] },
      { id: "geo-criteres", h: "What makes an assistant cite you", kind: "defs", band: true, lead: "What is known today, and what we measure for every client.", defs: [
        { t: "An unambiguous entity", d: "The same name, the same address, the same services everywhere: company register, website, LinkedIn, directories, Wikidata." },
        { t: "Pages that answer", d: "A definition in a few sentences, visible frequently asked questions, honest comparisons, dated pages." },
        { t: "Accurate structured data", d: "schema.org markup that describes exactly what the page displays, and a site that assistants' crawlers can read." },
        { t: "Mentions beyond your own site", d: "Press, professional directories, open databases: assistants cross-check their sources before they cite." },
      ] },
      { id: "geo-methode", h: "Our approach, in four stages", kind: "steps", lead: "Each stage delivers something you keep.", steps: [
        { t: "Measure", d: "The questions your clients ask, tested on the main assistants: who gets cited, with what information, and from where.", out: "AI visibility audit" },
        { t: "Structure", d: "Entity, structured data, definition pages, frequently asked questions, rules for crawlers: the site becomes readable and citable.", out: "A site ready for answer engines" },
        { t: "Publish", d: "Reference content, business listings, professional profiles, Wikidata: your off-site presence becomes consistent.", out: "Aligned third-party presence" },
        { t: "Monitor", d: "Search Console, Bing Webmaster Tools and regular tests of the assistants: we measure citations and make corrections.", out: "Tracking dashboard" },
      ] },
      { id: "geo-garantie", h: "What no one can guarantee", kind: "note", encre: true, p: [
        "No provider can guarantee a position in Google or a citation by an assistant: the models change, and so do their sources.",
        "What we commit to is measurable work: a crawlable site, valid and consistent data, an aligned presence, and regular tests to see what moves. This site puts it into practice: an entity described in structured data, definition pages, visible frequently asked questions, a summary for assistants.",
      ] },
      { id: "geo-pour-qui", h: "Who it is for", kind: "list", items: [
        "SMEs and professional firms whose clients do their own research before they call.",
        "Groups that want assistants to describe their offerings, brands and obligations correctly.",
        "Software and service providers whose name must come up when someone asks an assistant for a solution.",
        "Any company present in several languages: assistants answer in the language of the question.",
      ] },
    ],
    faq: [
      { q: "What is GEO?", a: "Generative Engine Optimization (GEO) makes a company understandable, verifiable and citable by answer engines such as ChatGPT, Claude, Perplexity, Gemini, Copilot and Google's AI Overviews." },
      { q: "Is SEO still useful?", a: "Yes. Answer engines rely largely on the indexes of search engines. Good SEO remains the foundation; GEO adds what makes content citable." },
      { q: "Can anyone guarantee that ChatGPT will cite you?", a: "No, and be wary of anyone who promises it. What can be done is to measure your visibility, fix what works against you and track how citations evolve." },
      { q: "Is an llms.txt file enough?", a: "No. It helps some tools summarise a site, but the main assistants rarely read it so far. We set it up without expecting miracles." },
      { q: "Do you need to rebuild your website?", a: "Rarely. Most fixes concern content, structured data and off-site presence." },
      { q: "Which languages do you work in?", a: "English, French and Dutch. Assistants answer in the language of the question: you need to exist in each one." },
    ],
  },
  {
    slug: "architecture-entreprise-solutions", key: "archi", path: r.archi, crumb: "Enterprise and solution architecture",
    title: "Enterprise and solution architecture in Belgium | Clixite",
    description: "IT landscape mapping, target architecture, roadmap options and solution selection, all the way to production. In Belgium and Luxembourg.",
    h1: ["Enterprise and solution architecture: ", "decide where your IT landscape is heading."],
    chapo: "Enterprise architecture links strategy to the information system: what you have, what you are aiming for and the path between the two. Solution architecture selects and designs the tools that get you there. Clixite does both, from mapping to production, for SMEs and regulated groups alike, in Belgium and Luxembourg.",
    photo: "aiguillage-45",
    serviceType: ["Enterprise architecture", "Solution architecture", "IT landscape mapping", "Architecture review"],
    blocs: [
      { id: "archi-quand", h: "When to bring us in", kind: "list", items: [
        "Your applications have piled up and no one has the full picture any more.",
        "A major choice is coming up: ERP, CRM, procurement tool, cloud, data platform.",
        "A merger, a demerger or a reorganisation redraws the map.",
        "A regulator or an auditor asks for a clear view of your systems and your critical suppliers.",
        "An AI project has to find its place in the existing landscape.",
      ] },
      { id: "archi-obtenez", h: "What you get", kind: "defs", band: true, defs: [
        { t: "A landscape map", d: "Applications, data, flows, contracts and critical suppliers, on a map your teams can read." },
        { t: "A target architecture", d: "Principles, building blocks, integrations and security: where you are heading, and why." },
        { t: "A roadmap with options", d: "What we keep, what we replace, what we stop; each option with its costs, risks and dependencies." },
        { t: "External architecture reviews", d: "An outside, reasoned view of a solution choice or an architecture document, before the decision becomes expensive." },
      ] },
      { id: "archi-suite", h: "From target to production", kind: "prose", p: [
        "A target only has value if it gets built. Once it is approved, we can implement it with your teams, through Forward Deployed Engineering, and manage the programme that delivers it.",
      ], link: { t: "Forward Deployed Engineering", href: r.fde } },
    ],
    faq: [
      { q: "What is the difference between enterprise architecture and solution architecture?", a: "Enterprise architecture decides the whole: business, data, applications, technology, and the path from today to the target. Solution architecture designs a specific solution within that framework, down to integrations and security." },
      { q: "Does an SME need enterprise architecture?", a: "Yes, at its own scale. A clear map of your tools and flows avoids redundant purchases and prepares for growth. For an SME, the exercise fits into a few short deliverables." },
      { q: "Do you follow a methodological framework?", a: "We draw on the concepts of recognised frameworks when they help, without imposing heavy formalism: an architecture deliverable has to be read and used by your teams." },
      { q: "Can you also build the target?", a: "Yes, through Forward Deployed Engineering: we join your teams to take what has been decided into production, then hand it over." },
    ],
  },
  {
    slug: "pilotage-de-programmes", key: "pilotage", path: r.pilotage, crumb: "Programme management",
    title: "Programme management and change management | Clixite",
    description: "Governance, planning, budget, risk and adoption: your multi-team programmes kept on track through to go-live, in Belgium and Luxembourg.",
    h1: ["Programme management: ", "multi-team programmes kept on track through to go-live."],
    chapo: "Programme management coordinates several projects that serve a single objective: governance, planning, budget, risk and change management. Clixite launches or takes over your transformation programmes in Belgium and Luxembourg, with recognised frameworks (PMP, PRINCE2, SAFe, Scrum, ADKAR) and one rule: decisions are made on the evidence.",
    photo: "salle-45",
    serviceType: ["Programme management", "Project management", "Change management", "Programme recovery"],
    blocs: [
      { id: "prog-quand", h: "When to bring us in", kind: "list", items: [
        "A programme has fallen behind or its budget is drifting.",
        "Several teams and several suppliers have to move at the same pace.",
        "Committees meet but do not decide.",
        "A critical go-live is approaching.",
        "Users are not adopting what has been delivered.",
      ] },
      { id: "prog-obtenez", h: "What you get", kind: "defs", band: true, defs: [
        { t: "A recovery assessment", d: "Where the programme really stands: scope, schedule, budget, risks and dependencies." },
        { t: "Governance that decides", d: "Clear committees, roles and decision rules, and dashboards that support decisions." },
        { t: "A plan that holds", d: "Milestones, dependencies and risks followed closely, with every team and every supplier." },
        { t: "Change you can measure", d: "Training, communication and adoption tracked against indicators defined at the start." },
      ] },
    ],
    faq: [
      { q: "Can you take over a programme already under way?", a: "Yes, it is a common case: an assessment, a recovery plan and clear trade-off decisions, then programme management close to the teams." },
      { q: "Iterative methods or the V-model?", a: "Both, depending on the nature of the programme and your constraints: SAFe and Scrum for product and software, PRINCE2 or PMP for heavily governed programmes, often a deliberate mix." },
      { q: "Do you work with our suppliers and integrators?", a: "Yes. We coordinate internal teams and suppliers, with clear commitments for each of them." },
      { q: "How do you measure adoption?", a: "With indicators defined at the start: actual usage, support requests, quality of the data entered, user feedback." },
    ],
  },
  {
    slug: "digitalisation", key: "digit", path: r.digit, crumb: "Digitalisation",
    title: "Process digitalisation and automation in Belgium | Clixite",
    description: "Processes simplified, then tooled: automated workflows, connected data and applied AI, from SMEs to large enterprises, in Belgium and Luxembourg.",
    h1: ["Process digitalisation: ", "from paper and double data entry to connected tools."],
    chapo: "Process digitalisation replaces paper, scattered files and double data entry with digital workflows and connected data. Clixite maps and simplifies your processes before automating them, then takes them into production with your teams, from SMEs to large enterprises, in Belgium and Luxembourg.",
    photo: "fibres-45",
    serviceType: ["Process digitalisation", "Process automation", "CRM and ERP integration", "Applied AI"],
    blocs: [
      { id: "digit-quand", h: "When to bring us in", kind: "list", items: [
        "A process still runs on paper, in Excel or by email.",
        "The same data is entered several times in several tools.",
        "Approvals get lost between inboxes.",
        "Dashboards exist but nobody uses them.",
        "You want to use AI but do not know where to start.",
      ] },
      { id: "digit-obtenez", h: "What you get", kind: "defs", band: true, defs: [
        { t: "Simplified processes", d: "Mapped, stripped of unnecessary steps, with clear rules, before any tool is added." },
        { t: "Automated workflows", d: "Forms, approvals, notifications and integrations with your CRM and your ERP." },
        { t: "Connected data", d: "Data entered once, clean master data and dashboards that get used." },
        { t: "Applied AI", d: "Where it saves time, under human oversight and in line with the GDPR." },
      ] },
    ],
    faq: [
      { q: "Where should you start?", a: "With the most painful and most frequent process. Simplify it before adding tools: automating a muddled process only makes it go faster." },
      { q: "Do you need to change tools?", a: "Not necessarily. We first make the most of what you already have; a new tool is only justified if it does better at a reasonable cost." },
      { q: "What role does AI play?", a: "Reading documents, sorting requests, drafting replies: AI is genuinely useful there, under human oversight and in line with the GDPR." },
      { q: "Will your teams be able to change the workflows themselves?", a: "Yes. Documentation and training are part of every assignment, so that your teams stay self-sufficient." },
    ],
  },
];
export default pages;
