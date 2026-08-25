# Level 10 — Solution Concepts

Use this Level Guide to classify, formulate, and audit **Solution Concepts** without leaking adjacent decisions into it.

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

**Established design activity; playbook-specific resolution.**

Concept generation, divergent ideation, prototyping, and solution discovery are established practices. “Solution Concept” here means a coherent candidate approach at a deliberately pre-interface resolution. It is not a synonym for a feature idea, mockup, final design, or validated product.

## Definition

A Solution Concept is **a coherent candidate explanation of how a product-service system could enable one or more Critical Experiences across priority scenarios**.

It specifies the proposed mechanism, system role, actor–system relationship, scenario coverage, assumptions, dependencies, and trade-offs at enough resolution to compare and test—but before the team commits to a detailed capability set, interaction architecture, or interface.

A concept should be distinguishable by its underlying approach, not merely by visual treatment. “Blue cards,” “compact cards,” and “large cards” are variations of presentation. “Ask the person,” “infer context,” “combine social signals,” and “let the person progressively steer” are meaningfully different concept mechanisms.

## Governing question

> **What meaningfully different, evidence-responsive approaches could enable the Critical Experience across its priority scenarios, and what must be true for each approach to create human value responsibly and work in practice?**

## Strategic job

This level prevents an opportunity from becoming a disguised requirement. It:

- creates alternatives before delivery investment hardens one answer;
- keeps the Critical Experience and scenario evidence as the evaluation frame;
- makes the mechanism and actor–system relationship explicit;
- exposes value, usability, feasibility, viability, accessibility, safety, privacy, and ethical assumptions early;
- invites product, design, engineering, research, data, content, policy, operations, and domain expertise into convergence;
- supports cheap tests of the riskiest assumptions;
- makes rejected, deferred, combined, and selected concepts traceable; and
- gives Level 11 a justified concept to decompose into enabling capabilities and features.

## Unit of analysis and scope

The unit is **one coherent candidate mechanism or system model** for enabling a declared Critical Experience and scenario set.

Each concept should declare:

- the target Critical Experience, actor, and priority scenarios;
- the essential mechanism and value proposition;
- what the actor does, what the system/service does, and where control sits;
- what changes from the current experience;
- boundaries, dependencies, and excluded scenarios;
- assumptions and the evidence behind them;
- material risks, trade-offs, and unintended consequences;
- the testable prediction and cheapest credible learning method; and
- current decision status.

Explore multiple concepts when the decision is consequential or meaningfully uncertain. Do not manufacture arbitrary variations to satisfy a ritual. When only one lawful or feasible mechanism exists, document that constraint and test the remaining assumptions rather than pretend there were alternatives.

## Expert and source anchors

