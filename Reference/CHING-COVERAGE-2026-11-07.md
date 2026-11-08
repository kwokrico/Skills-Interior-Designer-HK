# Ching and Binggeli coverage review — 2026-11-07

Source: *Interior Design Illustrated*, third edition, Francis D.K. Ching and Corky Binggeli, Wiley, copyright 2012. Original filename retains its spelling: [archived PDF](<SS/Francis D.K. Ching & Corky Binggeli - INTERIOR DESING ILLUSTRATED (3rd Edition).pdf>).

## Method and limits

Extracted the PDF's text across all 386 pages with pypdf and inventoried chapter/page headings. Compared chapter themes and selected substantive passages with the existing master router, shared references and specialist modules. Rendered and visually inspected representative PDF pages 5, 77, 113, 125, 137, 145, 257 and 349 (contents, flexible layout, solid/void, colour, scale, harmony, vision and storage). [Extraction and rendered pages](SS/Ching-extract/) preserve the evidence; [manifest](CHING-ARCHIVE-MANIFEST-2026-11-07.json) records hashes and extraction coverage.

This is a chapter/topic coverage review with targeted passage and illustration checks, not a line-by-line technical validation of every diagram or numerical value. Extraction is not OCR; an empty text page does not establish that its visual content is empty. Page text can interleave diagram labels and contain broken words, spacing or apparent unit mismatches. Consult the original image before relying on a specific detail. Printed body page numbers are PDF page numbers minus 8.

## Coverage and disposition

“Covered” below means reusable subject coverage exists, not that every textbook example has been reproduced.

| Chapter; printed / PDF pages | Existing coverage | Gap and action |
|---|---|---|
| 1 Interior Space; 1–34 / 9–42 | Anthropometrics, interface, thickness, MEP and statutory modules address physical constraints | Partial: added enclosure, geometry, vertical scale, transitions and mass/void reading in **spatial composition** |
| 2 Interior Design; 35–82 / 43–90 | HKRIDA design research/communication covers briefing, activity/adjacency, options, representations and approval; human-environment reference covers users | Partial: added tight/loose fit and future-use testing; retained existing process rather than duplicating it. Human dimensions remain illustrative, not current legal minima |
| 3 A Design Vocabulary; 83–146 / 91–154 | Broad concept/precedent and lighting guidance existed, but little explicit compositional method | Added form, figure/ground, texture, hue/value/saturation, proportion/scale, balance, harmony/variety, rhythm and emphasis with an actionable critique workflow |
| 4 Interior Building Elements; 147–218 / 155–226 | Interface, millwork, thickness, MEP, statutory and fire modules cover assemblies/openings/services coordination | Technical topics substantially covered; added spatial implications to composition. Do not adopt structural sketches, stair/ramp/elevator dimensions, fireplace or wood-stove details as HK construction instructions |
| 5 Interior Environmental Systems; 219–246 / 227–254 | MEP, sustainability/wellness, fire and statutory modules, plus DECO HVAC reference | Covered at practice-routing level. Historical electrical/code conventions and illustrative plumbing dimensions excluded from specification |
| 6 Lighting and Acoustics; 247–286 / 255–294 | Lighting science and acoustic engineering cover metrics, visual comfort, absorption/transmission and assembly checks | Added composition-facing light/material relationships; keep specialist modules for calculations. Historical lamp comparisons and efficiency/lifetime data excluded |
| 7 Finish Materials; 287–316 / 295–324 | Procurement, finish-selection field notes, HKRIDA materials evidence, interface and thickness modules | Covered at selection/specification level. No family-wide performance, prescribed buildup or maintenance claims imported; named product/assembly evidence remains necessary |
| 8 Furnishings; 317–352 / 325–360 | Anthropometrics, residential FF&E fit, procurement and millwork | Partial: added activity groupings, movable/built-in/modular tradeoffs, inventory-based storage, window-treatment coordination and accessory planning |
| Appendix; 353–360 / 361–368 | Sustainability/wellness and HKRIDA lifecycle evaluation | Historical certification reference only; LEED-CI 2009 and LEED for Homes 2008 points/thresholds not adopted as current schemes |
| Glossary, bibliography, index; 361 onward / 369–386 | Domain terms and source register | Used as navigation/background; no need to duplicate the book's full glossary or index |

## Integration locations

- [Spatial composition and visual design](../interior-designer-hk/references/ching-spatial-composition.md): source locators and original synthesis of the missing design principles.
- [Furnishings, storage and window treatments](../interior-designer-hk/references/ching-furnishings-and-window-treatments.md): chapter 8 synthesis and coordination checklist.
- [Master router](../interior-designer-hk/SKILL.md), HKRIDA design-research reference, and anthropometrics, lighting, procurement, millwork and brand/environmental-graphics modules now link the relevant addition.
- [Source register](../interior-designer-hk/references/source-register.md) points to archived sources; [evaluation prompts](../interior-designer-hk/evals/evals.json) add `ching-composition` and `ching-furnishings`.

## Exclusions and reliability controls

The book is educational and largely US-oriented. It is not an HK statutory source. Do not promote its example dimensions, drawings, electrical conventions, code summaries or old certification tables into current HK requirements. Do not use broad countertop/material claims as proof of a named product's thermal, hygienic, water, fire or maintenance performance. Colour effects and aesthetic ratios remain contextual design tools.

The extracted bathing/fixture diagrams (for example PDF pages 64 and 243) have apparent dimension/unit or label-association problems; no such values were integrated. Likewise, the structural and fireplace drawings are context for spatial coordination, not sufficient design authority. No current product, code or certification verification was undertaken because these claims were excluded rather than adopted.

## Verification and archive

Archive occurs after integration, following `.cursor/rules/source-archive.mdc`. The original PDF moves directly into `Reference/SS` with its filename preserved. The extraction folder moves intact to `Reference/SS/Ching-extract`. Hash verification and structural-check results are recorded in the manifest. Coverage audit and manifest remain outside the archive as working indexes.

Structural checks cover JSON parsing, unique evaluation IDs, links in changed Markdown files and successful dispatch of affected modules. These are not behavioural model evaluations; the two new prompts remain unexecuted scenarios.
