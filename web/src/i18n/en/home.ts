// Home page: film, logos, Forward Deployed Engineering, GEO, expertise areas, method, proof.
import type { Home } from "../fr/home";
import { routesFor } from "../routes";
const r = routesFor("en");

const home: Home = {
  title: "Clixite: consulting and engineering in Wavre since 2005",
  description: "Consulting and engineering in Wavre since 2005. Clixite designs, builds and ships the systems of Belgian and Luxembourg companies to production.",
  hero: {
    // chapters of the loop (11.5 s): the signature opens, then the film's captions in time with the shots
    story: [
      { t: "We solve your x.", from: 0 },
      { t: "Your architecture starts on paper.", from: 2 },
      { t: "It gains depth.", from: 4.5 },
      { t: "It lands in your organisation.", from: 7 },
      { t: "And it runs.", from: 9.5 },
    ],
    // the main title says what we do; the "x" remains the site's signature (film chapters, closing block)
    h1: ["We build your ", "solution", " inside your teams, all the way to production."],
    sub: "Consulting and engineering since 2005. We design, build and ship your systems to production, inside your teams, in Belgium and Luxembourg.",
    cta2: { t: "Forward Deployed Engineering", href: r.fde },
  },
  refs: {
    title: "Where we have worked.",
    note: "Telecoms, banking, insurance, pharmaceuticals, construction, aviation, distribution, leisure, SMEs: very different environments, on assignment, as consultants or in-house. The projects themselves stay confidential.",
  },
  fde: {
    title: "Forward Deployed Engineering.",
    lead: "Clixite joins your teams to design, build and ship your integrations, automations and AI agents to production, then hands the solution over to you. In Belgium and Luxembourg, in English, French or Dutch.",
    btn: "Forward Deployed Engineering in detail",
    items: [
      { t: "Inside your teams, not alongside them.", d: "On site or remotely, in your tools and at your pace. Decisions are made where the work gets done." },
      { t: "In production, not in PowerPoint.", d: "The assignment is measured by what runs: an integration, an automated process, an AI agent in use on Monday morning." },
      { t: "Under your control, then in your hands.", d: "Your environments, your security rules, named access. At the end, the code, the documentation and the know-how stay with you." },
    ],
  },
  geo: {
    title: "GEO: be the answer AI assistants give.",
    lead: "Your clients no longer just search Google. They ask ChatGPT, Claude, Perplexity, Gemini or Copilot who can help them. We work to help assistants find you and describe you accurately.",
    btn: "GEO in detail",
    items: [
      { t: "Measure", d: "The questions your clients ask, tested on the main assistants: who gets cited, and with what information." },
      { t: "Structure", d: "A consistent entity, pages that answer questions and accurate structured data: your site becomes citable." },
      { t: "Publish and monitor", d: "Business listings, profiles, open databases, third-party mentions, then regular tests: assistants cross-check their sources before they cite." },
    ],
  },
  expertises: {
    title: "Five expertise areas, one standard: what we deliver has to run.",
    lead: "We step in where a strategy has to become a working system, in SMEs and regulated groups alike.",
  },
  method: {
    title: "From discovery to go-live.",
    lead: "Four stages, each with a deliverable you keep, even if you stop there. You decide on the next one based on evidence.",
    steps: [
      { t: "Discover", d: "A map of your systems, flows, contracts and risks. We measure before we draw.", out: "Assessment" },
      { t: "Design", d: "The target architecture and the path to get there, as costed options. What we keep, what we replace, what we stop.", out: "Target architecture and roadmap" },
      { t: "Build", d: "Integrations, data, automations and AI, delivered in short increments that your teams test in real conditions.", out: "Increments in production" },
      { t: "Go live", d: "Deployment, adoption and handover. We leave when your teams run the solution on their own.", out: "Solution in operation and documented" },
    ],
  },
  // "Proof" block (HomeView): verifiable facts only. The 7 certifications come from
  // SITE.founder.certifications (site.ts) and the 14 displayed logos from data/clients.json.
  // TODO(content): publish anonymised client cases and quotations with written consent, then verifiable outcome figures.
  // No case, testimonial or percentage is invented here.
  proofs: {
    title: "What you can check.",
    lead: "Projects stay confidential. These are the facts you can check, and the commitments we make in writing.",
    facts: {
      founded: "Founded",
      foundedValue: "2005, so {years} years of activity.",
      certifications: "Founder's seven certifications",
      certificationsValue: "PMP, PRINCE2, AgilePM, SAFe, Scrum, ITIL v3, ADKAR.",
      logos: "Organisations cited",
      logosValue: "Fourteen organisations whose logos appear on this page, on assignment, as consultants or in-house.",
      languages: "Working languages",
      languagesValue: "English, French, Dutch.",
      area: "Area served",
      areaValue: "Belgium and Luxembourg.",
      commitments: "Commitments",
      commitmentsValue: "A non-disclosure agreement before we talk if you wish, documentation as we go, and the code, access and documentation stay with you.",
    },
  },
};
export default home;
