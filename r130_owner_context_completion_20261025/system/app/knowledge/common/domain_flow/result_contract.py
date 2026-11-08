"""One result contract across typed readers, native tools and compatibility."""
import copy,time
VERSION='r129-executor-result-v2'
PUBLIC_STATUS={'supported':'answer','partial':'partial_answer','missing_input':'clarification','missing_source':'unconfirmed','conflict':'partial_answer','not_current':'not_current','provider_unavailable':'unavailable','budget_exhausted':'partial_answer','unsupported_operation':'unconfirmed','invalid_plan':'unconfirmed'}
def package(task,ledger,result,snapshot,costs=None):
 obligations=copy.deepcopy(ledger.get('obligations',[]));metadata=result.get('plan',{}).get('metadata',{})
 terminal=ledger.get('terminal_state','missing_source')
 if metadata.get('authority_conflict'):terminal='conflict'
 receipts=[]
 for receipt in ledger.get('receipts',[]):
  receipts.append({**receipt,'contract_version':'r129-evidence-receipt-v2','snapshot':snapshot})
 calculations=[]
 for i,c in enumerate(result.get('computations',[])):
  calculations.append({'id':task.id+':calc:'+str(i+1),'version':'r129-calculation-receipt-v2',**c,'input_claim_refs':[c.get('fact_id')],'transformation':'decimal_source_declared_billing_v2','snapshot':snapshot})
 return {'version':VERSION,'task_id':task.id,'operation':task.capability.get('semantic_operation',task.capability['operation']),
  'status':terminal,'public_status':PUBLIC_STATUS.get(terminal,'unconfirmed'),'reason_codes':ledger.get('reason_codes',[]),
  'claims':copy.deepcopy(result.get('claims',[])),'receipts':receipts,'calculation_receipts':calculations,
  'resolved_obligations':[o for o in obligations if o.get('fulfilled') is True],
  'unresolved_obligations':[o for o in obligations if o.get('fulfilled') is not True],
  'result_scope':{'category':task.category,'field':task.facet,'entity_ids':task.bound_record_ids,'shared_binding_ids':[b.id for b in task.bindings],'snapshot':snapshot},
  'completeness':{'kind':'exact_set' if metadata.get('complete_set') else 'confirmed_subset' if result.get('claims') else 'unknown_coverage','basis':result.get('reason'),'member_ids':metadata.get('catalog_member_ids') or metadata.get('member_ids') or []},
  'costs':costs or {},'warnings':{k:v for k,v in metadata.items() if any(s in k for s in ['unconfirmed','partial','conflict','validity','limits'])},'human_semantic_accuracy_claimed':False}

def attach_runtime(result,context,snapshot):
 from dataclasses import replace
 from .request_provenance import capture,attach_compiled
 artifact=dict(result.decision_artifact or {});contract=copy.deepcopy(artifact.get('execution_contract') or {})
 if not contract:
  plan=artifact.get('query_plan') or {};receipts=artifact.get('obligations',[])
  state={'answer':'supported','list':'supported','partial_answer':'partial','clarification':'missing_input','unconfirmed':'missing_source','unavailable':'provider_unavailable','not_current':'not_current','retry':'not_current'}.get(artifact.get('response_type'),'missing_source')
  contract={'version':'r129','path':'bounded_compatibility_contract','tasks':[{'task_id':'t1','terminal_state':state,'reason_codes':[plan.get('method','compatibility_source_read')],'receipts':receipts,'obligations':artifact.get('need_ledger',{}).get('obligations',[]) if isinstance(artifact.get('need_ledger'),dict) else []}],'compatibility_limits_explicit':True,'whole_question_semantics_verified':False}
 contract['runtime_contract_version']='r129-complete-plan-v2'
 contract['source_snapshot']={'release_id':snapshot.get('active'),'epoch':snapshot.get('epoch')}
 contract['dialogue_resolution']=copy.deepcopy(context)
 contract['source_and_semantic_coverage_separate']=True
 queue=[]
 for task in contract.get('tasks',[]):
  state=task.get('terminal_state');reasons=task.get('reason_codes') or [task.get('reason')]
  if state in {'missing_source','not_current','conflict','invalid_plan','unsupported_operation','budget_exhausted'}:
   route='source_review' if state in {'missing_source','not_current','conflict'} else 'executor_review'
   queue.append({'task_id':task.get('task_id'),'route':route,'state':state,'reason_codes':[r for r in reasons if r],'auto_train':False,'review_before_labeling':True,'source_snapshot':contract['source_snapshot']})
 for event in artifact.get('domain_flow',{}).get('model_events',[]):
  if event.get('transport_ok') and event.get('schema_ok') is False:queue.append({'route':'planner_protocol_review','reason':event.get('reason'),'auto_train':False,'review_before_labeling':True})
 artifact['review_queue']=queue
 attach_compiled(contract,capture(context['execution_question']))
 artifact['execution_contract']=contract
 return replace(result,decision_artifact=artifact)
