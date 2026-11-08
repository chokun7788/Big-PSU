import copy,json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from unittest.mock import patch
import app.knowledge.common.domain_flow.meaning_reader as reader
O=R/("mechanical_independent_withhold_"+str(time.time_ns()));O.mkdir()
source=(R/"mechanical_semantic_scope_controls_1793233685932179200/meaning_reader_before_withdrawal.py").read_text(encoding="utf8"); ns={"__name__":"app.knowledge.common.domain_flow.old_meaning_reader","__package__":"app.knowledge.common.domain_flow"};exec(compile(source,"saved_reader","exec"),ns)
view=DraftSnapshotView(CommonStore(R/"mechanical_future_definition_1793228332945926700/source.sqlite"));q="What is a mechanical keyboard?";clock=datetime.fromisoformat("2026-10-16T12:00:00+07:00");engine=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,"equipment","C03","detail","equipment_definition")],True,"test",{"model_called":False})
with patch.object(reader,"apply",ns["apply"]): result=engine.answer(q,"en",at=clock,allow_llm=False,understanding=u)
encoded=json.dumps(result,ensure_ascii=False);checks={"verifier_detects_unproven_semantics":"source_receipt_equipment_definition_semantics_unproven" in encoded,"no_delivered_claims":not any(n.get("claims") for n in result["needs"])}
badview=DraftSnapshotView(CommonStore(R/"mechanical_semantic_scope_controls_1793233685932179200/source.sqlite"));badengine=Engine.from_snapshot(badview.snapshot())
with patch.object(reader,"apply",ns["apply"]): bad=badengine.answer(q,"en",at=clock,allow_llm=False,understanding=u)
checks["mislabelled_source_rejected_by_independent_verifier"]="source_receipt_equipment_definition_semantics_unproven" in json.dumps(bad,ensure_ascii=False);checks["mislabelled_source_not_delivered"]=not any(n.get("claims") for n in bad["needs"]);result={"valid_but_unreviewed":result,"mislabelled":bad}
report={"checks":checks,"all_passed":all(checks.values()),"scope":"saved experimental reader forced in isolated engine; verifier independently rejects"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
