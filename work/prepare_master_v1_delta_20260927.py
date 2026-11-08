"""Extract only master v1 questions not already exercised by v2."""

import json
from pathlib import Path


TASK = Path(__file__).resolve().parents[1]
PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
base = PROJECT / "data/eval"
read = lambda path: [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
v1 = read(base / "master_ground_truth_bilingual_10000_v1.jsonl")
v2 = read(base / "master_ground_truth_bilingual_10000_v2.jsonl")
keys = {(row["locale"], row["question"]) for row in v2}
delta = [row for row in v1 if (row["locale"], row["question"]) not in keys]
target = TASK / "work/master_v1_questions_absent_from_v2_20260927.jsonl"
with target.open("x", encoding="utf-8") as handle:
    for row in delta:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"v1={len(v1)} reused_questions={len(v1)-len(delta)} unique_to_v1={len(delta)} output={target}")
