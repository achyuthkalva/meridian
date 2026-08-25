# Level 8 — Critical Experience

Use this Level Guide to classify, formulate, and audit **Critical Experience** without leaking adjacent decisions into it.

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

**Playbook-synthesized operating level; source-grounded construction.**

“Critical Experience” is Meridian's label for a bounded experience unit. It is not presented as a standardized UX term or as the formal framework of any source. The construction draws on experience-first practice, Google SRE’s Critical User Journey concept, and whole-journey service-design practice.[source](source-index.md#src-cioreview-uxreactor) [source](source-index.md#src-google-cuj) [source](source-index.md#src-gov-whole-journey)

Google’s Critical User Journey is a useful adjacent concept: it identifies a sequence of tasks that is core to a user’s experience and essential to a service. This playbook deliberately uses **Critical Experience** more broadly. It begins with the meaningful human result and experience qualities; a task sequence is resolved later through scenarios, journeys, and interaction architecture.

## Definition

A Critical Experience is **one bounded, consequential episode in a specific actor’s pursuit of a human purpose that must work well for the Strategic UX Outcome and Experience Vision to become credible**.

It is:

- selected from an active Level 7 experience area;
- meaningful to the actor even when described without product architecture;
- bounded by an intelligible trigger, entry condition, meaningful result, and exit condition;
- large enough to require several coordinated capabilities, touchpoints, policies, or teams;
- small enough to generate concrete scenario variations and evidence; and
- solution-neutral enough that more than one concept could enable it.

The shorthand “smaller than the product, bigger than a feature” is useful but insufficient on its own. Size does not make an experience critical. **Consequence, strategic relevance, evidence, and the need for coordinated design do.**

## Governing question

> **Within a selected experience priority, what bounded and consequential experience must work—for whom, in what initiating context, toward what meaningful result, with which essential qualities and recovery conditions—for the intended human outcome to advance?**

## Strategic job

This level gives an experience-first culture a stable unit of strategic design. It:

- converts a broad experience-area priority into something teams can investigate and design;
- preserves the actor’s purpose and intended human result before mechanisms are chosen;
- creates a shared boundary across product, service, operations, policy, content, support, and engineering;
- makes essential qualities such as clarity, safety, agency, continuity, dignity, or trust explicit;
- defines what failure and recovery mean from the actor’s point of view;
- prevents departments or feature owners from fragmenting a consequential episode;
- supports meaningful experience-level evidence and indicators; and
- creates the direct parent for Level 9 scenarios and journeys.

## Unit of analysis and scope

The unit is **one actor-centered episode**, not an entire lifecycle, generic journey stage, product area, screen sequence, or capability.

Declare:

- the primary actor and any consequential co-actors;
- the Human Purpose and Level 7 experience area being advanced;
- the initiating situation or trigger;
- the entry boundary—when responsibility for this experience begins;
- the intended meaningful result;
- the exit boundary—when the actor can reasonably consider the episode complete, paused, transferred, or recovered;
- essential qualities that must hold across variations;
- material failure, exception, abandonment, and recovery conditions;
- channels, organizations, and systems the scope may cross; and
- known exclusions and adjacent experiences.

