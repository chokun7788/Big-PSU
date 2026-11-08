import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=R/("leg_strap_scope_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite");a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(o/"source.sqlite");view=DraftSnapshotView(store);details=[];checks={};rid="controls_nintendo_nintendo_switch_sports"
def run(q,src=None,locale="en"):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(src or view).answer(q,locale=locale,at="2026-10-16T12:00:00+07:00",planner=None)
 details.append({"q":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def facets(x):return {(c["record_id"],c["facet"]) for c in x.decision_artifact.get("domain_flow",{}).get("typed_claims",[])} if x else set()
local="In Nintendo Switch Sports, if you want to select the leg strap mode in Soccer during Local/Friends play, what button do you need to press?";globalq="In Nintendo Switch Sports, which button selects Soccer leg strap mode in Play Globally?"
x=run(local);checks["local_only"]= (rid,"binding_2") in facets(x) and (rid,"binding_1") not in facets(x)
x=run(globalq);checks["global_only"]= (rid,"binding_1") in facets(x) and (rid,"binding_2") not in facets(x)
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode?");checks["missing_mode_no_wrong_choice"]=not bool(facets(x)&{(rid,"binding_1"),(rid,"binding_2")})
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode on PS5 locally?");checks["wrong_platform_no_switch_binding"]=not bool(facets(x)&{(rid,"binding_1"),(rid,"binding_2")})
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode, not local play?");checks["negated_local_not_selected"]=(rid,"binding_2") not in facets(x)
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode, not Play Globally?");checks["negated_global_not_selected"]=(rid,"binding_1") not in facets(x)
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode without playing locally?");checks["without_local_not_selected"]=(rid,"binding_2") not in facets(x)
x=run("เกม Nintendo Switch Sports ฟุตบอลโหมดสายรัดขาเล่นกับเพื่อนต้องกดปุ่มอะไร",locale="th");checks["thai_friends_positive"]=(rid,"binding_2") in facets(x) and (rid,"binding_1") not in facets(x)
x=run("เกม Nintendo Switch Sports ฟุตบอลโหมดสายรัดขา ไม่ใช่เล่นกับเพื่อน ต้องกดปุ่มอะไร",locale="th");checks["thai_negation_not_local"]=(rid,"binding_2") not in facets(x)
x=run("In Nintendo Switch Sports, which button selects Soccer leg strap mode locally, and how much does PC use cost?");checks["compound_local_and_price"]=((rid,"binding_2") in facets(x) and any("rate" in rec for rec,facet in facets(x)))
r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);r["fields"]["bindings"]["value"][2]["notes"]["en"]="OWNER-LOCAL.TEST";save_owner_record(store,r,r["revision"],"isolated-legstrap-edit");x=run(local);checks["actual_owner_edit_delivered"]=bool(x and "OWNER-LOCAL.TEST" in x.answer and (rid,"binding_2") in facets(x))
r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);r["fields"]["bindings"]["value"][2]["notes"]["en"]="Do not press + for local play; this button is for global play only.";save_owner_record(store,r,r["revision"],"isolated-contradictory-edit");x=run(local);checks["contradictory_source_not_delivered_as_local"]=(rid,"binding_2") not in facets(x)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s["release"]["records"][rid]["fields"]["bindings"]["value"][2]["notes"]["en"]="FORGED.TEST";s["epoch"]+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(local,Forged());checks["forged_snapshot_not_delivered"]=not bool(x and "FORGED.TEST" in x.answer)
report={"checks":checks,"all_passed":all(checks.values()),"scope":"bounded isolated source only, not authority or full C05"};(o/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(o/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(o),**report}));assert report["all_passed"]
