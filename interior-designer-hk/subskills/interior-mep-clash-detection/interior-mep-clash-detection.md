---
name: interior-mep-clash-detection
description: >
  RCP and services coordination — ducts, sprinklers, lighting, diffusers, and ceiling zones.
  Use for ceiling clashes, service routing, and coordination hierarchy resolution.
disable-model-invocation: true
---

# interior-mep-clash-detection

For pure egress or fire-rating logic, use `interior-fire-life-safety` instead.  
For statutory permit scope, use `interior-statutory-compliance` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Ceiling / RCP / services clashes | `interior-mep-clash-detection` | — |
| Fire egress path or rating | — | `interior-fire-life-safety` |
| Acoustic baffle vs services | Pair with | `interior-acoustic-engineering` |
| HK MEP BOQ measurement | This skill + refs | `interior-tendering-qa` for package QA |

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

## HK Local Practice (HKEDCA)

> Cite `HKEDCA §水電/*`; EMSD/WSD statutory works are separate approvals.

### Reference Table: HK MEP Programme Position
| Trade | Position in sequence |
|---|---|
| 水電 | After 清拆; before 坭水 concealment |
| Wall devices | After tile wash (`§清拆/2.2` 機電) |
| Plant in plant rooms | After room finishes where guide requires |

### Reference Table: HK MEP Clash Hotspots (residential)
| Zone | Typical conflict |
|---|---|
| Bathroom ceiling | Exhaust vs downlights vs structure |
| Kitchen | Hood duct vs cabinet vs services |
| Corridor bulkhead | Drain drop vs ceiling level |
| AC | Refrigerant vs electrical vs casing |

### Reference Table: Mini-set P3 coordination cues
| Cue on drawing | Action |
|---|---|
| Clear height `+H` by zone | Compare living gypsum vs wet alu-strip soffits |
| AC niche / bulkhead | Void depth + casing vs lighting/燈槽 |
| Kitchen/bath alu strip 假天花 | Exhaust + wet downlights + access |
| Living gypsum + cove | Driver/access vs decorative trough |

Conventions: [`hk-residential-mini-tender-set.md`](../../references/cases/hk-residential-mini-tender-set.md). Flag open MEP depths beyond RCP notes before tender release → `interior-tendering-qa`.

### HKEDCA decision rules
1. Concealed works pressure-tested before plaster/tile close.
2. Do not use door frames as temporary MEP support (`§木工後期`).
3. Route measurement disputes to `interior-tendering-qa` (`§水電/6`).
4. Fire alarm isolate (**掛牌**) before works affecting detectors/sprinklers.
5. Kitchen fire-door callouts on plan/elev → chain `interior-fire-life-safety` (not solved by RCP notes alone).

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-plumbing-electrical.md` | Rough-in, testing, coordination |
| `references/hkedca-mep-measurement.md` | BOQ / 工程計算規則 |

### HKRG cross-reference

- Trade rules: `HKRG §裝修需知/1.4` (layout before rough-in, 谷磅, EMSD wire colours) + `§1.5` gas — `hkrg-renovation-essentials-trades.md`.
- Acceptance: `HKRG §驗收指引/2.1–2.3` — `hkrg-self-inspection-handover.md`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: coordinate per HKEDCA 水電 sequence; verify EMSD CoP for wiring and WSD for plumbing submissions where applicable.
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
| Ceiling void depth drives false ceiling downgrade | `interior-millwork-technical` | `RCP REVISION -> TROUGH/AC CASING ADJUSTMENT -> COORDINATION NOTES` |
| BOQ scope for chases/testing unclear | `interior-tendering-qa` | `CLARIFICATION LIST -> RISK ALLOWANCE -> DOCUMENT PATCH` |
| P3 heights/AC niche unresolved at tender | `interior-tendering-qa` | `MEP DEPTH GAP -> CLARIFICATION OR PROVISIONAL -> HOLD` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog
* [hk-residential-mini-tender-set.md](../../references/cases/hk-residential-mini-tender-set.md) — P3 heights + wet ceiling zones

