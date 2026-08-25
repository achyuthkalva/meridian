# Expert Foundations for Experience-First Strategy

This guide explains the research traditions Meridian brings together. It shows how human purpose, present evidence, strategic choices, experience priorities, design definition, delivery, and live learning form one traceable system.

## Meridian begins with the person, then carries that meaning into delivery

This playbook provides a working model for an **experience-first product culture**.

The central premise is simple:

> **Do not decompose a product first by features. Decompose it first by the meaningful experiences and human outcomes it must enable.**

Features still matter. Technology still matters. Product strategy still matters. Engineering constraints still matter. But none of them is the starting unit of thought.

The starting point is the person: what they are trying to accomplish in life or work, how they experience that today, where the experience breaks down, and how their future could become meaningfully better.

The model then progressively reduces abstraction until a multidisciplinary product team can design, validate, implement, and measure a real product experience.

This is a **synthesized operating model**, not a framework claimed by any single expert. It combines complementary ideas from Jared Spool / Center Centre, Indi Young, Kim Goodwin, Teresa Torres, Marty Cagan / SVPG, Atlassian design practitioners, GOV.UK service design, Satyam Kantamneni / UXReactor, and human-centred design, evaluation, and traceability standards.

Where terminology is not standardized, this guide states that explicitly.

---

## The foundational shift moves attention from product parts to human progress

The first move is conceptual: keep the product architecture, but stop using it as the main model of human value. The following contrast makes that shift concrete.

### Feature-first thinking vs. experience-first thinking

### Feature-first decomposition

A feature-first organization tends to decompose the product according to what the software contains:

```text
Product
├── Search
├── Recommendations
├── Playlists
├── Profile
├── Notifications
└── Payments
```

This structure is useful for architecture, ownership, delivery, and maintenance. The danger appears when the same structure becomes the **primary structure for understanding user value**.

A roadmap can then become a list of outputs:

```text
Improve Search
Build AI recommendations
Redesign playlists
Add notifications
Add social sharing
```

The user disappears behind the implementation.

### Experience-first decomposition

An experience-first organization asks a different question:

> **What meaningful things should become possible, easier, clearer, safer, more confident, or more valuable in the person’s life?**

For a music product, an experience-oriented decomposition could look like:

```text
Help me find something that fits this moment.
Help me discover something I did not know I would love.
Help me return effortlessly to something I care about.
Help me build a musical world that feels like mine.
Help me connect with another person through music.
```

Each of those experiences may require several features, surfaces, services, algorithms, data systems, policies, and teams.

Conversely, one technical capability can support several experiences.

That is the structural difference.

---

### What does “an experience” mean in this playbook?

The word **experience** is used at several levels in UX practice. Mixing them creates confusion.

#### Overall user experience

At the broadest level, user experience includes the person’s total relationship with a product, service, organization, or ecosystem — often including moments before and after direct interface use.

