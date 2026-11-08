"""Read-only reruns of representative failures with route and decision traces."""

import json
import os
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUT = TASK / "outputs/ground_truth_full_20260927/failure_probes.jsonl"
sys.path.insert(0, str(PROJECT))
os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402

CASES = [
    ("pc_price", "เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง", "th"),
    ("pc_games", "PC Zone มีเกมอะไรให้เล่น", "th"),
    ("ps5_games_price", "PS5 มีเกมอะไรกับราคาเท่าไหร่", "th"),
    ("tekken_price", "Tekken 8 ราคาเท่าไหร่", "th"),
    ("holiday_open", "วันหยุดราชการเปิดไหม", "th"),
    ("cs2_players", "Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน", "th"),
    ("mario_live_en", "What does the Y button do in Mario Kart Live: Home Circuit on Nintendo Switch", "en"),
    ("ps5_controller", "PS5 ใช้จอยแบบไหน", "th"),
]

with OUT.open("w", encoding="utf-8", buffering=1) as file:
    for tag, question, locale in CASES:
        result = answer_question_pipeline_debug(
            question, locale=locale, experimental_allow_llm=False,
            experimental_rag_fallback=False, global_timeout_sec=20.0,
        )
        row = {
            "tag": tag, "question": question, "locale": locale,
            "route": {"category": result.route.category, "intent": result.route.intent, "confidence": result.route.confidence},
            "mode": result.mode, "answer": result.answer, "elapsed": result.elapsed,
            "trace": [{
                "stage": t.stage, "decision": t.decision, "confidence": t.confidence,
                "detail": t.detail, "metadata": t.metadata,
            } for t in result.trace],
        }
        file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        print(tag, result.route.category, result.mode, flush=True)
