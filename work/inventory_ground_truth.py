"""Read-only inventory of source corpora and their schemas."""

import collections
import json
from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
paths = sorted((project / "data/eval").glob("*.jsonl"))
paths += sorted((project / "data/ground_truth").rglob("*.jsonl"))
paths += sorted((project / "data/routing").glob("*.jsonl"))
for path in paths:
    if "draft" in path.name or "review_queue" in path.name:
        continue
    rows = []
    error = ""
    try:
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    if not rows:
        print(f"{path.relative_to(project)} | 0 | {error}")
        continue
    first = rows[0]
    questions = [(str(row.get("locale") or ""), str(row.get("question") or row.get("question_en") or row.get("query") or "")) for row in rows if isinstance(row, dict)]
    reviews = collections.Counter(str(row.get("review_status") or "") for row in rows if isinstance(row, dict))
    print(f"{path.relative_to(project)} | {len(rows)} | unique_q={len(set(questions))} | keys={','.join(sorted(first)[:13]) if isinstance(first,dict) else type(first).__name__} | review={dict(reviews.most_common(3))} | {error}")
