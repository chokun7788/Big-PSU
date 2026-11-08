import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("mechanical_semantic_withdrawal_controls_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"mechanical_future_definition_1793228332945926700/source.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);a.close();b.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store);rows=[];checks={}
def run(q,loc):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view).answer(q,locale=loc,at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"question":q,"locale":loc,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def has(x,t):return bool(x and t in x.answer)
x=run("What is a mechanical keyboard and what is the PC price?","en");checks["compound_withholds_unverified_definition_and_keeps_price"]=not has(x,"OWNER-DEFINITION.TEST") and ("THB" in x.answer or "baht" in x.answer.lower())
x=run("What is an optical keyboard?","en");checks["other_subtype_not_given_mechanical_definition"]=not has(x,"OWNER-DEFINITION.TEST")
r=copy.deepcopy(view.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);r["fields"]["specifications"]["value"][-1]["value"]="This keyboard is in the PC zone, OPEN-ZONE-TEST.";save_owner_record(store,r,r["revision"],"isolated-mislabelled-definition")
x=run("What is a mechanical keyboard?","en");checks["location_statement_not_accepted_as_definition"]=not has(x,"OPEN-ZONE-TEST")
report={"checks":checks,"all_passed":all(checks.values()),"scope":"isolated source changes; semantic negative probe, no model"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
