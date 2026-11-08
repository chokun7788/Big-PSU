import json,urllib.request,urllib.error,uuid,time,sys
from pathlib import Path
OUT=Path((Path(__file__).parent/'two_turn_current_path.txt').read_text(encoding='utf-8'))
PORT=int(sys.argv[1]) if len(sys.argv)>1 else 8093
CASES=json.loads((OUT/'cases.json').read_text(encoding='utf-8'))
stamp=time.strftime('%H%M%S');raw=OUT/f'api_{PORT}_{stamp}.jsonl'
def ask(q,case,session,ack=''):
    payload=dict(question=q,locale=case['locale'],client_session_id=session,client_turn_id=str(uuid.uuid4()),last_seen_response_id=ack,debug=True)
    start=time.perf_counter()
    request=urllib.request.Request(f'http://127.0.0.1:{PORT}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=35) as r:status=r.status;body=json.load(r)
    except urllib.error.HTTPError as r:status=r.code;body=json.load(r)
    record=dict(case_id=case['id'],payload=payload,status=status,elapsed_sec=round(time.perf_counter()-start,3),response=body)
    with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    return record
summary=[]
for case in CASES:
    session='two-turn-'+str(uuid.uuid4())
    first=ask(case['initial'],case,session)
    second=ask(case['choice'],case,session,first['response'].get('request_id',''))
    r=second['response'];text=r.get('answer','').casefold()
    entry=dict(case=case,first_mode=first['response'].get('mode'),first_category=first['response'].get('route_category'),second_mode=r.get('mode'),second_category=r.get('route_category'),resolved_question=r.get('resolved_question'),second_answer=r.get('answer'),latency_sec=second['elapsed_sec'])
    # Conservative route/content checks; inspect failures and first-turn wording separately.
    entry['content_present']=all(s.casefold() in text for s in case['expected_contains'])
    entry['category_match']=r.get('route_category')==case['expected_category'] or (case['expected_category']=='game_control' and 'control' in r.get('route_category',''))
    entry['full_scope']=not case['full_detail'] or (r.get('rule_coverage') or {}).get('detail_level')=='full_sections'
    entry['passed']=second['status']==200 and entry['content_present'] and entry['category_match'] and entry['full_scope']
    summary.append(entry)
    print(case['id'],entry['first_mode'],'->',entry['second_mode'],'PASS' if entry['passed'] else 'REVIEW',flush=True)
(OUT/f'summary_{PORT}_{stamp}.json').write_text(json.dumps(dict(port=PORT,cases=len(summary),passed=sum(x['passed'] for x in summary),raw=raw.name,results=summary),ensure_ascii=False,indent=2),encoding='utf-8')
print('Passed',sum(x['passed'] for x in summary),'/',len(summary),flush=True)
