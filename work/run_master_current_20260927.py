"""Stream current deterministic master ground-truth results outside the repo."""

import argparse
import json
import os
import sys
import time
from pathlib import Path


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(PROJECT))
from tools.run_master_ground_truth_eval import evaluate, read_jsonl


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=0)
    parser.add_argument("--progress-every", type=int, default=100)
    args = parser.parse_args()
    corpus = Path(args.corpus)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = read_jsonl(corpus)
    rows = rows[args.start:args.end or None]
    existing = set()
    if output.exists():
        for line in output.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.add(json.loads(line)["id"])
    os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"
    start = time.perf_counter()
    passed = failed = errors = 0
    with output.open("a", encoding="utf-8") as handle:
        for index, case in enumerate(rows, 1):
            if case["id"] in existing:
                continue
            try:
                result = evaluate(case, allow_llm=False, rag_fallback=False)
                passed += bool(result["passed"])
                failed += not bool(result["passed"])
            except Exception as exc:
                errors += 1
                result = {
                    "id": case["id"], "locale": case.get("locale"),
                    "domain": case.get("domain"), "question": case.get("question"),
                    "passed": False, "evaluation_error": f"{type(exc).__name__}: {exc}",
                }
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")
            handle.flush()
            if index % args.progress_every == 0:
                print(f"{index}/{len(rows)} elapsed={time.perf_counter()-start:.1f}s new_pass={passed} new_fail={failed} exceptions={errors}", flush=True)
    print(f"DONE {len(rows)} rows, skipped={len(existing)}, new_pass={passed}, new_fail={failed}, exceptions={errors}, wall={time.perf_counter()-start:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
