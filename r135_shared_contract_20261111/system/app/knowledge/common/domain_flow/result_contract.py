"""One result contract across typed readers, native tools and compatibility."""
import copy,time
VERSION='r135-executor-result-v3'
from .terminal_states import PUBLIC as PUBLIC_STATUS,VERSION as STATUS_VERSION
def package(task,ledger,result,snapshot,costs=None):
 obligations=copy.deepcopy(ledger.get('obligations',[]));metadata=result.get('plan',{}).get('metadata',{})
 terminal=ledger.get('terminal_state','missing_source')
 receipts=[]
 for receipt in ledger.get('receipts',[]):
  receipts.append({**receipt,'contract_version':'r129-evidence-receipt-v2','snapshot':snapshot})
 calculations=[]
 for i,c in enumerate(result.get('computations',[])):
  calculations.append({'id':task.id+':calc:'+str(i+1),'version':'r129-calculation-receipt-v2',**c,'input_claim_refs':[c.get('fact_id')],'transformation':'decimal_source_declared_billing_v2','snapshot':snapshot})
 proof=ledger.get('collection_proof') or {}
 if proof.get('group_membership_verified') and task.operation=='group_count':
  for group,members in proof['groups'].items():calculations.append({'id':task.id+':count:'+str(group),'version':'r135-set-calculation-v1','group':group,'member_ids':members,'result_count':len(members),'transformation':'distinct_recorded_members','input_claim_refs':[c.get('fact_id') for c in result.get('claims',[])],'scope':proof['kind'],'snapshot':snapshot})
 excluded=next((d for d in ledger.get('dependency_receipts',[]) if d.get('verified') and d.get('outcome')=='false'),None)
 return {'version':VERSION,'status_mapping_version':STATUS_VERSION,'task_id':task.id,'operation':task.capability.get('semantic_operation',task.capability['operation']),
  'status':terminal,'public_status':PUBLIC_STATUS.get(terminal,'unconfirmed'),'reason_codes':ledger.get('reason_codes',[]),
  'claims':copy.deepcopy(result.get('claims',[])),'receipts':receipts,'calculation_receipts':calculations,
  'reader_route':copy.deepcopy(metadata.get('hybrid_route')),
  'source_field_claims':[{'record_id':r['record_id'],'field':r['field'],'value':copy.deepcopy(r.get('source_value')),'evidence_refs':r['evidence_refs'],'basis':'verified_native_field_pointer','not_a_rendered_text_entailment_proof':True} for r in receipts if r.get('pointer_verified') and 'source_value' in r],
  'observation_receipts':copy.deepcopy(ledger.get('live_observations',[])),'dependency_receipts':copy.deepcopy(ledger.get('dependency_receipts',[])),
  'resolved_obligations':[o for o in obligations if o.get('fulfilled') is True],
  'unresolved_obligations':[o for o in obligations if o.get('fulfilled') is not True],
  'result_scope':{'category':task.category,'field':task.facet,'entity_ids':task.bound_record_ids,'shared_binding_ids':[b.id for b in task.bindings],'snapshot':snapshot},
  'completeness':{'kind':'conditional_not_applicable','basis':'verified_prerequisite_condition_not_met','source_claim_refs':excluded['source_claim_refs']} if excluded else copy.deepcopy(ledger['collection_proof']) if ledger.get('collection_proof') else {'kind':'confirmed_subset' if result.get('claims') else 'unknown_coverage','basis':result.get('reason'),'member_ids':metadata.get('catalog_member_ids') or metadata.get('member_ids') or []},
  'costs':costs or {},'warnings':{k:v for k,v in metadata.items() if any(s in k for s in ['unconfirmed','partial','conflict','validity','limits'])},'human_semantic_accuracy_claimed':False}

