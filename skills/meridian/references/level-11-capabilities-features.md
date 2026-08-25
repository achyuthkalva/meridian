# Level 11 — Enabling Capabilities and Features

Use this Level Guide to classify, formulate, and audit **Enabling Capabilities and Features** without leaking adjacent decisions into it.

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

**Established but overloaded terms; playbook-specific taxonomy.**

Product, business, service, and enterprise disciplines use “capability” and “feature” differently. This playbook does not claim one universal definition. It uses a deliberate experience-first distinction: a **capability is an ability that must exist**; a **feature is a concrete product or service mechanism that provides, exposes, or uses that ability**.

This borrows the stable “ability” sense of capability from architecture practice while adapting it to product-service experience design. The Open Group’s ArchiMate specification treats capability as an ability possessed by an organization, person, or system; this playbook permits organizational, service, operational, data, policy, and technical capabilities but requires every included capability to trace to a Critical Experience.[source](source-index.md#src-archimate-capability)

## Definition

An **enabling capability** is a durable ability that a product-service ecosystem—including people, process, policy, data, content, operations, and technology—must possess at a required quality level for a selected Solution Concept to enable its Critical Experiences.

A **feature** is a scoped, concrete product or service behavior, affordance, or mechanism through which one or more capabilities are provided to or used on behalf of an actor.

Examples:

- **Capability:** preserve a person’s progress securely across sessions.
- **Possible features/mechanisms:** save draft, autosave, resume link, authenticated case dashboard, or assisted-service retrieval.

- **Capability:** let a person understand and correct a system-generated direction.
- **Possible features/mechanisms:** explanation cues, preference controls, negative feedback, undo, reset, or escalation.

The capability states **what ability must exist**. The feature states **one concrete mechanism selected to realize or expose that ability**. A requirement later states **the verifiable behavior or quality the implementation must satisfy**.

## Governing question

> **What abilities must the whole product-service ecosystem possess, at what quality, and through which justified features or mechanisms, for the selected concept to enable the Critical Experience across its priority scenarios?**

## Strategic job

This level converts a selected concept into an experience-traceable enablement model. It:

- identifies the abilities required across product, service, operations, policy, data, content, and technology;
- prevents the visible interface from hiding backstage dependencies;
- shows which capabilities enable several Critical Experiences and where reuse is valuable;
- reveals capability gaps, maturity limits, risks, and sequencing dependencies;
- derives features from experience and concept needs rather than treating the backlog as strategy;
- distinguishes durable abilities from temporary manifestations;
- creates shared planning language for design, product, engineering, architecture, operations, policy, QA, and support; and
- supplies the ingredients Level 12 will organize into information, actions, states, and rules.

## Unit of analysis and scope

There are three connected units:

1. **Capability:** one stable ability, stated without assuming a particular interface, vendor, component, or team.
2. **Feature/mechanism:** one scoped manifestation that realizes, exposes, or uses one or more capabilities for a declared actor and scenario.
3. **Capability-to-experience map:** the many-to-many relationships among Critical Experiences, concepts, scenarios, capabilities, features, enabling owners, dependencies, and quality conditions.

Declare:

- whether the capability is human, organizational, service, operational, policy, data, content, model/algorithm, application, integration, infrastructure, or cross-cutting;
- the actor and Critical Experiences it enables;
- the selected concept and scenarios that require it;
- current versus required maturity or quality;
- provider or accountable owner, users/consumers, dependencies, and constraints;
- relevant security, privacy, accessibility, reliability, safety, latency, explainability, and governance qualities; and
- how availability and fitness will be verified.

Avoid capability statements so broad that they become corporate aspirations or so narrow that they are components in disguise.

## Expert and source anchors

The Open Group’s ArchiMate standard provides the useful architecture distinction between a capability—an ability possessed by an organization, person, or system—and the structures or behaviors that realize it.[source](source-index.md#src-archimate-capability) This playbook adapts that distinction rather than importing the complete enterprise-architecture metamodel.

UXReactor's public material supports connecting user problems, broader experience context, cross-functional activity, and design decisions. Meridian applies that principle by requiring every capability or feature to trace to a selected experience and problem—not merely to a desired release.[source](source-index.md#src-uxreactor-5d) [source](source-index.md#src-uxreactor-redseal)

GOV.UK’s whole-problem and multidisciplinary-team standards reinforce that a coherent experience may depend on policy, operations, assisted service, content, and technology beyond one interface or department.[source](source-index.md#src-gov-whole) [source](source-index.md#src-gov-multi)

The UK Government Teal Book’s requirements guidance emphasizes traceability from user needs through requirements and later validation, supporting explicit links and verification without collapsing capability, feature, and requirement into one artifact.[source](source-index.md#src-teal-traceability)

The capability categories, formulas, feature distinction, and Level 10/12 boundary below are this playbook’s synthesis.

## Reasoning formula

```text
ENABLING CAPABILITY
= selected concept and Critical Experience need
+ stable ability the ecosystem must possess
+ provider and consuming actors/systems/services
+ required quality, policy, ethical, and operational conditions
+ dependencies, current maturity, and gap
+ verification method and evidence status
+ upstream and downstream traceability
− specific screen, component, vendor, team, or predetermined implementation

JUSTIFIED FEATURE
= required capability
+ selected concept and priority scenario
+ concrete actor-facing or backstage behavior/mechanism
+ scope and quality constraints
+ rationale for why this manifestation is appropriate
+ verification and release status
− strategic claim or outcome assumption

CAPABILITY MAP
= many-to-many links among experiences, concepts, capabilities, features,
  owners, dependencies, quality conditions, and evidence
```

## What belongs

- Human, service, operational, policy, data, content, model, technical, and cross-cutting abilities.
- The Critical Experiences, concepts, and scenarios each capability enables.
- Capability provider, consumer, accountable owner, and collaborating roles.
- Current and required maturity, gaps, dependencies, and sequence.
- Security, privacy, accessibility, inclusion, safety, reliability, performance, explainability, auditability, and governance qualities where relevant.
- Reusable or shared capabilities that support several experiences.
- Concrete actor-facing and backstage features or mechanisms justified by the concept.
- Buy/build/partner or manual/automated choices when evidenced.
- Verification method, status, residual risk, and traceability.
- Deliberate exclusions and deferred capabilities.

## What does not belong

- A feature backlog relabeled as capabilities.
- Screens, pages, buttons, components, APIs, databases, models, or vendors stated as the ability itself.
- “AI capability,” “search capability,” or “notification capability” without actor purpose, ability, quality, and scope.
- A department’s charter or current ownership boundary used to define the experience.
- Detailed interaction sequence, navigation, state logic, or interface behavior.
- Low-level functional or non-functional requirements and acceptance tests.
- Features included only because competitors have them or stakeholders requested them.
- Infrastructure work with no articulated experience or risk relationship.
- Capability availability treated as proof of usability, adoption, or human outcome.
- A release plan presented as a capability map.

## Adjacent-level boundaries

**Above — Level 10, Solution Concepts:** The concept is the coherent candidate approach: for example, **progressively steer a generated direction through lightweight feedback**. Level 11 decomposes the selected concept into abilities such as capture intent, generate a direction, preserve session context, interpret feedback, explain behavior, and recover—plus the features chosen to realize them.

**Below — Level 12, Interaction Architecture:** Level 11 establishes which abilities and mechanisms must exist. Level 12 defines how actors and the system cooperate through information, actions, states, rules, navigation, feedback, and recovery. “Preserve progress” is a capability; the save/resume state model and its user-system interaction belong at Level 12.

**Requirement boundary:** A capability is an ability; a feature is a manifestation; a requirement is a verifiable statement of needed behavior or quality. Requirements can emerge here but should be resolved, specified, and verified through Levels 12–15 rather than used to replace the experience chain.

## Required evidence

A credible Capability-to-Experience Map and feature set require:

- a selected Solution Concept, Critical Experiences, and priority scenarios;
- evidence of what the concept requires from people, service, policy, data, content, operations, and technology;
- existing architecture, process, service, data, security, policy, accessibility, and operational evidence;
- input from the disciplines accountable for feasibility and risk;
- current capability maturity and gap evidence rather than assumed availability;
- explicit quality conditions and a verification approach;
- rationale linking every proposed feature to one or more capabilities and experiences;
- documented dependencies, owners, sequencing, exclusions, and residual risk; and
- traceability into interaction models, requirements, tests, release scope, and live evidence.

A released behavior can demonstrate that some mechanism existed in that release. It does not by itself prove the intended capability quality, historical rationale, scenario coverage, or human impact.

## Permitted reconstruction

**Permitted:**

- reconstruct implemented capabilities from dated architecture, requirements, process, interface, API, data, QA, and release evidence;
- infer a minimum ability that necessarily existed when multiple artifacts independently show its behavior;
- build a retrospective capability-to-experience map while labeling the map as current synthesis;
- distinguish intended, designed, implemented, released, and operationally verified capability states;
- use confirmed recollection to clarify ownership, manual operations, constraints, or cross-team dependencies; and
- use external technical or regulatory research to explain possible constraints without claiming they drove the historical decision.

**Not permitted:**

- infer why a capability or feature was selected solely from the final implementation;
- claim an undocumented capability strategy, reuse intention, maturity assessment, or buy/build decision;
- equate an available API, model, database, component, or team with a usable capability;
- infer experience success from capability availability or feature release;
- omit manual work, policy, operations, or service dependencies to make the product appear self-sufficient;
- convert every shipped feature into a strategically justified feature after the fact; or
- claim ownership of engineering, architecture, product, policy, or operational decisions not actually held.

When evidence shows **what existed** but not **why**, preserve that distinction explicitly.

## Claim, lifecycle, and ownership controls

- **Component availability:** Capability identification, capability rationale, maturity, feature mapping, and verification may each be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable.
- **Provenance:** Classify ability, provider/owner, dependencies, required quality, current maturity, feature rationale, and verification separately.
- **Lifecycle:** A capability may be **needed, candidate, assessed, planned, partially available, available, verified, constrained, deprecated, or retired**. A feature may be **proposed, designed, validated, implemented, released, adopted, or measured**. Do not use the feature lifecycle as a proxy for capability fitness or experience success.
- **Ownership:** Use “I mapped,” “I identified the experience need,” “I specified interaction requirements,” “I facilitated dependency alignment,” “engineering determined,” “operations provided,” or “we agreed” according to evidence. Separate design influence from budget, architecture, product, and implementation authority.

## Writing grammar

**Capability formula**

> **To enable [Critical Experience] across [priority scenarios], the [product-service ecosystem / named provider] must be able to [stable ability] for [actor or consumer], while meeting [quality, policy, accessibility, ethical, and operational conditions]. It depends on [dependencies]; current maturity is [evidenced state]; fitness will be verified by [method].**

**Feature formula**

> **Provide [concrete behavior or mechanism] so [actor/system] can use [capability] within [selected concept and scenario]. This manifestation is justified by [evidence/rationale], constrained by [scope/quality], and is currently [lifecycle state].**

**Illustrative application**

```text
Capability — Steer and recover
To enable moment-based discovery across low-attention and ambiguous-intent
scenarios, the service must let the listener correct a generated direction without
losing useful context, while preserving agency, responsiveness, accessibility, and
privacy. It depends on interpretable feedback, session state, and recommendation
adaptation; fitness remains a testable claim.

Possible features — Lightweight preference signals, undo, reset direction, and an
explanation-and-adjustment control. Each is a candidate manifestation, not the
experience itself.
```

This is an illustrative capability model, not a claim about Spotify’s internal architecture or roadmap.

## Canonical output and traceability

The canonical output is a **Capability-to-Experience Map and Justified Feature Set** containing:

- scope, version, owners, contributors, and terminology legend;
- selected concept, Critical Experiences, and scenario coverage;
- capability statements grouped by human, service, operational, policy, data, content, model, technical, and cross-cutting type;
- provider, consumer, current maturity, required maturity, quality conditions, and gaps;
- dependencies, sequencing, risk, constraints, and accountable owners;
- actor-facing and backstage features/mechanisms mapped to capabilities;
- feature rationale, alternatives, exclusions, and lifecycle status;
- verification method and evidence status for every material capability;
- unresolved requirements and residual risks; and
- traceability upstream to Levels 0–10 and downstream to interaction architecture, interface, validation, implementation, release scope, observed use, and outcomes.

The map should support both directions: a team can start from a feature and find the capability, concept, scenario, Critical Experience, and strategy it serves; or start from a Critical Experience and find every human, service, policy, data, operational, and technical dependency needed to enable it.

## Quality audit

**Pass when:**

- each capability is a stable ability rather than a component or team;
- every capability and feature traces to an experience, concept, and scenario;
- actor-facing and backstage dependencies are represented together;
- quality, maturity, verification, ownership, and gaps are explicit;
- shared capabilities expose cross-experience leverage without redefining the experiences;
- features are justified manifestations rather than strategic starting points; and
- implementation availability is separated from experience and outcome evidence.

**Fail when:**

- the capability map is a system diagram or feature inventory with new labels;
- features dictate the experience formulation;
- organizational ownership fragments a cross-boundary episode;
- manual, policy, operational, content, or data work disappears behind the interface;
- generic terms such as “AI capability” conceal the required ability and quality;
- released is treated as verified, adopted, or successful; or
- ownership and rationale are reconstructed from implementation alone.

**Experience-first leadership signal:** The designer keeps capabilities and features subordinate to meaningful human experiences, convenes the disciplines required to make the whole system work, and preserves traceability from strategic intent through backstage enablement to released and measured outcomes.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [The Open Group, ArchiMate® 3.2 Specification, Strategy Layer definition of Capability; official standard published 2022.](source-index.md#src-archimate-capability) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [UXReactor, "5-D Framework for Experience Strategy, User Research, and Experience Design."](source-index.md#src-uxreactor-5d) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [UXReactor, "Beyond the Legacy: How a Former Cybersecurity Leader Pivoted to the Cloud Through User-Centered Design."](source-index.md#src-uxreactor-redseal) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [GOV.UK Service Manual, “2. Solve a Whole Problem for Users.”](source-index.md#src-gov-whole) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “6. Have a multidisciplinary team.”](source-index.md#src-gov-multi) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [UK Government Project Delivery Function, The Teal Book, “Chapter 31: User Needs and Requirements.”](source-index.md#src-teal-traceability) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
