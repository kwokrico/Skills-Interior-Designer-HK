---
name: interior-anthropometrics-ergonomics
description: >
  Reach ranges, clearances, and inclusivity by user type across interior typologies.
  Use for workstation, sanitary, retail, and residential ergonomic planning.
disable-model-invocation: true
---

# interior-anthropometrics-ergonomics

For statutory accessibility compliance sign-off, use `interior-statutory-compliance` instead.  
For lighting at task surfaces, use `interior-lighting-science` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Reach, clearance, inclusive dimensions | `interior-anthropometrics-ergonomics` | — |
| Code-mandated accessibility audit | — | `interior-statutory-compliance` |
| Task illuminance at desk | Chain to | `interior-lighting-science` |

## Purpose
Use for human-dimension fit, inclusive use, and ergonomic planning standards.

## Core Outputs
- Dimension guidance by user posture and task.
- Reach/clearance checks for mixed user groups.
- Risk notes for pinch points and inaccessible layouts.

## Reference Table: Ergonomic Baseline Dimensions
| Parameter | Typical Range |
|---|---|
| Worktop height | 720-900 mm by use case |
| Seated knee clearance | 600 mm width x 450 mm depth min |
| Primary reach zone (seated) | Approx. 350-550 mm from body |
| Accessible turning area | 1500 mm diameter preferred |

## Decision Rules
1. Prioritize function and inclusivity before styling decisions.
2. Validate clearances at doors, corners, and furniture pinch points.
3. Route statutory accessibility checks to `interior-statutory-compliance`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align accessibility expectations with local enforcement and project brief standards.
- Mainland mode: align with PRC accessibility implementation standards and local approval expectations.
- If region unclear, apply conservative inclusive dimensions and flag jurisdiction confirmation needed.

## Reference Table: Typology Ergonomic Priorities
| Typology | Ergonomic Focus |
|---|---|
| Residential | Kitchen/workflow reach and bathroom transfer comfort |
| Workplace | Desk posture range and circulation around collaboration zones |
| Retail | Queue comfort, fitting-room usability, and checkout access |
| Hospitality | Guest comfort, luggage movement, and intuitive room ergonomics |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Accessibility/code confirmation is required | `interior-statutory-compliance` | `ACCESS CHECKLIST -> CODE GAP NOTES -> REQUIRED CORRECTIONS` |
| Ergonomic clearances depend on joinery/edge detailing | `interior-interface-detailing` | `CLEARANCE CONSTRAINT -> DETAIL ADJUSTMENT -> TRANSITION NOTES` |
| Visual comfort materially impacts usability | `interior-lighting-science` | `VISUAL COMFORT ISSUE -> LIGHTING ADJUSTMENTS -> TARGET SETTINGS` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

