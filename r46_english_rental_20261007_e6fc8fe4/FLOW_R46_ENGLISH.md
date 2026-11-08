# Flow r46: English zone rental requests

## Evidence and priorities
The initial HTTP run executed 33 English cases: 22 passed and 11 failed.
1. Incorrect scope: whole-day returned both periods; long misspelled service defaulted to all targets; a fresh exclusion was lost.
2. Incorrect field intent/context: capacity, duration, booking and effective-date follow-ups failed or repeated prices.
3. Compound scope: versus/compare-with applied the Cartesian product of groups and periods instead of each clause's conditions.
4. Unknown-target extraction: per-machine and comparison words were treated as unknown products.

## Implementation flow
1. Preserve source snapshot and every initial request/response; bind expected 24 rates to original workbook cells, not generated answers.
2. Resolve exact services and conservative existing fuzzy token matches in long rental sentences. Preserve product digits and unknown targets.
3. Recognize whole-day as full-day; apply target/group/period exclusions before defaults.
4. Derive information follow-ups from requested source fields; inherit only acknowledged rental context and exclude game/rule topic changes.
5. Identify duration/effective-date questions as field requests. Answer known facts and explicitly label absent policy data.
6. Split comparison clauses; preserve each target/group/period tuple and prevent cross-product prices.
7. Source-test new English cases plus the existing targeted Thai/English regression. Fix only observed failures, save each run separately.
8. Freeze a new release; verify file hashes, start its hidden local server, repeat targeted HTTP checks with local LLM enabled.
9. Save before/after answers, failed checks, causes, limitations and measured timings. Passing HTTP transport alone does not certify a price.

## Review gates
- Exact rate IDs and values equal workbook cells; rendered requested prices present.
- English output contains no Thai; source SHA matches original workbook; validation succeeds; no timeout.
- Unknown hours, effective dates, booking procedure, staff cost, individual eligibility, custom prices remain unconfirmed.
- Ordinary hourly prices and games/rules must retain their own routes.
- No original workbook/schedule/log replacement; snapshot guards concurrent edits.
- No full 20k regression, no live availability correctness claim, no portable distribution claim.
