"""Exercise the actual admission consumer; no framework/model/GPU imports."""
import builtins,contextlib,copy,io,json,runpy,subprocess,sys,time
from pathlib import Path
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import Artifacts,prepare_dataset,digest,file_sha,source_identity
from app.knowledge.common.domain_flow import training_optimizer as opt

out=R/('training_optimizer_'+str(time.time_ns()));out.mkdir();checks={};details=[]
def write(name,value):
 p=out/name;p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8');return {'path':str(p.resolve()),'sha256':file_sha(p)}
def reject(name,fn):
 try:fn();checks[name]=False
 except (ValueError,KeyError,FileNotFoundError,FileExistsError) as exc:checks[name]=True;details.append({'case':name,'blocked':str(exc)})

# Reuse actual artifact-bound source/adjudication fixtures, not a mocked gate.
captured=io.StringIO()
with contextlib.redirect_stdout(captured):fixture=runpy.run_path(str(R/'verify_training_contract.py'))
(out/'UPSTREAM_GATE_OUTPUT.txt').write_text(captured.getvalue(),'utf8')
checks['upstream_admission_controls_pass']=all(fixture['checks'].values())
runtime=fixture['runtime'];train=fixture['train'];dev=fixture['dev'];source_ref=fixture['source_ref'];keys=fixture['keys'];exposed=fixture['exposed'];dataset=out/'ready'
prepare_dataset(dataset,[train,dev],[fixture['rev'],fixture['devrev']],Artifacts(R.parent),source_ref,runtime,expected_keys=keys,known_exposed=exposed)
base=out/'synthetic_base';base.mkdir();source_tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model')
for n in ['tokenizer_config.json','chat_template.jinja']:(base/n).write_bytes((source_tokenizer/n).read_bytes())
(base/'config.json').write_text('{"synthetic_control":true}','utf8');(base/'model.safetensors').write_bytes(b'SYNTHETIC-CONTROL-NEVER-LOADED')
manifest={'model_profile':runtime['model_profile'],'files':opt._files(base)};manifest_ref=write('BASE_MANIFEST.json',manifest)
family_ref=write('FAMILIES.json',{'version':'r135-semantic-family-review-v1','inventory_sha256':digest(sorted(keys)),'groups':[{'family':x['family'],'question_keys':[x['question_key']],'reason':'Controlled distinct source-language fixture; not corpus family review.'} for x in [train,dev]]})
coverage_ref=write('COVERAGE.json',{'version':'r135-strata-review-v1','inventory_sha256':digest(sorted(keys)),'strata':{n:{'question_keys':[],'status':'insufficient','reason':'Only two synthetic guard controls; no real stratum coverage measured.','interpretation_limit':'Cannot infer semantic coverage or training readiness of the real corpus.'} for n in opt.STRATA}})
weights=out/'synthetic_r121.safetensors';weights.write_bytes(b'SYNTHETIC-CONTROL-NOT-ACTUAL-R121')
eval_refs={'question_inventory_ref':write('EVAL_KEYS.json',{'question_keys':sorted(keys)}),'locale_ref':write('LOCALES.json',{'requested_locales':{k:'auto' for k in keys}}),'reference_clock_ref':write('CLOCK.json',{'reference_clock_iso':'2026-10-27T10:00:00+07:00'}),'live_fixture_ref':write('LIVE.json',{'mode':'frozen_fixture','observations':[]}),'budgets_ref':write('BUDGETS.json',{'context_generation_cap':850,'stage_budgets':{'context_understanding':45}}),'retained_adapter_ref':write('R121.json',{'stage':'context_understanding','base_revision':opt.CONFIG['base_revision'],'precision':opt.CONFIG['precision'],'weights_ref':{'path':str(weights.resolve()),'sha256':file_sha(weights)}}),'exposure_review_ref':write('EXPOSURE.json',{'question_exposures':{k:'retained_development' for k in keys}})}
source_sha=digest(source_identity(fixture['snapshot']))
evaluation={'version':'r135-three-arm-evaluation-v2','arms':['base','r121','candidate'],'runtime_contract_sha256':digest(runtime),'source_identity_sha256':source_sha,'semantic_unknown_handling':'review_required','structural_is_semantic':False,'metrics':{n:{'definitions':'Synthetic gate control only; no actual metric measured.','promotion_criteria':'No promotion from synthetic results.','review_method':'Explicit source review required for real questions.','components':{c:{'definition':'Synthetic guard control only','denominator':'Synthetic fixture only','review_method':'No production inference'} for c in opt.REQUIRED_METRIC_COMPONENTS[n]}} for n in opt.METRICS},**eval_refs}
eval_ref=write('EVALUATION.json',evaluation)
protocol={'version':'r135-optimization-protocol-v1','dataset_freeze_sha256':file_sha(dataset/'DATASET_FREEZE.json'),'runtime_contract_sha256':digest(runtime),'base_manifest_sha256':manifest_ref['sha256'],'optimization_config_sha256':digest(opt.CONFIG),'source_identity_sha256':source_sha,'family_review_ref':family_ref,'coverage_review_ref':coverage_ref,'evaluation_plan_ref':eval_ref}
protocol_ref=write('PROTOCOL.json',protocol)
def admit(m=manifest_ref,p=protocol_ref,rt=runtime):return opt.admit_run(dataset,Artifacts(R.parent),rt,base,m,p)
before={str(p):file_sha(p) for p in dataset.iterdir() if p.is_file()}
result=opt.run_optimizer(dataset,Artifacts(R.parent),runtime,base,manifest_ref,protocol_ref,None,check_only=True)
checks['fully_pinned_control_check_only_admitted_without_optimizer']=result['admitted'] and not result['optimizer_started'] and result['split_counts']['train']==result['split_counts']['development']==1
checks['check_only_does_not_mutate_bundle']=all(file_sha(p)==sha for p,sha in before.items())
checks['check_only_imports_no_model_frameworks']=not any(n in sys.modules for n in ['torch','transformers','peft','bitsandbytes'])
reject('output_cannot_overlap_base',lambda:opt.run_optimizer(dataset,Artifacts(R.parent),runtime,base,manifest_ref,protocol_ref,base/'nested'))
reject('output_cannot_overlap_admitted_dataset',lambda:opt.run_optimizer(dataset,Artifacts(R.parent),runtime,base,manifest_ref,protocol_ref,dataset/'nested'))
existing=out/'existing_run';existing.mkdir();(existing/'KEEP.txt').write_text('preserve','utf8')
reject('existing_run_never_overwritten',lambda:opt.run_optimizer(dataset,Artifacts(R.parent),runtime,base,manifest_ref,protocol_ref,existing))
checks['existing_run_bytes_preserved']=(existing/'KEEP.txt').read_text('utf8')=='preserve'
telemetry=out/'telemetry';telemetry.mkdir()
with patch.object(opt.os,'replace',side_effect=PermissionError('controlled reader lock')),patch.object(opt.time,'sleep'):
 opt._progress(telemetry,{'phase':'controlled','optimizer_started':False})
