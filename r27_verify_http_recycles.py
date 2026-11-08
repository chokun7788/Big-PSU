import json,time,urllib.request
from pathlib import Path
report=Path(Path(__file__).with_name('r27_report_path.txt').read_text().strip())
base='http://127.0.0.1:8091'
initial=json.load(urllib.request.urlopen(base+'/health',timeout=3))
path=Path(initial['pipeline_workers']['performance']['path']);rows=[]
for attempt in range(20):
    payload={'question':'How many players are in a CS2 team?','locale':'en','experimental_allow_llm':True,'experimental_rag_fallback':True,'recent_history':[],'debug':True}
    start=time.perf_counter()
    response=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'}),timeout=25))
    rows.append({'attempt':attempt,'elapsed':time.perf_counter()-start,'response':response})
    assert '5 players' in response['answer'].splitlines()[0]
    events=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines()]
    if sum(e.get('event')=='worker_recycle' and e.get('status')=='promoted' for e in events)>=2:break
    time.sleep(.5)
else:raise AssertionError('second planned recycle did not promote a ready worker')
health=json.load(urllib.request.urlopen(base+'/health',timeout=3))
result={'requests':rows,'health':health,'events':[e for e in events if e.get('event')=='worker_recycle'],'promotions':sum(e.get('event')=='worker_recycle' and e.get('status')=='promoted' for e in events),'http_errors':0}
with (report/'verified_http_recycles.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'promotions':result['promotions'],'extra_probe_requests':len(rows),'http_errors':0}))
