# Level 15 — Delivery, Live Experience, and Outcome Learning

Use this Level Guide to classify, formulate, and audit **Delivery, Live Experience, and Outcome Learning** without leaking adjacent decisions into it.

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

**Playbook-synthesized closure-and-renewal level; source-grounded lifecycle practice.**

Delivery, quality assurance, design QA, release, service operation, monitoring, live research, and outcome evaluation are established practices owned across disciplines. This playbook combines them at Level 15 to prevent release from being mistaken for success and to reconnect live evidence to the entire experience-first chain.

## Definition

Delivery, Live Experience, and Outcome Learning is the multidisciplinary work of:

1. **realizing** the accepted implementation definition in a production-capable system;
2. **verifying** the implemented configuration against requirements and design intent;
3. **releasing and operating** it safely, accessibly, reliably, securely, and sustainably;
4. **observing** what people actually experience across the wider service;
5. **measuring** intended and unintended human and organizational effects; and
6. **learning** whether evidence supports contribution to the Strategic UX Outcome and what should change upstream.

The output is not merely shipped software. It is a **live, governed experience plus a bounded evidence record about what was released, how it behaves, what people encounter, and what outcomes can and cannot be claimed**.

Engineering is not introduced at this level. Engineering, product, research, design, content, data, accessibility, security, policy, operations, support, QA, and domain expertise should already have influenced upstream decisions. Level 15 is where implementation and operation become dominant—not where responsibility for the experience transfers to one department.

## Governing question

> **What exactly was implemented and released, does the live product-service system deliver the intended experience safely and reliably across real conditions, what human and organizational change is actually evidenced, and what must the team revisit?**

## Strategic job

This level closes the strategy-to-delivery chain without closing learning. It:

- protects the accepted experience intent through implementation and change;
- verifies behavior, content, accessibility, and quality against the implementation definition;
- compares designed and engineered experiences through progressive design QA;
- manages rollout, migration, support, monitoring, rollback, and experience debt;
- establishes the exact release scope and exposed population;
- observes real contexts, workarounds, breakdowns, exceptions, and unintended effects;
- combines product analytics, service data, support evidence, research, operational evidence, and outcome measures;
- separates technical health, feature use, task performance, experience quality, human outcome, and business outcome;
- distinguishes correlation, plausible contribution, and causal attribution;
- monitors distributional effects, accessibility, exclusion, safety, privacy, bias, and harms;
- creates decision-ready learning for iteration; and
- sends evidence back to Current Experience, Opportunity, Strategic UX Outcome, Experience Strategy, Product Strategy, priorities, and Critical Experiences.

## Unit of analysis and scope

There are four connected units:

1. **Delivery configuration:** one versioned build or service change, environment, release scope, and implementation baseline.
2. **Live experience:** one actor/cohort + real context and scenario + actual interaction across relevant product, service, support, and offline conditions.
3. **Outcome claim:** one defined indicator or qualitative change + baseline + observation period + population + comparison or counterfactual logic + confidence and attribution status.
4. **Learning decision:** one evidence-backed decision to retain, fix, roll back, extend, investigate, or revisit an upstream level.

Declare:

- build/release version, environment, date, client/state/market, modules, cohorts, channels, and feature flags;
- designed, implemented, excluded, deferred, and changed scope;
- verification, QA, design-QA, accessibility, security, privacy, performance, reliability, and operational status;
- rollout, migration, support, rollback, and incident arrangements;
- instrumentation availability, consent, data quality, segmentation, and baseline status;
- live-research actors, contexts, methods, and limitations;
- intended and unintended outcome indicators;
- observation timeframe and comparison logic;
- contribution or causal-attribution method; and
- decision, owner, residual risk, experience debt, and upstream destination.

A release can be live for one client, state, cohort, module, or feature flag while other parts remain in development. Never convert partial scope into “the platform launched” without qualification.

## Expert and source anchors

UXReactor's public framework reinforces a connected approach to strategy, research, design, and execution. Meridian applies that connection through design-quality checks across scenarios, journeys, workflows, components, patterns, behavior, severity, and frequency, with unresolved differences tracked visibly with product and engineering.[source](source-index.md#src-uxreactor-5d)

