---
name: interior-material-procurement
description: >
  Material schedules (物料規格表), lead times, dye lots, or-equal sourcing, and
  owner- vs contractor-supply roles for interior packages. Use for 選料, finishes
  schedules, supply certainty, or batch continuity.
disable-model-invocation: true
---

# interior-material-procurement

For cost-driven alternates and Good-Better-Best options, use `interior-value-engineering` instead.  
For interface/detail implications of substitutions, use `interior-interface-detailing` instead.  
For loose furniture only, use deliverables FF&E §3.5 — not the full material schedule.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 物料表 / material or finishes schedule / 選料 | `interior-material-procurement` | — |
| Lead time, dye lot, supply risk | `interior-material-procurement` | — |
| VE / cost alternatives | Chain to | `interior-value-engineering` |
| Transition detail for substitute finish | Chain to | `interior-interface-detailing` |
| FD door / certified fire ironmongery | Chain to | `interior-fire-life-safety` |

## Purpose

Sourcing strategy, schedule generation, lead-time control, dye-lot consistency, owner- vs contractor-supply clarity, and substitution risk — with HK residential patterns from the material-schedule template.

## Core Outputs

- **Material schedule** from [`material-schedule.md`](../../references/templates/material-schedule.md) (main table + owner appliance/furniture sheets + soft 總則).
- Procurement risk register by long-lead item.
- Ex-stock vs indent recommendation.
- Batch/dye-lot control instructions.

## Local references

| File | Use |
|------|-----|
| [`item-code-map.md`](references/item-code-map.md) | Prefix → category coding |
| [`procurement-roles.md`](references/procurement-roles.md) | 採購方式 + 陪同選購 + HKRG owner-supply |
| [`hk-residential-defaults.md`](references/hk-residential-defaults.md) | Typical first pick / or equal |
| [`hk-brand-unit-prices.md`](references/hk-brand-unit-prices.md) | Indicative HKD unit-price ranges by brand/tier (budget only) |
| [`general-notes-checklist.md`](references/general-notes-checklist.md) | Soft 總則 (checklist only — not new hard stops) |

## Reference Table: Procurement Control Points

| Item | Control |
|---|---|
| Stone/tiles | Approve mockup and lock batch before production |
| Fabric/wallcovering | Single dye-lot for continuous surfaces where possible |
| Timber veneer | Sequence sheets for grain continuity zones |
| Imported specialty items | Confirm shipping + customs buffer |
| Wet porcelain sets | Same factory/batch for adjacent FL + WT lines |
| Fire door sets | Certified assembly only — no appearance-only swap |

## Decision Rules

1. On schedule / 選料 requests: emit [`material-schedule.md`](../../references/templates/material-schedule.md); seed brands from `hk-residential-defaults.md` as 「或同等」.
2. Empty brand/model on a showroom category → **待選** + 設計師陪同選購 = 是 (`procurement-roles.md`).
3. Soft 總則 from `general-notes-checklist.md` — suggest gaps; do **not** invent compliance hard stops (parent `compliance.md` still governs life-safety / licensed works).
4. Wet-area tile / stone / waterproof lines → apply soft wet notes; if joint/threshold detailing asked, chain `interior-interface-detailing`.
5. FD / fire-rated door or certified fire hardware → chain `interior-fire-life-safety`.
6. Owner appliances / loose furniture → companion sheets; completeness vs quote → `interior-tendering-qa`.
7. Budget cut on a locked schedule line → `interior-value-engineering` G-B-B; this skill validates or-equal + lead time.
8. Unit-rate / budget / brand price questions → load `hk-brand-unit-prices.md`; cite as indicative only; require live quote before tender.
9. Never recommend a substitute without a performance equivalency note.
10. Highlight programme impact from long-lead slippage.
11. From P2 hatch legend + P1 joinery tags (L/S/K/B): seed schedule codes; map `自購` to owner-supply sheets — conventions in [`hk-residential-mini-tender-set.md`](../../references/cases/hk-residential-mini-tender-set.md).

