# interior-tendering-qa

## Purpose
Use for pre-tender quality checks to ensure a complete and biddable interior package.

## Core Outputs
- Completeness audit (drawings, schedules, specs, details).
- Tender risk list with clarification requirements.
- Bid-query readiness checklist.

## Reference Table: Tender Completeness Minimum
| Package Item | Required Status |
|---|---|
| GA plans and RCP | Coordinated and revision-matched |
| Detail set | 1:10/1:5 details for bespoke elements |
| Schedules | Door, finishes, fixtures, and hardware complete |
| Specification | Material/system standards clearly stated |

## Decision Rules
1. Missing critical details must be flagged before release.
2. Ensure drawing/spec/schedule terminology is aligned.
3. Route unresolved buildability issues to relevant technical sub-skills.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align package structure with local consultant/contractor tender conventions.
- Mainland mode: align package structure with local institute and contractor bid documentation norms.
- If region unknown, issue universal completeness matrix plus local adaptation checklist.

## Reference Table: Typology Tender Risk
| Typology | Common Tender Gap |
|---|---|
| Residential | Bespoke joinery details missing for unique rooms |
| Workplace | Incomplete coordination between fit-out and landlord interfaces |
| Retail | Feature element details not aligned with rollout timeline |
| Hospitality | FF&E/spec pack misalignment across guestroom variants |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Bid exceeds target budget | `interior-value-engineering` | `COST GAP SUMMARY -> VE OPTIONS -> RECOMMENDED TRACK` |
| Code annotation is unresolved in tender set | `interior-statutory-compliance` | `CODE ISSUE LOG -> REQUIRED NOTES -> DOCUMENT CORRECTIONS` |
| Pre-award SI/RFI response workflow must be defined | `interior-site-supervision` | `SI/RFI PROTOCOL -> RESPONSE SLA -> SITE COMMUNICATION MATRIX` |
