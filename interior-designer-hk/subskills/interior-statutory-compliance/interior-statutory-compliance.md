---
name: interior-statutory-compliance
description: >
  Occupancy, accessibility, and general interior code compliance reviews.
  Use for statutory gaps, submission touchpoints, and AHJ-dependent checks.
disable-model-invocation: true
---

# interior-statutory-compliance

For detailed egress/fire strategy, use `interior-fire-life-safety` instead.  
For physical service conflicts, use `interior-mep-clash-detection` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Occupancy, accessibility, code gap list | `interior-statutory-compliance` | — |
| Travel distance / exit capacity detail | — | `interior-fire-life-safety` |
| HK pre-start insurance/permits (industry) | This skill + HKEDCA ref | `interior-site-supervision` for execution |

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

## HK Local Practice (HKEDCA)

> HKEDCA documents **industry pre-start practice** — not AHJ approval.

### Reference Table: HK Pre-Start (from 清拆 + safety appendix)
| Item | HKEDCA / practice |
|---|---|
| Contractor insurance | Before works |
| Estate renovation permit | Management office |
| Scaffold | Permitted + LD safety rules |
| Gas hob removal | Registered gas contractor |
| Fire alarm | 掛牌 before fire-related works |

### Reference Table: HKEDCA vs Statutory
| Topic | HKEDCA | Confirm with AHJ |
|---|---|---|
| Renovation permit | Estate rules | BD if structural/window statutory |
| Electrical | Trade guide | EMSD |
| Plumbing | Trade guide | WSD if applicable |
| Working at height | Safety appendix | LD |

### HKEDCA decision rules
1. Never state “compliant with HKEDCA” equals legally approved.
2. Output AHJ checklist when statutory trigger uncertain.
3. Gas, scaffold, and alarm isolate are stop-work items if missing.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-preconstruction-compliance.md` | Pre-start, permits, insurance |

### HKRG cross-reference

- Client duties before start: 保留清單, gas isolation, estate deposits (`HKRG §裝修需知/1.3`, `§1.1` items 8–9) — see `interior-site-supervision/references/hkrg-renovation-essentials-trades.md`.
- HKRG is **not** AHJ approval; clause 5 insurance waiver risk in HKRG quotation — pair with statutory insurance requirements.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: combine BO/FSD/BD/EMSD/WSD/LD with HKEDCA pre-start checklist (`§清拆/1`, `§附錄：安全建議`).
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

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

