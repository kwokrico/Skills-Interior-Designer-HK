---
name: interior-interface-detailing
description: >
  Transition joints, thresholds, shadow gaps, expansion joints, and waterproof interfaces.
  Use for material transitions, protection during works, and failure-prone junctions.
disable-model-invocation: true
---

# interior-interface-detailing

For total floor/wall build-up stacks and leveling, use `interior-thickness-build-up` instead.  
For joinery carcass and hardware, use `interior-millwork-technical` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Thresholds, joints, waterproof transitions | `interior-interface-detailing` | — |
| Total build-up depth / screed stacks | — | `interior-thickness-build-up` |
| Cabinet scribing / hardware | — | `interior-millwork-technical` |
| HK paint protection during works | This skill + refs | `interior-site-supervision` for sequence |

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

## HK Local Practice (HKEDCA)

> Cite `HKEDCA §坭水/4`, `§油漆/*`, `§木工後期` bathroom details.

### Reference Table: HK Wet/Dry & Paint Interfaces
| Interface | HKEDCA-oriented detail |
|---|---|
| Bathroom door frame | Waterproof sealant ~1.5 m at frame/jamb |
| Wet membrane | Continuous to threshold; test before tile |
| Fresh paint | Canvas on floors; 油漆未乾 signage; close windows before rain |
| Tile/stone edges | Protection until handover — joint trim as per traffic |

### Reference Table: HK Protection → Detail Link
| Site issue | Detail response |
|---|---|
| Trafficked waterproofing | Re-test + repair spec before finish |
| Paint on finished tile | Approved cleaners only at 幼清 |
| Frame ±2 mm masonry mismatch | Remake frame — detail not shim-only |

### HKEDCA decision rules
1. Wet-to-dry transitions always detailed when delta >3 mm.
2. Paint stage cannot compromise cured waterproof or stone edges.
3. Sealant at bath/wet room per late carpentry + 交收 neatness criteria.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-waterproof-transitions.md` | Wet rooms, thresholds, bath frame |
| `references/hkedca-paint-protection.md` | Paint cycles and interfaces |

### HKRG cross-reference

- `HKRG §裝修需知/1.10` paint limits (剷底, shrinkage, colour count) — `hkrg-renovation-essentials-trades.md`.
- Acceptance: `HKRG §驗收指引/2.9–2.10` — visual @1 m; pair with HKEDCA cleaning before final paint sign-off.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: humid-climate durability per HKEDCA protection and 交收 cleaning constraints.
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
| Handover rejects sealant or grout appearance | `interior-handover-dlp` | `ACCEPTANCE CRITERIA -> REWORK SCOPE -> RE-INSPECTION` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

