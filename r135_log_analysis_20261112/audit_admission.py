"""Inspect the saved health/cooldown receipt behind each admission-denied event."""
import collections,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;P=R/'.local-private'
rows=[json.loads(x) for x in (P/'QUESTION_AUDIT.jsonl').open(encoding='utf8')]
result={};items=[]
for name,relative in [('bounded_200','r135_bounded_eval200_20261111/evaluation'),('verified_200','r135_verified_eval200_20261111/evaluation')]:
 db=ROOT/relative/'runtime/logs/transcripts.sqlite';c=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True);counts=collections.Counter();unavail=collections.Counter()
 original={x['key']:x for x in map(json.loads,(ROOT/relative/'RESULTS.jsonl').open(encoding='utf8'))}
 for row in rows:
  if row['run']!=name or not any(e.get('stage')=='model_admission_denied' for e in row.get('model_calls',[])):continue
  m=json.loads(c.execute("select metadata_json from chat_messages where session_id=? and role='assistant' order by id desc limit 1",(original[row['key']]['session_id'],)).fetchone()[0]);events=m.get('decision_artifact',{}).get('request_context',{}).get('events',[])
  receipts=[]
  for e in events:
   if e.get('stage')!='model_admission_denied':continue
   a=e.get('admission') or {};safe={k:a.get(k) for k in ['llm_health_enabled','llm_health_allowed','llm_health_status','llm_health_kind','llm_health_failures','llm_health_cooldown_remaining_sec','llm_health_last_error_type','llm_health_failure_scope','llm_health_reason']}
   receipts.append({'stage':e['stage'],'model_stage':e.get('model_stage'),'http_attempted':e.get('http_attempted'),'reservation_consumed':e.get('reservation_consumed'),'admission':safe})
  statuses={str(x['admission'].get('llm_health_status')) for x in receipts};counts.update(statuses)
  if row['mode']=='pipeline:common_unavailable':unavail.update(statuses)
  items.append({'run':name,'key':row['key'],'question':row['question'],'mode':row['mode'],'receipts':receipts})
 c.close();result[name]={'denied_requests':sum(x['run']==name for x in items),'health_status_per_request_nonexclusive':dict(counts),'unavailable_health_status_per_request_nonexclusive':dict(unavail)}
(R/'ADMISSION_AUDIT.json').write_text(json.dumps({'runs':result,'source':'saved SQLite request_context.events only','not_codex_approval_rejection':True,'limits':'This identifies local application health gate status at the time. It does not prove model hardware was broken or that all future requests will be denied.'},ensure_ascii=False,indent=2),encoding='utf8')
(P/'ADMISSION_RECEIPTS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items),encoding='utf8');print(json.dumps(result))
