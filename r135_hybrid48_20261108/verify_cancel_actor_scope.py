import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("cancel_actor_scope_controls_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(source or view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 details.append({"question":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def claims(x):return {c["record_id"] for c in x.decision_artifact.get("domain_flow",{}).get("typed_claims",[])} if x else set()
studio={"migrated_faq_rule_booking_cancel_invalid_info","migrated_faq_curated_reservation_cancel_invalid_info"};customer={"migrated_faq_rule_cancel_advance","migrated_faq_curated_cancel_1_hour"}
q="รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า ยกเลิกการจองยังไง";x=run(q);checks["saved_preamble_customer_scope"]=bool(claims(x)&customer) and not bool(claims(x)&studio)
x=run("ศูนย์ยกเลิกการจองโดยไม่แจ้งในกรณีใด");checks["thai_explicit_studio"]=bool(claims(x)&studio)
x=run("When can the studio cancel a booking without notice?");checks["english_explicit_studio"]=bool(claims(x)&studio)
x=run("เช็กข้อมูลศูนย์ให้หน่อย ยกเลิกการจองยังไง และราคา PC เท่าไหร่");checks["compound_customer_price"]=not bool(claims(x)&studio) and bool(claims(x)&customer) and any("rate" in c for c in claims(x))
rid="migrated_faq_rule_cancel_advance";r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);print("FIELDS",list(r["fields"]));r["fields"]["answer"]["value"]["th"]="การยกเลิกการจองต้องทำล่วงหน้า OWNER-ACTOR.TEST";save_owner_record(store,r,r["revision"],"isolated-actor-test");x=run(q);checks["owner_edit_visible"]=bool(x and "OWNER-ACTOR.TEST" in x.answer and rid in claims(x))
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s["release"]["records"][rid]["fields"]["answer"]["value"]["th"]="การยกเลิกการจอง FORGED-ACTOR.TEST";s["epoch"]+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(q,Forged());checks["forged_not_delivered"]=not (x and "FORGED-ACTOR.TEST" in x.answer)
report={"checks":checks,"all_passed":all(checks.values()),"scope":"isolated source-only controls; no model/http; no authority or semantic completeness claim"};(O/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report},ensure_ascii=False));assert report["all_passed"]
