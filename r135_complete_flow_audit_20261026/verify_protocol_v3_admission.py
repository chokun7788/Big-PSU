"""Real artifact-bound version migration; no invented semantic reviews."""
import copy,json,subprocess,sys,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
from app.knowledge.common.domain_flow import graph_protocol_v3 as v3
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('protocol_v3_admission_*'))[-1];O=R/('protocol_v3_admission_controls_'+str(time.time_ns()));O.mkdir()
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
examples=rows(A/'EXAMPLES.jsonl');reviews=rows(A/'REVIEWS.jsonl');lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples};review_map={r['question_key']:r for r in reviews};runtime=read(A/'RUNTIME_CONTRACT.json');source_ref=read(W/'SOURCE_REF.json');summary=read(A/'SUMMARY.json');artifacts=Artifacts(R.parent);artifacts._cache={};checks={};details=[]
# Historical cohort pins the old admission implementation. Test the candidate
# with an in-memory runtime rebind; do not rewrite the immutable old cohort.
historical_runtime=copy.deepcopy(runtime);runtime=copy.deepcopy(runtime);runtime['admission_implementation_sha256']=IMPLEMENTATION_SHA256
def evaluate(x,review=None,rt=None):
 current=copy.deepcopy(x);selected=rt or runtime;current['annotation_provenance']['runtime_contract_sha256']=digest(selected)
 return admit(current,review or review_map[x['question_key']],artifacts,source_ref,selected)

def write(name,value):
 p=O/name;p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8');return {'path':str(p.resolve()),'sha256':file_sha(p)}
checks['all289_original_keys_once']=len(examples)==len({x['question_key'] for x in examples})==289
final_round=summary['manual_round']=='review_round_013'
checks['actual_review_migration_readmission_quarantine_counts']=len(reviews)==(289 if final_round else 225) and summary['existing_individual_reviews_reused_after_version_only_proof']==(286 if final_round else 223) and summary['new_protocol_specific_individual_readmissions']==(2 if final_round else 1) and summary['quarantined']==1 and summary['eligible']==(288 if final_round else 224)
known={}
old=R.parent/'r129_full_plan_completion_20261024/training_v2';frozen={str(old/(name+'.jsonl')):file_sha(old/(name+'.jsonl')) for name in ['train','validation','test']}
for split in ['train','validation','test']:
 for x in rows(old/(split+'.jsonl')):known[x['key']]=split
checks['independent281_saved_file_memberships_preserved']=len(known)==281 and all(x['split']==('train' if known[x['question_key']]=='train' else 'development') for x in examples if x['question_key'] in known)
checks['exposed_old_test_never_becomes_v3_training_or_fresh_holdout']=all(x['split']=='development' and x['exposure']=='development' for x in examples if known.get(x['question_key'])=='test')
admitted={r['question_key'] for r in reviews if r['adjudication_status'] in {'accepted','corrected'}}
expected={'train':sum(known.get(k)=='train' for k in admitted),'development':sum(known.get(k)!='train' for k in admitted),'holdout':0,'retained_evaluation':0}
checks['v3_actual_saved_membership_counts_no_fresh_holdout']=summary['eligible_split_counts']==expected
checks['dataset_gate_state_matches_current_review_inventory']=summary['unreviewed']==(0 if final_round else 64) and summary['training_ready']==final_round and (A/'bundle/READY_FOR_OPTIMIZATION.json').exists()==final_round
original206=next(x for x in rows(W/'review_round_012/EXAMPLES.jsonl') if x['question_key']==lookup[206]['question_key'])
original_review206=next(r for r in rows(W/'review_round_012/REVIEWS.jsonl') if r['question_key']==lookup[206]['question_key'])
checks['unresolved206_original_v2_proposal_and_review_preserved_exactly']=lookup[206]==original206 and review_map[lookup[206]['question_key']]==original_review206
decision=evaluate(lookup[206]);checks['version_change_does_not_readmit_fragment206']=not decision['eligible'] and decision['inventory_adjudicated'] and decision['adjudication_status']=='quarantined'
bad206=copy.deepcopy(original_review206);bad206['adjudication_status']='accepted';decision=evaluate(lookup[206],bad206);checks['accepted_flag_cannot_promote_fragment206']=not decision['eligible'] and not decision['inventory_adjudicated']
packed={x['question_key'] for split in ['train','development','holdout','retained_evaluation'] for x in rows(A/'bundle'/(split+'.jsonl'))};checks['fragment206_excluded_from_every_optimization_split']=lookup[206]['question_key'] not in packed and len(packed)==(288 if final_round else 224)
x=lookup[197];good=evaluate(x);checks['actual_prior_individual_review_admitted_after_structural_bridge']=good['eligible'] and good['review_acceptance_basis']=='pinned_prior_individual_adjudication_and_recomputed_version_only_migration' and not good['new_semantic_review_claimed_by_migration']
actual_191=evaluate(lookup[191]);checks['actual_row191_new_v3_semantic_review_admitted']=actual_191['eligible'] and actual_191['adjudication_status']=='corrected' and 'wire_migration_ref' not in lookup[191]['annotation_provenance']
checks['old_v2_row191_quarantine_bytes_and_state_retained']=read(W/'review_round_010/ADJUDICATION_191.json')['adjudication_status']=='quarantined'
if final_round:
 actual267=evaluate(lookup[267]);evidence267=read(A/'V3_ADJUDICATION_267.json');old267=read(W/'review_round_013/ADJUDICATION_267.json')
 checks['row267_has_individual_v3_readmission_not_automatic_migration']=actual267['eligible'] and actual267['adjudication_status']=='corrected' and 'wire_migration_ref' not in lookup[267]['annotation_provenance']
 checks['row267_old_v2_quarantine_retained']=old267['adjudication_status']=='quarantined' and old267['reviewed_label']['tasks'][0]['facet']=='open_periods'
 checks['row267_exact_play_facet_and_local_weekday_period']=lookup[267]['plan_label']['tasks'][0]['facet']=='service_periods' and lookup[267]['plan_label']['tasks'][0]['constraints']==[{'slot':'date','quote':'Monday','source_record_id':'','scope':'local'},{'slot':'time','quote':'afternoon','source_record_id':'','scope':'local'}]
 checks['row267_individual_source_revision_pinned']=evidence267['source_field_evidence']['migrated_schedule_0']['revision']==4 and all(evidence267['criteria'][k]['status']=='passed' for k in CRITERIA)
 bad267=copy.deepcopy(lookup[267]);bad267['plan_label']['tasks'][0]['facet']='bookable_periods';checks['row267_changed_semantic_facet_rejected']=not evaluate(bad267)['eligible']
