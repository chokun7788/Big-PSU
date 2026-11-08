import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("mechanical_future_definition_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store)
r=copy.deepcopy(view.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);r["fields"]["name"]["value"]={"th":"Mechanical Keyboard","en":"Mechanical Keyboard"};r["aliases"]={"th":["คีย์บอร์ด mechanical"],"en":["mechanical keyboard"]};r["fields"]["specifications"]["value"].append({"key":"definition","value":"OWNER-DEFINITION.TEST describes a keyboard with individual mechanical switches","unit":None});save_owner_record(store,r,r["revision"],"isolated-definition-test")
with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view).answer("What is a mechanical keyboard?",locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
checks={"owner_definition_delivered":bool(x and "OWNER-DEFINITION.TEST" in x.answer),"owner_definition_claim":bool(x and any(c.get("record_id")=="equipment_gaming_keyboard" for c in x.decision_artifact.get("domain_flow",{}).get("typed_claims",[])))};out={"checks":checks,"all_passed":all(checks.values()),"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None,"scope":"isolated source edit, not authority or factual assertion"};(O/"RESULT.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),"checks":checks},ensure_ascii=False));assert out["all_passed"]
