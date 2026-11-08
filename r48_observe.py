import os,sys,json,time,uuid
from dataclasses import asdict
import r48_probe as p
sys.path.insert(0,str(p.p.ROOT));os.chdir(p.p.ROOT)
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_CHAT_LOG_DIR=str(p.OUT/'observations_logs'))
from app.pipeline.engine import answer_question_pipeline_debug as answer
raw=json.loads((p.OUT/'USER_INPUT_50.json').read_text(encoding='utf-8'))
dest=p.OUT/('ORIGINAL_50_OBSERVATIONS_'+uuid.uuid4().hex[:6]+'.jsonl')
for item in raw['items']:
 start=time.perf_counter();r=answer(item['question'],locale='th',experimental_allow_llm=False)
 record=dict(**item,answer_observed=r.answer,mode=r.mode,route=asdict(r.route),validation=asdict(r.validation),trace=[asdict(t) for t in r.trace],elapsed_sec=round(time.perf_counter()-start,4),evaluation='observation_only_not_a_correctness_pass')
 with dest.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print(item['number'],r.mode,flush=True)
print(dest)
