import json,collections,sqlite3,zlib
from pathlib import Path
B=Path(__file__).resolve().parent;summary={};samples=[]
for arm in ('offline_01','llm_01'):
 p=B/('MATRIX_'+arm+'.jsonl')
 if not p.exists():continue
 rows=[json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]
 counts=collections.Counter();reasons=collections.Counter();methods=collections.Counter();locales=collections.defaultdict(collections.Counter)
 for r in rows:
  counts['requests']+=1
  if r.get('exception'):counts['exceptions']+=1;reasons[r['exception']]+=1
  result=r.get('result') or {};methods[result.get('mode','no_response')]+=1
  for g in r['grades']:
   counts['grades']+=1;counts['strict_pass']+=bool(g['passed']);locales[r['requested_locale']]['grades']+=1;locales[r['requested_locale']]['strict_pass']+=bool(g['passed'])
   part=g.get('r66_partitions',{});content=part.get('content_source_validation',[]);protocol=part.get('protocol',[]);perf=part.get('performance',[])
   if content:counts['content_source_validation_fail_grades']+=1
   elif perf:counts['performance_only_fail_grades']+=1
   elif protocol:counts['protocol_only_fail_grades']+=1
   if g.get('content_asserted'):counts['content_asserted_grades']+=1;counts['content_partition_pass']+=not content
   reasons.update(content)
  if any(g.get('r66_partitions',{}).get('content_source_validation') for g in r['grades']) or r.get('exception'):
   samples.append({'arm':arm,'key':r['key'],'question':r['question'],'locale':r['requested_locale'],'exception':r.get('exception'),'answer':result.get('answer'),'plan':result.get('decision_artifact',{}).get('query_plan'),'failures':[g for g in r['grades'] if not g['passed']]})
 summary[arm]={'counts':dict(counts),'locales':{k:dict(v) for k,v in locales.items()},'modes':dict(methods),'content_failure_reasons':reasons.most_common()}
out=B/('MATRIX_ANALYSIS_'+str(len(list(B.glob('MATRIX_ANALYSIS*.json')))+1)+'.json');out.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
samplefile=B/('MATRIX_FAILURES_'+str(len(list(B.glob('MATRIX_FAILURES*.json')))+1)+'.json');samplefile.write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:{'counts':v['counts'],'top_reasons':v['content_failure_reasons'][:10]} for k,v in summary.items()},ensure_ascii=False,indent=2))
print('SAMPLES')
for x in samples[:12]:print(json.dumps({'arm':x['arm'],'q':x['question'],'answer':str(x['answer'])[:350],'exception':x['exception'],'failure':[[g['file'],g.get('r66_partitions')] for g in x['failures']]},ensure_ascii=False))
