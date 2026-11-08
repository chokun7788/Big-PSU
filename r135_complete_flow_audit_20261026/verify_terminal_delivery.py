import json,time
from verification_support import R
from app.knowledge.common.domain_flow.terminal_states import PUBLIC,LEGACY_NEED,TERMINALS,from_result,aggregate
from app.knowledge.common.domain_flow.obligation_verifier import terminal,withhold_delivery
checks={};original={'supported','partial','missing_input','missing_source','conflict','not_current','provider_unavailable','budget_exhausted','unsupported_operation','invalid_plan'}
checks['all_original_states_mapped']=original<=TERMINALS and set(PUBLIC)==set(LEGACY_NEED)==TERMINALS
for reason,expected in [('request_model_budget_exhausted','budget_exhausted'),('model_transport_failure','model_unavailable'),('unsupported_operation','unsupported_operation'),('source_receipt_reference_mismatch','invalid_plan'),('no_confirmed_source','missing_source')]:
 checks['reason_'+reason]=terminal({'status':'missing_source','reason':reason,'plan':{'metadata':{}}})==expected
checks['conflict_consistent']=from_result({'status':'partial','reason':'policy','plan':{'metadata':{'authority_conflict':True}}})=='conflict'
checks['independent_answer_preserved_on_budget_failure']=aggregate(['supported','budget_exhausted'],True)=='partial'
checks['model_not_labelled_external_provider']=from_result({'status':'unavailable','reason':'model_transport_failure'})!='provider_unavailable'
ledger={'terminal_state':'supported','receipts':[{'fact_id':'rejected'}],'all_obligations_fulfilled':True,'collection_proof':{'verified':True},'fatal':['source_receipt_reference_mismatch'],'reason_codes':['old'],'obligations':[{'fulfilled':True,'claim_refs':['rejected']}]};safe=withhold_delivery(ledger,'source_receipt_verification_failed','invalid_plan')
checks['withheld_receipts_not_delivered']=not safe['receipts'] and not safe['all_obligations_fulfilled'] and all(not o['fulfilled'] and not o['claim_refs'] for o in safe['obligations'])
checks['forensic_evidence_retained']=safe['withheld_evidence']['receipts']==ledger['receipts'] and ledger['terminal_state']=='supported'
out=R/('terminal_verification_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'inferences':0,'real_data_changes':0};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(R/'TERMINAL_VERIFICATION_LATEST.json').write_text(json.dumps({'output':str(out),'all_passed':report['all_passed'],'checks':len(checks)},indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
