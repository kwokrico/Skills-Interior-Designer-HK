# interior-lighting-science

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

## Decision Rules
1. Avoid visual comfort issues from glare or excessive contrast.
2. Always coordinate fixture depth and driver locations with ceiling services.
3. Route service conflicts to `interior-mep-clash-detection`.

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
| Fixture depth or routing conflict appears | `interior-mep-clash-detection` | `SERVICE CONFLICT MAP -> REVISED FIXTURE ZONES -> COORDINATION ACTIONS` |
| Acoustic system changes photometric behavior | `interior-acoustic-engineering` | `ACOUSTIC-LIGHT INTERFACE -> PERFORMANCE IMPACT -> COMPENSATION STRATEGY` |
| Illuminated signage or identity element is involved | `interior-brand-environmental-graphics` | `SIGNAGE INTENT -> LEGIBILITY CRITERIA -> LIGHTING INTEGRATION NOTES` |
