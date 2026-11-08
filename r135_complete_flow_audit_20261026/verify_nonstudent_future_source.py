"""Isolated owner-edited staff eligibility probe; no HTTP or model."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=R/("nonstudent_future_source_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(o/"source.sqlite");view=DraftSnapshotView(store)
r=copy.deepcopy(view.snapshot()["release"]["records"]["r114_q037_owner_policy"])
r["fields"]["question"]["value"]={"th":"บุคลากร PSU ใช้ Cockpit ได้หรือไม่","en":"Can PSU staff use the Cockpit?"}
r["fields"]["answer"]["value"]={"th":"บุคลากร PSU ใช้ Cockpit ได้ตามเงื่อนไข STAFF-FIXTURE","en":"PSU staff may use the Cockpit subject to STAFF-FIXTURE."}
r["aliases"]={"th":["สิทธิบุคลากร PSU"],"en":["PSU staff eligibility"]}
r["fields"]["scope_note"]={"status":"unknown","value":None,"evidence_refs":[],"note":"fixture has no inherited external visitor scope"}
save_owner_record(store,r,r["revision"],"isolated-staff-eligibility-fixture")
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
 result=CommonAnswerer(view).answer("Can a PSU staff member access the Cockpit?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
a=result.decision_artifact if result else {};claims=a.get("domain_flow",{}).get("typed_claims",[]);checks={"edited_staff_eligibility_delivered":bool(result and "STAFF-FIXTURE" in result.answer),"edited_record_claim_delivered":any(c.get("record_id")==r["record_id"] for c in claims),"no_personnel_directory_for_access":not any(c.get("record_id","").startswith("member_") for c in claims)}
# Preserve the owner record revision when testing a misleading same-question answer.
r=copy.deepcopy(view.snapshot()["release"]["records"][r["record_id"]])
r["fields"]["answer"]["value"]={"th":"ห้องพักบุคลากรอยู่ใน PC zone MISLEADING.TEST","en":"The staff lounge is in the PC zone MISLEADING.TEST."}
save_owner_record(store,r,r["revision"],"isolated-staff-mislabel-fixture")
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
 bad=CommonAnswerer(view).answer("Can a PSU staff member access the Cockpit?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
checks["misleading_same_question_not_delivered"]=not bool(bad and "MISLEADING.TEST" in bad.answer)
# A literal positive-looking clause inside negation does not establish permission.
r=copy.deepcopy(view.snapshot()["release"]["records"][r["record_id"]])
r["fields"]["answer"]["value"]={"th":"ไม่จริงที่บุคลากร PSU ใช้ Cockpit ได้ NEGATED.TEST","en":"It is not true that PSU staff may use the Cockpit NEGATED.TEST."}
save_owner_record(store,r,r["revision"],"isolated-staff-negated-fixture")
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
 negated=CommonAnswerer(view).answer("Can a PSU staff member access the Cockpit?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
# A full negative statement is a legitimate answer, but must never be represented as positive permission.
claims_neg=negated.decision_artifact.get("domain_flow",{}).get("typed_claims",[]) if negated else []
checks["negated_source_not_misrepresented_as_positive_permission"]=not any(c.get("permission") is True for c in claims_neg)
checks["negated_source_not_selected_by_positive_literal_heuristic"]=not bool(negated and "NEGATED.TEST" in negated.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  snap=copy.deepcopy(view.snapshot());snap["release"]["records"][r["record_id"]]["fields"]["answer"]["value"]["en"]="PSU staff may use the Cockpit FORGED.TEST";snap["epoch"]+=10000;return snap
 def still_current(self,snap):return snap==self.snapshot()
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
 forged=CommonAnswerer(Forged()).answer("Can a PSU staff member access the Cockpit?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
checks["forged_snapshot_not_delivered"]=not bool(forged and "FORGED.TEST" in forged.answer)
out={"checks":checks,"all_passed":all(checks.values()),"source":"isolated copied sqlite owner edit only; hypothetical fixture, not policy","answer":result.answer if result else None,"artifact":a,"misleading_answer":bad.answer if bad else None,"misleading_artifact":bad.decision_artifact if bad else None,"negated_answer":negated.answer if negated else None,"negated_artifact":negated.decision_artifact if negated else None,"forged_answer":forged.answer if forged else None,"forged_artifact":forged.decision_artifact if forged else None};(o/"RESULT.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf8");print(json.dumps({"path":str(o),"checks":checks}));assert out["all_passed"]
