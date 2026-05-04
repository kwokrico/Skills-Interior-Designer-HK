---
name: interior-designer-master
description: >
  Activate for ANY professional interior design question across residential, workplace,
  retail, hospitality, and mixed-use fit-outs. Trigger when the query involves:
  planning layouts, anthropometrics, accessibility, occupancy loads, life safety and egress,
  reflected ceiling plans, MEP coordination, clash detection, materials and finishes,
  thickness build-up, joinery detailing, millwork, FF&E, lighting metrics (CCT/CRI/UGR/lux),
  acoustics (NRC/STC/RT60), tendering QA, value engineering, procurement lead times,
  site supervision, snagging, as-built discrepancies, SI workflows, O&M manuals,
  handover, DLP, and sustainability/wellness (LEED/WELL/BEAM Plus equivalents).
  When in doubt, activate — this is the master hub for full-service interior practice.
---

# Interior Designer Master Suite

Central intelligence hub and mandatory router for professional interior design.  
Provides a fast **Foundation Quick Reference** for common questions, then dispatches to specialist sub-skills when deeper expertise is needed.

---

## 1. Foundation Quick Reference

Answer routine questions directly from this section **before** loading a sub-skill.

### 1.1 Typical Clear Height Targets

| Space Type | Typical Finished Clear Height |
|---|---|
| Residential living/bedroom | 2.5-2.8 m |
| Office open workspace | 2.7-3.0 m |
| Retail sales floor | 3.0-4.5 m |
| Hospitality lobby | 3.6-6.0 m |
| Back-of-house/service corridors | 2.4-2.7 m |

> Verify against local code and landlord/base-build constraints. AHJ minimums override these defaults.

### 1.2 Egress + Accessibility Quick Numbers (Global Defaults)

| Parameter | Typical Baseline |
|---|---|
| Min clear egress door width | 850-900 mm |
| Min main corridor clear width | 1200 mm |
| Preferred two-way corridor | 1500 mm |
| Wheelchair turning circle | 1500 mm diameter |
| Accessible door maneuvering side | 300-600 mm latch-side clearance (jurisdiction dependent) |
| Max dead-end corridor (unsprinklered typical) | 6-9 m (jurisdiction dependent) |

### 1.3 Scale-to-Information Mapping (Implicit LOD Control)

| Requested Scale | Response Depth (LOD) | What to Provide |
|---|---|---|
| 1:100 / 1:50 | Planning / layout | zoning, circulation, room logic, key dimensions |
| 1:20 | Assembly coordination | wall build-up, service zones, key interfaces |
| 1:10 / 1:5 | Detail / joinery | sections, fixing intent, tolerances, material transitions |

> If user does not specify scale: default to **1:50** for layouts and **1:5** for joinery/detailing.

### 1.4 Build-Up Logic (Avoid "Bump at the Door")

| Finish Type | Typical Build-Up Depth |
|---|---|
| Stone tile + mortar bed | 30-45 mm |
| Porcelain tile + adhesive | 12-20 mm |
| Engineered timber on underlay | 12-18 mm |
| LVT + adhesive | 4-7 mm |
| Carpet tile + adhesive | 6-10 mm |
| Carpet + underpad | 10-18 mm |

**Rule:** resolve adjacent finish level difference at transitions using one of: substrate recess, screed ramp, threshold profile, or finish substitution.  
Always issue a transition detail when level delta > 3 mm.

### 1.5 Standard Market Thicknesses (Feasibility Guardrail)

| Material | Common Market Thickness |
|---|---|
| Gypsum board | 9.5 / 12.5 / 15 mm |
| MDF | 12 / 15 / 18 / 25 mm |
| Tempered glass | 10 / 12 mm |
| Plywood | 12 / 18 mm |
| Quartz/solid surface | 12 / 20 mm |

> Flag impossible assemblies early (example: "10 mm full wall partition housing 12 mm glass + studs").

### 1.6 Lighting Science Quick Ranges

| Area Type | Target Illuminance (Lux) | CCT Guidance | Notes |
|---|---|---|---|
| Residential living | 100-300 | 2700-3000K | warm layered lighting |
| Office workstation | 300-500 | 3500-4000K | glare control critical |
| Retail merchandising | 500-1000 | 3000-4000K | accent + contrast |
| Hospitality dining | 100-250 | 2200-3000K | dimming + mood |

### 1.7 Acoustic Quick Targets

| Condition | Typical Target |
|---|---|
| Open office reverberation (RT60) | 0.5-0.8 s |
| Meeting room partition | STC/Rw 45+ |
| Quiet room partition | STC/Rw 50+ |
| Absorptive ceiling/baffle | NRC 0.70+ |

### 1.8 Program Benchmarks (Rule-of-Thumb)

| Typology | Typical Net Area Allocation |
|---|---|
| Office workstation | 6-10 m2 per person |
| Restaurant dining | 1.2-1.8 m2 per seat |
| Retail sales | 60-75% FOH, 25-40% BOH |
| Hospitality guestroom floor | 65-80% keys, 20-35% support/circulation |

### 1.9 Delivery Milestones

| Stage | Core Deliverables |
|---|---|
| Concept | adjacency, narrative, mood, test-fit |
| SD | planning set, preliminary RCP/MEP intent |
| DD | coordinated details, materials, schedules |
| CD | issue-for-tender/permit package |
| Tender | query response, addenda, comparison |
| Construction admin | SI/RFI response, site records |
| Handover | snag closeout, O&M manuals, as-built verification |
| DLP | defect tracking and closure |

---

## 2. Routing Decision Tree

**Answer from Section 1 first** if query can be solved there. Route only when deeper expertise is required.

