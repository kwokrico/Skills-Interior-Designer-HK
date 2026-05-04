# interior-thickness-build-up

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

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: account for refurbishment constraints and tight slab tolerance realities.
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
