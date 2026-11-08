import json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
O=R/("mechanical_locale_compound_probe_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"mechanical_future_definition_1793228332945926700/source.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);a.close();b.close();view=DraftSnapshotView(CommonStore(O/"source.sqlite"));rows=[]
for q in ["คีย์บอร์ด mechanical คืออะไร", "What is a mechanical keyboard and how much is a PC?", "What is an optical keyboard?"]:
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"question":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None})
(O/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),"answers":[r["answer"] for r in rows]},ensure_ascii=False))
