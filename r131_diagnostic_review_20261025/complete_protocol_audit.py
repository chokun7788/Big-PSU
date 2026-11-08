"""Account for every saved successful model gateway event without new calls."""
import collections
import gzip
import json
from pathlib import Path

R=Path(__file__).resolve().parent
P=R.parent/'r130_owner_context_completion_20261025'
counts=collections.Counter();nonrejected=[];gateway=collections.Counter()
for path in sorted((P/'full01').glob('RESULTS_*.jsonl.gz')):
 with gzip.open(path,'rt',encoding='utf8') as stream:
  for line in stream:
   row=json.loads(line);a=(row.get('result') or {}).get('decision_artifact') or {}
   for e in (a.get('request_context') or {}).get('events',[]):
    if e.get('stage')=='R129_model_gateway' and e.get('transport_ok'):
     gateway[e.get('model_stage','unknown')]+=1
   events=list((a.get('domain_flow') or {}).get('model_events',[]))
   u=(a.get('understanding') or {}).get('event')
   if u:events.append(u)
   seen=set()
   for e in events:
    identity=e.get('id') or json.dumps(e,sort_keys=True)
    if identity in seen:continue
    seen.add(identity)
    if not e.get('transport_ok'):continue
    stage=e.get('stage','unknown')
    counts[(stage,str(e.get('schema_ok')),str(e.get('reason')),str(e.get('error')))]+=1
    if e.get('schema_ok') is not False:
     nonrejected.append({'key':row['key'],'question':row['question'],'answer':(row.get('result') or {}).get('answer'),'understanding_accepted':(a.get('understanding') or {}).get('accepted'),'event':e})
out={'saved_full_gateway_transport_successes_by_stage':dict(gateway),'parser_event_groups':[{'stage_schema_reason_error':list(k),'count':v} for k,v in counts.items()],'nonrejected_event_cases':nonrejected,'no_new_queries':True,'schema_pass_does_not_establish_semantic_correctness':True}
(R/'COMPLETE_PROTOCOL_ACCOUNTING.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in out.items() if k!='nonrejected_event_cases'},ensure_ascii=False))
print(json.dumps([{'key':x['key'],'question':x['question'],'accepted':x['understanding_accepted'],'reason':x['event'].get('reason'),'schema_ok':x['event'].get('schema_ok')} for x in nonrejected],ensure_ascii=False))
