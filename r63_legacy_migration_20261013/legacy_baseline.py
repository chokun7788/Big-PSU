"""Read-only old pipeline comparison, isolated knowledge/log paths, LLM disabled."""
import os,json,sys,shutil,time,dataclasses
from pathlib import Path
OUT=Path(sys.argv[1]).resolve();ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT))
db=OUT/'legacy_baseline.sqlite'
if db.exists():raise SystemExit('Baseline run already exists; preserve it')
shutil.copy2(OUT/'before.sqlite',db)
os.environ.update(PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_DIR=str(OUT/'legacy_logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'legacy_logs/transcripts.sqlite'),PSU_SEMANTIC_RETRIEVAL_ENABLED='0')
from app.runtime.pipeline_answer import answer_question_pipeline_debug
cases=json.loads((OUT/'DRAFT_QUESTIONS.json').read_text(encoding='utf-8'))['cases'];results=[]
for case in cases:
 start=time.perf_counter()
 try:
  result=answer_question_pipeline_debug(case['question'],locale='th')
  payload=dataclasses.asdict(result) if dataclasses.is_dataclass(result) else result
  row={'question':case['question'],'old_response':payload,'new_draft_answer':case['answer'],'expected_original':case.get('expected_original'),'expected_curated':case.get('expected_curated'),'seconds':time.perf_counter()-start}
 except Exception as e:row={'question':case['question'],'error':str(e),'new_draft_answer':case['answer']}
 results.append(row)
 with (OUT/'OLD_VS_DRAFT.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'cases':len(results),'runtime_errors':sum('error' in r for r in results),'comparison':'actual old pipeline vs draft preview with LLM disabled; response equality is not correctness'},ensure_ascii=False))
