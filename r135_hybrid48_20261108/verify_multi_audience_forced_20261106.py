"""Bounded forced-plan positive control; bypasses normal interpretation only."""
import json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.financial import billing
from app.knowledge.common.domain_flow.contracts import Plan
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
o=R/('multi_audience_forced_'+str(time.time_ns()));o.mkdir()
view=DraftSnapshotView(CommonStore(R/'multi_audience_positive_1793960278642793700'/'source.sqlite'))
e=Engine.from_snapshot(view.snapshot());q='What is the total for Amber service for Amber visitors 2 people and Sapphire visitors 3 people?'
facts=[f for f in e.index.byid.values() if f.get('record_id') in {'amber_rate','sapphire_rate'} and f.get('category')=='C06' and f.get('facet')=='amount']
lines=billing(e.index,q,facts);out={'fact_count':len(facts),'lines':lines}
try:
 assert len(facts)==2 and isinstance(lines,list) and len(lines)==2
 plan=Plan(ids=[f['id'] for f in facts],status='answer',reason='forced_source_facts',category='C06',facets=['amount'],metadata={'billing_lines':lines})
 at=datetime.fromisoformat('2026-03-16T12:00:00+07:00')
 plan=e.finish_plan('C06',q,plan,at);child=e._render_one('C06',q,'en',plan,at)
 u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
 initial=e.answer(q,'en',at=at,allow_llm=False,understanding=u)
 snap=initial['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0]
 ledger=assess(e.index,task,child,snap,q)
 out.update(answer=child['answer'],claims=child['claims'],computations=child['computations'],fatal=ledger['fatal'],receipts=ledger['receipts'])
 out['checks']={'two_source_bound_lines':len(lines)==2,'expected_total':any(c.get('total_thb')==60 for c in child['computations']) and any(c.get('total_thb')==20 for c in child['computations']),'verifier_accepts':not ledger['fatal'] and len(ledger['receipts'])==2}
except Exception as ex:out['exception']=repr(ex);out['checks']={'fixture_reached_verifier':False}
out['all_passed']=all(out['checks'].values());out['scope']='controlled data and forced plan; no normal-selection or semantic proof'
(o/'RESULT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),'checks':out['checks'],'exception':out.get('exception')},ensure_ascii=False))
