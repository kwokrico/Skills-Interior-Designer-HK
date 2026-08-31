# Deliverables Catalog — Interior Designer (Global + Hong Kong)

Master index for Phase 4 artifact generation. Use the **standalone file** when one exists; otherwise copy the **inline template** below.

**Conventions:** Cross-reference [`domain_terms.json`](../domain_terms.json). Apply [`compliance.md`](../compliance.md) halts before issuing field instructions. HK residential fit-out: pair **HKEDCA** (trade sequence, BOQ, protection) with **HKRG** (contract, payment, 驗收). Industry practice only — verify AHJ, estate rules, and signed contract.

---

## 1. Stage → deliverable map

| Stage | Primary deliverables | Typical scale / LOD | HK notes |
|-------|---------------------|---------------------|----------|
| **Intake** | Role confirmation, retention list, permit checklist | Narrative + checklist | Estate 裝修申請, scaffold approval, insurance |
| **Concept** | Adjacency, test-fit, mood, design narrative | 1:100–1:50 | Confirm 訂造傢俬 zones before MEP rough-in |
| **SD** | Planning set, preliminary RCP/MEP intent, area schedule | 1:50 | Trade sequence feasibility (§1.10 SKILL) |
| **DD** | Coordinated details, finishes/door/FF&E schedules, specs | 1:20–1:5 | Build-up stacks for 盪地台 / 防水 / 假天花 |
| **CD** | Issue-for-tender/permit package, BOQ alignment | 1:50 + 1:5 details | HKEDCA measurement rules on BOQ lines |
| **Tender** | Completeness audit, RFI log, addenda, bid comparison | Registers | HKRG 標準報價單 cross-check |
| **Construction** | SI, RFI response, protection matrix, concealed-works sign-off | Field records | 掛牌 before fire-triggering works |
| **Handover** | Snag log, acceptance record, O&M index, as-built baseline | Registers | HKRG 驗收指引 + HKEDCA cleaning sequence |
| **DLP** | Defect tracker, root-cause memo, closure evidence | Registers | Owner verification per contract |

---

## 2. Standalone template files

| Deliverable | File | Owner sub-skill |
|-------------|------|-----------------|
| Site Instruction (SI) | [`site-instruction.md`](site-instruction.md) | `interior-site-supervision` |
| Snag / defect log | [`snag-defect-log.md`](snag-defect-log.md) | `interior-handover-dlp` |
| Tender completeness audit | [`tender-completeness-audit.md`](tender-completeness-audit.md) | `interior-tendering-qa` |
| Good-Better-Best VE comparison | [`ve-comparison.md`](ve-comparison.md) | `interior-value-engineering` |
| Compliance gap memo | [`compliance-gap-memo.md`](compliance-gap-memo.md) | `interior-statutory-compliance` |
| HKRG adoption boilerplate | [`hkrg-adoption-boilerplate.md`](hkrg-adoption-boilerplate.md) | `interior-site-supervision` / `interior-handover-dlp` |

**Artifact IDs:** SI-### · SNAG-### · RFI-### · VO-### · ADD-### (see [`operational.md`](../operational.md)).

---

## 3. Inline templates

### 3.1 Request for Information (RFI)

**RFI No.:** RFI-###  
**Project:**  
**Date:**  
**From:**  
**To:**  
**Due date:**

| Field | Content |
|-------|---------|
| **Subject** | |
| **Drawing / spec ref** | Sheet ___ Rev ___ |
| **Location / grid** | |
| **Question** | |
| **Impact if unresolved** | Programme / cost / compliance |
| **Proposed assumption (if any)** | Mark *for contractor risk* unless approved |

**Response**

| Field | Content |
|-------|---------|
| **Answer** | |
| **Issued by** | |
| **Date** | |
| **Drawing update** | Yes — ref ___ / No |

**Distribution:** Contractor | Designer file | Client (if contract requires)

---

### 3.2 Variation Order / Change memo (VO)

**VO No.:** VO-###  
**Project:**  
**Date:**  
**Initiated by:** Owner | Designer | Contractor  
**Contract ref:** HKRG 標準報價單 cl. ___ / Main contract cl. ___

