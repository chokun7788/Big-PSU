import json,urllib.request,urllib.error,time,concurrent.futures,uuid
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip())
def ask(base,q,locale='auto'):
    t=time.perf_counter();payload={'question':q,'locale':locale,'recent_history':[],'client_session_id':'r30-'+uuid.uuid4().hex,'experimental_allow_llm':False,'experimental_rag_fallback':True,'debug':True}
    try:
        with urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25) as response:
            raw=json.load(response);return {'status':response.status,'content_language':response.headers.get('Content-Language'),'elapsed':time.perf_counter()-t,'response':raw}
    except urllib.error.HTTPError as e:return {'status':e.code,'elapsed':time.perf_counter()-t,'error_body':e.read().decode('utf-8')}
    except Exception as e:return {'status':None,'elapsed':time.perf_counter()-t,'exception':type(e).__name__+':'+str(e)}
rows=[]
for version,base in [('r29','http://127.0.0.1:8090'),('r30-F','http://127.0.0.1:8091')]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        queries=[('What games are available?','en') if i%2==0 else ('มีเกมอะไรบ้าง','th') for i in range(10)]
        futures=[pool.submit(ask,base,q) for q,l in queries]
        results=[f.result() for f in futures]
    rows.append({'version':version,'no_other_api_test_running':True,'large_direct_sweep_active':True,'results':results,'http_200':sum(v['status']==200 for v in results),'language_mismatches':sum(v['status']==200 and v['content_language']!=queries[i][1] for i,v in enumerate(results))})
    print(json.dumps({'version':version,'http_200':rows[-1]['http_200'],'language_mismatches':rows[-1]['language_mismatches']}),flush=True)
with (r/'api_concurrency_comparison.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
probes=[]
for locale in ('auto','th','en'):
    q='The Last of Us Part I / Part II ราคาเท่าไหร่';result=ask('http://127.0.0.1:8091',q,locale)
    probes.append({'q':q,'requested_locale':locale,**result})
with (r/'auto_locale_mixed_title_probe.json').open('x',encoding='utf-8') as f:json.dump(probes,f,ensure_ascii=False,indent=2)
print(json.dumps([{'locale':x['requested_locale'],'mode':x.get('response',{}).get('mode'),'answer':x.get('response',{}).get('answer')} for x in probes],ensure_ascii=False),flush=True)
