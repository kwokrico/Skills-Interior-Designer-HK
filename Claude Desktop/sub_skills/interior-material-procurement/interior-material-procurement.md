# interior-material-procurement

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
