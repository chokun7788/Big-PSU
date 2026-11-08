"""Read-only current English flow probe for all translated review pairs."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
REFERENCE = ROOT / "outputs/intent_trap_english_reference_200_20260926.jsonl"
OUTPUT = ROOT / "outputs/intent_trap_english_reference_current_flow_200_after_scope_20260926.jsonl"
sys.path.insert(0, str(PROJECT))

from app.pipeline.engine import answer_question_pipeline_debug


references = [json.loads(line) for line in REFERENCE.read_text(encoding="utf-8").splitlines() if line.strip()]
if len(references) != 200:
    raise ValueError(f"Expected 200 pairs, got {len(references)}")
with OUTPUT.open("x", encoding="utf-8") as handle:
    for index, row in enumerate(references, 1):
        result = answer_question_pipeline_debug(
            row["question_en"], locale="en", experimental_allow_llm=False,
            experimental_rag_fallback=False, global_timeout_sec=10.0,
        )
        record = {
            "id": row["id"],
            "domain": row["domain"],
            "facet": row["facet"],
            "question_en": row["question_en"],
            "reference_answer_en": row["reference_answer_en"],
            "reference_status": row["reference_status"],
            "current_answer_en": result.answer,
            "current_route": result.route.category,
            "current_mode": result.mode,
            "elapsed_sec": result.elapsed,
            "run_mode": "deterministic_pipeline_without_optional_llm",
        }
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()
        if index % 25 == 0:
            print(f"{index}/200 checked", flush=True)
print(OUTPUT)
