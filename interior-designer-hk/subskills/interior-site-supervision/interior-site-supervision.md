---
name: interior-site-supervision
description: >
  Site walks, defect management, SI drafting, HK trade sequence, and protection matrix.
  Use for 裝修, 清拆, 判頭 coordination, 執漏, and field discrepancies.
disable-model-invocation: true
---

# interior-site-supervision

For handover O&M and DLP registers, use `interior-handover-dlp` instead.  
For statutory permit scope, use `interior-statutory-compliance` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site defects, SI, HK sequence/protection | `interior-site-supervision` | — |
| HKRG client/contractor duties (裝修需知) | This skill + refs | `interior-tendering-qa` for contract |
| Practical handover / cleaning / 交收 | Pair with | `interior-handover-dlp` |
| Scaffold engineering detail | Pair with | `interior-fire-life-safety` |

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

## HK Local Practice (HKEDCA)

> Industry guide only — not statutory law. Cite `HKEDCA §{section}`; verify estate and AHJ rules.

### Reference Table: HK Demolition & Pre-Start (清拆)
| Item | Requirement (HKEDCA) |
|---|---|
| Insurance | In place before works (`§清拆/1`, ~p.6) |
| Estate application | Renovation, scaffolding (搭棚) via management office |
| Retained items | Owner confirmation before demolition |
| Gas hob | Registered gas contractor only |
| Early procurement | Aluminium windows, split AC, tiles with owner at demolition stage |

### Reference Table: HK Trade Sequence Gates
| Next trade | Site hold point |
|---|---|
| 水電 | Demolition complete; protection of retained elements |
| 坭水 | MEP rough-in inspected |
| 木工前期 | Wet-area waterproof tested where required |
| 木工後期 | Plaster dry + concealed MEP complete |
| 交收 | All trades complete; cleaning per 交收 sequence |

### Reference Table: Protection Priority (Top failures)
| Element | Control |
|---|---|
| 防水 | Barriers; pave soon after cure |
| 窗框 | Keep factory film until final clean |
| 盪地台 | No load until strength; signage while wet |
| 木地板 | Glass in windows before floor works |

### HKEDCA decision rules
1. Protection failure → SI + identify downstream trades affected before rework quote.
2. Wrong demolition → stop; record; reinstatement per contract.
3. Enforce late install of doors (except main/kitchen) and cabinet doors/hardware.
4. Fire works only after management **掛牌** alarm isolate.
5. Photo record at trade handover boundaries.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-demolition-protection.md` | Demolition, waste, demolition BOQ |
| `references/hkedca-site-protection-matrix.md` | Any protection dispute or programme risk |

## HK Local Practice (HKRG)

> Client–contractor process guide. Cite `HKRG §裝修需知/*`. Index: [Reference/HKRG-INDEX.md](../../../Reference/HKRG-INDEX.md).

### Reference Table: HKRG client vs contractor (§1.1 highlights)
| Topic | 客方 | 承辦方 |
|---|---|---|
| Decisions | Confirm in WhatsApp/record | Keep aligned records |
| Owner materials | Buy and deliver on time | Remind procurement deadlines |
| Variations | Agree price + date before work; notify insurer for 後加 | Quote VO before starting |
| Completion | Allow aesthetic 執漏 post handover if functional OK | Deliver reasonable occupation standard |
| Site access | Pre-notify visits; pay estate deposits | Work Mon–Fri 9–6 unless agreed (extra cost) |

### Reference Table: 額外工程費 red flags (by trade)
| Trade | Typical trigger (see trades file) |
|---|---|
| 清拆 | Extra floor layer; retain old MEP |
| 水電 | DB relocate, extra points, concealed cistern |
| 泥水 | Special tiles, screed before timber |
| 訂造傢俬 | Special finishes, hardware upgrades |
| 油漆 | Scrape to concrete, >3 colours |

### HKRG decision rules
1. SI must state whether item is 包料 or 客方 supply and who signs third-party deliveries.
2. Stop-work if retention list (保留清單) or gas isolation not done before demolition (`HKRG §1.3`).
3. No site change after client-confirmed sequence without written VO (`HKRG §1.1` items 3–5).
4. Pair with HKEDCA for protection matrix and trade hold points.

### HKRG Source Pointers
| File | Load when |
|---|---|
| `references/hkrg-renovation-essentials.md` | §1.1 overall, adoption, HKRG vs HKEDCA |
| `references/hkrg-renovation-essentials-trades.md` | Per-trade 一般需知 / 另收費 |

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: use SI workflow with consultant/contractor record discipline; apply HKEDCA trade sequence (`§清拆`–`§交收`) and protection matrix (`§清拆/2.1–2.2`).
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
| Waterproof or screed protection breached | `interior-interface-detailing` | `DAMAGE ASSESSMENT -> REWORK SCOPE -> PROTECTION REINSTATEMENT` |
| Door frame tolerance >2 mm to masonry finish | `interior-millwork-technical` | `FRAME REMEDY -> TRADE COST ALLOCATION -> RE-INSPECTION` |
| Scaffold / WAH non-compliance observed | `interior-fire-life-safety` | `STOP WORK -> SAFETY CORRECTIVE ACTIONS -> RESUME CRITERIA` |
| 額外工程費 / scope dispute on site | `interior-tendering-qa` | `HKRG TRADE TRIGGER -> VO STATUS -> COST/TIME IMPACT` |
| Owner disputes acceptance criterion | `interior-handover-dlp` | `HKRG §驗收指引 ITEM -> EVIDENCE -> RECTIFICATION PLAN` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

