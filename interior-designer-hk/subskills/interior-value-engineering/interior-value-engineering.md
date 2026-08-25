---
name: interior-value-engineering
description: >
  Budget alignment through technically valid Good-Better-Best alternatives.
  Use for cost pressure, scope trade-offs, and VE comparisons preserving intent.
disable-model-invocation: true
---

# interior-value-engineering

For supply feasibility of VE options, use `interior-material-procurement` instead.  
For tender reissue impact, use `interior-tendering-qa` instead.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Cost alternatives, G-B-B comparison | `interior-value-engineering` | — |
| Lead time / batch validation | Chain to | `interior-material-procurement` |
| Code-sensitive VE element | Chain to | `interior-statutory-compliance` |
| HK 另收費項目 scope control | This skill + HKRG ref | `interior-site-supervision` |

## Purpose
Use for budget alignment through technically valid alternatives that preserve core design intent.

## Core Outputs
- Good-Better-Best option set per cost hotspot.
- Cost/risk/performance comparison narrative.
- Recommendation with scope impact and approval note.

## Reference Table: Good-Better-Best Protocol
| Tier | Definition |
|---|---|
| Good | Meets minimum performance and code at lowest cost |
| Better | Balanced cost with improved durability/appearance |
| Best | Highest performance/longevity with premium cost |

## Decision Rules
1. Never downgrade below compliance or functional requirement.
2. State what design quality is preserved vs traded off.
3. Coordinate sourcing feasibility with `interior-material-procurement`.

### HKRG cross-reference (Hong Kong)

- Use `interior-site-supervision/references/hkrg-renovation-essentials-trades.md` **另收費項目** as VE scope-control checklist — confirm variations are priced before work (`HKRG §裝修需知/1.1`).
- Route contract/payment disputes to `interior-tendering-qa` + `hkrg-standard-quotation-contract.md` clause 14.

## Region-Switch Notes (HK / Mainland China)
- Hong Kong mode: prioritize alternatives with proven local installer familiarity and supply certainty.
- Mainland mode: prioritize alternatives with compliant local certification and stable regional supply.
- If region unknown, provide options tagged by import dependence and approval risk.

## Reference Table: Typology VE Strategy
| Typology | Preferred VE Direction |
|---|---|
| Residential | Optimize hidden substrates before visible signature elements |
| Workplace | Standardize repeated modules to reduce fabrication variance |
| Retail | Protect customer-facing finishes; value engineer back-of-house first |
| Hospitality | Protect brand-defining touchpoints; optimize secondary zones |

## Auto-Chain Directives (Deterministic Schema)
| Trigger | Chain | Output format |
|---|---|---|
| VE option requires real lead-time and batch validation | `interior-material-procurement` | `SUPPLY CHECK -> LEAD-TIME DELTA -> ACCEPT/REJECT RATIONALE` |
| VE change requires reissue or clarification | `interior-tendering-qa` | `DOCUMENT IMPACT LIST -> REISSUE SCOPE -> CLARIFICATION TEXT` |
| VE option touches code-sensitive element | `interior-statutory-compliance` | `COMPLIANCE RISK -> REQUIRED CHECKS -> CONDITIONAL APPROVAL NOTES` |

## Parent references

Load from parent references/ when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [deliverables.md](../../references/templates/deliverables.md) — output catalog

