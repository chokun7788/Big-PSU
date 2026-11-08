import sys,os,json,threading,urllib.request
from pathlib import Path
from types import SimpleNamespace
from http.server import ThreadingHTTPServer
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from evaluate import score
from app.knowledge.common.owner_server import make_handler
store=t.CommonStore(t.DB);records=store.snapshot()['release']['records'];before=store.snapshot()['epoch']
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='1'
rows=json.loads((B/'DEVELOPMENT.json').read_text(encoding='utf-8'))
focus=[r for r in rows if r['style']=='clean_new' and r['kind'] in {'game','service','competition','procedure','live_binding','person'}]
out=B/'owner_preview_verified';out.mkdir(exist_ok=False);result=[]
server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(store,'r60-local-fixture','fixture',0));port=server.server_port
server.RequestHandlerClass=make_handler(store,'r60-local-fixture','fixture',port)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
  for c in focus:
   c=dict(c);c['rid']=t.rid(c['kind'],c['profile']);c['question']=records[c['rid']]['aliases'][c['lang']][0]+' '+c['phrase']
   req=urllib.request.Request(f'http://127.0.0.1:{port}/api/preview',data=json.dumps({'question':c['question'],'locale':c['lang']}).encode(),headers={'Content-Type':'application/json','Authorization':'Bearer r60-local-fixture'})
   with urllib.request.urlopen(req,timeout=30) as response:body=json.load(response)
   art=body['trace'];hits=[e for o in art.get('obligations',[]) for e in o.get('evidence_refs',[])]
   ans=SimpleNamespace(answer=body['answer'],decision_artifact=art,hits=hits,validation=SimpleNamespace(ok=not art.get('errors')))
   ok,why,quality=score(ans,c,records)
   r={**c,'passed':ok,'reasons':why,'quality':quality,'answer':body['answer'],'decision':art};result.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush();print(c['id']+' '+str(ok),flush=True)
finally:
 server.shutdown();server.server_close();thread.join(timeout=2)
summary={'cases':len(result),'passed':sum(r['passed'] for r in result),'failures':[r['id'] for r in result if not r['passed']],'actual_authenticated_http':True,'actual_llm':True,'epoch_unchanged':before==store.snapshot()['epoch'],'live_wordpress':False,'source_pointer_check':'trace obligations; preview response does not expose separate hits'}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary)
