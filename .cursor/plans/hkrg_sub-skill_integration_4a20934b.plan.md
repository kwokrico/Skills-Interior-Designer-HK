---
name: HKRG sub-skill integration
overview: Integrate 《香港裝修指引》平台版 2.0 (HKRG) into the Claude Desktop skill suite using the same index + `references/hkrg-*.md` + sub-skill pointer pattern as HKEDCA, with comprehensive extracts of all three parts and dual-source routing so HKRG governs client–contractor process/acceptance/quote while HKEDCA remains the trade-execution anchor.
todos:
  - id: extract-hkrg-pdf
    content: Text-extract HKRG PDF; build TOC with page anchors in Reference/HKRG-INDEX.md
    status: completed
  - id: write-hkrg-refs
    content: Author 4 comprehensive hkrg-*.md reference files (Parts 1–3 + trade table)
    status: completed
  - id: update-primary-subskills
    content: Add HKRG sections to interior-site-supervision, interior-handover-dlp, interior-tendering-qa
    status: completed
  - id: crosslink-hkedca-subskills
    content: Add HKRG cross-reference blocks to 6 HKEDCA trade/compliance sub-skills
    status: completed
  - id: update-master-skill
    content: "Update Claude Desktop/SKILL.md: §1.11, routing, dispatcher_logic, sources"
    status: completed
  - id: verify-routing
    content: Spot-check quote, handover, and variation prompts for correct dual-source citations
    status: completed
isProject: false
---

# HKRG integration into Claude Desktop sub-skills

## Context

| Source | File | Role |
|--------|------|------|
| **HKEDCA** | [Reference/20231229121903_125_detail.pdf](Reference/20231229121903_125_detail.pdf) + [Reference/HKEDCA-INDEX.md](Reference/HKEDCA-INDEX.md) | Trade sequence, site protection, BOQ/measurement, contractor handover depth |
| **HKRG** | [Reference/HKRG-香港裝修指引-2.0.pdf](Reference/HKRG-香港裝修指引-2.0.pdf) | Client–contractor collaboration, **自助驗收**, **標準報價單** (HKAS / HKBIA / 好師傅, v2.0 ~Jun 2022) |

HKRG is **voluntary industry practice**, not statutory law — same disclaimer pattern as HKEDCA.

Existing integration pattern (reuse, do not reinvent):

```mermaid
flowchart LR
  PDF[Canonical PDF in Reference/]
  INDEX[INDEX.md routing table]
  REFS[sub_skills/.../references/hkrg-*.md]
  SUB[sub_skill.md HK sections]
  MASTER[Claude Desktop/SKILL.md router]

  PDF --> INDEX
  INDEX --> REFS
  REFS --> SUB
  SUB --> MASTER
```

## Dual-source rules (document in index + master skill)

| User question | Primary cite | Secondary cite |
|---------------|--------------|----------------|
| 清拆→交收 sequence, protection matrix, 工程計算 | `HKEDCA` | `HKRG` Part 1 only for **客方/承辦方** duties |
| Payment stages, quote template, contract T&C, retention/warranty wording | `HKRG` Part 3 | `HKEDCA §室內工程標準合同` for trade-scope alignment |
| Homeowner / designer snag walk, room-by-room acceptance | `HKRG` Part 2 | `HKEDCA §交收` for trade cleaning sequence & contractor thresholds |
| BD/FSD/EMSD/estate permits | `interior-statutory-compliance` + AHJ | Both guides as **pre-start practice** only |

**Conflict handling:** If HKRG and HKEDCA disagree on a numeric tolerance, list both with source tags; recommend field measurement + contract precedence. Never merge into a single unsourced number.

**Citation format:** `HKRG §{part}/{section}` e.g. `HKRG §自助驗收/廚房`, `HKRG §標準報價單/付款`. Optional PDF page from index.

---

## Phase 1 — Extract PDF to structured references (comprehensive)

The repo PDF is binary; extraction requires a one-time text pass (e.g. `pdftotext` or Adobe export) into a working `Reference/_hkrg-extract.txt`, then manual structuring into markdown.