Jared Spool’s experience-vision work deliberately pushes teams beyond a narrow interface boundary. His early writing on experience vision argues that a strong vision can include moments outside the technology touchpoint and should focus on what people experience rather than on the technology itself. [source](source-index.md#src-spool-vision-steps)

GOV.UK makes a similar move at service level: teams are expected to understand users and their needs, solve a whole problem, and provide joined-up experiences rather than optimize an isolated page or departmental touchpoint. [source](source-index.md#src-gov-needs) [source](source-index.md#src-gov-whole)

#### A bounded or critical experience

This playbook also uses **an experience** as a practical decomposition unit inside a larger product or service.

Working definition:

> **A critical experience is a bounded, meaningful human outcome or episode that is larger than an individual feature but smaller than the total product or service.**

Examples:

- Find something appropriate for this moment.
- Understand whether I can afford this decision.
- Recover confidently when something goes wrong.
- Know what requires my attention right now.
- Continue work without reconstructing my previous context.

This exact label is a synthesis for this playbook; it should not be attributed to Jared Spool, Indi Young, Teresa Torres, or another expert as their formal term.

#### A simple test

A candidate experience is usually at the right level when:

1. **A person can describe it without knowing your product architecture.**
2. **It expresses an outcome or meaningful episode, not a UI control.**
3. **Several capabilities may cooperate to make it possible.**
4. **It is concrete enough to generate scenarios and journeys.**
5. **It is still solution-neutral enough that multiple implementations are possible.**

For example:

| Statement | Experience-first? | Why |
| :---| :---| :---|
| “Use the recommendation carousel” | No | Already assumes a UI solution. |
| “Create a Blend playlist” | Mostly feature-level | Names a specific product mechanism. |
| “Discover music my friend and I both enjoy” | Yes | Expresses human value independent of implementation. |
| “Find something that fits my current mood” | Yes | Bounded human outcome with many possible solutions. |

---

## The expert foundations become stronger when their distinct jobs stay visible

No single source supplies Meridian's complete hierarchy. Each contribution answers a different question, and the synthesis works only when those boundaries remain clear.

### Jared Spool / Center Centre: outcomes, experience vision, and strategic UX

Jared Spool’s work is especially important because it moves UX **upstream from interface execution into organizational direction**.

#### UX Outcomes before the Experience Vision

Current Center Centre material describes **UX Outcomes** as precise statements of how work will improve the lives of real people. It explicitly says those outcomes become the basis of the experience vision and can function as a measurable destination for teams. [source](source-index.md#src-spool-outcomes)

That gives an important sequence:

```text
Understand people
      ↓
Define the human improvement we seek
      ↓
Strategic UX Outcome
      ↓
Experience Vision
```

This prevents the vision from becoming inspirational fiction detached from evidence.

#### Experience Vision as a distant human-centered destination

Spool has long described an experience vision as a future state that acts like a visible destination for decision-making. The vision is research-based, focused on the user’s experience, and shared across the organization. [source](source-index.md#src-spool-vision-steps)

Current Center Centre material goes further: it describes the experience vision as the long-term goal and the product roadmap as the path toward it. Every roadmap item should represent a step toward the vision. [source](source-index.md#src-spool-vision-roadmap)

This is a major experience-first principle:

> **The roadmap does not define the experience vision. The experience vision constrains and evaluates roadmap choices.**

#### Journey research can generate the vision

Spool’s journey-to-vision method starts by observing people using current solutions — including existing products, other tools, and non-product processes. Teams map the current experience, identify frustration and delight, and use patterns in those journeys to imagine a better future experience. [source](source-index.md#src-spool-journey)

This creates the flow:

```text
Observed current experience
        ↓
Patterns of frustration / delight
        ↓
Aspirational future experience
        ↓
Experience Vision
```

#### Vision → scenarios → development

Spool also gives a useful bridge from strategic storytelling into delivery. In his “Promise, Vision, Scenario, and User Stories” model:

- a **promise story** reflects what the person would later say about the experience,
- a **vision story** describes the desired experience as it happens,
- **scenarios** add the contextual detail needed for design,
- **user stories** connect that design context to development. [source](source-index.md#src-spool-stories)

This is important because it shows that strategic experience language does not have to remain abstract. It can progressively become implementable.

#### The broader strategic shift

Center Centre’s recent strategic UX writing calls for organizations to emphasize **outcomes over outputs, experiences over products, and proactive UX over reactive UX**. [source](source-index.md#src-spool-strategic)

For this playbook, that means UX is not a downstream activity that validates a chosen feature. It is part of how the organization decides **what future is worth creating**.

---

### Indi Young: start with human purpose, not the solution

Indi Young provides the strongest foundation for starting **above the product and even above the stated problem**.

Her problem-space work asks teams to understand people and their larger purpose without anchoring that understanding to a solution or even to a specific organization. [source](source-index.md#src-young-problem)

Her current method explicitly begins in the problem space by asking how people mentally approach a goal, intent, or purpose. [source](source-index.md#src-young-method)

This introduces an important hierarchy:

```text
Human purpose / intent
        ↓
How people currently think and act
        ↓
Patterns, needs, tensions, gaps
        ↓
Opportunities for support
        ↓
Possible solutions
```

#### Why this matters

If research begins with:

> “How do people use our playlist feature?”

then the product has already framed the problem.

If research begins with:

> “How do people decide what they want to hear when they need energy, focus, comfort, novelty, or social connection?”

then the organization can discover needs that the current product structure may not even recognize.

This is the top of the experience-first hierarchy.

---

### Kim Goodwin: scenarios turn human understanding into design

Kim Goodwin’s scenario-driven design work provides the bridge from strategic intent into interaction structure.

Goodwin describes scenarios as the engine that drives design because they tell the team **why** the person needs the design, **what** the design must enable, and **how** the interaction needs to unfold. Her UIE material also notes that scenarios help teams identify critical functionality, language, and screen flow. [source](source-index.md#src-goodwin-scenarios)

This suggests a powerful progression:

```text
Experience intent
      ↓
Persona / behavioral context
      ↓
Scenario
      ↓
Requirements
      ↓
Interaction framework
      ↓
Flow and screens
```

The critical point is that **screens are consequences of scenarios**, not the starting point.

---

### Teresa Torres: opportunity space before solution space

Teresa Torres provides a disciplined mechanism for stopping teams from jumping directly from outcome to feature.

Her Opportunity Solution Tree separates:

```text
Desired Outcome
      ↓
Opportunity Space
(customer needs, pain points, desires)
      ↓
Solution Space
      ↓
Assumption Tests
```

The tree makes explicit that teams should understand and choose opportunities before committing to a solution. [source](source-index.md#src-torres-ost)

#### Why this matters in experience-first culture

A team should not assume:

```text
Need better discovery
      ↓
Build AI DJ
```

It should explore:

```text
Desired outcome
      ↓
Several opportunity areas
      ↓
Target opportunity
      ↓
Several candidate solutions
      ↓
Test assumptions
      ↓
Choose what to build
```

That is the mechanism that keeps **feature ideas subordinate to the experience/problem**.

#### Product trio and the death of sequential handoff

Torres also argues against the classic sequence:

```text
Stakeholder → PM → Designer → Engineer
```

She describes how context and nuance are lost with each functional handoff. In the product-trio model, product management, design, and engineering jointly participate in discovery and decision-making. [source](source-index.md#src-torres-handoffs)

This is central to the lower half of the experience-first hierarchy: engineering should encounter the experience and problem context **before** a finished screen is thrown over the wall.

---

### Marty Cagan / SVPG: product strategy decides which problems deserve focus

Marty Cagan’s product-strategy framing is useful because it distinguishes **strategy from the roadmap**.

SVPG defines product strategy as the mechanism for making product vision real while meeting company needs. At the product-team level, strategy decides **what problems to solve**, discovery determines tactics that can solve them, and delivery builds the chosen solution. [source](source-index.md#src-cagan-strategy)

Cagan also stresses focus: strategy requires choosing the few things that matter and therefore choosing what not to pursue. [source](source-index.md#src-cagan-strategy)

In an experience-first culture, product strategy therefore does not disappear. It answers a different question from experience strategy:

- **Experience Strategy:** How must the experience evolve?
- **Product Strategy:** Which strategically important problems should receive product investment now?

They are coupled lenses rather than a clean waterfall.

---

### Atlassian practitioners: experience strategy turns strategic context into experience choices

Adam Furness and Henry Tapia’s Atlassian case study applies Richard Rumelt’s strategy kernel to experience strategy:

1. **Diagnosis** — understand the current state and key experience problems.
2. **Guiding Policy** — define a broad response without prematurely specifying solutions.
3. **Coherent Actions** — make concrete, mutually reinforcing experience decisions. [source](source-index.md#src-atlassian-strategy)

Their approach explicitly combines business and experience strategy into envisioning prompts, then uses cross-functional envisioning to turn direction into future experiences. [source](source-index.md#src-atlassian-strategy)

This is useful because it prevents “experience strategy” from becoming a list of design principles with no diagnosis or trade-offs.

A real strategy must answer:

```text
What is really happening?
        ↓
What stance will we take?
        ↓
What coordinated decisions follow?
```

---

### GOV.UK: solve the whole problem with a multidisciplinary team

GOV.UK’s Service Standard reinforces three experience-first principles:

1. **Understand users and their needs.** [source](source-index.md#src-gov-needs)
2. **Solve a whole problem for users**, including work across organizational boundaries when necessary. [source](source-index.md#src-gov-whole)
3. **Use a multidisciplinary team** rather than treating design, policy, technology, and operations as isolated contributions. [source](source-index.md#src-gov-multi)

This broadens the product-design perspective into service design.

A user’s experience does not respect your org chart.

If the person must cross channels, products, departments, policies, and offline processes to achieve the outcome, then the experience-first unit of thought must be able to cross those boundaries as well.

#### Satyam / UXReactor adds a connected experience-first operating lens

Meridian synthesizes this contribution only from the five approved public UXReactor sources in the [Research Source Index](source-index.md#satyam--uxreactor-public-sources). Together, they support an experience-first culture that connects strategy, research, design, cross-functional practice, and organizational transformation.[source](source-index.md#src-uxreactor-5d) [source](source-index.md#src-uxreactor-tekion) [source](source-index.md#src-uxreactor-redseal) [source](source-index.md#src-techlead-kantamneni) [source](source-index.md#src-cioreview-uxreactor)

Meridian uses that public contribution as a supporting operating lens, not as the source of the Level 0–15 taxonomy. Experience Ecosystem becomes a cross-level orientation view. Experience Roadmap and Priorities becomes the living strategy artifact at Level 7. Design-quality thinking strengthens validation, implementation definition, delivery fidelity, and live learning at Levels 14–15.

---

## The synthesis turns those contributions into one decreasing-resolution chain

The foundations above now converge. Each level keeps a distinct decision job while preserving traceability to the person's purpose and the evidence that supports it.

### The full experience-first hierarchy

The hierarchy below is the recommended working model for this playbook.

> **Important:** The levels represent decreasing abstraction, not a mandatory stage-gate process. Teams learn recursively. Experience Strategy and Product Strategy are particularly interdependent.

```text
LEVEL 0   HUMAN PURPOSE IN CONTEXT
          What purpose is the person pursuing, independent of our product?
                ↓
LEVEL 1   CURRENT EXPERIENCE
          How is that purpose pursued today across the full ecosystem?
                ↓
LEVEL 2   PROBLEM AND OPPORTUNITY SPACE
          What evidence-backed needs, frictions, desires, risks, and leverage points exist?
                ↓
LEVEL 3   STRATEGIC UX OUTCOME
          Whose lived experience should improve, and in what observable way?
                ↓
LEVEL 4   EXPERIENCE VISION
          What could that person’s future lived experience become?
                ↓
LEVEL 5   EXPERIENCE STRATEGY
          What experience choices will move us from the present toward that vision?
                ↕
LEVEL 6   PRODUCT STRATEGY
          Which important problems or bets merit product investment?
                ↓
LEVEL 7   EXPERIENCE ROADMAP AND PRIORITIES
          Which actor-specific experience areas should receive attention now, next, and later?
                ↓
LEVEL 8   CRITICAL EXPERIENCE
          Within a priority area, what bounded, consequential experience must work?
                ↓
LEVEL 9   SCENARIOS AND JOURNEYS
          For whom, when, under what conditions, and through what sequence does it occur?
                ↓
LEVEL 10  SOLUTION CONCEPTS
          What substantially different approaches might enable the experience?
                ↓
LEVEL 11  ENABLING CAPABILITIES AND FEATURES
          What product, service, and technical mechanisms are required?
                ↓
LEVEL 12  INTERACTION ARCHITECTURE
          How should people and the system cooperate across information, actions, states, and rules?
                ↓
LEVEL 13  INTERFACE DEFINITION AND PROTOTYPING
          How is the interaction architecture expressed and explored at interface resolution?
                ↓
LEVEL 14  VALIDATION AND IMPLEMENTATION DEFINITION
          Does it create the intended experience, and is its behavior unambiguous?
                ↓
LEVEL 15  DELIVERY, LIVE EXPERIENCE, AND OUTCOME LEARNING
          What happens in real operation, and does it improve the experience as intended?
                ↓
          MEASURE THE UX OUTCOME
                ↺
          Feed evidence back into Levels 0–7.
```

## Sources

| Source | Used here for |
| :--- | :--- |
| [Jared M. Spool, “The 3 Steps for Creating an Experience Vision.” Center Centre, 14 June 2018.](source-index.md#src-spool-vision-steps) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [GOV.UK Service Manual, “1. Understand Users and Their Needs.”](source-index.md#src-gov-needs) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [GOV.UK Service Manual, “2. Solve a Whole Problem for Users.”](source-index.md#src-gov-whole) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
| [Center Centre, “Establishing Strategic UX Outcomes.”](source-index.md#src-spool-outcomes) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [Center Centre, “Craft + Lead a Strategic UX Vision.” Especially the section “Mapping Your Vision Into Your Product Roadmap.”](source-index.md#src-spool-vision-roadmap) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [Jared M. Spool, “Building an Experience Vision From a Journey Map.” Center Centre, 21 June 2018.](source-index.md#src-spool-journey) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [Jared M. Spool, “Promise, Vision, Scenario, and User Stories.”](source-index.md#src-spool-stories) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [Jared M. Spool, “For UX, the Future Must Be Strategic.” Center Centre, 28 May 2025.](source-index.md#src-spool-strategic) | Strategic UX outcomes, experience vision, current experience, prioritization, and roadmap themes. |
| [Indi Young, “Explanations — Problem Space.”](source-index.md#src-young-problem) | Human purpose, problem-space inquiry, and deep listening. |
| [Indi Young, “The Method: Data Science that Listens.”](source-index.md#src-young-method) | Human purpose, problem-space inquiry, and deep listening. |
| [Kim Goodwin / UIE, “Designing with Scenarios: Putting Personas to Work.”](source-index.md#src-goodwin-scenarios) | Scenarios, goal-directed design, and interaction frameworks. |
| [Teresa Torres / Product Talk, “Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes.”](source-index.md#src-torres-ost) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [Teresa Torres, “Discovery Hand-Offs Kill Momentum: Here’s What to Do Instead.”](source-index.md#src-torres-handoffs) | Opportunity space, continuous discovery, and collaborative decision-making. |
| [Marty Cagan, “Product Strategy — Overview.” Silicon Valley Product Group, 17 February 2020.](source-index.md#src-cagan-strategy) | Product vision, product strategy, problem selection, and product risk. |
| [Adam Furness and Henry Tapia, “Demystifying UX Strategy: Translating Business Decisions Into Better Experiences for Users.” Designing Atlassian, 24 March 2022.](source-index.md#src-atlassian-strategy) | Experience strategy as diagnosis, guiding policy, and coherent actions. |
| [GOV.UK Service Manual, “6. Have a multidisciplinary team.”](source-index.md#src-gov-multi) | Whole-service design, user needs, research, accessibility, delivery, and live learning. |
