"""Probe independent total verification by forging a computed total."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
p=R/'flow_small_20261029'/'total_notice_fixture_1793332530765053000'
q='What is the total price for 2 people for Amber service for Amber visitors?'
e=Engine.from_snapshot(DraftSnapshotView(CommonStore(p/'source.sqlite')).snapshot())
u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
r=e.answer(q,'en',at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=u)
snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0])
assert child['computations'];baseline=assess(e.index,task,child,snap,q)
child['computations'][0]['total_thb']=9999
forged=assess(e.index,task,child,snap,q)
checks={'baseline_accepted':bool(baseline['receipts']) and not baseline['fatal'],'forged_total_rejected':bool(forged['fatal'])}
child=copy.deepcopy(r['needs'][0])
child['computations'][0]['billing_quantity']=3
child['computations'][0]['total_thb']=372
forged_quantity=assess(e.index,task,child,snap,q)
checks['forged_quantity_with_consistent_total_rejected']=bool(forged_quantity['fatal'])
child=copy.deepcopy(r['needs'][0])
child['computations'][0]['billing_quantity']=3
child['computations'][0]['total_thb']=372
child['plan']['metadata']['billing_lines']=[{'fact_id':child['computations'][0]['fact_id'],'persons':3}]
forged_lines=assess(e.index,task,child,snap,q)
checks['forged_billing_lines_rejected']=bool(forged_lines['fatal'])
o=R/('total_independent_forgery_'+str(time.time_ns()));o.mkdir();report={'checks':checks,'all_passed':all(checks.values()),'scope':'direct verifier result mutation; not normal execution or evidence of delivered forged total'}
(o/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(o/'DETAILS.json').write_text(json.dumps({'baseline':baseline,'forged':forged},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),**report}));assert report['all_passed']

