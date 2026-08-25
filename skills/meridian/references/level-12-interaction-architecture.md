# Level 12 — Interaction Architecture

Use this Level Guide to classify, formulate, and audit **Interaction Architecture** without leaking adjacent decisions into it.

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

**Playbook-synthesized operating level; source-adapted practice.**

Interaction frameworks, information architecture, workflows, conceptual models, state models, and navigation systems are established design practices. “Interaction Architecture” is this playbook’s umbrella label for resolving them as one coherent actor–system model before interface-detail decisions dominate. It is not presented as a universal UX level or as Kim Goodwin’s formal term.

## Definition

Interaction Architecture is the **coherent, medium-aware but interface-independent model of how people, systems, services, information, and rules cooperate over time to enable the selected Solution Concept across its priority scenarios**.

It resolves:

- what information and domain objects exist from the actor’s point of view;
- what actions people, systems, and service roles can take;
- how people enter, orient, progress, pause, resume, transfer, complete, and recover;
- which states, transitions, permissions, rules, and dependencies govern behavior;
- what the system initiates, recommends, automates, blocks, or explains;
- where people retain control, visibility, consent, and reversal;
- how feedback and status preserve a coherent mental model; and
- how the experience continues across channels, devices, roles, and time.

It is more resolved than a capability map and less resolved than a screen or component specification. A diagram is not automatically an Interaction Architecture; the architecture is the behavioral logic the artifact communicates.

## Governing question

> **How should the actor and the wider product-service system cooperate—through information, objects, actions, initiative, states, rules, feedback, handoffs, and recovery—so the selected concept enables the Critical Experience across priority scenarios?**

## Strategic job

This level converts a promising concept into a coherent behavioral system before visual polish creates false completeness. It:

- preserves the Critical Experience and scenarios while resolving concrete cooperation;
- integrates visible interaction with backstage service, policy, data, and operational behavior;
- establishes a conceptual model that people can understand and predict;
- reconciles information architecture, workflow, navigation, state logic, permissions, and content structure;
- makes system initiative, automation, AI behavior, and user agency explicit;
- designs waiting, interruption, exception, denial, handoff, and recovery as first-class states;
- exposes missing capabilities, data relationships, policies, and technical constraints early;
- provides a stable behavioral source for interface definition, prototype construction, implementation requirements, and analytics; and
- prevents individual screens or teams from optimizing fragments at the expense of the end-to-end experience.

## Unit of analysis and scope

The unit is **one interaction model for a declared Critical Experience and coherent scenario family**, including the domain objects, actor roles, system responsibilities, states, transitions, rules, and channels required to reach or recover toward the intended result.

Declare:

- the Critical Experience, selected concept, capabilities, and scenarios in scope;
- primary and co-actors, roles, permissions, and responsibility boundaries;
- entry, exit, pause, transfer, and recovery boundaries;
- core domain objects and the actor’s conceptual model of them;
- actions available to each actor or system;
- state vocabulary, transitions, events, preconditions, and business rules;
- navigation and information relationships;
- system initiative, automation, explanation, consent, control, and override;
- feedback, progress, status, confirmation, and error behavior;
- cross-channel, cross-device, offline, assisted, and temporal continuity;
- quality constraints such as accessibility, privacy, security, safety, latency, and reliability; and
- exclusions, unresolved decisions, and implementation dependencies.

One architecture can span several screens, channels, and teams. Separate models when actors have fundamentally different responsibilities or when a single diagram would conceal incompatible state systems.

## Expert and source anchors

