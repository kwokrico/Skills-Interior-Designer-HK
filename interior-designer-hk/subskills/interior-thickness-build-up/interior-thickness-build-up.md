---
name: interior-thickness-build-up
description: >
  Floor and wall build-up stacks, screed, waterproof layers, and transition leveling.
  Use for thickness mismatch, 盪地台, 英坭沙, and door threshold planning.
disable-model-invocation: true
---

# interior-thickness-build-up

For junction detailing and profiles at transitions, use `interior-interface-detailing` instead.  
For HK wet-area trade sequence gates, use `interior-site-supervision` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Build-up depth, level delta, screed/waterproof | `interior-thickness-build-up` | — |
| Threshold profile / expansion joint detail | Chain to | `interior-interface-detailing` |
| Numeric stack sum | Use | `run_interior_calculator` thickness_buildup |

## Purpose
Use for depth calculations and transition equalization across floor/wall/ceiling build-ups.

## Core Outputs
- Layer-by-layer thickness schedule.
- Delta comparison between adjacent finishes.
- Recommended correction method (recess, ramp, profile, or substitution).

## Reference Table: Common Build-Up Depths
| Assembly | Typical Total Depth |
|---|---|
| Stone + mortar bed | 30-45 mm |
| Tile + adhesive | 12-20 mm |
| Engineered timber + underlay | 12-18 mm |
| LVT + adhesive | 4-7 mm |
| Carpet + underpad | 10-18 mm |

## Decision Rules
1. Use measured substrate datum before proposing fixes.
2. Flag accessibility risk if transition creates abrupt edge.
3. Escalate interface geometry to `interior-interface-detailing`.

## HK Local Practice (HKEDCA)

> Cite `HKEDCA §坭水/*`. HK humid refurb stacks often at upper end of global depths.

### Reference Table: HK Typical Layers (坭水)
| Assembly | HKEDCA-oriented depth |
|---|---|
| Waterproof + primer | 2–5 mm (system dependent) |
| Cement screed (英坭沙) | 30–50 mm (falls in wet rooms) |
| Tile + adhesive | 12–20 mm |
| Stone + bed | 30–45 mm |

### Reference Table: Load / cure gates
| Condition | Rule |
|---|---|
| Wet screed | Barriers until strength; no storage on finish |
| Waterproof | Flood/test before tile; pave soon after cure |
| Door frame | Screed recess before frame install |

### HKEDCA decision rules
1. Measure existing slab FFL before promising flush transitions.
2. Waterproof failure → full stack review, not only finish layer.
3. Material substitutions → check annex tables in references.
4. Level delta >3 mm at wet/dry door → explicit threshold detail.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-masonry-screed-waterproof.md` | Screed, waterproof, measurement |
| `references/hkedca-material-annexes.md` | Standard residential materials |

### HKRG cross-reference

- `HKRG §裝修需知/1.7–1.8` (防水高度, 廚廁台高, 磚余量) + `§1.12` screed before floor — `hkrg-renovation-essentials-trades.md`.
- Acceptance: `HKRG §驗收指引/2.5–2.6` tile hollow 5% / fall 5–10 mm per metre — cite alongside HKEDCA where values differ.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: apply HKEDCA 坭水 build-ups and cure gates; tight flat refurbishment tolerances.
- Mainland mode: account for common local assembly standards and supplier system depths.
- If region is unknown, output conservative build-up assumptions plus verification checklist.

## Reference Table: Typology Build-Up Sensitivity
| Typology | Build-Up Sensitivity |
|---|---|
| Residential | Bathroom and balcony transition depths |
| Workplace | Lift lobby, core threshold, and raised-floor interfaces |
| Retail | Shopfront flushness and high-traffic transition durability |
| Hospitality | Wet-area detailing and premium stone leveling |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Joint/profile selection is required after buildup study | `interior-interface-detailing` | `TRANSITION TYPE -> PROFILE OPTION -> INSTALLATION NOTES` |
| Transition geometry affects accessibility comfort | `interior-anthropometrics-ergonomics` | `USER IMPACT CHECK -> CLEARANCE/COMFORT NOTES -> DIMENSION ADJUSTMENTS` |
| As-built levels deviate from design datum | `interior-site-supervision` | `FIELD MEASUREMENT PLAN -> SI CONTENT -> RECORD UPDATE ITEMS` |
| Waterproof test failed or membrane damaged | `interior-interface-detailing` | `REPAIR LAYERS -> RE-TEST -> FINISH STACK UPDATE` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

