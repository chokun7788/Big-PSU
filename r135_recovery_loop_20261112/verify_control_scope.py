"""C05 source action/platform/gesture/context and physical-button scope controls."""
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
out=R/('control_scope_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite');store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():
  if k=='input_device':v={'keyboard':'keyboard_mouse','controller':'gamepad'}.get(v,v)
  if k=='preset':v=v['en']
  r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('game','amber_game',{'title':bi('Amber game'),'summary':bi('Controlled game')})
def binding(buttons,gesture,action,context='',notes=''):return {'buttons':buttons,'gesture':gesture,'action':bi(action),'context':bi(context),'notes':bi(notes)}
pc=create('control_set','amber_pc',{'game_id':'amber_game','platform':'PC','input_device':'keyboard','preset':bi('Standard'),'game_version':'1.0','bindings':[binding(['K'],'hold','Heavy attack','Only while grounded'),binding(['Space'],'press','Jump','', 'Do not use this for heavy attack'),binding(['L1','R1'],'simultaneous','Charge pulse','Only with shield equipped')]})
ps=create('control_set','amber_ps5',{'game_id':'amber_game','platform':'PlayStation 5','input_device':'controller','preset':bi('Standard'),'game_version':'1.0','bindings':[binding(['R2'],'press','Heavy attack'),binding(['Cross'],'press','Jump')]})
def run(q,op='control',data=None):
 e=Engine.from_snapshot(data or view.snapshot());u=Understanding([MeaningTask(q,'game_controls','C05',op,'input_bindings')],True,'controlled_control_scope',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u)
 details.append({'question':q,'operation':op,'result':r});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,e,u
r,e,u=run('How do I perform heavy attack in Amber game on PC?');checks['action_lookup_not_bound_from_negative_note']={c['fact_id'] for c in r['claims']}=={'C05:amber_pc:binding_0'};checks['source_hold_gesture_is_customer_visible']='hold' in r['answer'].lower();checks['source_context_is_customer_visible']='Only while grounded' in r['answer']
r,_,_=run('How do I use Charge pulse in Amber game on PC?');checks['owner_added_action_label_works_without_router_edit']={c['fact_id'] for c in r['claims']}=={'C05:amber_pc:binding_2'};checks['simultaneous_chord_and_context_preserved']=all(s in r['answer'] for s in ['L1','R1','Only with shield equipped']) and 'simultaneous' in r['answer'].lower()
r,_,_=run('What does the K button do in Amber game on PC?');checks['button_reverse_lookup_source_action']='Heavy attack' in r['answer'] and {c['fact_id'] for c in r['claims']}=={'C05:amber_pc:binding_0'}
r,_,_=run('List all control bindings for Amber game on PC','list');checks['full_binding_list_is_all_three_entries_not_physical_count']={c['fact_id'] for c in r['claims']}=={'C05:amber_pc:binding_'+str(i) for i in range(3)} and r['needs'][0]['execution_contract']['collection_proof']['verified']
r,_,_=run('List the three buttons for Amber game on PC','list');checks['three_entries_not_proof_of_requested_three_physical_buttons']=r['status']=='partial' and not r['needs'][0]['execution_contract']['collection_proof']['verified']
r,_,_=run('List these three buttons: K, L1 and R1 for Amber game on PC','list');checks['explicit_three_physical_keys_select_two_source_entries']={c['fact_id'] for c in r['claims']}=={'C05:amber_pc:binding_0','C05:amber_pc:binding_2'} and r['needs'][0]['execution_contract']['collection_proof']['verified']
r,e,u=run('List the three buttons for Amber game on PC','list');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);child['plan']['metadata'].pop('requested_binding_count',None);child['plan']['metadata']['complete_set']=True;child['status']='answer';ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['forged_complete_set_cannot_prove_physical_subset']=ledger['terminal_state']!='supported' and not ledger['collection_proof']['verified'];details.append({'challenge':'forged_physical_completeness','ledger':ledger})
r,e,u=run('What does the K button do in Amber game on PC?');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=e.index.byid['C05:amber_ps5:binding_0'];child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['valid_other_platform_receipt_rejected_without_planner_target']=bool(ledger['fatal']);details.append({'challenge':'valid_wrong_platform','claims':child['claims'],'ledger':ledger})
edit=copy.deepcopy(ps);edit['fields']['platform']['value']='PS5';save_owner_record(store,edit,ps['revision'],'controlled-test');r,_,_=run('How do I perform heavy attack in Amber game on PS5?');checks['owner_PS5_platform_alias_is_source_equivalent']=bool(r['claims']) and all(c['record_id']=='amber_ps5' for c in r['claims'])
create('control_set','amber_pc_alternate',{'game_id':'amber_game','platform':'PC','input_device':'keyboard','preset':bi('Alternate'),'game_version':'1.0','bindings':[binding(['P'],'press','Heavy attack')]})
r,_,_=run('List all control bindings for Amber game on PC','list');checks['same_platform_different_presets_require_scope']=not r['claims'] and r['status']=='missing_input'
r,_,_=run('List all control bindings for Amber game on PC using Alternate preset','list');checks['explicit_source_preset_selects_only_its_bindings']=bool(r['claims']) and all(c['record_id']=='amber_pc_alternate' for c in r['claims'])
from app.knowledge.common.answer import CommonAnswerer
with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):a=CommonAnswerer(view).answer('Which buttons trigger Charge pulse in Amber game on PC using Standard preset?',locale='en',at='2026-10-26T12:00:00+07:00',planner=None)
claims=[c for child in a.decision_artifact['execution_contract']['executor_results'] for c in child['claims']];checks['natural_Common_source_action_subset_not_whole_list']={c['fact_id'] for c in claims}=={'C05:amber_pc:binding_2'};details.append({'mode':'common','answer':a.answer,'artifact':a.decision_artifact})
checks['natural_Common_action_not_misclassified_full_layout_list']=any(t['operation']=='control' for t in a.decision_artifact['execution_contract']['request_plan']['tasks'])
for field in ['game_id','platform','preset','game_version']:
 r,e,u=run('What does the K button do in Amber game on PC using Standard preset?');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);refs=pc['fields'][field]['evidence_refs'];child['claims'][0]['evidence_refs']=[ref for ref in child['claims'][0]['evidence_refs'] if ref not in refs];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['missing_scope_locator_rejected_'+field]=bool(ledger['fatal']);details.append({'challenge':'missing_control_scope_'+field,'ledger':ledger})
create('control_set','amber_pc_v2',{'game_id':'amber_game','platform':'PC','input_device':'keyboard','preset':bi('Standard'),'game_version':'2.0','bindings':[binding(['V'],'press','Heavy attack')]})
r,_,_=run('List all control bindings for Amber game on PC using Standard preset','list');checks['same_preset_different_versions_require_scope']=not r['claims'] and r['status']=='missing_input'
r,_,_=run('List all control bindings for Amber game on PC using Standard preset version 2.0','list');checks['explicit_source_version_selects_its_own_layout']=bool(r['claims']) and all(c['record_id']=='amber_pc_v2' for c in r['claims']);checks['source_preset_version_visible_without_replacing_requested_content']='Standard' in r['answer'] and '2.0' in r['answer'] and r['answer'].startswith('**Amber game / PC**')
r,_,_=run('List all control bindings for Amber game on PC using Mystery preset','list');checks['unknown_preset_not_substituted']=not r['claims']
r,_,_=run('List all control bindings for Amber game on PC using Standard preset version 9.0','list');checks['unknown_version_not_substituted']=not r['claims']
(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