Kim Goodwin describes moving from personas and scenarios to requirements, then using design patterns and principles to create an **interaction framework**—the initial sketch of the design that determines what functionality is available and what belongs together.[source](source-index.md#src-goodwin-interaction-framework) This directly supports a bridge between scenarios and interface detail.

UXReactor's public RedSeal case study reinforces a user-centered, system-aware view before detailed interface work. Meridian therefore anchors interaction architecture in journeys, problems, outcomes, scenarios, data relationships, start and end points, and workflow variations.[source](source-index.md#src-uxreactor-redseal)

ISO 9241-210 positions design solutions within an iterative human-centred process grounded in context of use, user requirements, and evaluation across the lifecycle.[source](source-index.md#src-iso-hcd) It supports the evidence and iteration controls here without defining this playbook’s Interaction Architecture level.

GOV.UK’s whole-problem guidance requires teams to account for online and offline touchpoints, back-end processes, evidence, and organizational boundaries.[source](source-index.md#src-gov-whole-journey) This supports modeling the wider system rather than only the visible interface.

The exact umbrella definition, formula, and Level 11/13 boundary below are this playbook’s synthesis.

## Reasoning formula

```text
INTERACTION ARCHITECTURE
= selected Solution Concept
+ Critical Experience and priority scenario requirements
+ enabling capabilities and quality conditions
+ actor roles, permissions, and responsibility boundaries
+ domain objects, information relationships, and conceptual model
+ human actions and system/service actions
+ entry, exit, states, transitions, events, and rules
+ system initiative, explanation, consent, control, and override
+ feedback, progress, confirmation, exception, and recovery
+ cross-channel, cross-device, assisted, and temporal continuity
+ accessibility, privacy, safety, security, latency, and reliability constraints
+ evidence, assumptions, unresolved decisions, and traceability
− pixel layout, visual styling, or component-level specification

COHERENCE TEST
= every scenario can traverse the model or reach a designed recovery
+ every state has an intelligible cause, status, action, and next condition
+ every capability has a behavioral role
+ every automation preserves appropriate visibility and control
− hidden state, dead end, contradictory rule, or channel-only logic
```

## What belongs

- Actor roles, co-actors, permissions, responsibility, and handoffs.
- Conceptual model and actor-facing domain objects.
- Information architecture, relationships, taxonomy, hierarchy, and findability logic.
- Entry points, orientation, navigation, task structure, and workflow.
- Actions available to people, systems, and service roles.
- State inventories, transitions, events, preconditions, and business rules.
- System initiative, automation, recommendation, AI behavior, consent, explanation, override, and reversal.
- Feedback, status, progress, confirmation, waiting, and interruption behavior.
- Error prevention, exception, denial, abandonment, escalation, and recovery.
- Cross-channel, device, role, session, and offline continuity.
- Accessibility behavior such as logical sequence, focus intent, non-pointer alternatives, time limits, and preservation of work at an architectural level.
- Data, service, policy, content, operational, technical, and quality dependencies.
- Scenario coverage, unresolved decisions, evidence confidence, and traceability.

## What does not belong

- Page composition, typography, color, iconography, spacing, visual hierarchy, or final component anatomy.
- A row of screens connected by arrows with no state or rule logic.
- A sitemap that represents only content location.
- A happy-path task flow that ignores exceptions and recovery.
- A data model copied directly into navigation without evidence of the actor’s mental model.
- API endpoints, database tables, or technical architecture presented as the interaction model.
- A detailed design-system specification.
- A polished prototype used as a substitute for explicit behavior.
- Feature ownership or current team boundaries used to split the experience.
- A requirement list with no model of how requirements cooperate.
- Accessibility deferred to visual design or production testing.
- A historical rationale inferred only from the released interface.

## Adjacent-level boundaries

**Above — Level 11, Enabling Capabilities and Features:** Level 11 identifies the abilities and justified mechanisms that must exist. Level 12 organizes those abilities into actor–system cooperation. **Preserve progress** is a capability; the state transitions for saving, resuming, expiring, transferring, and recovering work belong here.

**Below — Level 13, Interface Definition and Prototyping:** Level 12 defines behavior without settling every perceptual and component detail. Level 13 expresses the architecture through layouts, controls, content, visual hierarchy, responsive behavior, interaction states, and prototypes. A screen may change while the interaction architecture remains stable; if the object model, sequence, permissions, or state rules change, the architecture has changed.

**Technical-architecture boundary:** Interaction Architecture must be feasible and connected to technical architecture, but they are not interchangeable. One describes how actors and services cooperate toward an experience; the other describes how software and infrastructure are structured to provide it.

## Required evidence

A credible Interaction Architecture requires:

- a selected concept with explicit assumptions and trade-offs;
- Critical Experience boundaries and priority scenario coverage;
- a Capability-to-Experience Map;
- evidence of actor goals, mental models, vocabulary, current behavior, breakdowns, and recovery needs;
- domain, content, data, policy, role, permission, security, privacy, accessibility, and operational rules;
- input from product, design, research, engineering, content, data, operations, policy, security, accessibility, and domain experts as relevant;
- evidence or explicit hypotheses for system initiative and user-control choices;
- state, transition, exception, and cross-channel completeness checks;
- feasibility review and known technical constraints;
- prototype or evaluative evidence appropriate to the riskiest interaction assumptions; and
- bidirectional traceability to capabilities, scenarios, requirements, interface states, tests, and outcome instrumentation.

Design conventions can reduce learning burden, but convention alone is not evidence that a model fits the domain or actor. Novel interaction rules require stronger explanation and evaluation.

## Permitted reconstruction

**Permitted:**

- reconstruct the implemented interaction model from dated flows, wireframes, prototypes, state annotations, requirements, tickets, APIs, data rules, QA evidence, and released behavior;
- infer necessary states and transitions when several independent artifacts demonstrate them;
- create a current retrospective state model to explain complex delivered work, labeling it as reconstruction;
- distinguish the intended design model from implementation deviations documented in QA;
- use confirmed recollection to clarify verbal decisions, engineering constraints, permissions, or cross-role behavior;
- show unresolved or contradictory behavior rather than force false coherence; and
- use external standards or domain research to assess the model without claiming those sources drove the historical design.

**Not permitted:**

- claim the architecture preceded screen design when it was reconstructed afterward;
- infer actor mental models, preferred vocabulary, comprehension, or confidence from the interface alone;
- invent alternative architectures, state workshops, technical reviews, or validation activities;
- treat a shipped flow as proof that the interaction was coherent or usable;
- erase implementation compromises, missing states, or unsupported scenarios;
- convert technical constraints into user needs; or
- attribute cross-functional decisions solely to design without evidence.

When only the delivered behavior is known, use **“The implemented interaction model can be reconstructed as…”** rather than **“We architected the interaction as…”**.

## Claim, lifecycle, and ownership controls

- **Component availability:** Interaction Architecture may be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable. A set of screens does not automatically establish an explicit architecture artifact.
- **Provenance:** Classify object model, information structure, sequence, state logic, permission rules, system initiative, recovery, accessibility behavior, and rationale separately.
- **Lifecycle:** Use **candidate, modeled, compared, reviewed, prototyped, partially supported by evaluation, implementation-defined, implemented, verified, changed, or superseded** according to evidence. Do not label an entire architecture “validated” because one flow performed well in one study.
- **Ownership:** Distinguish “I modeled,” “I facilitated,” “I specified,” “I recommended,” “we resolved,” “engineering constrained,” and “policy required.” Name decision authority and contributing disciplines for material rules.

## Writing grammar

**Architecture formula**

> **To enable [Critical Experience] through [selected concept], [actor] enters through [condition], understands and acts on [objects/information], while [system/service/co-actors] perform [responsibilities]. Progress moves through [states/transitions] under [rules/permissions]. The system provides [feedback/explanation], preserves [control/continuity], and supports recovery through [path]. This model depends on [capabilities and constraints] and excludes [scope].**

**Illustrative application**

```text
To enable moment-based discovery through progressive steering, the listener enters
with explicit or inferred intent, receives a proposed listening direction, and can
accept, inspect, steer, pause, or reset it. The service preserves session context,
explains enough of the direction to support correction, and treats a poor fit as a
recoverable state rather than a dead end. Intent, direction, session, and feedback
are distinct objects; privacy consent and low-attention use constrain automation.
```

This is an illustrative interaction model, not a claim about Spotify’s internal architecture.

## Canonical output and traceability

The canonical output is an **Interaction Architecture Specification** containing:

- scope, version, owners, contributors, status, and decision log;
- parent Critical Experiences, scenarios, concept, and capabilities;
- actor-role and permission model;
- conceptual model, domain objects, vocabulary, and relationships;
- information architecture and navigation model;
- workflow, entry/exit, actions, and responsibility allocation;
- state inventory, transition model, events, preconditions, and business rules;
- system initiative, automation, AI, consent, explanation, control, and override behavior;
- feedback, progress, waiting, confirmation, exception, escalation, and recovery;
- cross-channel, cross-device, assisted, offline, and session continuity;
- content, accessibility, privacy, security, safety, performance, and reliability constraints;
- scenario-to-state coverage, unresolved decisions, assumptions, and evidence; and
- traceability upstream to Levels 0–11 and downstream to interface states, prototypes, requirements, tests, implementation, instrumentation, and live outcomes.

The artifact can be expressed through a combination of object maps, service blueprints, flows, statecharts, permission matrices, content models, and rule tables. Choose the smallest set that communicates the logic without hiding consequential behavior.

## Quality audit

**Pass when:**

- the model can explain how every priority scenario begins, progresses, completes, or recovers;
- actors, objects, actions, states, transitions, rules, and responsibility are coherent;
- system initiative and user control are deliberate and evidence-responsive;
- exceptions, waiting, denial, interruption, and cross-channel continuity are designed;
- accessibility and quality behavior are architectural inputs rather than final checks;
- technical and operational dependencies are visible without defining the experience; and
- each interface state and requirement can trace back to the model.

**Fail when:**

- screens, a sitemap, or an API diagram substitute for behavioral architecture;
- happy-path arrows conceal states and rules;
- navigation mirrors the org chart or legacy data model without actor evidence;
- automation acts without intelligible status, consent, correction, or recovery;
- exceptions are postponed to engineering;
- the model cannot explain one or more priority scenarios; or
- historical intent and validation are inferred from the shipped interface.

**Experience-first leadership signal:** The designer makes the whole actor–system relationship coherent before interface detail fragments attention, aligns disciplines around behavior and recovery, and protects human agency and purpose as the design becomes implementable.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [Kim Goodwin / UIE, “Goal-Directed Design: An Interview with Kim Goodwin.” Center Centre.](source-index.md#src-goodwin-interaction-framework) | Scenarios, goal-directed design, and interaction frameworks. |
| [UXReactor, "Beyond the Legacy: How a Former Cybersecurity Leader Pivoted to the Cloud Through User-Centered Design."](source-index.md#src-uxreactor-redseal) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [International Organization for Standardization, ISO 9241-210:2019, “Ergonomics of Human-System Interaction — Part 210: Human-Centred Design for Interactive Systems.”](source-index.md#src-iso-hcd) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Map and Understand a User’s Whole Problem.”](source-index.md#src-gov-whole-journey) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
