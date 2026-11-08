"""Actual HTTP acceptance of previously source-reviewed repair cases."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));out=Path(c['output'])
cases=json.loads((R.parent/'r131_diagnostic_review_20261025/CONSOLIDATED_SOURCE_REVIEW.json').read_text('utf8'))['cases']
prefixes=['f6a75fef','934b6162','9749c57f','cc40820b','0c25d981','06563f1a','b9fa6734','7e3ed641','db84ae34','4dc69c73']
rows=[]
with (out/'REPAIR_ACCEPTANCE.jsonl').open('x',encoding='utf8') as stream:
 for prefix in prefixes:
  item=next(x for x in cases if x['key'].startswith(prefix));q=item['question'];started=time.perf_counter();row={'key':item['key'],'question':q}
  try:
   payload={'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':'r132-repair-'+uuid.uuid4().hex,'client_turn_id':'turn-'+uuid.uuid4().hex}
   request=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
   with urllib.request.urlopen(request,timeout=195) as f:response=json.load(f)
   art=response.get('decision_artifact') or {};flow=art.get('domain_flow') or {}
   claims=flow.get('claims') or art.get('claims') or []
   selected={x['record_id'] for x in claims if x.get('record_id')}|set((art.get('query_plan') or {}).get('record_ids') or [])
   row.update(response=response,selected_record_ids=sorted(selected),transport_and_validation_ok=response.get('validation_ok') is True and not response.get('timed_out'),semantic_review='pending_agent_source_review')
  except Exception as e:row.update(error=repr(e),transport_and_validation_ok=False)
  row['elapsed_sec']=time.perf_counter()-started;rows.append(row);stream.write(json.dumps(row,ensure_ascii=False)+'\n');stream.flush()
  print(json.dumps({'key':prefix,'elapsed_sec':row['elapsed_sec'],'validation_ok':row.get('transport_and_validation_ok'),'source_ids':row.get('selected_record_ids'),'answer':row.get('response',{}).get('answer','')[:650],'error':row.get('error')},ensure_ascii=False),flush=True)
result={'complete':len(rows)==len(prefixes),'requests':len(rows),'transport_validation_failures':[x['key'] for x in rows if not x['transport_and_validation_ok']],'semantic_review_complete':False,'production_installed':False}
(out/'REPAIR_ACCEPTANCE_COMPLETE.json').write_text(json.dumps(result,indent=2),'utf8')
assert not result['transport_validation_failures']
