import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=R/("cancel_future_source_controls_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(o/"source.sqlite");view=DraftSnapshotView(store)
r=copy.deepcopy(view.snapshot()["release"]["records"]["procedure_change_time"]);r["fields"]["topic"]["value"]="cancel_booking";r["fields"]["name"]["value"]={"th":"วิธียกเลิกการจอง","en":"Cancel a booking"};r["fields"]["preconditions"]["value"]=[];r["fields"]["steps"]["value"]=[{"order":1,"contact_id":None,"instruction":{"th":"ทดสอบยกเลิกผ่าน PORTAL.TEST","en":"Cancel using PORTAL.TEST"}}];r["aliases"]={"th":["วิธียกเลิกการจอง"],"en":["Cancel a booking"]};save_owner_record(store,r,r["revision"],"isolated-cancel-fixture")
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
 result=CommonAnswerer(view).answer("How do I cancel my booking?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
a=result.decision_artifact if result else {};claims=a.get("domain_flow",{}).get("typed_claims",[]);checks={"owner_procedure_delivered":bool(result and "PORTAL.TEST" in result.answer),"owner_procedure_has_claim":any(c.get("record_id")=="procedure_change_time" for c in claims),"no_unconfirmed_when_procedure_delivered":bool(result and "cancellation procedure is not confirmed" not in result.answer.lower())};out={"checks":checks,"all_passed":all(checks.values()),"source":"isolated copied sqlite owner edit only","answer":result.answer if result else None,"artifact":a};(o/"RESULT.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf8");print(json.dumps({"path":str(o),"checks":checks},ensure_ascii=False));assert out["all_passed"]
