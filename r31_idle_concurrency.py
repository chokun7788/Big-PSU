import json,urllib.request,uuid,time,sys,concurrent.futures
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2]
health=json.load(urllib.request.urlopen(base+'/health',timeout=8));assert health['runtime']['version']=='2026.10.02-question-target-content-r31'
def ask(i):
    loc='en' if i%2==0 else 'th';q='What games are available?' if loc=='en' else 'มีเกมอะไรบ้าง';payload={'question':q,'locale':'auto','recent_history':[],'client_session_id':'r30-idle-'+uuid.uuid4().hex,'debug':False,'experimental_allow_llm':False,'experimental_rag_fallback':False};start=time.perf_counter()
    try:
        with urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=20) as response:
            d=json.load(response);h=response.headers.get('Content-Language');status=response.status
    except urllib.error.HTTPError as e:status=e.code;h=e.headers.get('Content-Language');d=json.loads(e.read().decode())
    except Exception as e:status=0;h=None;d={'error':repr(e)}
    errors=[]
    if status!=200:errors.append('http:'+str(status))
    else:
        if h!=loc or d.get('language',{}).get('effective')!=loc:errors.append('locale_mismatch')
        if '42' not in d.get('answer',''):errors.append('catalog_count_missing')
    return {'id':i,'expected_locale':loc,'http_status':status,'content_language':h,'elapsed':time.perf_counter()-start,'passed':not errors,'failures':errors,'response':d}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:rows=list(pool.map(ask,range(10)))
with (r/(run+'_concurrency.json')).open('x',encoding='utf-8') as out:json.dump({'url':base,'scope':'idle ten concurrent requests; locale/count oracle only, not slow WordPress load SLA','health':health,'total':len(rows),'passed':sum(x['passed'] for x in rows),'rows':rows},out,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(rows),'passed':sum(x['passed'] for x in rows),'failed':[(x['id'],x['failures']) for x in rows if not x['passed']]}),flush=True)
