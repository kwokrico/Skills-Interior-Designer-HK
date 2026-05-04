# interior-handover-dlp

## Purpose
Use for handover readiness, O&M completeness, as-built verification, and defect liability period tracking.

## Core Outputs
- Handover checklist with pass/fail criteria.
- O&M manual completeness audit.
- DLP issue register and closure protocol.

## Reference Table: Handover Closeout Essentials
| Item | Minimum Requirement |
|---|---|
| O&M manuals | Indexed by system/product with maintenance intervals |
| As-built drawings | Reflect approved SI/variation and field conditions |
| Test/commissioning docs | Available for relevant systems and fixtures |
| Snag status | Critical defects closed before practical handover |

## Decision Rules
1. No practical handover recommendation without O&M and as-built baseline.
2. DLP log must include owner, due date, and verification evidence.
3. Escalate repeat defects to root-cause review before closure.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align handover package to local contract closeout and FM expectations.
- Mainland mode: align handover and warranty records to local contract and property management standards.
- If region unclear, produce universal handover matrix with localized approval placeholders.

## Reference Table: Typology Handover Emphasis
| Typology | Handover Priority |
|---|---|
| Residential | Appliance/manual completeness and wet-area defect closure |
| Workplace | MEP operation clarity and phased occupancy readiness |
| Retail | Trading-ready signoff and maintenance quick-response plan |
| Hospitality | Guest-impact defects triage and rapid DLP turnaround |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Unresolved defect requires field verification | `interior-site-supervision` | `SITE VERIFICATION PLAN -> SI/RECTIFICATION NOTES -> CLOSURE EVIDENCE` |
| Replacement stock continuity is needed during DLP | `interior-material-procurement` | `REPLACEMENT STOCK MATRIX -> LEAD-TIME RISK -> SUPPLY ACTION PLAN` |
| Final document set needs compliance confirmation | `interior-statutory-compliance` | `DOCUMENT CHECKLIST -> COMPLIANCE STATUS -> FINAL SIGNOFF NOTES` |
