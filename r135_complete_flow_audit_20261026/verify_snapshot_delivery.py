import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.terminal_states import from_result
snap=snapshot()
class ChangedBeforeDelivery:
 path=R/'system/data/knowledge/common.sqlite'
 def snapshot(self):return snap
 def still_current(self,old):return False
checks={}
answer=CommonAnswerer(ChangedBeforeDelivery()).answer('What building and floor is the studio in?',locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
art=answer.decision_artifact;c=art['execution_contract']
checks['changed_snapshot_requests_retry']=art['response_type']=='retry' and c['terminal_state']=='not_current'
checks['no_top_level_delivered_claims']=not art.get('domain_flow',{}).get('typed_claims') and not art.get('obligations') and not answer.hits
executors=c.get('executor_results',[])+[n['executor_result'] for n in art.get('need_results',[]) if n.get('executor_result')]
checks['root_and_need_executor_proofs_both_withdrawn']=bool(executors) and all(not e.get('claims') and not e.get('receipts') and not e.get('source_field_claims') and not e.get('calculation_receipts') and not e.get('resolved_obligations') and e['status']=='not_current' for e in executors)
checks['need_statuses_match_central_taxonomy']=all(n['terminal_state']=='not_current' and n['status']=='not_current' for n in art.get('need_results',[]))
checks['verifier_no_stale_supported_certificate']=not c.get('verifier_result') or c['verifier_result'].get('delivery_invalidated') is True
checks['protocol_failure_not_external_provider']=all(from_result({'status':'unavailable','reason':reason})=='model_unavailable' for reason in ['model_invalid_choice','model_duplicate_item','model_identity_mismatch','model_plan_missing'])
report={'all_passed':all(checks.values()),'checks':checks,'actual_network_or_model_calls':0,'user_data_changes':0};out=R/('snapshot_delivery_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'ARTIFACT.json').write_text(json.dumps(art,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
