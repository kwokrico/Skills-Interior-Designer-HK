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

## Hard stops (halt and offer remediated options)

| Condition | Action |
|-----------|--------|
| Egress/fire/accessibility breach without AHJ variation path | Halt; cite rule; propose compliant alternatives only |
| Gas hob removal or installation without registered gas contractor | Halt; require registered contractor per HKEDCA |
| Scaffold/bamboo works without engineer design or inspection cadence | Halt; stop exterior works until compliant |
| Typhoon/cyclone signal active for scaffold/WAH | Halt exterior height works |
| Fire/alarm triggering works without management **掛牌** isolate | Halt until alarm isolate confirmed |
| Unauthorized demolition or breach of estate renovation approval | Halt; reinstatement per contract |
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
