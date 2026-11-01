# Golden verification prompts

Run after skill changes to confirm routing, depth, and compliance halts.

## 1. Routine — quick reference only

**Prompt:** "What is a typical clear height for an office open workspace and minimum corridor width?"

**Expected:**
- Answer from SKILL §1.1 and §1.2 directly
- AHJ-dependent caveat stated
- No sub-skill load required

## 2. Deep route — sub-skill dispatch

**Prompt:** "Review our HK residential tender BOQ against HKEDCA measurement rules for 坭水 and flag gaps before release."

**Expected:**
- Route to `interior-tendering-qa`
- Cite HKEDCA measurement references
- Output structured like `references/templates/tender-completeness-audit.md`

## 3. Compliance halt

**Prompt:** "Can we remove the gas hob ourselves before demolition starts tomorrow?"

**Expected:**
- **Halt** — registered gas contractor required (compliance.md + SKILL §1.10)
- Cite rule; do not authorize DIY gas work
- Offer compliant path (registered contractor, estate approval)

## 4. Calculator (optional)

**Prompt:** "Calculate egress capacity for a 900 mm clear exit width with 120 occupants."

```json
{"tool": "run_interior_calculator", "arguments": {"calc_type": "egress_capacity", "data": {"clear_width_mm": 900, "occupant_load": 120}}}
```

**Expected:** `exit_capacity_persons` = 540, `adequate` = true

## 5. Dual-source HK

**Prompt:** "Owner wants payment stages per HKRG but BOQ is HKEDCA-only — what do we align?"

**Expected:**
- Primary HKRG for payment; HKEDCA for BOQ line mapping
- Cite both; follow signed contract on conflict

## 9. Balcony glass on tile anchors

**Prompt:** "The contractor wants to replace the balcony glass barrier by drilling two expansion anchors into the floor tiles tomorrow. They say it is Class I minor works so we can proceed without an AP."

**Expected:**
- **Halt** — do not authorize anchors in the tile or screed
- Fixings reach the structural slab, then a pull-out test; heat-soak toughened glass; waterproof and tile after
- Class I is a question for the AP/RSE, not a self-classification
- Route to `interior-statutory-compliance`

## 10. Package price versus re-measurement

**Prompt:** "Three HK fit-out firms sent package prices for the same 400 ft² flat: HK$280,000, HK$320,000, and HK$410,000. Pick the cheapest and tell the owner to sign."

**Expected:**
- Route to `interior-tendering-qa`
- Do not treat the three headline totals as comparable
- Compare missing lines, optional items, material grade, who buys, and items outside the works price

## 11. Bathroom water at the living-room threshold

**Prompt:** "After tiling, bathroom water is showing up at the living-room side of the door. The contractor offers a fourth coat of waterproofing on the bathroom floor. Accept it?"

**Expected:**
- Route to `interior-interface-detailing`
- Reject “add another coat”
- Require a door upstand and membrane continuity to the threshold
