"""Finish summaries after successful gates outgrew the old partial-only assertion.

Existing corpus/gate/freeze bytes are verified and preserved, never regenerated.
Dataset readiness is distinct from base/protocol/evaluation/optimizer readiness.
"""
import json
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha,digest
W=R/'training_review_workbench_1793037663397671000';S=W/'review_round_013'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines()]
def save(p,d):
 if p.exists():assert read(p)==d
 else:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
originals={x['question_key'] for x in rows(S/'EXAMPLES.jsonl')};assert len(originals)==289
results=[]
for name,wire in [('current_admission_1793109983060241500','r129-plan-v2'),('protocol_v3_admission_1793109982985437000','r135-plan-v3')]:
 A=W/name;bundle=A/'bundle';a=read(bundle/'ADMISSION.json');freeze=read(bundle/'DATASET_FREEZE.json');ready=read(bundle/'READY_FOR_OPTIMIZATION.json');runtime=read(A/'RUNTIME_CONTRACT.json');examples=rows(A/'EXAMPLES.jsonl');reviews=rows(A/'REVIEWS.jsonl')
 assert {x['question_key'] for x in examples}==originals and len(examples)==len(reviews)==289 and a['ready_for_optimization'] and a['inventory_individually_adjudicated'] and not a['dataset_issues']
 assert ready['freeze_sha256']==file_sha(bundle/'DATASET_FREEZE.json') and ready['admission_sha256']==file_sha(bundle/'ADMISSION.json') and freeze['runtime_contract_sha256']==digest(runtime)
 assert all(file_sha(bundle/p)==h for p,h in freeze['files'].items())
 eligible=sum(x['eligible'] for x in a['rows']);quarantined=[x for x in reviews if x['adjudication_status']=='quarantined'];assert eligible+len(quarantined)==289
 if wire=='r129-plan-v2':
  process=read(A/'PROCESS.json');assert process['exit_code']==0 and eligible==286 and len(quarantined)==3
  summary={'manual_round':S.name,'current_runtime_contract_sha256':digest(runtime),'source_identity_sha256':a['source_identity_sha256'],'rows':289,'individually_reviewed':289,'eligible_reviewed_rows':286,'quarantined':3,'unreviewed':0,'eligible_split_counts':a['eligible_split_counts'],'training_ready':True,'optimizer_started':False,'semantic_adjudications_changed':0,'all_original_labels_semantically_reviewed':False,'all_original_questions_individually_reviewed':True,'base_protocol_and_evaluation_admission_proven':False}
 else:
  assert eligible==288 and len(quarantined)==1 and len(list(A.glob('MIGRATION_*.json')))==286
  assert all(read(A/('V3_ADJUDICATION_'+str(n)+'.json'))['historical_review_row']==n for n in [191,267])
  lookup={x['question_key']:x for x in examples};qrows=sorted(lookup[r['question_key']]['annotation_provenance']['historical_review_ref']['line']-1 for r in quarantined);assert qrows==[206]
  summary={'wire_version':wire,'manual_round':S.name,'all_original_keys':289,'unique_original_questions_individually_reviewed':289,'existing_individual_reviews_reused_after_version_only_proof':286,'new_protocol_specific_individual_readmissions':2,'eligible':288,'quarantined':1,'quarantined_original_rows':[206],'unreviewed':0,'eligible_split_counts':a['eligible_split_counts'],'training_ready':True,'source_identity_sha256':a['source_identity_sha256'],'runtime_contract_sha256':digest(runtime),'old_v2_files_unchanged':True,'old_v2_row191_still_quarantined':True,'other_original_quarantine_proposals_and_reviews_unchanged':True,'actual_model_generation_or_optimization':False,'new_semantic_reviews_claimed_for_version_only_migrations':False,'gateway_default_wire_changed':False,'complete':False}
 save(A/'SUMMARY.json',summary);results.append({'path':str(A.relative_to(R)),'summary_sha256':file_sha(A/'SUMMARY.json'),'wire_version':wire,'dataset_ready':True,'eligible':eligible,'quarantined':len(quarantined)})
receipt={'cohorts':results,'harness_issue':'Old builders asserted that every corpus remained partial. Both actual dataset gates succeeded after all289 questions were individually reviewed; only summary finalization failed. Existing source/example/review/freeze/READY bytes were preserved and verified.','corpus_rebuilt_again':False,'actual_optimizer_or_model_inferences':0,'base_protocol_evaluation_readiness_proven':False,'whole_flow_complete':False}
save(R/'ROUND013_DATASET_GATE_FINALIZATION.json',receipt);print(json.dumps(receipt))