| Item | Detail |
|------|--------|
| **Description of change** | |
| **Reason** | Design development / site condition / client request / AHJ comment |
| **Drawings affected** | |
| **Trade(s)** | 清拆 / 水電 / 坭水 / 木工 / 油漆 / 雜項 |
| **Cost impact** | HK$ ___ (provisional) |
| **Time impact** | ___ days |
| **Compliance** | [ ] No reduction below egress, fire, accessibility, or waterproof performance |

**Approvals**

| Party | Name | Date | Signature |
|-------|------|------|-----------|
| Designer | | | |
| Owner (客方) | | | |
| Contractor (承辦方) | | | |

> HKRG: confirm whether item is 額外工程費 or included scope before site start.

---

### 3.3 Finishes schedule

**Project:**  
**Issue:** Rev ___  
**Date:**

| FS-ID | Room / zone | Element | Product / ref | Manufacturer | Colour / finish | Size / pattern | Substrate / build-up ref | Install trade | Sample status | Remarks |
|-------|-------------|---------|---------------|--------------|-----------------|----------------|--------------------------|---------------|---------------|---------|
| FS-001 | | Floor | | | | | Detail ___ | 坭水 / 雜項 | Approved / Submitted | Dye lot control |
| FS-002 | | Wall | | | | | | 油漆 / 坭水 | | |
| FS-003 | | Ceiling | | | | | | 木工 / 油漆 | | 假天花 coordination |

**HK checks**

- [ ] Wet-area finishes coordinated with 防水 detail and falls  
- [ ] Transition details issued where adjacent finishes differ > 3 mm  
- [ ] Stone/tile cutting method — not on laid floor (HKEDCA protection)

---

### 3.4 Door schedule

**Project:**  
**Issue:** Rev ___

| DR-ID | Location | Type | W×H (mm) | Leaf / frame mat. | Fire rating | Acoustic Rw/STC | Hardware set | Glazing | Threshold / detail | Install sequence |
|-------|----------|------|----------|-------------------|-------------|-----------------|--------------|---------|-------------------|------------------|
| DR-001 | | Single swing | | | FD ___ / Non-rated | | HS-01 | | | Late 木工 — after scaffold off |

**Egress / accessibility**

- [ ] Clear width ≥ AHJ minimum (typ. 850–900 mm — verify)  
- [ ] Maneuvering clearance at latch side documented  
- [ ] Door swing does not reduce egress width below minimum

---

### 3.5 FF&E schedule

**Project:**  
**Issue:** Rev ___

| FF-ID | Room | Item | Qty | Dim (L×W×H) | Spec / model | Power / data | Weight (kg) | Supplier | Lead time (wk) | Install by | Remarks |
|-------|------|------|-----|-------------|--------------|--------------|-------------|----------|----------------|------------|---------|
| FF-001 | | | | | | | | | | 雜項 / specialist | Client-supply? |

**Coordination**

- [ ] Floor loading checked for heavy items  
- [ ] Built-in vs loose furniture interface with 訂造傢俬  
- [ ] Delivery access (lift size, estate rules)

---

### 3.6 RCP / MEP coordination memo

**Project:**  
**Date:**  
**Drawing ref:** RCP Rev ___

| Zone | Conflict ID | Systems | Issue | Clash hierarchy resolution | Action owner | Target close |
|------|-------------|---------|-------|---------------------------|--------------|--------------|
| | CL-001 | FS / P&D / HVAC / ELV | Sprinkler vs luminaire vs duct | FS > P&D > HVAC > ELV | MEP | |

**Design parameters captured**

| Parameter | Office | Meeting | WC | Corridor |
|-----------|--------|---------|-----|----------|
| Target lux (maintained) | | | | |
| CCT / CRI | | | | |
| UGR limit | | | | |
| NRC (ceiling) | | | | |

**HK residential note:** Early 木工 (假天花 / 燈槽) only after concealed MEP signed off.

---

### 3.7 Site protection matrix (HK fit-out)

**Project:**  
**Effective date:**  
**Contractor (承辦方):**