base_record=artifacts.read(x['annotation_provenance']['wire_migration_ref'])
for name,change in [
 ('facet',lambda p:p['plan_label']['tasks'][0].update(facet='bookable_periods')),
 ('operation',lambda p:p['plan_label']['tasks'][0].update(operation='list')),
 ('slot_role',lambda p:p['plan_label']['tasks'][0]['constraints'][0].update(slot='platform')),
 ('slot_quote',lambda p:p['plan_label']['tasks'][0]['constraints'][0].update(quote='จันทร์')),
 ('target',lambda p:p['plan_label']['tasks'][0].update(target='วันจันทร์')),
 ('raw_input',lambda p:p.update(raw_question=p['raw_question']+' พรุ่งนี้')),
 ('family',lambda p:p.update(family='invented-other-family')),
 ('origin_method',lambda p:p['annotation_provenance'].update(method='teacher_plan')),
 ('context',lambda p:p.update(allowed_context=[{'client_approved_history':True}]))]:
 bad=copy.deepcopy(x);change(bad);record=copy.deepcopy(base_record);record['migrated_example_sha256']=example_sha(bad);bad['annotation_provenance']['wire_migration_ref']=write('FORGED_'+name+'.json',record)
 bad['messages']=v3.messages(bad['raw_question'])+[{'role':'assistant','content':json.dumps(bad['plan_label'],ensure_ascii=False,separators=(',',':'))}]
 decision=evaluate(bad);checks['changed_'+name+'_cannot_reuse_prior_review']=not decision['eligible'] and not decision['inventory_adjudicated'];details.append({'case':name,'decision':decision})
