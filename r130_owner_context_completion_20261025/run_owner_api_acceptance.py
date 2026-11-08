"""Existing owner50 through the actual final selected candidate API, LLM ON."""
import json,re,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent
config=json.loads((R/'PROCESS.json').read_text('utf8'));out=Path(config['output'])
source=json.loads((R/'OWNER_READ_AUDIT_LATEST.json').read_text('utf8'))
expected=[json.loads(s) for s in (Path(source['output'])/'RESULTS.jsonl').read_text('utf8').splitlines()]
def normalized(text):return re.sub(r'\s+','',re.sub(r'\[S\d+\]|[*#`]','',text)).casefold()
rows=[];errors=[]
with (out/'OWNER50_API_ACCEPTANCE.jsonl').open('x',encoding='utf8') as f:
 for e in expected:
  row={'number':e['number'],'question':e['question']};started=time.perf_counter()
  try:
   payload={'question':e['question'],'locale':'th','debug':True,'experimental_rag_fallback':True,'client_session_id':'r130-owner-'+uuid.uuid4().hex,'client_turn_id':'turn-'+uuid.uuid4().hex}
   req=urllib.request.Request(config['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
   with urllib.request.urlopen(req,timeout=195) as response:r=json.load(response)
   row.update(response=r,source_read_retained=normalized(e['answer']) in normalized(r.get('answer','')),validation_ok=r.get('validation_ok') is True,response_type=(r.get('decision_artifact') or {}).get('response_type'))
   row['partial_state_retained']=e['response_type']!='partial_answer' or row['response_type']=='partial_answer'
   row['passed']=row['source_read_retained'] and row['validation_ok'] and row['partial_state_retained'] and not r.get('timed_out')
  except Exception as exc:row.update(error=repr(exc),passed=False)
  row['wall_sec']=time.perf_counter()-started;rows.append(row)
  if not row['passed']:errors.append({'number':e['number'],'error':row.get('error'),'source_read_retained':row.get('source_read_retained'),'partial_state_retained':row.get('partial_state_retained')})
  f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  print(json.dumps({'number':e['number'],'passed':row['passed'],'wall_sec':round(row['wall_sec'],3)},ensure_ascii=False),flush=True)
summary={'all_passed':len(rows)==50 and not errors,'existing_questions':50,'new_questions':0,'experimental_llm_allowed':True,'model_not_forced_on_source_reads':True,'errors':errors,'partial_status_not_accuracy_metric':True,'fresh_semantic_benchmark':False,'max_wall_sec':max(r['wall_sec'] for r in rows)}
(out/'OWNER50_API_COMPLETE.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
if not summary['all_passed']:raise SystemExit(1)
