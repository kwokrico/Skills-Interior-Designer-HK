# Lighting evidence review

**The supplier’s claim is not substantiated.** A schedule showing 500 lux initially establishes neither the maintained illuminance nor comfortable screen work. Hold acceptance of those claims pending the evidence below; this is an evidence gap, not a finding that the installed scheme necessarily fails.

The applicable jurisdiction, contract lighting standard/edition, actual maintained target and task areas have not been provided. Confirm these before declaring compliance. A generic office lux range is not a statutory requirement or project acceptance criterion.

| Missing evidence | What the supplier / lighting designer should submit |
|---|---|
| Meaning of “500 lux” | State whether calculated or measured, average/minimum/single point, electric-only or including daylight, workplane height, task-area boundaries and operating/control scene. A room average can conceal poorly lit desks. |
| Maintenance basis | A documented total maintenance factor, design period/operating hours, LED lumen depreciation and survival/replacement assumptions, luminaire dirt and room-surface depreciation, cleaning intervals and replacement policy. Link these to the actual selected product and an achievable O&M plan. |
| Maintained calculation | Initial and maintained results for the same task areas, calculation grid, minimum/average illuminance and uniformity, plus immediate surroundings and background. Supply the model with room dimensions, mounting positions/heights, furniture/partition obstructions, surface reflectances and verified IES/LDT photometry for the exact luminaires. |
| Direct glare | A layout-specific Unified Glare Rating (UGR) assessment against the agreed criterion, including seated observer locations and viewing directions. A catalogue “low-glare” or UGR label alone does not validate the room. |
| Screen reflections and contrast | Review actual screen positions/tilts, screen finish and brightness, luminaire luminance/distribution, window orientation, daylight/blinds and bright or glossy surfaces in users’ fields of view. Include representative daytime and evening conditions. Passing UGR does not by itself eliminate reflected glare. |
| Other lighting quality | Model-specific colour temperature and colour-rendering data; driver/control compatibility and flicker evidence at the intended dimming levels. Lux does not describe these properties. |
| Installation verification | Calibrated lux-meter survey at the agreed grid/workplane, recording daylight, blinds, dimming and control settings; compare with the approved model. Test scenes and daylight controls, and review representative occupied workstations for reflections, shadows and visual comfort. Record corrective actions and rechecks. |

For a conventional depreciation calculation, **maintained illuminance = initial illuminance × total maintenance factor**. Therefore 500 lux initially with a total factor below 1 produces less than 500 lux maintained. Do not invent the factor. If constant-light-output controls are claimed, require evidence of control strategy, output headroom and performance over the maintenance period. CIE defines the factor as the aged-to-new illuminance ratio and includes lamp output decline and dirt losses; ISO/CIE TS 22012 gives the determination framework. [CIE definition](https://cie.co.at/eilv/753), [ISO/CIE TS 22012:2019](https://www.iso.org/standard/72353.html).

**Avoid double-counting depreciation:** if the quoted maintenance factor already incorporates lumen maintenance, do not multiply by another lamp-lumen/light-loss factor covering the same loss. Require the supplier to define every factor and its components.

Screen comfort also requires control of bright sources, reflections and brightness imbalance. This is consistent with [HSE display-screen guidance, paragraphs 30–31](https://www.hse.gov.uk/PuBns/priced/l26.pdf) and [CIBSE lighting guidance](https://www.cibse.org/knowledge-research/knowledge-portal/lighting-in-buildings-top-tips?id=a0q20000006oaz1AAA); these are technical references here, not a claim that UK duties apply to this project.

Suggested review comment: **“Revise and resubmit: demonstrate the specified maintained illuminance and uniformity using a documented maintenance basis, provide layout-specific glare and screen-reflection assessment, and submit commissioning and maintenance evidence. Initial 500 lux alone is insufficient for acceptance.”**

---

## File and URL trace

Read only the assigned case input; no other evaluation cases, reports or agent outputs consulted.

Local files read:
- `interior-designer-hk/evals/runs/remaining-2026-11-07/inputs/case-54.txt`
- `interior-designer-hk/SKILL.md`
- `interior-designer-hk/references/config.json`
- `interior-designer-hk/references/compliance.md`
- `interior-designer-hk/references/operational.md`
- `interior-designer-hk/references/domain_terms.json`
- `interior-designer-hk/subskills/interior-lighting-science/interior-lighting-science.md`
- `interior-designer-hk/references/templates/deliverables.md`
- `interior-designer-hk/references/ching-hk-adaptation.md` (tool excerpt; unrelated sections truncated)
- `.cursor/rules/source-archive.mdc`

Primary web evidence checked via search on 2026-11-07:
- https://cie.co.at/eilv/753 — maintenance factor definition and included losses.
- https://www.iso.org/standard/72353.html — ISO/CIE TS 22012:2019 scope.
- https://www.hse.gov.uk/PuBns/priced/l26.pdf — screen glare, reflections and brightness imbalance, paragraphs 30–31.
- https://www.cibse.org/knowledge-research/knowledge-portal/lighting-in-buildings-top-tips?id=a0q20000006oaz1AAA — visual discomfort factors including reflections, glare and flicker.

No project photometry, maintenance factors or acceptance criteria were supplied. No numerical maintenance factor was assumed and no fixture-sizing calculation was performed. The master skill's generic MF × LLF expression must not be applied where MF already includes the same lumen depreciation. No source integration was requested, so the archive rule did not trigger.
