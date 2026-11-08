"""Independent source calculations: positives, lifecycle, and adversarial outputs."""
import copy,json,runpy,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.calculation_check import errors

d=runpy.run_path(str(R/'verify_multi_audience_positive_20261106.py'))
e=d['e2'];u=d['u'];q=d['q'];result=d['updated'];child=result['needs'][0];snap=result['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0]
checks={'mixed_total_and_actual_owner_edit':all(d['checks'].values()),'positive_independent_source_check':not errors(e.index,q,child)};details=[]
for name,change in [
 ('forged_total',lambda x:x['computations'][0].update(total_thb=9999)),
 ('forged_rate',lambda x:x['computations'][0].update(unit_rate_thb=9999)),
 ('forged_quantity_and_arithmetic',lambda x:x['computations'][0].update(billing_quantity=9,total_thb=90)),
 ('forged_output_only',lambda x:x.update(answer=x['answer'].replace('Total: 110','Total: 9999'))),
]:
    x=copy.deepcopy(child);change(x);ledger=assess(e.index,task,x,snap,q);checks[name]=bool(ledger['fatal']);details.append({'case':name,'ledger':ledger})
x=copy.deepcopy(child);x['computations'][0].update(billing_quantity=9,total_thb=90)
x['plan']['metadata']['billing_lines'][0]['persons']=9
with patch('app.knowledge.common.domain_flow.financial.billing',return_value=x['plan']['metadata']['billing_lines']):
    ledger=assess(e.index,task,x,snap,q)
checks['forged_lines_rejected_even_if_selector_agrees']='hybrid_independent_calculation_unproven' in ledger['fatal']
for language,query in [('th','บริการอำพัน สำหรับ Amber visitors 2 คน ราคา รวมกี่บาท'),('en','What is the total price for Amber service for Amber visitors 2 people?')]:
    from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
    single=e.answer(query,language,at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=Understanding([MeaningTask(query,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False}))
    checks[language+'_valid_total']=bool(single['claims']) and any(c.get('total_thb')==20 for n in single['needs'] for c in n.get('computations',[])) and 'total is not confirmed' not in single['answer'] and 'ยังยืนยันยอดรวมไม่ได้' not in single['answer']
    details.append({'language':language,'result':single})
query='What is the total price for Amber service for Amber visitors?'
missing=e.answer(query,'en',at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=Understanding([MeaningTask(query,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False}))
checks['missing_quantity_notice']='total is not confirmed' in missing['answer'].lower() and missing['terminal_state']!='supported'
out=R/('hybrid_finance_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'source-only controlled fixtures, explicit numeric quantities; no general semantic proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps({'cases':details,'missing':missing},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
