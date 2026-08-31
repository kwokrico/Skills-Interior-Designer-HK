---
name: interior-lighting-science
description: >
  Illuminance, CCT, CRI, UGR, and fixture-driver coordination for interior spaces.
  Use for lighting quality targets and glare control by typology.
disable-model-invocation: true
---

# interior-lighting-science

For ceiling/service conflicts with luminaires, use `interior-mep-clash-detection` instead.  
For numeric lux/fixture count estimates, use `run_interior_calculator` lux_targeting.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Lux, CCT/CRI/UGR, layering strategy | `interior-lighting-science` | — |
| RCP vs duct/sprinkler clash | — | `interior-mep-clash-detection` |
| Maintained lux / fixture count | Use calculator | `lux_targeting` |
| Acoustic baffle blocks light | Pair with | `interior-acoustic-engineering` |

## HK Local Practice

- HK residential: coordinate with `interior-millwork-technical` for 燈槽 and false ceiling zones.
- Pair with HKEDCA carpentry early-stage refs when lighting is embedded in 假天花.
- P3 legend conventions: [`hk-residential-mini-tender-set.md`](../../references/cases/hk-residential-mini-tender-set.md).

## Purpose
Use for performance-led lighting design decisions, including quality metrics and coordination constraints.

## Core Outputs
- Lighting intent by layer (ambient/task/accent).
- CCT/CRI/UGR recommendations by function.
- Driver/control and maintenance access coordination notes.

## Reference Table: Lighting Quality Targets
| Use Case | Typical Target |
|---|---|
| Office task area | 300-500 lux, CRI 80+, controlled glare |
| Retail highlight | 500-1000 lux with accent contrast |
| Hospitality dining | 100-250 lux, warm CCT with dimming |
| Residential living | 100-300 lux layered scene strategy |

## Reference Table: HK residential P3 legend (mini-set)
| Symbol role | Layer | Notes |
|---|---|---|
| Panel / pendant | Ambient | Living/bedroom centrepiece |
| Wet-rated recessed downlight | Ambient (wet) | Kitchen/bath 假天花 — moisture/IP note |
| Accent recessed spot | Accent | Decorative living layer |
| Cove / 燈槽 + LED strip | Wash / 滲光 | Coordinate trough depth with MEP |
| Curtain track | — | Window-head clash check |

Clear heights as `+H` on P3; wet ceilings typically lower than living `+2800`-class soffits.

## Decision Rules
1. Avoid visual comfort issues from glare or excessive contrast.
2. Always coordinate fixture depth and driver locations with ceiling services.
3. Route service conflicts to `interior-mep-clash-detection`.
4. Wet recessed fixtures: require moisture/IP callout; do not copy dry-zone fixtures into bath/kitchen without review.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: account for compact ceiling zones and maintenance access constraints common in fit-out works.
- Mainland mode: align fixture/driver standards with local supply and certification availability.
- If region unclear, provide universal performance targets and flag code-specific lighting checks.

## Reference Table: Typology Lighting Priorities
| Typology | Lighting Priority |
|---|---|
| Residential | Layered scenes and warm comfort lighting |
| Workplace | Task uniformity with glare control and visual comfort |
| Retail | Accent hierarchy and merchandise color fidelity |
| Hospitality | Atmosphere control with dimming and focal rhythm |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Material schedule LG lines need CCT/CRI/IP or driver-access review | `interior-material-procurement` | `SCHEDULE LG SPEC -> PHOTOMETRIC/IP CHECK -> ACCESS NOTES` |
| Fixture depth or routing conflict appears | `interior-mep-clash-detection` | `SERVICE CONFLICT MAP -> REVISED FIXTURE ZONES -> COORDINATION ACTIONS` |
| Acoustic system changes photometric behavior | `interior-acoustic-engineering` | `ACOUSTIC-LIGHT INTERFACE -> PERFORMANCE IMPACT -> COMPENSATION STRATEGY` |
| Illuminated signage or identity element is involved | `interior-brand-environmental-graphics` | `SIGNAGE INTENT -> LEGIBILITY CRITERIA -> LIGHTING INTEGRATION NOTES` |
| Tender P3 legend incomplete vs package release | `interior-tendering-qa` | `LEGEND GAP -> CLARIFICATION -> HOLD OR ADDENDA` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog
* [hk-residential-mini-tender-set.md](../../references/cases/hk-residential-mini-tender-set.md) — P3 legend + height markers

