"""Check actual pinned questions, review provenance and conservative split direction."""
import json,re,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
W=R/'training_review_workbench_1793037663397671000';P=W/'semantic_amendments_round014/FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json';g=json.loads(P.read_text('utf8'));A=W/'protocol_v3_admission_1793109982985437000';xs=[json.loads(t) for t in (A/'EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['question_key']:x for x in xs};saved=R.parent/'r129_full_plan_completion_20261024/training_v2';hashes={str(saved/(n+'.jsonl')):file_sha(saved/(n+'.jsonl')) for n in ['train','validation','test']};checks={};members=g['members']
checks['exact_four_distinct_questions']=len(members)==len({m['question_key'] for m in members})==4 and {m['original_row'] for m in members}=={104,133,134,135}
checks['each_raw_question_and_original_review_reference_is_pinned']=all(lookup[m['question_key']]['raw_question']==m['question'] and file_sha(m['example_ref']['path'])==m['example_ref']['sha256'] and file_sha(m['review_ref']['path'])==m['review_ref']['sha256'] for m in members)
checks['all_have_separate_price_and_reservation_needs']=all({(t['domain'],t['operation']) for t in lookup[m['question_key']]['plan_label']['tasks']}=={('service_fee','price_calculate'),('reservation','detail')} for m in members)
checks['shared_service_is_explicit_in_each_reviewed_plan']=all(lookup[m['question_key']]['plan_label']['shared_bindings'] for m in members)
checks['different_services_and_durations_are_not_claimed_identical']=len({m['source_service'] for m in members})==3 and len({m['source_duration'] for m in members})==2 and 'not identical factual questions' in g['semantic_rationale']
checks['same_template_was_split_across_training_and_development']={m['current_split'] for m in members}=={'train','development'}
checks['proposal_only_moves_training_to_development']=all(m['proposed_split']=='development' for m in members) and sum(m['current_split']=='train' for m in members)==3
checks['prior_family_and_exposure_remain_unchanged']=all(lookup[m['question_key']]['family']==m['original_family'] and lookup[m['question_key']]['original_families']==m['original_families'] and lookup[m['question_key']]['exposure']=='development' for m in members)
checks['historical_split_files_and_cohort_unchanged']=all(file_sha(p)==h for p,h in hashes.items()) and not g['current_cohorts_modified'] and not g['semantic_labels_changed']
checks['unreviewed_template_not_added']=not re.fullmatch(r'นักศึกษา PSU เล่น (PC|Nintendo Switch|VR) (30 นาที|2 ชั่วโมง) เสียกี่บาท แล้วจองยังไง','บุคคลทั่วไป เล่น VR 2 ชั่วโมง เสียกี่บาท แล้วจองยังไง')
checks['no_fresh_holdout_or_training_claim']=not g['fresh_holdout_claimed'] and not g['optimizer_authorized'] and not g['new_unique_question_reviews']
O=R/('shared_template_family_controls_'+str(time.time_ns()));O.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'family_review':str(P.relative_to(R)),'full_semantic_family_audit_complete':False,'actual_model_training_or_inferences':0,'historical_files_modified':False}
(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
