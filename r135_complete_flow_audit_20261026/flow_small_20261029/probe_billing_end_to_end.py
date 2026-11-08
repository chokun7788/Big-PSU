"""Observe unforced source-only mixed-audience billing against copied edits."""
import json,time,sys
from pathlib import Path
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
v=DraftSnapshotView(CommonStore(W/'billing_source_scope_1793318329343937400/source.sqlite'))
e=Engine.from_snapshot(v.snapshot());o=W/('billing_end_to_end_'+str(time.time_ns()));o.mkdir()
qs=['What is the total price for 1 PSU Student and Staff person and 1 PSU Alumni and General Student person to play Nintendo Switch for 1 hour?',
    'What is the total price for 1 PSU Student and Staff person and 1 PSU Alumni and General Student person to play PC for 1 hour?',
    'What is the price for PSU Student and Staff to play PC for 1 hour?',
    'What is the total price for 2 PSU Student and Staff people to play PC for 1 hour?']
rows=[]
for q in qs:
 u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
 r=e.answer(q,'en',at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=u)
 rows.append({'question':q,'result':r})
(o/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),'observations':len(rows),'scope':'unforced execution, source-only, not acceptance'}))
