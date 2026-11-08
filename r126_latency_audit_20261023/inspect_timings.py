import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output'])
rows=[json.loads(s) for s in (OUT/'TIMINGS.jsonl').read_text('utf8').splitlines()]
for row in rows[-int(sys.argv[1] if len(sys.argv)>1 else 6):]:
 events=row['events'];http=row['http'];gen=[x for x in http if x['kind']=='model' and any(s in x['url'] for s in ['/api/chat','/api/generate'])]
 print(json.dumps({'q':row['question'],'wall':round(row['wall_sec'],3),'cpu':round(row['local_cpu_sec'],3),'model':[{'stage':x.get('stage'),'sec':round(x.get('total_sec',0),3),'tokens':x.get('eval_count'),'request_bytes':x.get('request_bytes')} for x in gen], 'spans':[{k:s.get(k) for k in ['name','duration_sec','parent']} for s in events if s['name'] in ['source.snapshot','index.from_snapshot','context.interpret','evidence.select','provider.fetch','answer.render_one','request.compile']], 'state':row['pipeline'].get('decision_artifact',{}).get('response_type')},ensure_ascii=False))
