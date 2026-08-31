# Operational SOPs

## Intake checklist (Phase 1)

Before analysis, confirm or declare assumptions for:

1. **Typology** — residential, workplace, retail, hospitality, mixed-use
2. **Jurisdiction** — global default or HK mode (BD/FSD/EMSD/WSD/LD + estate rules)
3. **Project stage** — concept, SD, DD, CD, tender, construction, handover, DLP
4. **Scale / LOD** — 1:50 layout default; 1:5 joinery default
5. **Stakeholders** — owner, designer, contractor (判頭), AHJ, estate management

Cross-reference [`domain_terms.json`](domain_terms.json) and [`config.json`](config.json) before proceeding.

## Scale defaults

| Request type | Default scale | LOD |
|--------------|---------------|-----|
| Layout / planning | 1:50 | Room logic, circulation, key dimensions |
| Assembly coordination | 1:20 | Build-up, service zones, interfaces |
| Joinery / detailing | 1:5 | Sections, tolerances, material transitions |

## Clash resolution hierarchy

When multiple systems conflict, resolve in order:

1. Fire / Life Safety (FS)
2. Plumbing & Drainage (P&D)
3. HVAC
4. Electrical / ELV
5. Aesthetic treatment and decorative intent

## Ambiguous prompt priority

1. Regulatory / Safety — Is it legal and safe?
2. Technical / Structural — Is it buildable?
3. Human / Functional — Does it work for users?
4. Aesthetic / Stylistic — Does it express design intent?

## HK trade sequence gates

Do not proceed until gate conditions in SKILL §1.10 are met:

```text
清拆 → 水電 → 坭水/防水 → 木工（前期）→ 油漆 → 木工（後期）→ 雜項 → 交收
```

## Dual-source citation (HKEDCA + HKRG)

| Question type | Primary | Secondary |
|---------------|---------|-----------|
| Trade sequence, protection, BOQ measurement | HKEDCA | HKRG Part 1 for client/contractor duties |
| Payment, quote template, contract T&C | HKRG Part 3 | HKEDCA §室內工程標準合同 for trade alignment |
| Owner snag walk, room acceptance | HKRG Part 2 | HKEDCA §交收 for cleaning sequence |
| Permits and statutory compliance | AHJ + interior-statutory-compliance | HKEDCA/HKRG as pre-start practice only |

On conflicting numbers between HKEDCA and HKRG, cite both and follow the signed contract.

## Artifact naming conventions

| Artifact | ID format | Owner sub-skill |
|----------|-----------|-----------------|
| Site Instruction | SI-### | interior-site-supervision |
| Snag / defect log | SNAG-### | interior-handover-dlp |
| Request for Information | RFI-### | interior-site-supervision |
| Variation order | VO-### | interior-tendering-qa |
| Tender addendum | ADD-### | interior-tendering-qa |

## Escalation paths

1. **Code conflict** → interior-statutory-compliance + interior-fire-life-safety
2. **Buildability / clash** → interior-mep-clash-detection per hierarchy above
3. **Field vs drawing discrepancy** → measure first → SI → as-built update
4. **Contract / payment dispute** → interior-tendering-qa + HKRG references
5. **Repeat DLP defect** → root-cause review before closure (interior-handover-dlp)

## Review gates

| Stage | Gate |
|-------|------|
| Tender release | interior-tendering-qa completeness audit |
| Practical handover | O&M + as-built baseline + critical snags closed |
| DLP closure | Evidence of repair + owner verification |

## Module reference extracts

HKEDCA and HKRG markdown extracts live under `subskills/<slug>/references/` and load only when that subskill is dispatched (progressive disclosure). Shared vocabulary, compliance, and templates remain in `references/` at skill root — one hop from `SKILL.md`.
