import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("mechanical_mixed_locale_controls_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"mechanical_future_definition_1793228332945926700/source.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);a.close();b.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store);rows=[];checks={}
def run(q,loc):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(view).answer(q,locale=loc,at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"question":q,"locale":loc,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def has(x,t):return bool(x and t in x.answer)
x=run("คีย์บอร์ด mechanical คืออะไร","th");checks["english_only_not_presented_as_thai"]=not has(x,"OWNER-DEFINITION.TEST")
x=run("What is a mechanical keyboard?","en");checks["english_source_to_english"]=has(x,"OWNER-DEFINITION.TEST")
x=run("What is a mechanical keyboard?","th");checks["explicit_thai_override_blocks_english_source"]=not has(x,"OWNER-DEFINITION.TEST")
r=copy.deepcopy(view.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);r["fields"]["specifications"]["value"][-1]["value"]="นิยามทดสอบ THAI-DEFINITION.TEST มีสวิตช์แยกแต่ละปุ่ม";save_owner_record(store,r,r["revision"],"isolated-definition-thai")
x=run("คีย์บอร์ด mechanical คืออะไร","th");checks["thai_owner_definition_delivered"]=has(x,"THAI-DEFINITION.TEST")
x=run("คีย์บอร์ด mechanical คืออะไร","en");checks["explicit_english_override_blocks_thai_source"]=not has(x,"THAI-DEFINITION.TEST")
r=copy.deepcopy(view.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);r["fields"]["specifications"]["value"][-1]["value"]="A mechanical keyboard uses individual switches under each key ภาษาไทย";save_owner_record(store,r,r["revision"],"isolated-mixed-english")
x=run("คีย์บอร์ด mechanical คืออะไร","th");checks["mostly_english_mixed_not_delivered_as_thai"]=not has(x,"individual switches")
r=copy.deepcopy(view.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);r["fields"]["specifications"]["value"][-1]["value"]="คีย์บอร์ดชนิดนี้ใช้สวิตช์แยกสำหรับแต่ละปุ่ม เรียกว่า mechanical switch";save_owner_record(store,r,r["revision"],"isolated-mixed-thai")
x=run("คีย์บอร์ด mechanical คืออะไร","th");checks["mostly_thai_mixed_delivered"]=has(x,"สวิตช์แยก")
report={"checks":checks,"all_passed":all(checks.values()),"scope":"scalar language script heuristic, no translation or semantic verification"};(O/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report},ensure_ascii=False));assert report["all_passed"]