bad=copy.deepcopy(x);bad['annotation_provenance'].pop('wire_migration_ref');checks['missing_migration_record_cannot_reuse_old_review']=not evaluate(bad)['eligible']
bad=copy.deepcopy(x);bad['annotation_provenance']['wire_migration_ref']['sha256']='0'*64;checks['changed_migration_record_hash_rejected']=not evaluate(bad)['eligible']
bad=copy.deepcopy(x);record=copy.deepcopy(base_record);record['from_version']=v3.VERSION;bad['annotation_provenance']['wire_migration_ref']=write('FORGED_VERSION.json',record);checks['undeclared_version_bridge_rejected']=not evaluate(bad)['eligible']
dev=next(e for e in examples if e['split']=='development' and e['question_key'] in review_map and 'wire_migration_ref' in e['annotation_provenance']);bad=copy.deepcopy(dev);bad['split']='train';decision=evaluate(bad);checks['stale_or_forged_train_tag_cannot_override_saved_eval_file']=not decision['eligible'] and 'wire_migration_saved_file_split_mismatch' in decision['issues']
bad=copy.deepcopy(lookup[191]);bad['split']='train';decision=evaluate(bad);checks['new_manual_v3_review_does_not_authorize_old_test_to_train']=not decision['eligible'] and 'historical_evaluation_file_cannot_be_v3_training' in decision['issues']
originals=rows(W/'review_round_011/EXAMPLES.jsonl');original_reviews=rows(W/'review_round_011/REVIEWS.jsonl');oi=next(i for i,e in enumerate(originals,1) if e['question_key']==lookup[191]['question_key']);ri=next(i for i,r in enumerate(original_reviews,1) if r['question_key']==lookup[191]['question_key']);prior191=original_reviews[ri-1]
def ref(p,**kw):return {'path':str(p.resolve()),'sha256':file_sha(p),**kw}
record={'kind':'structural_wire_version_migration','from_version':WIRE_VERSION,'to_version':v3.VERSION,'original_example_ref':ref(W/'review_round_011/EXAMPLES.jsonl',line=oi),'original_review_ref':ref(W/'review_round_011/REVIEWS.jsonl',line=ri),'original_example_sha256':example_sha(originals[oi-1]),'migrated_example_sha256':example_sha(lookup[191])}
bad=copy.deepcopy(lookup[191]);bad['annotation_provenance']['wire_migration_ref']=write('QUARANTINE_OVERRIDE.json',record);decision=evaluate(bad,prior191);checks['old_quarantine_cannot_be_auto_readmitted_by_migration']=not decision['eligible'] and 'wire_migration_prior_review_not_accepted' in decision['issues']
forged_review=copy.deepcopy(prior191);forged_review['adjudication_status']='accepted';checks['accepted_flag_cannot_override_old_quarantined_artifact']=not evaluate(bad,forged_review)['eligible']
tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');v2_runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'))
decision=evaluate(x,rt=v2_runtime);checks['v3_label_not_admitted_under_retained_v2_runtime']=not decision['eligible'] and 'current_wire_schema_prompt_mismatch' in decision['issues']
bad_runtime=copy.deepcopy(runtime);bad_runtime['planner_protocol_implementation_sha256']='0'*64;checks['changed_protocol_implementation_blocks_admission']=not evaluate(x,rt=bad_runtime)['eligible']
unused=O/'UNUSED_REF.json';unused.write_text('{}\n','utf8');cmd=[sys.executable,'-B',str(R/'system/tools/train_reviewed_planner.py'),'--dataset',str(A/'bundle'),'--runtime-contract',str(A/'RUNTIME_CONTRACT.json'),'--base','D:/CodexTraining/psu-r121-20261022/model','--base-manifest-ref',str(unused),'--protocol-ref',str(unused),'--artifact-root',str(R.parent),'--check-only'];p=subprocess.run(cmd,capture_output=True,text=True,timeout=300);consumer=json.loads(p.stdout)
checks['actual_v3_consumer_blocks_missing_base_protocol_before_frameworks' if final_round else 'actual_v3_consumer_blocks_unreviewed_inventory_before_frameworks']=p.returncode==2 and consumer['phase']=='admission_blocked' and not consumer['admitted'] and consumer['model_frameworks_loaded']==[]
# Real staged family moves are replayed as immutable source-bound evidence.
family_dir=W/'semantic_amendments_round014'
family_refs=[ref(family_dir/'FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json'),ref(family_dir/'FAMILY_EN_PRICE_BOOKING_141_282.json')]
from app.knowledge.common.domain_flow.semantic_family_plan import apply_reviewed_family_moves
planned,moves=apply_reviewed_family_moves(examples,family_refs,artifacts)
planned_by_key={e['question_key']:e for e in planned};checks['four_reviewed_train_to_development_moves_replay']=len(moves)==4
for move in moves:
 moved=copy.deepcopy(planned_by_key[move['question_key']]);moved['annotation_provenance']['semantic_family_move_ref']=move['family_review_ref'];decision=evaluate(moved)
 checks['reviewed_move_admitted_'+move['question_key'][:12]]=decision['eligible'] and decision['inventory_adjudicated']
 bad=copy.deepcopy(moved);bad['annotation_provenance'].pop('semantic_family_move_ref');checks['move_without_review_rejected_'+move['question_key'][:12]]=not evaluate(bad)['eligible']
 bad=copy.deepcopy(moved);bad['annotation_provenance']['semantic_family_move_ref']['sha256']='0'*64;checks['forged_move_review_rejected_'+move['question_key'][:12]]=not evaluate(bad)['eligible']
 bad=copy.deepcopy(moved);bad['split']='train';checks['reviewed_move_cannot_claim_train_'+move['question_key'][:12]]=not evaluate(bad)['eligible']
checks['historical_split_files_not_modified']=all(file_sha(Path(p))==h for p,h in frozen.items());artifacts.verify_pinned_files()
report={'all_passed':all(checks.values()),'checks':checks,'v3_cohort':str(A.relative_to(R)),'summary':summary,'consumer':{'exit_code':p.returncode,'response':consumer},'old_v2_gateway_switched':False,'actual_model_generation_or_optimization':False,'all289_individually_reviewed':final_round,'all289_labels_accepted':False,'migration_is_new_semantic_review':False,'complete':False}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