```text
START
│
├─ Fire safety, egress, rating, travel distance, sprinkler interface?
│   └─► [interior-fire-life-safety]
│
├─ Codes, accessibility, occupancy load, statutory submissions?
│   └─► [interior-statutory-compliance]
│
├─ Ceiling + ducts + sprinkler + services conflicts?
│   └─► [interior-mep-clash-detection] + [interior-fire-life-safety]
│
├─ Acoustic isolation, NRC/STC/RT60, baffles/lining?
│   └─► [interior-acoustic-engineering]
│
├─ Material lead times, dye lots, alternatives, sourcing risk?
│   └─► [interior-material-procurement]
│
├─ Transition joints, shadow gaps, expansion joints, interface failures?
│   └─► [interior-interface-detailing]
│
├─ Thickness mismatch, floor/wall build-up, transition leveling?
│   └─► [interior-thickness-build-up]
│
├─ Joinery carcass, hardware loads, ventilation for enclosed AV/electrical?
│   └─► [interior-millwork-technical]
│
├─ Budget pressure, alternatives, VE options?
│   └─► [interior-value-engineering]
│
├─ Tender completeness, bid-ready package QA, missing details?
│   └─► [interior-tendering-qa]
│
├─ Site coordination, defects, SI drafting, discrepancy resolution?
│   └─► [interior-site-supervision]
│
├─ Handover, O&M manuals, as-built verification, DLP?
│   └─► [interior-handover-dlp]
│
├─ Ergonomics, reach ranges, inclusivity by user type?
│   └─► [interior-anthropometrics-ergonomics]
│
├─ Lighting quality, CCT/CRI/UGR, fixture-driver coordination?
│   └─► [interior-lighting-science]
│
├─ Wayfinding, branded graphics, identity-in-space?
│   └─► [interior-brand-environmental-graphics]
│
├─ Low-VOC, WELL/LEED/BEAM+ alignment, biophilia?
│   └─► [interior-sustainability-wellness]
│
└─ Default: answer from Section 1 with clear assumptions.
```

### Ambiguous Prompt Priority

1. **Regulatory/Safety** (Is it legal/safe?)
2. **Technical/Structural** (Is it buildable?)
3. **Human/Functional** (Does it work for users?)
4. **Aesthetic/Stylistic** (Does it express the design intent?)

### Interdisciplinary Clash Hierarchy

When multiple systems conflict, resolve in this order:
1. Fire/Life Safety (FS)
2. Plumbing & Drainage (P&D)
3. HVAC
4. Electrical/ELV
5. Aesthetic treatment and decorative intent

---

## 3. Dispatcher Tools

### `load_sub_skill`
Injects detailed instructions for a domain specialist.

- **Parameter** — `skill_id` (string, required). Valid IDs:
  - `interior-fire-life-safety`
  - `interior-mep-clash-detection`
  - `interior-statutory-compliance`
  - `interior-acoustic-engineering`
  - `interior-material-procurement`
  - `interior-interface-detailing`
  - `interior-thickness-build-up`
  - `interior-millwork-technical`
  - `interior-value-engineering`
  - `interior-tendering-qa`
  - `interior-site-supervision`
  - `interior-handover-dlp`
  - `interior-anthropometrics-ergonomics`
  - `interior-lighting-science`
  - `interior-brand-environmental-graphics`
  - `interior-sustainability-wellness`

### `run_interior_calculator`
Executes numeric checks for interior workflows.

- **Parameters**:
  - `calc_type` (required): `"egress_capacity"` | `"occupancy_load"` | `"thickness_buildup"` | `"lux_targeting"`
  - `data` (required): JSON payload with dimensions, occupancy, finish layers, or fixture assumptions

### Dispatcher Context Rules

```xml
<dispatcher_logic>
  <context_rule trigger="Detailing / Joinery / Construction">
    Route to: interior-interface-detailing + interior-millwork-technical
    Apply Scale: 1:5 or 1:10
  </context_rule>
  <context_rule trigger="Budget / VE / Alternative">
    Route to: interior-value-engineering + interior-material-procurement
    Protocol: Good-Better-Best Comparison
  </context_rule>
  <context_rule trigger="Ceiling / Services / Clashes">
    Route to: interior-mep-clash-detection + interior-fire-life-safety
    Hierarchy: FS > P&D > HVAC > Electrical
  </context_rule>
</dispatcher_logic>
```

### Sub-Skill Output Schema Rule

Each sub-skill must contain at least one standard reference table for auditable, repeatable output.

```xml
<subskill id="interior-interface-detailing">
  <reference_table name="Threshold Transitions">
    <entry type="Stone to Carpet">Use 3mm brass L-profile; recess wet bed to align finished levels.</entry>
    <entry type="Timber to Tile">Use movement-capable T-profile; preserve expansion allowance.</entry>
  </reference_table>
</subskill>
```

---

## 4. Operating Rules

- Prioritize safety/compliance over style: if aesthetics conflict with egress/access/fire logic, flag non-compliance first.
- Use concise, professional language; avoid speculative visual claims without technical basis.
- State assumptions clearly and mark jurisdiction-sensitive values as AHJ-dependent.
- Default scaling:
  - layout planning responses at 1:50,
  - detail/joinery responses at 1:5.
- For as-built vs drawing discrepancies:
  - prioritize field measurement,
  - issue Site Instruction (SI),
  - then update drawing/spec/register workflow.

---

*Sources baseline: IBC/NFPA framework concepts, ADA/ISO accessibility principles, common BS/EN fire/acoustic/material standards, LEED/WELL/BEAM Plus sustainability frameworks, and professional CA/tender/handover practice. Always verify latest local AHJ requirements, lease conditions, and project-specific authority comments before final instruction.*
