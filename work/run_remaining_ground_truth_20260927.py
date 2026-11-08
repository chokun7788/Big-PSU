"""Evaluate routing and machine English shadow without writing inside source repo."""

import json
import os
import sys
import time
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUT = TASK / "outputs/ground_truth_full_20260927"
sys.path.insert(0, str(PROJECT))
os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"


def routing() -> None:
    from tools import run_routing_eval as module

    module.REPORT_DIR = OUT / "routing"
    for name in ("routing_eval_cases.jsonl", "routing_eval_real_usage.jsonl"):
        module.CASES_PATH = PROJECT / "data/routing" / name
        sys.argv = [sys.argv[0], "--cases", str(module.CASES_PATH)]
        module.main()


def shadow() -> None:
    from app.core.locale import contains_thai_prose
    from app.pipeline.engine import answer_question_pipeline_debug

    source = PROJECT / "data/eval/english_shadow_1600_machine_20260908.jsonl"
    out = OUT / "english_shadow_machine_1600_current.jsonl"
    cases = [json.loads(line) for line in source.open(encoding="utf-8-sig") if line.strip()]
    seen = {}
    for path in (OUT / "master_v2_5000_7500.jsonl", OUT / "master_v2_7500_10000.jsonl"):
        for line in path.open(encoding="utf-8"):
            row = json.loads(line)
            seen[("en", row["question"])] = row
    completed = set()
    if out.exists():
        for line in out.open(encoding="utf-8"):
            completed.add(json.loads(line)["id"])
    with out.open("a", encoding="utf-8", buffering=1) as writer:
        for index, case in enumerate(cases, 1):
            if case["id"] in completed:
                continue
            question = str(case.get("question_en") or "").strip()
            if not question:
                continue
            previous = seen.get(("en", question))
            if previous is not None:
                answer = previous["answer"]
                mode = previous["mode"]
                category = previous["actual_route"]
                elapsed = previous["elapsed_sec"]
                reused = True
            else:
                result = answer_question_pipeline_debug(
                    question, locale="en", experimental_allow_llm=False,
                    experimental_rag_fallback=False, global_timeout_sec=20.0,
                )
                answer = result.answer or ""
                mode = result.mode
                category = result.route.category
                elapsed = result.elapsed
                reused = False
            expected = case.get("expected_category") or ""
            expected = expected if isinstance(expected, list) else [expected]
            prefixes = case.get("expected_mode_prefix") or ""
            prefixes = prefixes if isinstance(prefixes, list) else [prefixes]
            errors = []
            if any(expected) and category not in expected:
                errors.append("category")
            if any(prefixes) and not any(mode.startswith(prefix) for prefix in prefixes):
                errors.append("mode")
            if contains_thai_prose(answer):
                errors.append("thai_prose_leak")
            if elapsed >= 20:
                errors.append("latency")
            row = {
                "id": case["id"], "question": question, "expected_category": expected,
                "actual_category": category, "expected_mode_prefix": prefixes,
                "mode": mode, "answer": answer, "elapsed_sec": round(elapsed, 4),
                "reused_master_response": reused, "translation_status": case.get("translation_status"),
                "failures": errors, "passed": not errors,
            }
            writer.write(json.dumps(row, ensure_ascii=False) + "\n")
            if index % 100 == 0 or index == len(cases):
                print(f"{index}/{len(cases)} pass={row['passed']} mode={mode} reused={reused}", flush=True)


if __name__ == "__main__":
    {"routing": routing, "shadow": shadow}[sys.argv[1]]()
