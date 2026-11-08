import copy,json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
O=R/("mechanical_receipt_controls_"+str(time.time_ns()));O.mkdir();view=DraftSnapshotView(CommonStore(R/"mechanical_future_definition_1793228332945926700/source.sqlite"));q="What is a mechanical keyboard?";clock=datetime.fromisoformat("2026-10-16T12:00:00+07:00");engine=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,"equipment","C03","detail","equipment_definition")],True,"test",{"model_called":False});result=engine.answer(q,"en",at=clock,allow_llm=False,understanding=u);snap=result["execution_contract"]["request_plan"]["snapshot"];task=compile_request(q,u,engine.index,snap).tasks[0];child=result["needs"][0];base=assess(engine.index,task,child,snap,q);checks={"valid_receipt_accepted":not base["fatal"] and bool(base["receipts"])};details={"baseline":base}
def challenge(name,change):
 x=copy.deepcopy(child);change(x["claims"][0]);ledger=assess(engine.index,task,x,snap,q);checks[name]=bool(ledger["fatal"]);details[name]=ledger
challenge("forged_name_source_rejected",lambda c:[r.__setitem__("source_id","FORGED") for r in c["evidence_refs"] if r["locator"].endswith("/name")])
challenge("missing_name_evidence_rejected",lambda c:c.__setitem__("evidence_refs",[r for r in c["evidence_refs"] if not r["locator"].endswith("/name")]))
challenge("forged_spec_source_rejected",lambda c:[r.__setitem__("source_id","FORGED") for r in c["evidence_refs"] if r["locator"].endswith("/specifications")])
challenge("altered_definition_rejected",lambda c:c.__setitem__("value","FORGED VALUE"))
challenge("wrong_facet_rejected",lambda c:c.__setitem__("facet","usage"))
report={"checks":checks,"all_passed":all(checks.values()),"scope":"actual isolated saved owner record; in-memory claim mutations, no HTTP/model"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
