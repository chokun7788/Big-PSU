import json,collections
from pathlib import Path
import analyze
B=Path(__file__).resolve().parent
samples=[];counts=collections.Counter()
for mode in ('legacy','common'):
 path=B/'model_matrix_memo_counter'/(mode+'_RESULTS.jsonl.gz')
 for r in analyze.read(path):
  for t in r.get('result',{}).get('trace',[]):
   serialized=json.dumps(t,ensure_ascii=False)
   if any(w in serialized.lower() for w in ('ollama','embedding','llm','semantic')):
    counts[mode+':'+str(t.get('stage'))+':'+str(t.get('decision'))]+=1
    if len(samples)<20:samples.append({'mode':mode,'question':r['question'],'trace':t})
(B/'MODEL_CALL_EVIDENCE_SAMPLE.json').write_text(json.dumps({'counts':counts,'samples':samples,'scope':'current memo_counter arm only, trace labels do not themselves prove HTTP200 or factual correctness'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'counts':counts,'samples':samples[:3]},ensure_ascii=False))
