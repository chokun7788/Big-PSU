"""Freeze reviewed data and reuse the locally proven NF4 optimizer mechanics."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
(R/'context_contract.py').write_text("import sys\nfrom pathlib import Path\nsys.path.insert(0,str(Path(__file__).resolve().parent/'system'))\nfrom app.knowledge.common.domain_flow.graph_protocol import messages\n",'utf8')
(R/'pack_tokens.py').write_text((OLD/'pack_tokens.py').read_text('utf8'),'utf8')
source=(OLD/'train_planner02.py').read_text('utf8')
source=source.replace('from planner_metrics import score,aggregate','')
begin=source.index('def infer_set(');end=source.index('def validation_loss(',begin);source=source[:begin]+source[end:]
source=source.replace("parser.add_argument('--run',default='train02')","parser.add_argument('--run',default='train01')")
source=source.replace("'TOKENIZED_test.json','BASE_MODEL_COMPLETE.json','CUDA_PREFLIGHT.json'","'TOKENIZED_test.json','ANNOTATION_REVIEW_SUMMARY.json','EVALUATION_PROTOCOL.json'")
source=source.replace("'planner_metrics.py',", "'context_contract.py','system/app/knowledge/common/domain_flow/graph_protocol.py',")
source=source.replace(" assert read('BASE_MODEL_COMPLETE.json')['complete'] and read('CUDA_PREFLIGHT.json')['nf4_forward_backward_passed']", " assert read('ANNOTATION_REVIEW_SUMMARY.json')['reviewed']==289")
source=source.replace("len(train)>=200 and len(test)==30", "len(train)>100 and len(test)>30")
begin=source.index(" prior=R/'train01';");end=source.index(' before_base=fingerprint',begin);source=source[:begin]+source[end:]
source=source.replace(" infer_set(model,tok,test,'trained_test',False)"," # Held-out test generation is performed later by the identical three-arm server.")
source=source.replace("'business_answer_targets':False", "'protocol':'r129-plan-v2','reviewed_labels':True,'business_answer_targets':False")
(R/'train_planner.py').write_text(source,'utf8')
protocol={'version':'r129-pre-inference-v1','frozen_before_training_and_inference':True,'arms':['base','retained','new'],'same_engine_data_clock_prompt_schema_precision_decoding_budgets_provider_fixture':True,'context_only_adapters':True,'other_stages_use_base_for_all_arms':True,'clock':'2026-10-24T12:00:00+07:00','generation':{'temperature':0,'max_context_tokens':8192,'max_new_tokens':900,'max_time_seconds':90},'checkpoint_selection':'validation completion loss only','metrics':['wire_schema_acceptance','task_domain_operation_field_multiset_exact','exact_target','slot_quote_role_f1','shared_edge_exact','clarification_exact','source_fatal_count','typed_obligation_completion','actual_content_review_separate','latency_p50_p95','transport_error_count'],'promotion':{'new_source_fatal_must_equal':0,'new_operation_field_exact_at_least_retained':True,'new_slot_f1_at_least_retained':True,'new_transport_rate_not_worse_than_retained':True,'noninferiority_margin':0.0,'otherwise_keep_retained_for_delivery':True},'accepted_wire_versions':['r129-plan-v2','explicit_r121_legacy_adapter'],'legacy_wire_adaptation_reported_separately':True,'historically_exposed_retained_questions':True,'fresh_generalization_claimed':False,'full_test_unique_keys':20554,'full_test_grades':55811,'legacy_full_rerun':False}
(R/'EVALUATION_PROTOCOL.json').write_text(json.dumps(protocol,indent=2),'utf8')
files=[R/n for n in ['train.jsonl','validation.jsonl','test.jsonl','ANNOTATION_REVIEW.jsonl','ANNOTATION_REVIEW_SUMMARY.json','EVALUATION_PROTOCOL.json','context_contract.py','system/app/knowledge/common/domain_flow/graph_protocol.py','system/app/knowledge/common/domain_flow/context_contract.py']]
(R/'DATASET_FREEZE.json').write_text(json.dumps({str(p.resolve()):sha(p) for p in files},indent=2),'utf8')
print('Prepared training and fixed evaluation protocol; GPU work not started.')