A Critical Experience can cross online and offline touchpoints and organizational boundaries. GOV.UK’s guidance is relevant here: a person’s wider journey may involve multiple transactions, back-end processes, evidence, and organizations even when delivery teams are separated.[source](source-index.md#src-gov-whole-journey)

## Expert and source anchors

UXReactor's public profile frames experience transformation as a broad organizational concern. Combined with journey practice, it supports Meridian's need for an experience unit above scenario variation.[source](source-index.md#src-cioreview-uxreactor) [source](source-index.md#src-gov-whole-journey)

Google SRE defines a Critical User Journey as a sequence of tasks that is core to a user’s experience and essential to the service, then argues that teams must identify what matters to the user before choosing service indicators.[source](source-index.md#src-google-cuj) This supports criticality, user-centered boundaries, and measurement—but its reliability-oriented CUJ definition is not copied as this level’s definition.

GOV.UK asks teams to solve whole problems and map how journeys cross touchpoints, back-end processes, evidence, and organizational boundaries.[source](source-index.md#src-gov-whole) [source](source-index.md#src-gov-whole-journey) This supports the rule that a Critical Experience must not be trimmed to the current team or interface boundary.

The exact definition, formula, fields, and Level 7/9 boundaries below are this playbook’s synthesis.

## Reasoning formula

```text
CRITICAL EXPERIENCE
= specific actor
+ human purpose and selected experience area
+ consequential initiating situation or trigger
+ explicit entry and exit boundary
+ meaningful intended human result
+ essential experience qualities
+ material failure, exception, and recovery conditions
+ evidence, uncertainty, and candidate indicators
+ upstream and downstream traceability
− feature, screen, channel, product component, or chosen solution

CRITICALITY
= consequence if the experience fails
+ importance to the actor's purpose
+ relationship to Strategic UX Outcome and Experience Vision
+ recurrence, reach, obligation, or risk where evidenced
+ need for coordinated cross-boundary design
− stakeholder volume or assumed business importance alone
```

No arithmetic threshold determines criticality. The rationale should expose human consequence, evidence strength, strategic relationship, and uncertainty rather than hide judgment behind an invented score.

## What belongs

- A specific actor or coordinated actor relationship.
- The human purpose and Level 7 priority the experience supports.
- A consequential situation or trigger.
- Entry, pause, transfer, completion, and exit boundaries.
- A meaningful actor result independent of a particular solution.
- Essential qualities such as confident, understandable, controllable, safe, respectful, or recoverable.
- High-level variation dimensions that Level 9 must cover.
- Failure, exception, abandonment, handoff, and recovery conditions.
- Cross-channel, service, operational, data, policy, and organizational scope.
- Evidence of importance and current breakdowns.
- Intended indicators with an honest baseline status.
- Assumptions, exclusions, confidence, ownership, and traceability.

## What does not belong

- “Search experience,” “checkout experience,” or “notification experience” when only a product function is named.
- A feature, epic, capability, component, screen group, or team boundary.
- A whole-product aspiration or distant future narrative; that belongs at Level 4.
- A broad investment theme or Now / Next / Later priority; that belongs at Level 7.
- One detailed circumstance or persona story; that belongs in a Level 9 scenario.
- A chronological journey or workflow.
- A selected solution mechanism or concept.
- Detailed functional requirements, business rules, IA, states, or interface behavior.
- A success metric stated as an achieved result before release evidence exists.
- Generic adjectives such as “seamless” or “delightful” without observable meaning.

## Adjacent-level boundaries

**Above — Level 7, Experience Roadmap and Priorities:** Level 7 selects and sequences broad actor-centered experience areas. Level 8 defines one bounded consequential experience within a selected area. For example, **moment-based discovery** may be a priority area; **find fitting audio for this moment without first knowing what to search for** is a Critical Experience.

**Below — Level 9, Scenarios and Journeys:** Level 8 defines what must remain true across relevant circumstances. Level 9 varies the actor’s context, trigger, knowledge, constraints, stakes, channels, and sequence. Several scenarios can instantiate one Critical Experience; a journey can model one or more of those scenarios over time.

**Cross-chain boundary:** Level 3 states the broader life improvement and Level 4 portrays its distant future. The Critical Experience is one nearer, bounded experience whose success contributes to them; it is not evidence that the outcome has already been achieved.

## Required evidence

A credible Critical Experience Definition requires:

- evidence that the actor and purpose are real;
- a selected Level 7 experience area and its prioritization rationale;
- Current Experience evidence showing the episode, breakdown, or unmet need;
- a defensible trigger and boundary based on what people actually encounter;
- evidence of the meaningful result and why it matters;
- evidence or explicitly marked hypotheses for essential qualities;
- known variations, exclusions, failure modes, and recovery needs;
- relevant business, policy, accessibility, safety, technical, service, and operational constraints;
- a trace to Strategic UX Outcome, Experience Vision, and Experience Strategy; and
- candidate indicators with baseline, target, observed result, and attribution status kept separate.

Direct research is strongest. Requirements, support logs, operational records, analytics, service blueprints, prototypes, QA records, and released behavior can corroborate parts of the definition, but each source proves different things.

## Permitted reconstruction

**Permitted:**

- reconstruct an episode’s boundary from dated flows, requirements, support records, prototypes, operational procedures, and implemented states;
- infer that multiple mechanisms cooperated when the released service visibly required them;
- translate a documented feature-centered scope into a present-day Critical Experience formulation, clearly labeled as retrospective synthesis;
- use confirmed recollection to clarify purpose, failure consequence, collaboration, or decision boundaries;
- use external research to establish domain obligations or common risks without claiming the team discovered them; and
- retain multiple candidate formulations when evidence does not identify one stable boundary.

**Not permitted:**

- claim the team explicitly defined a Critical Experience when no contemporaneous artifact or recollection supports that;
- infer human importance from implementation complexity or executive attention alone;
- treat a shipped feature as proof that the underlying experience succeeded;
- invent user language, emotional states, recurrence, reach, severity, or recovery needs;
- move boundaries to make the final solution look strategically complete;
- omit failures or actors the historical product did not support and call that exclusion intentional; or
- use today’s framework to imply that this exact reasoning preceded the design.

Retrospective wording should say **“The evidence supports framing the critical experience as…”**, not **“We defined the critical experience as…”**, unless that historical action is evidenced.

## Claim, lifecycle, and ownership controls

- **Component availability:** A Critical Experience may be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable. A feature name in the Evidence Hub does not automatically establish this level.
- **Provenance:** Classify actor, trigger, boundary, intended result, qualities, failure/recovery, criticality rationale, and indicators separately. One field can be Documented while another is Reconstructed or Unknown.
- **Lifecycle:** A Critical Experience may be **candidate, defined, prioritized, investigated, designed for, validated in prototype, supported in implementation, observed in use, or measured**. These states are not interchangeable. “Supported in the released product” does not mean “validated as successful.”
- **Ownership:** Use “I identified,” “I framed,” “I facilitated,” “I recommended,” “we agreed,” or “the evidence now supports framing” according to the record. Cross-functional delivery and decision authority must remain visible.

## Writing grammar

**Definition formula**

> **When [specific actor] encounters [consequential situation or trigger] while pursuing [human purpose], enable them to move from [evidenced starting condition] to [meaningful result] within [entry/exit boundary], while preserving [essential qualities] and enabling [failure/recovery condition]. This matters because [human consequence + strategic relationship].**

**Illustrative application**

```text
When a listener has a desired state but cannot name a song, artist, or genre,
enable them to move from vague intent to audio that feels fitting within one
discovery episode, while preserving agency, intelligibility, and cheap recovery
from a poor direction. This matters because repeated search formulation and
uncertain recommendations can prevent the listener from reaching the moment
they wanted music to support.
```

This is an illustrative experience-first formulation, not a claim about Spotify’s internal strategy or historical research.

## Canonical output and traceability

The canonical output is a **Critical Experience Definition** containing:

- identifier, version, scope, owner, contributors, and status;
- primary actor, relevant co-actors, and Human Purpose;
- parent Level 7 experience area and priority rationale;
- initiating context and trigger;
- entry, pause, transfer, completion, and exit boundaries;
- intended meaningful result;
- essential experience qualities and observable interpretations;
- variation dimensions to cover at Level 9;
- material failure, exception, abandonment, and recovery conditions;
- evidence ledger, confidence, assumptions, and unknowns;
- candidate indicators with baseline and measurement status;
- relevant accessibility, inclusion, safety, policy, and ethical conditions; and
- links upstream to Levels 0–7 and downstream to scenarios, journeys, concepts, capabilities, interaction architecture, validation, release, and outcomes.

Every downstream feature should be able to state which Critical Experience and scenario it enables. One Critical Experience may require many features; one capability may enable several Critical Experiences.

## Quality audit

**Pass when:**

- a person could recognize the experience without knowing the product structure;
- the actor, trigger, entry, exit, result, qualities, and recovery are explicit;
- the unit is consequential, bounded, and supported by evidence;
- the formulation remains open to multiple concepts;
- cross-channel and cross-organizational dependencies remain visible;
- scenario variations can be generated without redefining the experience; and
- traceability reaches both strategy and released outcome evidence.

**Fail when:**

- a feature or department has merely been renamed as an experience;
- the statement is too broad to bound or too narrow to require coordinated design;
- the desired result is a click, completion event, adoption metric, or business result with no human meaning;
- “seamless” substitutes for observable qualities;
- only the happy path is represented;
- criticality rests on assertion rather than consequence and evidence; or
- delivery, validation, and outcome claims are collapsed.

**Experience-first leadership signal:** The designer gives multidisciplinary teams a shared human episode to optimize, prevents feature and organizational boundaries from defining the problem, and carries human purpose, quality, recovery, and evidence into every downstream decision.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [CIOReview, "UXReactor: Experience Transformation to Thrive in a Digital World."](source-index.md#src-cioreview-uxreactor) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [Google, The Site Reliability Workbook, Chapter 2, “Implementing SLOs,” section “Modeling User Journeys.”](source-index.md#src-google-cuj) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Map and Understand a User’s Whole Problem.”](source-index.md#src-gov-whole-journey) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “2. Solve a Whole Problem for Users.”](source-index.md#src-gov-whole) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
