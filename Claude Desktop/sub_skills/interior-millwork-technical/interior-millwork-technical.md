# interior-millwork-technical

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

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: emphasize site-fit tolerance, moisture resistance, and compact-space serviceability.
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
