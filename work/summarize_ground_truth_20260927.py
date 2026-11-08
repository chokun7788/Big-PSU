"""Summarize all completed evaluation outputs and sample failures."""

import collections
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "outputs/ground_truth_full_20260927"


def read(path):
    return [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]


for path in sorted(OUT.glob("*.jsonl")):
    if not any(word in path.stem for word in ("current", "rescored", "master_v2_")):
        continue
    rows = read(path)
    if not rows or "passed" not in rows[0]:
        continue
    failed = [row for row in rows if not row["passed"]]
    print(f"\n{path.name}: {len(rows) - len(failed)}/{len(rows)} pass, {len(failed)} fail")
    print("domains", collections.Counter(row.get("domain") or row.get("group") or row.get("case_type") for row in failed).most_common(10))
    print("modes", collections.Counter(row.get("mode") for row in failed).most_common(8))
    print("failure types", collections.Counter(str(failure).split(":")[0] for row in failed for failure in row.get("failures", [])).most_common(8))
    for row in failed[:3]:
        print("sample", row.get("id"), row.get("question"), row.get("failures"), str(row.get("answer"))[:230])
