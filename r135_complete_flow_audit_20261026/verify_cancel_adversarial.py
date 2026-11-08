import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("cancel_adversarial_controls_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite")
a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store);details=[];checks={};rid="procedure_change_time"
def edit(topic,pre,status="known",marker="PORTAL.TEST"):
 r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);r["fields"]["topic"]["value"]=topic;r["fields"]["name"]["value"]={"th":"วิธียกเลิกการจอง","en":"Cancel a booking"};r["fields"]["preconditions"]["value"]=pre;r["fields"]["preconditions"]["status"]=status;r["fields"]["preconditions"]["evidence_refs"]=[] if status=="unknown" else r["fields"]["preconditions"]["evidence_refs"];r["fields"]["steps"]["value"]=[{"order":1,"contact_id":None,"instruction":{"th":"ทดสอบยกเลิกผ่าน "+marker,"en":"Cancel using "+marker}}];r["aliases"]={"th":["วิธียกเลิกการจอง"],"en":["Cancel a booking"]};save_owner_record(store,r,r["revision"],"isolated-cancel-adversarial")
def run(q="How do I cancel my booking?",src=None):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(src or view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 details.append({"question":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def delivered(x,marker):return bool(x and marker in x.answer)
edit("cancel_booking",[]);x=run();checks["positive"]=delivered(x,"PORTAL.TEST")
x=run("How does the studio cancel a customer booking?");checks["wrong_actor_not_delivered"]=not delivered(x,"PORTAL.TEST")
edit("change_time",[]);x=run();checks["wrong_action_not_delivered"]=not delivered(x,"PORTAL.TEST")
edit("cancel_booking",[{"field":"issue","operator":"eq","value":"change_time"}]);x=run();checks["conditional_not_general"]=not delivered(x,"PORTAL.TEST")
edit("cancel_booking",None,"unknown");x=run();checks["unknown_preconditions_not_general"]=not delivered(x,"PORTAL.TEST")
edit("cancel_booking",[],marker="OWNER-SECOND.TEST");x=run();checks["second_owner_edit_delivered"]=delivered(x,"OWNER-SECOND.TEST") and not delivered(x,"PORTAL.TEST")
r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);r["fields"]["steps"]["value"][0]["instruction"]={"th":"เจ้าหน้าที่ยกเลิกผ่าน STAFF-ONLY.TEST","en":"Staff cancels using STAFF-ONLY.TEST"};save_owner_record(store,r,r["revision"],"isolated-cancel-actor");x=run();checks["staff_only_steps_not_customer_procedure"]=not delivered(x,"STAFF-ONLY.TEST")
edit("cancel_booking",[],marker="OWNER-SECOND.TEST")
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s["release"]["records"][rid]["fields"]["steps"]["value"][0]["instruction"]["en"]="Cancel using FORGED.TEST";s["epoch"]+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(src=Forged());checks["forged_snapshot_not_delivered"]=not delivered(x,"FORGED.TEST")
store.withdraw(rid,actor="isolated-cancel-withdrawal");x=run();checks["withdrawn_source_not_delivered"]=not delivered(x,"OWNER-SECOND.TEST")
report={"checks":checks,"all_passed":all(checks.values()),"source":"isolated copied sqlite owner edits; no HTTP or model","limitations":"Does not establish authority, semantic entailment, or full C08"};(O/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]

