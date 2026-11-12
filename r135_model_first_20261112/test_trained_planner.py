"""Supplied retained-wire controls, bounded review and source integration."""
import json,os,time
from unittest.mock import patch
from verification_support import R
os.environ.update(PSU_MODEL_FIRST_TRIAL='1',PSU_MODEL_FIRST_PLANNER='retained',PSU_ANALYSIS_BUDGET_SEC='60')
from app.knowledge.common.trained_planner import plan,parse
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.flow_context import request_context
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));index=Engine.from_snapshot(reader.store.snapshot(),cache_key=reader.store.path.resolve()).index
def task(q,d,f,op='detail'):
 return {'quote':q,'domain':d,'operation':op,'facet':f,'target':'','constraints':[],'ambiguous':False}
def wire(tasks):return json.dumps({'focus':'multiple','context_quotes':[],'tasks':tasks},ensure_ascii=False)
def response(content):return {'message':{'content':content},'provenance':{'effective_profile':'retained'}}
q='มีเกมอะไรบ้าง แล้วจองยังไง';single=wire([task('มีเกมอะไรบ้าง','games','game_catalog','list')]);full=wire([task('มีเกมอะไรบ้าง','games','game_catalog','list'),task('แล้วจองยังไง','reservation','owner_policy')])
checks={};rows=[]
def run(name,question,responses,left=60):
 with request_context() as ctx:
  ctx.input={'raw_question':question}
  with patch('app.knowledge.common.domain_flow.model_gateway.call',side_effect=responses) as call,patch('app.knowledge.common.bounded_time.remaining',return_value=left),patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP in supplied-plan controls')):
   items,audit=plan(question,index)
 rows.append({'id':name,'items':items,'audit':audit});return items,audit,call.call_count
items,audit,n=run('complete',[q][0],[response(full)])
checks['complete_plan_one_call']=len(items)==2 and n==1
checks['exact_quote_binding']=all(q[x['source_span']['start']:x['source_span']['end']]==x['quote'] for x in items)
checks['booking_subtype_bound_without_changing_domain']=items[1]['canonical_operation']=='policy.booking_steps' and items[1]['category']=='C08'
items,audit,n=run('repair_missing_booking',q,[response(single),response(full)])
checks['one_review_recovers_omitted_need']=n==2 and len(items)==2 and audit['selected_attempt']==2
checks['review_has_original_question']=audit['raw_question']==q
items,audit,n=run('failed_review_keeps_partial',q,[response(single),response('bad json')])
checks['failed_review_keeps_supported_subset']=n==2 and len(items)==1 and audit.get('partial_plan_retained') is True
checks['no_native_task_added']=items[0]['category']=='C04' and audit['native_corrective_tasks_added'] is False
items,audit,n=run('no_review_budget',q,[response(single)],left=5)
checks['review_skips_when_budget_low']=n==1 and audit['review_skipped']=='insufficient_remaining_request_budget'
items,audit,n=run('transport_failure',q,[OSError('synthetic unavailable')])
checks['transport_not_hidden_retry']=n==1 and items==[] and audit.get('transport_failure') is True
items,audit,n=run('truncated_output_no_repeat',q,[response('{"focus":"multiple","tasks":[')])
checks['truncated_protocol_not_retried']=n==1 and items==[] and audit.get('review_skipped')=='incomplete_protocol_output_not_retried'
items,audit,n=run('invalid_then_repaired',q,[response('bad json'),response(full)])
checks['invalid_protocol_one_review_only']=n==2 and len(items)==2
for name,content in [('invented_quote',wire([task('ราคาปลอม 123','service_fee','amount')])),('extra_fact',full[:-1]+',"answer":"FREE"}'),('duplicate_key',full[:-1]+',"focus":"price"}'),('forged_source_id',wire([{**task('มีเกมอะไรบ้าง','games','game_catalog'),'constraints':[{'slot':'audience','quote':'มีเกมอะไรบ้าง','source_record_id':'FORGED'}]}]))]:
 try:parse(content,q);checks[name+'_rejected']=False
 except (ValueError,TypeError,KeyError):checks[name+'_rejected']=True
q2='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง';full2=wire([task(q2.split(' แล้ว')[0],'service_fee','amount'),task('แล้วจองยังไง','reservation','owner_policy')])
with patch('app.knowledge.common.domain_flow.model_gateway.call',return_value=response(full2)) as call,patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP in source control')):
 r=reader.answer(q2,locale='th',planner=None)
rows.append({'id':'source_integration','answer':r.answer,'artifact':r.decision_artifact})
checks['source_price_and_booking']='0 บาท' in r.answer and 'สลิป' in r.answer
checks['no_false_plan_notice']='ส่วนที่ยังไม่มีแผนประมวลผล' not in r.answer
checks['duration_verified_not_erased']='ยังยืนยันการใช้เงื่อนไข' not in r.answer
checks['one_model_call_for_complete_integration']=call.call_count==1
checks['parent_receipts_retained']=len(r.decision_artifact['execution_contract']['tasks'])==2 and bool(r.decision_artifact['execution_contract']['tasks'][0]['receipts'])
out=R/('trained_planner_controls_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_calls':0,'mocked_gateway':True,'scope':'wire validation, at-most-one review/budget and source adapter; not model semantic accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
