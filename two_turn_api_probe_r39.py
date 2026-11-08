import json,urllib.request,uuid,time,sys
from two_turn_grader_r39 import OUT,grade
PORT=int(sys.argv[1]);file=sys.argv[2] if len(sys.argv)>2 else 'cases.json'
cases=json.loads((OUT/file).read_text(encoding='utf-8'))
stamp=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
raw=OUT/f'api_{PORT}_{stamp}.jsonl';results=[]
def ask(q,case,session,ack=''):
    payload=dict(question=q,locale=case['locale'],client_session_id=session,client_turn_id=str(uuid.uuid4()),last_seen_response_id=ack,debug=True)
    start=time.perf_counter()
    request=urllib.request.Request(f'http://127.0.0.1:{PORT}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=40) as r:status=r.status;body=json.load(r)
    record=dict(case_id=case['id'],payload=payload,status=status,elapsed_sec=round(time.perf_counter()-start,3),response=body)
    with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    return record
for case in cases:
    session='r39-'+str(uuid.uuid4())
    a=ask(case['initial'],case,session);b=ask(case['choice'],case,session,a['response'].get('request_id',''))
    result=grade(case,a['response'],b['response'],b['status']);result['latency_sec']=b['elapsed_sec'];results.append(result)
    print(case['id'],result['first_mode'],'->',result['second_mode'],'PASS' if result['passed'] else 'FAIL',flush=True)
report=dict(port=PORT,case_file=file,raw=raw.name,conversations=len(results),requests=len(results)*2,passed=sum(x['passed'] for x in results),results=results)
(OUT/f'api_summary_{PORT}_{stamp}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS',report['passed'],'/',len(results),flush=True)
