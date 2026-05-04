# interior-sustainability-wellness

## Purpose
Use for sustainability and wellness-driven interior choices across material, air, light, and occupant experience.

## Core Outputs
- Low-impact material strategy (VOC, recycled, durability).
- Wellness-focused design recommendations (air, light, comfort, biophilia).
- Credit-alignment guidance (LEED/WELL/BEAM Plus style frameworks).

## Reference Table: Wellness Design Controls
| Domain | Practical Control |
|---|---|
| Materials | Low-VOC paints, adhesives, sealants |
| Air quality | Source control + ventilation strategy coordination |
| Light | Circadian-supportive CCT/intensity by time/use |
| Nature connection | Biophilic elements with maintainable species selection |

## Decision Rules
1. Prefer measurable performance over purely narrative claims.
2. Ensure sustainable alternatives still meet durability and code.
3. Coordinate with procurement for availability and lead-time risk.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align with project-selected sustainability framework and local material availability constraints.
- Mainland mode: align with PRC implementation standards and local certification pathways.
- If region unclear, provide framework-agnostic performance strategy and tag regional credits for confirmation.

## Reference Table: Typology Sustainability Focus
| Typology | Sustainability/Wellness Focus |
|---|---|
| Residential | Low-VOC finishes and healthy indoor baseline comfort |
| Workplace | IAQ strategy, visual comfort, and occupant wellness metrics |
| Retail | Durable low-impact materials for high-traffic turnover |
| Hospitality | Wellness narrative with maintainable biophilic integration |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| EPD/VOC/supply certainty data is required | `interior-material-procurement` | `MATERIAL DATA REQUEST -> COMPLIANCE EVIDENCE -> PROCUREMENT RISK` |
| Circadian-supportive lighting strategy is needed | `interior-lighting-science` | `WELLNESS LIGHTING TARGETS -> FIXTURE/CONTROL STRATEGY -> PERFORMANCE NOTES` |
| Sustainability intent is challenged by budget pressure | `interior-value-engineering` | `SUSTAINABILITY-VE MATRIX -> TRADE-OFF NOTES -> RECOMMENDED OPTION` |
