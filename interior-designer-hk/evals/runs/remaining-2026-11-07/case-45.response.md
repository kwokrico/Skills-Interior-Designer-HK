**Compliance gap memo — HOLD: single exit not approved**

I cannot approve a single 900 mm exit for this 120-person Hong Kong training room. The skill's [compliance rules](../../../references/compliance.md), Universal §2 and Hard stops, require an advisory-only boundary and a halt on egress breaches.

The calculator's **540** is only `900 × 0.6`. Its default factor and `adequate` result do not establish HK code compliance; the calculation does not check exit count, independence, travel distance or downstream escape capacity. Do not use it as an approved occupancy limit.

For the stated 120 occupants, **BD Fire Safety Code 2011 (2024 Edition), B7.1 and Table B2, 31–200-person row**, gives:

| Check | Requirement | Proposed arrangement |
|---|---|---|
| Exit doors | At least 2 | 1 — fails |
| Combined door width | At least 1,750 mm | 900 mm — fails |
| Each door | At least 850 mm | 900 mm potentially meets this check only, if actual clear width |
| Exit routes | At least 1,050 mm each; 2,100 mm combined | Not demonstrated |

B7.2 requires independent escape routes; for up to 200 occupants, doors may open onto one corridor/balcony approach **only where escape is possible in more than one direction**. [Official BD code, printed pp.32–34](https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf).

**Remediation:** have the project's Authorized Person develop a two-exit arrangement. Two genuinely clear 900 mm doors would meet the table's door-width totals, but would not alone establish compliance. Provide the measured plan, actual use classification, room area/seating and total occupants including trainers, approved building records, floor level, door operation, travel distances and complete routes to final discharge for review. The applicable code/approval basis and any special-use provisions remain to be confirmed.

If a second compliant exit is impracticable, relocate the training use or have the Authorized Person assess a reduced occupancy and obtain any required approvals. Simply widening the sole door does not resolve the exit-count failure. No construction or occupancy approval is issued here.

---

Read trace (checked 7 November 2026):

- `interior-designer-hk/evals/runs/remaining-2026-11-07/inputs/case-45.txt`
- `interior-designer-hk/SKILL.md`
- `interior-designer-hk/references/config.json`
- `interior-designer-hk/references/compliance.md`
- `interior-designer-hk/references/operational.md`
- `interior-designer-hk/references/domain_terms.json`
- `interior-designer-hk/references/ching-hk-adaptation.md`
- `interior-designer-hk/references/templates/deliverables.md`
- `interior-designer-hk/references/templates/compliance-gap-memo.md`
- `interior-designer-hk/subskills/interior-fire-life-safety/interior-fire-life-safety.md`
- `interior-designer-hk/subskills/interior-statutory-compliance/interior-statutory-compliance.md`
- `interior-designer-hk/scripts/calculators.py` (source inspected; attempted Python execution unavailable because Python was not on PATH; arithmetic independently checked as 900 × 0.6 = 540).
- Web search: `site.bd.gov.hk fire safety code 2011 2024 Table B2 101 200 exits 1050`; search results included official BD code/index and unrelated results, which were not relied upon.
- Opened and searched official PDF: https://www.bd.gov.hk/doc/en/resources/codes-and-references/code-and-design-manuals/fs_code2011.pdf — B7.1–B7.3 and Table B2; screenshot requested for zero-based page 42 (printed p.34).
- No other evaluation files, research review/validation reports or agent outputs read. No source archive written because this test authorizes only this response file.

