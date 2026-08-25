---
name: interior-handover-dlp
description: >
  Handover readiness, O&M completeness, as-built verification, and DLP tracking.
  Use for 交收, 驗收, 自助驗收, snag closeout, and defect liability.
disable-model-invocation: true
---

# interior-handover-dlp

For active site defects and SI during construction, use `interior-site-supervision` instead.  
For tender contract DLP clauses, use `interior-tendering-qa` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Handover checklist, O&M, DLP log | `interior-handover-dlp` | — |
| HKRG owner self-inspection / 驗收指引 | This skill + refs | — |
| Active site rework / protection | — | `interior-site-supervision` |
| HKRG payment retention / clause 12 | — | `interior-tendering-qa` |

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

## HK Local Practice (HKEDCA)

> Industry guide only. Cite `HKEDCA §交收/*` and `§雜項/*`.

### Reference Table: HK Cleaning Sequence (交收)
| Stage | Order / rule |
|---|---|
| Masonry snag | 坭水執爛 first |
| Tile clean | 內隴 → 外層 → 幼清 (approved cleaners only) |
| Rough clean | Water-sensitive joinery/switches after rough clean |
| Fine clean | After fixtures/kitchen complete; unit locked |
| Direction | Outside-in, top-down; shoe covers; padded ladders |

### Reference Table: HK Acceptance Methods (驗收)
| Method | Use for |
|---|---|
| 目測 Visual | All finishes |
| 耳聽 Sound | Hollow plaster, loose render |
| 腳踏 Foot | Timber floor adhesion |
| 平水尺 Level | Sloping floors, sills, frames |
| 灑水 Water | Wet areas, screens, windows (with management approval) |

### Reference Table: HK Handover Defect Thresholds (examples)
| Item | Criteria |
|---|---|
| Timber floor gap/level | ≤1 mm adjacent boards |
| Plaster hollow grid | Tap ≤300 mm; repair per guide tables |
| Plaster tolerance | 3–5 mm verticality/flatness typical |

### HKEDCA decision rules
1. No practical completion without 交收 cleaning stages complete.
2. DLP log must map to acceptance test method used.
3. Misc fixtures (潔具/燈具/掣面/窗台石/五金) verified before sign-off.
4. Repeat leaks → water test + waterproof review chain.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-handover-acceptance.md` | 交收, cleaning, acceptance checklist |
| `references/hkedca-misc-fixtures.md` | Final fixture install and measurement |

## HK Local Practice (HKRG)

> Part 2 **驗收指引** (自助驗收). Cite `HKRG §驗收指引/*`. If contract adopts HKRG clause 23, use Part 2 as acceptance standard.

### Reference Table: HKRG ↔ HKEDCA acceptance crosswalk
| HKRG § | Topic | HKEDCA method | Notes |
|---|---|---|---|
| 2.5 | Tiles | 目測 @1m | HKEDCA allows 5% hollow per 100 ft² — align contract |
| 2.6 | Plaster | Visual + hollow | HKEDCA tap grid ≤300 mm |
| 2.12 | Timber floor | Foot + visual | HKEDCA: ≤1 mm gap/level adjacent boards |
| 2.4 | Doors | Gap 2–5 mm frame; 3–6 mm floor | HKEDCA door operation + hardware |
| 2.15 | Clean | Visual | HKEDCA cleaning **sequence** still applies |

### Reference Table: DLP register — add HKRG field
| Field | Content |
|---|---|
| HKRG checklist ref | e.g. `HKRG §驗收指引/2.8` item 5 |
| Contract basis | HKRG clause 12 months + 3-month repair window from notice |

### HKRG decision rules
1. If contract references HKRG only: walk Part 2 room-by-room before practical completion.
2. If contract references HKEDCA 交收: require **both** HKRG Part 2 pass and HKEDCA cleaning stages complete.
3. On numeric conflict (e.g. tile hollow %), cite both sources; contract precedence wins.
4. Snag holdback per HKRG quotation clause 10 may apply to final payment.

### HKRG Source Pointers
| File | Load when |
|---|---|
| `references/hkrg-self-inspection-handover.md` | Full §2.1–2.15 checklists |

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align handover to HKRG Part 2 (if adopted) **and** HKEDCA 交收 methods; use `§交收/5–6` where contract references HKEDCA.
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
| Protection damage found during final clean | `interior-site-supervision` | `DAMAGE LOG -> SI -> REWORK BEFORE SIGNOFF` |
| Hollow plaster or waterproof test fail | `interior-interface-detailing` | `DEFECT LOCATION -> REPAIR SPEC -> RE-TEST PLAN` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

