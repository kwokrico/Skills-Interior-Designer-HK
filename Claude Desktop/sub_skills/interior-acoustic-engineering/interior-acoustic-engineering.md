# interior-acoustic-engineering

## Purpose
Use for acoustic performance planning, including envelope/partition targets and reverberation control.

## Core Outputs
- Recommended NRC/STC/RT targets by room type.
- Acoustic assembly strategy (partition, ceiling, floor, doors).
- Risk notes for flanking paths and service penetrations.

## Reference Table: Typical Acoustic Targets
| Space | Target |
|---|---|
| Open office | RT60 0.5-0.8 s |
| Meeting room | STC/Rw 45+ |
| Private room | STC/Rw 50+ |
| Absorptive ceiling/baffle | NRC 0.70+ |

## Decision Rules
1. Prioritize speech privacy and intelligibility criteria by use case.
2. Call out all penetrations that reduce effective rating.
3. Coordinate acoustic baffles and soffits with `interior-mep-clash-detection`.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: use project acoustic criteria plus local authority/environmental constraints where applicable.
- Mainland mode: align with PRC acoustic standards and local submission expectations.
- If jurisdiction unclear, provide performance targets first and mark standard mapping as pending.

## Reference Table: Typology Acoustic Targets
| Typology | Primary Acoustic Goal |
|---|---|
| Residential | Inter-unit privacy and bedroom quietness |
| Workplace | Speech privacy + distraction control in open zones |
| Retail | Noise moderation without killing merchandising energy |
| Hospitality | Comfort and intimacy in dining/lounge zones |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| Baffle/ceiling zone has service conflict | `interior-mep-clash-detection` | `CLASH LOCATIONS -> PRIORITY RESOLUTION -> SPACE CLAIM NOTES` |
| Acoustic treatment changes luminous performance | `interior-lighting-science` | `LIGHTING EFFECT -> COMPENSATION STRATEGY -> UPDATED TARGETS` |
| Acoustic product lead-time/availability risk appears | `interior-material-procurement` | `PROCUREMENT RISK -> ALTERNATIVE OPTIONS -> PROGRAM IMPACT` |
