"""C14 field aliases, event identity, validity and natural Common delivery."""
import copy,json,time,os
from datetime import datetime,timedelta
from unittest.mock import patch
from verification_support import R,snapshot
out=R/('news_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);clock=datetime.fromisoformat('2026-10-26T12:00:00+07:00');checks={};details=[]
def create(rid,title,body,start,end):
 r=template('news');r['record_id']=rid;r['aliases']['en']=['Amber Circuit'] if 'Amber' in title else [];r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':start,'effective_until':end}
 fields={'title':{'th':title,'en':title},'body':{'th':body,'en':body},'event_start':('2027' if '2027' in title else '2026')+'-12-01T09:00:00+07:00','event_end':('2027' if '2027' in title else '2026')+'-12-01T17:00:00+07:00','registration_url':'https://example.org/'+rid,'registration_status':'open','registration_status_as_of':(clock-timedelta(seconds=30)).isoformat(),'registration_status_max_age_seconds':120}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
current=create('news_amber_current','Amber Circuit 2026','Current controlled Amber announcement','2026-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00')
other=create('news_amber_other','Amber Circuit 2027','Other edition controlled announcement','2026-01-01T00:00:00+07:00','2028-01-01T00:00:00+07:00')
expired=create('news_expired','Archived Summit','Archived controlled announcement','2025-01-01T00:00:00+07:00','2026-01-01T00:00:00+07:00')
future=create('news_future','Future Summit','Future publication controlled announcement','2026-11-01T00:00:00+07:00','2027-01-01T00:00:00+07:00')
def run(q,facet='body',mode='engine',target='',at=clock,data=None):
 engine=Engine.from_snapshot(data or view.snapshot());u=Understanding([MeaningTask(q,'news','C14','detail',facet,target)],True,'controlled_news_matrix',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
  if mode=='common':
   result=CommonAnswerer(view).answer(q,locale='en',at=at,planner=None);r={'answer':result.answer,'claims':[c for e in result.decision_artifact['execution_contract']['executor_results'] for c in e['claims']],'execution_contract':result.decision_artifact['execution_contract'],'artifact':result.decision_artifact}
  else:r=engine.answer(q,'en',at=at,allow_llm=False,understanding=u)
 details.append({'question':q,'facet':facet,'mode':mode,'result':r});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,engine,u
cases=[('description','What are the details of Amber Circuit 2026?','body','Current controlled Amber announcement'),('body','What are the details of Amber Circuit 2026?','body','Current controlled Amber announcement'),('date','What is the event date of Amber Circuit 2026?','event_start','2026-12-01'),('event_start','What is the event date of Amber Circuit 2026?','event_start','2026-12-01'),('registration','What is the registration link for Amber Circuit 2026?','registration_url','https://example.org/news_amber_current'),('registration_url','What is the registration link for Amber Circuit 2026?','registration_url','https://example.org/news_amber_current'),('status','Is registration open for Amber Circuit 2026?','status','open')]
for facet,q,source_field,expected in cases:
 r,_,_=run(q,facet);checks['source_field_'+facet]=any(c['record_id']==current['record_id'] and c['facet']==source_field and expected in c['value'] for c in r['claims']) and all(c['record_id']==current['record_id'] for c in r['claims'])
r,e,u=run('What are the details of Amber Circuit 2026?');task=compile_request(details[-1]['question'],u,e.index,r['execution_contract']['request_plan']['snapshot']).tasks[0];child=copy.deepcopy(r['needs'][0]);fact=next(f for f in e.index.byrecord[other['record_id']] if f['facet']=='body');child['claims']=[{'fact_id':fact['id'],'record_id':fact['record_id'],'facet':'body','value':fact['value']['en'],'numeric':None,'evidence_refs':fact['evidence_refs']}];ledger=assess(e.index,task,child,r['execution_contract']['request_plan']['snapshot'],details[-1]['question']);checks['other_event_edition_rejected_even_when_planner_omits_target']=bool(ledger['fatal']);details.append({'challenge':'other_event_body_with_valid_source_refs','claims':child['claims'],'ledger':ledger})
for rid,name in [(expired['record_id'],'Archived Summit'),(future['record_id'],'Future Summit')]:
 r,_,_=run('Is registration open for '+name+'?','status');checks[rid+'_fresh_observation_does_not_override_publication_validity']=not r['claims'] and r['status']=='not_current'
r,_,_=run('What is the current announcement for Archived Summit?','body');checks['expired_announcement_not_current_publication']=not r['claims'] and r['status']=='not_current'
r,_,_=run('What is the registration link in the Amber Circuit 2026 announcement?','registration_url',mode='common');checks['natural_common_registration_link_is_first_requested_content']=r['claims'] and r['claims'][0]['facet']=='registration_url' and 'Current controlled Amber announcement' not in r['answer']
r,_,_=run('Is registration open for Unknown Cup?','status');checks['unknown_named_news_not_replaced_by_neighbor']=not r['claims']
r,_,_=run('Is registration open for Amber Circuit?','status');checks['shared_event_alias_requires_edition_not_arbitrary_status']=not r['claims'] and r['status']=='missing_input'
for q,facet,expected in [('ขอลิงก์สมัครในข่าวประชาสัมพันธ์ Amber Circuit 2026','registration_url','https://example.org/news_amber_current'),('วันจัดกิจกรรม Amber Circuit 2026 คือเมื่อไร','event_start','2026-12-01')]:
 r,_,_=run(q,facet,mode='common');checks['common_Thai_requested_'+facet]=r['claims'] and r['claims'][0]['facet']==facet and expected in r['claims'][0]['value']
r,_,_=run('Show the historical announcement for Archived Summit.','body');checks['explicit_historical_body_is_labelled_not_current_status']=bool(r['claims']) and 'Historical recorded announcement' in r['answer']
r,_,_=run('Is registration open in the historical announcement for Archived Summit?','status');checks['historical_word_does_not_authorize_current_status']=not r['claims']
r,_,_=run('Show the historical announcement for Future Summit.','body');checks['historical_word_does_not_authorize_future_publication']=not r['claims']
data=copy.deepcopy(view.snapshot());data['release']['records'][current['record_id']]['validity']={'state':'unknown'}
r,_,_=run('What are the details of Amber Circuit 2026?','body',data=data);checks['unknown_validity_body_is_recorded_partial_with_visible_limit']=bool(r['claims']) and r['status']=='partial' and 'validity period is unconfirmed' in r['answer']
r,_,_=run('Is registration open for Amber Circuit 2026?','status',data=data);checks['fresh_status_does_not_replace_unknown_publication_validity']=not r['claims']
# Bypass the reader with a valid status claim: the independent verifier must
# still reject a different requested observation date and expired publication.
r,e,u=run('Is registration open for Amber Circuit 2026?','status');snap=r['execution_contract']['request_plan']['snapshot'];child=copy.deepcopy(r['needs'][0])
for q,data,name in [('Is registration open for Amber Circuit 2026 tomorrow?',None,'forged_current_status_for_tomorrow_rejected'),('Is registration open for Amber Circuit 2026?',copy.deepcopy(view.snapshot()),'forged_fresh_status_from_expired_publication_rejected')]:
 challenged=e
 if data:
  data['release']['records'][current['record_id']]['validity']=copy.deepcopy(expired['validity']);challenged=Engine.from_snapshot(data)
 task=compile_request(q,Understanding([MeaningTask(q,'news','C14','detail','status')],True,'controlled',{}),challenged.index,snap).tasks[0]
 ledger=assess(challenged.index,task,child,snap,q);checks[name]=bool(ledger['fatal']);details.append({'challenge':name,'claims':child['claims'],'ledger':ledger})
actual=snapshot();actual_news=[rid for rid,r in actual['release']['records'].items() if r['kind']=='news'];checks['actual_source_news_absence_not_filled_by_controlled_fixture']=not actual_news
(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8')
report={'all_passed':all(checks.values()),'checks':checks,'actual_source_news_records':actual_news,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_news_not_real_announcement_or_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
