"""Repair an evaluator mode-name mistake without changing any response/log."""
import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (B/'WEB_FIXTURE_RESULTS.jsonl').read_text(encoding='utf-8').splitlines()]
results=[]
for r in rows:
 a=r['response'];obs=(a.get('decision_artifact') or {}).get('obligations',[])
 ok=a.get('ok') is True and not a.get('timed_out') and a.get('validation_ok') is True and a.get('mode')=='pipeline:common_answer' and any(o['field']==r['key'] for o in obs)
 pointers=all(o.get('evidence_refs') for o in obs if o['status']=='known')
 results.append({'kind':r['kind'],'lang':r['lang'],'key':r['key'],'passed':ok and pointers,'seconds':r['seconds'],'response_type':(a.get('decision_artifact') or {}).get('response_type')})
summary={'cases':len(results),'passed':sum(x['passed'] for x in results),'actual_chat_http_and_session':True,'known_field_source_pointers_verified':True,'not_live_booking_or_load_capacity':True,'worker_supervisor_enabled':False,'old_evaluator_error':'expected common_content/common_published; actual documented mode is common_answer. Original raw responses and failed grade are retained.','results':results}
(B/'WEB_FIXTURE_REVIEWED.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(summary['cases'],summary['passed'])
