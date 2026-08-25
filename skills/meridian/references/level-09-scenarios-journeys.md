# Level 9 — Scenarios and Journeys

Use this Level Guide to classify, formulate, and audit **Scenarios and Journeys** without leaking adjacent decisions into it.

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

**Established practices; playbook-specific pairing and boundary.**

Scenarios, user journeys, journey maps, and experience maps are established design practices, but the terms are not used uniformly across the industry. This playbook pairs them at one level while preserving two different units: a **scenario** is a context-rich account of a particular attempt; a **journey** is a temporal model of what unfolds across that attempt or a coherent set of attempts.

## Definition

A **scenario** is an evidence-grounded or explicitly hypothetical account of a specific actor trying to achieve a meaningful result under particular circumstances, constraints, knowledge, stakes, and risks.

A **journey** is a time-ordered model of the experience across a declared scope, showing what the actor and relevant co-actors do, decide, encounter, interpret, feel where evidenced, and receive from systems or services—including breakdowns, handoffs, exceptions, and recovery.

Scenarios expose **variation and context**. Journeys expose **sequence, relationships, and change over time**. A scenario can exist as prose before it is mapped. A journey can compare several scenarios or represent one in depth. Neither artifact is inherently current-state or future-state; its mode must be declared.

## Governing question

> **Under which concrete circumstances must the Critical Experience work, and what happens over time across people, touchpoints, decisions, systems, failures, and recovery?**

## Strategic job

This level protects design from a context-free happy path. It:

- translates one Critical Experience into the range of real situations it must support;
- preserves actor goals, prior knowledge, constraints, stakes, and environments;
- reveals the temporal structure of current and intended experiences;
- exposes cross-channel, cross-role, frontstage, backstage, policy, and data dependencies;
- distinguishes common paths from rare but consequential exceptions;
- makes breakdown, waiting, transfer, abandonment, and recovery designable;
- creates evidence-based requirements and evaluation scenarios; and
- provides the conditions against which solution concepts can be generated and compared.

## Unit of analysis and scope

**Scenario unit:** one declared actor or coordinated actor relationship + one initiating situation + one purpose or result + a coherent set of contextual conditions and stakes.

**Journey unit:** one declared journey scope + one or more scenarios + chronological stages, events, decisions, touchpoints, actors, system/service responses, and experience evidence.

Declare for every artifact:

- current-state, future-state, evaluation, exception, or hybrid mode;
- actor and behavioral evidence;
- Critical Experience and scenario family;
- start and end boundary;
- level of resolution and time span;
- represented channels, systems, organizations, and co-actors;
- evidence versus hypothesis encoding; and
- important variations deliberately omitted.

Do not make one synthetic journey carry mutually incompatible contexts. If novice and expert behavior, accessible and inaccessible channels, routine and emergency situations, or citizen and caseworker responsibilities materially differ, represent separate scenarios and compare them.

## Expert and source anchors

