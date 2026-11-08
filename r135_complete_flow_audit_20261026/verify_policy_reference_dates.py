"""Independent explicit-date source-interval controls for policy readers."""
import json,time,os,copy
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.policy_scope import applicability
from app.knowledge.common.answer import CommonAnswerer
O=R/('policy_reference_dates_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);checks={};details=[];clock='2026-10-27T12:00:00+07:00'
for cat,intent in [('C08','customer_cancel'),('C09','refund'),('C10','food_bring')]:
 r=template('faq');r['record_id']='dated_'+intent;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-06-01T00:00:00+07:00','effective_until':'2026-12-01T00:00:00+07:00'}
 for k,v in {'question':{'th':intent,'en':intent},'answer':{'th':'นโยบายควบคุมช่วงวันที่เฉพาะ','en':'Controlled policy valid only in its recorded interval.'},'topic':cat,'intent_key':intent}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 save_owner_record(store,r,0,'controlled-date-test')
view=DraftSnapshotView(store);e=Engine.from_snapshot(view.snapshot())
queries={'C08':'how can I cancel my booking?','C09':'how do I request a refund?','C10':'can I bring food?'}
def run(cat,prefix,public=False):
 q=prefix+', '+queries[cat];u=Understanding([MeaningTask(q,'reservation' if cat=='C08' else 'payment' if cat=='C09' else 'rules',cat,'detail','owner_policy',canonical_operation='policy.'+{'C08':'customer_cancel','C09':'refund','C10':'food_bring'}[cat])],True,'controlled_policy_dates',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')) as network:
  if public:
   out=CommonAnswerer(view).answer(q,locale='en',at=clock,planner=None);r={'answer':out.answer,'claims':out.decision_artifact.get('domain_flow',{}).get('typed_claims',[]),'artifact':out.decision_artifact}
  else:r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u)
 assert not network.called;details.append({'question':q,'public':public,'category':cat,'result':r});return r
for cat in queries:
 for prefix,expected,name in [('On 2026-07-01',True,'inside'),('On 2026-02-01',False,'before'),('On 2026-12-15',False,'after'),('On 2569-02-01',False,'buddhist_before'),('On 2026-02-30',False,'invalid'),('In 2026',False,'year_only'),('On 2026-07-01 and 2026-08-01',False,'multiple')]:
  r=run(cat,prefix);checks[cat+'_'+name]=bool(r['claims']) is expected
  if expected:
   need=r['needs'][0];proof=need['plan']['metadata'].get('policy_applicability',{});checks[cat+'_explicit_day_receipt']=bool(proof) and '2026-07-01' in json.dumps(proof)
   checks[cat+'_final_date_constraint_recomputed']=any(c['kind']=='date' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
for prefix,expected,name in [('On 2026-07-01',True,'inside'),('On 2026-02-01',False,'before')]:
 r=run('C08',prefix,True);checks['public_'+name]=bool(r['claims']) is expected
 if expected:checks['public_final_policy_date_constraint_supported']=any(c['kind']=='date' and c['status']=='structurally_supported' for c in r['artifact']['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
r=run('C08','On 2026-07-01');q=details[-1]['question'];u=Understanding([MeaningTask(q,'reservation','C08','detail','owner_policy')],True,'controlled_date_receipt',{'model_called':False});stamp=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,stamp).tasks[0];bad=copy.deepcopy(r['needs'][0]);bad['plan']['metadata']['policy_applicability'][bad['claims'][0]['fact_id']]['requested_reference_time']=clock;checks['forged_current_date_receipt_rejected']=bool(assess(e.index,task,bad,stamp,q)['fatal'])
from app.knowledge.common.domain_flow.request_verifier import verify
bad_contract=copy.deepcopy(r['execution_contract']);bad_contract['executor_results'][0]['receipts'][0]['requested_scope']['policy_applicability']['requested_reference_time']=clock;challenge=verify(e.index,q,bad_contract,children=r['needs']);checks['final_verifier_rejects_forged_policy_date']=all(c['status']!='structurally_supported' for c in challenge['constraint_coverage']['constraints'] if c['kind']=='date')
for prefix in ['On July 1, 2026','ในวันที่ 1 กรกฎาคม 2569']:
 r=run('C08',prefix);checks['month_text_'+prefix]=bool(r['claims']) and '2026-07-01' in json.dumps(r['needs'][0]['plan']['metadata'].get('policy_applicability',{}))
for prefix in ['On July 1, 2026 or December 15, 2026','On 2026-07-01 or December 15, 2026','วันนี้หรือพรุ่งนี้']:
 r=run('C08',prefix);checks['multiple_date_roles_'+prefix]=not r['claims']
dated=copy.deepcopy(e.index.records['dated_customer_cancel']);dated['validity']['effective_until']='2026-08-01T00:00:00+07:00';dated=save_owner_record(store,dated,dated['revision'],'controlled-date-test')['record'];e=Engine.from_snapshot(view.snapshot());r=run('C08','On 2026-07-01');checks['historical_policy_after_current_expiry_keeps_requested_day']=bool(r['claims']);r=run('C08','Today');checks['expired_policy_not_current']=not r['claims']
dated['validity']={'state':'known','effective_from':'2026-11-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'};save_owner_record(store,dated,dated['revision'],'controlled-date-test');e=Engine.from_snapshot(view.snapshot());r=run('C08','On 2026-12-01');checks['future_effective_policy_uses_requested_day']=bool(r['claims']);r=run('C08','Today');checks['future_effective_policy_not_yet_current']=not r['claims']
dated=copy.deepcopy(e.index.records['dated_customer_cancel']);dated['validity']={'state':'known','effective_from':'2026-11-01T13:00:00+07:00','effective_until':'2026-11-01T17:00:00+07:00'};save_owner_record(store,dated,dated['revision'],'controlled-date-test');e=Engine.from_snapshot(view.snapshot())
for prefix,expected,name in [('On 2026-11-01 at 14:00',True,'inside'),('On 2026-11-01 at 12:00',False,'before'),('On 2026-11-01 at 18:00',False,'after'),('On 2026-11-01 at 25:00',False,'invalid'),('On 2026-11-01 at 14:00 or 18:00',False,'multiple')]:
 r=run('C08',prefix);checks['policy_time_'+name]=bool(r['claims']) is expected
 if expected:checks['final_policy_time_constraint_supported']=any(c['kind']=='time' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
r=run('C08','On 2026-11-01 at 14:00',True);checks['public_source_interval_and_time_supported']=bool(r['claims']) and any(c['kind']=='time' and c['status']=='structurally_supported' for c in r['artifact']['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
r=run('C08','On 2026-11-01 at 14:00');bad_contract=copy.deepcopy(r['execution_contract']);bad_contract['executor_results'][0]['receipts'][0]['requested_scope']['policy_applicability']['requested_reference_time']='2026-11-01T16:00:00+07:00';challenge=verify(e.index,details[-1]['question'],bad_contract,children=r['needs']);checks['final_verifier_rejects_different_time_within_same_source_interval']=all(c['status']!='structurally_supported' for c in challenge['constraint_coverage']['constraints'] if c['kind']=='time')
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'semantic_accuracy_benchmark':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(O),**report}));assert report['all_passed']
