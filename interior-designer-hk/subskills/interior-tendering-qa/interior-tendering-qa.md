---
name: interior-tendering-qa
description: >
  Pre-tender package completeness, BOQ alignment, and bid-ready QA.
  Use for HKEDCA measurement rules, HKRG 標準報價單, and tender risk flags.
disable-model-invocation: true
---

# interior-tendering-qa

For site execution of contract terms, use `interior-site-supervision` instead.  
For handover acceptance criteria, use `interior-handover-dlp` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Tender completeness, BOQ, HKRG quote | `interior-tendering-qa` | — |
| Buildability detail gaps | Route unresolved to | relevant technical sub-skill |
| Owner snag walk / 驗收指引 | — | `interior-handover-dlp` |
| Payment dispute on site | Pair with | `interior-site-supervision` |

## Purpose
Use for pre-tender quality checks to ensure a complete and biddable interior package.

## Core Outputs
- Completeness audit (drawings, schedules, specs, details).
- Tender risk list with clarification requirements.
- Bid-query readiness checklist.

## Reference Table: Tender Completeness Minimum
| Package Item | Required Status |
|---|---|
| GA plans and RCP | Coordinated and revision-matched |
| Detail set | 1:10/1:5 details for bespoke elements |
| Schedules | Door, finishes, fixtures, and hardware complete |
| Specification | Material/system standards clearly stated |

## HK residential mini drawing set (P0–P7)

Case hub: [`hk-residential-mini-tender-set.md`](../../references/cases/hk-residential-mini-tender-set.md).  
Audit template: [`tender-completeness-audit.md`](../../references/templates/tender-completeness-audit.md).

### Reference Table: Mini-set sheet completeness
| Sheet | Required |
|---|---|
| P0 現狀平面圖 | Issued; not a substitute for site measure |
| P1 設計平面圖 | Joinery tags L/S/K/B; elev bubbles; `自購` marked |
| P2 地板窗台物料標示圖 | Hatch legend ↔ schedule codes |
| P3 天花/燈具工程標示圖 | Symbol legend; `+H` heights; AC niche notes |
| P4–P7 room elevations | Continuous elev nos.; materials match P1 tags |
| Schedules + BOQ/HKRG | Not satisfied by drawings alone |

### Gap QA (flag before release)
Door/ironmongery schedule · consolidated 物料規格表 · power/ELV layout · 1:20/1:5 for high-risk bespoke joinery · waterproofing build-up sheet · BOQ/HKRG quote attachment · MEP depths beyond RCP notes — full register in the case hub.

## Decision Rules
1. Missing critical details must be flagged before release.
2. Ensure drawing/spec/schedule terminology is aligned.
3. Route unresolved buildability issues to relevant technical sub-skills.
4. For HK residential P0–P7 packages, load the mini-set case hub and run gap QA before “release for tender.”

## HK Local Practice (HKEDCA)

> Cite `HKEDCA §室內工程標準合同`, per-trade `§6 工程計算規則`.

### Reference Table: HK Tender Package vs HKEDCA vs HKRG quotation
| BOQ section | HKEDCA trade | HKRG §標準報價單 |
|---|---|---|
| Preliminaries | 清拆 protection, insurance, estate fees | §8 前期及其他; §9 保險 |
| Demolition | 清拆 | §1 清拆工程 |
| MEP | 水電 | §2 水電工程 |
| Masonry/wet | 坭水/防水 | §3 泥水工程 |
| Joinery/ceilings | 木工前期+後期 | §4 木工工程 |
| Finishes | 油漆 | §5 油漆工程 |
| External | — | §6 外牆工程 |
| Owner install | 雜項 (partial) | §7 代客安裝服務 |
| Cleaning/handover | 交收 | Clause 9–10; Part 2 驗收指引 |

### Reference Table: HK Contract Risk Flags
| Missing item | Risk |
|---|---|
| Protection matrix by reference | Rework disputes |
| 交收 acceptance methods | Sign-off conflict |
| Gas works scope | Statutory breach |
| Measurement §6 per trade | Quantity disputes |

### HKEDCA decision rules
1. Standard contract template requires legal review — not issue verbatim without adaptation.
2. Cross-check every BOQ line to `hkedca-measurement-rules-summary.md`.
3. Require provisional sums for demolition unknowns and MEP congestion.

## HKEDCA Source Pointers
| File | Load when |
|---|---|
| `references/hkedca-standard-contract.md` | Contract structure, risk review |
| `references/hkedca-measurement-rules-summary.md` | BOQ completeness |

