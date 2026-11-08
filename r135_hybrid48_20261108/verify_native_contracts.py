import copy,json,time
from types import SimpleNamespace
from verification_support import R
from app.knowledge.common.domain_flow.native_contract import invalidate,aggregate_contract,guard_contract
from app.knowledge.common.domain_flow.result_contract import attach_runtime
from app.knowledge.common.domain_flow.plan_contract import CompiledTask,CompiledRequest,Span,Obligation
task=CompiledTask('t1',Span(0,7,'hours?'),'C11','list','open_periods',{'operation':'list'},obligations=[Obligation('t1:a','task_completion','t1','open_periods')])
compiled=CompiledRequest('hours?',{'release_id':'fixture','epoch':1},[task])
child={'version':'fixture','tasks':[{'task_id':'t1','terminal_state':'supported','receipts':[{'field':'open_periods'}],'obligations':[{'id':'a','fulfilled':True,'claim_refs':['f1']}]}], 'executor_results':[{'task_id':'t1','claims':[{'fact_id':'f1'}],'source_field_claims':[{'value':['09:00','17:00']}],'calculation_receipts':[{'amount':1}],'resolved_obligations':[{'id':'a','fulfilled':True}],'receipts':[{'fact_id':'f1'}],'child_executor_result':{'claims':[{'fact_id':'nested'}],'receipts':[{}],'resolved_obligations':[]}}]}
checks={}
parent=aggregate_contract(compiled,[SimpleNamespace(decision_artifact={'execution_contract':child})],True)
checks['compound_has_one_executor_per_task']=len(parent['executor_results'])==1 and parent['executor_results'][0]['task_id']=='t1'
checks['child_evidence_preserved_before_delivery_invalidation']=parent['executor_results'][0]['claims']==[{'fact_id':'f1'}]
invalid=invalidate(parent)
checks['root_and_nested_executor_claims_withdrawn']=not invalid['executor_results'][0]['claims'] and not invalid['executor_results'][0]['child_executor_result']['claims']
checks['nested_calculations_and_source_values_withdrawn']=not invalid['executor_results'][0]['child_executor_result']['calculation_receipts'] and not invalid['executor_results'][0]['child_executor_result']['source_field_claims']
checks['all_delivered_obligations_retracted']=not invalid['tasks'][0]['obligations'][0]['fulfilled'] and not invalid['tasks'][0]['obligations'][0]['claim_refs']
checks['original_receipts_unchanged']=bool(parent['tasks'][0]['receipts']) and bool(child['executor_results'][0]['claims'])
guard={'needs':[{'claims':[{'value':'must disappear'}]}],'claims':[{}]};guard_contract(guard,compiled,'missing_source','no_binding')
checks['guard_uniform_contract']=len(guard['execution_contract']['executor_results'])==1 and guard['execution_contract']['executor_results'][0]['status']=='missing_source' and not guard['claims']
from dataclasses import dataclass
@dataclass
class Output:
 decision_artifact:dict
out=attach_runtime(Output({'response_type':'answer','query_plan':{'method':'bounded_test'},'obligations':[{'record_id':'r','field':'x'}]}),{'execution_question':'hours?'},{'active':'fixture','epoch':1})
c=out.decision_artifact['execution_contract']
checks['compatibility_uniform_but_not_fabricated_full_proof']=len(c['executor_results'])==1 and c['terminal_state']=='partial' and c['executor_results'][0]['unresolved_obligations'] and not c['executor_results'][0]['claims']
checks['compatibility_public_and_internal_consistent']=out.decision_artifact['response_type']=='partial_answer' and c['executor_results'][0]['public_status']=='partial_answer'
report={'checks':checks,'all_passed':all(checks.values()),'actual_model_inferences':0,'real_source_changes':0};outdir=R/('native_contract_verification_'+str(time.time_ns()));outdir.mkdir();(outdir/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
