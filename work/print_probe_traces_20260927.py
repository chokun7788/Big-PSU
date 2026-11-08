import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "outputs/ground_truth_full_20260927/failure_probes.jsonl"
for line in path.open(encoding="utf-8"):
    row = json.loads(line)
    print("\n", row["tag"], row["question"], row["route"], row["mode"])
    print("ANSWER", row["answer"][:300].replace("\n", " | "))
    for trace in row["trace"]:
        if trace["stage"] in {
            "preprocess", "active_route_selection", "question_frame", "target_guard",
            "candidate_execution", "competition_contract_retrieval", "guard_scope",
            "ambiguous_target", "semantic_route_refiner", "universal_intent",
            "game_target_resolution", "game_resolution", "route",
        }:
            metadata = {key: value for key, value in trace["metadata"].items() if key not in {"candidates", "trace"}}
            print(trace["stage"], trace["decision"], trace["detail"][:180], str(metadata)[:260])
