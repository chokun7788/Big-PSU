"""Stream specialized current pipeline evaluations outside the project repo."""

import argparse
import json
import os
import sys
import time
from pathlib import Path


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(PROJECT))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("competition", "rag", "real_usage"), required=True)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=0)
    args = parser.parse_args()
    if args.kind == "competition":
        from tools.run_competition_rules_rag_ground_truth import evaluate_case
    elif args.kind == "rag":
        from tools.run_rag_robustness_ground_truth import evaluate_case
    else:
        from tools.run_real_usage_golden_eval import evaluate_case
    cases = [json.loads(line) for line in Path(args.corpus).read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    cases = cases[args.start:args.end or None]
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    if output.exists():
        seen = {json.loads(line)["id"] for line in output.read_text(encoding="utf-8").splitlines() if line.strip()}
    os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"
    started = time.perf_counter()
    passed = failed = errors = 0
    with output.open("a", encoding="utf-8") as handle:
        for index, case in enumerate(cases, 1):
            if case["id"] in seen:
                continue
            try:
                if args.kind == "real_usage":
                    row = evaluate_case(case, allow_llm=False, rag_fallback=False, include_trace=False)
                else:
                    row = evaluate_case(case, allow_llm=False, rag_fallback=False, include_trace=False)
                passed += bool(row["passed"])
                failed += not bool(row["passed"])
            except Exception as exc:
                errors += 1
                row = {"id": case["id"], "passed": False, "evaluation_error": f"{type(exc).__name__}: {exc}"}
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            handle.flush()
            if index % 100 == 0:
                print(f"{index}/{len(cases)} pass={passed} fail={failed} exceptions={errors} wall={time.perf_counter()-started:.1f}s", flush=True)
    print(f"DONE {len(cases)} rows pass={passed} fail={failed} exceptions={errors} wall={time.perf_counter()-started:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
