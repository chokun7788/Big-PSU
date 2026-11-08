"""Read original logs to distinguish queue admission from failed inference."""
import collections,gzip,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025'
counts=collections.Counter();parser=collections.Counter();examples=collections.defaultdict(list)
for p in sorted((P/'full01').glob('RESULTS_*.jsonl.gz')):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:
   x=json.loads(line);a=(x.get('result') or {}).get('decision_artifact') or {};context=a.get('request_context') or {};events=list((a.get('domain_flow') or {}).get('model_events',[]));u=(a.get('understanding') or {}).get('event')
   if u:events.append(u)
   unique={e.get('id',str(i)):e for i,e in enumerate(events)}
   denies=[e for e in unique.values() if 'model_admission_unavailable' in str(e.get('error'))]
   busy=[e for e in denies if (e.get('admission') or {}).get('llm_concurrency_allowed') is False]
   calls=x.get('observed_model_http_calls',[]);reserved=context.get('model_calls_reserved',0)
   state=a.get('response_type');counts['all_requests']+=1
   if denies:counts['requests_with_admission_denial']+=1
   if busy:counts['requests_with_explicit_concurrency_busy']+=1
   if denies and not calls:
    counts['admission_denied_without_any_http']+=1
    if reserved>=context.get('max_model_calls',2):counts['budget_fully_reserved_without_any_http']+=1
    if state in ['unavailable','live_unavailable','retry','unconfirmed','clarification']:counts['nonanswer_or_partial_state_without_http_after_denial']+=1
    if len(examples['no_http_denial'])<8:examples['no_http_denial'].append({'key':x['key'],'question':x['question'],'answer':x['result'].get('answer'),'reserved':reserved,'max':context.get('max_model_calls'),'events':[{'stage':e.get('stage'),'error':e.get('error'),'http_attempted':e.get('http_attempted'),'admission':e.get('admission')} for e in denies]})
   for e in unique.values():
    if not e.get('transport_ok') or e.get('schema_ok') is not False:continue
    prov=e.get('model_provenance') or {};stage='context' if e.get('stage')=='context_understanding' else 'selector';parser[(stage,e.get('reason'),e.get('error'))]+=1
   for e in context.get('events',[]):
    if e.get('stage')=='R129_budget_ledger' and e.get('accepted') is False:counts['budget_reservation_rejections_events']+=1
out={'read_only':True,'new_model_or_assistant_queries':0,'counts':dict(counts),'parser_rejections_unique_event_ids':[{'stage_reason_error':list(k),'events':v} for k,v in parser.most_common()],'examples':dict(examples),'source_code_evidence':[{'path':'R130/system/app/knowledge/common/domain_flow/model_gateway.py','finding':'ctx.reserve_model(stage) occurs before llm_call_allowed; rejected admission can consume a reservation without HTTP. Need to distinguish reserved/attempted/spent in a future fix.'},{'path':'R130/system/app/pipeline/llm_health.py','finding':'Concurrency wait defaults to0.20sec and limit1; global ModelAdmissionBroker shared by2workers in retained harness.'},{'path':'R129/serve_model.py','finding':'One generation lock; format/schema is hashed but not used for constrained decoding.'}],'interpretation':'Confirmed admission/serialization mechanisms are separate from semantic model ability and source absence. Counting rejected admission against a reservation is observed behavior; whether to refund depends on the explicit budget policy, not automatically labelled a defect.','created_at':time.time()}
(R/'ADMISSION_AND_PROTOCOL_FORENSICS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'counts':dict(counts),'parser':out['parser_rejections_unique_event_ids']},ensure_ascii=False))
