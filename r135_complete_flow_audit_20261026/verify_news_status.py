"""Positive and negative C14 status source controls through the real owner API."""
import copy,json,time
from datetime import datetime,timedelta
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.task_registry import readiness
from app.knowledge.common.answer import CommonAnswerer
out=R/('news_status_verification_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled_news.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store)
at=datetime.fromisoformat('2026-10-26T12:00:00+07:00');checks={};rows=[]
r=template('news');r['record_id']='controlled_summit_news';r['aliases']['en']=['Fixture Summit'];r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'}
fields={'title':{'th':'งานทดลองซัมมิต','en':'Fixture Summit'},'body':{'th':'รายละเอียดงานจากข้อมูลทดสอบ','en':'Controlled event details'},'event_start':'2026-12-01T09:00:00+07:00','event_end':'2026-12-01T17:00:00+07:00','registration_url':'https://example.org/register'}
for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
version=0
def save(changes):
 global r,version
 for key,value in changes.items():r['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''} if value is not None else {'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled missing source'}
 result=save_owner_record(store,copy.deepcopy(r),version,'controlled-test');version=result['version'];r=result['record'];return Engine.from_snapshot(view.snapshot(),cache_key=view.path)
def run(e,question='Is registration open for Fixture Summit?',clock=at):
 u=Understanding([MeaningTask(question,'news','C14','detail','status',target='Fixture Summit')],True,'controlled_status_source',{'model_called':False})
 result=e.answer(question,'en',at=clock,allow_llm=False,understanding=u);rows.append({'question':question,'clock':clock.isoformat(),'result':result});return result
e=save({});result=run(e);checks['future_event_date_and_url_do_not_imply_open']=not result['claims']
e=save({'registration_status':'open','registration_status_as_of':(at-timedelta(seconds=30)).isoformat(),'registration_status_max_age_seconds':120});result=run(e)
checks['owner_can_add_status_without_model_or_code_change']=any(c['facet']=='status' and c['value']=='open' for c in result['claims'])
checks['fresh_status_has_source_and_clock_receipts']=bool(result['needs'][0]['plan']['metadata']['registration_status_freshness']) and all(c['evidence_refs'] for c in result['claims']) and not result['needs'][0]['execution_contract']['fatal']
checks['observation_time_is_customer_visible']='2026-10-26T11:59:30+07:00' in result['answer']
checks['natural_intent_preserves_status']=propose(e.index,'Is registration open for Fixture Summit?').tasks[0].facet=='status'
natural=CommonAnswerer(view).answer('Is registration open for Fixture Summit?',locale='en',at=at,planner=None)
checks['shared_chat_path_uses_real_status_source']='open' in natural.answer and bool(natural.decision_artifact.get('domain_flow',{}).get('typed_claims'))
expired=run(e,clock=at+timedelta(seconds=121));checks['expired_observation_not_delivered']=not expired['claims'] and expired['status']=='not_current'
future=run(e,clock=at-timedelta(seconds=31));checks['future_observation_not_delivered']=not future['claims'] and future['status']=='not_current'
tomorrow=run(e,'Is registration open for Fixture Summit on 2026-10-27?');checks['observed_now_not_projected_to_other_date']=not tomorrow['claims']
e=save({'registration_status':'closed'});edited=run(e);checks['source_edit_changes_next_request']=any(c['value']=='closed' for c in edited['claims']) and not any(c['value']=='open' for c in edited['claims'])
e=save({'registration_status_max_age_seconds':None});unknown=run(e);checks['missing_freshness_not_guessed']=not unknown['claims']
diagnostic=readiness(r,view.snapshot()['release']['records'],locale='en',at=at)
checks['owner_readiness_names_missing_status_evidence']='registration_status_max_age_seconds' in json.dumps(diagnostic)
legacy=template('news');legacy['fields'].pop('registration_status');legacy['fields'].pop('registration_status_as_of');legacy['fields'].pop('registration_status_max_age_seconds')
from app.knowledge.common.registry import schema_errors
checks['old_optional_field_absence_still_schema_valid']=not schema_errors(legacy)
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_data_or_approvals_modified':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
