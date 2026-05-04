# interior-brand-environmental-graphics

## Purpose
Use for integrating branding, wayfinding, and environmental graphics into interior architecture.

## Core Outputs
- Signage hierarchy and placement logic.
- Brand expression guidelines tied to physical touchpoints.
- Coordination notes for visibility, durability, and maintenance.

## Reference Table: Wayfinding Hierarchy
| Layer | Role |
|---|---|
| Identity signs | Confirm arrival and place identity |
| Directional signs | Guide decision points and circulation |
| Informational signs | Provide contextual or operational info |
| Regulatory signs | Mandatory compliance/safety messaging |

## Decision Rules
1. Wayfinding clarity outranks decorative complexity.
2. Verify readable contrast, placement height, and viewing distance.
3. Coordinate sign power/data and fixing with relevant disciplines.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: verify bilingual or project-mandated language conventions and local sign controls.
- Mainland mode: verify local language/signage conventions and landlord/authority approval pathways.
- If region unclear, provide neutral wayfinding hierarchy and mark local language/regulatory checks required.

## Reference Table: Typology EGD Strategy
| Typology | EGD Priority |
|---|---|
| Residential | Minimal, intuitive navigation in shared/common zones |
| Workplace | Departmental wayfinding and visitor journey clarity |
| Retail | Brand storytelling + conversion-oriented path cues |
| Hospitality | Arrival sequence, amenity navigation, and calm orientation |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Illuminated graphic or sign legibility issue appears | `interior-lighting-science` | `LEGIBILITY ISSUE -> LIGHTING TUNING -> VISUAL VALIDATION NOTES` |
| Signage intersects mandatory safety/code requirement | `interior-statutory-compliance` | `CODE INTERFACE CHECK -> REQUIRED SIGN TYPES -> COMPLIANCE NOTES` |
| Fabrication durability/replacement strategy is needed | `interior-material-procurement` | `MATERIAL DURABILITY OPTIONS -> REPLACEMENT PLAN -> LEAD-TIME RISK` |
