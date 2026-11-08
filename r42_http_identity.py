import json,time,uuid,urllib.request,urllib.error,threading,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
port=int(sys.argv[1]);rows=[]
def payload():return dict(question='What are the studio opening hours?',locale='en',debug=True,client_session_id='r42-identity-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex)
def request(p):
    t=time.perf_counter();req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(p).encode(),headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=40) as r:result=dict(status=r.status,response=json.load(r))
    except urllib.error.HTTPError as e:result=dict(status=e.code,response=json.load(e))
    result.update(payload=p,elapsed_sec=round(time.perf_counter()-t,4));return result
def consistent(records):
    good=[r['response'] for r in records if r['status']==200]
    return bool(good) and len({r['request_id'] for r in good})==1 and len({r['answer'] for r in good})==1 and all(r['conversation_state']['revision']==1 for r in good)
p=payload();records=[request(p),request(p)];rows.append(dict(id='duplicate-replay',passed=all(r['status']==200 for r in records) and consistent(records),records=records))
p=payload();barrier=threading.Barrier(2)
def concurrent(_):barrier.wait();return request(p)
with ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(concurrent,range(2)))
def retryable(r):return r['status']==503 or (r['status']==409 and r['response'].get('error')=='session_busy')
if any(retryable(r) for r in records):records.append(request(p))
rows.append(dict(id='concurrent-identical-turn',passed=all(r['status']==200 or retryable(r) for r in records) and sum(r['status']==200 for r in records)>=2 and consistent(records),records=records))
p=payload();records=[request(p),request({**p,'question':'How can I contact the studio?'})]
rows.append(dict(id='changed-input-same-turn-conflict',passed=records[0]['status']==200 and records[1]['status']==409 and records[1]['response'].get('error')=='client_turn_conflict',records=records))
with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=8) as r:health=json.load(r)
minor=sys.argv[2] if len(sys.argv)>2 else '2'
dest=OUT/(f'final_r42_{minor}_identity_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]+'_summary.json')
with dest.open('x',encoding='utf-8') as f:json.dump(dict(executed_cases=len(rows),requests=sum(len(r['records']) for r in rows),passed=sum(r['passed'] for r in rows),health=health,results=rows),f,ensure_ascii=False,indent=2)
for r in rows:print(r['id'],r['passed'],[t['status'] for t in r['records']])
print(dest.name)
sys.exit(int(not all(r['passed'] for r in rows)))
