import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
e=Engine.from_snapshot(snapshot());q='What GPU do the PCs use?';clock=reference_time('2026-10-26T12:00:00+07:00')
u=Understanding([MeaningTask(q,'equipment','C03','detail','specifications')],True,'controlled_projection_check',{'model_called':False})
r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u);child=r['needs'][0];context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0];checks={};rows=[]
checks['actual_component_projection_recomputed']=bool(child['claims']) and child['plan']['metadata'].get('specification_keys')==['GPU'] and not child['execution_contract']['fatal'] and all(c['value_validation']=='registered_specification_projection_recomputed' for c in child['execution_contract']['receipts'])
for label,mutation in [('arbitrary_claim',lambda x:x['claims'][0].update(value='GPU: Free unlimited cloud GPU')),('extra_unrequested_component',lambda x:x['plan']['metadata'].update(specification_keys=['GPU','CPU'])),('foreign_calendar_display',lambda x:x['plan']['metadata'].update(customer_calendar_answer={'th':'เปิดทุกเวลา','en':'Open all hours'}))]:
 x=copy.deepcopy(child);mutation(x);ledger=assess(e.index,task,x,context,q);rows.append({'case':label,'ledger':ledger});checks[label+'_rejected']='source_receipt_projection_mismatch' in ledger['fatal']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'real_source_changes':0};out=R/('projection_receipts_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps({'original':r,'negative_controls':rows},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
