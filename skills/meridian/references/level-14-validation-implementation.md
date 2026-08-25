# Level 14 — Validation and Implementation Definition

Use this Level Guide to classify, formulate, and audit **Validation and Implementation Definition** without leaking adjacent decisions into it.

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

**Two established activities paired through a playbook-synthesized convergence level.**

Validation and implementation definition are established concerns, but there is no universal UX level with this exact name. The pairing creates a controlled convergence point: the team first records what the evidence supports about the proposed experience, then defines the version that multidisciplinary delivery will attempt to realize and verify.

Validation is not stakeholder approval, and implementation definition is not a static-screen handoff.

## Definition

**Validation** is the evidence-based evaluation of whether a specified design version supports its intended use, Critical Experiences, and essential experience qualities for declared actors, scenarios, and environments—within explicit limitations. It can test the plausibility of the design’s outcome logic, but it does not establish that a live human outcome occurred.

**Implementation Definition** is the versioned, shared, testable description of the intended experience and system behavior that a multidisciplinary team will build, verify, instrument, and operate without having to reconstruct consequential design logic from disconnected screens.

This level distinguishes three questions:

1. **Design evaluation:** What does evidence from representative scenarios and people support or challenge?
2. **Validation:** Does the design appear fit for its intended purpose and environment within the tested scope?
3. **Implementation verification planning:** What observable requirements and checks will show whether the build conforms to the accepted design definition?

