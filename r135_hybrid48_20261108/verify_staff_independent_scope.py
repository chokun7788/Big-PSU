"""Force a mislabelled FAQ through an independent verifier in isolation."""
import json,time
from datetime import datetime
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
import app.knowledge.common.domain_flow.readers as reader
O=R/("staff_independent_scope_"+str(time.time_ns()));O.mkdir()
view=DraftSnapshotView(CommonStore(R/"nonstudent_future_source_1793245403159265800/source.sqlite"));engine=Engine.from_snapshot(view.snapshot());q="Can a PSU staff member access the Cockpit?";u=Understanding([MeaningTask(q,"rules","C10","detail","owner_policy")],True,"test",{"model_called":False})
def forced(index,cat,question,forced_intent=None,at=None):
 fs=[f for f in index.bycat[cat] if f["record_id"]=="r114_q037_owner_policy"]
 return reader.confirmed(cat,fs,"forced_mislabelled_staff_scope") if fs else None
with patch.object(reader,"policy",forced):result=engine.answer(q,"en",at=datetime.fromisoformat("2026-10-16T12:00:00+07:00"),allow_llm=False,understanding=u)
claims=[c for n in result.get("needs",[]) for c in n.get("claims",[])]; checks={"misleading_source_not_delivered":not any("MISLEADING.TEST" in str(c) for c in claims)}
receipts=[r for n in result.get("needs",[]) for r in n.get("execution_contract",{}).get("receipts",[])]
checks["unbound_staff_scope_not_verified"]=bool(receipts and all(not r.get("requested_scope",{}).get("verified") for r in receipts))
report={"checks":checks,"all_passed":all(checks.values()),"scope":"forced reader with actual owner-edited copied SQLite; no model or HTTP","limitations":"Tests independent delivery only; fixture is not policy."};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