NASA’s verification/validation distinction supports checking implemented conformance separately from intended-use fitness.[source](source-index.md#src-nasa-vv-distinction) At Level 15, production configuration can be verified; live experience and outcome still require their own evidence.

GOV.UK requires teams to define success metrics, track whether a service solves its intended problem, and use performance data to improve it.[source](source-index.md#src-gov-success-data) Its metrics guidance starts with service purpose and user needs, develops explicit hypotheses, plans measurement while building, combines metrics with user research, and uses multiple data sources with context.[source](source-index.md#src-gov-service-metrics)

GOV.UK’s current reliability standard requires appropriate monitoring, proportionate response, and monitoring of user outcomes and ethical issues such as bias—not only technical faults.[source](source-index.md#src-gov-reliable-service) Its live-phase guidance treats operation as sustainable support plus continuing research, accessibility testing, QA, and improvement across the whole user journey.[source](source-index.md#src-gov-live-phase) [source](source-index.md#src-gov-research-live)

Jared Spool’s outcome-driven UX metrics work focuses measurement on changes in people’s actual experiences and lives rather than product use alone.[source](source-index.md#src-spool-outcome-metrics) The Magenta Book’s contribution-analysis guidance reinforces that a plausible contribution claim is not the same as causal attribution.[source](source-index.md#src-magenta-contribution)

The exact combined level, formulas, status vocabulary, and feedback loop below are this playbook’s synthesis.

## Reasoning formula

```text
DELIVERY RECORD
= exact implementation definition and build configuration
+ implemented, changed, excluded, and deferred scope
+ functional and design verification
+ accessibility, security, privacy, performance, reliability, safety, and quality evidence
+ rollout, migration, support, monitoring, rollback, and experience-debt controls
+ instrumentation and data-governance readiness
+ owners, approvals, residual risk, and release status

LIVE EXPERIENCE EVIDENCE
= actor or cohort
+ real context and Critical Experience scenario
+ actual behavior across product, service, support, and offline touchpoints
+ success, interpretation, effort, confidence, failure, abandonment, and recovery evidence
+ accessibility, inclusion, distributional, safety, privacy, bias, and unintended effects
+ data source, timeframe, segment, limitations, and confidence

OUTCOME CLAIM
= Strategic UX Outcome and indicator definition
+ baseline and target status
+ observed qualitative or quantitative change
+ population, timeframe, segmentation, and data quality
+ alternative explanations and organizational/context change
+ correlation, contribution, or causal-attribution status
+ intended and unintended effects
− shipment, adoption, or task completion presented as life improvement

LEARNING DECISION
= delivery + live experience + outcome evidence
+ residual uncertainty and risk
+ retain, repair, roll back, extend, investigate, or revisit decision
+ owner, trigger, and upstream level affected
```

## What belongs

- Exact release, module, client, cohort, channel, flag, environment, and date scope.
- Production architecture and implementation status relevant to the experience.
- Functional QA, exploratory QA, design QA, content QA, accessibility verification, and requirements traceability.
- Security, privacy, safety, performance, reliability, resilience, capacity, and incident readiness.
- Data migration, interoperability, operational procedure, policy, training, support, and service readiness.
- Rollout, experiment, feature-flag, rollback, and retirement logic.
- Known deviations, accepted risk, unresolved defects, and experience debt.
- Instrumentation, event definitions, consent, data minimization, data quality, and segment definitions.
- Live analytics, operational data, support contacts, complaints, research, observation, and accessibility evidence.
- Task, experience, human-outcome, business-outcome, and ecosystem indicators kept distinct.
- Baselines, targets, observation windows, comparison logic, uncertainty, and alternative explanations.
- Distributional effects, exclusion, bias, harm, workarounds, and unintended consequences.
- Correlation, contribution, and causal-attribution status.
- Decisions, owners, review triggers, and upstream learning links.

## What does not belong

- “Shipped” or “live” with no scope, date, population, or module qualification.
- Design approval presented as production release.
- Passing engineering QA presented as design fidelity, usability, accessibility, or outcome evidence.
- Design QA presented as user validation.
- Feature adoption presented as human value without a defensible link.
- A target, projected saving, or planned KPI presented as achieved impact.
- Anecdotal praise generalized to all users.
- No complaints presented as evidence of success.
- Dashboard movement with no metric definition, baseline, segment, timeframe, or data-quality assessment.
- Correlation described as causation.
- A release that omits failed, excluded, assisted, or offline experiences from monitoring.
- Automated accessibility testing as the sole accessibility evidence.
- Experience debt silently converted into deliberate non-scope.
- Technical monitoring used as a substitute for live user research.

## Adjacent-level boundaries

**Above — Level 14, Validation and Implementation Definition:** Level 14 states what evidence supports about a proposed design and defines what should be built and verified. Level 15 records what was actually built, checks conformance, operates it, and observes the live experience and outcomes. A Level 14 target or usability result remains pre-release evidence.

**Feedback loop — Levels 0–13:** Level 15 has no lower abstraction level. Its downstream evidence becomes upstream input. Live behavior updates Current Experience; unexplained breakdowns update the Opportunity Space; outcome evidence challenges the Strategic UX Outcome and causal logic; changing context can revise Experience and Product Strategy; repeated issues can alter priorities, Critical Experiences, scenarios, concepts, capabilities, architecture, or interface.

**Verification boundary:** Functional QA asks whether software behaves as specified. Design QA asks whether the engineered experience preserves accepted design intent. Accessibility conformance asks whether applicable standards are met. Live research asks what people actually experience. Outcome evaluation asks what changed and why. None replaces the others.

## Required evidence

A credible Level 15 record requires evidence proportionate to each claim:

- deployment, release-note, client, module, environment, configuration, or operational evidence for release status;
- requirements-linked functional and non-functional verification;
- design-to-build comparison across priority scenarios and consequential states;
- accessibility evaluation combining automation, manual checks, assistive technologies, and disabled-user research as appropriate;[source](source-index.md#src-gov-accessibility-testing) [source](source-index.md#src-w3c-accessibility-evaluation)
- security, privacy, performance, reliability, safety, data, operations, migration, support, and rollback readiness;
- instrumentation tested for correctness, consent, minimization, and segment integrity;
- baseline and target definitions established before or explicitly reconstructed after release;
- multiple live evidence sources appropriate to the outcome, including research and service data rather than analytics alone;
- observation over a timeframe capable of capturing the claimed change;
- context, segments, adoption/exposure, organizational changes, external events, and alternative explanations;
- explicit contribution or causal-attribution method where impact language is used;
- unintended effects and distributional outcomes; and
- decision records showing how evidence changes the experience or strategy.

The absence of measured metrics does not eliminate all credible outcome language. It limits the claim to documented release, observed behavior, qualitative evidence, stakeholder acceptance, or intended effect—each labeled accurately.

## Permitted reconstruction

**Permitted:**

- confirm release scope from deployment records, client/state references, release notes, production URLs, screenshots, tickets, approvals, support records, or corroborated stakeholder evidence;
- reconstruct implemented behavior and deviations from production builds, QA logs, defect records, design comparisons, and release artifacts;
- report qualitative outcomes from attributable stakeholder or user feedback with source, context, and scope;
- describe design authority in final QA when approval responsibility is documented;
- reconstruct candidate baselines or measurement plans for future learning while labeling them retrospective and unmeasured;
- combine external context with project evidence to explain plausible constraints without attributing historical reasoning;
- make a bounded contribution argument when timing, mechanism, evidence, and alternatives support it; and
- state that outcome evidence is unavailable even when the product was successfully released.

**Not permitted:**

- invent launch dates, clients, modules, user counts, adoption, efficiencies, savings, satisfaction, defect reduction, or outcome metrics;
- turn stakeholder praise, approval, or awards into population-level user impact;
- infer reduced effort, error, training, support, or processing time solely from a simplified design;
- claim causal impact because a metric changed after release;
- treat expected, targeted, modeled, projected, observed, and measured outcomes as equivalent;
- call the entire product live when only selected modules or clients were released;
- attribute implementation or outcome solely to design in multidisciplinary work;
- hide post-release failures, rollback, debt, accessibility gaps, or excluded populations; or
- use present-day production behavior to rewrite what was released historically.

## Claim, lifecycle, and ownership controls

- **Component availability:** Delivery status, implementation fidelity, operational quality, live-experience evidence, and outcome evidence may each be Evidenced, Partially evidenced, Reconstructed, Unknown, or Not applicable.
- **Provenance:** Classify every release field, QA result, production behavior, qualitative observation, metric, baseline, target, contribution claim, and attribution claim separately.
- **Lifecycle — delivery:** Use **in development, code complete, in QA, design-QA approved, release candidate, partially released, released, rolled back, replaced, or retired** only with evidence.
- **Lifecycle — evidence:** Use **instrumentation planned, instrumented, data collected, qualitatively observed, quantitatively measured, contribution supported, or causally attributed** according to method. “Released” never describes an outcome.
- **Lifecycle — debt:** Use **identified, triaged, must-fix, accepted temporarily, scheduled, resolved, reverified, or retired** with owner and scope.
- **Ownership:** Distinguish “I conducted design QA,” “I approved design fidelity,” “I supported engineering,” “I defined instrumentation,” “we released,” “operations monitored,” and “research/evaluation found.” Separate design authority from release authority, implementation, operations, and impact attribution.

## Writing grammar

**Release formula**

> **[Version/module] was [implementation/release state] for [client/cohort/channel] on [evidenced date or period]. The released scope included [items] and excluded or deferred [items]. Verification covered [types]; known deviations and debt were [status].**

**Live-evidence formula**

> **Across [actors, contexts, segments, and period], [data/research source] showed [observed behavior or condition]. This indicates [bounded interpretation], while [limitations, non-users, and alternative explanations] remain.**

**Outcome formula**

> **Relative to [baseline or comparison], [indicator] changed from [value/status] to [value/status] for [population and period]. Evidence [shows correlation / supports contribution / supports causal attribution] because [method and mechanism]. It does not establish [boundary].**

**No-metric formula**

> **The evidence confirms [release, approval, observed behavior, or qualitative response]. The design was intended to [targeted human effect], but no reliable measurement is available to claim that effect occurred.**

**Illustrative application**

```text
Release — The progressive-steering experience was released to a defined cohort with
explicit-intent, generating, playback, steering, reset, offline, and recovery states.
Design QA verified the accepted interaction and interface states; two lower-severity
content deviations remained tracked as experience debt.

Outcome — Instrumentation and live research would need to show whether exposed listeners
reach fitting audio with less effort and recover more successfully than the baseline.
A rise in steering-control use alone would show feature use, not improvement in the
listener’s life or causal impact.
```

This is an illustrative release-and-measurement grammar, not a claim about Spotify deployment or results.

## Canonical output and traceability

The canonical output is a **Delivery, Live Experience, and Outcome Learning Record** containing:

- release identity, configuration, environment, date, client/cohort/channel, flags, modules, owners, and status;
- accepted implementation definition and exact implemented, changed, excluded, and deferred scope;
- functional QA, exploratory QA, design QA, content QA, accessibility, security, privacy, performance, reliability, safety, and operational evidence;
- defects, deviations, severity, priority, experience debt, acceptance, rollback, and resolution status;
- rollout, migration, training, support, monitoring, incident, continuity, and retirement plans;
- instrumentation specification, validation, consent, data governance, baselines, targets, segments, and observation windows;
- live analytics, service data, support evidence, user research, accessibility evidence, and operational observation;
- task, experience, human, business, ecosystem, unintended, and distributional outcomes kept distinct;
- metric definitions, data quality, comparison logic, alternative explanations, and correlation/contribution/causal status;
- qualitative evidence with speaker, context, date, and scope;
- decisions to retain, fix, roll back, extend, investigate, or revisit;
- owners, triggers, residual risk, and next evidence need; and
- bidirectional traceability to every upstream level and to the exact release and evidence sources.

The learning loop is explicit:

```text
Released configuration
        ↓
Observed live experience and service behavior
        ↓
Human, organizational, and unintended outcome evidence
        ↓
Bounded interpretation and decision
        ↓
Update Current Experience, Opportunity, outcomes, strategy,
priorities, Critical Experiences, scenarios, or downstream design
```

## Quality audit

**Pass when:**

- release scope and status are exact;
- the built experience is verified against behavior and intent, not only pixels;
- accessibility, reliability, security, privacy, operations, and support are experience conditions;
- live research and metrics cover real contexts and relevant populations;
- technical health, use, task success, experience quality, human outcome, and business outcome remain distinct;
- targets and results, qualitative and quantitative evidence, and correlation and causation are separated;
- experience debt and unintended effects are visible;
- every impact statement has proportionate evidence and attribution language; and
- learning visibly changes an upstream decision or evidence need.

**Fail when:**

- shipping is the outcome;
- design QA or stakeholder approval is described as user impact;
- metrics lack baseline, definition, population, timeframe, or context;
- adoption is treated as value;
- automation replaces human accessibility and experience evidence;
- only successful or digitally included users are measured;
- a multidisciplinary release becomes an individual impact claim;
- debt, deviations, or harms disappear from the story; or
- learning produces another feature backlog without revisiting the experience chain.

**Experience-first leadership signal:** The designer remains accountable to the lived experience after delivery, protects intent through implementation, makes evidence and attribution boundaries visible, and turns live learning into strategic change rather than retrospective celebration.

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [UXReactor, "5-D Framework for Experience Strategy, User Research, and Experience Design."](source-index.md#src-uxreactor-5d) | Experience-first operating practice synthesized from the approved UXReactor sources. |
| [NASA, “2.4 Distinctions Between Product Verification and Product Validation.”](source-index.md#src-nasa-vv-distinction) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “10. Define What Success Looks Like and Publish Performance Data.”](source-index.md#src-gov-success-data) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “How to Set Performance Metrics for Your Service.”](source-index.md#src-gov-service-metrics) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “14. Operate a Reliable Service.”](source-index.md#src-gov-reliable-service) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “How the Live Phase Works.”](source-index.md#src-gov-live-phase) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “User Research in Live.”](source-index.md#src-gov-research-live) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [Jared M. Spool, “What Are Outcome-Driven UX Metrics?” Center Centre, 13 May 2025.](source-index.md#src-spool-outcome-metrics) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [HM Treasury and UK Evaluation Task Force, The Magenta Book, “Annex A: Analytical Methods for Use Within an Evaluation,” section on contribution analysis.](source-index.md#src-magenta-contribution) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
| [GOV.UK Service Manual, “Testing for Accessibility.”](source-index.md#src-gov-accessibility-testing) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [W3C Web Accessibility Initiative, “Evaluating Web Accessibility Overview.”](source-index.md#src-w3c-accessibility-evaluation) | Human-centred quality, accessibility, traceability, verification, validation, and evaluation. |
