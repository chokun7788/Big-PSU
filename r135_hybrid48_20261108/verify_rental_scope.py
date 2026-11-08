"""C07 source controls: negated organization and unsupported multi-day totals."""
import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.projection import value
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
e=Engine.from_snapshot(snapshot());clock=reference_time('2026-10-26T12:00:00+07:00');checks={};rows=[]
def run(q,op='price_calculate'):
 u=Understanding([MeaningTask(q,'rental','C07',op,'amount_thb')],True,'controlled_rental_scope',{'model_called':False});r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u);rows.append({'q':q,'result':r});return r,u
q='ราคาเหมา PC เต็มวัน หน่วยงานภายใน 2 วัน รวมเท่าไร';r,_=run(q)
checks['two_days_not_claimed_single_package_total']=r['status']=='partial' and bool(r['claims']) and 'No declared billing rule confirms a total' in r['answer'] and not r['needs'][0]['computations']
checks['multi_day_quantity_is_independent_unresolved_obligation']=any(c['kind']=='package_quantity' and c['status']=='review_required' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints']) and any(o['kind']=='request_constraint' for o in r['execution_contract']['executor_results'][0]['unresolved_obligations'])
r,_=run('ราคาเหมา PC เต็มวัน ไม่ใช่หน่วยงานภายในเท่าไร');checks['negative_only_does_not_infer_external_organization']=not r['claims'] and r['status']=='missing_input'
r,_=run('What is the PC full-day package price for an external visitor?');checks['individual_visitor_not_external_organization']=not r['claims'] and r['status']=='missing_input'
q='ราคาเหมา PC เต็มวัน หน่วยงานภายนอก ไม่ใช่หน่วยงานภายในเท่าไร';r,u=run(q);checks['positive_external_excludes_negated_internal']=bool(r['claims']) and all(value(e.index.records[c['record_id']],'audience_id')=='audience_external_org' for c in r['claims'])
child=copy.deepcopy(r['needs'][0]);fact=next(f for f in e.index.bycat['C07'] if f['facet']=='amount_thb' and value(e.index.records[f['record_id']],'audience_id')=='audience_internal_org')
child['claims']=[{'fact_id':fact['id'],'record_id':fact['record_id'],'facet':fact['facet'],'numeric':fact['numeric'],'value':fact['value']['en'],'evidence_refs':fact['evidence_refs']}];context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0];ledger=assess(e.index,task,child,context,q)
checks['valid_source_negative_organization_receipt_rejected']='source_receipt_organization_scope_mismatch' in ledger['fatal']
for quantity in ['0','-2','0.5']:
 r,_=run('ราคาเหมา PC เต็มวัน หน่วยงานภายใน '+quantity+' วัน');checks['invalid_quantity_'+quantity]=not r['claims'] and r['status']=='missing_input'
r,_=run('ราคาเหมา PC เต็มวัน หน่วยงานภายใน 1 แพ็กเกจ');cs=r['execution_contract']['verifier_result']['constraint_coverage']['constraints'];checks['one_package_unit_not_false_multi_day_total']=bool(r['claims']) and any(c['kind']=='package_quantity' and c['status']=='structurally_supported' for c in cs)
r,_=run('ราคาเหมา PC เต็มวัน หน่วยงานภายใน 2 packages รวมเท่าไร');checks['english_package_quantity_also_bounded']=r['status']=='partial' and 'No declared billing rule confirms a total' in r['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_source_changes':0};out=R/('rental_scope_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
