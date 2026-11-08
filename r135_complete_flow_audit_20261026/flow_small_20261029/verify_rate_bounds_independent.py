import copy,json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
O=R/("rate_bounds_independent_"+str(time.time_ns()));O.mkdir();v=DraftSnapshotView(CommonStore(R.parent/"rate_person_bounds_1793258094431170400/source.sqlite"));e=Engine.from_snapshot(v.snapshot());q="นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท";clock=datetime.fromisoformat("2026-03-16T12:00:00+07:00");u=Understanding([MeaningTask(q,"service_fee","C06","detail","amount")],True,"test",{"model_called":False});result=e.answer(q,"th",at=clock,allow_llm=False,understanding=u);snap=result["execution_contract"]["request_plan"]["snapshot"];task=compile_request(q,u,e.index,snap).tasks[0];child=result["needs"][0];base=assess(e.index,task,child,snap,q);checks={"baseline_receipt_exists":bool(base["receipts"])};details={"baseline":base}
x=copy.deepcopy(child)
for c in x["claims"]:c["evidence_refs"]=[r for r in c["evidence_refs"] if not r["locator"].endswith(("persons_min","persons_max"))]
y=assess(e.index,task,x,snap,q);checks["missing_bounds_refs_rejected"]=bool(y["fatal"]);details["missing_bounds_refs"]=y
z=copy.deepcopy(child)
for c in z["claims"]:
 for ref in c["evidence_refs"]:
  if ref["locator"].endswith("persons_min"):ref["source_id"]="FORGED"
f=assess(e.index,task,z,snap,q);checks["forged_bound_refs_rejected"]=bool(f["fatal"]);details["forged_bound_refs"]=f
z=copy.deepcopy(child)
for c in z["claims"]:c["numeric"]=999999
f=assess(e.index,task,z,snap,q);checks["altered_amount_rejected"]=bool(f["fatal"]);details["altered_amount"]=f
fact_id=child["claims"][0]["fact_id"]
fact=e.index.byid[fact_id]
old=fact.get("persons_min")
fact["persons_min"]=999
f=assess(e.index,task,child,snap,q);checks["forged_projected_min_rejected"]=bool(f["fatal"]);details["forged_projected_min"]=f
fact["persons_min"]=old
old=fact.get("persons_max")
fact["persons_max"]=999
f=assess(e.index,task,child,snap,q);checks["forged_projected_max_rejected"]=bool(f["fatal"]);details["forged_projected_max"]=f
fact["persons_max"]=old
report={"checks":checks,"all_passed":all(checks.values()),"scope":"forced receipt mutation in isolated Engine, no HTTP/model"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]

