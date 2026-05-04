# interior-value-engineering

## Purpose
Use for budget alignment through technically valid alternatives that preserve core design intent.

## Core Outputs
- Good-Better-Best option set per cost hotspot.
- Cost/risk/performance comparison narrative.
- Recommendation with scope impact and approval note.

## Reference Table: Good-Better-Best Protocol
| Tier | Definition |
|---|---|
| Good | Meets minimum performance and code at lowest cost |
| Better | Balanced cost with improved durability/appearance |
| Best | Highest performance/longevity with premium cost |

## Decision Rules
1. Never downgrade below compliance or functional requirement.
2. State what design quality is preserved vs traded off.
3. Coordinate sourcing feasibility with `interior-material-procurement`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: prioritize alternatives with proven local installer familiarity and supply certainty.
- Mainland mode: prioritize alternatives with compliant local certification and stable regional supply.
- If region unknown, provide options tagged by import dependence and approval risk.

## Reference Table: Typology VE Strategy
| Typology | Preferred VE Direction |
|---|---|
| Residential | Optimize hidden substrates before visible signature elements |
| Workplace | Standardize repeated modules to reduce fabrication variance |
| Retail | Protect customer-facing finishes; value engineer back-of-house first |
| Hospitality | Protect brand-defining touchpoints; optimize secondary zones |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| VE option requires real lead-time and batch validation | `interior-material-procurement` | `SUPPLY CHECK -> LEAD-TIME DELTA -> ACCEPT/REJECT RATIONALE` |
| VE change requires reissue or clarification | `interior-tendering-qa` | `DOCUMENT IMPACT LIST -> REISSUE SCOPE -> CLARIFICATION TEXT` |
| VE option touches code-sensitive element | `interior-statutory-compliance` | `COMPLIANCE RISK -> REQUIRED CHECKS -> CONDITIONAL APPROVAL NOTES` |
