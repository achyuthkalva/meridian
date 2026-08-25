# Level 13 — Interface Definition and Prototyping

Use this Level Guide to classify, formulate, and audit **Interface Definition and Prototyping** without leaking adjacent decisions into it.

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

Interface design, detailed design, prototyping, design systems, and visual/content design are established disciplines. This playbook pairs **Interface Definition** and **Prototyping** because the interface expresses the Interaction Architecture while prototypes make selected assumptions experienceable and testable. A prototype is an evidence instrument, not proof, a release state, or a required fidelity milestone.

## Definition

**Interface Definition** is the medium- and platform-specific expression of the Interaction Architecture through perceivable information, content, controls, components, composition, states, transitions, responsive behavior, accessibility semantics, and visual form.

**Prototyping** is the deliberate construction of a partial representation of a concept, interaction, interface, or service experience at the fidelity necessary to answer declared questions before or during implementation.

Together, this level makes the intended experience sufficiently concrete to:

- perceive and act through;
- inspect across states and contexts;
- evaluate with relevant people and disciplines;
- communicate behavior and quality;
- discover gaps in the architecture; and
- prepare an evidence-backed implementation definition.

Fidelity is multidimensional. Visual realism, data realism, interaction realism, content realism, technical realism, breadth, and environmental realism can differ. Higher visual fidelity does not mean higher validity or greater completeness.

## Governing question

> **How should the Interaction Architecture be expressed through content, controls, composition, states, accessibility behavior, and visual form—and what representation is sufficient to test the most important unresolved experience assumptions?**

## Strategic job

This level makes abstract behavior tangible without allowing polish to close inquiry prematurely. It:

- expresses the conceptual and state model in a perceivable, operable interface;
- integrates interaction, content, visual, motion, and accessibility design;
- reuses and extends appropriate patterns and design-system components;
- resolves information hierarchy, control affordance, feedback, density, and responsive behavior;
- represents loading, empty, error, permission, timeout, interruption, and recovery states;
- uses realistic content and data to expose comprehension and edge-case problems;
- selects prototype fidelity according to the question and risk;
- supports user research, accessibility evaluation, engineering feasibility, content review, and stakeholder understanding;
- records what the prototype does and does not simulate; and
- produces a versioned interface definition that can be validated and implementation-defined at Level 14.

## Unit of analysis and scope

There are two connected units:

1. **Interface-definition unit:** one coherent surface, flow segment, state family, or cross-surface pattern expressed for declared platforms, viewports, inputs, content conditions, and actor roles.
2. **Prototype unit:** one versioned representation constructed to answer one or more explicit questions across a defined scenario set and fidelity profile.

Declare:

- the parent Interaction Architecture and scenarios;
- platforms, channels, viewports, devices, input modes, and assistive-technology assumptions;
- design-system version and pattern sources;
- content and data realism;
- states, variants, permissions, roles, errors, and recovery covered;
- visual, interaction, data, content, service, and technical fidelity;
- what is functional, simulated, omitted, or intentionally false;
- the research, accessibility, feasibility, or communication questions;
- version, decision status, and change history; and
- relevant NDA, privacy, and test-data controls.

A prototype may represent a single risky transition, an end-to-end scenario, a backstage service enactment, or a production-like experience. Scope should follow the learning question, not an assumption that every prototype must look like the finished product.

## Expert and source anchors

