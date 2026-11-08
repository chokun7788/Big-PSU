"""One frozen acceptance lane, 37 source preconditions × 3 locales × 4 forms."""
import os,sys,json,traceback,hashlib,time,dataclasses
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';tag=sys.argv[1];T=R/'verification'/tag;T.mkdir(parents=True,exist_ok=False)
sys.path[:0]=[str(S),str(R)]
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-20T12:00:00+07:00')
from scenario_support import Fixture
from acceptance_cases import QUESTIONS,variants,execute
jobs=json.loads((R/'BATCH_JOBS.json').read_text('utf8'));before=hashlib.sha256((R/'fixtures/BASE_SYNTHETIC.sqlite').read_bytes()).hexdigest();rows=[];started=time.perf_counter()
for job in jobs:
 f=None;t=time.perf_counter()
 try:
  f=Fixture.clone(T/job['id']/'SYNTHETIC_ONLY.sqlite',R/'fixtures/BASE_SYNTHETIC.sqlite')
  result,checks=execute(job['scenario'],f,job['question'],job['locale'])
  row={**job,'passed':all(c['passed'] for c in checks),'checks':checks,'elapsed_sec':time.perf_counter()-t,
    'turns':f.results,'model_http_calls':f.calls,'model_protocol_simulated':job['scenario']=='C31','live_provider_simulated':True}
 except Exception as e:
  row={**job,'passed':False,'phase':'fixture_or_execution_exception','exception':type(e).__name__,'error':str(e),'traceback':traceback.format_exc(),
    'turns':f.results if f else [],'model_http_calls':f.calls if f else [],'elapsed_sec':time.perf_counter()-t}
 rows.append(row)
 with (T/'RESULTS.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 progress={'completed':len(rows),'total':len(jobs),'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows),'elapsed_sec':round(time.perf_counter()-started,2),'running':len(rows)!=len(jobs)}
 (T/'PROGRESS.json').write_text(json.dumps(progress,indent=2),'utf8')
 if len(rows)%12==0:print(progress,flush=True)
summary={**progress,'count':len(rows),'scenarios':len({x['scenario'] for x in rows}),'model_calls':sum(len(x['model_http_calls']) for x in rows),
 'original_fixture_unchanged':hashlib.sha256((R/'fixtures/BASE_SYNTHETIC.sqlite').read_bytes()).hexdigest()==before,
 'exceptions':sum('exception' in x for x in rows),'failed_case_ids':[x['id'] for x in rows if not x['passed']],
 'not_independent_semantic_adjudication':True,'live_provider':'simulated','llm_enabled':True}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed'] or not summary['original_fixture_unchanged']))
