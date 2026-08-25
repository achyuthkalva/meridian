# Meridian independent forward-test report

## Seven isolated scenarios tested the knowledge baseline

The evaluation suite began with six fresh-agent runs. Each agent received Meridian, one realistic user request, and only the raw material needed for that request. A seventh run then added layout-bearing PDF and CSV evidence.

The agents did not receive the scoring rubric, expected behavior, known failure risks, intended wording, or another agent's output. All project names and evidence were synthetic.

Each response was scored across ten dimensions. A case required at least **18 of 20 points**, no hard failure, and every case-specific acceptance condition.

The full prompts, fixtures, rubric, and acceptance conditions are available in [`cases.md`](cases.md) and [`suite.json`](suite.json).

## Five baseline cases passed while one public claim lost source distance

| Case | Main risk | Baseline result | Final result |
|---|---|---|---|
| Test Case 1 | Later summary overpowers dated evidence | 20/20 - Pass | 20/20 - Pass |
| Test Case 2 | Strategy levels blur together | 20/20 - Pass | 20/20 - Pass |
| Test Case 3 | B2B metric replaces Human Purpose | 20/20 - Pass | 20/20 - Pass |
| Test Case 4 | Screens invent their own history | 20/20 - Pass | 20/20 - Pass |
| Test Case 5 | Impact, testimony, or ownership inflates | 16/20 - Fail | 20/20 - Pass |
| Test Case 6 | Full chain collapses actors or causality | 20/20 - Pass | 20/20 - Pass |
| Test Case 7 | PDF layout and CSV lifecycle flatten | Not run in baseline | 20/20 - Pass |

The baseline result was **five of six passes**. No baseline response invented a full strategy, converted a target into a measured result, or used an embedded source instruction as an agent command.

Test Case 5 still failed the stricter publication standard. It correctly kept the 25% and 15% figures as targets and gave shared designers credit, but compressed indirect notes into direct “staff” feedback and used an ownership verb stronger than the source.

## The failed wording showed how true evidence can weaken during compression

The raw source was a product manager's note reporting what operations and one supervisor had said. The first response shortened that chain to:

> “Staff said the new queue felt clearer...”

That sentence lost three facts:

- the evidence was secondhand;
- one claim came from one supervisor; and
- fewer calls were a reported belief, not an observed or measured reduction.

The same run changed participation in engineering clarification into “resolved state logic.” The underlying leadership was real, but the verb implied stronger decision authority.

Neither error changed the 16-level architecture. Both showed that evidence controls must survive the final sentence, not remain only in a private ledger.

## Four narrow repairs moved precision into every public sentence

| Repair | Rule added or strengthened | What the next isolated run revealed |
|---|---|---|
| 1 | Preserve reporting distance, speaker count, and certainty in the evidence reference. | Supporting guidance alone did not reliably survive final compression. |
| 2 | Move the source-distance pattern into Meridian's core instructions. | Attribution improved, but an ownership verb still exceeded the source. |
| 3 | Match every ownership verb to the documented contribution. | Ownership became exact, but a second speaker still relied on the prior sentence's attribution. |
| 4 | Repeat the source chain whenever the claim or speaker changes. | The final response preserved source, speaker count, evidence verb, targets, and shared ownership. |

The final safe pattern was:

> “The product manager's notes separately report that one supervisor said new staff understood the status labels without extra explanation.”

This is slightly longer than “staff found the labels clear.” It is also materially more truthful.

## A seventh case then proved that mixed formats retain their meaning

Test Case 7 added a visually structured PDF and a CSV validation log.

The successful response:

- visually inspected the PDF instead of relying only on extracted text;
- kept the left-column observations separate from right-column proposals;
- recognized that only the CRM non-replacement decision was approved;
- treated five CSV rows as bounded prototype evidence, not five proven unique participants;
- refused to call four completed rows an 80% success rate because one required help; and
- left implementation, release, and live outcomes Unknown.

This case verifies chat, Markdown, text, CSV, and layout-bearing PDF routes. Connector behavior remains dependent on the host and permissions, but Meridian's evidence standard does not change with the route.

## The final suite passed without changing the level architecture

The final result is **seven of seven passes**, **140 of 140 scored points**, and **zero hard failures** in the final runs.

The repairs changed only evidence-language controls:

- testimony distance;
- speaker identity and count;
- belief versus observation or measurement;
- sentence-level attribution; and
- ownership verb strength.

The Level 0-15 architecture, Product Direction decision, B2B applicability, interaction modes, and controlled cadence remain unchanged.

## The result is strong evidence, not a promise of perfect future output

Forward tests show whether an independent agent can apply the skill in realistic cases. They do not prove deterministic behavior across every model, host, domain, source quality, or connector.

This suite uses one main run per case, with repeated fresh runs only for the failed publication case. Scoring was manual and evidence-based, not a statistical benchmark. The synthetic fixtures are intentionally small and contain no real user or client data.

Future changes to evidence, ownership, outcome, interaction, or communication rules should rerun at least Test Case 1, Test Case 4, Test Case 5, and Test Case 7. Changes to the level architecture should rerun the complete suite.