GOV.UK describes prototypes ranging from quick paper sketches to interactive code and advises selecting the form that best meets the current need; more realistic code prototypes can be more appropriate for user research.[source](source-index.md#src-gov-prototypes) This supports question-led fidelity rather than a universal low-to-high sequence.

UXReactor's public framework connects strategy, research, and experience design. Meridian applies that connection by requiring fidelity choices, key-scenario testing, design rationale, and traceability from problems and outcomes through interface definition.[source](source-index.md#src-uxreactor-5d)

UXReactor's public Tekion case study illustrates the organizational role of a design-driven culture. Meridian applies this through explicit foundations, components, patterns, states, responsive changes, role-based behavior, workflows, prototypes, and interaction notes.[source](source-index.md#src-uxreactor-tekion)

W3C’s WCAG 2.2 resources establish testable accessibility success criteria, while the ARIA Authoring Practices Guide provides roles, states, properties, keyboard behavior, and functional examples for common web patterns.[source](source-index.md#src-w3c-wcag22) [source](source-index.md#src-w3c-aria-apg) These sources make accessibility a behavioral design input; they do not make a prototype conformant merely because it visually resembles an accessible pattern.

ISO 9241-210 supports producing and evaluating design solutions iteratively against context and requirements.[source](source-index.md#src-iso-hcd) The exact pairing, fidelity model, and Level 12/14 boundaries below are this playbook’s synthesis.

## Reasoning formula

```text
INTERFACE DEFINITION
= Interaction Architecture
+ platform, medium, viewport, device, and input context
+ information and visual hierarchy
+ content, labels, instructions, and feedback language
+ controls, components, patterns, and affordances
+ default, loading, zero, one, many, error, permission, and recovery states
+ responsive, adaptive, cross-device, and role-based behavior
+ accessibility semantics, focus, keyboard, reading order, alternatives, and motion behavior
+ realistic content and data conditions
+ design-system relationship, rationale, and traceability
− decorative polish without behavioral completeness

PROTOTYPE
= declared question or risk
+ priority scenario and participants or reviewers
+ minimum sufficient fidelity across relevant dimensions
+ explicit functional, simulated, omitted, and false behavior
+ version, test conditions, and evidence plan
− assumption that realism equals validity
```

## What belongs

- Page, screen, view, voice, conversational, spatial, or service-touchpoint composition.
- Information hierarchy, density, grouping, emphasis, and progressive disclosure.
- Content design: labels, instructions, prompts, explanations, confirmations, errors, and recovery language.
- Controls, components, patterns, affordances, and interaction cues.
- Default, hover, focus, selected, disabled, loading, empty, partial, success, warning, error, permission, offline, timeout, and recovery states as applicable.
- Responsive, adaptive, orientation, zoom, device, and input-mode behavior.
- Role-, permission-, locale-, language-, and data-dependent variants.
- Visual foundations, typography, color, iconography, imagery, spacing, grids, and motion where meaningful.
- Accessibility semantics, reading order, focus order, keyboard behavior, non-pointer access, contrast, text alternatives, announcements, timing, and reduced-motion behavior.
- Realistic data and content, including long, missing, ambiguous, sensitive, and erroneous cases.
- Prototype purpose, fidelity profile, limitations, version, scenario coverage, and research instrumentation.
- Design rationale and links to the interaction model and evidence.

## What does not belong

- A polished happy path treated as the complete experience.
- Visual styling that contradicts unresolved interaction logic.
- Placeholder copy or idealized data in a prototype meant to test comprehension or edge cases.
- A component gallery without its experience context and behavior.
- Every conceivable screen when a smaller prototype can answer the question.
- A click-through whose transitions hide missing rules and states.
- High fidelity presented as validation, approval, feasibility, or implementation readiness.
- Accessibility represented only through a contrast score.
- Automated accessibility checks presented as proof of accessibility.
- A design-system component assumed appropriate without scenario evidence.
- Engineering specifications, acceptance criteria, production instrumentation, or release status.
- Retrospective rationale invented from the final screen.

## Adjacent-level boundaries

**Above — Level 12, Interaction Architecture:** Level 12 defines objects, actions, information relationships, states, rules, initiative, feedback, and recovery. Level 13 decides how those behaviors become perceivable and operable on particular surfaces. If a screen reveals a missing state or incoherent object model, return to Level 12 rather than conceal it with layout.

**Below — Level 14, Validation and Implementation Definition:** Level 13 creates the interface and representations used to investigate it. Level 14 evaluates declared claims with appropriate people and methods, then converts the sufficiently resolved design into shared, verifiable implementation definition. A tested prototype produces scoped evidence; it does not automatically make the full interface “validated.”

**Production boundary:** A coded prototype may reuse production technology, and a design-system example may be functional, but neither is a released service unless it is integrated, quality-assured, operated, and made available to the intended population under Level 15 controls.

## Required evidence

A credible Interface Definition and prototype require:

- approved or clearly provisional Interaction Architecture;
- Critical Experience and scenario coverage;
- evidence-based content, vocabulary, mental-model, and information-hierarchy decisions;
- applicable brand, design-system, platform, content, accessibility, legal, policy, privacy, and security standards;
- realistic data ranges, roles, permissions, content conditions, and errors;
- documented responsive, input, device, locale, and assistive-technology requirements;
- rationale for new or modified components and patterns;
- a declared prototype question and fidelity profile;
- technical and operational input for behavior the prototype simulates;
- versioning, change history, scope, and known omissions; and
- traceability from every consequential interface state to interaction logic, requirements, evaluation evidence, and later QA.

Aesthetic judgment is legitimate design expertise, but claims about comprehension, usability, accessibility, preference, or outcome require appropriate evidence beyond the designer’s judgment.

## Permitted reconstruction

**Permitted:**

- reconstruct interface-definition sets from dated Figma files, screenshots, prototypes, design-system libraries, annotations, exports, requirements, review comments, and released interfaces;
- identify state and responsive coverage visible across multiple design artifacts;
- infer that an artifact functioned as a prototype when its interactive behavior and purpose are documented;
- describe a prototype’s apparent fidelity and scope from the artifact itself;
- use confirmed recollection to clarify review purpose, iteration rationale, test data, or omitted behavior;
- distinguish designed states from implemented states using QA evidence; and
- create an NDA-safe abstraction of structure and behavior while labeling transformed visuals and omitted details.

**Not permitted:**

- claim a prototype was tested, validated, approved, or used for engineering when evidence shows only that it was created;
- infer user reactions, comprehension, accessibility, or preference from visual quality;
- invent iterations, alternatives, critiques, or design rationales;
- treat a Figma frame modification date as proof of decision sequence;
- claim a design-system component was reused or created without artifact evidence;
- erase missing, contradictory, or placeholder states;
- present NDA-transformed visuals as the original delivered interface; or
- attribute visual, content, interaction, or system decisions solely to one person without evidence.

## Claim, lifecycle, and ownership controls

- **Component availability:** Interface Definition, prototype existence, prototype purpose, evaluation use, and design-system relationship may each be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable.
- **Provenance:** Classify layout, content, visual system, component behavior, state coverage, responsive rules, accessibility behavior, prototype fidelity, and rationale separately.
- **Lifecycle:** An interface may be **sketched, explored, resolved provisionally, prototyped, reviewed, revised, selected, implementation-defined, implemented, verified, released, or superseded**. A prototype may be **planned, built, used in evaluation, revised, discarded, or archived**. “High fidelity” is a representation property, not a lifecycle status.
- **Ownership:** Use “I designed,” “I wrote,” “I prototyped,” “I facilitated critique,” “I extended the system,” “we selected,” or “the design system provided” according to evidence. Separate direct craft, direction, review authority, and delegated execution.

## Writing grammar

**Interface-definition formula**

> **Express [interaction model/state] for [actor, platform, and context] through [information hierarchy + content + controls/patterns], including [state and variant coverage]. Preserve [experience qualities] through [accessibility, responsive, feedback, and recovery behavior]. Reuse or extend [design-system source] because [rationale].**

**Prototype formula**

> **To learn whether [declared assumption/question] holds in [scenario], create a prototype with [fidelity profile and functional scope]. It simulates [behavior], omits [behavior], and must not be used to claim [limitation]. Evidence will come from [method at Level 14].**

**Illustrative application**

```text
Interface definition — Express the proposed listening direction as an inspectable
session with clear start, steering, pause, and reset controls. Represent initial,
generating, playable, poor-fit, corrected, offline, and interrupted states; preserve
keyboard, screen-reader, reduced-motion, and low-attention use.

Prototype — Build a realistic end-to-end interaction for two ambiguous-intent
scenarios to test whether people understand the proposed direction and can cheaply
correct it. Recommendation quality is simulated, so the prototype cannot establish
model feasibility or live recommendation value.
```

This is an illustrative interface and prototype definition, not a claim about Spotify’s internal design work.

## Canonical output and traceability

The canonical output is an **Interface Definition Set and Prototype Record** containing:

- scope, version, owners, contributors, status, platform, and design-system version;
- parent Interaction Architecture, Critical Experiences, scenarios, and requirements;
- page, screen, surface, or touchpoint compositions;
- component and pattern usage, variants, states, and rationale;
- content model, final or provisional copy, data conditions, and localization rules;
- visual foundations, responsive behavior, motion, and asset specifications;
- accessibility semantics, focus and keyboard behavior, reading order, announcements, alternatives, timing, and zoom/reflow behavior;
- role, permission, device, channel, offline, loading, empty, error, and recovery coverage;
- prototype purpose, questions, fidelity profile, functional scope, simulation, omissions, test data, and version;
- design review decisions, unresolved issues, and change history;
- evidence and rationale links; and
- traceability upstream to Levels 0–12 and downstream to validation claims, implementation requirements, acceptance tests, design QA, release scope, instrumentation, and live outcomes.

## Quality audit

**Pass when:**

- the interface faithfully expresses the complete relevant Interaction Architecture;
- realistic content, data, roles, states, exceptions, and recovery are represented;
- visual, content, interaction, and accessibility decisions work as one system;
- reused and new patterns have explicit rationale;
- prototype fidelity is tied to a declared question and limitation;
- high fidelity never substitutes for evidence; and
- engineering and research can identify what is resolved, provisional, simulated, and omitted.

**Fail when:**

- polish hides missing states or rules;
- only the ideal path and ideal data exist;
- the prototype question is “Do users like it?” rather than a decision-relevant uncertainty;
- realism is mistaken for validity or implementation readiness;
- accessibility is reduced to annotations or automated scores;
- design-system consistency overrides scenario fit; or
- untested, approved, implemented, and released are treated as synonyms.

**Experience-first leadership signal:** The designer connects high craft to system intent, makes consequential states and accessibility behavior tangible, and uses prototypes to learn rather than to sell an assumed solution.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [GOV.UK Service Manual, “Making Prototypes.”](source-index.md#src-gov-prototypes) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [UXReactor, "5-D Framework for Experience Strategy, User Research, and Experience Design."](source-index.md#src-uxreactor-5d) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [UXReactor, "UXReactor and Tekion Collaborate, Nurturing a Design-Driven Culture for Early Adoption Dominance."](source-index.md#src-uxreactor-tekion) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [W3C Web Accessibility Initiative, “How to Meet WCAG 2.2 (Quick Reference).”](source-index.md#src-w3c-wcag22) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [W3C Web Accessibility Initiative, “ARIA Authoring Practices Guide.”](source-index.md#src-w3c-aria-apg) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [International Organization for Standardization, ISO 9241-210:2019, “Ergonomics of Human-System Interaction — Part 210: Human-Centred Design for Interactive Systems.”](source-index.md#src-iso-hcd) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
