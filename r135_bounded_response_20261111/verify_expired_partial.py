"""Force an unresolved sibling after a valid typed price; expire model budget."""
import json,os,time
from unittest.mock import patch
from verification_support import R,snapshot
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.contracts import Plan
e=Engine.from_snapshot(snapshot());q='บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ';u=propose(e.index,q)
original=Engine.plan
def pending(self,category,question,at=None,meaning=None):
 if category=='C08':return Plan(category='C08',status='missing_source',reason='fixture_unresolved_booking',ambiguous=True,locked=False)
 return original(self,category,question,at,meaning)
candidate=next(f for f in e.index.byid.values() if f['category']=='C08')
with request_context() as ctx,patch.object(Engine,'plan',pending),patch.object(e,'scoped_candidates',return_value=[candidate]),patch.object(e.selector,'select',side_effect=AssertionError('expired model must not be called')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):
 result=e.answer(q,'th',at='2026-11-08T12:00:00+07:00',allow_llm=True,understanding=u)
checks={'verified_price_retained':any(c.get('facet')=='amount' and c.get('numeric')==400 for c in result.get('claims',[])),'budget_event_recorded':any(s.get('phase')=='analysis_budget_exhausted' for s in result['execution_contract']['schedule']),'timeout_disclosed':'วิเคราะห์ไม่ทันเวลา' in result['answer']}
out=R/('expired_partial_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'forced pending task with zero budget; source-only, no live slow-model proof'};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
