# Flow r47: verify actual answer content

1. Save current source snapshot and capture original HTTP responses/trace.
2. Check address against existing bilingual contact rule + curated fact, not API status alone.
3. Diagnose English wording gaps, wrong venue identity, and Thai frame validation rejection.
4. Bind English studio-location paraphrases to the existing recorded address, source ID and URL. Separate equipment/game/person/competition subjects; unknown venue asks clarification. Address does not establish travel directions.
5. Protect contact domain in question frame before generic equipment location cues; preserve competition precedence.
6. Test location paraphrases, context after rental/rules, known other location subjects, and strengthened content assertions for previously weak negative tests.
7. Review failures, fix evidenced cases, rerun related regressions and unit tests.
8. Freeze new immutable local release, compare source hashes, start verified server, repeat HTTP cases with local LLM enabled.
9. Save per-case before/after answers, root-cause trace, coverage limits and owner-dependent gaps.

No new address facts, owner policy, live availability validation or full 20k test. Legacy English address is reused; do not label it newly human-approved.

## Reviewed outcome
- Address content and domain/source checks are mandatory; non-rental mode alone is insufficient.
- Thai contact frame guard and explicit source-bound Thai resolver were added after trace analysis.
- Canonical source lookup uses content_id; catalog URL checks follow the actual source dataset.
- Focused 25/25, final HTTP 206/206, unit 50/50; no owner data changes.
- Cancel acknowledgment, live occupancy oracle and portable package update remain distinct follow-up work.
