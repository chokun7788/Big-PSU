"""Run legacy question banks without rewriting their source files in repo."""

import sys
from pathlib import Path


TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(PROJECT))
kind = sys.argv[1]
base = TASK / "outputs/ground_truth_full_20260927"
if kind == "broad":
    from tools import run_broad_usage_eval_v1 as module

    module.BANK_JSONL = base / "broad_usage_663/bank.jsonl"
    module.BANK_JSON = base / "broad_usage_663/bank.json"
    sys.argv = [sys.argv[0], "--out-dir", str(base / "broad_usage_663"), "--quiet", "--progress-every", "100"]
elif kind == "user":
    from tools import run_user_question_bank_eval as module

    module.ROOT = base / "user_question_bank_400"
    sys.argv = [sys.argv[0], "--out-dir", str(base / "user_question_bank_400"), "--quiet", "--progress-every", "100", "--no-rag-fallback"]
else:
    raise SystemExit(f"unknown bank {kind!r}")
raise SystemExit(module.main())
