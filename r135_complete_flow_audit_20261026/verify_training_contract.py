"""Artifact-bound admission controls, not semantic review of all289 labels."""
import copy,json,time,os,hashlib
from unittest.mock import patch
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
out=R/('training_contract_'+str(time.time_ns()));out.mkdir();checks={};details=[];store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False)
record=template('game');record['record_id']='admission_control_game';record['localization']['en_status']='agent_translated'
for k,v in {'title':{'th':'เกมอำพัน','en':'Amber game'},'genre':{'th':'แนวทดสอบ','en':'Controlled genre'}}.items():record['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
save_owner_record(store,record,0,'controlled-test');snapshot=DraftSnapshotView(store).snapshot()
def write(name,value):
 p=out/name;p.write_text(json.dumps(value,ensure_ascii=False,indent=2),'utf8');return {'path':str(p.resolve()),'sha256':file_sha(p)}
source_ref=write('SOURCE.json',snapshot);identity=digest(source_identity(snapshot));artifacts=Artifacts(R.parent)
tokenizer_path=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');profile={'base_repository':'typhoon-ai/typhoon2.5-qwen3-4b','base_revision':'ce0a7416fe82d4404b2b4a253ce3ac095ab1252c','precision':'HF_NF4_doublequant_BF16','selector_profile':'base','generic_profile':'base'};runtime=runtime_contract(json.loads(tokenizer_path.read_text('utf8')),chat_template=tokenizer_path.with_name('chat_template.jinja').read_text('utf8'),model_profile=profile)
old=R.parent/'r129_full_plan_completion_20261024/training_v2';historical={}
for split in ['train','validation','test']:
 p=old/(split+'.jsonl')
 for line,text in enumerate(p.read_text('utf8').splitlines(),1):
  row=json.loads(text);historical[row['key']]=(row,{'path':str(p.resolve()),'sha256':file_sha(p),'line':line})
inputs=json.loads((old.parent/'LABELS_REVIEW_INPUT.json').read_text('utf8'))
def make(i,split):
 raw=inputs[i];row,ref=historical[raw['key']];label=copy.deepcopy(row['label'])
 return {'question_key':row['key'],'family':row['review_family'],'original_families':[row['family'],row['review_family']],'split':split,'raw_question':row['question'],'allowed_context':[],'contract_version':WIRE_VERSION,'plan_label':label,'annotation_provenance':{'method':'manual_review_of_saved_question','origin_ref':ref,'runtime_contract_sha256':digest(runtime)},'messages':messages(row['question'])+[{'role':'assistant','content':json.dumps(label,ensure_ascii=False,separators=(',',':'))}],'exposure':'development'}
counter=0
def reviewed(example,*,decision='accepted',source=source_ref,teacher_status='not_applicable',traces=None,alignment=None,teacher_source_hash=None):
 global counter
 counter+=1;reviewer={'id':'controlled_adjudication_fixture','kind':'agent'}
 criteria={c:{'status':'passed','reason':'Controlled fixture for '+c+'; this is not an empirical semantic-accuracy certificate.','raw_quotes':[example['raw_question']],'source_record_ids':[]} for c in CRITERIA}
 evidence={'question_key':example['question_key'],'example_sha256':example_sha(example),'adjudication_status':decision,'reviewer':reviewer,'source_identity_sha256':identity,'criteria':criteria,'unresolved_issues':[]}
 if decision=='quarantined':evidence['quarantine_reason']='Controlled unresolved annotation, excluded from optimization.'
 if teacher_source_hash:evidence['teacher_source_identity_sha256']=teacher_source_hash
 ref=write('REVIEW_EVIDENCE_'+str(counter)+'.json',evidence)
 review={'version':VERSION,'question_key':example['question_key'],'example_sha256':example_sha(example),'adjudication_status':decision,'reviewer':reviewer,'review_method':'individual_source_adjudication','source_version':source,'adjudication_ref':ref,'teacher_status':teacher_status,'teacher_trace_refs':traces if traces is not None else [],'unresolved_issues':[]}
 if decision=='quarantined':review['quarantine_reason']=evidence['quarantine_reason']
 if alignment:review['teacher_source_alignment']=alignment
 return review
def result(name,example,review,expected=False,rt=None):
 r=admit(example,review,artifacts,source_ref,rt or runtime);checks[name]=r['eligible'] is expected;details.append({'case':name,'result':r});return r
train=make(97,'train');dev=make(81,'development');rev=reviewed(train);devrev=reviewed(dev)
result('exact_artifact_bound_individual_review_admitted',train,rev,True)
result('missing_review_never_admitted',train,None)
legacy_review=json.loads((old/'ANNOTATION_REVIEW.jsonl').read_text('utf8').splitlines()[97]);result('historical_generic_review_not_current_adjudication',train,legacy_review)
draft=copy.deepcopy(rev);draft['review_method']='heuristic_draft';result('heuristic_draft_not_promoted_by_accepted_flag',train,draft)
draft=copy.deepcopy(rev);draft.pop('unresolved_issues');result('missing_unresolved_issue_inventory_not_assumed_empty',train,draft)
draft=reviewed(train);data=json.loads(Path(draft['adjudication_ref']['path']).read_text('utf8'));draft['unresolved_issues']=[{'scope':'label','reason':'Wrong action unresolved','handling':'still pending'}];data['unresolved_issues']=draft['unresolved_issues'];draft['adjudication_ref']=write('PENDING_LABEL_ISSUE.json',data);result('accepted_flag_cannot_hide_unresolved_label_issue',train,draft)
changed=copy.deepcopy(train);changed['plan_label']['focus']='multiple';result('review_not_reused_after_label_edit',changed,rev)
changed=copy.deepcopy(train);changed['raw_question']+='?';result('review_not_reused_after_input_edit',changed,rev)
for name,mutate in [('unquoted_target',lambda x:x['plan_label']['tasks'][0].update(target='invented service')),('business_answer_target',lambda x:x['plan_label'].update(answer='300 THB')),('invented_source_record_id',lambda x:x['plan_label']['tasks'][0]['constraints'].append({'slot':'service','quote':'มีอะไรบ้าง','source_record_id':'invented','scope':'local'})),('undeclared_history_flattening',lambda x:x.update(allowed_context=[{'role':'assistant','content':'A made-up prior answer'}])),('original_family_removed',lambda x:x.update(original_families=[])),('old_prompt_same_version',lambda x:x['messages'][0].update(content='Old prompt with same r129-plan-v2 version'))]:
 x=copy.deepcopy(train);mutate(x);result(name,x,reviewed(x))
badrt=copy.deepcopy(runtime);badrt['template_options']['enable_thinking']=True;result('changed_actual_template_options_rejected',train,rev,rt=badrt)
badrt=copy.deepcopy(runtime);badrt['schema_sha256']='0'*64;result('schema_fingerprint_mismatch_rejected',train,rev,rt=badrt)
other=copy.deepcopy(snapshot);other['epoch']+=1;other_ref=write('OTHER_SOURCE.json',other);result('review_of_other_source_snapshot_rejected',train,reviewed(train,source=other_ref))
bad=reviewed(train);evidence=json.loads(Path(bad['adjudication_ref']['path']).read_text('utf8'));evidence['criteria']['needs_and_style']['raw_quotes']=['not present in input'];bad['adjudication_ref']=write('BAD_INPUT_EVIDENCE.json',evidence);result('unbound_review_quote_rejected',train,bad)
bad=reviewed(train);evidence=json.loads(Path(bad['adjudication_ref']['path']).read_text('utf8'));evidence['criteria']['source_version_alignment']['source_record_ids']=['missing_record'];bad['adjudication_ref']=write('BAD_SOURCE_EVIDENCE.json',evidence);result('nonexistent_review_source_record_rejected',train,bad)
rawbytes=Path(rev['adjudication_ref']['path']).read_bytes();Path(rev['adjudication_ref']['path']).write_bytes(rawbytes+b' ');result('adjudication_artifact_hash_change_rejected',train,rev);Path(rev['adjudication_ref']['path']).write_bytes(rawbytes)
teacher=copy.deepcopy(train);teacher['annotation_provenance']['method']='teacher_plan';result('teacher_plan_without_actual_trace_rejected',teacher,reviewed(teacher,teacher_status='recorded'))
receipt={'status':'success','stage':'context_understanding','question_key':teacher['question_key'],'request_id':'controlled-request','response_request_id':'controlled-request','request':{'messages':messages(teacher['raw_question']),'planner_profile':'base'},'response':{'content':json.dumps(teacher['plan_label'],ensure_ascii=False)},'model_identity':{'base_revision':profile['base_revision'],'backend':'controlled-HF-receipt','precision':profile['precision'],'profile':'base','adapter_sha256':None}}
receipt_ref=write('CONTROLLED_TEACHER_RECEIPT.json',receipt)
trace_ref=write('TEACHER_TRACE.json',{'question_key':teacher['question_key'],'plan':teacher['plan_label'],'source_version':source_ref,'inference_receipt_ref':receipt_ref});result('same_source_teacher_trace_and_current_review_admitted',teacher,reviewed(teacher,teacher_status='recorded',traces=[trace_ref],alignment='same_source'),True)
bad_receipt=copy.deepcopy(receipt);bad_receipt['response_request_id']='another-request';bad_trace=write('WRONG_REQUEST_TRACE.json',{'question_key':teacher['question_key'],'plan':teacher['plan_label'],'source_version':source_ref,'inference_receipt_ref':write('WRONG_REQUEST_RECEIPT.json',bad_receipt)});result('successful_other_request_receipt_not_teacher_proof',teacher,reviewed(teacher,teacher_status='recorded',traces=[bad_trace],alignment='same_source'))
bad_receipt=copy.deepcopy(receipt);bad_receipt['model_identity']={'alias':'psu-r129:latest'};bad_trace=write('ALIAS_ONLY_TRACE.json',{'question_key':teacher['question_key'],'plan':teacher['plan_label'],'source_version':source_ref,'inference_receipt_ref':write('ALIAS_ONLY_RECEIPT.json',bad_receipt)});result('teacher_alias_not_actual_model_provenance',teacher,reviewed(teacher,teacher_status='recorded',traces=[bad_trace],alignment='same_source'))
bad_receipt=copy.deepcopy(receipt);bad_receipt['stage']='selector';bad_trace=write('WRONG_STAGE_TRACE.json',{'question_key':teacher['question_key'],'plan':teacher['plan_label'],'source_version':source_ref,'inference_receipt_ref':write('WRONG_STAGE_RECEIPT.json',bad_receipt)});result('selector_receipt_not_context_teacher_proof',teacher,reviewed(teacher,teacher_status='recorded',traces=[bad_trace],alignment='same_source'))
trace_ref=write('CHANGED_TEACHER_TRACE.json',{'question_key':teacher['question_key'],'plan':teacher['plan_label'],'source_version':other_ref,'inference_receipt_ref':receipt_ref});result('changed_teacher_source_without_adjudication_rejected',teacher,reviewed(teacher,teacher_status='recorded',traces=[trace_ref],alignment='same_source'))
result('explicit_source_change_adjudication_admitted',teacher,reviewed(teacher,decision='corrected',teacher_status='recorded',traces=[trace_ref],alignment='adjudicated_source_change',teacher_source_hash=digest(source_identity(other))),True)
result('manual_review_cannot_invent_teacher_trace',train,reviewed(train,traces=[trace_ref]))
keys=[train['question_key'],dev['question_key']];exposed=set(historical);batch=audit_dataset([train,dev],[rev,devrev],artifacts,source_ref,runtime,expected_keys=keys,known_exposed=exposed);checks['two_individually_reviewed_distinct_families_ready']=batch['ready_for_optimization']
import app.knowledge.common.domain_flow.training_contract as tc
actual_audit=tc._audit_dataset;path=Path(rev['adjudication_ref']['path']);before=path.read_bytes()
def change_during_admission(*args,**kwargs):
 value=actual_audit(*args,**kwargs);path.write_bytes(before+b' ');return value
with patch.object(tc,'_audit_dataset',side_effect=change_during_admission):changed_batch=tc.audit_dataset([train,dev],[rev,devrev],artifacts,source_ref,runtime,expected_keys=keys)
checks['artifact_change_during_batch_blocks_optimization']=not changed_batch['ready_for_optimization'] and 'artifact_changed_during_admission' in changed_batch['dataset_issues'];path.write_bytes(before)
missing=audit_dataset([train,dev],[rev],artifacts,source_ref,runtime,expected_keys=keys);checks['one_unreviewed_row_blocks_declared_inventory']=not missing['ready_for_optimization'] and not missing['inventory_individually_adjudicated']
leak=copy.deepcopy(dev);leak['family']=train['family'];leakrev=reviewed(leak);r=audit_dataset([train,leak],[rev,leakrev],artifacts,source_ref,runtime,expected_keys=keys);checks['review_family_cannot_cross_splits']=not r['ready_for_optimization'] and bool(r['family_overlaps'])
leak=copy.deepcopy(dev);leak['original_families'].append(train['original_families'][0]);r=audit_dataset([train,leak],[rev,reviewed(leak)],artifacts,source_ref,runtime,expected_keys=keys);checks['original_family_cannot_cross_splits']=not r['ready_for_optimization'] and bool(r['family_overlaps'])
same=copy.deepcopy(train);same.update(question_key=dev['question_key'],family='different_declared_family',original_families=['different_origin_family'],split='development');same['annotation_provenance']['origin_ref']=write('DUPLICATE_RAW_ORIGIN.json',{'key':same['question_key'],'question':same['raw_question'],'family':'different_origin_family'});r=audit_dataset([train,same],[rev,reviewed(same)],artifacts,source_ref,runtime,expected_keys=keys);checks['identical_normalized_core_cannot_hide_behind_new_key_and_family']=not r['ready_for_optimization'] and any(k.startswith('normalized_raw:') for k in r['family_overlaps'])
exposed_row=copy.deepcopy(dev);exposed_row.update(split='holdout',exposure='unseen');r=audit_dataset([train,exposed_row],[rev,reviewed(exposed_row)],artifacts,source_ref,runtime,expected_keys=keys,known_exposed=exposed);checks['known_retained_key_cannot_be_relabelled_fresh_holdout']=not r['ready_for_optimization']
r=audit_dataset([train,train],[rev],artifacts,source_ref,runtime,expected_keys=keys);checks['duplicate_keys_and_missing_inventory_rejected']=not r['ready_for_optimization'] and 'duplicate_question_keys' in r['dataset_issues']
q=reviewed(dev,decision='quarantined');r=admit(dev,q,artifacts,source_ref,runtime);checks['explicit_quarantine_is_reviewed_but_not_optimized']=r['inventory_adjudicated'] and not r['eligible']
try:require_ready({'version':VERSION,'ready_for_optimization':True});checks['bare_ready_flag_not_optimization_authority']=False
except ValueError:checks['bare_ready_flag_not_optimization_authority']=True
ready=prepare_dataset(out/'ready_bundle',[train,dev],[rev,devrev],artifacts,source_ref,runtime,expected_keys=keys,known_exposed=exposed);loaded=load_admitted_dataset(out/'ready_bundle',artifacts,runtime);checks['consumer_revalidates_actual_approved_frozen_rows']=len(loaded['train'])==len(loaded['development'])==1
Path(out/'ready_bundle/train.jsonl').write_text('{}\n','utf8')
try:load_admitted_dataset(out/'ready_bundle',artifacts,runtime);checks['consumer_rejects_changed_optimization_file']=False
except ValueError:checks['consumer_rejects_changed_optimization_file']=True
blocked=prepare_dataset(out/'blocked_bundle',[train,dev],[rev],artifacts,source_ref,runtime,expected_keys=keys);checks['blocked_bundle_has_quarantine_and_no_ready_marker']=not blocked['ready_for_optimization'] and (out/'blocked_bundle/QUARANTINE.jsonl').exists() and not (out/'blocked_bundle/READY_FOR_OPTIMIZATION.json').exists()
try:prepare_dataset(out/'blocked_bundle',[train,dev],[rev],artifacts,source_ref,runtime,expected_keys=keys);checks['existing_bundle_never_overwritten']=False
except FileExistsError:checks['existing_bundle_never_overwritten']=True
checks['gate_never_claims_semantic_truth']=all(d['result'].get('semantic_truth_verified_by_gate') is False for d in details)
report={'all_passed':all(checks.values()),'checks':checks,'actual_tokenizer_config_sha256':file_sha(tokenizer_path),'actual_model_inferences':0,'optimizer_started':False,'user_data_modified':False,'controlled_review_fixtures_not_semantic_review_of_all289':True,'unattested_history_training_explicitly_quarantined':True,'native_history_positive_controls_separate':'verify_training_history_input.py'};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
