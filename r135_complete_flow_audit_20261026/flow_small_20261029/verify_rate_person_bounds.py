import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=R/("rate_person_bounds_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite");a=sqlite3.connect((R.parent/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(o/"source.sqlite");v=DraftSnapshotView(store);out=[];checks={}
lo="migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student";hi="migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student"
def run(q,view=None,at="2026-10-16T12:00:00+07:00"):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view or v).answer(q,locale="th",at=at,planner=None)
 out.append({"q":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def claims(x):return [c for c in x.decision_artifact.get("domain_flow",{}).get("typed_claims",[]) if c["record_id"] in {lo,hi}] if x else []
def ids(x):return {c["record_id"] for c in claims(x)}
x=run("นักศึกษาต่างมหาลัย 1 คน เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท");checks["one_person_scope_disclosed"]=ids(x)=={lo,hi} and "1–2" in x.answer and "3–4" in x.answer
x=run("นักศึกษาต่างมหาลัย 4 คน เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท");checks["four_people_allocation_unconfirmed"]=ids(x)=={lo,hi} and "คำนวณยอดรวมไม่ได้" in x.answer and "× 4" not in x.answer;checks["bounds_refs_present"]=bool(claims(x)) and all({"/mapped_fields/persons_min","/mapped_fields/persons_max"}<={r["locator"] for r in c["evidence_refs"]} for c in claims(x))
x=run("นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท");checks["unbound_capacity_disclosed"]=bool(x and ("1–2" in x.answer or "1-2" in x.answer) and ("3–4" in x.answer or "3-4" in x.answer))
r=copy.deepcopy(v.snapshot()["release"]["records"][hi]);r["fields"]["persons_min"]["value"]=5;r["fields"]["persons_max"]["value"]=6;save_owner_record(store,r,r["revision"],"isolated-bounds-edit");x=run("นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท",at="2026-03-16T12:00:00+07:00");checks["owner_bounds_edit_visible"]=bool(x and "5–6" in x.answer and "3–4" not in x.answer)
class Forged:
 path=v.path
 def connect(self):return store.connect()
 def snapshot(self):
  z=copy.deepcopy(v.snapshot());z["release"]["records"][hi]["fields"]["persons_min"]["value"]=8;z["epoch"]+=10000;return z
 def still_current(self,z):return z==self.snapshot()
x=run("นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท",Forged());checks["forged_bounds_not_delivered"]=not bool(x and "8–6" in x.answer)
report={"checks":checks,"all_passed":all(checks.values()),"scope":"source-only copied SQLite; no authority or general billing claim"};(o/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(o/"DETAILS.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(o),**report}));assert report["all_passed"]
