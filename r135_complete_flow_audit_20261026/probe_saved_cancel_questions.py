import json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/("saved_cancel_questions_source_probe_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();view=DraftSnapshotView(CommonStore(o/"source.sqlite"));cases=json.loads((R/"FIRST_ROUND_CANCEL_COMPARISON_BASELINE_20261029.json").read_text(encoding="utf8"))["cases"];rows=[]
for c in cases:
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):r=CommonAnswerer(view).answer(c["question"],locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"key":c["key"],"question":c["question"],"saved_r132_answer":c["r132_answer"],"candidate_source_only_answer":r.answer if r else None,"artifact":r.decision_artifact if r else None})
(o/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(o),"count":len(rows),"answers":[x["candidate_source_only_answer"] for x in rows]},ensure_ascii=False))
