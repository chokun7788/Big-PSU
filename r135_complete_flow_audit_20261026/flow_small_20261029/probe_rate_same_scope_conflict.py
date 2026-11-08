import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=R/("rate_bounds_same_scope_probe_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite");a=sqlite3.connect((R.parent/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(o/"source.sqlite");v=DraftSnapshotView(store);out=[];checks={}
lo="migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student";hi="migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student"
def run(q,view=None,at="2026-10-16T12:00:00+07:00"):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view or v).answer(q,locale="th",at=at,planner=None)
 out.append({"q":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def claims(x):return [c for c in x.decision_artifact.get("domain_flow",{}).get("typed_claims",[]) if c["record_id"] in {lo,hi}] if x else []
def ids(x):return {c["record_id"] for c in claims(x)}

q="นักศึกษาต่างมหาลัย 4 คน เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท"
run(q,at="2026-03-16T12:00:00+07:00")
r=copy.deepcopy(v.snapshot()["release"]["records"][hi]);r["fields"]["persons_min"]["status"]="unknown";r["fields"]["persons_min"]["value"]=None;r["fields"]["persons_min"]["evidence_refs"]=[];save_owner_record(store,r,r["revision"],"isolated-missing-bounds");run(q,at="2026-03-16T12:00:00+07:00");run("นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท",at="2026-03-16T12:00:00+07:00")
r=copy.deepcopy(v.snapshot()["release"]["records"][hi]);r["fields"]["persons_min"]["status"]="known";r["fields"]["persons_min"]["value"]=1;r["fields"]["persons_max"]["value"]=2;save_owner_record(store,r,r["revision"],"isolated-overlap-bounds");run(q,at="2026-03-16T12:00:00+07:00");run("นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท",at="2026-03-16T12:00:00+07:00")
(o/"DETAILS.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(o),"answers":[x["answer"] for x in out]},ensure_ascii=False))
