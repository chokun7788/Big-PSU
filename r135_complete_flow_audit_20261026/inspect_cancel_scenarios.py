"""Read-only draft source-only cancellation scope observations; no model or HTTP."""
import json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/("cancel_scenario_scope_probe_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
view=DraftSnapshotView(CommonStore(R/"system/data/knowledge/common.sqlite")); rows=[]
questions=["ต้องการแก้ไขข้อมูลหลังจอง ต้องทำอย่างไร", "จองผิดเครื่องจะเปลี่ยนได้อย่างไร", "How can I change my booking time?", "How do I cancel my booking?", "ต้องยกเลิกการจองล่วงหน้ากี่ชั่วโมง", "ยกเลิกการจองอย่างไร และราคา PC เท่าไหร่"]
for q in questions:
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
  r=CommonAnswerer(view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"question":q,"answer":r.answer if r else None,"decision_artifact":r.decision_artifact if r else None})
(o/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print(json.dumps({"path":str(o),"observations":[{"question":x["question"],"answer":x["answer"],"record_ids":list(dict.fromkeys(c.get("record_id") for c in (x["decision_artifact"] or {}).get("domain_flow",{}).get("typed_claims",[]) if c.get("record_id")))} for x in rows]},ensure_ascii=False))
