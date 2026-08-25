---
name: interior-millwork-technical
description: >
  Joinery carcass, hardware loads, ventilation for enclosed AV/electrical, HK carpentry trades.
  Use for 假天花, 燈槽, 廚櫃, 木門, 木地板, and bespoke millwork.
disable-model-invocation: true
---

# interior-millwork-technical

For floor finish transitions at joinery bases, use `interior-interface-detailing` instead.  
For site inspection and SI workflow, use `interior-site-supervision` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Joinery, cabinets, doors, timber floor tech | `interior-millwork-technical` | — |
| Interface thresholds at millwork | Pair with | `interior-interface-detailing` |
| Field defect / SI | — | `interior-site-supervision` |

## Purpose
Use for cabinetry/joinery technical resolution including carcass logic, hardware selection, and service integration.

## Core Outputs
- Joinery technical notes by element type.
- Hardware suitability checks (load, cycles, clearance).
- Ventilation and access provisions for enclosed equipment.

## Reference Table: Millwork QA Essentials
| Item | Check |
|---|---|
| Door and drawer clearances | No binding at full opening; handle conflict resolved |
| Hinge/runner capacity | Rated for panel/drawer weight with safety margin |
| Carcass material | Moisture-resistant grade in wet/service environments |
| AV/electrical joinery | Passive/active ventilation and maintenance access |

## Decision Rules
1. Do not finalize without dimensional coordination to site conditions.
2. For bespoke components, require detail at 1:10 or 1:5.
3. Coordinate visible interfaces with `interior-interface-detailing`.

## HK Local Practice (HKEDCA)

> Cite `HKEDCA §木工前期/*`, `§木工後期/*`.

### Reference Table: HK Joinery Gates (木工後期/3)
| Prerequisite | Status required |
|---|---|
| Plaster (批盪) | Dry |
| Concealed MEP | Complete and approved |
| Timber flooring | Windows glazed |

### Reference Table: HK Door Frame Fixing (summary)
| Item | Rule |
|---|---|
| First fix height | 250 mm from head/base |
| Tall frames | Extra fix if >2300 mm |
| Masonry tolerance | ≤2 mm to frame or contractor remakes door |
| MEP support | Forbidden as temporary frame bracing |

### Reference Table: HK Early Carpentry Items
| Item | Coordinate with |
|---|---|
| 燈槽 | Lighting + MEP |
| 冷氣機殼 | AC equipment + external sleeve |
| 假天花 | Sprinklers, detectors, diffusers |

### HKEDCA decision rules
1. No fixed cabinets until MEP + dry plaster gate passed.
2. Hollow/solid door specs per BOQ — lock block and edge band rules apply.
3. Glass after scaffold removal.
4. Site-fit always before shop drawing finalization in HK refurb.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-carpentry-early.md` | Ceiling, troughs, AC box |
| `references/hkedca-carpentry-late-doors-flooring.md` | Doors, floors, glass |

### HKRG cross-reference

- `HKRG §裝修需知/1.9–1.13` joinery, doors, ceiling, floor — `hkrg-renovation-essentials-trades.md`.
- Acceptance: `HKRG §驗收指引/2.7–2.8`, `2.11–2.12` — `hkrg-self-inspection-handover.md`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: HKEDCA joinery gates, moisture zones, and frame tolerance rules (`§木工後期`).
- Mainland mode: emphasize factory prefabrication interfaces and production tolerances by vendor.
- If region not set, provide neutral hardware/performance criteria and require supplier shop-drawing validation.

## Reference Table: Typology Millwork Focus
| Typology | Millwork Priority |
|---|---|
| Residential | Wardrobe/storage efficiency and moisture-prone zone durability |
| Workplace | Pantry/file/storage robustness and service access |
| Retail | Display durability, replaceable components, and lighting integration |
| Hospitality | Premium finish continuity and housekeeping resilience |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Joinery termination detail remains unresolved | `interior-interface-detailing` | `EDGE CONDITION -> JOINT DETAIL OPTIONS -> FINISH COORDINATION NOTES` |
| Veneer/hardware availability or lead-time issue appears | `interior-material-procurement` | `SUPPLY RISK -> SUBSTITUTE OPTIONS -> PROGRAM IMPACT` |
| Mockup review or installation QA sequencing is needed | `interior-site-supervision` | `MOCKUP CHECKLIST -> SITE QA STEPS -> DEFECT PREVENTION NOTES` |
| MEP rough-in incomplete but joinery pressured | `interior-mep-clash-detection` | `HOLD POINT -> REQUIRED MEP SIGNOFF -> REVISED PROGRAMME` |
| Floor level/stack conflicts at door threshold | `interior-thickness-build-up` | `BUILD-UP ADJUSTMENT -> FRAME SILL DETAIL -> RE-CHECK` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

