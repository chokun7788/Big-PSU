import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/("mechanical_definition_adversarial_"+str(time.time_ns()));O.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(O/"sessions.sqlite");a=sqlite3.connect((R/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);b.close();a.close();store=CommonStore(O/"source.sqlite");view=DraftSnapshotView(store);rid="equipment_gaming_keyboard";details=[];checks={}
def edit(name,entries):
 r=copy.deepcopy(view.snapshot()["release"]["records"][rid]);r["fields"]["name"]["value"]={"th":name,"en":name};r["aliases"]={"th":["คีย์บอร์ด mechanical"],"en":["mechanical keyboard"]};r["fields"]["specifications"]["value"]=[{"key":"zone","value":"PC Zone","unit":None}]+[{"key":k,"value":v,"unit":None} for k,v in entries];save_owner_record(store,r,r["revision"],"isolated-definition-adversarial")
def run(q="What is a mechanical keyboard?",src=None):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):x=CommonAnswerer(src or view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 details.append({"question":q,"answer":x.answer if x else None,"artifact":x.decision_artifact if x else None});return x
def has(x,t):return bool(x and t in x.answer)
edit("Mechanical Keyboard",[("definition","DEFINITION-ONE.TEST switches")]);x=run();checks["positive"]=has(x,"DEFINITION-ONE.TEST") and not has(x,"PC Zone")
edit("Gaming Keyboard",[("definition","WRONG-NAME.TEST")]);x=run();checks["wrong_name_alias_not_sufficient"]=not has(x,"WRONG-NAME.TEST")
edit("Mechanical Keyboard",[("usage","WRONG-KEY.TEST")]);x=run();checks["wrong_key_not_definition"]=not has(x,"WRONG-KEY.TEST")
edit("Mechanical Keyboard",[("definition","DUPLICATE-A.TEST"),("definition","DUPLICATE-B.TEST")]);x=run();checks["duplicate_definitions_not_selected"]=not has(x,"DUPLICATE-A.TEST") and not has(x,"DUPLICATE-B.TEST")
edit("Mechanical Keyboard",[("definition","DEFINITION-TWO.TEST switches")]);x=run();checks["second_edit_replaces_prior"]=has(x,"DEFINITION-TWO.TEST") and not has(x,"DEFINITION-ONE.TEST")
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s["release"]["records"][rid]["fields"]["specifications"]["value"][-1]["value"]="FORGED-DEFINITION.TEST";s["epoch"]+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(src=Forged());checks["forged_snapshot_not_delivered"]=not has(x,"FORGED-DEFINITION.TEST")
store.withdraw(rid,actor="isolated-definition-withdrawal");x=run();checks["withdrawal_not_delivered"]=not has(x,"DEFINITION-TWO.TEST")
report={"checks":checks,"all_passed":all(checks.values()),"scope":"isolated source edits only, no authority or semantic entailment claim"};(O/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
