# Level 2 — Problem and Opportunity Space

Use this Level Guide to classify, formulate, and audit **Problem and Opportunity Space** without leaking adjacent decisions into it.

## Card Path

- [Terminology](#terminology)
- [Definition](#definition)
- [Governing Question](#governing-question)
- [Strategic Job](#strategic-job)
- [Unit and Scope](#unit-of-analysis-and-scope)
- [Expert and Source Anchors](#expert-and-source-anchors)
- [Reasoning Formula](#reasoning-formula)
- [What Belongs](#what-belongs)
- [What Does Not Belong](#what-does-not-belong)
- [Adjacent-Level Boundaries](#adjacent-level-boundaries)
- [Required Evidence](#required-evidence)
- [Permitted Reconstruction](#permitted-reconstruction)
- [Claim, Lifecycle, and Ownership Controls](#claim-lifecycle-and-ownership-controls)
- [Writing Grammar](#writing-grammar)
- [Canonical Output and Traceability](#canonical-output-and-traceability)
- [Quality Audit](#quality-audit)


## Terminology

### Terminology Status

**Playbook-synthesized combined label; source-adapted concepts.**

Indi Young uses “problem space” for knowledge about people and their purposes outside the offering. Teresa Torres uses “opportunity space” for customer needs, pain points, and desires that could drive a desired outcome. This level combines the complementary ideas while preserving their differences.[source](source-index.md#src-young-problem) [source](source-index.md#src-torres-ost)

Young’s problem space is broader than this single level: it informs Levels 0–2 of this hierarchy. Level 2 is specifically where the playbook converts purpose and current-experience knowledge into an evidence-backed opportunity structure.

## Definition

Problem and Opportunity Space is the structured, evidence-backed interpretation of the unmet needs, frictions, desires, anxieties, harms, risks, constraints, positive deviations, and leverage points revealed by the current experience.

It explains **where and why meaningful improvement may be possible** without selecting the intended outcome, strategy, or solution.

## Governing question

> **What evidence-backed conditions prevent or weaken meaningful human progress, and where could intervention create value?**

## Strategic job

This level converts raw current-experience evidence into a navigable decision space. It:

- prevents a single stakeholder request from becoming “the problem”;
- separates customer or user opportunity from solution ideas;
- reveals relationships, clusters, causes, constraints, and competing explanations;
- shows where evidence is strong, weak, or contradictory;
- enables Level 3 to choose a meaningful human change; and
- preserves alternatives before strategy narrows the field.

## Unit of analysis and scope

The smallest unit is an **opportunity node**: one actor’s evidence-backed need, friction, desire, risk, or beneficial condition in a particular context.

The level as a whole is an **opportunity structure** containing related nodes, their relationships, evidence strength, human consequences, and uncertainties.

Keep nodes at comparable granularity. “Cannot understand status,” “complete the entire application,” and “redesign the dashboard” are three different kinds and sizes of statement; they should not appear as peers.

## Expert and source anchors

Young’s problem-space work keeps attention on people’s purposes and reasoning before the organization returns to selecting problems and generating solutions.[source](source-index.md#src-young-problem-research)

Torres distinguishes the opportunity space—needs, pain points, and desires—from the solution space and recommends grounding opportunity nodes in customer stories rather than generating them from team assumptions.[source](source-index.md#src-torres-ost) [source](source-index.md#src-torres-prioritize-opportunities)

Torres’s Opportunity Solution Tree commonly starts with a desired business outcome. This playbook borrows her opportunity-versus-solution separation; it does not use her outcome placement to redefine the human-centered Strategic UX Outcome at Level 3.

GOV.UK discovery guidance similarly separates a problem from a proposed mechanism and asks teams to understand users, wider journeys, inclusion, constraints, legacy systems, and cross-organizational conditions.[source](source-index.md#src-gov-discovery)

## Reasoning formula

```text
OPPORTUNITY NODE
= specific actor
+ context and trigger
+ unmet need, friction, desire, harm, risk, or positive deviation
+ evidence from the current experience
+ human consequence or value at stake
+ confidence and unresolved questions
− proposed solution

PROBLEM AND OPPORTUNITY SPACE
= related opportunity nodes
+ relationships, patterns, constraints, and causal hypotheses
+ evidence strength, prevalence, severity, and variation where known
+ counterevidence and alternative explanations
```

Correlation may justify an opportunity for further inquiry. It does not automatically justify a root-cause claim.

## What belongs

- Needs, pain points, desires, anxieties, and unmet expectations expressed or demonstrated by people.
- Barriers created by policy, information, coordination, technology, environment, ability, or authority.
- Human risks, harms, exclusion, error exposure, and loss of agency.
- Recurring workarounds and their costs.
- Positive deviations: contexts where people succeed unusually well and why that may matter.
- Frequency, severity, reach, confidence, and consequence where known.
- Relationships between opportunity nodes.
- Competing causal hypotheses and counterevidence.
- Constraints that limit the plausible intervention space.
- Explicit unknowns requiring further research.

## What does not belong

- Features, interface patterns, technologies, or solution concepts.
- “We need an AI assistant,” “build a dashboard,” or another mechanism framed as a problem.
- A business target disguised as something a person wants.
- A final strategic priority or roadmap horizon.
- A chosen Strategic UX Outcome.
- A root cause asserted without evidence or alternatives.
- Every observation copied into a flat pain-point backlog.
- An internal requirement treated as a human need without tracing the human consequence.

## Adjacent-level boundaries

**Above — Level 1, Current Experience:** Level 1 records what happens. Level 2 interprets what those patterns may mean for needs, barriers, risks, and leverage.

**Below — Level 3, Strategic UX Outcome:** Level 2 preserves the range of possible improvements. Level 3 chooses and defines the specific human change the initiative will pursue.

## Required evidence

At minimum, an opportunity node needs:

- a traceable Level 1 observation, account, artifact, or data signal;
- a specific actor and context;
- a defensible human consequence or value at stake; and
- explicit confidence and uncertainty.

Stronger evidence triangulates:

- repeated recent-event stories;
- contextual observation;
- behavioral or operational data;
- support and complaint patterns;
- accessibility and inclusion evidence;
- domain, policy, safety, or regulatory constraints;
- successful contrasting cases; and
- disconfirming evidence.

A qualitative pattern can be strategically important without population-level prevalence. The claim must be worded at the level the sample supports.

## Permitted reconstruction

**Permitted:**

- group documented observations into a later opportunity structure;
- reconstruct an opportunity when several downstream decisions trace to the same evidenced friction or need;
- record a root cause as a hypothesis when evidence is incomplete;
- use external research to establish category, policy, or technical context; and
- retain alternative problem framings pending confirmation.

**Not permitted:**

- start with the released solution and ask which problem would make it look inevitable;
- assert that the historical team prioritized an opportunity without evidence;
- transform a contextual industry fact into a project research finding;
- invent frequency, severity, or emotional consequence; or
- hide contradictory evidence to create a cleaner narrative.

## Claim, lifecycle, and ownership controls

- **Component availability:** Required. A partial space is acceptable when scope and evidence gaps are explicit.
- **Provenance:** Classify each node and relationship independently; a documented observation may still support only an inferred interpretation.
- **Lifecycle:** Use **Hypothesized** when an opportunity interpretation remains unconfirmed and **Targeted** only when evidence shows it was selected for attention. Designed, Implemented, and Released describe the downstream intervention—not proof that the opportunity was resolved. An opportunity’s existence does not prove it was selected or solved.
- **Ownership:** Use “I synthesized,” “I framed,” “we identified,” or “the evidence suggested” according to the record. Avoid “I discovered” when the insight came from a team or later reconstruction.

## Writing grammar

**Problem statement**

> **[Actor] needs to [make human progress] when [context], but [evidence-backed condition] makes this difficult, leading to [human consequence].**

**Opportunity statement**

> **This creates an opportunity to [improve a human condition or capability] without presuming [solution mechanism].**

**Illustrative application**

> Listeners with clear situational intent but no specific song in mind must translate a desired feeling into catalogue terms, then sample and reject options. This creates decision burden before listening begins and an opportunity to help people reach suitable audio without requiring content knowledge.

## Canonical output and traceability

The canonical output is an **Evidence-Backed Opportunity Structure** containing:

- opportunity-node IDs and statements;
- actors and contexts;
- supporting Level 1 evidence;
- human consequence or value at stake;
- relationships and hierarchy;
- evidence strength, prevalence, severity, and variation where known;
- causal hypotheses and alternatives;
- constraints, risks, and unknowns;
- provenance and reconstruction status; and
- explicit separation from solution ideas.

Every node must trace upward to current-experience evidence and the Level 0 purpose. Candidate Level 3 outcomes may reference nodes, but this level does not yet choose the outcome or assign roadmap priority.

## Quality audit

**Pass when:**

- every consequential node names an actor, context, evidence, and human consequence;
- opportunities are distinct from solutions and business wishes;
- node granularity is coherent;
- uncertainty and alternative explanations remain visible; and
- the space is broad enough to preserve genuine strategic choice.

**Fail when:**

- a feature request has been reworded as a need;
- the built solution is the only evidence;
- a flat list conceals relationships and evidence strength;
- assumed causes are stated as facts; or
- opportunity selection is falsely presented as contemporaneous strategy.

**Experience-first leadership signal:** The designer protects the organization from premature solution commitment and turns human evidence into a shared space for strategic choice.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [Indi Young, “Explanations — Problem Space.”](source-index.md#src-young-problem) | Human purpose, problem-space inquiry, and deep listening. |
| [Teresa Torres / Product Talk, “Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes.”](source-index.md#src-torres-ost) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [Indi Young and Kunyi Mangalam, “Launching Problem Space Research in the Frenzy of Software Production.” Interactions 25, no. 1 (January–February 2018): 66–69.](source-index.md#src-young-problem-research) | Human purpose, problem-space inquiry, and deep listening. |
| [Teresa Torres, “Prioritize Opportunities, Not Solutions.” Product Talk.](source-index.md#src-torres-prioritize-opportunities) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [GOV.UK Service Manual, “How the Discovery Phase Works.”](source-index.md#src-gov-discovery) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
