import json,urllib.request,urllib.error
from r27_fixture import PROJECT,REPORT
package=PROJECT/'owner_local_delivery_20261001_competition_contract_r27_ready/PSU_Esports_Chatbot_Local'
rows=[json.loads(x) for x in (REPORT/'http_candidate_320_details.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
fixture=json.loads((REPORT/'content_contract_fixture_v2.json').read_text(encoding='utf-8'))['cases']
print(json.dumps({'finished':len(rows),'last':rows[-1]['id'],'next':fixture[len(rows)]['question']},ensure_ascii=False))
performance=next((package/'data/logs/performance').glob('pipeline_*.jsonl'))
events=[json.loads(x) for x in performance.read_text(encoding='utf-8').splitlines() if x.strip()]
interesting=[x for x in events if any(term in json.dumps(x) for term in ('timeout','restart','crash','worker_exit','busy','terminate'))]
with (REPORT/'candidate_http_503_investigation.json').open('x',encoding='utf-8') as f:json.dump({'partial_completed':len(rows),'next_case':fixture[len(rows)],'events':interesting,'performance_log':str(performance)},f,ensure_ascii=False,indent=2)
for x in interesting[-14:]:print(json.dumps(x,ensure_ascii=False)[:1900])
payload={'question':'What are the tournament rules?','locale':'en','experimental_allow_llm':True,'debug':True}
try:
    raw=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8091/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'}),timeout=25))
    result={'http_status':200,'response':raw}
except urllib.error.HTTPError as e:result={'http_status':e.code,'response':json.loads(e.read().decode())}
with (REPORT/'candidate_after_503_probe.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'http_status':result['http_status'],'mode':result['response'].get('mode'),'message':result['response'].get('message')},ensure_ascii=False))
