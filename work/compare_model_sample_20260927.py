"""Compare the same 40 benchmark questions with and without local LLM."""

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "outputs/ground_truth_full_20260927"
BASE = OUT / "model_benchmark_1600/no_llm/results.jsonl"
MODEL = OUT / "model_sample_40/llm_scb10x_typhoon2.5-qwen3-4b/results.jsonl"
baseline = {row["id"]: row for row in (json.loads(line) for line in BASE.open(encoding="utf-8"))}
sample = [json.loads(line) for line in MODEL.open(encoding="utf-8")]
rows = []
for model in sample:
    old = baseline[model["id"]]
    rows.append({
        "id": model["id"], "question": model["question"], "group": model["group"],
        "no_llm_pass": old["judge"]["passed"], "with_llm_pass": model["judge"]["passed"],
        "no_llm_errors": old["judge"]["errors"], "with_llm_errors": model["judge"]["errors"],
        "no_llm_answer": old["answer"], "with_llm_answer": model["answer"],
        "no_llm_wall_sec": old["wall_sec"], "with_llm_wall_sec": model["wall_sec"],
    })
summary = {
    "same_40_no_llm_pass": sum(row["no_llm_pass"] for row in rows),
    "same_40_with_llm_pass": sum(row["with_llm_pass"] for row in rows),
    "improved": [row["id"] for row in rows if not row["no_llm_pass"] and row["with_llm_pass"]],
    "regressed": [row["id"] for row in rows if row["no_llm_pass"] and not row["with_llm_pass"]],
    "both_failed": [row["id"] for row in rows if not row["no_llm_pass"] and not row["with_llm_pass"]],
}
(OUT / "model_same_40_comparison.json").write_text(json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