checks['reader_locked_progress_cannot_abort_work_and_journal_preserved']=json.loads((telemetry/'STATUS_JOURNAL.jsonl').read_text('utf8'))['phase']=='controlled' and len(list(telemetry.glob('progress_*.json')))==1
code_fixture=out/'code_fixture';code_fixture.mkdir();(code_fixture/'a.py').write_text('x=1\n','utf8');frozen=opt._run_files(dataset,code_fixture);(code_fixture/'b.py').write_text('y=2\n','utf8')
checks['run_freeze_detects_new_code_files']=opt._run_files(dataset,code_fixture)!=frozen
bad=copy.deepcopy(manifest);bad['model_profile']['base_revision']='wrong';reject('base_revision_mismatch',lambda:admit(m=write('WRONG_BASE.json',bad)))
bad=copy.deepcopy(manifest);bad['files'].pop('config.json');reject('incomplete_base_manifest',lambda:admit(m=write('INCOMPLETE_BASE.json',bad)))
bad=copy.deepcopy(manifest);bad['files']['../outside']='0'*64;reject('base_manifest_path_escape',lambda:admit(m=write('ESCAPE_BASE.json',bad)))
extra=base/'UNDECLARED.txt';extra.write_text('unlisted','utf8');reject('base_inventory_addition_detected',admit);extra.unlink()
raw=(base/'model.safetensors').read_bytes();(base/'model.safetensors').write_bytes(raw+b'changed');reject('base_weight_bytes_changed',admit);(base/'model.safetensors').write_bytes(raw)
for field in ['dataset_freeze_sha256','runtime_contract_sha256','base_manifest_sha256','optimization_config_sha256','source_identity_sha256']:
 bad=copy.deepcopy(protocol);bad[field]='0'*64;ref=write('CHANGED_'+field+'.json',bad);reject('changed_'+field,lambda ref=ref:admit(p=ref))
bad=copy.deepcopy(protocol);bad.pop('family_review_ref');reject('missing_actual_family_review',lambda:admit(p=write('NO_FAMILY.json',bad)))
def protocol_variant(name,field,value):
 p=copy.deepcopy(protocol);p[field]=write(name+'.json',value);return write(name+'_PROTOCOL.json',p)
