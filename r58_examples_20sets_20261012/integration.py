"""Real owner HTTP handler and real chat pipeline, in isolated test process."""
import experiment as t
import os,json,time,threading,secrets,urllib.request,concurrent.futures,traceback
from http.server import ThreadingHTTPServer
from app.knowledge.common.owner_server import make_handler
os.environ['PSU_KNOWLEDGE_DB']=str(t.DB)
os.environ['PSU_COMMON_ALLOW_DEMO']='1'
def selected(records):
    focus={'resource','service','audience','game_mode','closure','competition_rule','game','live_binding'}
    return [c for c in t.cases(records) if c['rid'].startswith('demo20_') and c['rid'].endswith(('_01','_20')) and (c['style']=='all_fields' or c['kind'] in focus and c['style'] in {'natural','paraphrase','followup','multi_field'})]
def http_score(r,c,records):
    trace=r.get('trace') or {};why=[]
    if trace.get('response_type') not in {'answer','list'}:why.append('response_'+str(trace.get('response_type')))
    for key in c['expected_fields']:
        f=records[c['rid']]['fields'][key];obs=[x for x in trace.get('obligations',[]) if x.get('record_id')==c['rid'] and x.get('field')==key]
        if not obs:why.append('missing_field:'+key);continue
        if obs[0]['status']!=f['status']:why.append('wrong_status:'+key)
        if f['status']=='known':
            for v in t.prior.expected_leaves(f['value'],c['lang'],records,key):
                if v and v not in r['answer']:why.append('missing_content:'+key)
        else:
            v=('Not applicable' if f['status']=='not_applicable' else 'Not yet confirmed') if c['lang']=='en' else ('ไม่เกี่ยวข้อง' if f['status']=='not_applicable' else 'ยังไม่มีข้อมูลยืนยัน')
            if v not in r['answer']:why.append('missing_unknown_wording:'+key)
    return not why,why
def main():
    store=t.CommonStore(t.DB);snap=store.snapshot();records=snap['release']['records'];qs=selected(records)
    if not snap['allow_demo']:raise RuntimeError('DEMO only')
    mode=t.sys.argv[1];rows=[]
    if mode.startswith('http'):
        token=secrets.token_urlsafe(30)
        server=ThreadingHTTPServer(('127.0.0.1',0),make_handler(store,token,t.ACTOR,0));port=server.server_port
        server.RequestHandlerClass=make_handler(store,token,t.ACTOR,port)
        threading.Thread(target=server.serve_forever,daemon=True).start()
        def one(c):
            req=urllib.request.Request(f'http://127.0.0.1:{port}/api/preview',data=json.dumps({'question':c['question'],'locale':c['lang'],'history':c['history']}).encode(),headers={'Content-Type':'application/json','Authorization':'Bearer '+token})
            try:
                with urllib.request.urlopen(req,timeout=40) as response:r=json.load(response);status=response.status
                ok,why=http_score(r,c,records)
                return {**c,'http_status':status,'passed':ok,'reasons':why,'answer':r['answer'],'decision':r.get('trace')}
            except Exception:return {**c,'passed':False,'reasons':['transport_exception'],'exception':traceback.format_exc()}
        try:
            with (t.B/(mode.upper()+'_RESULTS.jsonl')).open('x',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                for n,r in enumerate(pool.map(one,qs),1):
                    rows.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n')
                    if n%40==0:f.flush();print('HTTP '+str(n)+'/'+str(len(qs)),flush=True)
        finally:server.shutdown();server.server_close()
    elif mode=='pipeline':
        from app.pipeline.engine import answer_question_pipeline_debug
        gate=t.CommonAnswerer(t.OneReleaseStore(t.DB).freeze())
        with (t.B/'PIPELINE_RESULTS.jsonl').open('x',encoding='utf-8') as f:
            for n,c in enumerate(qs,1):
                if gate.answer(c['question'],locale=c['lang'],history=c['history'],at=t.AT) is None:r={**c,'passed':False,'reasons':['common_miss'],'legacy_skipped':True,'answer':None}
                else:
                    try:
                        ans=answer_question_pipeline_debug(c['question'],locale=c['lang'],recent_history=c['history'],experimental_allow_llm=False,experimental_rag_fallback=False,global_timeout_sec=30)
                        ok,why=t.prior.score(ans,c,records);r={**c,'passed':ok,'reasons':why,'answer':ans.answer,'decision':ans.decision_artifact,'mode':ans.mode,'legacy_skipped':False}
                    except Exception:r={**c,'passed':False,'reasons':['exception'],'exception':traceback.format_exc()}
                rows.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n')
                if n%40==0:f.flush();print('PIPELINE '+str(n)+'/'+str(len(qs)),flush=True)
    else:raise RuntimeError('http or pipeline')
    bystyle={}
    for style in sorted({r['style'] for r in rows}):
        rs=[r for r in rows if r['style']==style];bystyle[style]={'pass':sum(r['passed'] for r in rs),'fail':sum(not r['passed'] for r in rs)}
    summary={'queries':len(rows),'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'http_200':sum(r.get('http_status')==200 for r in rows),'legacy_skipped':sum(r.get('legacy_skipped',False) for r in rows),'styles':bystyle,'isolated_demo_only':True,'database_unchanged':store.still_current(snap),'llm':False,'wordpress':False,'checks':'HTTP obligations/full content/status wording, no hit evidence exposed by this API' if mode.startswith('http') else 'actual pipeline and obligations/content/evidence; legacy fallback skipped only on common miss'}
    t.filejson(mode.upper()+'_SUMMARY.json',summary);print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
