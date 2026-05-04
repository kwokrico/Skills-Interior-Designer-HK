# interior-mep-clash-detection

## Purpose
Use for detecting and resolving physical/service clashes between ceiling intent and MEP systems.

## Core Outputs
- Clash matrix by zone (public, back-of-house, critical routes).
- Resolution options with consequences on height, cost, and maintenance access.
- Sequenced coordination instructions for consultants/trades.

## Reference Table: Clash Priority Hierarchy
| Priority | System |
|---|---|
| 1 | Fire/Life Safety (FS) |
| 2 | Plumbing and Drainage (P&D) |
| 3 | HVAC |
| 4 | Electrical/ELV |
| 5 | Decorative/aesthetic ceiling intent |

## Decision Rules
1. Route with `interior-fire-life-safety` when prompt includes egress, sprinklers, or smoke logic.
2. Preserve inspection and maintenance clearances for valves, dampers, and access panels.
3. Document the selected compromise (height, reroute, or system swap) with rationale.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: coordinate against FSD acceptance constraints and local service authority expectations.
- Mainland mode: align with PRC code path and local institute submission requirements.
- If unknown jurisdiction, issue dual-track clash resolution notes and mark code confirmation pending.

## Reference Table: Typology Clash Hotspots
| Typology | Typical Clash Zone |
|---|---|
| Residential | Corridor bulkheads and bathroom service drops |
| Workplace | Open office ceiling raft + sprinkler grid + VAV routes |
| Retail | Feature ceilings at storefront zones with dense services |
| Hospitality | Lobby feature lighting zones and BOH service transfer points |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Sprinkler or egress element is affected | `interior-fire-life-safety` | `LIFE-SAFETY IMPACT -> NON-NEGOTIABLE CONSTRAINTS -> ACCEPTABLE OPTIONS` |
| Fixture depth or glare strategy changes due to rerouting | `interior-lighting-science` | `LIGHTING IMPACT -> PHOTOMETRIC ADJUSTMENTS -> COORDINATION NOTES` |
| Soffit/joint expression changes after clash resolution | `interior-interface-detailing` | `INTERFACE DETAIL INTENT -> JOINT STRATEGY -> TOLERANCE NOTES` |
