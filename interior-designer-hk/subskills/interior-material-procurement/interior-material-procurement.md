---
name: interior-material-procurement
description: >
  Material lead times, dye lots, alternates, and sourcing risk for interior packages.
  Use when supply certainty or batch continuity affects design decisions.
disable-model-invocation: true
---

# interior-material-procurement

For cost-driven alternates and Good-Better-Best options, use `interior-value-engineering` instead.  
For interface/detail implications of substitutions, use `interior-interface-detailing` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Lead time, dye lot, supply risk | `interior-material-procurement` | — |
| VE / cost alternatives | — | `interior-value-engineering` |
| Transition detail for substitute finish | Chain to | `interior-interface-detailing` |

## Purpose
Use for sourcing strategy, lead-time control, dye-lot consistency, and material substitution risk.

## Core Outputs
- Procurement risk register by long-lead item.
- Ex-stock vs indent recommendation.
- Batch/dye-lot control instructions.

## Reference Table: Procurement Control Points
| Item | Control |
|---|---|
| Stone/tiles | Approve mockup and lock batch before production |
| Fabric/wallcovering | Single dye-lot for continuous surfaces where possible |
| Timber veneer | Sequence sheets for grain continuity zones |
| Imported specialty items | Confirm shipping + customs buffer |

## Decision Rules
1. If budget alternatives are requested, pair with `interior-value-engineering`.
2. Never recommend a substitute without performance equivalency note.
3. Highlight program impact from long-lead slippage.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: prioritize importer/distributor stock checks and customs lead-time buffers.
- Mainland mode: prioritize domestic manufacturer qualification, regional logistics, and factory QA norms.
- If location is unclear, present dual sourcing strategy (local + imported fallback).

## HK Local Practice

- HK residential refurb: owner-supplied tiles/fixtures per HKRG — confirm delivery dates at demolition (`interior-site-supervision`).
- Align long-lead items with HKEDCA trade sequence (e.g. windows/AC at 清拆 stage per HKEDCA).
- Route contract supply disputes to `interior-tendering-qa` + HKRG §6 owner-supply list.

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
| Budget gap or substitution request appears | `interior-value-engineering` | `GOOD-BETTER-BEST MATRIX -> COST DELTA -> DESIGN IMPACT` |
| Proposed substitute changes joints/transitions | `interior-interface-detailing` | `INTERFACE IMPACT -> REVISED DETAIL LOGIC -> PROFILE REQUIREMENTS` |
| Spare stock and maintenance data planning is required | `interior-handover-dlp` | `HANDOVER STOCK LIST -> O&M DATA NEEDS -> DLP PREP NOTES` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

