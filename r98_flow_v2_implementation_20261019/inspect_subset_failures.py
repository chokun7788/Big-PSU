from pathlib import Path
import gzip,json,sys
R=Path(__file__).resolve().parent;output=[]
tag=sys.argv[1] if len(sys.argv)>1 else 'subset01'
for path in (R/tag).glob('RESULTS_*.jsonl.gz'):
 with gzip.open(path,'rt',encoding='utf8') as f:
  for line in f:
   row=json.loads(line);failed=[g for g in row['grades'] if g.get('partitions',{}).get('content')]
   if failed:
    r=row['result'];a=r.get('decision_artifact') or {};output.append({'key':row['key'],'question':row['question'],'locale':row['requested_locale'],'answer':r.get('answer'),'mode':r.get('mode'),'artifact':a,'failed_grades':failed})
(R/tag/'CONTENT_REVIEW.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),'utf8')
for r in output:print(json.dumps({'q':r['question'],'answer':r['answer'][:430],'mode':r['mode'],'failures':[g['partitions']['content'] for g in r['failed_grades']]},ensure_ascii=False))
