"""Verify the English pair against saved inputs and prior human reviews."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
W=R/'training_review_workbench_1793037663397671000';A=W/'protocol_v3_admission_1793109982985437000';P=W/'semantic_amendments_round014/FAMILY_EN_PRICE_BOOKING_141_282.json';g=json.loads(P.read_text('utf8'));xs=[json.loads(t) for t in (A/'EXAMPLES.jsonl').read_text('utf8').splitlines()];bykey={x['question_key']:x for x in xs};members=g['members'];checks={}
checks['two_unique_original_rows']={m['original_row'] for m in members}=={141,282} and len({m['question_key'] for m in members})==2
checks['raw_inputs_and_example_hashes_are_exact']=all(bykey[m['question_key']]['raw_question']==m['question'] and file_sha(m['example_ref']['path'])==m['example_ref']['sha256'] for m in members)
checks['prior_individual_reviews_are_attested']=all(file_sha(m['review_ref']['path'])==m['review_ref']['sha256'] for m in members)
checks['price_and_booking_are_separate_for_both']=all({(t['domain'],t['operation']) for t in bykey[m['question_key']]['plan_label']['tasks']}=={('service_fee','price_calculate'),('reservation','detail')} for m in members)
checks['ellipsis_and_anaphor_are_not_collapsed']={m['binding_basis'] for m in members}=={'source_related_ellipsis','explicit_anaphor'}
checks['different_service_audience_and_duration_preserved']=len({m['service_target'] for m in members})==2 and len({str(m['price_audience_quotes']) for m in members})==2 and len({str(m['price_duration_quotes']) for m in members})==2
checks['cross_split_risk_is_observed']={m['current_split'] for m in members}=={'train','development'} and all(m['proposed_split']=='development' for m in members)
checks['original_families_and_exposure_are_unchanged']=all(bykey[m['question_key']]['family']==m['original_family'] and bykey[m['question_key']]['original_families']==m['original_families'] and bykey[m['question_key']]['exposure']=='development' for m in members)
checks['no_business_answer_equivalence_or_fresh_holdout_claim']='not identical factual questions' in g['semantic_rationale'] and not g['fresh_holdout_claimed'] and not g['optimizer_authorized']
checks['no_cohort_or_label_changed']=not g['current_cohorts_modified'] and not g['semantic_labels_changed'] and g['new_unique_question_reviews']==0
O=R/('english_price_booking_family_controls_'+str(time.time_ns()));O.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'family_review':str(P.relative_to(R)),'whole_semantic_family_audit_complete':False,'actual_model_training_or_inferences':0,'historical_files_modified':False};(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