Kim Goodwin treats scenarios as design-driving stories grounded in research and people’s goals, skills, context, and human characteristics. Her work uses scenarios to derive requirements and shape the interaction framework; she also distinguishes complete stories from fragmented user stories.[source](source-index.md#src-goodwin-scenarios) [source](source-index.md#src-goodwin-effective-scenarios)

Spool positions scenarios below the Experience Vision: they add the contextual detail needed for design before user stories connect that design context to development.[source](source-index.md#src-spool-stories)

ISO 9241-210’s human-centred design framing requires understanding and specifying context of use—including users, goals and tasks, resources, and environments—which supports scenario completeness without prescribing this playbook’s exact artifact.[source](source-index.md#src-iso-hcd)

GOV.UK defines experience maps as representations of what users do, think, and feel over time, from when they begin needing a service until they stop using it, and asks teams to research the current experience with participants rather than invent it.[source](source-index.md#src-gov-experience-map) [source](source-index.md#src-gov-current-experience-map)

UXReactor's public material reinforces connecting user-centered design to the broader product and service context before detailed interface work. Meridian therefore keeps scenarios concrete: outcomes, boundaries, activities, challenges, dependencies, and workflow variations must be explicit.[source](source-index.md#src-cioreview-uxreactor) [source](source-index.md#src-uxreactor-redseal)

The exact scenario/journey distinction, formulas, and evidence controls below are this playbook’s operational synthesis.

## Reasoning formula

```text
SCENARIO
= specific actor or coordinated actors
+ human purpose and parent Critical Experience
+ situation, trigger, and initiating state
+ prior knowledge, expectations, and available resources
+ physical, social, organizational, technical, and temporal context
+ constraints, stakes, concerns, and accessibility conditions
+ desired meaningful result
+ plausible failure and recovery conditions
+ evidence or explicit hypothesis status
− chosen interface sequence or assumed solution

JOURNEY
= declared current- or future-state scenario scope
+ chronological stages, actions, decisions, and transitions
+ touchpoints, channels, co-actors, and organizational handoffs
+ system, service, policy, data, and backstage responses
+ thoughts, interpretations, and feelings only where evidenced or marked hypothetical
+ waits, breakdowns, exceptions, abandonment, and recovery
+ evidence links, variation markers, and boundary
− generic lifecycle template or unsupported emotional curve
```

## What belongs

- Actor, purpose, scenario family, trigger, and intended result.
- Prior knowledge, expectations, mental models, and available resources.
- Physical, social, organizational, technical, temporal, and accessibility context.
- Stakes, constraints, concerns, dependencies, and risks.
- Current behavior, workarounds, artifacts, and non-digital activity.
- Journey stages, actions, decisions, transitions, and waiting.
- Touchpoints, channels, devices, organizations, and co-actors.
- Frontstage and relevant backstage responses.
- Breakdowns, exceptions, handoffs, abandonment, and recovery.
- Evidence-backed thoughts, interpretations, and feelings.
- Current/future mode, evidence/hypothesis state, frequency, and confidence where known.
- Requirements, questions, and concept-evaluation criteria that emerge from the scenarios.

## What does not belong

- A persona biography with no situated attempt.
- A generic user story such as “As a user, I want X”.
- A use case limited to actor-system transactions while ignoring lived context.
- A task flow that already assumes the selected interface.
- A feature walkthrough or list of screens.
- A generic funnel or lifecycle with no evidence from actual actors.
- An invented emotional curve, quote, frequency, or pain point.
- One idealized happy path presented as representative of everyone.
- A service blueprint pretending to be a user journey when only internal processes are shown.
- Detailed interface states, component specifications, or acceptance criteria.
- A future-state journey presented as observed current behavior.

## Adjacent-level boundaries

**Above — Level 8, Critical Experience:** Level 8 defines the invariant experience intent, boundary, essential qualities, and recovery obligation. Level 9 shows the different contexts and sequences in which it must hold. If changing the context changes the fundamental intended human result, the work may represent a different Critical Experience rather than another scenario.

**Below — Level 10, Solution Concepts:** Scenarios and current-state journeys describe actors, conditions, needs, breakdowns, and sequences without committing to a mechanism. Future-state scenarios may describe an intended experience, but should remain at a resolution that allows meaningfully different concepts. Level 10 proposes the coherent approaches that could enable those scenarios.

**Related artifacts:** A journey map emphasizes the actor’s experience over time. A service blueprint may add visible and backstage service delivery. A workflow or task flow resolves system cooperation more concretely and belongs primarily at Level 12. A user story is a delivery-oriented fragment and does not replace scenario context.

## Required evidence

A credible scenario set and journey model require:

- direct or well-corroborated evidence of the represented actors and situations;
- the parent Critical Experience and its boundaries;
- behavioral research, operational observation, analytics, logs, support records, requirements, or artifacts appropriate to each claim;
- evidence of context, constraints, knowledge, workarounds, and breakdowns;
- representation of relevant accessibility and assisted-service conditions;
- evidence for cross-role, channel, service, policy, and organizational relationships;
- explicit identification of current-state observations versus future-state hypotheses;
- sampling limitations, variation coverage, confidence, and unknowns; and
- traceability from each requirement or concept criterion back to scenario evidence.

Analytics can show sequence, frequency, and drop-off but usually not purpose or meaning. Interviews can reveal interpretation and intent but do not by themselves establish prevalence. Requirements can show intended behavior but not lived experience. Keep these evidentiary roles separate.

## Permitted reconstruction

**Permitted:**

- reconstruct an operational sequence from dated flows, requirements, logs, audit trails, support records, prototypes, QA evidence, and released behavior;
- combine corroborating artifacts to identify actors, handoffs, states, and exception paths;
- write a future-state scenario as an explicit design hypothesis grounded in a Critical Experience;
- use confirmed recollection to clarify decision points, verbal constraints, collaboration, or observed breakdowns;
- mark unresolved variants and ask targeted questions rather than force one synthetic path; and
- use domain research to explain external processes or obligations without attributing them to historical team discovery.

**Not permitted:**

- claim reconstructed journeys came from user research when they came from requirements or interfaces;
- invent feelings, quotes, goals, motivations, frequency, pain severity, or accessibility behavior;
- make the shipped interface the inevitable sequence and then call it a discovery artifact;
- erase unsupported, abandoned, or failed paths to make the story coherent;
- treat one actor’s recollection as representative of a population;
- convert a future-state storyboard into evidence of current experience; or
- claim the team used scenarios or journey mapping historically without evidence.

Use labels such as **Observed current-state**, **Artifact-reconstructed current-state**, **Proposed future-state**, and **Validated future-state**.

## Claim, lifecycle, and ownership controls

- **Component availability:** Scenario and journey artifacts may be independently Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable. A documented flow does not automatically prove a researched journey.
- **Provenance:** Classify actor, context, sequence, thought/feeling, frequency, failure, system response, and future-state proposition separately.
- **Lifecycle:** A scenario may be **candidate, research-grounded, reconstructed, selected for design, selected for evaluation, validated, superseded, or unresolved**. A journey may be **current-state observed, current-state reconstructed, future-state proposed, future-state tested, implemented, or observed after release**. Implementation does not validate the model’s human claims.
- **Ownership:** Distinguish “I researched,” “I synthesized,” “I facilitated mapping,” “I modeled,” “we validated,” and “the artifact record now supports reconstruction.” Name co-authors and operational experts where they materially shaped the model.

## Writing grammar

**Scenario formula**

> **[Actor], while [purpose and situation], encounters [trigger]. They know or expect [relevant knowledge], have [resources], and face [constraints, stakes, and risks]. They need to reach [meaningful result] while preserving [essential qualities]. The scenario succeeds when [observable completion or recovery condition].**

**Journey formula**

> **From [entry] to [exit], [actor] moves through [stages]. At each stage they [actions and decisions], encounter [touchpoints/co-actors], interpret [evidence-backed meaning], receive [system/service response], and may face [breakdown]. Recovery requires [condition].**

**Illustrative application**

```text
Scenario — A listener starts a short walk feeling mentally overloaded. They want
audio that settles the moment but cannot name an artist or genre. They have one
hand available, limited attention, and a recent history that may not reflect this
need. They need to reach something fitting quickly, understand how to redirect a
poor choice, and recover without restarting.

Journey scope — Need arises → intent is expressed or inferred → direction is
offered → listener samples and interprets it → listener accepts, steers, or
recovers → the session continues with context preserved.
```

This scenario is illustrative and hypothetical; it is not represented as Spotify user research.

## Canonical output and traceability

The canonical output is a **Scenario Set and Journey Model** containing:

- artifact mode, scope, version, owner, contributors, and provenance legend;
- parent Critical Experience and intended result;
- primary, secondary, edge, exception, recovery, and assisted scenarios;
- actor, trigger, context, knowledge, resources, constraints, stakes, and desired result for each;
- current-state and future-state journeys kept visibly distinct;
- stages, actions, decisions, touchpoints, actors, waits, and transitions;
- system, service, policy, data, and backstage relationships where relevant;
- thoughts and feelings with evidence links or hypothesis labels;
- breakdowns, abandonment, handoffs, exceptions, and recovery;
- variation coverage, frequency where known, confidence, unknowns, and exclusions;
- derived design requirements and concept-evaluation criteria; and
- traceability upstream to Level 8 and downstream to concepts, capabilities, interaction architecture, evaluation tasks, release behavior, and outcomes.

## Quality audit

**Pass when:**

- every scenario has a specific actor, situation, trigger, purpose, context, and result;
- relevant variations and exception paths are visible;
- the journey has a declared boundary and represents change over time;
- current observation and future proposition are unmistakably separated;
- emotions, quotations, and prevalence claims trace to evidence;
- channels, co-actors, systems, and organizational handoffs remain visible; and
- the artifacts reveal requirements without prematurely fixing the solution.

**Fail when:**

- the scenario is a persona paragraph, generic user story, or feature use case;
- the journey is a row of generic stages populated with assumptions;
- the current interface dictates every step before alternatives are explored;
- only the happy path is modeled;
- unsupported feelings or quotes manufacture empathy;
- one map hides incompatible actors or contexts; or
- the journey looks rigorous but cannot trace to evidence.

**Experience-first leadership signal:** The designer makes real variation, context, systems, and failure visible before the team converges, ensuring that downstream decisions serve people’s circumstances rather than an abstract “user” or idealized flow.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [Kim Goodwin / UIE, “Designing with Scenarios: Putting Personas to Work.”](source-index.md#src-goodwin-scenarios) | Scenarios, goal-directed design, and interaction frameworks. |
| [Kim Goodwin and Jared M. Spool / UIE, “Developing Effective Scenarios.” Recorded July 2011.](source-index.md#src-goodwin-effective-scenarios) | Scenarios, goal-directed design, and interaction frameworks. |
| [Jared M. Spool, “Promise, Vision, Scenario, and User Stories.”](source-index.md#src-spool-stories) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [International Organization for Standardization, ISO 9241-210:2019, “Ergonomics of Human-System Interaction — Part 210: Human-Centred Design for Interactive Systems.”](source-index.md#src-iso-hcd) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Creating an Experience Map.”](source-index.md#src-gov-experience-map) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GDS User Research, “Researching and Mapping Your Users’ Current Experience.” 17 June 2015.](source-index.md#src-gov-current-experience-map) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [CIOReview, "UXReactor: Experience Transformation to Thrive in a Digital World."](source-index.md#src-cioreview-uxreactor) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [UXReactor, "Beyond the Legacy: How a Former Cybersecurity Leader Pivoted to the Cloud Through User-Centered Design."](source-index.md#src-uxreactor-redseal) | Experience-first operating practice synthesized from the approved UXReactor sources. |
