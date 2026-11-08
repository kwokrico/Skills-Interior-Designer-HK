---
name: interior-lighting-science
description: >
  Illuminance, CCT, CRI, UGR, and fixture-driver coordination for interior spaces.
  Use for lighting quality targets and glare control by typology.
disable-model-invocation: true
---

# interior-lighting-science

For HK application of overseas textbook examples, read [Hong Kong adaptation](../../references/ching-hk-adaptation.md): accessibility/legal status, fire/stairs/barriers, daylight, services, energy, IAQ and certification. Confirm scope and edition before adopting a dimension or performance claim.

For ceiling/service conflicts with luminaires, use `interior-mep-clash-detection` instead.  
For numeric lux/fixture count estimates, use `run_interior_calculator` lux_targeting.

### Maintained-lighting calculation basis

Use `E_maintained = E_initial × MF_total`, with one supported overall maintenance factor. CIE includes lamp output decline and dirt on luminaires/room surfaces in MF; IES uses LLF for a wider loss allowance, not simply lamp lumen maintenance. Define each component and count it once. Sources checked 2026-11-07: [CIE definition](https://cie.co.at/eilv/753), [IES definition](https://ies.org/definitions/light-loss-factor-llf/).

The calculator requires explicit `target_lux` (maintained) and `maintenance_factor` (overall); a separate `llf` input is rejected because its overlap is unknown. A fixture estimate additionally needs `room_area_m2`, `lumens_per_fixture` and `utilization_factor`. Do not invent these inputs. The lumen-method estimate does not establish distribution, glare, uniformity, screen comfort or compliance; obtain actual photometry, geometry, maintenance programme and commissioning evidence. Initial 500 lux alone does not prove 500 lux maintained.

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

HKRIDA Products and Materials chapter 10 ([archived source](../../../Reference/SS/HKRIDA/application_20200331_3y12O-compressed.pdf), PDF pp. 44–73) supplements the numerical targets: consider daylight, direct/indirect distribution, beam/aiming, glare, contrast, surface reflectance/texture and the change of scenes through use/time. Review actual materials under the proposed light. Illuminance is incident flux per area (lux); luminance describes light leaving a surface toward a viewer (cd/m²). Do not copy the book's conflated terminology or historical lamp tables as current product performance.

For luminaire selection record tag/location/quantity, manufacturer/model, distribution/photometric data, output and power, CCT/colour rendering, mounting/cutout/depth, finish, driver/control compatibility and access, environmental rating and any emergency role. Verify a product's data and maintainability; lamp wattage or a rendering alone cannot establish task illuminance or visual comfort.
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

## Spatial design and furnishing reference

When the brief concerns composition, visual hierarchy, furniture grouping, storage planning or window coverings, read the relevant shared reference:

- [spatial composition](../../references/ching-spatial-composition.md)
- [furnishings and window treatments](../../references/ching-furnishings-and-window-treatments.md)


For retained appliances, shower controls/screens, smart sockets, drainage or cabinet lighting, read [deco-fixtures-and-retained-services](../../references/deco-fixtures-and-retained-services.md).
