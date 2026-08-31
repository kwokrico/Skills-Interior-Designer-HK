---
name: interior-designer-skill
overview: Create a new master `SKILL.md` for Claude Code tailored to a global, full-service professional interior designer, using the provided architect skill as structural reference while replacing architecture-specific content with interior design workflows and standards.
todos:
  - id: outline-sections
    content: Draft mirrored section skeleton from architect reference adapted to interior design master-skill framing.
    status: completed
  - id: build-quick-reference
    content: Populate interior-focused quick-reference tables and critical default metrics with AHJ caveats.
    status: completed
  - id: design-routing-tree
    content: Create interior sub-skill decision tree and multi-skill priority hierarchy.
    status: completed
  - id: define-dispatcher-tools
    content: Specify sub-skill loader and optional calculator tool interface for interior workflows.
    status: completed
  - id: final-polish
    content: Normalize terminology, ensure global applicability, and prepare final `SKILL.md` wording.
    status: completed
isProject: false
---

# Professional Interior Designer Master Skill Plan

## Goal
Produce a production-ready `SKILL.md` that activates for interior design queries and routes to specialized sub-skills, matching the clarity and depth of the architect reference while focusing on global interior design practice.

## Target File
- [Claude Desktop/SKILL.md](Claude Desktop/SKILL.md)

## Planned Structure
- Frontmatter (`name`, `description`) rewritten for interior design domain and trigger terms.
- `# Interior Designer Master Suite` intro framing this as the central router.
- `## 1. Foundation Quick Reference` with practical, high-frequency guidance for interiors.
- `## 2. Routing Decision Tree` that dispatches to interior-specific sub-skills.
- `## 3. Dispatcher Tools` defining `load_sub_skill` and optional calc utility hooks.
- Closing source notes adapted to global references (e.g., IBC/NFPA/ADA/ISO/WELL/LEED/BIFMA/FIDIC where applicable).
- `Dispatcher Tools` will also include explicit scale-context rules for detailing, VE routing, and ceiling/services clash hierarchy.

## Foundation Content to Include
- Typical dimensional standards:
  - ceiling heights by typology,
  - circulation/clearance standards,
  - door/corridor/egress-width quick numbers,
  - accessible turning radii and reach ranges.
- Build-up calculator logic:
  - floor-finish transition equalization (e.g., stone-on-bed to carpet-on-pad),
  - threshold planning rules to prevent level mismatch at doors,
  - prompt-time checks that flag likely "bump at the door" conditions.
- Scale-to-information mapping table:
  - 1:100 / 1:50 = planning and general arrangement response depth,
  - 1:20 = assembly-level coordination depth,
  - 1:10 / 1:5 = joinery/details/spec-ready response depth,
  - token discipline guidance so output LOD matches requested scale.
- Program + planning quick tables:
  - space allocation benchmarks (office, retail, hospitality, residential),
  - occupancy load and seating/queuing assumptions,
  - front-of-house vs back-of-house ratios.
- Technical quick references:
  - reflected ceiling/service coordination principles,
  - lighting level ranges (lux) by room type,
  - acoustic target ranges (NRC/STC/RT60 guidance),
  - core material performance and fire classification reminders,
  - standard market thickness reference (e.g., 12.5mm gypsum, 18mm MDF, 12mm glass) for feasibility checks.
- Delivery and compliance milestones:
  - concept, SD, DD, CD, tender, site admin, punch list, handover.

## Routing Taxonomy (Interior-Focused)
Use this categorized taxonomy for routing so each query maps to the right project-stage mental model:

- Technical Performance & Compliance:
  - interior-fire-life-safety
  - interior-mep-clash-detection
  - interior-statutory-compliance
  - interior-acoustic-engineering
- Materiality & Build-Up:
  - interior-material-procurement
  - interior-interface-detailing
  - interior-thickness-build-up
  - interior-millwork-technical
- Logistical & Commercial Management:
  - interior-value-engineering
  - interior-tendering-qa
  - interior-site-supervision
  - interior-handover-dlp
- Human-Centric Design & Typology:
  - interior-anthropometrics-ergonomics
  - interior-lighting-science
  - interior-brand-environmental-graphics
  - interior-sustainability-wellness

When a query is ambiguous, enforce this priority order:
1. Regulatory/Safety (is it legal?)
2. Technical/Structural (is it buildable?)
3. Human/Functional (does it fit the body/use?)
4. Aesthetic/Stylistic (does it look right?)

- Add explicit interdisciplinary clash routing:
  - if prompt includes ceiling height + ducting + sprinklers, invoke both `interior-mep-coordination` and `interior-fire-life-safety`,
  - define conflict-resolution order (life safety first, then services coordination, then design intent).

## Dispatcher Tools Logic to Include
- Add a `dispatcher_logic` block so routing explicitly understands scale context and commercial intent:

```xml
<dispatcher_logic>
  <context_rule trigger="Detailing / Joinery / Construction">
    Route to: interior-materials-finishes + interior-visualization-documentation
    Apply Scale: 1:5 or 1:10
  </context_rule>
  <context_rule trigger="Budget / VE / Alternative">
    Route to: interior-cost-procurement
    Protocol: Good-Better-Best Comparison
  </context_rule>
  <context_rule trigger="Ceiling / Services / Clashes">
    Route to: interior-mep-coordination
    Hierarchy: FS > P&D > HVAC > Electrical
  </context_rule>
</dispatcher_logic>
```
- Ensure this logic is reflected both in human-readable decision tree text and tool-level routing instructions.
- Ensure skill IDs in dispatcher logic match final taxonomy names (e.g., `interior-mep-clash-detection` vs. legacy naming).
- Require each sub-skill definition to include at least one standard reference table for consistent, auditable outputs.
- Include a canonical XML pattern in the generated `SKILL.md`:

```xml
<subskill id="interior-interface-detailing">
  <reference_table name="Threshold Transitions">
    <entry type="Stone to Carpet">Use 3mm brass "L" profile; ensure mortar bed is recessed 15mm.</entry>
    <entry type="Timber to Tile">Use T-profile expansion joint; allow 5mm for seasonal movement.</entry>
  </reference_table>
</subskill>
```

## Authoring Rules
- Keep concise, operational language suitable for production use by Claude Code.
- Preserve “answer from Section 1 first; route only when deeper expertise needed” behavior.
- Use neutral global wording; avoid single-jurisdiction lock-in.
- Keep numbers as practical defaults with caution notes that local authority having jurisdiction (AHJ) prevails.
- Prioritize structural/code integrity over aesthetic drift: if a style request conflicts with life safety/access/egress, flag compliance issue first.
- Use implicit scaling defaults when user does not specify scale:
  - default to 1:50 for layouts/planning,
  - default to 1:5 for joinery/detailing.

## Quality Checks Before Finalizing Draft
- Ensure the file is self-contained and immediately usable as a master hub.
- Verify decision tree covers major interior design intents without overlap confusion.
- Confirm quick-reference tables are practical and not over-legalistic.
- Confirm sub-skill IDs are internally consistent with dispatcher section.
- Confirm material-thickness assumptions are realistic and catch impossible assemblies early.
- Confirm delivery "last mile" includes millwork inspection protocol (grain matching, hardware clearance, scribing) and O&M manual handover requirements.
- Discrepancy resolution: when as-built site condition conflicts with contract drawing, confirm workflow prioritizes field measurement and issues Site Instruction (SI) before updating downstream documents.