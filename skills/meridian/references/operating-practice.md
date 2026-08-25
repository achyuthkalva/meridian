# Operating Practice — Turn Experience Strategy into Shared Product Work

This guide turns Meridian's hierarchy into practical collaboration, decision, and leadership habits. Use it when product, design, engineering, research, operations, or leadership need to carry one experience definition from discovery through live learning.

## Progressive convergence replaces the old handoff model

### Replace “handoff” with progressive convergence

The classic model is:

```text
Product decides requirements
        ↓
Design creates screens
        ↓
Engineering receives handoff
        ↓
Build
```

Experience-first product development should look more like:

```text
Research / Design / Product / Engineering
share the problem and experience context
        ↓
Product + Design shape strategy and experience priorities
with technical and business reality visible
        ↓
Product Trio / multidisciplinary team
explores scenarios and solution concepts
        ↓
Design increases interaction resolution
while engineering increases technical resolution
        ↓
The team validates assumptions together
        ↓
Implementation becomes dominant
        ↓
Released experience is measured together
```

Teresa Torres’s handoff critique is useful here: when PM, design, and engineering work from different fragments of context, each transition can distort the original problem.[source](source-index.md#src-torres-handoffs)

#### Engineering should enter before screen completion

Engineering contributes to:

- technical opportunities
- feasibility
- architecture
- latency and performance constraints
- data availability
- security/privacy
- platform conventions
- failure/recovery behavior
- cost
- implementation trade-offs

The design becomes better because engineering participates early.

#### Design should stay after implementation begins

Design contributes to:

- implementation decisions
- state behavior
- visual/interaction QA
- accessibility
- content behavior
- edge-case interpretation
- scope trade-offs
- outcome instrumentation

The product becomes better because design does not disappear at handoff.

---

### What is actually handed to engineering?

There can still be an implementation-ready package, but it should be understood as **shared product definition**, not the moment engineering first learns the problem.

A strong package can include:

#### Why

- strategic UX outcome
- relevant experience vision
- relevant experience-roadmap priority
- critical experience
- scenario(s)

#### What behavior

- validated scenario and journey
- task flow
- interaction architecture
- state model
- information architecture

#### Interface definition

- screens
- components
- design-system references
- responsive rules
- motion/transition behavior
- content rules
- accessibility

#### System definition

- data requirements
- service dependencies
- permissions
- errors
- edge cases
- analytics events

#### Quality definition

- acceptance criteria
- UX outcome measures
- usability thresholds where appropriate
- QA scenarios

The artifacts maintain **traceability from the implementation back to the experience**.

---

## Operating rules keep the experience line intact

### Rules for an experience-first culture

#### Rule 1 — Start above your product

Study the person’s purpose before studying the interface.

#### Rule 2 — Research the current experience, not only product usage

Include other tools, people, workarounds, offline steps, and before/after moments.

#### Rule 3 — Separate opportunity from solution

Do not let a feature request masquerade as a problem statement.

#### Rule 4 — Define the human change before the future product

Use a Strategic UX Outcome to specify whose life should improve and how.

#### Rule 5 — Let the Experience Vision constrain the roadmap

A roadmap item should have a visible relationship to the desired future experience.

#### Rule 6 — Make Experience Strategy a set of choices

Diagnosis, guiding policy, and coherent actions are stronger than generic design values.

#### Rule 7 — Let Product Strategy choose the problems, not prescribe every solution

Strategy requires focus and explicit non-choices.

#### Rule 8 — Express Experience Roadmap and Priorities in actor-specific experience language

Prioritize the experiences that should improve, not the features presumed to improve them. Make the horizon, rationale, dependencies, and deliberate non-priorities visible.

#### Rule 9 — Treat critical experiences as the primary human-value decomposition

Organize thinking around what people need to achieve, not around the navigation tree or service architecture.

#### Rule 10 — Use scenarios to force context into design

A scenario should make visible why, what, and how the product must support the person.

#### Rule 11 — Generate several solutions for the same opportunity

Do not confuse your first idea with the requirement.

#### Rule 12 — Introduce features only as enabling mechanisms

Every feature should be able to answer:

> Which experience does this enable, and which outcome does that experience serve?

#### Rule 13 — Define the interaction architecture before polishing interfaces

Behavior, states, hierarchy, recovery, and control matter more than mockup completeness.

#### Rule 14 — Bring engineering into discovery

Feasibility is a design input, not a post-design rejection step.

#### Rule 15 — Learn from the live experience, not just adoption of the output

Feature usage is not proof of human improvement.

---

## Decision tools expose category errors before delivery

### The experience traceability test

For any proposed feature, ask the chain backward:

```text
FEATURE
What mechanism are we proposing?
        ↑
CRITICAL EXPERIENCE
What meaningful experience does it enable?
        ↑
EXPERIENCE-ROADMAP PRIORITY
Why should that actor-specific experience receive attention now?
        ↑
PRODUCT / EXPERIENCE STRATEGY
Why are we choosing this problem and this experience stance?
        ↑
EXPERIENCE VISION
What future experience does it move us toward?
        ↑
STRATEGIC UX OUTCOME
Whose life becomes better, and how?
        ↑
HUMAN PURPOSE
What was the person trying to accomplish in the first place?
```

If the chain breaks, the proposal may be an orphaned feature.

---

### The “feature disguised as experience” test

Ask five questions:

1. Could this experience exist if our current product disappeared?
2. Could several different solutions enable it?
3. Does the statement describe value to a person rather than functionality?
4. Does it have a recognizable start and outcome?
5. Can multiple capabilities cooperate to deliver it?

If the answers are mostly no, the statement is probably a feature, surface, or capability.

---

### The strategy test

A useful Experience Strategy should contain:

```text
Diagnosis
What is the decisive challenge?

Guiding Policy
What stance are we taking?

Coherent Actions
What experience decisions reinforce that stance?
```

If it contains only aspirations such as:

- delightful
- intuitive
- seamless
- personalized
- simple

it is probably not yet a strategy.

---

### The roadmap test

For each roadmap item:

1. Which experience portfolio priority does it serve?
2. Which experience-strategy choice and product-strategy bet justify that priority?
3. Which critical experience does it improve?
4. Which scenario demonstrates the need?
5. Which Strategic UX Outcome should move if it works?
6. How does it move the organization toward the Experience Vision?

A roadmap can still contain infrastructure, compliance, reliability, or technical-debt work. Experience-first does not mean pretending those obligations do not exist. It means making their relationship to the delivered experience visible whenever possible.

---

## The experience-first mindset changes what designers lead

### “Do not think in features; think in experiences”

The deepest interpretation is **not**:

```text
Search feature
      ↓ rename
Search experience
```

That is only vocabulary change.

The deeper shift is:

> **Decompose the product according to human value before decomposing it according to software architecture.**

Engineering may reasonably see:

```text
Authentication
Search
Recommendations
Playlists
Profiles
Payments
Notifications
```

Experience-first design may see:

```text
Find something right for this moment.
Discover something I did not know I would love.
Return effortlessly to something I care about.
Build a musical world that feels like mine.
Connect with another person through music.
Recover when the system misunderstands me.
```

Both views are legitimate.

They answer different questions.

#### Software architecture asks

> **What systems and capabilities must exist?**

#### Experience architecture asks

> **What meaningful human outcomes must the system make possible?**

The product becomes coherent when the two architectures are intentionally mapped to one another.

---

### Why “smaller than a product, bigger than a feature” is powerful

The phrase describes a valuable middle layer that many organizations accidentally skip.

Without that layer, teams jump from:

```text
High-level strategy
      ↓
Feature roadmap
```

The missing bridge is:

```text
High-level strategy
      ↓
Desired future experience
      ↓
Critical experiences
      ↓
Scenarios
      ↓
Possible solutions
      ↓
Features
```

That middle layer preserves human meaning while strategy becomes concrete.

It allows a strategic designer to ask:

- What should the person experience?
- In what context?
- What makes that experience successful?
- Which parts of the ecosystem must cooperate?
- What could we build to enable it?

Only then does the team decide what feature form is justified.

---

### The role of the UX designer in this culture

The UX designer is not simply the person at Levels 12–14 who creates flows and screens.

The designer’s contribution can span the hierarchy:

#### Strategic resolution

- synthesize research
- identify experience tensions
- define UX outcomes
- help articulate experience vision
- shape experience strategy
- influence product and experience priorities

#### Experience resolution

- frame critical experiences
- create scenarios
- model journeys
- explore concepts
- evaluate solution alternatives

#### Interaction resolution

- architecture
- flows
- state models
- content hierarchy
- interaction behavior
- prototypes
- accessibility
- detailed screens

#### Delivery resolution

- collaborate with engineering
- resolve implementation trade-offs
- perform design QA
- define experience instrumentation
- observe production outcomes

The craft does not change identity as it moves downward. **Its resolution changes.**

At the top, the designer asks:

> What should become different in this person’s life?

At the bottom, the designer asks:

> What happens when this request fails, the network is slow, the recommendation is wrong, and the person wants to recover without losing context?

Both are experience design.

---

## A compact reference keeps the hierarchy usable

### The hierarchy in one table

| Level | Layer | Primary question | Primary output |
| :---| :---| :---| :---|
| 0 | Human Purpose in Context | What purpose is the person pursuing, independent of our product? | Human-purpose-in-context frame |
| 1 | Current Experience | How does this happen today? | Current-state journey / ecosystem |
| 2 | Problem and Opportunity Space | What evidence-backed needs, frictions, desires, risks, and leverage points exist? | Evidence-backed opportunity structure |
| 3 | Strategic UX Outcome | Whose lived experience should improve, and in what observable way? | Human-centered outcome statement and indicators |
| 4 | Experience Vision | What could that person’s future lived experience become? | Future-state experience narrative |
| 5 | Experience Strategy | What experience choices will move us from the present toward that vision? | Diagnosis + guiding policy + coherent experience actions |
| 6 | Product Strategy | Which important problems or bets merit product investment? | Strategic problem bets and non-choices |
| 7 | Experience Roadmap and Priorities | Which actor-specific experience areas should receive attention now, next, and later? | Prioritized experience areas, horizons, and sequencing rationale |
| 8 | Critical Experience | Within a priority area, what bounded, consequential experience must work? | Critical Experience Definition |
| 9 | Scenarios and Journeys | For whom, when, under what conditions, and through what sequence does it occur? | Context-rich scenarios and journeys |
| 10 | Solution Concepts | What different approaches could work? | Alternative concepts + assumptions |
| 11 | Enabling Capabilities and Features | What product, service, and technical mechanisms are required? | Capability map and justified feature set |
| 12 | Interaction Architecture | How should people and the system cooperate across information, actions, states, and rules? | IA, task flows, state/permission model, and interaction rules |
| 13 | Interface Definition and Prototyping | How is the interaction architecture expressed and explored at interface resolution? | Interface definitions and testable prototypes |
| 14 | Validation and Implementation Definition | Does it create the intended experience, and is its behavior unambiguous? | Evidence-backed design decisions and shared implementation definition |
| 15 | Delivery, Live Experience, and Outcome Learning | What happens in real operation, and does it improve the experience as intended? | Released system, live experience evidence, and learning decisions |

---

### Five sentences to remember

> **Experience Vision:** What better future should people experience?

> **Experience Strategy:** What choices will move the experience toward that future?

> **Product Strategy:** Which important problems will the product invest in solving to create value and move toward that future?

> **Experience Roadmap and Priorities:** Which actor-specific experiences deserve attention now, next, and later—and why?

> **Critical Experience:** What meaningful, bounded human experience must the product make possible?

And then:

> **Features are mechanisms. Screens are representations. The experience is what happens to the person.**

---

## The final mental model returns learning to the person

### Final mental model

```text
DO NOT START HERE

Feature idea
   ↓
Requirements
   ↓
Screen
   ↓
Engineering

────────────────────────────────────────

START HERE

Human purpose
   ↓
Current experience
   ↓
Problem / opportunity
   ↓
Desired human outcome
   ↓
Experience vision
   ↓
Experience + product strategy
   ↓
Experience roadmap and priorities
   ↓
Critical experiences
   ↓
Scenarios and journeys
   ↓
Multiple solution concepts
   ↓
Enabling capabilities and features
   ↓
Interaction architecture
   ↓
Interface definition and prototypes
   ↓
Bounded validation evidence and implementation definition
   ↓
Delivery
   ↓
Live experience and outcome learning
   ↓
Did the person’s life actually improve?
   ↺
```

The central discipline of an experience-first culture is maintaining that chain of meaning as abstraction collapses.

**A feature is something the organization builds. An experience is something a person goes through. Strategic design connects the two without losing sight of why the product exists.**

---

## Sources

| Source | Used here for |
| :--- | :--- |
| [Teresa Torres, “Discovery Hand-Offs Kill Momentum: Here’s What to Do Instead.”](source-index.md#src-torres-handoffs) | Opportunity space, continuous discovery, and collaborative decision-making. |
