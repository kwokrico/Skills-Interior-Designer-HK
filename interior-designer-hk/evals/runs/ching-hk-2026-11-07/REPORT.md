# Ching HK behavioural evaluation — 7 November 2026

Final result: **4/4 scenarios pass, 14/14 content assertions pass, 4/4 expected routes pass.** Seven fresh-context executions were performed: four baseline cases, two first retests and one final stair retest.

## Method

Independent agents received the exact user prompt and skill path, with no expected answers, suspected bugs or proposed fixes. They were instructed not to read evaluation files, review reports or other agents' outputs. They read the routed skill resources and checked official sources. Actual responses and traces are saved here. The parent manually graded their content and routing; keyword presence alone was not used as a pass criterion.

Skill source hashes were captured before editing in [baseline-manifest.json](baseline-manifest.json); original cases and assertions are in [cases.json](cases.json). The updated cases are in [cases-final.json](cases-final.json). These are executed behavioural evaluations, separate from dispatcher/link/JSON checks.

## Results and corrections

| Scenario | Baseline | Action and final evidence |
|---|---|---|
| Access status | All 3 assertions and routing pass | No change needed. [Response](ching-hk-access-status.response.md) distinguishes enacted requirements, advisory provisions and client requirements; rejects unchanged ADA plan and automatic exemption |
| Required stair | All original 3 assertions and routing pass | Agent's official-source check surfaced B23 provisions missing from the skill summary. Added scoped flight/turn guidance and a fourth assertion. First retest passed B23 but omitted explicit accessibility, failing the existing combined assertion. Added a fire-module reporting rule. [Final response](ching-hk-required-stair.final.md) passes all 4 assertions and routing |
| Services | All 3 assertions and routing pass | No change needed. [Response](ching-hk-services.response.md) uses completion/connection dates, REC/REW/WR1 and separate drainage assessment |
| Green and IAQ | All 4 content assertions pass; expected MEP route missing | Added an explicit sustainability-to-MEP chain for BEC/major-retrofitting questions. [Retest response](ching-hk-green-and-iaq.retest.md) passes all 4 assertions and routing |

Changes are limited to:

- [HK adaptation](../../../references/ching-hk-adaptation.md): B23 scope and flight/turn checks alongside general B14 guidance.
- [Fire-life-safety module](../../../subskills/interior-fire-life-safety/interior-fire-life-safety.md): explicitly report unresolved accessibility checks in required-stair reviews.
- [Sustainability module](../../../subskills/interior-sustainability-wellness/interior-sustainability-wellness.md): load MEP for HK BEC/services applicability, adding statutory review where needed.
- [Evaluation definitions](../../evals.json): strengthened stair case without removing or weakening any original assertion.

The [BD Fire Safety Code](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf), B23.1–B23.3, was rechecked for the correction. Its follow-up retrieval is archived under `Reference/SS/Ching-HK-research-2026-11-07/b23-evaluation-followup.json`.

## Audit and limits

[Baseline grades](baseline-grades.json) preserve 13/13 content passes and 3/4 route passes. [First retest grades](retest-grades.json) retain the failed stair accessibility assertion. [Final results](results.json) give assertion-level evidence and response hashes. [Structural verification](post-change-structure.json) records changed-file links, five successful module loads and post-change source hashes. JSON parses and evaluation IDs remain unique.

Access and services use their initial passing executions; only affected scenarios were rerun. This is a small sampled evaluation, not proof of consistent behaviour on every run or a project compliance certificate. The response generators were independent; the parent grader also authored the fixes. The access run could not retrieve DMUA itself and correctly avoided claiming dimensional verification, while checking APP-176 successfully. Transient tool limits and corrected lookup attempts are retained in response traces.
