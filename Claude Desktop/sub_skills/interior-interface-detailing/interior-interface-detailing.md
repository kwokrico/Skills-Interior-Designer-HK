# interior-interface-detailing

## Purpose
Use for transition and interface details where dissimilar materials meet.

## Core Outputs
- Buildable detail intent for joints/transitions.
- Tolerance and movement allowances.
- Moisture, cracking, and edge-protection mitigation notes.

## Reference Table: Threshold Transitions
| Type | Recommended Approach |
|---|---|
| Stone to carpet | 3 mm brass L-profile; recess wet bed to align FFL |
| Timber to tile | T-profile movement joint; keep expansion allowance |
| LVT to tile | Flush transition strip with substrate feathering |
| Wet to dry zone | Step-down or drain edge with waterproofing continuity |

## Decision Rules
1. If level mismatch exceeds 3 mm, issue explicit transition detail.
2. Include movement joint strategy for long runs and dissimilar materials.
3. Route unresolved level mismatches to `interior-thickness-build-up`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: prioritize maintainability and humid-climate durability details.
- Mainland mode: prioritize local system compatibility and factory-fabricated detail options.
- If jurisdiction is unclear, issue neutral detail principles and flag profile/spec verification.

## Reference Table: Typology Interface Priorities
| Typology | Critical Interface |
|---|---|
| Residential | Wet-to-dry transitions and skirting terminations |
| Workplace | Raised-floor to fixed-floor boundaries and service boxes |
| Retail | High-traffic threshold durability at storefront entries |
| Hospitality | Stone/timber transitions in lobby and wet-area edges |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Finish level delta creates interface risk | `interior-thickness-build-up` | `LAYER STACK COMPARISON -> LEVEL DELTA -> CORRECTION OPTIONS` |
| Joinery meets architectural finish with unresolved edges | `interior-millwork-technical` | `JOINERY EDGE CONDITION -> HARDWARE/BUILDABILITY CHECK -> DETAIL ACTIONS` |
| Field tolerance or SI-based adjustment is needed | `interior-site-supervision` | `SITE CHECK STEPS -> SI BULLET POINTS -> AS-BUILT UPDATE NOTES` |
