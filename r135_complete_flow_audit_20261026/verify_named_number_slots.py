"""Entity title numbers/units must not become user quantity constraints."""
import json,time,os,copy
from datetime import datetime
from unittest.mock import patch
from verification_support import R
out=R/('named_number_slots_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'isolated_conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.dialogue_task import resolve
from app.knowledge.common.domain_flow.meaning_reader import execution_query
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};rows=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for key,value in fields.items():r['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
for n,name in enumerate(['One Hour','2 Players','Two Sessions','7 Minutes']):create('game','controlled_numeric_game_'+str(n),{'title':{'th':'ชื่อทดสอบ '+name,'en':name},'genre':{'th':'แนวเกมทดสอบ '+str(n),'en':'Controlled genre '+str(n)}})
create('equipment_model','controlled_numeric_device',{'name':{'th':'พีซีทดสอบหมายเลข7','en':'PC 7'},'device_type':'pc','specifications':[{'key':'RAM','value':'16','unit':'GB'}]})
e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);clock='2026-10-26T12:00:00+07:00'
for n,name in enumerate(['One Hour','2 Players','Two Sessions','7 Minutes']):
 q='What genre is '+name+'?';task=MeaningTask(q,'games','C04','detail','genre',name);u=Understanding([task],True,'controlled_numeric_names',{'model_called':False});working=apply(q,e.index,copy.deepcopy(u));context=resolve(e.index,q,[],view.snapshot()['active'],datetime.fromisoformat(clock))
 checks[name+'_title_not_quantity_slot']=not any(c['slot'] in {'duration','sessions','persons'} for c in working.tasks[0].constraints)
 checks[name+'_dialogue_preserves_title']=name.casefold() in context['execution_question'].casefold() and context['task'].get('duration_minutes') is None and not context['task'].get('person_counts')
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):result=CommonAnswerer(view).answer(q,locale='en',at=clock,planner=None)
 rows.append({'name':name,'question':q,'working':working.as_dict(),'dialogue':context,'answer':result.answer,'artifact':result.decision_artifact});checks[name+'_normal_source_answer']='Controlled genre '+str(n) in result.answer
 contract=result.decision_artifact['execution_contract'];checks[name+'_no_phantom_verifier_quantity_or_extra_need']=not any(c['kind'] in {'persons','duration','sessions'} for c in contract['verifier_result']['constraint_coverage']['constraints']) and not any(t.get('facet')=='players_max' for t in contract['request_plan']['tasks'])
q='What genre is 2 Players for 3 people?';u=Understanding([MeaningTask(q,'games','C04','detail','genre','2 Players')],True,'controlled_real_quantity',{'model_called':False});working=apply(q,e.index,u)
checks['real_persons_outside_title_preserved']=any(c['slot']=='persons' and c['quote'].casefold()=='3 people' for c in working.tasks[0].constraints) and not any(c['slot']=='persons' and c['quote'].casefold()=='2 players' for c in working.tasks[0].constraints)
create('game','controlled_numeric_ambiguous_name',{'title':{'th':'ชื่อทดสอบ 3 people','en':'3 people'},'genre':{'th':'แนวเกมทดสอบ','en':'Controlled extra genre'}});e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
from app.knowledge.common.domain_flow.request_verifier import observe
observed=observe(e.index,q);checks['real_quantity_not_hidden_by_another_game_having_that_title']=any(c['kind']=='persons' and c['source_span']['text']=='3 people' for c in observed['constraints'])
q='What is the price of game One Hour for 2 hours?';task=MeaningTask(q,'service_fee','C06','detail','amount','One Hour');u=apply(q,e.index,Understanding([task],True,'controlled_title_plus_duration',{'model_called':False}));executed=execution_query(e.index,q,u.tasks[0]);checks['unit_normalizer_preserves_target_title_but_keeps_real_duration']='One Hour' in executed and '2 hours' in executed and not any(c['slot']=='duration' and c['quote'].casefold()=='one hour' for c in u.tasks[0].constraints)
ordinary=resolve(e.index,'What is the price of PC for one hour?',[],view.snapshot()['active'],datetime.fromisoformat(clock));checks['ordinary_duration_not_stolen_by_matching_game_title']=ordinary['task']['duration_minutes']==60 and not ordinary['task']['game_ids']
q='What is the price of game One Hour for One Hour?';task=MeaningTask(q,'service_fee','C06','detail','amount','One Hour');u=apply(q,e.index,Understanding([task],True,'controlled_repeated_title_unit',{'model_called':False}));executed=execution_query(e.index,q,u.tasks[0]);checks['same_unit_phrase_as_title_and_real_duration_keeps_both']='game One Hour for 1 Hour' in executed
q='What genre is 2 Players for 2 Players?';task=MeaningTask(q,'games','C04','detail','genre','2 Players');u=apply(q,e.index,Understanding([task],True,'controlled_repeated_entity_quantity',{'model_called':False}))
from app.knowledge.common.domain_flow.plan_contract import compile_request
compiled=compile_request(q,u,e.index,{'release_id':'owner-draft-preview','epoch':view.snapshot()['epoch'],'reference_time':clock});persons=[s for s in compiled.tasks[0].slots if s.kind=='persons'];checks['repeated_quantity_quote_binds_outside_title']=len(persons)==1 and persons[0].source_span.start==q.rfind('2 Players')
q='What are the specifications of PC 7?';task=MeaningTask(q,'equipment','C03','detail','specifications','PC 7');u=apply(q,e.index,Understanding([task],True,'controlled_numbered_device',{'model_called':False}));checks['resource_number_not_person_or_session_quantity']=u.tasks[0].target=='PC 7' and not any(c['slot'] in {'persons','sessions','duration'} for c in u.tasks[0].constraints)
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
