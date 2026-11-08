"""Actual frozen file membership controls, independent of stale row split tags."""
import json,time,collections,hashlib
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import example_sha,file_sha,admit,Artifacts
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('current_admission_*'))[-1];examples=[json.loads(x) for x in (A/'EXAMPLES.jsonl').read_text('utf8').splitlines()];reviews=[json.loads(x) for x in (A/'REVIEWS.jsonl').read_text('utf8').splitlines()];old=R.parent/'r129_full_plan_completion_20261024/training_v2';known={};family_splits=collections.defaultdict(set);original_splits=collections.defaultdict(set);stale=0
before={str(p):file_sha(p) for p in [old/(s+'.jsonl') for s in ['train','validation','test']]}
for split in ['train','validation','test']:
 for row in map(json.loads,(old/(split+'.jsonl')).read_text('utf8').splitlines()):known[row['key']]=(split,row);stale+=row.get('split')!=split
checks={'all289_original_keys_once':len(examples)==len({x['question_key'] for x in examples})==289,'all281_saved_split_rows_found':len(known)==281,'stale_original_row_split_metadata_observed':stale>0}
for x in examples:
 if x['question_key'] not in known:continue
 split,row=known[x['question_key']];expected='train' if split=='train' else 'development';checks.setdefault('current_split_uses_final_frozen_file_membership',True);checks['current_split_uses_final_frozen_file_membership'] &= x['split']==expected
 family_splits[x['family']].add(x['split'])
 for family in x['original_families']:original_splits[family].add(x['split'])
checks['review_families_stay_disjoint_after_test_to_development']=all(len(v)==1 for v in family_splits.values());checks['original_families_stay_disjoint_after_test_to_development']=all(len(v)==1 for v in original_splits.values());checks['all_exposed_rows_explicit_development_history']=all(x['exposure']=='development' and x['split']!='holdout' for x in examples)
index={x['question_key']:x for x in examples};checks['packing_and_split_fix_do_not_rewrite_semantic_reviews']=all(r['example_sha256']==example_sha(index[r['question_key']]) for r in reviews)
manual=W/json.loads((A/'SUMMARY.json').read_text('utf8'))['manual_round'];recorded=[json.loads(x) for x in (manual/'REVIEWS.jsonl').read_text('utf8').splitlines()]
final_round=manual.name=='review_round_013'
checks['all_recorded_current_adjudications_preserved']=reviews==recorded and len(reviews)==(289 if final_round else 225)
prior205=[json.loads(x) for x in (W/'review_round_011/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior205_adjudication_records_unchanged']=reviews[:205]==prior205
prior195=[json.loads(x) for x in (W/'review_round_010/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior195_adjudication_records_unchanged']=reviews[:195]==prior195
prior175=[json.loads(x) for x in (W/'review_round_009/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior175_adjudication_records_unchanged']=reviews[:175]==prior175
prior155=[json.loads(x) for x in (W/'review_round_008/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior155_adjudication_records_unchanged']=reviews[:155]==prior155
prior135=[json.loads(x) for x in (W/'review_round_007/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior135_adjudication_records_unchanged']=reviews[:135]==prior135
prior115=[json.loads(x) for x in (W/'review_round_006/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior115_adjudication_records_unchanged']=reviews[:115]==prior115
prior96=[json.loads(x) for x in (W/'review_round_005/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior96_adjudication_records_unchanged']=reviews[:96]==prior96
prior86=[json.loads(x) for x in (W/'review_round_004/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior86_adjudication_records_unchanged']=reviews[:86]==prior86
prior66=[json.loads(x) for x in (W/'review_round_003/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior66_adjudication_records_unchanged']=reviews[:66]==prior66
prior=[json.loads(x) for x in (W/'review_round_001/REVIEWS.jsonl').read_text('utf8').splitlines()];checks['prior21_adjudication_records_unchanged']=reviews[:21]==prior
checks['historical_split_files_unchanged']=all(file_sha(Path(p))==sha for p,sha in before.items());checks['actual_dataset_gate_state']=json.loads((A/'bundle/ADMISSION.json').read_text('utf8'))['ready_for_optimization']==final_round and (A/'bundle/READY_FOR_OPTIMIZATION.json').exists()==final_round
quarantined=[r for r in reviews if r['adjudication_status']=='quarantined'];checks['individually_unresolved_labels_explicitly_quarantined']=len(quarantined)==(3 if final_round else 2) and {index[r['question_key']]['annotation_provenance']['historical_review_ref']['line']-1 for r in quarantined}==({191,206,267} if final_round else {191,206})
eligible_keys={x['question_key'] for split in ['train','development','holdout','retained_evaluation'] for x in map(json.loads,(A/'bundle'/(split+'.jsonl')).read_text('utf8').splitlines())}
checks['actual_quarantined_label_never_enters_optimization_splits']=all(r['question_key'] not in eligible_keys for r in quarantined) and len(eligible_keys)==(286 if final_round else 223)
for r in quarantined:
 row=index[r['question_key']]['annotation_provenance']['historical_review_ref']['line']-1
 evidence=json.loads(Path(r['adjudication_ref']['path']).read_text('utf8'));checks['row'+str(row)+'_quarantine_preserves_prior_proposal_and_unresolved_facet']=evidence['prior_label']==evidence['reviewed_label'] and evidence['criteria']['intent_operation_facet']['status']=='unresolved'
 bad=dict(r);bad['adjudication_status']='accepted';result=admit(index[bad['question_key']],bad,Artifacts(R.parent),json.loads((W/'SOURCE_REF.json').read_text('utf8')),json.loads((A/'RUNTIME_CONTRACT.json').read_text('utf8')));checks['row'+str(row)+'_accepted_flag_cannot_override_actual_quarantine_record']=not result['eligible'] and not result['inventory_adjudicated']
out=R/('saved_training_import_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'current_admission':str(A.relative_to(R)),'historical_rows_with_stale_split_tag':stale,'final_saved_bucket_counts':dict(collections.Counter(s for s,r in known.values())),'current_proposal_split_counts':dict(collections.Counter(x['split'] for x in examples)),'historical_files_modified':False,'actual_model_inferences':0,'optimizer_started':False,'all_labels_semantically_reviewed':False};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
