"""C04 exact game fields, offered relations and player-range source controls."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.scope import reference_time
out=R/('game_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite');store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():
  if kind=='game_mode' and k=='mode_name':v=bi(v)
  r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
for key,name,platform in [('pc','Amber PC Zone','PC'),('ps5','Cobalt Console Zone','PS5')]:
 create('zone','zone_'+key,{'name':bi(name)})
 create('resource','resource_'+key,{'name':bi('Station '+key),'zone_id':'zone_'+key,'capacity_persons':1})
 create('service','service_'+key,{'name':bi(name+' service'),'platform':platform,'resource_ids':['resource_'+key],'session_minutes':30,'capacity_min':1,'capacity_max':1})
for key,title in [('opal','Opal game'),('ruby','Ruby game'),('unhosted','Unhosted game')]:
 create('game','game_'+key,{'title':bi(title),'summary':bi('Controlled '+key+' summary'),'genre':bi('Controlled '+key+' genre'),'how_to_play':bi('Controlled '+key+' tutorial'),'supported_platforms':['PC','PS5'],'official_description':bi('Complete controlled '+key+' description'),'description_scope_note':bi('Recorded controlled description, not a live patch guarantee'),'description_captured_at':'2026-10-01T00:00:00+07:00'})
for game,platform in [('opal','pc'),('ruby','pc'),('ruby','ps5')]:create('game_service','offer_'+game+'_'+platform,{'game_id':'game_'+game,'service_id':'service_'+platform,'offered':True,'installed_resource_ids':['resource_'+platform]})
mode=create('game_mode','mode_opal',{'game_id':'game_opal','mode_name':'local','platform':'PC','players_min':2,'players_max':4,'studio_supported':True})
create('game_mode','mode_ruby',{'game_id':'game_ruby','mode_name':'local','platform':'PS5','players_min':1,'players_max':2,'studio_supported':True})
def run(q,op,facet,data=None):
 e=Engine.from_snapshot(data or view.snapshot());u=Understanding([MeaningTask(q,'games','C04',op,facet)],True,'controlled_game_matrix',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u)
 details.append({'question':q,'operation':op,'facet':facet,'result':r});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,e,u
for facet,q,expected in [('summary','What is Opal game?','Controlled opal summary'),('official_description','What is the full source description of Opal game?','Complete controlled opal description'),('how_to_play','How to play Opal game?','Controlled opal tutorial'),('genre','What genre is Opal game?','Controlled opal genre'),('supported_platforms','Which platforms does Opal game support?','PS5'),('studio_services','Which studio service offers Opal game?','Amber PC Zone service'),('zone','Which studio zone offers Opal game?','Amber PC Zone'),('players_max','How many players in Opal game on PC?','4'),('game_catalog','What games are offered in Amber PC Zone service?','Opal game')]:
 r,_,_=run(q,'detail',facet);checks['detail_'+facet+'_source_value']=any(c['facet']==facet and expected in c['value'] for c in r['claims'])
for facet,q,expected in [('studio_services','Can I play Opal game on PC?','Amber PC Zone service'),('zone','Which studio zone offers Opal game?','Amber PC Zone')]:
 r,_,_=run(q,'availability',facet);checks['availability_'+facet+'_confirmed_relation']=any(c['facet']==facet and expected in c['value'] for c in r['claims'])
for op,facet,q in [('list','game_catalog','List games offered by Amber PC Zone service'),('list','players_max','Which games can 3 people play?'),('list','zone','List games by studio zone'),('count','game_catalog','Count recorded games for PC'),('group_list','game_catalog','Group recorded games by platform PC and PS5'),('group_count','game_catalog','Count recorded games grouped by platform PC and PS5'),('group_list','zone','Group recorded games by zone'),('group_count','zone','Count recorded games grouped by zone')]:
 r,_,_=run(q,op,facet);checks[op+'_'+facet+'_actual_relation_values']=bool(r['claims']) and (all(c['record_id']=='mode_opal' for c in r['claims']) if facet=='players_max' else True)
 if op in {'group_list','group_count'}:
  groups=r['needs'][0]['execution_contract']['collection_proof']['groups'];expected={'PC':['game_opal','game_ruby'],'PS5':['game_ruby']} if facet=='game_catalog' else {'zone_pc':['game_opal','game_ruby'],'zone_ps5':['game_ruby']};checks[op+'_'+facet+'_exact_source_groups']=groups==expected
r,_,_=run('Which games can three people play?','list','players_max');checks['word_player_count_not_ignored']={c['record_id'] for c in r['claims']}=={'mode_opal'}
r,_,_=run('Which games can 3 people play?','list','players_max');checks['filtered_player_request_not_supplemented_unfiltered_catalog']=all(c['facet']=='players_max' for c in r['claims']);checks['player_range_and_mode_are_customer_visible']='2–4' in r['answer'] and 'local' in r['answer'];checks['final_player_constraint_has_source_range_proof']=any(c['kind']=='persons' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
r,_,_=run('Can I play Ruby game on PC?','availability','studio_services');checks['multi_platform_game_reply_uses_only_requested_service']=bool(r['claims']) and all('Cobalt Console Zone' not in c['value'] for c in r['claims'])
r,_,_=run('Which studio zone offers Ruby game on PC?','availability','zone');checks['multi_platform_game_reply_uses_only_requested_zone']=bool(r['claims']) and all(c['value']=='Amber PC Zone' for c in r['claims'])
for label,q,wanted,excluded in [('digits','Which games can 3 people play?','Opal game','Ruby game'),('words','Which games can three people play?','Opal game','Ruby game'),('mixed','Which games can 3 คน play?','Opal game','Ruby game'),('thai','มีเกมอะไรเล่นได้สามคน','Opal game','Ruby game'),('service','Can I play Ruby game on PC?','Amber PC Zone service','Cobalt Console Zone'),('zone','Which studio zone offers Ruby game on PC?','Amber PC Zone','Cobalt Console Zone')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):natural=CommonAnswerer(view).answer(q,locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
 details.append({'natural_question':q,'answer':natural.answer,'artifact':natural.decision_artifact});checks['natural_common_'+label+'_source_scope']=wanted in natural.answer and excluded not in natural.answer
r,_,_=run('Can I play Opal game on PS5?','availability','studio_services');checks['supported_platform_not_inferred_as_studio_offering']=not r['claims']
r,_,_=run('Can I play Unhosted game on PS5?','availability','studio_services');checks['unhosted_supported_game_not_studio_available']=not r['claims']
for label,q in [('multiple_counts','Which games can 2 people or 3 people play?'),('bounded_count','Which games can at least 3 people play?'),('count_range','Which games can 2–4 people play?'),('fractional_count','Which games can 2.5 people play?')]:
 r,_,_=run(q,'list','players_max');checks[label+'_not_silently_exact_first_count']=not r['claims'] and r['needs'][0]['status']=='missing_input'
r,e,u=run('Which games can 3 people play?','list','players_max');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0]
for field in ['players_min','players_max','studio_supported','game_id','platform']:
 child=copy.deepcopy(r['needs'][0]);refs=e.index.records['mode_opal']['fields'][field]['evidence_refs'];child['claims'][0]['evidence_refs']=[v for v in child['claims'][0]['evidence_refs'] if v not in refs];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['player_scope_required_locator_'+field]=bool(ledger['fatal'])
child=copy.deepcopy(r['needs'][0]);child['plan']['metadata']['player_filter_proofs'][child['claims'][0]['fact_id']]['players_min']=1;checks['forged_player_minimum_proof_rejected']=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
edit=copy.deepcopy(mode);edit['fields']['players_min']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled minimum not confirmed'};save_owner_record(store,edit,mode['revision'],'controlled-test');r,_,_=run('Which games can 1 person play on PC?','list','players_max');checks['unknown_players_min_not_assumed_one']=not r['claims']
mode=save_owner_record(store,{**edit,'fields':{**edit['fields'],'players_min':{'status':'known','value':2,'evidence_refs':[],'note':''}}},2,'controlled-test')['record']
r,e,u=run('Can I play Ruby game on PC?','availability','studio_services');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);child['plan']['metadata']['game_relation_projections'][child['claims'][0]['fact_id']]['target_ids']=['service_ps5'];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['forged_platform_projection_metadata_rejected']=bool(ledger['fatal']);details.append({'challenge':'forged_game_platform_projection','ledger':ledger})
r,e,u=run('What genre is Opal game?','detail','genre');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byrecord['game_ruby'] if f['facet']=='genre');child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['wrong_game_valid_field_receipt_rejected_without_target']=bool(ledger['fatal']);details.append({'challenge':'wrong_game_source_genre','ledger':ledger})
visitor=create('audience','not_service',{'name':bi('Visitor group, not a studio service')})
try:create('game_service','bad_service_offer',{'game_id':'game_opal','service_id':visitor['record_id'],'offered':True,'installed_resource_ids':[]});checks['owner_rejects_wrong_reference_kind']=False
except ValueError as ex:checks['owner_rejects_wrong_reference_kind']='wrong reference kind' in str(ex)
invalid=view.snapshot();bad=copy.deepcopy(invalid['release']['records']['offer_opal_pc']);bad['record_id']='invalid_snapshot_offer';bad['fields']['service_id']['value']=visitor['record_id'];invalid['release']['records'][bad['record_id']]=bad;r,_,_=run('Which studio service offers Opal game?','detail','studio_services',invalid);checks['unvalidated_snapshot_wrong_kind_not_printed_as_service']=bool(r['claims']) and 'Visitor group' not in r['answer']
from app.knowledge.common.domain_flow.capabilities import SUPPORTED
registered={(op,f) for op,fs in SUPPORTED['C04'].items() for f in fs};observed={(r['operation'],r['facet']) for r in details if 'operation' in r};checks['all_registered_C04_pairs_have_source_cases']=registered<=observed
(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');report={'all_passed':all(checks.values()),'checks':checks,'registered_operation_field_pairs':[list(p) for p in sorted(registered)],'invalid_snapshot_case_is_defensive_not_owner_accepted_data':True,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
