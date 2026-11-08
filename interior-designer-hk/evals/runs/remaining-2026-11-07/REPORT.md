# Remaining behavioural scenarios — 7 November 2026

**Final sampled result: 18/18 planned scenarios, 61/61 content assertions and 18/18 routing checks pass after corrections.** The baseline was 6/18 scenarios, 55/61 assertions and 8/18 routes. These are sampled responses, not a reliability rate or statutory validation.

The general-education positive control (55) and previously passing egress case (45) pass again. The earlier energy/IAQ case (44) also passes its four assertions and routing. There were **37 response executions: 34 graded and 3 excluded for concurrent version changes**. Nine numerical regression tests pass separately.

## Scope and method

Executed the agreed 12 new cases (promoted to IDs45–56) and existing IDs6,7,35,36,39,40. The original [plan](../../NEXT-EVALUATION-PLAN.md) and [planned prompts](../../planned-scenarios.json) remain unchanged. Concurrent work subsequently added IDs57–62; those six are **not tested by this report**. This is not a full 62-case-suite pass.

Each response came from a fresh independent evaluator given only its exact prompt, the skill and relevant source access. Expected assertions, previous answers and proposed fixes were withheld. Parent review graded every content assertion and the recorded module trace separately, requiring both to pass. No assertions were weakened. Exact inputs, unedited responses, per-assertion evidence and hashes are retained in [grading.json](grading.json) and [cases.json](cases.json).

## Results

| ID | Scenario | Baseline | Latest sampled result |
|---|---|---|---|
| 6 | eval-material-schedule-hk | pass | [pass](case-6.response.md) |
| 7 | eval-mini-tender-set-bid-readiness | pass | [pass](case-7.response.md) |
| 35 | deco-stage-inspections | fail | [pass](case-35.frozen-1.md) |
| 36 | deco-closeout-cleaning | fail | [pass](case-36.frozen-1.md) |
| 39 | ching-composition | fail | [pass](case-39.frozen-1.md) |
| 40 | ching-furnishings | fail | [pass](case-40.frozen-1.md) |
| 45 | hk-egress-calculator-limit | pass | [pass](case-45.frozen-2.md) |
| 46 | hk-barrier-raised-floor | fail | [pass](case-46.frozen-1.md) |
| 47 | hk-room-subdivision-daylight | fail | [pass](case-47.frozen-1.md) |
| 48 | hk-energy-phased-positive | fail | [pass](case-48.frozen-1.md) |
| 49 | hk-electrical-grace-boundary | fail | [pass](case-49.frozen-1.md) |
| 50 | hk-fire-assembly-substitution | fail | [pass](case-50.frozen-1.md) |
| 51 | concept-deliverable-positive | fail | [pass](case-51.frozen-1.md) |
| 52 | window-treatment-coordination | pass | [pass](case-52.response.md) |
| 53 | acoustic-system-distinction | fail | [pass](case-53.frozen-1.md) |
| 54 | lighting-maintained-target | fail | [pass](case-54.frozen-2.md) |
| 55 | general-question-no-overblocking | pass | [pass](case-55.frozen-1.md) |
| 56 | source-failure-contained | pass | [pass](case-56.response.md) |

Additional regression: [44 — energy/IAQ](case-44.frozen-2.md), 4/4 assertions and required routes pass.

## Demonstrated corrections

- **Routing:** readers often answered correctly from a single module but skipped required coordination. The master now requires reading and applying applicable modules, including remediation during a compliance hold. It adds reusable multi-domain routes without requiring code checks for general lessons.
- **Barrier platforms:** require separate estate/management and statutory review, AP/RSE assessment and interface coordination even when anchors are unchanged.
- **Concept design:** require actual section/height and sightline considerations, plus fixed-versus-movable tradeoffs and future-use checks when flexibility is requested.
- **Closeout cleaning:** give concrete tasks, inclusions/exclusions, responsibility and fixed-hours versus completed-task basis, not merely a request for an itemised quote.
- **Lighting calculation:** case54 inspected the helper and exposed duplicated MF/LLF losses even though its answer avoided that mistake. The helper now applies one explicit overall factor, rejects ambiguous legacy `llf`, and requires supported inputs. The formula, glossary and lighting guidance agree. At 500 lux maintained and MF0.8, initial design illuminance is 625 lux; no second default factor is applied. Nine tests cover the result, missing/invalid inputs and fixture rounding. Legacy callers relying on default factors or `llf` must now provide a resolved overall factor.

Details: [change log](CHANGELOG.md), [calculator test results](calculator-test-results.json), [test source](../../test_lighting_calculator.py). The final lighting response is [case54 frozen-2](case-54.frozen-2.md).

## Versions, concurrency and sources

All 86 original baseline resources retained their captured hashes until the baseline completed. Three new DECO reference files appeared meanwhile, but none was read in the baseline traces. During the first retest batch, concurrent work changed shared resources and added six evaluation cases. Responses `case-46.retest-1.md`, `case-47.retest-1.md` and `case-48.retest-1.md` are preserved but excluded because their exact resource version could not be assured.

Subsequent retests used a frozen copy, preserved in [retest-skill-snapshot.zip](retest-skill-snapshot.zip) with [manifest](retest-manifest.json). The lighting correction and final regressions use [final-skill-snapshot.zip](final-skill-snapshot.zip) with [manifest](final-manifest.json). The later snapshot also incorporates a concurrent heading correction and inspector-quality note. These do not remove the earlier fixes. Improvements cannot be attributed solely to this patch because concurrent integration preceded the frozen runs.

Responses record official source URLs, checked dates and retrieval limitations. Search excerpts are distinguished from full-document inspection. Case56 tests the user's stated unavailable-source premise, not an induced tool outage. Source retrieval failures are not counted as successful live checks. No licensed sign-off, external submission or purchase occurred.

Lighting definitions were checked against official CIE/IES material; [archived retrieval notes](../../../../Reference/SS/Lighting-maintenance-verification-2026-11-07/source-notes.json) record the successful CIE retrieval and IES search excerpt after a direct-fetch timeout. These are source notes, not a complete webpage archive.

## Validation and limits

[Structural validation](structural-validation.json) records unique active IDs, all 16 dispatcher modules loading, changed-instruction/new-source/report link checks, preserved response hashes and the remaining live-versus-snapshot differences. Structural checks and calculator unit tests are separate from behavioural passes.

No planned scenario remains failed or blocked. One response per case/version does not establish robustness. Next useful coverage is an artifact-based round with dimensioned plans, door/service schedules, photometric data and comparable quotations, plus varied valid/boundary prompts for critical paths. Untested scenarios, including concurrent IDs57–62, retain unverified status here.

Source-register audit also found 47 pre-existing unresolved extract links outside the new lighting entry; these are listed in structural-validation.json and were not used as evidence for this run. Their source recovery is outside the planned behavioural evaluation.
