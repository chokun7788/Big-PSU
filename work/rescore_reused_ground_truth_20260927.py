"""Rescore unchanged questions against older contracts, preserving raw responses."""

import collections
import json
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUT = TASK / "outputs/ground_truth_full_20260927"
sys.path.insert(0, str(PROJECT))
from tools.run_master_ground_truth_eval import contains_contract, expected_status_ok  # noqa: E402


def load(path):
    return [json.loads(line) for line in path.open(encoding="utf-8-sig") if line.strip()]


def rescore(corpus_name, output_name, result_paths):
    source = load(PROJECT / "data/eval" / corpus_name)
    result_by_question = {}
    for path in result_paths:
        for row in load(OUT / path):
            result_by_question[(row["locale"], row["question"])] = row
    missing = []
    scores = []
    for case in source:
        raw = result_by_question.get((case["locale"], case["question"]))
        if raw is None:
            missing.append(case["id"])
            continue
        routes = case.get("expected_route_categories") or []
        route_ok = raw["actual_route"] in routes
        status_ok = expected_status_ok(
            case.get("expected_answer_status") or "", raw["actual_status"], raw["mode"]
        )
        content_ok, failures = contains_contract(raw["answer"], case.get("answer_contract") or {})
        latency_ok = raw["elapsed_sec"] <= float(case.get("latency_ceiling_sec", 20.0))
        if not route_ok:
            failures.append(f"route expected {routes}, got {raw['actual_route']}")
        if not status_ok:
            failures.append(f"status expected {case.get('expected_answer_status')}, got {raw['actual_status']}")
        if not latency_ok:
            failures.append("latency exceeded ceiling")
        scores.append({
            "id": case["id"], "locale": case["locale"], "domain": case["domain"],
            "question": case["question"], "review_status": case.get("review_status"),
            "expected_routes": routes, "actual_route": raw["actual_route"],
            "expected_status": case.get("expected_answer_status"), "actual_status": raw["actual_status"],
            "mode": raw["mode"], "elapsed_sec": raw["elapsed_sec"], "answer": raw["answer"],
            "route_ok": route_ok, "status_ok": status_ok, "content_ok": content_ok,
            "latency_ok": latency_ok, "passed": not failures, "failures": failures,
        })
    target = OUT / output_name
    with target.open("w", encoding="utf-8") as handle:
        for row in scores:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    summary = {
        "corpus": corpus_name, "total": len(source), "scored": len(scores), "missing": missing,
        "passed": sum(row["passed"] for row in scores),
        "failed": sum(not row["passed"] for row in scores),
        "by_domain": {domain: {"pass": sum(r["passed"] for r in rows), "fail": sum(not r["passed"] for r in rows)} for domain, rows in ((d, [r for r in scores if r["domain"] == d]) for d in sorted({r["domain"] for r in scores}))},
    }
    target.with_suffix(".summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output_name, len(scores), summary["passed"], summary["failed"], "missing", len(missing))


if __name__ == "__main__":
    rescore(
        "master_ground_truth_bilingual_10000_v1.jsonl", "master_v1_rescored_current.jsonl",
        ["master_v2_current.jsonl", "master_v2_2500_5000.jsonl", "master_v2_5000_7500.jsonl", "master_v2_7500_10000.jsonl", "master_v1_delta_300_current.jsonl"],
    )
    rescore(
        "intent_trap_bilingual_1000_v1.jsonl", "intent_trap_v1_rescored_current.jsonl",
        ["intent_trap_v2_current.jsonl"],
    )
