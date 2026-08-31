# HKRG Index — 香港裝修指引 (平台版 2.0)

## Document metadata

| Field | Value |
|-------|-------|
| Title | 香港裝修指引 (Hong Kong Renovation Guidelines) |
| Web name | 裝修資訊 (Renovation Information) — [HKAS](https://www.hkarbsoc.org.hk/hk/renovation_hk.htm) |
| Publishers | 香港仲裁公會 (HKAS), 香港樓宇檢驗學會 (HKBIA), 好師傅 (Codeco) |
| Canonical file | [HKRG-香港裝修指引-2.0.pdf](HKRG-香港裝修指引-2.0.pdf) |
| Version | 2.0 (07/2022 print) |
| Language | Traditional Chinese (source); English structure in sub-skill `references/` |
| Approx. length | 74 PDF pages |

## Disclaimer

Voluntary **industry practice**, not statutory law. Do not replace legal advice. User bears risk of reliance. Always verify:

- Buildings Department (BD), Fire Services Department (FSD), Labour Department (LD)
- EMSD, WSD, estate / owners' corporation, insurance, project contract

## Citation format

`HKRG §{part}/{section}` — e.g. `HKRG §驗收指引/2.5`, `HKRG §標準報價單/條款14`, `HKRG §裝修需知/1.4`.

Markdown extracts: `interior-designer-hk/subskills/{skill_id}/references/hkrg-*.md`.

## Table of contents (PDF page anchors)

| Section | PDF pages (approx.) | Sub-sections |
|---------|---------------------|--------------|
| 免責聲明 | 4 | — |
| 序 | 8–9 | Purpose, three parts |
| **1. 裝修需知** | 11–31 | 1.1–1.14 (see below) |
| **2. 驗收指引** | 33–47 | 2.1–2.15 |
| **3. 標準報價單** | 49–58 | Blank template + T&C clauses 1–24 |
| **4. 標準報價單（樣本）** | 59–66 | Worked example |
| **5. 附件：保留清單** | 69–71 | Pre-demolition retention form |

### Part 1 — 裝修需知 (doc pp. 02–20)

| § | Topic | PDF ~p. |
|---|-------|---------|
| 1.1 | 工程整體 | 12–13 |
| 1.2 | 客方第三方度尺/送貨/安裝 | 14 |
| 1.3 | 清拆工程 | 15 |
| 1.4 | 水電工程 | 16–17 |
| 1.5 | 煤氣工程 | 18 |
| 1.6 | 鋁窗工程 | 19 |
| 1.7 | 防水工程 | 20 |
| 1.8 | 泥水工程 | 21–22 |
| 1.9 | 訂造傢俬 | 23–24 |
| 1.10 | 油漆/牆紙 | 25–26 |
| 1.11 | 木門 | 27 |
| 1.12 | 木地板 | 28 |
| 1.13 | 假天花 | 29 |
| 1.14 | 清潔及保養 | 30–31 |

### Part 2 — 驗收指引 (doc pp. 24–37)

| § | Topic | PDF ~p. |
|---|-------|---------|
| 2.1–2.2 | 來去水/潔具 | 34–35 |
| 2.3 | 電工 | 35–37 |
| 2.4 | 門窗玻璃露台 | 37–38 |
| 2.5–2.6 | 鋪磚/批盪 | 39–40 |
| 2.7–2.8 | 傢俬/廚櫃 | 41–42 |
| 2.9–2.10 | 油漆/牆紙 | 43 |
| 2.11–2.12 | 木工/木地板 | 44–45 |
| 2.13–2.15 | 電器/冷氣/清潔 | 46–47 |

## Skill routing table

| HKRG part | `skill_id` | Reference file(s) |
|-----------|------------|-------------------|
| 裝修需知 (overview + 1.1) | `interior-site-supervision` | `hkrg-renovation-essentials.md` |
| 裝修需知 (1.2–1.14 trades) | `interior-site-supervision` | `hkrg-renovation-essentials-trades.md` |
| 驗收指引 | `interior-handover-dlp` | `hkrg-self-inspection-handover.md` |
| 標準報價單 + 保留清單 | `interior-tendering-qa` | `hkrg-standard-quotation-contract.md` |
| 額外工程費 / VE triggers | `interior-value-engineering` | `hkrg-renovation-essentials-trades.md` (另收費) |
| Pre-start (client view) | `interior-statutory-compliance` | `hkrg-renovation-essentials-trades.md` §1.3 |

## HKRG vs HKEDCA

| | HKRG | HKEDCA |
|---|------|--------|
| Audience | Homeowner + contractor | Trade contractor / 判頭 |
| Strength | Contract, payment, owner acceptance | Sequence, protection, measurement |
| Handover | Room checklist (Part 2) | Cleaning sequence, trade tests (§交收) |
| Contract | Standard quotation (Part 3) | 室內工程標準合同 |

Use **both** for HK residential: HKRG for client contract & snag; HKEDCA for site execution & BOQ.

## Contract adoption boilerplate

本工程將採用「裝修資訊」中的「裝修需知」及「自助驗收指引」，作為工作流程與驗收的標準。

(Part 3 template uses 《香港裝修指引》 wording for 「裝修需知」及「驗收指引」.)

## Glossary

| Term | English | Notes |
|------|---------|-------|
| 客方 | Client / owner | Pays, supplies owner materials |
| 承辦方 | Contractor | Executes works per quotation |
| 裝修資訊 | Renovation Information | HKAS web branding |
| 驗收指引 | Acceptance guide | Part 2; aka 自助驗收 on web |
| 執漏 | Snag rectification | May be post-handover per §1.1 |
| 變更工程 | Variation works | Clause 14 |
| 交吉 | Vacant possession | Clause 1 — before start |

## Extraction status

| Reference file | Status |
|----------------|--------|
| `hkrg-renovation-essentials.md` | Integrated v1 (2026-05) |
| `hkrg-renovation-essentials-trades.md` | Integrated v1 (2026-05) |
| `hkrg-self-inspection-handover.md` | Integrated v1 (2026-05) |
| `hkrg-standard-quotation-contract.md` | Integrated v1 (2026-05) |

## Master skill pointer

Dual-source HK routing: [interior-designer-hk/SKILL.md](../interior-designer-hk/SKILL.md) §1.10 (HKEDCA) + §1.11 (HKRG).
