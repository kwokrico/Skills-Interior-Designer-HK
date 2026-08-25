---
name: interior-fire-life-safety
description: >
  Egress, compartmentation, sprinkler/detector coordination, and HK scaffold/WAH safety.
  Use for fire strategy, travel distance, exit width, alarm/sprinkler interfaces, or 搭棚.
disable-model-invocation: true
---

# interior-fire-life-safety

For statutory submissions and occupancy classification, use `interior-statutory-compliance` instead.  
For ceiling/service physical clashes, use `interior-mep-clash-detection` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Egress, travel distance, exit width | `interior-fire-life-safety` | — |
| HK scaffold / WAH / 搭棚 | `interior-fire-life-safety` | `interior-site-supervision` for site sequence |
| Occupancy load / permit submissions | — | `interior-statutory-compliance` |
| Duct vs sprinkler conflicts | — | `interior-mep-clash-detection` |

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

## HK Local Practice (HKEDCA)

> Safety appendix supports **scaffold/WAH** on exterior works — verify latest LD CoP and engineer design.

### Reference Table: HK Scaffold Controls (安全建議)
| Control | Requirement |
|---|---|
| Design | Professional engineer |
| Inspection | Before first use; every 14 days; after alteration/weather |
| Weather | Stop on cyclone/monsoon signals |
| Harness anchor | ≥6 kN; no window frame / pipe anchors |
| Exclusion zone | Barricade below scaffold |

### Reference Table: Interior Fire Protection During Fit-Out
| Element | Protection |
|---|---|
| Sprinklers | Metal guards |
| Detectors | Plastic caps until commissioning |
| Alarm | 掛牌 isolate during triggering works |
| Escape signs | Film protection |

### HKEDCA decision rules
1. Scaffold non-compliance → stop exterior works immediately.
2. Special scaffold types require engineer design — guide diagrams are not design drawings.
3. Coordinate anchor access with estate management and site supervision.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-scaffolding-safety.md` | 搭棚, harness, inspections |

### HKRG cross-reference

- Estate/neighbour issues: `HKRG §裝修需知/1.1` item 9 (noise, dust, scaffold water) — not a substitute for LD/FSD scaffold rules.
- Quotation §6/§9: external works insurance and scaffold — `hkrg-standard-quotation-contract.md`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: FSD/BD for fire strategy; HKEDCA appendix for bamboo scaffold and site fire device protection during 裝修.
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
| Exterior scaffold or WAH programme on HK residential job | `interior-site-supervision` | `PERMIT CHECK -> SAFETY PLAN -> INSPECTION LOG` |
| Estate refuses anchor points for harness | `interior-statutory-compliance` | `MANAGEMENT ESCALATION -> ALTERNATIVE ANCHOR OPTIONS` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

