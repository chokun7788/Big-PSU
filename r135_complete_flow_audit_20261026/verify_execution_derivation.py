"""Changed execution text needs a validated derivation, not just an audit tag."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
out=R/('execution_derivation_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'isolated_conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.request_provenance import derived_input
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False)
r=template('game');r['record_id']='controlled_derivation_game';r['localization']['en_status']='agent_translated'
for k,v in {'title':{'th':'เกมอำพันทดสอบ','en':'Amber game'},'genre':{'th':'แนวทดสอบอำพัน','en':'Controlled amber genre'},'summary':{'th':'คำอธิบายอำพันทดสอบ','en':'Controlled amber summary'}}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
save_owner_record(store,r,0,'controlled-test');view=DraftSnapshotView(store);e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);checks={};rows=[]
raw='What is the genre of Amber game?';changed='What is the summary of Amber game?'
def typed(q,facet):return Understanding([MeaningTask(q,'games','C04','detail',facet,'Amber game')],True,'controlled_derivation',{'model_called':False})
with request_context() as ctx:
 ctx.input={'raw_question':raw,'requested_locale':'en','effective_locale':'en'}
 result=e.answer(changed,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(changed,'summary'));rows.append({'case':'unattested_field_change','result':result})
 checks['unattested_changed_field_cannot_deliver_source_claims']=not result['claims'] and result['terminal_state'] not in {'supported','partial'}
with request_context() as ctx:
 ctx.input={'raw_question':raw,'requested_locale':'en','effective_locale':'en'};derived_input(changed,'invented_transform',[{'origin':'current_user','text':raw}],facts_inherited=False)
 result=e.answer(changed,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(changed,'summary'));rows.append({'case':'unregistered_receipt','result':result});checks['audit_receipt_alone_does_not_authorize_field_change']=not result['claims']
with request_context() as ctx:
 ctx.input={'raw_question':raw,'requested_locale':'en','effective_locale':'en'}
 ctx.pin_reference_time('2026-10-26T12:00:00+07:00')
 derived_input(changed,'calendar_date_resolution',[{'origin':'current_or_delivered_user_date_scope','text':raw}],index=e.index,parent_question=raw)
 result=e.answer(changed,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(changed,'summary'));checks['known_transform_name_without_valid_recomputation_rejected']=not result['claims']
parent='What is the genre of Amber game and what is its summary?';part='what is its summary?';child=part+' Amber game'
with request_context() as ctx:
 ctx.input={'raw_question':parent,'requested_locale':'en','effective_locale':'en'}
 segments=[{'origin':'current_question_task','source_span':{'start':parent.index(part),'end':len(parent),'text':part}},{'origin':'explicit_shared_binding','binding':{'source_span':{'start':parent.index('Amber game'),'end':parent.index('Amber game')+len('Amber game'),'text':'Amber game'},'validation_outcome':'validated'}}]
 derived_input(child,'compiled_parent_task',segments,index=e.index,parent_question=parent)
 result=e.answer(child,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(child,'summary'));checks['validated_parent_span_and_shared_entity_still_work']=any('Controlled amber summary' in c['value'] for c in result['claims'])
with request_context() as ctx:
 ctx.input={'raw_question':parent,'requested_locale':'en','effective_locale':'en'}
 result=e.answer(part,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(part,'summary'));checks['arbitrary_raw_substring_is_not_a_parent_task_receipt']=not result['claims']
with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 ctx.input={'raw_question':raw,'requested_locale':'en','effective_locale':'en'}
 result=CommonAnswerer(view).answer(changed,locale='en',at='2026-10-26T12:00:00+07:00',planner=None);rows.append({'case':'common_changed_field','answer':result.answer,'artifact':result.decision_artifact});checks['common_reader_cannot_bypass_raw_input_guard']=not result.decision_artifact.get('domain_flow',{}).get('typed_claims') and 'Controlled amber summary' not in result.answer
with request_context() as ctx:
 ctx.input={'raw_question':raw.upper(),'requested_locale':'en','effective_locale':'en'}
 result=e.answer(raw.lower(),'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=Understanding([MeaningTask(raw.lower(),'games','C04','detail','genre','amber game')],True,'controlled_normalized',{'model_called':False}));checks['actual_casefold_normalization_still_delivers']=any('Controlled amber genre' in c['value'] for c in result['claims'])
for day in [0,6]:
 calendar=template('schedule');calendar['record_id']='controlled_derivation_calendar_'+str(day)
 for key,value in {'weekday':day,'timezone':'Asia/Bangkok','zone_ids':[],'open_periods':[{'start':'09:00','end':'18:00'}],'bookable_periods':[{'start':'09:00','end':'12:00'}],'maintenance_periods':[{'start':'13:00','end':'16:00'}],'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'16:00','state':'maintenance'}],'service_closed':False}.items():calendar['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
 save_owner_record(store,calendar,0,'controlled-test')
with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 result=CommonAnswerer(view).answer('Is play service open today at 10:00?',locale='en',at='2026-10-26T12:00:00+07:00',planner=None);rows.append({'case':'real_date_resolution','answer':result.answer,'artifact':result.decision_artifact})
 checks['real_date_resolution_preserves_source_answer']=bool(result.decision_artifact.get('domain_flow',{}).get('typed_claims'))
 checks['real_date_transform_has_recomputed_receipt']=any(event.get('kind')=='calendar_date_resolution' and event.get('input_derivation_validation',{}).get('verified') for event in ctx.events)
with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 history=[{'role':'assistant','delivery_status':'server_written','common_read_state':{'schema_version':1,'date_pending':{'version':1,'day':25,'query':'Is play service open on 25 at 10:00?','reference_date':'2026-10-26','facts_in_state':False}}}]
 result=CommonAnswerer(view).answer('October 2026',history=history,locale='en',at='2026-10-26T12:00:00+07:00',planner=None);rows.append({'case':'delivered_month_reply','answer':result.answer,'artifact':result.decision_artifact})
 checks['delivered_date_reply_recomputed_from_current_reply_and_state']=any(event.get('kind')=='calendar_date_resolution' and event.get('input_derivation_validation',{}).get('verified') for event in ctx.events) and result.decision_artifact.get('execution_contract',{}).get('path')!='input_derivation_guard'
service=template('service');service['record_id']='controlled_derivation_service'
for key,value in {'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'capacity_min':1,'capacity_max':1}.items():service['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
save_owner_record(store,service,0,'controlled-test')
for label,question,state,kind in [('financial','30 minutes',{'r114_pending':{'version':1,'category':'C06','query':'What is the price of Amber service for 2 hours?','root_ids':[service['record_id']],'slot':'billing_period'}},'delivered_financial_resume'),('live','Amber service',{'live_scope_pending':{'version':1,'query':'Is it available on 2026-10-26 at 10:00?','facts_in_state':False}},'delivered_live_resume')]:
 with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
  history=[{'role':'assistant','delivery_status':'server_written','common_read_state':{'schema_version':1,**state}}]
  result=CommonAnswerer(view).answer(question,history=history,locale='en',at='2026-10-26T12:00:00+07:00',planner=None);rows.append({'case':label+'_reply','answer':result.answer,'artifact':result.decision_artifact})
  checks[label+'_resume_has_validated_derivation_without_claiming_missing_business_data']=any(event.get('kind')==kind and event.get('input_derivation_validation',{}).get('verified') for event in ctx.events) and result.decision_artifact.get('execution_contract',{}).get('path')!='input_derivation_guard'
from app.session.conversation_store import ConversationStore
from app.knowledge.common.dialogue import state_from_answer
initial=CommonAnswerer(view).answer(raw,locale='en',at='2026-10-26T12:00:00+07:00',planner=None);state=state_from_answer(initial);sessions=ConversationStore(persistence_path=None)
turn=sessions.begin('controlled-derived-session','t1',raw,locale='en');sessions.complete('controlled-derived-session','t1',turn['revision'],{'ok':True,'request_id':'controlled-derived-response','answer':initial.answer,'common_read_state':state});sessions.delivery('controlled-derived-session','t1','server_written')
with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 result=CommonAnswerer(view).answer('And its summary?',history=sessions.history('controlled-derived-session'),locale='en',at='2026-10-26T12:00:00+07:00',planner=None);rows.append({'case':'actual_server_delivered_game_followup','answer':result.answer,'artifact':result.decision_artifact})
 checks['actual_delivered_task_resolution_recomputed_and_source_backed']='Controlled amber summary' in result.answer and any(event.get('kind')=='r128_delivered_task_resolution' and event.get('input_derivation_validation',{}).get('verified') for event in ctx.events)
with request_context() as ctx:
 ctx.input={'raw_question':parent,'requested_locale':'en','effective_locale':'en'};ctx.pin_reference_time('2026-10-26T12:00:00+07:00');ctx.bind_snapshot(view.snapshot());before=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
 derived_input(child,'compiled_parent_task',segments,index=before.index,parent_question=parent)
 edit=store.get(r['record_id'])['record'];edit['fields']['genre']['value']={'th':'แนวทดสอบรุ่นใหม่','en':'Controlled updated genre'};save_owner_record(store,edit,edit['revision'],'controlled-test')
 after=Engine.from_snapshot(view.snapshot(),cache_key=view.path);result=after.answer(child,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=typed(child,'summary'));checks['source_epoch_change_invalidates_previous_derivation_receipt']=not result['claims'] and result['execution_contract']['input_derivation_validation'].get('reason')=='derivation_source_snapshot_changed'
empty_store=CommonStore(out/'empty.sqlite');empty_store.initialize(allow_demo=False)
with request_context() as ctx:
 ctx.input={'raw_question':raw,'requested_locale':'en','effective_locale':'en'}
 result=CommonAnswerer(empty_store).answer(changed,locale='en',at='2026-10-26T12:00:00+07:00',planner=None);checks['empty_source_unverified_input_still_has_safe_uniform_result']=not result.hits and result.decision_artifact['execution_contract']['terminal_state']=='invalid_plan' and not result.decision_artifact['execution_contract']['executor_results'][0]['claims']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