### 1.1 Create [Reference/HKRG-INDEX.md](Reference/HKRG-INDEX.md)

Mirror [Reference/HKEDCA-INDEX.md](Reference/HKEDCA-INDEX.md):

- Metadata: title, publishers (HKAS, HKBIA, Codeco), canonical PDF path, language, ~74 pp, v2.0 date
- Disclaimer + statutory cross-check list (same AHJ set as HKEDCA index)
- **TOC with PDF page anchors** for all three parts (build while extracting)
- **Skill routing table** (below)
- **HKRG vs HKEDCA** comparison table (purpose, audience, when to load which)
- Contract adoption boilerplate from [HKAS renovation page](https://www.hkarbsoc.org.hk/hk/renovation_hk.htm):  
  `本工程將採用"裝修資訊"中的"裝修需知"及"自助驗收指引"，作為工作流程與驗收的標準。`
- Glossary extension: 客方, 承辦方, 裝修資訊 (official web name) vs 香港裝修指引 (document title)
- Extraction status table

### 1.2 Reference markdown files (comprehensive content)

| File | HKRG part | Hosted under |
|------|-----------|--------------|
| `hkrg-renovation-essentials.md` | Part 1 裝修需知 — intro, general flow, cross-trade rules | `interior-site-supervision/references/` |
| `hkrg-renovation-essentials-trades.md` | Part 1 — **per major trade**: 客方責任, 承辦方責任, 重點事項, **額外工程費** triggers (preserve guide wording in tables) | same folder |
| `hkrg-self-inspection-handover.md` | Part 2 自助驗收指引 — **full room/element checklists** | `interior-handover-dlp/references/` |
| `hkrg-standard-quotation-contract.md` | Part 3 標準報價單 — line-item structure, payment schedule, programme, 保養期, 條款及細則 | `interior-tendering-qa/references/` |

**Formatting conventions** (match existing `hkedca-*.md`):

- English headings + Traditional Chinese terms in tables
- Source line at top: `Source: HKRG §…, PDF ~p.X–Y`
- Numbered checklist items copied faithfully from PDF; add English gloss column only where it aids routing, not as a substitute for the Chinese criterion text

If Part 1 trade sections exceed ~40k tokens in one file, split `hkrg-renovation-essentials-trades.md` into `hkrg-trades-A-D.md` / `hkrg-trades-E-H.md` by guide structure (decide from TOC during extract).

---

## Phase 2 — Update primary sub-skills (3 parts → 3 owners)

### 2.1 [interior-site-supervision/interior-site-supervision.md](Claude Desktop/sub_skills/interior-site-supervision/interior-site-supervision.md)

Add **`## HK Local Practice (HKRG)`** after the HKEDCA block (keep both sections separate):

- Reference tables: **Client vs contractor obligations** per stage; **variation / 額外工程費** red flags from Part 1
- Decision rules: SI must reference which party supplied owner materials; stop-work when HKRG preconditions (e.g. approvals, scope sign-off) not met
- **HKRG Source Pointers** → `hkrg-renovation-essentials.md`, `hkrg-renovation-essentials-trades.md`
- Auto-chain: `額外工程費` / scope dispute → `interior-tendering-qa`; acceptance dispute → `interior-handover-dlp`

### 2.2 [interior-handover-dlp/interior-handover-dlp.md](Claude Desktop/sub_skills/interior-handover-dlp/interior-handover-dlp.md)

Add **`## HK Local Practice (HKRG)`**:

- Map Part 2 checklists to existing acceptance methods (目測/耳聽/腳踏/灑水) — crosswalk table: `HKRG item` ↔ `HKEDCA §交收/5 method`
- Decision rules: practical completion requires **both** HKRG Part 2 pass items (contractual if adopted) **and** HKEDCA cleaning sequence where contract references HKEDCA
- DLP register: add field `HKRG checklist ref`
- **HKRG Source Pointers** → `hkrg-self-inspection-handover.md`

### 2.3 [interior-tendering-qa/interior-tendering-qa.md](Claude Desktop/sub_skills/interior-tendering-qa/interior-tendering-qa.md)

Add **`## HK Local Practice (HKRG)`**:

- Reference tables: standard quote sections, payment milestone checklist, missing-clause risks (retention, warranty, programme, variations)
- BOQ alignment: map HKRG line items to HKEDCA trade BOQ sections (extend existing “HK Tender Package vs HKEDCA Trades” table with HKRG column)
- Decision rules: legal review still required; flag when contract adopts HKRG Part 3 but BOQ uses HKEDCA measurement only
- **HKRG Source Pointers** → `hkrg-standard-quotation-contract.md`

---

## Phase 3 — Light cross-links in HKEDCA-heavy sub-skills (no duplicate full text)

Nine sub-skills already have `## HK Local Practice (HKEDCA)` ([grep set](Claude Desktop/sub_skills)). Add a **5–8 line** `### HKRG cross-reference` block only:

| Sub-skill | Pointer |
|-----------|---------|
| `interior-statutory-compliance` | Part 1 pre-start / estate / insurance from **client** perspective |
| `interior-value-engineering` | Part 1 **額外工程費** triggers → VE scope control |
| `interior-mep-clash-detection`, `interior-thickness-build-up`, `interior-millwork-technical`, `interior-interface-detailing`, `interior-fire-life-safety` | Trade row in `hkrg-renovation-essentials-trades.md` + HKEDCA technical ref |
| `interior-tendering-qa`, `interior-handover-dlp`, `interior-site-supervision` | full HKRG sections (Phase 2) |

Do **not** add HKRG blocks to non-HK sub-skills (`interior-acoustic-engineering`, `interior-lighting-science`, etc.) unless Part 1 explicitly covers them (unlikely).

---

## Phase 4 — Master router [Claude Desktop/SKILL.md](Claude Desktop/SKILL.md)

1. **New §1.11** `HK Residential Renovation — Client & Contract (HKRG)`  
   - Three-part summary, adoption sentence, link to [Reference/HKRG-INDEX.md](Reference/HKRG-INDEX.md)  
   - One-line: use with §1.10 HKEDCA trade sequence

2. **Routing tree** additions (after existing HKEDCA triggers ~L200–216):

   - `裝修資訊` / `香港裝修指引` / `HKRG` → site-supervision + index  
   - `標準報價單` / payment terms / 保養期 → tendering-qa  
   - `自助驗收` / owner walkthrough → handover-dlp  

3. **`dispatcher_logic`** — new rule:

   ```xml
   <context_rule trigger="HKRG / 裝修資訊 / 標準報價單 / 自助驗收">
     Region: Hong Kong
     Load: Reference/HKRG-INDEX.md
     Route: interior-site-supervision | interior-handover-dlp | interior-tendering-qa
     Pair with HKEDCA when trade execution or BOQ measurement needed
   </context_rule>
   ```

4. **Sources footnote** (§4): add HKRG alongside HKEDCA.

---

## Phase 5 — Verification

- [ ] Every `hkrg-*.md` file has source tags and appears in HKRG-INDEX routing table  
- [ ] Every updated sub-skill lists HKRG pointers in “Source Pointers” tables  
- [ ] Spot-check 3 user prompts: (1) quote review, (2) owner snag list, (3) 額外工程費 dispute — router reaches correct sub-skill and cites HKRG + HKEDCA appropriately  
- [ ] No contradiction without dual citation (handover tolerances, payment terms)

---

## Deliverables summary

| Artifact | Count |
|----------|-------|
| `Reference/HKRG-INDEX.md` | 1 new |
| `references/hkrg-*.md` | 4 new (comprehensive) |
| Sub-skill `.md` updates | 3 full + ~6 cross-ref |
| `Claude Desktop/SKILL.md` | §1.11, routing, dispatcher, sources |

**Out of scope (unless you ask later):** embedding PDF in repo beyond existing file; legal opinion on contract clauses; Mainland China parallel guide.
