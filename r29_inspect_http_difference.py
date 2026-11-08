import json,urllib.request,uuid
from pathlib import Path
report=Path(Path(__file__).with_name('r29_report_path.txt').read_text(encoding='utf-8').strip())
case=next(r for r in map(json.loads,(report/'http_noise36_details.jsonl').read_text(encoding='utf-8').splitlines()) if r['id']=='MASTER-GT-EN-03708')
reference=next(r for r in map(json.loads,(report/'pipeline31_C_details.jsonl').read_text(encoding='utf-8').splitlines()) if r['id']==case['id'])
q=reference['clean']['question']
payload={'question':q,'locale':'en','recent_history':[],'client_session_id':'r29-clean-'+uuid.uuid4().hex,'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
response=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8091/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'}),timeout=30))
with (report/'http_safe_unknown_clean_probe.json').open('x',encoding='utf-8') as f:json.dump({'question':q,'clean_response':response,'noisy_response':case['response']},f,ensure_ascii=False,indent=2)
print(json.dumps({k:response.get(k) for k in ('answer','mode','route_category','validation_ok','hits')},ensure_ascii=False))
for t in case['response'].get('trace',[]):
    if t.get('stage') in ('formatting','validation','experimental_fallback','english_render','rag_llm','finalization'):
        print(json.dumps(t,ensure_ascii=False))
