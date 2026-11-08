"""Focused behavioral and adversarial contracts, real read-only source data."""
import copy,dataclasses,hashlib,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path[:0]=[str(S),str(R)]
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-16T12:00:00+07:00')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.request_plan import make_plan,attach,VERSION
from app.knowledge.common.query_scope import derived_names
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.intent_contracts import infer
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.pending_bindings import bind
from app.knowledge.common.registry import value
from app.knowledge.common.store import CommonStore
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
from app.pipeline.request_deadline import request_deadline,reserve_llm_call,current_deadline
view=MigratedView(S/'data/knowledge/common.sqlite');snap=view.snapshot();records=snap['release']['records'];names=derived_names(snap['release']['names'],records);checks=[]
before=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':dataclasses.asdict(detail) if dataclasses.is_dataclass(detail) else detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def ask(q,lang='en',h=None,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model network in deterministic contracts')):
  r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'contract_fixture'),history=h or [],allow_llm=False,allow_live=False,store=source or view)
 check('final envelope '+q, r.decision_artifact.get('request_plan',{}).get('version')==VERSION and bool(r.decision_artifact.get('need_results')) and all(n['task'] in TASKS or n['task']=='unresolved' for n in r.decision_artifact['request_plan']['needs']),r)
 return r
def hist(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
for q,task,predicate in [('VALORANT ใช้ผู้เล่นกี่คน','game_players','game_player_count'),('ศูนย์อยู่ไหน','center_location','center_location'),('How do I book?','procedure','booking_steps'),('What times can I book?','schedule','bookable_period'),('PC price','price','current_rate'),('PC full-day rental price','rental','rental_package'),('Can I bring alcohol?','policy','bring_permission')]:
 contract=infer(q);check('canonical predicate '+q,contract['task']==task and contract['predicate']==predicate,contract)
q='I want prices for external visitors';first=ask(q);h=hist(q,first)
pc=ask('PC',h=h);need=pc.decision_artifact['request_plan']['needs'][0]
check('PC binds service from current user and task from delivered state',need['task']=='price' and need['slots'].get('service',{}).get('origin')=='current_user' and need['slots'].get('task',{}).get('origin')=='delivered_state',pc)
location=ask('ศูนย์อยู่ไหน','th',h)
check('short new topic is not marked inherited',location.decision_artifact['request_plan']['needs'][0]['slot_origin']=='current_user' and 'pending_binding' not in location.decision_artifact['request_plan']['scope'],location)
untrusted=copy.deepcopy(h);untrusted[-1]['delivery_status']='not_sent'
plan=make_plan('PC',records,names,untrusted)
check('undelivered assistant state cannot bind price task',not plan.scope.get('pending_binding') and plan.needs[0].slot_origin=='current_user',dataclasses.asdict(plan))
newer=h+[{'role':'user','text':'hello'},{'role':'assistant','text':'Hello','delivery_status':'server_written','common_read_state':None}]
check('latest delivered turn blocks resurrection of older pending state',not make_plan('PC',records,names,newer).scope.get('pending_binding'))
ordinal=ask('option 2',h=h);expected=state_from_answer(first)['price_scope_request']['candidate_service_ids'][1]
check('ordinal selects displayed service preserving pending task',ordinal.decision_artifact['query_plan'].get('set_receipt',{}).get('member_ids')==[expected],ordinal)
missing=dict(records);missing.pop(expected)
b=bind('option 2',h,missing,names)
check('withdrawn ordinal does not shift to another service',b and b['action']=='invalid_selection' and b['reason']=='selected_record_withdrawn',b)
for q,lang in [('จองได้ช่วงไหน','th'),('What times can I book?','en'),('Which hours can I reserve?','en')]:
 r=ask(q,lang)
 check('timetable rather than steps '+q,r.decision_artifact.get('query_plan',{}).get('operation')=='calendar' and '13:00' in r.answer and r.decision_artifact['need_results'][0]['status']=='supported',r)
# Wrong-source injection: valid citations must not certify a wrong predicate.
steps=ask('How do I book?');raw_art={k:v for k,v in steps.decision_artifact.items() if k not in {'request_plan','need_results'}}
bad=attach(dataclasses.replace(steps,decision_artifact=raw_art),make_plan('What times can I book?',records,names),snap)
check('source-backed booking steps rejected as schedule answer',not bad.hits and bad.decision_artifact.get('predicate_rejection') and 'select a service' not in bad.answer.lower(),bad)
broken=dataclasses.replace(steps,validation=ValidationResult(False,('missing_source_pointer:fixture:answer',)),decision_artifact=raw_art)
bad=attach(broken,make_plan('How do I book?',records,names),snap)
check('broken source pointer classified separately from missing owner fact',bad.decision_artifact['need_results'][0]['status']=='broken_relation',bad)
with patch('app.knowledge.common.answer.CommonAnswerer.answer',return_value=bad):
 rejected=ask('How do I book?')
check('dispatcher rejection preserves source error and drops candidate facts',rejected.decision_artifact['need_results'][0]['status']=='broken_relation' and not rejected.hits and not rejected.decision_artifact['need_results'][0]['coverage']['receipts'],rejected)
q='Call of Duty เล่นได้ที่ไหน';first=ask(q,'th');pending=state_from_answer(first) or {};targets=pending.get('pending_target',{}).get('candidate_ids',[])
check('franchise ambiguity names current editions',len(targets)>=2 and first.decision_artifact['need_results'][0]['status']=='needs_user_slot',first)
if targets:
 title=value(records[targets[0]],'title')['en'];selected=ask(title,'en',hist(q,first))
 check('bare edition resumes offered location with source facts',selected.decision_artifact.get('target_binding',{}).get('record_id')==targets[0] and bool(selected.hits),selected)
 check('edition binding preserves real user span',selected.decision_artifact['request_plan']['question']==title and selected.decision_artifact['request_plan']['needs'][0]['slots']['task']['origin']=='delivered_state',selected)
q='Where can I play Call of Duty in 2027?';future=ask(q);pending=(state_from_answer(future) or {}).get('pending_target',{})
check('English franchise discovery preserves original qualified question',len(pending.get('candidate_ids',[]))>=2 and '2027' in pending.get('original_query',''),future)
if pending.get('candidate_ids'):
 selected=ask(value(records[pending['candidate_ids'][0]],'title')['en'],h=hist(q,future))
 check('edition selection retains year rather than returning unqualified facts',all('2027' in n['query'] or '2027' in n.get('slots',{}).get('qualified_query',{}).get('quote','') for n in selected.decision_artifact['request_plan']['needs']) and selected.decision_artifact['response_type'] not in {'answer','list'},selected)
q='Can I use an unknown game called Example Quest? Please answer briefly';r=ask(q)
check('unknown mention retained without claiming game does not exist','Example Quest' in r.answer and r.decision_artifact.get('unmatched_target',{}).get('reason')=='no_catalog_match',r)
check('catalog miss is explicitly no-answer without changing source status',r.decision_artifact.get('public_response_kind')=='no_answer' and r.decision_artifact['need_results'][0]['status']=='missing_source',r)
r=ask('Where is the Racezone Full Cockpit V3 located')
check('equipment location grammar keeps deterministic source answer',r.decision_artifact['request_plan']['needs'][0]['task']=='equipment_location' and bool(r.hits) and r.decision_artifact['response_type'] in {'answer','list'},r)
r=ask('What is Animal Crossing: New Horizons and what is FINAL FANTASY XVI?')
check('compound receipts bind to parent need IDs rather than child-local n1',len(r.decision_artifact['need_results'])==2 and all(row.get('receipts') and all(receipt.get('need_id')==row['need_id'] for receipt in row['receipts']+row['coverage']['receipts']) for row in r.decision_artifact['need_results']),r)
r=ask('Can I bring alcohol into the gaming area?')
check('alcohol consumption source does not prove bringing permission',r.decision_artifact.get('source_scope_review',{}).get('permission_inferred') is False and 'consum' in r.answer.lower() and bool(r.hits),r)
check('policy scope limit does not fabricate unrelated booking quota','per booking' not in r.answer.lower() and 'daily limit' not in r.answer.lower(),r)
r=ask('Can visitors use VR without booking?')
check('booking required policy is distinct from booking steps',r.decision_artifact['request_plan']['needs'][0]['predicate']=='booking_required' and bool(r.hits) and 'must' in r.answer.lower(),r)
for q in ['hello','Could you summarize an unknown studio topic?', 'PC ว่างไหม แล้วจองยังไง']:
 r=ask(q,'th' if 'จอง' in q else 'en')
corrupt=T/'ISOLATED_INVALID_NOT_PRODUCTION.sqlite';corrupt.write_text('not a sqlite database','utf8')
failed=ask('PC price',source=CommonStore(corrupt))
check('database failure remains temporary failure through finalizer',failed.decision_artifact['need_results'][0]['status']=='temporary_failure' and not failed.hits,failed)
check('no confirmed current price from unknown validity',ask('คนทั่วไปจอง PC ต้องจ่ายเท่าไหร่','th').decision_artifact['need_results'][0]['status']=='missing_source')
with patch.dict(os.environ,{'PSU_LLM_MAX_CALLS':'1'}):
 with request_deadline(20) as outer:
  allowed,_=reserve_llm_call('fixture_first')
  with request_deadline(1000) as nested:
   again,metadata=reserve_llm_call('fixture_nested');same=nested.deadline<=outer.deadline
  check('nested explicit timeout cannot extend deadline or reset model budget',allowed and not again and same and metadata['llm_budget_used_calls']==1,metadata)
  with request_deadline(.5) as nested:
   again,metadata=reserve_llm_call('fixture_shorter')
   check('shortened child deadline shares attempt ledger',not again and nested.deadline<outer.deadline,metadata)
after=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest();check('real database unchanged',before==after)
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x['case'] for x in checks if not x['passed']],'model_calls':0,'real_source_read_only':True,'full_test':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed']))
