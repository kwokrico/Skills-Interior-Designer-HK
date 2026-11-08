# HKRIDA coverage audit — 2026-11-06

## Scope and conclusion

Reviewed all seven files named in `Reference/HKRIDA` through extraction, contents/chapter mapping, targeted full-page text reading and visual checks. Total: 486 PDF pages. The skill already contained strong technical routing for fire, compliance, MEP, acoustics, procurement, joinery, tender, site and handover, but did not adequately cover the six-domain educational framework or the research, communication and professional-practice workflows. Coverage was partial in every volume; these gaps are now supplemented. This is reusable-practice coverage, not a claim that every historical fact, interview or model clause has been copied or verified.

Inventory, full chapter disposition and page locators: [HKRIDA-INDEX.md](HKRIDA-INDEX.md). All original PDFs and page-numbered extracts: [SS/HKRIDA](SS/HKRIDA/).

## Integration record

| Gap | Change |
|---|---|
| Brief/user research, contextual precedent, concept across scales and competence/education | Added `references/hkrida-design-research-communication.md`; router handles these requests directly |
| Ethics, conflicts, consultant vs contractor appointments, six agreement schedules, PM authority, delivery method, tender contents and specification types | Added `references/hkrida-professional-practice.md`; linked from tender and site modules |
| Perception/thermal factors, seven universal-design principles, user trials and POE | Added ergonomics `references/hkrida-human-environment.md`; handover link separates POE from DLP |
| Wider material families, standards evidence, emerging products and claim limits | Added procurement `references/hkrida-materials-evidence.md` |
| Lighting distribution, surface interaction and product-selection record | Expanded lighting module; corrected illuminance/luminance distinction |
| Approval layers, food/care licensing and adaptive reuse | Added statutory `references/hkrida-licensing-adaptive-reuse.md` with official-source pointers |
| Lifecycle assessment/energy/cost, adaptability and post-occupancy evaluation | Added sustainability `references/hkrida-lifecycle-evaluation.md` |
| Usable records and vocabulary | Expanded deliverables catalog, domain terms, compliance boundary and source register |

## Claims qualified or excluded

- **Source status:** government funding is not government endorsement or law. The Professional Guideline is ©2014; six knowledge volumes are ©2020. Upload-like filename dates are not editions.
- **Qualifications/CPD:** proposed durations, qualification levels, logbooks, historical international registration rules and CPD/CEU tables are not asserted as current HK legal requirements.
- **Contract documents:** the Professional Practice volume PDF p. 27 says specifications prevail over drawings. The integration requires the actual contract's precedence and a discrepancy record instead.
- **Contract defaults:** seven-day payment/notice examples, deposits, fixed fees despite reduced scope, liability caps and dispute forums belong to dated model clauses. They are not automatically adopted or declared enforceable. HKIAC in the consultancy source is not HKAS in HKRG.
- **AP signatures:** Communication PDF p. 5 overgeneralises AP-stamped documents. BD's domestic alterations FAQ distinguishes exempted works, prescribed minor works and other alterations; determine the actual route. Existing safety halts remain unchanged.
- **Glass:** Products PDF pp. 23–24 mixes glass treatment/type examples and makes an overly broad recommendation against toughened glass. Do not adopt it. Thermal toughening is described by Pilkington's primary product guidance; the actual use, impact, support, retention and installed system govern selection. No barrier design provided.
- **Standards:** a BS installation code is not itself product certification; ISO 9001 management-system certification is not a product-performance certificate, and CE is not a generic quality mark or HK approval. Historic editions remain dated examples.
- **Environment:** bio-based does not establish biodegradability or actual composting/recycling availability. Nanotechnology, 'air-purifying', antimicrobial, permanent-coating, generic insulation multipliers and comparative carbon claims need product/use-specific evidence. No health protection, zero-emission, certification or maintenance-free promise adopted.
- **Lighting:** the incident/observed-light terminology on Products PDF p. 46 is not carried forward; the skill distinguishes lux from luminance. Historical lamp comparisons are not current procurement data.
- **Cases/opinions:** design histories, firm interviews, pre-modernism, dress etiquette, survey counts and foreign professionalisation inform context; they do not establish universal aesthetics, commercial rules or HK law.

Official/manufacturer sources used for the corrections are linked in the relevant new references and were checked on 2026-11-06. The audit does not revalidate every historical code clause or scheme credit; those are explicitly excluded from live numerical guidance.

## Extraction and review limits

Pypdf and PDFium text extraction were used; PDFium supplies the archived page-numbered text. Contact sheets were rendered to identify figure-only and image-only content and inspect representative technical/communication pages. Table columns and diagrams must be read in the PDF before numerical reliance.

Professional Practice PDF pp. 60–87 is an image-only Chinese consultancy agreement appendix: it was visually identified but has no reliable automatic text extraction. Readable G pp. 31–40 supplies related consultancy-agreement themes; do not infer that the two versions are identical. Products PDF pp. 67–72 contains a mostly image-based lighting glossary. These pages have archived PNG extracts for inspection; they were not transcribed as new numerical or contractual rules. Short cover/figure-only pages are enumerated in the manifest. No claim of exhaustive OCR or independent legal clause certification is made.

## Verification

The final validation record is in `HKRIDA-VALIDATION-2026-11-06.json`: archive hashes/counts, local links introduced in this change, JSON parsing, skill frontmatter, dispatcher availability and reference discovery. Golden prompts were extended for the new workflows. Structural/routing checks and manual scenario walkthroughs do not establish an independently run model-behaviour evaluation; no such score is claimed.

## Archive

After extraction, integration and checks, the named source folder is moved to `Reference/SS/HKRIDA`, preserving all seven original PDF filenames. The archive also contains seven `.txt` extracts, extraction provenance/hashes and image-only page extracts. Indexes, audit notes and skill files stay outside the source archive, per `.cursor/rules/source-archive.mdc`.
