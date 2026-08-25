# Level Guide Standard — Make Every Meridian Level Clear and Testable

This standard gives every Meridian level the same evidence, boundary, writing, and traceability controls. Use it to create, reconstruct, or audit a Level Guide without forcing incomplete projects to look more certain than they are.

## Every Meridian level uses the same Level Guide

The hierarchy is useful only if every component can be defined, distinguished, evidenced, written, and audited consistently. Each Level 0–15 entry therefore uses the same sixteen-part Level Guide.

The Level Guide is an analytical structure. A public case study should translate approved claims into natural article-style prose rather than expose the complete internal classification record.

The Level Guide is a playbook synthesis, not a standard reproduced from one source. Its controls are informed by human-centred design across the system lifecycle, evidence-backed user needs, requirements traceability, theory-of-change reasoning, contribution analysis, and the distinction between verification and validation.[source](source-index.md#src-iso-hcd) [source](source-index.md#src-gov-user-needs) [source](source-index.md#src-teal-traceability) [source](source-index.md#src-toc-toolkit) [source](source-index.md#src-magenta-contribution) [source](source-index.md#src-nasa-vv)

### The sixteen parts

| # | Field | Required purpose |
| :---| :---| :---|
| 1 | **Level identity and terminology status** | State the level number, final name, and whether the term is source-defined, source-adapted, or playbook-synthesized. |
| 2 | **Definition** | Explain what the component means in one precise statement. It must remain solution-neutral wherever the level requires it. |
| 3 | **Governing question** | Provide the single question this component must answer. |
| 4 | **Strategic job** | Explain why the component exists and what decision it enables. |
| 5 | **Unit of analysis and scope** | Define the object being classified and its appropriate granularity. |
| 6 | **Expert and source anchors** | Identify the authorities that support the component and which parts are this playbook’s synthesis. |
| 7 | **Reasoning formula** | Provide the conceptual structure used to derive the component. |
| 8 | **What belongs** | Identify the evidence, decisions, and statements that legitimately belong at this level. |
| 9 | **What does not belong** | Identify content that belongs elsewhere or contaminates the classification. |
| 10 | **Adjacent-level boundaries** | Distinguish the component from the level immediately above and below it. |
| 11 | **Required evidence** | State the minimum evidence needed to formulate or claim the component credibly. |
| 12 | **Permitted reconstruction** | Define what may be inferred, how it must be qualified, and what cannot be reconstructed. |
| 13 | **Claim, lifecycle, and ownership controls** | Record component availability, provenance, maturity, and personal contribution. |
| 14 | **Writing grammar** | Provide a practical statement formula, preferred vocabulary, and claim-safe verbs. |
| 15 | **Canonical output and traceability** | Define the expected artifact and its required upstream and downstream links. |
| 16 | **Quality audit** | Supply pass/fail tests, experience-first leadership signals, and common failure modes. |

## Four independent claim controls keep evidence honest

A credible strategic statement must separately identify whether the component exists, where the evidence came from, what stage the work reached, and who contributed what. These dimensions must never be collapsed into a single confidence claim.

### Component availability

| Status | Meaning |
| :---| :---|
| **Evidenced** | Adequately supported by project evidence. |
| **Partially evidenced** | Some elements are supported, but consequential gaps remain. |
| **Reconstructed** | Formulated later from corroborated project evidence. |
| **Unknown** | Insufficient evidence to formulate responsibly. |
| **Not applicable** | Genuinely outside the initiative’s scope; use only with explicit justification. |

An unknown component is an acceptable result. The framework must never force a project to appear strategically complete.

### Evidence provenance

| Code | Classification | Publication rule |
| :---| :---| :---|
| **D** | Documented fact | May be stated confidently and precisely. |
| **R** | Corroborated reconstruction | May be used with wording calibrated to the supporting evidence. |
| **C** | Contextual reconstruction | May explain the environment, but not the team’s historical reasoning. |
| **I** | Working inference | Internal working material; confirm before public use. |
| **U** | Unsupported | Exclude. |

**Documented facts** may come from dated research, requirements, design history, decisions, meeting notes, QA logs, approvals, a released product, analytics, or another traceable project artifact.

**Corroborated reconstruction** requires converging project evidence, or project evidence that agrees with a confirmed recollection. It cannot manufacture chronology or imply that today’s language was explicitly used at the time.

**Contextual reconstruction** may establish regulation, market conditions, publicly known technology constraints, competitor capabilities, or category expectations. It cannot establish what the team knew, what discussions occurred, why a decision was made, or who made it.

**Working inference** is a plausible proposition awaiting confirmation. It may guide questions and evidence gathering, but it must not enter a public case study as historical fact.

Research evidence should establish people’s needs, circumstances, constraints, and the outcomes they seek; it should not merely validate an assumed solution.[source](source-index.md#src-gov-user-needs)

### Lifecycle and outcome-claim status

| Claim state | Safe wording |
| :---| :---|
| **Hypothesized** | “We hypothesized that…” |
| **Targeted** | “We aimed to…” |
| **Designed** | “The experience was designed to…” |
| **Validated** | “Testing indicated…” |
| **Approved** | “Stakeholders approved…” |
| **Implemented** | “The team implemented…” |
| **Released** | “The experience was released and live…” |
| **Qualitatively observed** | “Stakeholders or users reported…” |
| **Quantitatively measured** | “The recorded data showed…” |
| **Contribution supported** | “The available evidence indicates that the work contributed to…” |
| **Causally attributed** | Use “caused” or “resulted in” only when the evaluation design supports causal attribution. |

Released does not mean successful. A change observed after release does not automatically mean the design caused it.

Contribution and causal attribution are deliberately separate. Contribution analysis can strengthen a reasoned claim that an intervention helped produce change, but causal wording requires an evaluation design capable of ruling out credible alternative explanations.[source](source-index.md#src-magenta-contribution)

### Ownership vocabulary

| Ownership type | Appropriate language |
| :---| :---|
| **Led and decided** | “I set…”, “I decided…”, “I established…” |
| **Directed or delegated** | “I directed…”, “I assigned…”, “I guided…” |
| **Co-led or influenced** | “I helped shape…”, “I influenced…”, “We jointly decided…” |
| **Personally designed** | “I designed…”, “I defined…” |
| **Reviewed or approved** | “I reviewed…”, “I quality-gated…”, “I approved…” |
| **Supported or informed** | “I contributed evidence…”, “I advised…” |
| **Team or organizational result** | “The team released…”, “The organization observed…” |

Leading through direction, trade-off decisions, review, delegation, and quality approval is legitimate design leadership. It must not be rewritten as personal production work.

## A universal writing grammar keeps the reasoning readable

Each formal component statement should be capable of expressing five elements:

> **For [specific actor], in [relevant context], [level-specific proposition], because [evidence or strategic rationale], so that [relationship to the intended human outcome].**

Not every final sentence needs all five clauses, but the underlying reasoning must contain them.

### Writing rules

- Name the actor whenever evidence permits; avoid generic “users.”
- Make one principal claim per sentence.
- Separate evidence from interpretation.
- Separate current state from desired future state.
- Use active voice for decisions and state ownership explicitly.
- Define adjectives through observable qualities.
- Preserve human purpose when introducing business or technical constraints.
- Do not select a solution mechanism before Level 10.
- Introduce features as enabling mechanisms at Level 11, not as upstream strategy.
- Use dates or sequence markers when making historical claims.

### Replace vague language

| Avoid | Prefer |
| :---| :---|
| Seamless | Without re-entering information, changing channels, or losing progress |
| Intuitive | People could proceed without assistance or repeated correction |
| Efficient | Required fewer steps, less time, less coordination, or less cognitive effort |
| Delightful | Produced a specifically evidenced positive emotional response |
| Improved | State exactly what became better and how it was observed |
| Transformed | Describe the before-and-after system change |
| Ensured | Use “designed to,” “validated that,” or “verified that” |
| Users | Name the evidenced role or behavioral group |

## A traceability record connects claims to consequences

Every significant component claim receives a private traceability record.

The record operationalizes two complementary controls: maintain traceability from evidenced needs into requirements and delivery decisions, and make the intended pathway from actions to outcomes explicit enough to test.[source](source-index.md#src-teal-traceability) [source](source-index.md#src-toc-toolkit)

| Field | Purpose |
| :---| :---|
| **Claim ID** | Stable identifier such as `L8-CE-01`. |
| **Level** | Correct architectural classification. |
| **Statement** | Exact claim. |
| **Upstream parent** | Higher-level claim that justifies it. |
| **Downstream child** | Decision, behavior, or artifact it shapes. |
| **Evidence references** | Project artifacts, confirmed recollection, or external sources. |
| **Provenance** | D, R, C, I, or U. |
| **Lifecycle state** | Targeted, designed, released, observed, measured, and so forth. |
| **Ownership** | Led, designed, reviewed, supported, or team result. |
| **Date or period** | Historical placement where known. |
| **Open question** | Missing confirmation or evidence. |
| **Publication status** | Safe, qualified, internal-only, or excluded. |

## Reconstruction needs a visible gate

A reconstructed component may be accepted only when all applicable conditions pass:

1. At least one legitimate project-evidence source exists.
2. The interpretation is consistent with the project’s known chronology.
3. It explains multiple downstream decisions, not only one convenient interface.
4. It does not assume the implemented solution was inevitable.
5. Alternative explanations have been considered.
6. External research is used only for surrounding context.
7. Ownership can be stated accurately.
8. Uncertainty is recorded.
9. Wording matches the evidence class and lifecycle state.
10. The reconstruction improves traceability without inventing causality.

A reconstruction fails immediately when the solution is the only evidence for the alleged problem or strategy.

## A ten-gate quality audit tests the guide before use

Verification and validation are not synonyms: the team must examine both whether the defined system was implemented correctly and whether the resulting system addresses the intended need in its operating context.[source](source-index.md#src-nasa-vv)

| Gate | Test |
| :---| :---|
| 1 | Does it answer its governing question directly? |
| 2 | Is the unit of analysis at the correct granularity? |
| 3 | Is content from adjacent levels excluded? |
| 4 | Are the actor and context sufficiently specific? |
| 5 | Is every historical claim evidence-classified? |
| 6 | Does the language match lifecycle and ownership status? |
| 7 | Is the component traceable upward and downward? |
| 8 | Is the level solution-neutral where required? |
| 9 | Does it preserve the intended human improvement? |
| 10 | Does it enable a concrete decision at the next level? |

### Hard-failure conditions

A component cannot be approved if it contains:

- unsupported historical strategy;
- a solution presented as the origin of its own problem;
- a target presented as an achieved outcome;
- a business metric substituted for human improvement;
- a later portfolio summary presented as contemporaneous evidence;
- external research presented as the team’s historical insight;
- personal ownership inflated beyond the evidence;
- a feature disguised as an experience;
- a generic actor where distinct actors materially differ;
- causal language without causal evidence;
- no traceable relationship to the levels above or below; or
- a polished artifact treated as proof that the underlying experience worked.

## Experience-first leadership signals remain evidence-bound

Each level should identify only the leadership signals the evidence supports:

- starting above the product;
- building deep human and contextual understanding;
- seeing the entire ecosystem;
- separating opportunity from solution;
- defining a meaningful human outcome;
- establishing and communicating an experience vision;
- making explicit experience trade-offs;
- connecting human, product, and business value;
- prioritizing experiences rather than features;
- orchestrating across functional boundaries;
- maintaining traceability into interaction and interface decisions;
- protecting experience integrity through design QA; and
- learning from the live experience.

## Use this Level Guide template when a formal record is needed

```markdown
## Level [N] — [Final Name]

**Terminology status:**
**Component availability:**

### Definition

### Governing question

### Strategic job

### Unit of analysis and scope

### Expert and source anchors

### Reasoning formula

### What belongs

### What does not belong

### Boundary with the level above

### Boundary with the level below

### Required evidence

### Permitted reconstruction

### Claim, lifecycle, and ownership controls

### Writing grammar

### Canonical output and traceability

### Quality audit
- Pass/fail tests
- Experience-first leadership signal
- Common failure modes
```

---

## The standard ends where the level-specific guide begins

Apply the template at the decision level that the evidence supports. The [Level Map](level-map.md) identifies the correct guide; the [Experience Ecosystem](experience-ecosystem.md) keeps wider system relationships visible when they matter.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [International Organization for Standardization, ISO 9241-210:2019, “Ergonomics of Human-System Interaction — Part 210: Human-Centred Design for Interactive Systems.”](source-index.md#src-iso-hcd) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Start by Learning User Needs.”](source-index.md#src-gov-user-needs) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [UK Government Project Delivery Function, The Teal Book, “Chapter 31: User Needs and Requirements.”](source-index.md#src-teal-traceability) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [UK Government Analysis Function, “The Analysis Function Theory of Change Toolkit.”](source-index.md#src-toc-toolkit) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [HM Treasury and UK Evaluation Task Force, The Magenta Book, “Annex A: Analytical Methods for Use Within an Evaluation,” section on contribution analysis.](source-index.md#src-magenta-contribution) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [NASA Independent Verification and Validation Program, “IV&V Overview.”](source-index.md#src-nasa-vv) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
