"""Source-adjudicated controller/console positive and negative controls."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R,snapshot
from app.knowledge.common.registry import template,schema_errors
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.controller_catalog import selection,request,claim_errors,FACET
from app.knowledge.common.answer import CommonAnswerer
O=R/('controller_catalog_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated_session.sqlite');checks={};details=[];store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);at='2026-10-27T05:00:00+07:00';bi=lambda s:{'th':s,'en':s}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-source-test')['record']
for platform in ['PC','PS5']:
 create('zone','zone_'+platform.lower(),{'name':bi('Amber room' if platform=='PC' else 'Cobalt room')});create('resource','resource_'+platform.lower(),{'name':bi('Unit '+platform),'zone_id':'zone_'+platform.lower(),'capacity_persons':1});create('service','service_'+platform.lower(),{'name':bi(platform+' offered service'),'platform':platform,'studio_zone_ids':['zone_'+platform.lower()],'resource_ids':['resource_'+platform.lower()],'session_minutes':60,'capacity_min':1,'capacity_max':1})
for key in ['amber','ruby','unknown','unoffered','wheel','mouse','motion']:
 create('game','game_'+key,{'title':bi(key.title()+' game'),'summary':bi(key+' description')})
for key,platform in [('amber','PC'),('ruby','PS5'),('unknown','PS5'),('wheel','PC'),('mouse','PC'),('motion','PC')]:create('game_service','offer_'+key,{'game_id':'game_'+key,'service_id':'service_'+platform.lower(),'offered':True,'installed_resource_ids':['resource_'+platform.lower()]})
binding={'buttons':['X'],'gesture':'press','action':bi('Controlled action'),'context':{'th':None,'en':None},'notes':{'th':None,'en':None},'section':{'th':None,'en':None},'source_order':1,'button_label':bi('X')}
controls={}
for key,platform,model in [('amber','PC','PS5'),('ruby','PS5','PS4'),('unknown','PS5',None),('unoffered','PC','PS5')]:
 f={'game_id':'game_'+key,'platform':platform,'input_device':'gamepad','preset':'controlled','bindings':[binding]}
 if model:f['input_device_model']=model
 controls[key]=create('control_set','controls_'+key,f)
for key,kind,model in [('wheel','racing_wheel','AmberWheel'),('mouse','keyboard_mouse','AmberPoint'),('motion','vr_motion','AmberMotion')]:controls[key]=create('control_set','controls_'+key,{'game_id':'game_'+key,'platform':'PC','input_device':kind,'input_device_model':model,'preset':'controlled','bindings':[binding]})
def run(q,*,public=False,locale='en',data=None,op=None,facet='game_catalog'):
 snap=data or view.snapshot();e=Engine.from_snapshot(snap);u=Understanding([MeaningTask(q,'games','C04',op or ('count' if 'Count' in q else 'list'),facet)],True,'controlled_controller_catalog',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')) as network:
  if public:
   class View:
    path=store.path
    def snapshot(self):return snap
    def still_current(self,s):return s is snap
   obj=CommonAnswerer(View()).answer(q,locale=locale,at=at,planner=None);r={'answer':obj.answer,'artifact':obj.decision_artifact,'claims':obj.decision_artifact.get('domain_flow',{}).get('typed_claims',[])}
  else:r=e.answer(q,locale,at=at,allow_llm=False,understanding=u)
 assert not network.called;details.append({'q':q,'public':public,'result':r});(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,e,u
q='Which games support a PS5 controller?';r,e,u=run(q)
checks['specific_controller_uses_PC_game_with_exact_model_source']={c['record_id'] for c in r['claims']}=={'controls_amber'}
checks['console_game_is_not_controller_model_proof']='Ruby game' not in r['answer'] and 'Unknown game' not in r['answer']
checks['unoffered_game_not_studio_catalog']='Unoffered game' not in r['answer']
checks['unknown_compatibility_visible_without_claiming_absence']='remain unconfirmed' in r['answer']
checks['only_controller_facet_returned']=all(c['facet']==FACET for c in r['claims'])
checks['controller_model_not_interpreted_as_console_platform']=selection(e.index,q,at)['request']['model']=='ps5' and selection(e.index,q,at)['proofs'][r['claims'][0]['fact_id']]['requested_platforms']==[] if r['claims'] else False
for query in ['เกมที่ใช้จอย PS5 มีอะไร','Which games support a PS5 controller?']:
 p,_,_=run(query,public=True,locale='th' if query.startswith('เกม') else 'en');checks['public_'+('th' if query.startswith('เกม') else 'en')+'_preserves_controller_scope']={c['record_id'] for c in p['claims']}=={'controls_amber'}
r,_,_=run('Which games on PS5 use a PS5 controller?');checks['separate_console_constraint_not_lost']=not r['claims']
r,_,_=run('Which games in Amber room use a PS5 controller?');checks['source_named_zone_kept']={c['record_id'] for c in r['claims']}=={'controls_amber'}
r,_,_=run('Which games in Cobalt room use a PS5 controller?');checks['wrong_named_zone_does_not_leak_PC_controller_game']=not r['claims']
r,_,_=run('Which games on Unit PC use a PS5 controller?');checks['named_resource_requires_recorded_installation']={c['record_id'] for c in r['claims']}=={'controls_amber'}
r,_,_=run('Which games on Unit PS5 use a PS5 controller?');checks['wrong_resource_does_not_leak_controller_game']=not r['claims']
r,_,_=run('Which games use a PS5 controller on 2026-02-01?');checks['explicit_controller_date_source_intervals_applied']={c['record_id'] for c in r['claims']}=={'controls_amber'} and any(c['kind']=='date' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
r,_,_=run('Which games use a PS5 controller on 2025-02-01?');checks['current_controller_fact_not_used_before_effective_date']=not r['claims']
r,_,_=run('Which games use a PS5 controller in 2025?');checks['controller_year_not_silently_current_date']=not r['claims'] and 'give the date' in r['answer']
r,_,_=run('Which games use a controller?');checks['generic_gamepad_not_specific_model']={c['record_id'] for c in r['claims']}=={'controls_amber','controls_ruby','controls_unknown'}
r,_,_=run('เกมที่ใช้จอยมีอะไร');checks['generic_thai_gamepad_not_question_words_as_model']={c['record_id'] for c in r['claims']}=={'controls_amber','controls_ruby','controls_unknown'}
r,_,_=run('Which games use a PS4 controller?');checks['different_model_uses_own_source_only']={c['record_id'] for c in r['claims']}=={'controls_ruby'}
r,_,_=run('Which games support PS6 controllers?');checks['unknown_plural_model_not_generic_gamepad']=not r['claims']
r,_,_=run('List controller games');checks['generic_prefix_not_model_name']={c['record_id'] for c in r['claims']}=={'controls_amber','controls_ruby','controls_unknown'}
r,_,_=run('Which games use PS5 or PS4 controllers?');checks['multiple_model_roles_not_silently_last_model']=not r['claims'] and 'separate list' in r['answer']
r,_,_=run('Which games do not support a PS5 controller?');checks['other_model_not_negative_compatibility_proof']=not r['claims'] and 'does not prove incompatibility' in r['answer']
checks['definition_not_catalog']=request(e.index,'What is a PS5 controller game?') is None
checks['button_question_not_catalog']=request(e.index,'What does the PS5 controller X button do in Amber game?') is None
r,_,_=run('Which games use an AmberWheel racing wheel?');checks['racing_wheel_model_source_supported']={c['record_id'] for c in r['claims']}=={'controls_wheel'}
r,_,_=run('Which games use a Delta racing wheel?');checks['unknown_wheel_model_not_generic_wheel']=not r['claims']
r,_,_=run('Which games use an AmberPoint mouse?');checks['mouse_model_source_supported']={c['record_id'] for c in r['claims']}=={'controls_mouse'}
r,_,_=run('Which games use a Delta mouse?');checks['unknown_mouse_model_not_generic_mouse']=not r['claims']
r,_,_=run('Which games use a keyboard and mouse?');checks['keyboard_mouse_class_not_multiple_models']={c['record_id'] for c in r['claims']}=={'controls_mouse'}
r,_,_=run('Which games use VR motion controllers?');checks['VR_controller_type_not_console_or_gamepad']={c['record_id'] for c in r['claims']}=={'controls_motion'}
r,_,_=run('Which games use an AmberMotion VR controller?');checks['VR_controller_model_source_supported']={c['record_id'] for c in r['claims']}=={'controls_motion'}
r,_,_=run('Count games with a PS5 controller');checks['count_deduplicates_game_identity']=r['claims'] and r['needs'][0]['plan']['metadata']['catalog_member_ids']==['game_amber'] and '1 distinct games' in r['answer']
r,_,_=run('Group games with a PS5 controller by platform',op='group_list');checks['controller_platform_groups_filtered_before_grouping']=r['needs'][0]['execution_contract']['collection_proof']['groups']=={'pc':['game_amber']} and 'Amber game' in r['answer'] and 'Ruby game' not in r['answer']
r,_,_=run('Count games with a PS5 controller grouped by zone',op='group_count',facet='zone');checks['controller_zone_counts_have_source_members']=r['needs'][0]['execution_contract']['collection_proof']['groups']=={'zone_pc':['game_amber']} and 'Amber room' in r['answer'] and '1 games' in r['answer']
p,_,_=run('Count games with a PS5 controller grouped by zone',public=True);checks['public_grouped_controller_count_uses_typed_source_join']=p['claims'] and 'Amber room' in p['answer'] and '1 games' in p['answer']
r,e,u=run(q);child=copy.deepcopy(r['needs'][0]);snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0]
slots=r['execution_contract']['request_plan']['tasks'][0]['slots'];checks['device_model_not_compiled_as_platform_or_service']=not any(s['kind'] in {'service','platform'} for s in slots) and any(s['role']=='input_device' for s in slots)
r2,_,_=run('Which games use a PS5 controller on PS5?');slots2=r2['execution_contract']['request_plan']['tasks'][0]['slots'];checks['same_word_outside_device_keeps_platform_raw_span']=any(s['kind']=='platform' and s['source_span']['start']>20 for s in slots2)
checks['native_receipts_independently_verify']=not assess(e.index,task,child,snap,q)['fatal']
prefix_q='For a PS5 controller, which games are available and what is the PC price?'
prefix_u=Understanding([MeaningTask('which games are available','games','C04','list','game_catalog'),MeaningTask('what is the PC price?','service_fee','C06','price_calculate','amount')],True,'controlled_shared_input_device_prefix',{'model_called':False})
with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 prefix=e.answer(prefix_q,'en',at=at,allow_llm=False,understanding=prefix_u)
details.append({'q':prefix_q,'public':False,'result':prefix})
checks['shared_prefix_controller_fact_preserved']={c['record_id'] for c in prefix['claims']}=={'controls_amber'}
checks['shared_prefix_controller_constraint_independently_supported']=any(c['kind']=='input_device' and c['status']=='structurally_supported' for c in prefix['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
prefix_tasks=prefix['execution_contract']['request_plan']['tasks'];checks['shared_prefix_device_role_and_origin']=any(s['role']=='input_device' and s['scope']=='shared' and s['source_span']['text']=='PS5 controller' for s in prefix_tasks[0]['slots'])
checks['shared_prefix_device_does_not_broadcast_console_to_price']=not any(s['source_span']['text']=='PS5' or s['role']=='input_device' for s in prefix_tasks[1]['slots'])
public_prefix,_,_=run(prefix_q,public=True);checks['public_multi_need_prefix_has_source_join']=any(c['record_id']=='controls_amber' for c in public_prefix['claims']) and 'Ruby game' not in public_prefix['answer']
public_different,_,_=run(prefix_q.replace('the PC price','the PS5 price'),public=True);checks['public_other_task_platform_not_applied_to_controller_games']={c['record_id'] for c in public_different['claims']}=={'controls_amber'}
bad=copy.deepcopy(child);bad['plan']['metadata']['controller_catalog_scope']['proofs'][bad['claims'][0]['fact_id']]['device_model']='PS4';checks['forged_model_metadata_rejected']=bool(assess(e.index,task,bad,snap,q)['fatal'])
bad=copy.deepcopy(child);bad['plan']['metadata']['controller_catalog_scope']['request']['model']='ps4';checks['forged_request_model_selector_rejected']=bool(assess(e.index,task,bad,snap,q)['fatal'])
for key in ['input_device_model','input_device','game_id','platform']:
 bad=copy.deepcopy(child);removed=controls['amber']['fields'][key]['evidence_refs'];bad['claims'][0]['evidence_refs']=[x for x in bad['claims'][0]['evidence_refs'] if x not in removed];checks['required_controller_locator_'+key]=bool(assess(e.index,task,bad,snap,q)['fatal'])
bad=copy.deepcopy(child);removed=e.index.records['offer_amber']['fields']['offered']['evidence_refs'];bad['claims'][0]['evidence_refs']=[x for x in bad['claims'][0]['evidence_refs'] if x not in removed];checks['required_offering_locator']=bool(assess(e.index,task,bad,snap,q)['fatal'])
bad=copy.deepcopy(child);bad['claims'][0]['value']='Ruby game';checks['wrong_game_title_rejected']=bool(assess(e.index,task,bad,snap,q)['fatal'])
unsafe=view.snapshot();unsafe['release']['records']['controls_ruby']['fields']['input_device_model']['value']='PS5';r,_,_=run(q,data=unsafe);checks['same_reference_with_changed_source_model_rejected']={c['record_id'] for c in r['claims']}=={'controls_amber'}
edit=copy.deepcopy(controls['ruby']);edit['fields']['input_device_model']={'status':'known','value':'Amber Pad Pro','evidence_refs':[],'note':''};changed=save_owner_record(store,edit,edit['revision'],'controlled-source-test')['record'];r,_,_=run('Which games use an Amber Pad Pro controller?');checks['new_owner_model_name_without_code_alias']={c['record_id'] for c in r['claims']}=={'controls_ruby'}
checks['optional_model_field_does_not_break_old_records']=not schema_errors(controls['unknown'])
expired=copy.deepcopy(controls['amber']);expired['validity']['effective_until']='2026-01-02T00:00:00+07:00';save_owner_record(store,expired,expired['revision'],'controlled-source-test');r,_,_=run(q);checks['expired_controller_relation_withheld']=not r['claims']
actual=snapshot()
class ActualView:
 path=R/'system/data/knowledge/common.sqlite'
 def snapshot(self):return actual
 def still_current(self,s):return s is actual
from app.knowledge.common.domain_flow.source_decisions import guard_result
from app.knowledge.common.domain_flow.scope import reference_time
with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 reader=CommonAnswerer(ActualView());console=reader.answer('เกมบนเครื่อง PS5 มีอะไร',locale='th',at=at,planner=None);controller=reader.answer('เกมที่ใช้จอย PS5 มีอะไร',locale='th',at=at,planner=None)
checks['retained_unknown_controller_has_explicit_customer_notice']=not controller.decision_artifact.get('domain_flow',{}).get('typed_claims') and 'รุ่นจอย' in controller.answer
checks['retained_console_catalog_preserved']=bool(console.decision_artifact.get('domain_flow',{}).get('typed_claims')) and 'Call of Duty' in console.answer
guarded=guard_result(reader,console,actual,Engine.from_snapshot(actual).index,'เกมที่ใช้จอย PS5 มีอะไร',reference_time(at),'th');checks['compatibility_console_receipt_cannot_bypass_controller_scope']=not guarded.decision_artifact.get('domain_flow',{}).get('typed_claims') and 'รุ่นจอย' in guarded.answer
# An exact FAQ question is not the typed compatibility relation. Its literal
# answer must neither override the native join nor bypass final delivery guards.
faq=create('faq','exact_controller_question_wrong_answer',{'question':bi('Which games support a PS5 controller?'),'answer':bi('Ruby console game list, not controller compatibility'),'topic':'games'})
p,_,_=run(q,public=True);checks['exact_FAQ_does_not_override_controller_relations']='Ruby console game list' not in p['answer']
from app.knowledge.common.domain_flow.exact_faq import answer as exact_answer
class FAQView:
 path=store.path
 def snapshot(self):return view.snapshot()
 def still_current(self,s):return True
faq_reader=CommonAnswerer(FAQView());faq_snap=view.snapshot();faq_engine=Engine.from_snapshot(faq_snap);raw_faq=exact_answer(faq_reader,faq_snap,faq_engine.index,q,reference_time(at),'en',_rows=[(faq,'C04')]);blocked=guard_result(faq_reader,raw_faq,faq_snap,faq_engine.index,q,reference_time(at),'en');checks['exact_FAQ_receipts_cannot_bypass_final_scope_guard']='Ruby console game list' not in blocked.answer and 'controller compatibility' in blocked.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'user_data_modified':False,'positive_fixtures_owner_schema_and_source_refs':True,'semantic_accuracy_benchmark':False};(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(O),**report}));assert report['all_passed']
