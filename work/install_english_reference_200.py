import json
from pathlib import Path


workspace = Path(__file__).resolve().parents[1]
project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
source = workspace / "outputs/intent_trap_english_reference_200_20260926.jsonl"
source_manifest = workspace / "outputs/intent_trap_english_reference_200_20260926_manifest.json"
destination = project / "data/eval/intent_trap_english_reference_200_20260926.jsonl"
destination_manifest = project / "data/eval/intent_trap_english_reference_200_20260926_manifest.json"
if destination.exists() or destination_manifest.exists():
    raise RuntimeError("Will not overwrite an existing English reference")
manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
manifest["source_corpus"] = "reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl"
manifest["source_review"] = "intent_trap_review_2026-09-24T13-54-43-758Z.json (external user export; SHA-256 above)"
manifest["prior_projection"] = "reports/master_ground_truth_eval/intent_trap_review_bilingual_assisted_20260924.json"
with destination.open("xb") as handle:
    handle.write(source.read_bytes())
with destination_manifest.open("x", encoding="utf-8") as handle:
    json.dump(manifest, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(f"Added {destination} and matching manifest without changing previous review or Gold files.")