| Zone / finish | Protection measure | Install by trade | Remove only when | Responsible |
|---------------|-------------------|------------------|------------------|-------------|
| Waterproof wet areas | Barrier + signage | 坭水 | After membrane cure + flood test | Contractor |
| Screed / 批盪 | No traffic; pad loads | 坭水 / 油漆 | Strength / dry per spec | Contractor |
| Stone / tile floors | Corner guards; no on-floor cutting | 坭水 | Handover cleaning stage | Contractor |
| Paint walls | Canvas; 油漆未乾 signage | 油漆 | Touch-up complete | Contractor |
| Kitchen cabinets | No foot traffic on tops | 木工後期 | Hardware last | Contractor |
| Timber flooring | Rain protection via windows | 木工後期 | After glass in | Contractor |
| Glass | After scaffold removal | 木工後期 | — | Contractor |

**Gate:** Premature removal → document as 翻執 risk; issue SI if damage occurs.

---

### 3.8 Pre-demolition retention & permit checklist (HK)

**Project:**  
**Walk date:**  
**Owner (客方):**  
**Contractor (承辦方):**

**Retention list (保留清單)**

| Item | Location | Retain? Y/N | Photo ref | Condition note |
|------|----------|-------------|-----------|----------------|
| | | | | |

**Permits & notifications**

| Item | Required? | Ref no. | Expiry | Status |
|------|-----------|---------|--------|--------|
| Estate 裝修申請 | | | | |
| Scaffold approval | | | | |
| 掛牌 (fire alarm isolate) | | | | |
| Insurance certificate | | | | |
| Gas hob removal (registered contractor) | | | | |
| BD / FSD / EMSD / WSD submission (if applicable) | | | | |

**Do not start 清拆 until:** retention signed · permits active · protection plan agreed · neighbour / estate rules acknowledged.

---

### 3.9 Concealed works inspection record

**Project:**  
**Inspection No.:** CW-###  
**Date:**  
**Trade:** 水電 | 防水 | Other ___  
**Location:**

| Check | Pass | Fail | N/A | Evidence (photo) |
|-------|------|------|-----|------------------|
| Routing per approved drawing | | | | |
| Pipe / conduit support spacing | | | | |
| Waterproof membrane continuity | | | | |
| Corner / penetration detailing | | | | |
| Flood test (wet areas) | | | | |
| RCD / earthing (electrical — EMSD CoP) | | | | |

**Sign-off**

| Role | Name | Date |
|------|------|------|
| Designer / inspector | | |
| Contractor | | |

> **Gate:** Do not close walls/floors until this record is complete (SKILL §1.10).

---

### 3.10 Handover acceptance record (HKRG-aligned)

**Project:**  
**交收 date:**  
**Parties:** 客方 · 承辦方 · Designer (witness)

| Room / area | Test method (HKRG 驗收指引) | Criteria | Pass | Fail | Snag ref |
|-------------|------------------------------|----------|------|------|----------|
| Living | Visual finish | No obvious defect | | | |
| Wet room | Water test | No leakage 24h | | | |
| Floor | Foot test | No hollow drum, level trip hazard | | | |
| Joinery | Visual + operation | Doors/drawers align | | | |
| MEP devices | Operation | Switches, outlets, sanitary | | | |

**Outstanding**

| Item | Agreed rectification date | DLP? Y/N |
|------|---------------------------|----------|
| | | |

**Signatures**

| Party | Name | Date |
|-------|------|------|
| Owner (客方) | | |
| Contractor (承辦方) | | |

Adoption text: see [`hkrg-adoption-boilerplate.md`](hkrg-adoption-boilerplate.md).

---

### 3.11 O&M handover index

**Project:**  
**Handover date:**

| System / element | Manual ref | Format | Location in building | Maintenance freq. | Specialist contact |
|------------------|------------|--------|----------------------|-------------------|-------------------|
| HVAC FCU | | PDF / binder | | Quarterly filter | |
| BMS | | | | | |
| Lighting controls | | | | | |
| Waterproof / wet areas | | | | Annual inspect | |
| Custom joinery | | | | | |

**Completeness**

