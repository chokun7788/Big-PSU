"""Native history reconstruction controls, not production semantic acceptance."""
import copy,json,os,time
from pathlib import Path
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
from app.knowledge.common.domain_flow.training_input import VERSION as INPUT_VERSION,reconstruct
from app.knowledge.common.flow_context import Context,CURRENT
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.dialogue_task import resolve
from app.session.history_boundary import history_from_record
with patch.dict(os.environ,{'PSU_CONVERSATION_PERSISTENCE':'0'}):
 from app.session.conversation_store import ConversationStore

O=R/('training_history_input_'+str(time.time_ns()));O.mkdir();checks={};details=[]
W=R/'training_review_workbench_1793037663397671000'
def read(p):return json.loads(p.read_text('utf8'))
def write(name,data):
 p=O/name;p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf8');return {'path':str(p.resolve()),'sha256':file_sha(p)}
artifacts=Artifacts(R.parent);artifacts._cache={};snapshot=read(W/'SOURCE_SNAPSHOT.json');source_ref=read(W/'SOURCE_REF.json');source_sha=digest(source_identity(snapshot));tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'))
session='isolated-history-control';at='2026-10-27T04:30:00+07:00';ctx=Context(request_id='controlled-prior-request');ctx.input={'raw_question':'What is TEKKEN 8?'};ctx.pin_reference_time(at);ctx.bind_snapshot(snapshot);token=CURRENT.set(ctx)
try:prior=resolve(Engine.from_snapshot(snapshot).index,ctx.input['raw_question'],[],snapshot['active'],ctx.pin_reference_time())
finally:CURRENT.reset(token)
store=ConversationStore(persistence_path=None);turn=store.begin(session,'prior-turn','What is TEKKEN 8?',locale='en');response={'ok':True,'request_id':'controlled-prior-response','answer':'Controlled response fixture, not business gold.','common_read_state':{'schema_version':1,'dialogue_task':prior['task']}}
assert store.complete(session,'prior-turn',turn['revision'],response);store.delivery(session,'prior-turn','server_written');record=copy.deepcopy(store._sessions[session]);record_ref=write('NATIVE_RECORD.json',record)
raw='What about its buttons?';key='controlled-history-key';reconstruction=reconstruct(raw,'controlled-current-request',session,at,snapshot,record);execution=reconstruction['execution_question'];checks['real_native_dialogue_recomputed']=execution.startswith('TEKKEN 8 ') and reconstruction['resolution']['used_context'] and reconstruction['input_derivation_validation']['verified']
checks['same_history_boundary_as_store']=history_from_record(record,session)==store.history(session)
before=copy.deepcopy(record);history_from_record(record,session);checks['native_record_not_mutated']=record==before
saved={'version':INPUT_VERSION,'question_key':key,'raw_question':raw,'request_id':'controlled-current-request','session_id':session,'reference_time':at,'source_ref':source_ref,'session_record_ref':record_ref,'reconstruction':reconstruction,'planner_messages':messages(execution)};saved_ref=write('RUNTIME_INPUT.json',saved)
origin_ref=write('ORIGIN.json',{'key':key,'question':raw,'family':'controlled-history-family','runtime_input_ref':saved_ref})
label={'version':WIRE_VERSION,'focus':'game_controls','context_quotes':['TEKKEN 8'],'tasks':[{'id':'t1','quote':execution,'domain':'game_controls','operation':'list','facet':'input_bindings','target':'TEKKEN 8','constraints':[],'ambiguous':False}],'shared_bindings':[]}
example={'question_key':key,'family':'controlled-history-family','original_families':['controlled-history-family'],'split':'train','raw_question':raw,'allowed_context':[{'kind':INPUT_VERSION,'runtime_input_ref':saved_ref}],'contract_version':WIRE_VERSION,'plan_label':label,'annotation_provenance':{'method':'manual_review_of_saved_question','origin_ref':origin_ref,'runtime_contract_sha256':digest(runtime)},'messages':messages(execution)+[{'role':'assistant','content':json.dumps(label,ensure_ascii=False,separators=(',',':'))}],'exposure':'development'}
counter=0
def reviewed(x):
 global counter
 counter+=1;who={'id':'controlled-history-review-fixture','kind':'agent'};evidence={'question_key':key,'example_sha256':example_sha(x),'adjudication_status':'accepted','reviewer':who,'source_identity_sha256':source_sha,'criteria':{name:{'status':'passed','reason':'Controlled native-history admission fixture; no actual corpus adjudication claimed.','raw_quotes':[raw],'source_record_ids':[]} for name in CRITERIA},'unresolved_issues':[]}
 return {'version':VERSION,'question_key':key,'example_sha256':example_sha(x),'adjudication_status':'accepted','reviewer':who,'review_method':'individual_source_adjudication','source_version':source_ref,'adjudication_ref':write('REVIEW_'+str(counter)+'.json',evidence),'teacher_status':'not_applicable','teacher_trace_refs':[],'unresolved_issues':[]}
