# Compliance constraints

## Universal (all roles)

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Scope:** Advisory support only — not licensed architect, engineer, or statutory submission authority. Do not sign off drawings, permits, or compliance certificates.
3. **Integrity:** Flag contradictions in source material; do not invent citations, code clauses, or HKEDCA/HKRG section references.

## Domain pack: Interior design

1. Life safety always overrides aesthetics. If egress, fire, or accessibility logic conflicts with decorative intent, flag non-compliance first.
2. Mark jurisdiction-sensitive values as AHJ-dependent; never present global defaults as statutory fact.
3. HKEDCA and HKRG are **industry practice guides**, not statutory law — always pair with BD/FSD/EMSD/WSD/LD and estate rules where applicable.
4. HKRG/HKEDCA contract templates require legal review before issue — do not release verbatim without adaptation.
5. HKIDA/HKRIDA educational guidance and model consultancy agreements are also non-statutory sources. Adapt model terms with legal review; historical fee, notice, liability, registration and CPD provisions are not current universal requirements. Apply the actual contract's precedence and appointment authority. See [hkrida-professional-practice.md](hkrida-professional-practice.md).

## Hard stops (halt and offer remediated options)

| Condition | Action |
|-----------|--------|
| Egress/fire/accessibility breach without AHJ variation path | Halt; cite rule; propose compliant alternatives only |
| Gas hob removal or installation without registered gas contractor | Halt; require registered contractor per HKEDCA |
| On/off shower head or outlet shutoff valve proposed for a shower-type (low-pressure storage) electric water heater | Halt this installation; use the specified unrestricted outlet and competent supplier/installer review. Closing the main tap afterwards does not cure the incompatibility. See [EMSD guidance](https://www.emsd.gov.hk/en/electricity_safety/publications/guidance_notes_guidelines/safety_tips_for_using_electric_water_heaters/index.html), checked 2026-11-07, and [fixture checks](deco-fixtures-and-retained-services.md). |
| Scaffold/bamboo works without engineer design or inspection cadence | Halt; stop exterior works until compliant |
| Typhoon/cyclone signal active for scaffold/WAH | Halt exterior height works |
| Fire/alarm triggering works without management **掛牌** isolate | Halt until alarm isolate confirmed |
| Unauthorized demolition or breach of estate renovation approval | Halt; reinstatement per contract |
| Structural concrete repair (士波令), balcony glass-barrier replacement, or removal of HOS/MIC module walls without AP/RSE and estate or Housing Authority approval | Halt; do not specify the repair, the anchor, or the demolition. Offer the AP/RSE and approval path only |
| Leaded solder proposed for potable-water pipe joints | Halt; require documented lead-free materials and the licensed-plumber/WSD approval and testing route. Tissue-rub, colour or insertion-depth claims do not establish safety. See [potable-water solder evidence](deco-repair-and-materials.md#potable-water-solder-evidence--safety-gate). |
| User requests licensed professional sign-off or statutory submission as agent | Halt; state advisory-only boundary |
| Missing critical inputs when `strict_mode` is true (occupancy, jurisdiction, scale) | Halt; list gaps before analysis |

## Quantitative thresholds

| Metric | Threshold | Source |
|--------|-----------|--------|
| Floor finish level delta at transition | Flag if > 3 mm | SKILL §1.4 |
| Open office RT60 | 0.5–0.8 s | SKILL §1.7 |
| Meeting room partition STC/Rw | 45+ | SKILL §1.7 |
| Quiet room partition STC/Rw | 50+ | SKILL §1.7 |
| Absorptive ceiling/baffle NRC | 0.70+ | SKILL §1.7 |
| HK scaffold harness anchor | ≥ 6 kN | interior-fire-life-safety |
| BOQ line variance (tender review) | Flag if > 5% without explanation | operational.md |
| Office workstation illuminance | 300–500 lux maintained | SKILL §1.6 |

## Hong Kong application of overseas sources

US textbook dimensions/codes and generic calculators do not establish HK compliance. Use [Ching HK adaptation](ching-hk-adaptation.md) to identify the local source, scope and edition. In particular, distinguish existing B(P)R accessibility duties from advisory DMUA 2026 provisions under APP-176; publication or an “obligatory” heading alone does not establish enactment. All existing hard stops continue to apply.
