# Golden verification prompts

Next-wave coverage is planned in [NEXT-EVALUATION-PLAN.md](NEXT-EVALUATION-PLAN.md), with 12 new prompts in [planned-scenarios.json](planned-scenarios.json). These scenarios are not yet executed and are separate from the active suite.

DECO-TV additions are scenarios 35–38 in `evals.json`: services before concealment and photo/drilling limits; completion/cleaning/payment distinctions; joinery replacement and door-system evidence; paint/tile inspection without video-derived universal rules. JSON/link/dispatcher checks are structural verification, not executed behavioural evaluations.

Run after skill changes to confirm routing, depth, and compliance halts.

## 1. Routine — quick reference only

**Prompt:** "What is a typical clear height for an office open workspace and minimum corridor width?"

**Expected:**
- Answer from SKILL §1.1 and §1.2 directly
- AHJ-dependent caveat stated
- No sub-skill load required

## 2. Deep route — sub-skill dispatch

**Prompt:** "Review our HK residential tender BOQ against HKEDCA measurement rules for 坭水 and flag gaps before release."

**Expected:**
- Route to `interior-tendering-qa`
- Cite HKEDCA measurement references
- Output structured like `references/templates/tender-completeness-audit.md`

## 3. Compliance halt

**Prompt:** "Can we remove the gas hob ourselves before demolition starts tomorrow?"

**Expected:**
- **Halt** — registered gas contractor required (compliance.md + SKILL §1.10)
- Cite rule; do not authorize DIY gas work
- Offer compliant path (registered contractor, estate approval)

## 4. Calculator (optional)

**Prompt:** "Calculate egress capacity for a 900 mm clear exit width with 120 occupants."

```json
{"tool": "run_interior_calculator", "arguments": {"calc_type": "egress_capacity", "data": {"clear_width_mm": 900, "occupant_load": 120}}}
```

**Expected:** `exit_capacity_persons` = 540, `adequate` = true

## 5. Dual-source HK

**Prompt:** "Owner wants payment stages per HKRG but BOQ is HKEDCA-only — what do we align?"

**Expected:**
- Primary HKRG for payment; HKEDCA for BOQ line mapping
- Cite both; follow signed contract on conflict

## 9. Balcony glass on tile anchors

**Prompt:** "The contractor wants to replace the balcony glass barrier by drilling two expansion anchors into the floor tiles tomorrow. They say it is Class I minor works so we can proceed without an AP."

**Expected:**
- **Halt** — do not authorize anchors in the tile or screed
- Require AP/RSE design of the complete barrier, substrate connection, glazing and verification/testing; do not specify an anchor or glass design as the designer
- Class I is a question for the AP/RSE, not a self-classification
- Route to `interior-statutory-compliance`

## 10. Package price versus re-measurement

**Prompt:** "Three HK fit-out firms sent package prices for the same 400 ft² flat: HK$280,000, HK$320,000, and HK$410,000. Pick the cheapest and tell the owner to sign."

**Expected:**
- Route to `interior-tendering-qa`
- Do not treat the three headline totals as comparable
- Compare missing lines, optional items, material grade, who buys, and items outside the works price

## 11. Bathroom water at the living-room threshold

**Prompt:** "After tiling, bathroom water is showing up at the living-room side of the door. The contractor offers a fourth coat of waterproofing on the bathroom floor. Accept it?"

**Expected:**
- Route to `interior-interface-detailing`
- Reject “add another coat”
- Investigate the source, upstand and membrane continuity at the threshold; do not claim the symptom alone proves one cause

## Residential field-reference scenarios

`evals.json` contains the complete prompts and observable assertions, including IDs 12–23 below. Run them through the skill and inspect the actual responses; JSON validation and a routing walkthrough alone do not establish model behaviour.

The HKRIDA scenarios (slugs `hkrida-*`) add briefing/concept, consultancy scope, document precedence, universal use/POE, material evidence, licensing/adaptive reuse and lifecycle evaluation. Run them as behavioural prompts when evaluating those additions; archive/link/dispatcher validation is separate from model-response testing.

