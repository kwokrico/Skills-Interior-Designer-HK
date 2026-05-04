# interior-statutory-compliance

## Purpose
Use for statutory checks covering occupancy load, accessibility, and general interior code compliance.

## Core Outputs
- Compliance gap list with severity.
- Occupancy and fixture assumptions used.
- Required approval touchpoints and submission notes.

## Reference Table: Compliance Review Layers
| Layer | Typical Scope |
|---|---|
| Life safety | Egress, travel distance, exits, alarm/sprinkler interfaces |
| Accessibility | Clear widths, turning circles, sanitary provisions |
| Use/occupancy | Occupant load, function classification, capacity limits |
| Documentation | Drawing annotations, schedules, approval records |

## Decision Rules
1. If conflict exists, apply stricter requirement unless AHJ grants variation.
2. Separate assumed values from confirmed values.
3. Route detail-level physical conflicts to `interior-mep-clash-detection`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: apply BO/associated practice assumptions and note FSD/BD interface points.
- Mainland mode: apply PRC code and local implementation standards by city/province.
- Always state the governing authority explicitly; if unknown, output jurisdiction checklist first.

## Reference Table: Typology Compliance Emphasis
| Typology | Statutory Emphasis |
|---|---|
| Residential | Means of escape, sanitary/accessibility minimums |
| Workplace | Occupant density, accessible route continuity, toilet ratios |
| Retail | Crowd load, frontage egress distribution, signage obligations |
| Hospitality | Public assembly interfaces and back-of-house separation |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Egress or fire-system implication is identified | `interior-fire-life-safety` | `RISK STATEMENT -> FIRE-LIFE-SAFETY CHECKLIST -> REQUIRED ACTIONS` |
| Clearance/access practicality needs validation | `interior-anthropometrics-ergonomics` | `DIMENSION CHECKS -> USER IMPACT -> ADJUSTMENT RECOMMENDATIONS` |
| Compliance notes must flow into tender docs | `interior-tendering-qa` | `TENDER INSERT LIST -> DRAWING TAGS -> SPEC ADDENDA NOTES` |