def check(name,x,expected=False):
 result=admit(x,reviewed(x),artifacts,source_ref,runtime);checks[name]=result['eligible'] is expected;details.append({'name':name,'result':result})
check('artifact_bound_native_history_input_admitted',example,True)
def with_saved(data,name):
 x=copy.deepcopy(example);ref=write(name+'.json',data);x['allowed_context'][0]['runtime_input_ref']=ref;x['annotation_provenance']['origin_ref']=write(name+'_ORIGIN.json',{'key':key,'question':raw,'family':'controlled-history-family','runtime_input_ref':ref});return x
x=copy.deepcopy(example);x['allowed_context'][0]['runtime_input_ref']['sha256']='0'*64;check('missing_hashed_history_artifact_rejected',x)
x=copy.deepcopy(example);x['allowed_context']=[{'role':'assistant','delivery_status':'server_written','common_read_state':response['common_read_state']}];check('client_delivery_flag_not_history_evidence',x)
x=copy.deepcopy(example);x['annotation_provenance']['origin_ref']=write('NO_CONTEXT_ORIGIN.json',{'key':key,'question':raw,'family':'controlled-history-family'});check('history_not_added_after_saved_origin',x)
for name,mutate in [
 ('forged_derived_text_rejected',lambda d:d['reconstruction'].update(execution_question='VR free play forever')),
 ('bare_verified_receipt_rejected',lambda d:d['reconstruction'].update(input_derivation_validation={'verified':True})),
 ('another_current_question_rejected',lambda d:d.update(raw_question='A different request')),
 ('wrong_current_request_rejected',lambda d:d.update(request_id='another-current-request')),
 ('different_clock_rejected',lambda d:d.update(reference_time='2026-11-03T12:00:00+07:00')),
 ('naive_clock_rejected',lambda d:d.update(reference_time='2026-10-27T04:30:00')),
 ('old_implementation_derivation_rejected',lambda d:d['reconstruction'].update(implementation_sha256='0'*64)),
 ('other_session_record_rejected',lambda d:d.update(session_id='another-session')),
 ('old_prompt_for_history_rejected',lambda d:d['planner_messages'][0].update(content='Old different prompt')),
]:
 d=copy.deepcopy(saved);mutate(d);check(name,with_saved(d,name))
d=copy.deepcopy(saved);other=copy.deepcopy(snapshot);other['epoch']+=1;d['source_ref']=write('OTHER_SOURCE.json',other);check('source_change_requires_new_alignment',with_saved(d,'OTHER_SOURCE_INPUT'))
for name,mutate in [
 ('changed_recorded_common_state_rejected',lambda d:d['history'][-1]['common_read_state']['dialogue_task'].update(game_ids=[])),
 ('wrong_saved_user_question_rejected',lambda d:d['history'][0].update(text='What is VR?')),
 ('user_history_without_saved_turn_rejected',lambda d:d['history'][0].update(turn_id='invented-prior-turn')),
 ('wrong_response_delivery_rejected',lambda d:d['turns']['prior-turn'].update(delivery='uncertain')),
 ('unsuccessful_saved_response_rejected',lambda d:d['turns']['prior-turn']['response'].update(ok=False)),
]:
 changed=copy.deepcopy(record);mutate(changed);d=copy.deepcopy(saved);d['session_record_ref']=write(name+'_RECORD.json',changed);check(name,with_saved(d,name))
x=copy.deepcopy(example);x['messages']=messages(raw)+x['messages'][-1:];check('raw_only_prompt_cannot_silently_flatten_inherited_scope',x)
x=copy.deepcopy(example);x['plan_label']['tasks'][0]['target']='Invented game';x['messages'][-1]['content']=json.dumps(x['plan_label'],ensure_ascii=False,separators=(',',':'));check('unquoted_inherited_entity_cannot_be_invented',x)
fallback=history_from_record({'history':[],'turns':{}},session,store.history(session));checks['client_fallback_always_uncertain_no_server_carrier']=all(t['delivery_status']=='uncertain' and '_server_history_ref' not in t for t in fallback)
checks['assistant_prose_business_answer_not_in_prompt']='Controlled response fixture' not in json.dumps(example['messages'])
checks['model_inference_not_needed']=reconstruction['semantic_correctness_claimed'] is False
artifacts.verify_pinned_files();checks['all_artifacts_still_match_pinned_bytes']=True
write('DETAILS.json',details);report={'all_passed':all(checks.values()),'checks':checks,'new_corpus_adjudications':0,'controlled_fixture_not_production_gold':True,'native_data_modified':False,'actual_model_inferences':0,'optimizer_started':False,'supported_context_stage':'native dialogue_task resolution only; other stages remain explicitly unsupported'};write('RESULT.json',report);print(json.dumps({'output':str(O),**report}));assert report['all_passed']
