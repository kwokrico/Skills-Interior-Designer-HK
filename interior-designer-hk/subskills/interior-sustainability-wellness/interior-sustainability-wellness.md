---
name: interior-sustainability-wellness
description: >
  Low-VOC materials, WELL/LEED/BEAM Plus alignment, and biophilic strategies.
  Use for sustainability targets and wellness certification planning.
disable-model-invocation: true
---

# interior-sustainability-wellness

For HK application of overseas textbook examples, read [Hong Kong adaptation](../../references/ching-hk-adaptation.md): accessibility/legal status, fire/stairs/barriers, daylight, services, energy, IAQ and certification. Confirm scope and edition before adopting a dimension or performance claim.

For material sourcing and lead times of certified products, use `interior-material-procurement` instead.  
For VE when sustainability premium exceeds budget, use `interior-value-engineering` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| WELL/LEED/BEAM+, VOC, biophilia | `interior-sustainability-wellness` | — |
| Certified product availability | Chain to | `interior-material-procurement` |
| Cost trade-off on green options | Chain to | `interior-value-engineering` |

## HK Local Practice

- BEAM Plus and local material certification paths differ from US/EU frameworks — map credits explicitly.
- Pair with `interior-statutory-compliance` when wellness claims touch ventilation or IEQ submissions.

## Purpose

For reuse/adaptability, LCA, LCEA, LCC, post-occupancy evaluation or rating evidence, read [hkrida-lifecycle-evaluation.md](references/hkrida-lifecycle-evaluation.md). Use the selected scheme's actual current version rather than historical textbook credits.
Use for sustainability and wellness-driven interior choices across material, air, light, and occupant experience.

## Core Outputs
- Low-impact material strategy (VOC, recycled, durability).
- Wellness-focused design recommendations (air, light, comfort, biophilia).
- Credit-alignment guidance (LEED/WELL/BEAM Plus style frameworks).

## Reference Table: Wellness Design Controls
| Domain | Practical Control |
|---|---|
| Materials | Low-VOC paints, adhesives, sealants |
| Air quality | Source control + ventilation strategy coordination |
| Light | Circadian-supportive CCT/intensity by time/use |
| Nature connection | Biophilic elements with maintainable species selection |

## Decision Rules
1. Prefer measurable performance over purely narrative claims.
2. Ensure sustainable alternatives still meet durability and code.
3. Coordinate with procurement for availability and lead-time risk.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: align with project-selected sustainability framework and local material availability constraints.
- Mainland mode: align with PRC implementation standards and local certification pathways.
- If region unclear, provide framework-agnostic performance strategy and tag regional credits for confirmation.

## Reference Table: Typology Sustainability Focus
| Typology | Sustainability/Wellness Focus |
|---|---|
| Residential | Low-VOC finishes and healthy indoor baseline comfort |
| Workplace | IAQ strategy, visual comfort, and occupant wellness metrics |
| Retail | Durable low-impact materials for high-traffic turnover |
| Hospitality | Wellness narrative with maintainable biophilic integration |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| HK BEC applicability, major retrofitting, central services or phased services replacement | `interior-mep-clash-detection` (also read its instructions); add statutory compliance for legal applicability | `SERVICES SCOPE -> BEC APPLICABILITY GAPS -> REA REVIEW INPUTS` |
| EPD/VOC/supply certainty data is required | `interior-material-procurement` | `MATERIAL DATA REQUEST -> COMPLIANCE EVIDENCE -> PROCUREMENT RISK` |
| Circadian-supportive lighting strategy is needed | `interior-lighting-science` | `WELLNESS LIGHTING TARGETS -> FIXTURE/CONTROL STRATEGY -> PERFORMANCE NOTES` |
| Sustainability intent is challenged by budget pressure | `interior-value-engineering` | `SUSTAINABILITY-VE MATRIX -> TRADE-OFF NOTES -> RECOMMENDED OPTION` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog



For feature finishes, overlays, skirting, flooring/cleaning demonstrations or flood-test claims, read [deco-finish-evidence-and-maintenance](../../references/deco-finish-evidence-and-maintenance.md).


## Tim Ho field review

Read the applicable supplement for detailed checks and qualified source evidence: [finishes and home use](../../references/tim-ho-finishes-and-home-use.md).