def attach_runtime(result,context,snapshot,index=None):
 from dataclasses import replace
 from .request_provenance import capture,attach_compiled
 from .terminal_states import from_public,aggregate,VERSION as status_version
 artifact=dict(result.decision_artifact or {});contract=copy.deepcopy(artifact.get('execution_contract') or {})
 if not contract.get('tasks'):
  plan=artifact.get('query_plan') or {};receipts=artifact.get('obligations',[])
  state='invalid_plan' if contract.get('path')=='invalid_compiled_plan' else from_public(artifact)
  obligations=artifact.get('need_ledger',{}).get('obligations',[]) if isinstance(artifact.get('need_ledger'),dict) else []
  if not obligations:obligations=[{'id':'t1:operation','kind':'task_completion','expected':plan.get('requested_fields',[]),'fulfilled':False,'reason':'bounded_compatibility_operation_not_independently_verified'}]
  if state=='supported' and not all(o.get('fulfilled') is True for o in obligations):state='partial'
  contract={**contract,'version':'r135','path':contract.get('path','bounded_compatibility_contract'),'tasks':[{'task_id':'t1','terminal_state':state,'reason_codes':[plan.get('method','compatibility_source_read')],'receipts':receipts,'obligations':obligations,'all_obligations_fulfilled':all(o.get('fulfilled') is True for o in obligations)}],'compatibility_limits_explicit':True,'whole_question_semantics_verified':False}
 if not contract.get('executor_results'):
  from types import SimpleNamespace
  executors=[]
  for ledger in contract['tasks']:
   task=SimpleNamespace(id=ledger['task_id'],category=artifact.get('domain_flow',{}).get('category'),facet=None,capability={'operation':'bounded_compatibility'},bound_record_ids=[],bindings=[])
   typed={'claims':[],'computations':[],'plan':{'metadata':{}},'reason':contract.get('reason','compatibility_operation_unverified')}
   executors.append(package(task,ledger,typed,{'release_id':snapshot.get('active'),'epoch':snapshot.get('epoch')}))
  contract['executor_results']=executors
 contract['terminal_state']=aggregate((t['terminal_state'] for t in contract['tasks']),any(t.get('receipts') for t in contract['tasks']))
 contract['status_mapping_version']=status_version
 if artifact.get('response_type')!='retry':artifact['response_type']=PUBLIC_STATUS[contract['terminal_state']]
 contract['runtime_contract_version']='r135-complete-flow-v3'
 contract['source_snapshot']={'release_id':snapshot.get('active'),'epoch':snapshot.get('epoch')}
 contract['dialogue_resolution']=copy.deepcopy(context)
 contract['source_and_semantic_coverage_separate']=True
 delivered_answer=getattr(result,'answer','')
 if index is not None and not contract.get('verifier_result'):
  from .request_verifier import verify
  contract['verifier_result']=verify(index,context['execution_question'],contract,getattr(result,'answer',''))
 verifier=contract.get('verifier_result') or {}
 if verifier:
  from .request_verifier import attach_constraint_obligations
  attach_constraint_obligations(contract,verifier)
  for row,ledger in zip(artifact.get('need_results',[]),contract.get('tasks',[])):
   from .terminal_states import LEGACY_NEED
   row.update(terminal_state=ledger['terminal_state'],status=LEGACY_NEED[ledger['terminal_state']],execution_contract=ledger)
 if verifier.get('requires_partial_delivery') and not verifier.get('delivery_invalidated') and contract['terminal_state'] in {'supported','partial'}:
  contract['terminal_state']='partial';artifact['response_type']='partial_answer'
  artifact['request_coverage_notice']={'reason':'independent_request_or_constraint_coverage_unresolved','need_ids':verifier['plan_coverage']['uncovered_need_ids']}
  from .request_verifier import delivery_notice
  from .engine import language
  notice=delivery_notice(verifier,context.get('effective_locale') or language(context['execution_question'],context.get('requested_locale','auto')))
  if notice and notice not in delivered_answer:delivered_answer+='\n\n'+notice
 queue=[]
 for task in contract.get('tasks',[]):
  state=task.get('terminal_state');reasons=task.get('reason_codes') or [task.get('reason')]
  if state in {'missing_source','not_current','conflict','invalid_plan','unsupported_operation','budget_exhausted','model_unavailable','provider_unavailable'}:
   route='source_review' if state in {'missing_source','not_current','conflict'} else 'executor_review'
   queue.append({'task_id':task.get('task_id'),'route':route,'state':state,'reason_codes':[r for r in reasons if r],'auto_train':False,'review_before_labeling':True,'source_snapshot':contract['source_snapshot']})
  elif state=='partial' and any('variant' in str(r) for r in reasons):
   queue.append({'task_id':task.get('task_id'),'route':'source_review','state':state,'reason_codes':[r for r in reasons if r],'auto_train':False,'review_before_labeling':True,'source_snapshot':contract['source_snapshot']})
 for event in artifact.get('domain_flow',{}).get('model_events',[]):
  if event.get('transport_ok') and event.get('schema_ok') is False:queue.append({'route':'planner_protocol_review','reason':event.get('reason'),'auto_train':False,'review_before_labeling':True})
 verifier=contract.get('verifier_result') or {}
 if verifier and not verifier.get('delivery_invalidated') and (verifier.get('plan_coverage',{}).get('status') in {'uncovered','review_required'} or verifier.get('constraint_coverage',{}).get('status')=='review_required'):
  queue.append({'route':'request_semantics_review','reason':'independent_request_or_constraint_coverage_unresolved','auto_train':False,'review_before_labeling':True,'source_snapshot':contract['source_snapshot']})
 artifact['review_queue']=queue
 attach_compiled(contract,capture(context['execution_question']))
 artifact['execution_contract']=contract
 updates={'decision_artifact':artifact}
 if hasattr(result,'answer'):updates['answer']=delivered_answer
 return replace(result,**updates)
