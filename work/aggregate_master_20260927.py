"""Create compact, reproducible aggregate for the bilingual master corpus."""

import collections
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "outputs/ground_truth_full_20260927"
NAMES = ["master_v2_current.jsonl", "master_v2_2500_5000.jsonl", "master_v2_5000_7500.jsonl", "master_v2_7500_10000.jsonl"]
rows = [json.loads(line) for name in NAMES for line in (OUT / name).open(encoding="utf-8") if line.strip()]
by_id = {row["id"]: row for row in rows}
if len(rows) != 10000 or len(by_id) != 10000:
    raise SystemExit(f"Expected 10000 unique rows, got {len(rows)} / {len(by_id)}")

def group_stats(field):
    groups = collections.defaultdict(list)
    for row in rows:
        groups[str(row.get(field) or "")].append(row)
    return {name: {"total": len(group), "passed": sum(item["passed"] for item in group), "failed": sum(not item["passed"] for item in group)} for name, group in sorted(groups.items())}

failure_rows = [row for row in rows if not row["passed"]]
summary = {
    "total": len(rows), "passed": len(rows) - len(failure_rows), "failed": len(failure_rows),
    "by_locale": group_stats("locale"),
    "by_domain": group_stats("domain"),
    "by_review_status": group_stats("review_status"),
    "failure_by_locale_domain": dict(collections.Counter(f"{row['locale']}:{row['domain']}" for row in failure_rows).most_common()),
    "failure_modes": dict(collections.Counter(row["mode"] for row in failure_rows).most_common()),
    "failure_reasons": dict(collections.Counter(reason.split(":")[0] for row in failure_rows for reason in row["failures"]).most_common()),
    "latency_over_20sec": sum(not row["latency_ok"] for row in rows),
}
(OUT / "master_v2_aggregate_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
