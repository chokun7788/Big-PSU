"""Run older quality/competition corpora while redirecting reports outside repo."""

import os
import sys
from pathlib import Path


TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
BASE = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B")
OUT = TASK / "outputs/ground_truth_full_20260927"
sys.path.insert(0, str(PROJECT))
os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"
kind = sys.argv[1]

if kind == "quality":
    from tools import run_answer_quality_eval as module

    module.REPORT_DIR = OUT / "answer_quality_26"
    sys.argv = [sys.argv[0]]
    raise SystemExit(module.main())

from tools import run_ground_truth_pipeline_eval as module
module.REPORT_DIR = OUT / "legacy_competition"
if kind == "base360":
    module.evaluate(BASE / "ground_truth/ground_truth_v2_360.jsonl", "base_360_current")
elif kind == "baselegacy":
    module.evaluate(BASE / "ground_truth/ground_truth_full.jsonl", "base_full_105_current")
    module.evaluate(BASE / "ground_truth/ground_truth_seed.jsonl", "base_seed_10_current")
elif kind == "competition":
    paths = [PROJECT / "data/ground_truth/ground_truth_competition_rules_v1_228.jsonl"]
    paths += sorted((PROJECT / "data/ground_truth/competition_by_game_v2").glob("*.jsonl"))
    paths += sorted((PROJECT / "data/ground_truth/competition_challenger_v1").glob("*.jsonl"))
    paths += sorted((PROJECT / "data/ground_truth/competition_challenger_v2").glob("*.jsonl"))
    for path in paths:
        print(f"START {path.name}", flush=True)
        module.evaluate(path, path.stem + "_current")
else:
    raise SystemExit(f"unknown kind {kind!r}")
