import json,time
from datetime import datetime
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.readers import confirmed
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
O=R/("leg_strap_independent_"+str(time.time_ns()));O.mkdir()
view=DraftSnapshotView(CommonStore(R/"leg_strap_scope_1793253500961145500/source.sqlite"));e=Engine.from_snapshot(view.snapshot());q="In Nintendo Switch Sports, which button selects Soccer leg strap mode locally?";u=Understanding([MeaningTask(q,"game_controls","C05","control","input_bindings")],True,"test",{"model_called":False})
target="binding_1"
def forced(category,question,at=None,meaning=None):
 fs=[f for f in e.index.bycat["C05"] if f["record_id"]=="controls_nintendo_nintendo_switch_sports" and f["facet"]==target]
 p=confirmed("C05",fs,"forced_wrong_global_binding",operator="action_to_button");p.locked=True;return p
with patch.object(e,"plan",side_effect=forced): x=e.answer(q,"en",at=datetime.fromisoformat("2026-10-16T12:00:00+07:00"),allow_llm=False,understanding=u)
claims=[c for n in x.get("needs",[]) for c in n.get("claims",[])];checks={"wrong_global_binding_not_delivered":not any(c.get("facet")=="binding_1" for c in claims)}
target="binding_2"
with patch.object(e,"plan",side_effect=forced): y=e.answer(q,"en",at=datetime.fromisoformat("2026-10-16T12:00:00+07:00"),allow_llm=False,understanding=u)
claims2=[c for n in y.get("needs",[]) for c in n.get("claims",[])];checks["contradictory_binding_not_delivered"]=not any(c.get("facet")=="binding_2" for c in claims2)
report={"checks":checks,"all_passed":all(checks.values()),"scope":"forced plan in isolated engine using copied owner-edited source, not normal selector"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps({"wrong_binding":x,"contradictory_binding":y},ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
