# Agent instructions — Interior Designer HK

## Professional skill activation

When the user's request matches **interior design**, **fit-out**, **joinery**, **FF&E**, **HK renovation** (裝修), **HKEDCA**, **HKRG**, or related construction-administration topics:

1. Read and follow [`interior-designer-hk/SKILL.md`](interior-designer-hk/SKILL.md) as the master router.
2. Apply [`interior-designer-hk/references/config.json`](interior-designer-hk/references/config.json), [`interior-designer-hk/references/compliance.md`](interior-designer-hk/references/compliance.md), and [`interior-designer-hk/references/operational.md`](interior-designer-hk/references/operational.md).
3. Cross-reference [`interior-designer-hk/references/domain_terms.json`](interior-designer-hk/references/domain_terms.json) for acronyms.
4. Answer from Foundation Quick Reference (Section 1) when sufficient; otherwise route to subskills via decision tree or `python interior-designer-hk/scripts/dispatcher.py load <slug>`.
5. Use [`interior-designer-hk/references/templates/deliverables.md`](interior-designer-hk/references/templates/deliverables.md) to pick artifacts; standalone files in [`interior-designer-hk/references/templates/`](interior-designer-hk/references/templates/) for SI, snag, tender audit, VE, compliance gap, HKRG boilerplate, and material schedule.
6. On compliance violations, **halt** per compliance rules — cite the rule and offer remediated options only.

Dispatch to `subskills/<slug>/<slug>.md` for the selected module.

## Golden verification prompts

See [`interior-designer-hk/evals/README.md`](interior-designer-hk/evals/README.md) and [`interior-designer-hk/evals/evals.json`](interior-designer-hk/evals/evals.json) for test cases after skill changes.
