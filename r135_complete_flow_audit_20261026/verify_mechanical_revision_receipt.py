import copy,json,time,sqlite3
from datetime import datetime
from verification_support import R
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
O=R/("mechanical_revision_receipt_controls_"+str(time.time_ns()));O.mkdir();view=DraftSnapshotView(CommonStore(R/"mechanical_future_definition_1793228332945926700/source.sqlite"));q="What is a mechanical keyboard?";clock=datetime.fromisoformat("2026-10-16T12:00:00+07:00");engine=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,"equipment","C03","detail","equipment_definition")],True,"test",{"model_called":False});result=engine.answer(q,"en",at=clock,allow_llm=False,understanding=u);snap=result["execution_contract"]["request_plan"]["snapshot"];task=compile_request(q,u,engine.index,snap).tasks[0];child=result["needs"][0];base=assess(engine.index,task,child,snap,q);checks={"valid_receipt_accepted":not base["fatal"] and bool(base["receipts"])};details={"baseline":base}
def challenge(name,change):
 x=copy.deepcopy(child);change(x["claims"][0]);ledger=assess(engine.index,task,x,snap,q);checks[name]=bool(ledger["fatal"]);details[name]=ledger
challenge("forged_name_source_rejected",lambda c:[r.__setitem__("source_id","FORGED") for r in c["evidence_refs"] if r["locator"].endswith("/name")])
challenge("missing_name_evidence_rejected",lambda c:c.__setitem__("evidence_refs",[r for r in c["evidence_refs"] if not r["locator"].endswith("/name")]))
challenge("forged_spec_source_rejected",lambda c:[r.__setitem__("source_id","FORGED") for r in c["evidence_refs"] if r["locator"].endswith("/specifications")])
challenge("altered_definition_rejected",lambda c:c.__setitem__("value","FORGED VALUE"))
challenge("wrong_facet_rejected",lambda c:c.__setitem__("facet","usage"))
a=sqlite3.connect((R/"mechanical_future_definition_1793228332945926700/source.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(O/"source.sqlite");a.backup(b);a.close();b.close();store=CommonStore(O/"source.sqlite");newview=DraftSnapshotView(store);record=copy.deepcopy(newview.snapshot()["release"]["records"]["equipment_gaming_keyboard"]);record["fields"]["specifications"]["value"][-1]["value"]="A different definition after owner revision.";save_owner_record(store,record,record["revision"],"isolated-revision-replay");newengine=Engine.from_snapshot(newview.snapshot());newresult=newengine.answer(q,"en",at=clock,allow_llm=False,understanding=u);newsnap=newresult["execution_contract"]["request_plan"]["snapshot"];newtask=compile_request(q,u,newengine.index,newsnap).tasks[0];replay=assess(newengine.index,newtask,child,newsnap,q);checks["old_claim_rejected_after_owner_revision"]=bool(replay["fatal"]);newchild=newresult["needs"][0];newledger=assess(newengine.index,newtask,newchild,newsnap,q);checks["new_receipt_uses_current_owner_revision"]=bool(newledger["receipts"]) and newledger["receipts"][0]["record_revision"]==newview.snapshot()["release"]["records"]["equipment_gaming_keyboard"]["revision"];details["new_receipt"]=newledger;details["old_claim_after_owner_revision"]=replay
report={"checks":checks,"all_passed":all(checks.values()),"scope":"actual isolated saved owner record; in-memory claim mutations, no HTTP/model"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
