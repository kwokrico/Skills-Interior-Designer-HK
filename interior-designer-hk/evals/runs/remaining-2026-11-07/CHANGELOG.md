# Changes made by this evaluation

## Cycle 1

- Master router: require reading and applying all relevant modules, including remediation while work is held; add reusable routes for barriers, subdivision, energy/electrical applicability, fire assemblies, concept layouts, furnishings, acoustics, lighting acceptance and concealed services. Keep general educational questions proportionate and prevent reciprocal routing loops.
- Statutory module: raised adjacent finishes trigger interface, AP/RSE and separate estate/statutory approval checks even without anchor alterations.
- Spatial composition reference: require actual plan-and-section considerations and explicit fixed-versus-movable comparison when future flexibility matters; unknown geometry becomes a conditional check.
- Handover module: cleaning advice must define tasks, exclusions, ownership and hours-versus-completed-task scope.

No expected assertions were relaxed. Baseline response files are preserved. The planned scenarios were promoted as IDs45-56; the original plan and planned JSON were not edited.

## Concurrent work

Another workspace update added DECO resources, modified shared modules and promoted IDs57-62 during the first live-workspace retests. The three overlapping responses (46,47,48 `.retest-1.md`) are retained but excluded. Subsequent evaluations use the frozen skill archive identified by `retest-manifest.json`. These concurrent changes are not attributed to the fixes above; improvements cannot be causally attributed to this patch alone. The planned 18-case scope is unchanged.

## Lighting helper correction

Case 54 explicitly inspected the helper and identified MF/LLF overlap. Corrected the master formula, LLF glossary entry and lighting module; the helper now requires explicit maintained target and overall maintenance factor and rejects legacy `llf` rather than silently multiplying overlapping losses. Fixture estimates require explicit area, output and utilization. Invalid/non-finite factors return an error. This intentionally changes callers that relied on defaults or passed `llf`; the error gives the migration path. Nine dispatcher-level unit tests cover the numerical result, boundaries, invalid inputs and fixture rounding. CIE/IES verification notes are archived under Reference/SS. A new frozen snapshot and case54 rerun verify the final helper guidance.
