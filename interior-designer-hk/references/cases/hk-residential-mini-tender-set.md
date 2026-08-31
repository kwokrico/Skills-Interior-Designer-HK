# HK residential mini tender drawing set — case study

Anonymized conventions distilled from a compact Hong Kong residential fit-out tender package.  
Use as the shared hub for drawing-set QA; do not invent project identity from this file.

**Typology:** HK residential mini fit-out (living/dining, bedroom/study, bath, kitchen)  
**Default sheet format:** A4 landscape · scale **1:50** · dimensions in **mm** · Rev schema (`Rev.00`, …)

Load from: `interior-tendering-qa` (primary), plus material-procurement / lighting / millwork / MEP spokes when those sheets are in play.

---

## Sheet index (P0–P7)

| Sheet | Chinese title | Owns |
|-------|---------------|------|
| **P0** | 現狀平面圖 | Existing walls, openings, levels; baseline for demolition/remeasure |
| **P1** | 設計平面圖 | Proposed GA, joinery tags, elevation bubbles, general notes, `自購` marks |
| **P2** | 地板窗台物料標示圖 | Floor/sill hatch legend + skirting notes (wet exclusions) |
| **P3** | 天花/燈具工程標示圖 | Ceiling zones, lighting symbols, clear-height `+H`, AC niche notes |
| **P4** | 客廳立面圖 | Living elevations (typical elev nos. 01–04) |
| **P5** | 睡房書房立面圖 | Bedroom/study elevations (continues numbering) |
| **P6** | 浴室立面圖 | Bathroom elevations; wet finishes + fixtures |
| **P7** | 廚房立面圖 | Kitchen elevations; fire door / wet ceiling callouts |

Revision-match all sheets before tender release. P0 is not a substitute for site measure.

---

## Golden conventions

### Title block / disclaimer

- Sheet title + **No. Px**, scale, paper size, date, revision.
- State: drawings for **tender / quotation reference**; contractor must **verify on site**; report drawing–site discrepancies.
- Units: **mm** unless noted.

### Joinery tags (P1 + elevations)

| Prefix | Room / zone |
|--------|-------------|
| **L** | Living / dining |
| **S** | Bedroom / study |
| **K** | Kitchen |
| **B** | Bathroom |

Call material/finish on plan and again on matching elevation (e.g. 耐磨夾層板 + 裝飾耐火板, LED 滲光).

### Elevation scheme

- Numbered bubbles on **P1** point to elevation sheets.
- Elevations numbered **continuously** across rooms (e.g. 01…21), not restarted per sheet.
- Use **EQ** for equal door/bay spacing where intentional.

### Floor / sill legend (P2)

Typical hatch → code pattern (adapt codes to the project schedule):

| Pattern role | Example material |
|--------------|------------------|
| Living/bedroom field | SPC / stone-plastic plank (e.g. 600×600 / 600×300) |
| Wet floor A | Porcelain tile type D |
| Wet floor B | Porcelain tile type E |
| Door threshold | Marble/quartz saddle |
| Window sill | Marble sill stone |

Note skirting height (e.g. 80 mm) and **exclude** bath/kitchen where wet skirting/tile base applies differently.

### Ceiling / lighting legend (P3)

| Symbol role | Typical use |
|-------------|-------------|
| Panel / pendant | Ambient centrepiece |
| Wet-rated recessed downlight (7–9 W class) | Kitchen / bath 假天花 |
| Accent recessed spot (lower W) | Living decorative layer |
| Dotted cove / 燈槽 + LED strip | Perimeter wash / 滲光 |
| Curtain track | Window head coordination |

Mark finished clear heights as **`+H`** (e.g. `+2800` living, lower wet ceilings). Note AC niche / bulkhead and exhaust fan positions.

### Owner vs contract

- Mark loose FF&E / appliances as **`自購`** on P1 so BOQ does not price owner items.
- Cross-check to material-schedule owner-supply companion sheets → `interior-material-procurement`.

### Fire / life safety callouts

- Kitchen **fire-rated door** (e.g. 兩小時防火門) on plan/elev → chain `interior-fire-life-safety`; no appearance-only substitute.

---

## Gap register (flag before “release for tender”)

These are common bid-readiness gaps when only a P0–P7 mini-set exists:

1. **No standalone door / ironmongery schedule**
2. **No consolidated 物料規格表** (codes live only on drawings)
3. **No dedicated power / ELV layout** (switches noted ad hoc only)
4. **Elevations only at 1:50 A4** — flag missing **1:20 / 1:5** for bespoke joinery if bid risk is high
5. **No dedicated waterproofing / wet build-up sheet** (notes only)
6. **Drawing set alone ≠ contract package** — still need BOQ / HKRG 標準報價單 attachment
7. **MEP depths beyond RCP notes** (AC niche, exhaust) still open for coordination

Route gaps: schedules → `interior-material-procurement`; lighting symbols → `interior-lighting-science`; joinery LOD → `interior-millwork-technical`; ceiling heights/AC → `interior-mep-clash-detection`; FD → `interior-fire-life-safety`; package release → `interior-tendering-qa` + [`templates/tender-completeness-audit.md`](../templates/tender-completeness-audit.md).

---

## Decision rules (hub)

1. Treat P0–P7 as the **minimum residential drawing skeleton**, not a complete bid package.
2. Align joinery tags, hatch codes, and elevation numbers with the material schedule and BOQ terminology.
3. Any `自購` item must appear on owner-supply sheets and must not be double-counted in contractor BOQ.
4. Wet recessed lights and alu strip ceilings → confirm IP / moisture notes with lighting + MEP.
5. Do not release tender while gap-register items critical to pricing remain unmarked or unallocated (drawing note vs schedule vs provisional sum).