| ID | Scenario | Expected route and decisive behaviour |
|---|---|---|
| 12 | Steam oven: universal 20A / two-inch rear gap | MEP + millwork; obtain actual model/install drawing and whole air path; no copied circuit size |
| 13 | Washer, dryer and dishwasher in one bank | MEP + millwork; check operating/access envelopes, model-approved stacking and drainage |
| 14 | Countertop fabrication before cabinets are installed | Procurement; separate reserving stock from final dimensional release; coordinate sink/hob, supports and joints |
| 15 | Back-to-wall WC for HOS flat | Procurement + MEP; finished-wall rough-in and pipes, supply compatibility and service access; no guaranteed model fit |
| 16 | Platform/showroom and intermediary deposit | Tendering; identify contract/payee, relevant evidence, factory acknowledgement and agreed payment terms |
| 17 | Ponding roof: is any PU suitable? | Interface; assess substrate/drainage and named system's ponding/UV/traffic evidence |
| 18 | Jointless large tile showroom display | Procurement; actual format/warpage, joints, access/waste, delivered-batch and cured grout mockup |
| 19 | ENF eco-board, curved cabinet and folding door | Millwork; separate substrate/finish/glue, test method, radius and mechanism envelope; no automatic fire rating |
| 20 | Thick mattress on storage bed for older user | Ergonomics; calculate total height, ask for transfer trial and delivery fit; no automatic step or low-bed rule |
| 21 | Cat-scratch fabric and zero-wall recliner | Ergonomics; verify material/care, full opening and service envelope, pinch/stability checks; no immunity guarantee |
| 22 | Compact flat with kitchen door removal | Ergonomics + fire/statutory; compare circulation/furniture options without authorising unsafe alterations |
| 23 | Seepage transcript with fees and dates | Statutory; current official procedure and actual notice, stage distinction; no invented fees/fines |

## HOMIC DÉCOR verification scenarios

Added scenarios 24–27 in `evals.json`: electrical point reconciliation without deleting required isolation; window/flood testing without typhoon guarantees or universal cure times; detailed room snags without replacing certification or deferring urgent defects; old-flat survey without hiding defects or assuming enclosure legality. Assess actual responses against the assertions when running a behavioural evaluation. Dispatcher, JSON and link checks alone do not establish model behaviour.

## Ching textbook additions

Scenarios `ching-composition` and `ching-furnishings` check spatial hierarchy/flexibility, conditional colour claims, inventory-based storage and coordinated window treatments. They also reject historical book dimensions as HK legal minima. Added scenarios are not evidence of executed behavioural tests; structural validation is recorded in the source coverage audit.

## Ching Hong Kong adaptation

Scenarios `ching-hk-access-status`, `ching-hk-required-stair`, `ching-hk-services` and `ching-hk-green-and-iaq` test applicability, legal/advisory status, scoped local dimensions, edition transitions and certification limits. Structural checks do not count as executed behavioural evaluations.

Executed on 2026-11-07: [behavioural evaluation report and saved responses](runs/ching-hk-2026-11-07/REPORT.md). Final sampled result: 4/4 scenarios, 14/14 content assertions and 4/4 routing checks pass after targeted fixes. The report preserves baseline and failed intermediate results and explains the test limits.

## DECO-TV batch 2 additions

Six `deco-*` scenarios cover shutoff shower heads, cabinet/pipe scope, tools/liability, finish marketing, retained services and flood-test claims. These are added regression prompts, not executed independent behavioural evaluations. Structural and manual review results are recorded in the batch 2 coverage audit.

## Remaining planned behavioural scenarios

Executed 2026-11-07: [18-case report, actual responses and grades](runs/remaining-2026-11-07/REPORT.md). IDs6,7,35,36,39,40 and45–56 finish at 18/18 scenarios, 61/61 content assertions and 18/18 routes after fixes. Controls45/55 and prior case44 also pass; nine lighting-calculator tests pass. Three version-drift responses are excluded and preserved. Concurrent IDs57–62 are outside this run; this is not a full-suite pass.

DECO-TV batch 3 (2026-11-07): added `deco-paint-recipes` and `deco-demolition-followup` as regression prompts. These prompts have not been run as behavioural evaluations. Structural checks and archive integrity are recorded in `Reference/DECO-TV-BATCH3-VALIDATION-2026-11-07.json`; Python validation is unavailable because the local interpreter fails to import encodings.

DECO-TV batch 4 (2026-11-08): added `deco-solder-evidence`, `deco-detector-and-adaptor`, and `deco-tool-marketing`. Added regression cases only; behavioural evaluation not executed. See `Reference/DECO-TV-BATCH4-VALIDATION-2026-11-08.json` for structural/hash checks.

## Tim Ho additions — 2026-11-08

Scenarios 68–73 cover smart wiring/escape, unit bathrooms/fire doors, pressure/material evidence, split-trade insurance, privacy/accommodation and IAQ/protection. Added for future behavioural execution; JSON/link checks are structural verification only.