bad=json.loads(Path(family_ref['path']).read_text('utf8'));bad['groups']=bad['groups'][:1];reject('family_inventory_missing',lambda:admit(p=protocol_variant('MISSING_FAMILY','family_review_ref',bad)))
bad=json.loads(Path(coverage_ref['path']).read_text('utf8'));bad['strata'].pop(opt.STRATA[-1]);reject('one_of_eight_strata_missing',lambda:admit(p=protocol_variant('MISSING_STRATUM','coverage_review_ref',bad)))
bad=json.loads(Path(coverage_ref['path']).read_text('utf8'));bad['strata'][opt.STRATA[0]]['status']='assessed';reject('empty_stratum_cannot_claim_coverage',lambda:admit(p=protocol_variant('EMPTY_ASSESSED','coverage_review_ref',bad)))
bad=json.loads(Path(coverage_ref['path']).read_text('utf8'));bad['strata'][opt.STRATA[0]]['interpretation_limit']='';reject('sparse_stratum_without_limit',lambda:admit(p=protocol_variant('NO_LIMIT','coverage_review_ref',bad)))
bad=copy.deepcopy(evaluation);bad['structural_is_semantic']=True;reject('schema_not_semantic_evaluation',lambda:admit(p=protocol_variant('SCHEMA_SEMANTIC','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['metrics']['planner']['promotion_criteria']='';reject('metrics_without_frozen_criteria',lambda:admit(p=protocol_variant('NO_CRITERIA','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['metrics']['end_to_end_answer']['components'].pop('complete_supported_answer_answerable_unanswerable');reject('missing_answerable_denominators',lambda:admit(p=protocol_variant('NO_ANSWERABLE_METRIC','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['metrics']['planner']['components']['slot_role_scope']['denominator']='';reject('metric_component_missing_denominator',lambda:admit(p=protocol_variant('NO_METRIC_DENOMINATOR','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['version']='r135-three-arm-evaluation-v1';reject('legacy_generic_metrics_not_sufficient',lambda:admit(p=protocol_variant('LEGACY_METRIC_PLAN','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['semantic_unknown_handling']='keyword_correct';reject('semantic_unknown_not_forced_to_keyword_correct',lambda:admit(p=protocol_variant('KEYWORD_JUDGE','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['locale_ref']=write('MISSING_LOCALE.json',{'requested_locales':{train['question_key']:'th'}});reject('evaluation_locale_inventory_missing',lambda:admit(p=protocol_variant('BAD_LOCALES','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['reference_clock_ref']=write('NAIVE_CLOCK.json',{'reference_clock_iso':'2026-10-27T10:00:00'});reject('naive_evaluation_clock',lambda:admit(p=protocol_variant('BAD_CLOCK','evaluation_plan_ref',bad)))
bad=copy.deepcopy(evaluation);bad['exposure_review_ref']=write('FRESH_CLAIM.json',{'question_exposures':{k:'unseen' for k in keys}});reject('retained_exposed_keys_cannot_be_fresh',lambda:admit(p=protocol_variant('FRESH','evaluation_plan_ref',bad)))
original=weights.read_bytes();weights.write_bytes(original+b'changed');reject('retained_adapter_weight_tamper',admit);weights.write_bytes(original)

class TinyTokenizer:
 def apply_chat_template(self,ms,**kw):
  assert kw['tokenize'] is False and kw['enable_thinking'] is False
  return ''.join('<'+m['role']+'>'+m['content']+'</'+m['role']+'>' for m in ms)+('<assistant>' if kw['add_generation_prompt'] else '')
 def __call__(self,text,**kw):assert kw=={'add_special_tokens':False};return {'input_ids':list(text.encode())}
sample={'question_key':'controlled-packing','messages':[{'role':'user','content':'Q'},{'role':'assistant','content':'{}'}]}
packed=opt.pack_examples(TinyTokenizer(),[sample],runtime)[0];checks['exact_template_completion_prefix_and_labels_preserved']=packed['input_ids'][packed['prompt_len']:]==list(b'{}</assistant>')
long=copy.deepcopy(sample);long['messages'][-1]['content']='x'*851;reject('generation_cap_never_silently_truncated',lambda:opt.pack_examples(TinyTokenizer(),[long],runtime))
long=copy.deepcopy(sample);long['messages'][0]['content']='x'*2048;reject('sequence_cap_never_silently_truncated',lambda:opt.pack_examples(TinyTokenizer(),[long],runtime))
reject('empty_development_cannot_select_checkpoint',lambda:opt.pack_examples(TinyTokenizer(),[],runtime))
class BadTemplate(TinyTokenizer):
 def apply_chat_template(self,ms,**kw):return 'different' if kw['add_generation_prompt'] else 'unrelated'
reject('template_prefix_mismatch',lambda:opt.pack_examples(BadTemplate(),[sample],runtime))
class BadTokenPrefix(TinyTokenizer):
 def __call__(self,text,**kw):return {'input_ids':list(text.encode())+[0]}
reject('bpe_prefix_mismatch',lambda:opt.pack_examples(BadTokenPrefix(),[sample],runtime))

actual=sorted((R/'training_review_workbench_1793037663397671000').glob('current_admission_*'))[-1]
rt=json.loads((actual/'RUNTIME_CONTRACT.json').read_text('utf8'))
called=[]
original_import=builtins.__import__
def import_guard(name,*args,**kw):
 if name.split('.')[0] in {'torch','transformers','peft','bitsandbytes'}:called.append(name);raise AssertionError('EXPENSIVE_IMPORT_BEFORE_ADMISSION')
 return original_import(name,*args,**kw)
with patch('builtins.__import__',import_guard):
 reject('actual_corpus_invalid_refs_blocked_before_model_assets_or_frameworks',lambda:opt.run_optimizer(actual/'bundle',Artifacts(R.parent),rt,object(),{}, {},out/'must_not_exist'))
checks['actual_corpus_invalid_refs_did_not_create_run_or_import_frameworks']=not (out/'must_not_exist').exists() and not called
finalization=json.loads((R/'ROUND013_DATASET_GATE_FINALIZATION.json').read_text('utf8'))
cohort=next(c for c in finalization['cohorts'] if (R/c['path']).resolve()==actual.resolve())
checks['actual_dataset_gate_ready_is_not_optimizer_authorization']=cohort['dataset_ready'] is True and (actual/'bundle/READY_FOR_OPTIMIZATION.json').is_file() and finalization['base_protocol_evaluation_readiness_proven'] is False and not (out/'must_not_exist').exists()
empty_ref=write('UNUSED_REF.json',{})
command=[sys.executable,str(R/'system/tools/train_reviewed_planner.py'),'--dataset',str(actual/'bundle'),'--runtime-contract',str(actual/'RUNTIME_CONTRACT.json'),'--base',str(out/'nonexistent_base'),'--base-manifest-ref',empty_ref['path'],'--protocol-ref',empty_ref['path'],'--artifact-root',str(R.parent),'--output',str(out/'cli_must_not_exist')]
process=subprocess.run(command,capture_output=True,text=True,encoding='utf8');write('ACTUAL_CLI_PROCESS.json',{'command':command,'exit_code':process.returncode,'stdout':process.stdout,'stderr':process.stderr})
cli=json.loads(process.stdout);checks['actual_cli_blocks_invalid_refs_before_framework_import']=process.returncode==2 and cli['admitted'] is False and cli['model_frameworks_loaded']==[] and not (out/'cli_must_not_exist').exists()
rr=write('CLI_RUNTIME.json',runtime);mr=write('CLI_MANIFEST_REF.json',manifest_ref);pr=write('CLI_PROTOCOL_REF.json',protocol_ref)
command=[sys.executable,str(R/'system/tools/train_reviewed_planner.py'),'--dataset',str(dataset),'--runtime-contract',rr['path'],'--base',str(base),'--base-manifest-ref',mr['path'],'--protocol-ref',pr['path'],'--artifact-root',str(R.parent),'--output',str(base/'forbidden_nested')]
process=subprocess.run(command,capture_output=True,text=True,encoding='utf8');write('POST_ADMISSION_CLI_PROCESS.json',{'command':command,'exit_code':process.returncode,'stdout':process.stdout,'stderr':process.stderr});cli=json.loads(process.stdout)
checks['cli_distinguishes_post_admission_failure_from_rejected_data']=process.returncode==1 and cli['admitted'] is True and cli['phase']=='failed_after_admission' and cli['model_frameworks_loaded']==[] and not (base/'forbidden_nested').exists()
checks['all_pinned_synthetic_positive_rechecks']=admit()['source_identity_sha256']==source_sha
report={'all_passed':all(checks.values()),'checks':checks,'details':details,'actual_current_admission':str(actual.relative_to(R)),'source_control_scope':'Synthetic source-schema/adjudication/model-byte fixtures exercise gate behavior only. Not semantic corpus acceptance or actual optimizer/GPU proof.','actual_model_inferences':0,'optimizer_started':False,'production_installed':False,'gpu_optimization_tested':False}
_ref=write('RESULT.json',report);print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed'],[k for k,v in checks.items() if not v]
