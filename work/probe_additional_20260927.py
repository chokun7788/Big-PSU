import json
import os
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(PROJECT))
os.environ["PSU_LIVE_BOOKING_ENABLED"] = "0"
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402

questions = [
    "PS5 มีเกมอะไร",
    "PS5 มีเกมอะไรบ้าง",
    "เครื่อง PC ใช้การ์ดจอรุ่นอะไร",
    "Gaming Headset คืออุปกรณ์อะไร",
    "ศูนย์อยู่ที่ไหน",
    "ขอข้อมูลเรื่องอีเมล",
    "จองวันนี้เลยได้ไหม",
    "ตอนนี้ศูนย์เปิดอยู่ไหม",
    "อัดวิดีโอในศูนย์ได้ไหม",
    "ของหายต้องทำยังไง",
    "Hades II มีให้เล่นไหม",
]
out = TASK / "outputs/ground_truth_full_20260927/additional_probes.jsonl"
with out.open("w", encoding="utf-8", buffering=1) as file:
    for question in questions:
        result = answer_question_pipeline_debug(question, locale="th", experimental_allow_llm=False, experimental_rag_fallback=False, global_timeout_sec=20.0)
        row = {
            "question": question, "route": result.route.category, "intent": result.route.intent,
            "mode": result.mode, "answer": result.answer,
            "trace": [{"stage": t.stage, "decision": t.decision, "detail": t.detail, "metadata": t.metadata} for t in result.trace],
        }
        file.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        print(result.route.category, result.mode, question, flush=True)
