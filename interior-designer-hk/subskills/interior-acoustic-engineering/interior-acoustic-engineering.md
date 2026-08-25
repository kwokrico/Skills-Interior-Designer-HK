---
name: interior-acoustic-engineering
description: >
  NRC, STC/Rw, RT60 planning and acoustic assembly strategy.
  Use for speech privacy, reverberation control, and flanking-path risks.
disable-model-invocation: true
---

# interior-acoustic-engineering

For ceiling/service zone conflicts with baffles, use `interior-mep-clash-detection` instead.  
For lighting compensation after acoustic treatment, use `interior-lighting-science` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| RT60, STC/Rw, NRC targets | `interior-acoustic-engineering` | — |
| Baffle vs duct/sprinkler clash | Pair with | `interior-mep-clash-detection` |
| Acoustic product lead time | Chain to | `interior-material-procurement` |

## Purpose
Use for acoustic performance planning, including envelope/partition targets and reverberation control.

## Core Outputs
- Recommended NRC/STC/RT targets by room type.
- Acoustic assembly strategy (partition, ceiling, floor, doors).
- Risk notes for flanking paths and service penetrations.

## Reference Table: Acoustic Targets by Space and Typology

| Context | Space / typology | Target / goal |
|---------|------------------|---------------|
| Workplace | Open office | RT60 0.5–0.8 s |
| Workplace | Meeting room | STC/Rw 45+ |
| Workplace | Private room | STC/Rw 50+ |
| All | Absorptive ceiling/baffle | NRC 0.70+ |
| Residential | Inter-unit / bedroom | Inter-unit privacy and bedroom quietness |
| Retail | Sales floor | Noise moderation without killing merchandising energy |
| Hospitality | Dining/lounge | Comfort and intimacy |

## Decision Rules
1. Prioritize speech privacy and intelligibility criteria by use case.
2. Call out all penetrations that reduce effective rating.
3. Coordinate acoustic baffles and soffits with `interior-mep-clash-detection`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: use project acoustic criteria plus local authority/environmental constraints where applicable.
- Mainland mode: align with PRC acoustic standards and local submission expectations.
- If jurisdiction unclear, provide performance targets first and mark standard mapping as pending.

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Baffle/ceiling zone has service conflict | `interior-mep-clash-detection` | `CLASH LOCATIONS -> PRIORITY RESOLUTION -> SPACE CLAIM NOTES` |
| Acoustic treatment changes luminous performance | `interior-lighting-science` | `LIGHTING EFFECT -> COMPENSATION STRATEGY -> UPDATED TARGETS` |
| Acoustic product lead-time/availability risk appears | `interior-material-procurement` | `PROCUREMENT RISK -> ALTERNATIVE OPTIONS -> PROGRAM IMPACT` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

