from pathlib import Path
import json, time, urllib.request, uuid

R = Path(r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003')
W = Path(__file__).parent
records = []
def get(path):
    with urllib.request.urlopen('http://127.0.0.1:8091'+path,timeout=6) as f:
        return f.status, f.read()
for path in ['/', '/app.js', '/styles.css', '/health']:
    status, body = get(path)
    assert status == 200 and body
    records.append({'path':path,'status':status,'bytes':len(body)})
for q, locale in [('What games can I compete in?', 'en'), ('กฏตอนแข่ง tekken 8 มีอะไรมั่ง','th')]:
    payload = dict(question=q,locale=locale,client_session_id='ready-relocation-'+uuid.uuid4().hex,recent_history=[],debug=True,experimental_rag_fallback=True)
    request = urllib.request.Request('http://127.0.0.1:8091/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    start=time.perf_counter()
    with urllib.request.urlopen(request,timeout=35) as f: result=json.load(f)
    if locale=='en': assert result['route_intent']=='competition_rulebook_catalog'
    else: assert result['route_category']=='competition_rules' and all('competition_rules_tekken8_' in s['url'] for s in result['sources'])
    assert result['answer'] and not result.get('timed_out')
    records.append({'question':q,'result':result,'elapsed_sec':round(time.perf_counter()-start,3),'passed':True})
out = W / ('ready_relocation_'+time.strftime('%Y%m%d_%H%M%S')+'.json')
with out.open('x',encoding='utf-8') as f:json.dump(records,f,ensure_ascii=False,indent=2)
print(json.dumps({'static_checks':4,'questions':2,'passed':True,'log':str(out)},ensure_ascii=False),flush=True)
