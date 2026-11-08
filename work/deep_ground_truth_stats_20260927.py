"""Join candidate contracts to results and group failures by scenario and mechanism."""

import collections
import json
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUT = TASK / "outputs/ground_truth_full_20260927"


def read(path):
    return [json.loads(line) for line in path.open(encoding="utf-8-sig") if line.strip()]


names = ["master_v2_current.jsonl", "master_v2_2500_5000.jsonl", "master_v2_5000_7500.jsonl", "master_v2_7500_10000.jsonl"]
results = {r["id"]: r for name in names for r in read(OUT / name)}
cases = {r["id"]: r for r in read(PROJECT / "data/eval/master_ground_truth_bilingual_10000_v2.jsonl")}
failures = [r for r in results.values() if not r["passed"]]

def top_examples(items, n=3):
    return [{"id": r["id"], "question": r["question"], "mode": r["mode"], "failure": r["failures"], "answer": r["answer"][:500]} for r in items[:n]]

by_scenario = collections.defaultdict(list)
by_origin = collections.defaultdict(list)
for r in failures:
    c = cases[r["id"]]
    key = f"{r['locale']}:{c.get('metadata', {}).get('scenario_id', '')}"
    by_scenario[key].append(r)
    by_origin[(r["locale"], c.get("origin", ""), c.get("origin_id", ""))].append(r)

scenario_summary = []
for key, items in sorted(by_scenario.items(), key=lambda pair: -len(pair[1])):
    scenario_summary.append({
        "scenario": key, "failed": len(items),
        "mode_counts": dict(collections.Counter(r["mode"] for r in items).most_common(6)),
        "examples": top_examples(items),
    })

by_domain_mode = collections.defaultdict(list)
for r in failures:
    by_domain_mode[(r["locale"], r["domain"], r["mode"])].append(r)
domain_mode = [{
    "locale": key[0], "domain": key[1], "mode": key[2], "failed": len(items),
    "examples": top_examples(items, 2),
} for key, items in sorted(by_domain_mode.items(), key=lambda pair: -len(pair[1]))]

summary = {
    "total_failures": len(failures),
    "distinct_scenario_keys_with_failures": len(by_scenario),
    "distinct_origin_keys_with_failures": len(by_origin),
    "failure_origin_counts": dict(collections.Counter(cases[r["id"]].get("origin", "") for r in failures).most_common()),
    "top_origin_keys": [{"key": key, "failed": len(items), "examples": top_examples(items, 1)} for key, items in sorted(by_origin.items(), key=lambda pair: -len(pair[1]))[:30]],
    "scenario_summary": scenario_summary,
    "domain_mode": domain_mode,
}
by_expected = collections.defaultdict(list)
for r in results.values():
    by_expected[(r["locale"], r["expected_status"])].append(r)
summary["by_expected_status"] = [
    {"locale": key[0], "expected_status": key[1], "total": len(items), "passed": sum(r["passed"] for r in items), "failed": sum(not r["passed"] for r in items), "actual_statuses": dict(collections.Counter(r["actual_status"] for r in items))}
    for key, items in sorted(by_expected.items())
]
summary["failure_flag_counts"] = {
    "route_only": sum(not r["route_ok"] and r["status_ok"] and r["content_ok"] and r["latency_ok"] for r in failures),
    "status_only": sum(r["route_ok"] and not r["status_ok"] and r["content_ok"] and r["latency_ok"] for r in failures),
    "content_only": sum(r["route_ok"] and r["status_ok"] and not r["content_ok"] and r["latency_ok"] for r in failures),
    "multiple_flags": sum(sum(not r[k] for k in ("route_ok", "status_ok", "content_ok", "latency_ok")) > 1 for r in failures),
    "latency_any": sum(not r["latency_ok"] for r in failures),
}
(OUT / "failure_taxonomy_stats.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print("failures", len(failures), "distinct scenarios", len(by_scenario))
print("distinct origin keys", len(by_origin))
print("origin counts", summary["failure_origin_counts"])
print("top scenario counts", [(x["scenario"], x["failed"]) for x in scenario_summary[:25]])
print("top domain mode", [(x["locale"], x["domain"], x["mode"], x["failed"]) for x in domain_mode[:30]])
print("expected statuses", summary["by_expected_status"])
print("failure flags", summary["failure_flag_counts"])