## HK Local Practice (HKRG)

> Part 3 **標準報價單**. Cite `HKRG §標準報價單/*`. Legal review mandatory.

### Reference Table: HKRG quotation completeness
| Clause / section | Tender QA check |
|---|---|
| §9 Insurance | Third-party (scaffold scope stated) + 勞保 |
| Payment stages | % sum = 100%; milestones defined |
| Clause 14 | Variation mechanism + signed VO |
| Clause 12 | DLP months filled; repair within 3 months of notice |
| Clause 23 | HKRG 裝修需知 + 驗收指引 adoption |
| Attachment | 保留清單 signed before demolition |
| Clause 10 | Snag holdback for final payment |

### Reference Table: HKRG contract risk flags
| Gap | Risk |
|---|---|
| HKRG contract + HKEDCA BOQ only | Measurement dispute — align line items |
| Missing clause 6 owner-supply list | Supply delay / cost argument |
| Blank LD / insurance self-pay | Unpriced contingency |
| No arbitration clause | Weaker dispute path (clause 20) |

### HKRG decision rules
1. If using HKRG Part 3 as contract, still cross-check quantities to `hkedca-measurement-rules-summary.md`.
2. Flag when client adopts HKRG acceptance but contractor prices HKEDCA trades only.
3. Include boilerplate clause 23 or HKAS web equivalent in contract schedule.
4. Retention list must be contract attachment before tender issue.

### HKRG Source Pointers
| File | Load when |
|---|---|
| `references/hkrg-standard-quotation-contract.md` | Clauses 1–24, BOQ sections, 保留清單 |

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align to HKRG standard quotation (client contracts) and/or HKEDCA contract outline for trade BOQ; map sections per routing table above.
- Mainland mode: align package structure with local institute and contractor bid documentation norms.
- If region unknown, issue universal completeness matrix plus local adaptation checklist.

## Reference Table: Typology Tender Risk
| Typology | Common Tender Gap |
|---|---|
| Residential | Bespoke joinery details missing for unique rooms |
| Workplace | Incomplete coordination between fit-out and landlord interfaces |
| Retail | Feature element details not aligned with rollout timeline |
| Hospitality | FF&E/spec pack misalignment across guestroom variants |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Owner-supply sheets on material schedule incomplete vs quote | `interior-material-procurement` | `OWNER-SUPPLY GAP LIST -> QUOTE CROSS-CHECK -> DELIVERY HOLD POINTS` |
| P2 hatch / P1 joinery tags need 物料規格表 | `interior-material-procurement` | `CODE MAP -> SCHEDULE DRAFT -> OWNER-SUPPLY (自購) SPLIT` |
| P3 lighting legend / lux or IP unclear | `interior-lighting-science` | `LEGEND -> LAYER INTENT -> WET IP / ACCESS NOTES` |
| Bespoke joinery only at 1:50 or tag/elev mismatch | `interior-millwork-technical` | `LOD GAP -> 1:20/1:5 REQUIREMENT -> TAG ALIGNMENT` |
| P3 heights / AC niche / wet ceiling clash | `interior-mep-clash-detection` | `HEIGHT/ZONE MAP -> CLASH OPTIONS -> COORDINATION NOTES` |
| Kitchen FD / fire door callout on plan or elev | `interior-fire-life-safety` | `RATING CHECK -> CERTIFIED SET -> NON-COMPLIANT SWAP BLOCKED` |
| Bid exceeds target budget | `interior-value-engineering` | `COST GAP SUMMARY -> VE OPTIONS -> RECOMMENDED TRACK` |
| Code annotation is unresolved in tender set | `interior-statutory-compliance` | `CODE ISSUE LOG -> REQUIRED NOTES -> DOCUMENT CORRECTIONS` |
| Pre-award SI/RFI response workflow must be defined | `interior-site-supervision` | `SI/RFI PROTOCOL -> RESPONSE SLA -> SITE COMMUNICATION MATRIX` |
| Estate permit or insurance not in preliminaries | `interior-statutory-compliance` | `COMPLIANCE GAP -> CONTRACT CLAUSE -> COST ALLOWANCE` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog
* [hk-residential-mini-tender-set.md](../../references/cases/hk-residential-mini-tender-set.md) — P0–P7 conventions + gap register
* [tender-completeness-audit.md](../../references/templates/tender-completeness-audit.md) — audit artifact

