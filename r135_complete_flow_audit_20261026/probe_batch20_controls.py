import json,os,time,hashlib
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/("game_controls_batch20_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
batches=R/"changed_answer_source_batches_1793167120954709200/BATCHES.json";queue=R/"changed_answer_group_queue_1793166229784847000/ITEMS.jsonl";b=json.loads(batches.read_text(encoding="utf8"))[19];ks=set(b["keys"]);items=[x for line in queue.read_text(encoding="utf8").splitlines() if (x:=json.loads(line))["key"] in ks];assert len(items)==5
view=DraftSnapshotView(CommonStore(R/"system/data/knowledge/common.sqlite"));out=[]
for x in items:
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):r=CommonAnswerer(view).answer(x["question"],locale=x["requested_locale"],at="2026-10-16T12:00:00+07:00",planner=None)
 out.append({"saved":x,"candidate_answer":r.answer if r else None,"candidate_artifact":r.decision_artifact if r else None})
(o/"DETAILS.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8");(o/"RESULT.json").write_text(json.dumps({"count":len(out),"source_only":True,"semantic_review_required":True,"queue_sha256":hashlib.sha256(queue.read_bytes()).hexdigest()}),encoding="utf8");print(str(o))
