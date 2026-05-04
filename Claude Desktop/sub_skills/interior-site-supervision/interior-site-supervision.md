# interior-site-supervision

## Purpose
Use for site walk protocols, defect management, SI drafting, and field discrepancy handling.

## Core Outputs
- Site observation record format.
- Defect/snag log with closure responsibilities.
- Site Instruction (SI) drafting guidance.

## Reference Table: Millwork Inspection Protocol
| Checkpoint | Site Verification |
|---|---|
| Grain matching | Consecutive veneer sequencing at visible runs |
| Hardware clearance | Full opening without collision or binding |
| Scribing to wall | Tight fit at uneven substrate without forced distortion |
| Joint quality | Uniform reveals and no unsupported weak edges |

## Decision Rules
1. If as-built differs from drawing, measure first, then issue SI.
2. Do not authorize workaround that breaks code or function.
3. Record all accepted deviations for as-built updates.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: use SI workflow with consultant/contractor record discipline expected in local practice.
- Mainland mode: use equivalent site instruction/technical clarification workflow per local contract administration practice.
- If region unclear, enforce field-measurement-first protocol and neutral SI log template.

## Reference Table: Typology Site Supervision Focus
| Typology | Site Priority |
|---|---|
| Residential | Wet-area detailing and finishing tolerances |
| Workplace | Ceiling-services coordination and phased handover zones |
| Retail | Launch-critical feature completion and signage readiness |
| Hospitality | Room-to-room finish consistency and defect closeout rhythm |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Joinery defect or installation tolerance issue appears | `interior-millwork-technical` | `DEFECT TYPE -> TECHNICAL ROOT CAUSE -> RECTIFICATION NOTES` |
| Site change affects egress or fire element | `interior-fire-life-safety` | `LIFE-SAFETY IMPACT -> IMMEDIATE CONTROL ACTIONS -> APPROVAL NEEDS` |
| Snag closure enters handover readiness phase | `interior-handover-dlp` | `HANDOVER READINESS CHECK -> OUTSTANDING ITEMS -> DLP SETUP` |