- [ ] As-built drawings issued (Rev ___)  
- [ ] Warranties and test certificates filed  
- [ ] Keys / access cards handed to 客方  
- [ ] Critical snags closed or listed with DLP dates

---

### 3.12 As-built discrepancy register

**Project:**  
**Survey date:**

| DISC-ID | Drawing ref | Field measurement | Drawing value | Delta | Action |
|---------|-------------|-------------------|---------------|-------|--------|
| DISC-001 | | | | | SI-### / Drawing update Rev ___ |

**Rule:** Measure first → SI if build change required → update drawing/spec register (operational SOP).

---

### 3.13 Design intent narrative (concept / SD)

**Project:**  
**Typology:**  
**Date:**

| Section | Content |
|---------|---------|
| **Programme summary** | GFA / key rooms / occupancy assumptions |
| **Circulation concept** | Public vs private; accessibility intent |
| **Material palette** | Floors, walls, ceilings — performance notes (acoustic, slip, VOC) |
| **Lighting concept** | Layering (ambient/task/accent); CCT mood |
| **Brand / identity** (if applicable) | |
| **Sustainability** | BEAM Plus / WELL targets; low-VOC strategy |
| **HK constraints** | Estate rules, clear height, structure, MEP capacity |
| **Exclusions** | Items in base build vs fit-out scope |

---

### 3.14 Trade coordination meeting minute

**Project:**  
**Meeting No.:** TCM-###  
**Date:**  
**Attendees:** 判頭 · trades · designer · client (optional)

| # | Item | Trade | Decision / action | Owner | Due |
|---|------|-------|-------------------|-------|-----|
| 1 | Programme vs 裝修工序 | All | | | |
| 2 | Protection status | All | | | |
| 3 | Concealed works pending | 水電 / 坭水 | | | |
| 4 | RFI / SI open items | — | | | |

**Next meeting:**  
**Sequence reminder:** 清拆 → 水電 → 坭水/防水 → 木工前期 → 油漆 → 木工後期 → 雜項 → 交收

---

### 3.15 DLP defect closure memo

**Project:**  
**SNAG ref:** SNAG-###  
**Reported:**  
**Closed:**

| Field | Detail |
|-------|--------|
| **Description** | |
| **Root cause** | Workmanship / design / material / third party |
| **Rectification** | |
| **Repeat risk** | Low / Med / High — preventive action |
| **Evidence** | Photo set ___ |
| **Owner verification** | Date ___ |

---

## 4. Quick selection guide

| User asks for… | Use |
|----------------|-----|
| Field direction to contractor | §2 [`site-instruction.md`](site-instruction.md) |
| Drawing clarification during tender/build | §3.1 RFI |
| Scope/cost change | §3.2 VO |
| Punch list / 執漏 | §2 [`snag-defect-log.md`](snag-defect-log.md) |
| Owner walk / 自助驗收 | §3.10 + HKRG Part 2 via `interior-handover-dlp` |
| BOQ / tender package QA | §2 [`tender-completeness-audit.md`](tender-completeness-audit.md) |
| Cost option study | §2 [`ve-comparison.md`](ve-comparison.md) |
| Code / submission gap | §2 [`compliance-gap-memo.md`](compliance-gap-memo.md) |
| Before hacking walls | §3.8 retention + §3.9 concealed works |
| Damage prevention on site | §3.7 protection matrix |

---

## 5. Output rules (all deliverables)

1. **No conversational preamble** — start with the artifact title and fields.  
2. Mark jurisdiction-sensitive values as **AHJ-dependent**.  
3. On compliance conflict: **halt** per [`compliance.md`](../compliance.md); do not issue build instructions that breach egress, fire, accessibility, or statutory boundaries.  
4. **HK dual-source:** cite HKEDCA for execution/BOQ; HKRG for contract/acceptance; follow signed contract on conflict.  
5. **Scale:** layout 1:50 default; joinery/interface 1:5 default unless user specifies otherwise.

---

*Aligned with SKILL.md §1.9–§1.11, [`operational.md`](../operational.md), HKEDCA 裝修業界攻略, and HKRG 香港裝修指引 v2.0. Verify latest AHJ, estate, and contract before issue.*