Teresa Torres’s Opportunity Solution Tree separates outcome, opportunity space, solution space, and assumption tests. Her method recommends brainstorming for a selected opportunity, exploring multiple solutions, breaking them into assumptions, and testing the riskiest assumptions before deciding what to build.[source](source-index.md#src-torres-ost)

The Design Council’s Double Diamond asks teams first to understand and define the problem, then to develop different answers and test, reject, and improve solutions at small scale.[source](source-index.md#src-design-council-double-diamond)

SVPG’s four-risk framing makes explicit that a product solution must address value, usability, feasibility, and business viability, and that strong teams address these risks collaboratively and early.[source](source-index.md#src-cagan-four-risks)

UXReactor's public framework supports connecting user research, experience strategy, and design work. Meridian applies that connection by holding problem framing, alternative concepts, assumptions, and rationale together before a team commits to one mechanism.[source](source-index.md#src-uxreactor-5d)

These sources support divergence, risk testing, collaboration, and traceability. The exact pre-interface concept definition and Level 9/11 boundary are this playbook’s synthesis.

## Reasoning formula

```text
SOLUTION CONCEPT
= selected Critical Experience and priority scenarios
+ coherent mechanism or system model
+ actor role, system/service role, and locus of control
+ intended change from the current experience
+ scenario coverage and exclusions
+ value, usability, feasibility, and viability assumptions
+ accessibility, safety, privacy, fairness, and ethical assumptions
+ dependencies, trade-offs, and unintended-consequence hypotheses
+ testable prediction and learning plan
+ provenance and decision status
− detailed UI, component list, or feature specification

CONCEPT DECISION
= comparative evidence against experience and scenario criteria
+ tests of the riskiest differentiating assumptions
+ cross-functional judgment and constraints
+ documented trade-offs, reversibility, and residual risk
− preference, visual polish, executive enthusiasm, or build ease alone
```

## What belongs

- Target Critical Experience and scenario coverage.
- A coherent solution mechanism or service model.
- Actor–system roles, degree of initiative, and locus of control.
- The hypothesized change to the current experience.
- Multiple meaningfully different candidates where uncertainty warrants them.
- Value, usability, feasibility, and viability assumptions.
- Accessibility, inclusion, safety, privacy, security, fairness, sustainability, and ethical assumptions as relevant.
- Dependencies on people, operations, policy, data, models, integrations, and technology.
- Trade-offs, failure implications, misuse, and unintended consequences.
- Low-cost evidence such as sketches, storyboards, role-play, technical spikes, data probes, or prototypes appropriate to the risk.
- Comparative criteria, decision record, residual uncertainty, and concept status.

## What does not belong

- The first stakeholder request restated as a concept.
- A feature name without a coherent mechanism and experience rationale.
- Cosmetic screen variations masquerading as strategic alternatives.
- A detailed navigation model, state chart, workflow, component inventory, or interface specification.
- A full capability map or delivery backlog.
- A prototype presented as proof merely because it exists.
- A brainstorm count used as evidence of quality.
- A desirability claim inferred from stakeholder approval.
- A feasibility claim made without engineering input.
- A selected concept described as validated, implemented, released, or successful without matching evidence.
- Alternatives invented retrospectively to make convergence look rigorous.

## Adjacent-level boundaries

**Above — Level 9, Scenarios and Journeys:** Level 9 defines the circumstances, sequence, needs, and breakdowns the design must address. It should not make one mechanism inevitable. Level 10 proposes and compares the mechanisms that might create the intended experience across those conditions.

**Below — Level 11, Enabling Capabilities and Features:** Level 10 says **how the system might work in principle**. Level 11 identifies **what stable abilities and concrete mechanisms must exist** for the selected concept to work. A concept can be selected while its capability feasibility remains unresolved.

**Prototype boundary:** A prototype is an evidence instrument, not a level by itself. Low-resolution prototypes may test a Level 10 concept; interaction and interface prototypes primarily resolve Levels 12 and 13. Always name the assumption and fidelity purpose.

## Required evidence

A credible concept set and decision require:

- a selected Critical Experience and priority scenario set;
- Current Experience and opportunity evidence;
- explicit experience qualities and concept-evaluation criteria;
- more than one meaningfully different candidate when a real choice existed;
- user, service, policy, business, market, data, and technical constraints appropriate to the concept;
- assumption mapping across value, usability, feasibility, viability, and responsible-design risks;
- risk-proportionate evidence from research, prototypes, technical spikes, policy review, operations, data analysis, or experiments;
- cross-functional participation from the competencies needed to judge the concept;
- a comparison that records rejection, selection, combination, deferral, and residual uncertainty; and
- traceability from evidence to concept and from concept to later capabilities and outcomes.

The team does not need equal evidence for every candidate. It does need enough evidence to explain why investment moved, stopped, or remained conditional.

## Permitted reconstruction

**Permitted:**

- identify the operative concept embodied across dated requirements, diagrams, flows, prototypes, design reviews, and implemented behavior;
- reconstruct the concept’s mechanism and dependencies as a retrospective explanatory model;
- identify documented alternatives, rejected ideas, or changed directions from comments, sketches, tickets, and meeting records;
- use confirmed recollection to clarify why an evidenced alternative changed;
- label untested assumptions and residual risks revealed by later evidence; and
- use external research to compare market or technical patterns without claiming the team used that research historically.

**Not permitted:**

- invent alternative concepts, ideation workshops, prototypes, tests, or decision criteria;
- claim the implemented solution was selected through comparison when only the final direction is evidenced;
- infer user validation from approval, build completion, adoption, or lack of complaints;
- reconstruct a strategic rationale solely from the final interface;
- describe engineering feasibility, legal approval, or business viability without the responsible evidence;
- erase concept changes, compromises, or unsupported scenarios to produce a clean story; or
- claim a retrospective concept model was an explicit historical artifact.

When only the final mechanism is evidenced, call it **“operative concept reconstructed from delivery artifacts”**, not **“the winning concept.”**

## Claim, lifecycle, and ownership controls

- **Component availability:** A concept set and a selected concept may be separately Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable. A polished mockup does not prove alternative exploration.
- **Provenance:** Classify concept mechanism, alternatives, assumptions, tests, decision criteria, selection rationale, and residual risk separately.
- **Lifecycle:** Use **idea, candidate concept, explored, prototyped, assumption-tested, rejected, combined, selected conditionally, selected, superseded, designed, implemented, released, or observed** only with supporting evidence. “Selected” is a decision state, not outcome evidence.
- **Ownership:** Distinguish “I generated,” “I facilitated,” “I modeled,” “I prototyped,” “I recommended,” “we selected,” and “leadership approved.” Credit product, engineering, research, data, policy, and operational contributors to the risks they helped resolve.

## Writing grammar

**Concept formula**

> **For [actor + Critical Experience + priority scenarios], use [coherent mechanism] so that [actor role] and [system/service role] enable [intended experience change]. This depends on [key capabilities/conditions] and assumes [riskiest assumptions]. Compared with [alternatives], it favors [benefit] while accepting [trade-off]. We will learn by [test + evidence threshold].**

**Illustrative concept set**

```text
Concept A — Explicit intent
Let the listener describe or choose the state they want, then generate a direction
they can inspect and steer. Favors agency and intelligibility; risks input burden.

Concept B — Contextual inference
Infer a likely direction from context and history, then make correction cheap.
Favors immediacy; risks opacity, privacy concerns, and confident misinterpretation.

Concept C — Progressive steering
Start with a broad direction and let lightweight reactions refine the session.
Favors low initial effort and recovery; may delay a strongly fitting result.
```

These are hypothetical concept mechanisms for illustrating the writing grammar, not claims about Spotify’s internal alternatives.

## Canonical output and traceability

The canonical output is a **Concept Set, Assumption Map, and Decision Record** containing:

- parent Critical Experience and scenario coverage;
- current-experience evidence and evaluation criteria;
- candidate concepts expressed at comparable resolution;
- mechanism, actor role, system/service role, scope, and exclusions for each;
- sketches, storyboards, prototypes, service models, or technical probes as appropriate;
- assumptions across value, usability, feasibility, viability, and responsible design;
- dependency, trade-off, misuse, failure, and unintended-consequence analysis;
- tests, evidence, confidence, and decision thresholds;
- selected, combined, rejected, deferred, and unresolved concepts with rationale;
- residual risks, owners, and next learning step; and
- traceability upstream to scenarios and strategy, and downstream to capabilities, features, interaction architecture, implementation, release, and outcomes.

## Quality audit

**Pass when:**

- each candidate is a coherent mechanism rather than a UI treatment;
- concepts respond to the same Critical Experience and comparable scenario criteria;
- meaningful alternatives exist where there was real uncertainty;
- assumptions and risks are explicit and tested proportionately;
- selection reflects evidence and multidisciplinary judgment;
- rejected directions and residual uncertainty remain visible; and
- the chosen concept can be decomposed into capabilities without becoming a feature backlog first.

**Fail when:**

- the requested feature is treated as the only possible answer;
- divergence is decorative or purely visual;
- polished prototypes create false confidence;
- one discipline silently judges all risks;
- accessibility, safety, privacy, policy, or operational consequences appear only after selection;
- a selected concept is described as validated or successful; or
- retrospective alternatives or tests are invented.

**Experience-first leadership signal:** The designer keeps teams attached to the human experience while creating genuine alternatives, orchestrates the right expertise around risk, and makes convergence an evidence-visible decision rather than a preference contest.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [Teresa Torres / Product Talk, “Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes.”](source-index.md#src-torres-ost) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [Design Council, “The Double Diamond.” Especially the Discover, Define, Develop, and Deliver descriptions.](source-index.md#src-design-council-double-diamond) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [Marty Cagan, “The Four Big Risks.” Silicon Valley Product Group.](source-index.md#src-cagan-four-risks) | Product vision, product strategy, problem selection, and product risk. |
| [UXReactor, "5-D Framework for Experience Strategy, User Research, and Experience Design."](source-index.md#src-uxreactor-5d) | Experience-first operating practice synthesized from the approved UXReactor sources. |
