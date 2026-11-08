import json, urllib.request, uuid, time, sys
from pathlib import Path
from two_turn_grader_r39 import grade
from r40_targeted_probe import OUT, BASE
port=int(sys.argv[1])
cases=json.loads((BASE/'two_turn_choices_20261005_000041/cases.json').read_text(encoding='utf-8'))
stamp=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
raw=OUT/f'adjacent_http_{stamp}_raw.jsonl'; results=[]
for c in cases:
    session='r40-adjacent-'+uuid.uuid4().hex; ack=''; records=[]
    for q in (c['initial'],c['choice']):
        payload=dict(question=q,locale=c['locale'],client_session_id=session,client_turn_id=uuid.uuid4().hex,last_seen_response_id=ack,debug=True)
        start=time.perf_counter()
        req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=40) as r:record=dict(case_id=c['id'],payload=payload,status=r.status,response=json.load(r),elapsed_sec=round(time.perf_counter()-start,4))
        with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
        ack=record['response'].get('request_id','');records.append(record)
    result=grade(c,records[0]['response'],records[1]['response'],records[1]['status'])
    result['records']=records; results.append(result)
    print(c['id'],'PASS' if result['passed'] else 'FAIL',[k for k,v in result['checks'].items() if not v],flush=True)
with (OUT/f'adjacent_http_{stamp}_summary.json').open('x',encoding='utf-8') as f:
    json.dump(dict(port=port,executed_cases=len(results),requests=2*len(results),passed=sum(r['passed'] for r in results),raw_file=raw.name,results=results),f,ensure_ascii=False,indent=2)
print('SUMMARY',sum(r['passed'] for r in results),'/',len(results),flush=True)
