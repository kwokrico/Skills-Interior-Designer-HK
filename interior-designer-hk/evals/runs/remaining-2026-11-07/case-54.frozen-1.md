# Lighting schedule review — evidence outstanding

**The supplier’s claim is not substantiated.** A schedule showing **500 lux initially** establishes neither the maintained illuminance nor comfortable screen work. Hold performance acceptance pending the evidence below; this is an evidence gap, not proof that the installation fails.

The maintained target, its contractual standard/edition, jurisdiction, task definition and assessment plane have not been provided. Confirm these before making a compliance determination. No project maintenance factor is assumed.

| Missing evidence | Required submission and review |
|---|---|
| Defined acceptance criteria | State the maintained target for the actual office tasks, task and surrounding areas, working-plane height, uniformity and glare criteria, and the applicable specification/standard edition. Clarify whether “500 lux” is an average, minimum or isolated point; calculated or measured; and electric lighting alone or including daylight. |
| Maintenance calculation | Provide the overall maintenance factor, its component factors and supporting product/environment data. Identify operating hours, design/maintenance interval, lumen depreciation, luminaire and room-surface dirt effects, survival/replacement policy, cleaning intervals and responsibilities. Initial output cannot substitute for this calculation. |
| Reproducible photometric model | Supply the calculation report and matching IES/LDT files for the exact luminaire/optic/driver/output variant. Include mounting heights, spacing/aiming, room geometry, reflectances, furniture/partition obstructions and the calculation grid. Report initial and maintained average/minimum values, distribution and uniformity separately. A whole-room average can conceal underlit desks. |
| Glare and screen reflections | Assess direct discomfort glare from relevant seated positions and viewing directions using the applicable method, such as UGR where suitable. A catalogue “low-glare” or UGR claim alone does not establish performance in this room. Review luminaire/window reflections in screens, screen orientation and tilt, bright sources within the field of view, desk finish and luminance contrast between screen and surroundings. Lux measures incident light; it does not measure these brightness relationships. |
| Daylight and operating scenes | Review representative daytime and evening conditions, window orientation and shading/blinds, and their effect on glare and screen reflections. Show that the electric-lighting design meets the agreed basis without relying on unspecified daylight. Document control zones, dimming/daylight response, driver compatibility and flicker performance through the intended dimming range. |
| Complete product schedule | Link each luminaire tag/location/quantity to manufacturer and model, photometry, output/power, CCT, colour-rendering evidence, mounting/depth, driver/control specification and maintenance access. Verify supplied products against the model; substitutions require renewed equivalence and performance checks. CCT or CRI alone does not establish comfort. |
| Verification and upkeep | Provide a commissioning plan using a calibrated meter and defined task-plane grid in the completed furniture layout. Record daylight/blind conditions, control settings, installed product variants, average/minimum/uniformity results and screen-reflection observations. Include as-built records and an O&M schedule supporting the maintenance factor. A commissioning measurement at installation verifies initial conditions; it does not by itself prove future maintained performance. |

For an unchanged output setting and comparable conditions:

**Maintained illuminance = initial illuminance × overall maintenance factor.**

If the agreed target is 500 lux maintained, 500 lux initial leaves no allowance for depreciation. If constant-light-output control is proposed, require its documented output reserve, control strategy and performance over the maintenance period. Do not simply assume that it preserves 500 lux.

Use one clearly defined overall factor: **do not multiply an overall MF by a second light-loss/lumen-depreciation factor if that loss is already included.** CIE describes maintenance-factor determination using equipment, environment and maintenance conditions; IES uses “LLF” for a broad light-loss allowance, so the supplier must define its terminology and avoid double counting. [CIE maintenance-factor guidance](https://www.cie.co.at/publications/light-and-lighting-maintenance-factor-determination-way-working), [IES definition of LLF](https://ies.org/definitions/light-loss-factor-llf/).

Screen comfort needs separate evidence: official HSE guidance identifies reflected light on screens, abrupt contrasts and workstation conditions as relevant lighting issues. It supports reviewing blinds, source angles and workstation arrangement; it is cited as technical guidance, not as Hong Kong statutory criteria. [HSE workplace lighting guidance](https://www.hse.gov.uk/humanfactors/topics/lighting.htm).

**Return to supplier:** “Revise and resubmit with the agreed maintained-performance criteria, a supported maintenance calculation, room-specific photometric and glare/reflection assessment, exact product/driver data, and a commissioning and maintenance plan. The 500-lux initial entry is insufficient for acceptance of either maintained illuminance or screen-work comfort.”

---

## File and URL trace

Only the supplied test prompt and frozen skill resources were accessed; no live workspace skill files, other evaluation files, reports or prior responses were read.

Prompt:
- `C:/Users/Rico/PycharmProjects/Skills-Interior Designer-HK/interior-designer-hk/evals/runs/remaining-2026-11-07/inputs/case-54.txt`

Frozen root: `C:/Users/Rico/AppData/Local/Temp/interior-hk-eval-9ln4jtyb/interior-designer-hk/`

Files read relative to frozen root:
- `SKILL.md`
- `references/config.json`
- `references/compliance.md`
- `references/operational.md`
- `references/domain_terms.json`
- `references/templates/deliverables.md`
- `subskills/interior-lighting-science/interior-lighting-science.md`
- `subskills/interior-material-procurement/interior-material-procurement.md`
- `subskills/interior-mep-clash-detection/interior-mep-clash-detection.md`
- `subskills/interior-handover-dlp/interior-handover-dlp.md`
- `scripts/calculators.py`

Calculator inspection: the frozen helper multiplies MF and LLF, while the glossary describes MF as combined depreciation. That can double-count losses. No project numerical calculation was run because no supported maintenance inputs were supplied; the answer uses the defined overall-factor relationship and flags the terminology issue.

Official web evidence consulted on 2026-11-07 through web search results:
- CIE, ISO/CIE TS 22012:2019(E): https://www.cie.co.at/publications/light-and-lighting-maintenance-factor-determination-way-working
- CIE 97:2005: https://www.cie.co.at/publications/guide-maintenance-indoor-electric-lighting-systems-2nd-ed
- IES, light loss factor definition: https://ies.org/definitions/light-loss-factor-llf/
- HSE, workplace lighting guidance: https://www.hse.gov.uk/humanfactors/topics/lighting.htm

No numerical UGR, uniformity or statutory threshold is asserted without the project’s applicable standard and edition. No separate archive files were created, as the test instruction restricts output to this response file.