NASA’s systems-engineering distinction is useful here: verification shows compliance with requirements, while validation shows that the product accomplishes its intended purpose in its intended environment.[source](source-index.md#src-nasa-vv-distinction) This playbook adapts that distinction cautiously to experience design; it does not import NASA’s full engineering process as UX methodology.

## Governing question

> **What does the evidence support about this design’s fitness for the intended experience, for which actors and conditions—and is the accepted version defined completely enough to be implemented, verified, instrumented, and changed without losing its human intent?**

## Strategic job

This level prevents two common credibility failures: calling a design “validated” after weak evidence, and asking engineering to infer the product from polished screens. It:

- turns prototype or design evaluation into scoped, reviewable claims;
- tests the Critical Experience, scenario outcomes, essential qualities, and riskiest interaction assumptions;
- includes representative actors, accessibility needs, contexts, exceptions, and recovery;
- separates observation, interpretation, recommendation, decision, and residual uncertainty;
- distinguishes stakeholder alignment from user evidence;
- converts the accepted interaction and interface definition into verifiable behavioral, content, quality, data, analytics, and accessibility requirements;
- creates one shared source of truth across design, product, engineering, research, content, data, QA, operations, security, accessibility, policy, and domain roles;
- preserves decision history and traceability as implementation changes; and
- defines the evidence and instrumentation Level 15 will need to assess the live experience and outcome.

## Unit of analysis and scope

There are two linked units:

1. **Validation claim:** one design version + one intended-use claim or critical assumption + declared actors, scenarios, environments, method, evidence, criteria, and limitations.
2. **Implementation-definition package:** one accepted release or increment scope + the complete relevant experience, behavior, content, state, quality, data, instrumentation, and verification definition.

Declare for validation:

- research question or claim;
- design/prototype version;
- Critical Experience and scenarios;
- participant or evaluator characteristics and exclusions;
- environment, task framing, data, assistance, and method;
- criteria or decision rule;
- observations, interpretation, severity, confidence, and limitations; and
- resulting decision and residual questions.

Declare for implementation definition:

- release/increment scope and version;
- accepted and provisional design decisions;
- flows, states, rules, roles, content, accessibility, data, and quality behavior;
- dependencies, owners, constraints, feature flags, rollout assumptions, and unresolved risks;
- acceptance and verification methods; and
- instrumentation and live-outcome learning plan.

Validation should be as broad as the claim, not broader. A study of one citizen flow does not validate the internal portal, the whole service, or the Strategic UX Outcome.

## Expert and source anchors

NASA clearly separates verification against requirements from validation of intended purpose in the intended environment.[source](source-index.md#src-nasa-vv-distinction) The distinction helps this playbook prevent design conformance, usability evidence, and live human outcome from collapsing into one word.

GOV.UK’s moderated usability-testing guidance asks teams to agree research questions, relevant user types, and parts of the prototype or service before sessions and recruit actual or likely users.[source](source-index.md#src-gov-usability-testing) Its alpha and beta guidance extends research across end-to-end service interactions, disabled users, support roles, and production code with assistive technologies.[source](source-index.md#src-gov-research-alpha) [source](source-index.md#src-gov-research-beta)

W3C distinguishes standards conformance from evaluation with real people: accessibility tools cannot determine every accessibility aspect automatically, and user evaluation can reveal usability barriers that conformance checks alone do not.[source](source-index.md#src-w3c-accessibility-evaluation) [source](source-index.md#src-w3c-involving-users)

The UK Government Teal Book emphasizes traceability from user needs through requirements and validation.[source](source-index.md#src-teal-traceability) UXReactor's public material reinforces keeping strategy, research, design, and cross-functional execution connected; Meridian expresses that through scenario testing, interaction documentation, workflows, error cases, specifications, behavior, and experience-level rationale.[source](source-index.md#src-uxreactor-5d) [source](source-index.md#src-uxreactor-tekion)

Teresa Torres’s warning about discovery handoffs supports continuous product, design, and engineering participation rather than a late transfer of documents.[source](source-index.md#src-torres-handoffs) The exact paired level, claim formula, and implementation package below are this playbook’s synthesis.

## Reasoning formula

```text
VALIDATION CLAIM
= exact design or prototype version
+ intended-use claim or critical assumption
+ Critical Experience and scenario coverage
+ relevant participants/evaluators and environment
+ method, task framing, data, assistance, and criteria
+ observed behavior and direct evidence
+ interpretation, severity, confidence, and limitations
+ supported, partially supported, unsupported, or unresolved decision
− stakeholder approval, preference, or unbounded certainty

IMPLEMENTATION DEFINITION
= accepted Interaction Architecture and Interface Definition
+ release/increment scope and configuration baseline
+ flows, objects, actions, states, transitions, rules, and permissions
+ components, content, responsive, accessibility, and recovery behavior
+ data, service, API, model, operational, security, privacy, and policy dependencies
+ performance, reliability, safety, and other quality requirements
+ analytics events, outcome indicators, consent, and data governance
+ acceptance criteria, verification method, ownership, and decision history
+ provisional decisions, residual risk, and change control
− static screens, redlines, or annotations without behavioral context
```

## What belongs

- Exact design/prototype version and evaluated claims.
- Research questions, study design, participants, scenarios, environments, tasks, and data.
- Direct observations, errors, assistance, completion, interpretation, confidence, and recovery behavior.
- Qualitative and quantitative evidence appropriate to the question.
- Accessibility conformance evaluation and research with disabled people.
- Content comprehension, mental-model, trust, agency, safety, and failure evidence where relevant.
- Severity, recurrence within the study, uncertainty, limitations, and excluded populations.
- Supported, partially supported, unsupported, and unresolved assumptions.
- Design decisions, revisions, and residual risks.
- Complete flows, state models, business rules, permissions, content rules, component behavior, responsive behavior, accessibility requirements, errors, and recovery.
- Data, service, API, model, operations, security, privacy, policy, and technical dependencies.
- Analytics events, outcome measures, data minimization, consent, and interpretation plan.
- Acceptance criteria, verification method, owner, status, version, and traceability.

## What does not belong

- “Users loved it” without method, sample, evidence, or relevance.
- Stakeholder, client, product, engineering, or QA approval presented as user validation.
- Five participants presented as proof of population prevalence or live outcome.
- Task completion presented as proof of comprehension, trust, long-term value, or life improvement.
- WCAG annotations or an automated scan presented as complete accessibility validation.
- A design review or heuristic critique relabeled as user testing.
- A prototype limitation concealed from the claim.
- Static happy-path screens, redlines, and asset exports presented as implementation definition.
- “Same as design” acceptance criteria.
- Requirements with no scenario, rationale, owner, or verification method.
- Instrumentation added after release with no relationship to the Strategic UX Outcome.
- A signed-off package treated as immutable when implementation evidence changes.

## Adjacent-level boundaries

**Above — Level 13, Interface Definition and Prototyping:** Level 13 makes behavior tangible and creates representations. Level 14 evaluates explicit claims about those versions and records what must be built. A prototype can be reviewed without being validated; an interface can be implementation-defined with residual risks explicitly accepted.

**Below — Level 15, Delivery, Live Experience, and Outcome Learning:** Level 14 defines and evaluates the intended design before or during construction. Level 15 verifies the implemented configuration, manages rollout and operation, observes real use, and evaluates live outcomes. Pre-release usability evidence cannot prove post-release human impact, reliability at scale, or causal outcome.

**Iteration boundary:** This is not a one-time gate. Evaluation may send the team back to Levels 8–13; implementation questions may reveal architecture gaps; build evidence may require definition changes. The level marks a type of resolution, not a waterfall phase.

## Required evidence

A credible Validation and Implementation Definition record requires:

- traceable Critical Experiences, scenarios, intended-use claims, and essential qualities;
- exact versions and configuration of evaluated stimuli;
- research questions and methods appropriate to the claims;
- relevant participants, including disabled people and support roles where applicable;
- realistic environments, tasks, content, data, devices, and assistive technologies proportionate to the risk;
- raw or traceable observations and an analysis process;
- explicit criteria, limitations, uncertainty, contradictions, and negative evidence;
- cross-functional decision records and residual-risk ownership;
- reviewed interaction, interface, content, state, accessibility, data, policy, operational, security, and quality definitions;
- engineering and QA feasibility of verification methods;
- instrumentation definitions connected to the Strategic UX Outcome; and
- version control and bidirectional requirements traceability.

No single method establishes every claim. Combine behavioral evidence, accessibility evaluation, domain review, technical testing, content evaluation, and other methods according to the risk and intended use.

## Permitted reconstruction

**Permitted:**

- reconstruct a validation record from dated research plans, recordings, notes, findings, prototype versions, observation grids, revisions, and decision records;
- state the narrow claim supported by documented user or evaluator behavior even when no formal report exists;
- reconstruct an implementation-definition package from Figma annotations, design-system documentation, flows, state tables, user stories, acceptance criteria, tickets, API contracts, meeting notes, and QA evidence;
- distinguish what was explicit before development from what engineering or QA clarified later;
- use confirmed recollection to clarify research setup, decision ownership, verbal knowledge transfer, or implementation agreements;
- label stakeholder approval, expert review, engineering feasibility, user evaluation, and accessibility audit as different evidence types; and
- mark missing validation as Unknown rather than forcing completeness.

**Not permitted:**

- invent participants, sessions, tasks, observations, quotations, findings, metrics, accessibility audits, or revisions;
- infer validation from a prototype link, approval comment, release, adoption, or lack of complaints;
- convert internal QA into evidence that intended users could use the service;
- claim broad validation beyond the tested actors, scenarios, versions, and environments;
- reconstruct acceptance criteria from the shipped interface and present them as pre-build intent;
- erase unresolved implementation questions or accepted experience debt;
- claim that a knowledge-transfer meeting transferred complete understanding without evidence; or
- attribute implementation decisions or final approval solely to design when authority was shared.

## Claim, lifecycle, and ownership controls

- **Component availability:** Validation evidence and Implementation Definition may independently be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable.
- **Provenance:** Classify each claim, participant/context field, observation, interpretation, decision, requirement, and acceptance criterion separately. A directly observed behavior can still support only a limited interpretation.
- **Lifecycle:** A validation claim may be **untested, under evaluation, supported within scope, partially supported, unsupported, contradicted, or unresolved**. A design version may be **revised, accepted with conditions, or superseded**. An implementation definition may be **draft, reviewed, implementation-ready, changed during build, baselined, verified, or superseded**. Avoid the blanket phrase “validated design.”
- **Ownership:** Use “I planned,” “I moderated,” “I observed,” “I synthesized,” “I specified,” “I led knowledge transfer,” “we accepted,” or “QA/engineering verified” according to evidence. Separate research, design, decision, implementation, and approval authority.

## Writing grammar

**Validation-claim formula**

> **For [exact design version], we evaluated whether [actor] could [Critical Experience/intended use] in [scenario and environment] using [method and participant/evaluator scope]. Evidence showed [observation]. This [supports / partially supports / does not support] [bounded claim], with [limitations and uncertainty]. We therefore [decision], while [residual risk] remains.**

**Implementation-definition formula**

> **For [release/increment scope], implement [actor–system behavior] across [flows/states/roles], using [content/components/data/services] while meeting [accessibility and quality requirements]. Verify through [test/inspection/demonstration/analysis], instrument [events and indicators], and preserve traceability to [Critical Experience and outcome]. [Items] remain provisional or excluded.**

**Illustrative application**

```text
Validation claim — In a realistic prototype of two ambiguous-intent scenarios,
participants understood the proposed listening direction and most recovered from a
poor first fit without restarting. This supports the steering model for those tested
conditions; it does not establish recommendation quality, accessibility with production
code, sustained value, or population-level effect.

Implementation definition — Build explicit and inferred-intent entry, generating,
playable, poor-fit, corrected, paused, offline, and expired-session states. Preserve
keyboard and assistive-technology behavior, privacy consent, undo, and session recovery;
instrument direction offered, first play, steer, reset, abandon, and recovery events.
```

This is an illustrative validation and implementation record, not a claim about Spotify research or delivery.

## Canonical output and traceability

The canonical output is a **Validation Evidence Record and Implementation Definition Package** containing:

- exact versions, scope, owners, contributors, dates, and status;
- parent Critical Experiences, scenarios, architecture, interface, assumptions, and intended-use claims;
- research questions, methods, participants/evaluators, environment, tasks, data, and criteria;
- observations, evidence links, findings, severity, confidence, limitations, contradictions, and decisions;
- accessibility conformance and disabled-user evidence kept distinct;
- accepted, revised, rejected, provisional, and residual-risk decisions;
- complete flows, objects, actions, states, transitions, rules, roles, permissions, and exceptions;
- interface, component, content, responsive, localization, accessibility, and motion behavior;
- data, service, API, model, operations, security, privacy, policy, performance, reliability, and safety requirements;
- analytics events, outcome indicators, data governance, and measurement interpretation;
- acceptance criteria, verification method, test owner, and configuration baseline;
- implementation questions, change log, experience debt, and escalation path; and
- bidirectional traceability upstream to Levels 0–13 and downstream to build artifacts, verification, design QA, release, live research, and outcome evidence.

## Quality audit

**Pass when:**

- every validation statement is bound to a version, claim, actor, scenario, method, evidence, and limitation;
- negative and contradictory evidence remain visible;
- stakeholder approval, user evidence, accessibility conformance, and technical feasibility are distinct;
- the implementation package describes behavior, states, content, quality, and rationale—not just appearance;
- requirements have acceptance and verification methods;
- instrumentation is designed before release and traces to the Strategic UX Outcome;
- residual risks and provisional decisions have owners; and
- implementation can change without losing traceability or human intent.

**Fail when:**

- “validated” is an unbounded adjective;
- task success is generalized into trust, long-term value, or population effect;
- approval substitutes for research;
- accessibility rests on automation or annotations alone;
- static screens require engineering to reconstruct behavior;
- acceptance criteria repeat the design rather than define observable conditions;
- missing evidence is replaced by confidence; or
- the package behaves like a late handoff instead of shared product definition.

**Experience-first leadership signal:** The designer makes evidence boundaries explicit, turns uncertainty into decisions rather than theatre, and ensures that the build definition retains the human purpose, failure conditions, accessibility, and outcome logic behind every consequential requirement.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [NASA, “2.4 Distinctions Between Product Verification and Product Validation.”](source-index.md#src-nasa-vv-distinction) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Using Moderated Usability Testing.”](source-index.md#src-gov-usability-testing) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “User Research in Alpha.”](source-index.md#src-gov-research-alpha) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “User Research in Beta.”](source-index.md#src-gov-research-beta) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [W3C Web Accessibility Initiative, “Evaluating Web Accessibility Overview.”](source-index.md#src-w3c-accessibility-evaluation) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [W3C Web Accessibility Initiative, “Involving Users in Evaluating Web Accessibility.”](source-index.md#src-w3c-involving-users) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [UK Government Project Delivery Function, The Teal Book, “Chapter 31: User Needs and Requirements.”](source-index.md#src-teal-traceability) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [UXReactor, "5-D Framework for Experience Strategy, User Research, and Experience Design."](source-index.md#src-uxreactor-5d) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [UXReactor, "UXReactor and Tekion Collaborate, Nurturing a Design-Driven Culture for Early Adoption Dominance."](source-index.md#src-uxreactor-tekion) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [Teresa Torres, “Discovery Hand-Offs Kill Momentum: Here’s What to Do Instead.”](source-index.md#src-torres-handoffs) | Opportunity space, continuous discovery, and collaborative decision-making. |