## Drawing-set → schedule map (HK residential mini-set)

| Drawing cue | Schedule action |
|---|---|
| P2 floor/sill hatch codes | FL / sill / threshold lines; same batch notes for wet sets |
| P1 tags L/S/K/B | Joinery CB lines; elev cross-ref in 圖樣 column |
| `自購` on plan | Owner appliance / loose FF&E companion sheet — exclude from contractor BOQ |
| Codes only on drawings | Flag missing consolidated 物料規格表 → `interior-tendering-qa` gap register |

## Region-Switch Notes (HK / Mainland China)

- Hong Kong mode: importer/distributor stock checks, customs buffers, HKRG owner-supply timing, showroom 選樣 with designer.
- Mainland mode: domestic manufacturer qualification, regional logistics, factory QA norms.
- If location unclear: dual sourcing (local + imported fallback).

## HK Local Practice

- HK residential refurb: owner-supplied tiles/fixtures per HKRG — confirm delivery dates at demolition (`interior-site-supervision`).
- Align long-lead items with HKEDCA trade sequence (e.g. windows/AC at 清拆 stage per HKEDCA).
- Route contract supply disputes to `interior-tendering-qa` + HKRG owner-supply list adaptation.

## Reference Table: Typology Procurement Risk

| Typology | Highest Procurement Risk |
|---|---|
| Residential | Small-batch customization and finish consistency |
| Workplace | Program-critical carpet/ceiling/partition systems |
| Retail | Branded feature materials with short launch deadlines |
| Hospitality | High-spec finishes with long mockup approval loops |

## Auto-Chain Directives (Deterministic Schema)

| Trigger | Chain | Output format |
|---|---|---|
| Budget gap or substitution request appears | `interior-value-engineering` | `GOOD-BETTER-BEST MATRIX -> COST DELTA (cite hk-brand-unit-prices) -> DESIGN IMPACT` |
| Unit-rate or brand price band needed on a schedule line | `interior-value-engineering` (if comparing tiers) | `INDICATIVE UNIT RANGE -> LIVE QUOTE HOLD -> OR-EQUAL NOTE` |
| Proposed substitute changes joints/transitions | `interior-interface-detailing` | `INTERFACE IMPACT -> REVISED DETAIL LOGIC -> PROFILE REQUIREMENTS` |
| Spare stock and maintenance data planning is required | `interior-handover-dlp` | `HANDOVER STOCK LIST -> O&M DATA NEEDS -> DLP PREP NOTES` |
| Schedule line is FD / certified fire door or fire ironmongery | `interior-fire-life-safety` | `RATING CHECK -> CERTIFIED SET REQUIREMENTS -> NON-COMPLIANT SUBSTITUTES BLOCKED` |
| Schedule line needs joinery carcass / HPL / hardware detailing | `interior-millwork-technical` | `CARCASS/FACE SPEC -> HARDWARE SET -> BUILDABILITY NOTES` |
| LG line needs CCT/CRI/IP / driver access review | `interior-lighting-science` | `PHOTOMETRIC TARGETS -> IP/CCT CHECK -> ACCESS REQUIREMENTS` |
| Owner-supply sheets incomplete vs tender quote | `interior-tendering-qa` | `OWNER-SUPPLY GAP LIST -> QUOTE CROSS-CHECK -> DELIVERY HOLD POINTS` |
| P2/P1 codes present but no consolidated schedule | `interior-tendering-qa` | `MINI-SET GAP -> SCHEDULE REQUIRED -> HOLD RELEASE` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog
* [material-schedule.md](../../references/templates/material-schedule.md) — schedule artifact
* [hk-residential-mini-tender-set.md](../../references/cases/hk-residential-mini-tender-set.md) — P2 hatch / P1 tag / 自購 conventions