# Next behavioural evaluation plan

Status: **planned, not executed**. Created 7 November 2026. This plan extends the four tested Ching HK cases; it does not treat the other existing scenarios as already verified. The 12 new prompts and their 36 assertions are in [planned-scenarios.json](planned-scenarios.json). They have separate plan IDs and do not change the active 44-case suite.

## Scope and order

| Wave | Scenarios | Why / expected outcome |
|---|---|---|
| 1 — Safety and applicability | New PLAN-01–06: egress calculator, raised-floor barrier, windowless subdivision, phased energy works, electrical grace boundary, fire assembly substitution | Checks consequential local decisions and whether numerical shortcuts are rejected for the right reason; includes a case that can satisfy a historical grace condition |
| 2 — Useful design outputs | Existing 39–40 (composition/furnishings), plus new PLAN-07–10: concept alternatives, window-treatment brief, acoustics, lighting review | Checks that the skill can deliver practical advice and artifacts as well as halt unsuitable proposals |
| 3 — Proportionate response and regression | New PLAN-11–12: general educational question and unavailable current source; existing 6 (material schedule), 7 (tender readiness), 35 (concealed works), 36 (closeout) | Checks overblocking, source honesty, complete deliverables and preservation of earlier workflows |

Initial scope: **18 scenarios** (12 new + 6 existing), each with one independent baseline response. Add focused retests only for demonstrated failures and affected routes. The four already-tested cases 41–44 are regression candidates when a shared rule or their relevant module changes; avoid automatic full-suite reruns for unrelated edits.

## Execution protocol

1. Capture the skill version/hashes and exact prompt. Keep inputs/expected assertions separate from response artifacts.
2. Give a fresh-context evaluator the user prompt, skill entrypoint and only necessary raw fixtures. Withhold expected answers, prior results and proposed fixes. Use read-only source access; permit only its designated result artifact to be written. No external submissions, certificates, emails or purchases.
3. Allow official-source checking where the task needs it. Record actual source URLs, editions, dates and failed retrievals. Historical audit questions require the relevant historical basis. This plan's assertions are evaluation objectives, not newly verified legal advice.
4. Assess the saved response against every assertion and expected route. Use human/parent judgement with quoted or located evidence, not keyword matching alone. Separately note factual accuracy, source currency, useful task completion and unsupported assumptions.
5. Fix the smallest demonstrated skill defect. Preserve failed responses and grades. Rerun the affected prompt in a fresh context, without telling the evaluator what failed. If a shared instruction changes, also run a relevant positive control and previously passing case.
6. Report pass/fail/blocked clearly. A failed source lookup is not a pass on source verification; determine whether the response honestly limits the affected claim. Do not mark an unrun assertion as passed.

## Fixtures and fairness

The first wave uses text-only scenarios; no missing attachments are required. Concept PLAN-07 intentionally omits opening positions and requests early options: passing means useful conditional design plus identified limitations, not an invented final fit. Window PLAN-08 asks for a brief before product selection, so missing measurements should become schedule fields rather than prevent all work.

For source-failure PLAN-12, the user explicitly supplies the limitation. This tests response handling, not whether the tool actually fails. A future tool-outage test must record the actual tool condition separately. Do not misreport a prompt-level hypothetical as a simulated infrastructure failure.

Before declaring the whole skill reliable, add a later artifact-based round with synthetic dimensioned plans, door/service schedules, photometric inputs and comparable quotes. Define fixture facts and scope first; never penalise a response for information the fixture did not supply.

## Acceptance and stopping criteria

- A scenario passes only when all its assertions and required routing pass, with no material contradictory advice elsewhere in the response.
- Treat unsafe approval, fabricated statutory status/source checks, and unsupported certification as critical failures. Fix and retest before using the affected behaviour as a passed capability.
- For an observed omission, correct the reusable decision or reporting rule rather than teaching the exact test answer.
- After two unsuccessful correction/retest cycles, stop that scenario and report the unresolved failure; continue independent unaffected cases. Preserve evidence rather than weakening assertions to obtain a pass.
- One passing response is sampled evidence, not a reliability rate. For critical paths, later run at least three materially varied prompts (including a valid/positive case and a boundary case) before claiming broader robustness.

## Deliverables

Save a new run folder with exact inputs, source hashes, responses/traces, assertion-level grades, changes, retests and final limits. Keep this planning file and planned JSON unchanged as the original plan; promote selected cases into the active suite with fresh unique IDs when execution starts. Record which tests were executed and which remain pending.
