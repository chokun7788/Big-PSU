"""HTTP owner preview and actual chat pipeline, immutable DEMO database only."""
import sys,os,json,threading,secrets,urllib.request,concurrent.futures,traceback
from pathlib import Path
from http.server import ThreadingHTTPServer
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
import integration as old
from app.knowledge.common.owner_server import make_handler
from app.pipeline.engine import answer_question_pipeline_debug
os.environ['PSU_KNOWLEDGE_DB']=str(t.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='1'
snap=t.CommonStore(t.DB).snapshot();records=snap['release']['records'];qs=old.selected(records)
mode=sys.argv[1];out=B/mode;out.mkdir(exist_ok=False);results=[]
if mode.startswith('http'):
    token=secrets.token_urlsafe(30);server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(t.CommonStore(t.DB),token,t.ACTOR,0));port=server.server_port
    server.RequestHandlerClass=make_handler(t.CommonStore(t.DB),token,t.ACTOR,port)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    def one(c):
        req=urllib.request.Request(f'http://127.0.0.1:{port}/api/preview',data=json.dumps({'question':c['question'],'locale':c['lang'],'history':c['history']}).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
        try:
            with urllib.request.urlopen(req,timeout=40) as r:data=json.load(r);status=r.status
            ok,why=old.http_score(data,c,records);return {**c,'passed':ok,'reasons':why,'http_status':status,'answer':data['answer'],'decision':data['trace']}
        except Exception:return {**c,'passed':False,'exception':traceback.format_exc()}
else:
    def one(c):
        try:
            ans=answer_question_pipeline_debug(c['question'],locale=c['lang'],recent_history=c['history'],experimental_allow_llm=False,experimental_rag_fallback=False,global_timeout_sec=30)
            ok,why=t.prior.score(ans,c,records);return {**c,'passed':ok,'reasons':why,'answer':ans.answer,'decision':ans.decision_artifact,'mode':ans.mode}
        except Exception:return {**c,'passed':False,'exception':traceback.format_exc()}
try:
    with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4 if mode.startswith('http') else 1) as pool:
        for n,row in enumerate(pool.map(one,qs),1):
            f.write(json.dumps(row,ensure_ascii=False)+'\n');results.append(row)
            if n%40==0:f.flush();print(mode+' '+str(n)+'/'+str(len(qs)),flush=True)
finally:
    if mode.startswith('http'):server.shutdown();server.server_close()
summary={'total':len(results),'passed':sum(r['passed'] for r in results),'http_200':sum(r.get('http_status')==200 for r in results),'failed':[r['id'] for r in results if not r['passed']],'llm':False,'live_wordpress':False,'isolated_demo_only':True,'database_epoch_unchanged':t.CommonStore(t.DB).still_current(snap),'actual_pipeline' : not mode.startswith('http')}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary),flush=True)
