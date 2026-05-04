# interior-fire-life-safety

## Purpose
Use for interior fire strategy, egress checks, compartment interface, and sprinkler/fire alarm coordination.

## Core Outputs
- Egress path logic with travel distance assumptions.
- Exit width and door swing compliance notes.
- Interior finish fire-performance checks by occupancy type.
- Coordination checklist between interior package and life-safety systems.

## Reference Table: Egress Baseline Checks
| Item | Baseline Rule |
|---|---|
| Exit access | Maintain continuous unobstructed route to final exit. |
| Door leaf impact | Verify door swing does not reduce required egress width. |
| Dead-end condition | Flag and propose alternative escape path where required by AHJ. |
| Decorative features | Do not compromise sprinkler throw, detector coverage, or signs. |

## Decision Rules
1. Life safety always overrides aesthetics.
2. If uncertain on local code number, state AHJ verification required.
3. When ceiling design conflicts with services, escalate to `interior-mep-clash-detection`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: use BO/FSD practice assumptions and verify latest FSD acceptance criteria.
- Mainland mode: use PRC national/local fire code pathway and local fire authority review workflow.
- If project location is unclear, provide both pathways side-by-side and request jurisdiction confirmation.

## Reference Table: Typology Fire Focus
| Typology | Primary Fire-Life-Safety Focus |
|---|---|
| Residential | Protected escape route continuity and door/corridor clear widths |
| Workplace | Occupant load, exit distribution, and floor evacuation logic |
| Retail | Peak crowd scenarios and escape path visibility |
| Hospitality | Back-of-house separation and guest route legibility |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Occupancy load or accessibility requirement appears | `interior-statutory-compliance` | `ASSUMPTIONS -> COMPLIANCE GAP LIST -> REQUIRED CODE CHECKS` |
| Ceiling, ducts, sprinklers, detector conflict appears | `interior-mep-clash-detection` | `CLASH MATRIX -> PRIORITY ORDER -> RESOLUTION OPTIONS` |
| As-built deviation impacts egress intent | `interior-site-supervision` | `FIELD CHECKLIST -> SI DRAFT POINTS -> DRAWING UPDATE NOTES` |
