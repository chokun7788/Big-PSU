"""Actual HTTP preview and actual chat pipeline, using only the isolated demo DB."""
import os,sys,json,time,urllib.request,concurrent.futures,collections,traceback
from pathlib import Path
import build_and_test as task
BASE=task.BASE
os.environ['PSU_KNOWLEDGE_DB']=str(task.DB)
os.environ['PSU_COMMON_ALLOW_DEMO']='1'
def api_checks():
    session=json.loads((BASE/'demo-owner-session.json').read_text(encoding='utf-8'));port=session['port'];token=session['url'].split('#token=',1)[1]
    def request(path,body=None):
        data=json.dumps(body).encode() if body is not None else None
        req=urllib.request.Request(f'http://127.0.0.1:{port}'+path,data=data,headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)
    store=task.CommonStore(task.DB);snap=store.snapshot();records=snap['release']['records']
    qs=[c for c in task.cases(records) if c['style']=='all_fields'];results=[]
    def one(c):
        start=time.perf_counter();r=request('/api/preview',{'question':c['question'],'locale':c['lang']});trace=r.get('trace') or {};obs=trace.get('obligations',[]);why=[]
        if not r.get('demo_only') or not r['answer'].startswith('ข้อมูลตัวอย่างแยกเท่านั้น'):why.append('missing_demo_warning')
        for key in c['expected_fields']:
            if not any(o.get('record_id')==c['rid'] and o.get('field')==key for o in obs):why.append('missing_field:'+key)
            f=records[c['rid']]['fields'][key]
            if f['status']=='known':
                for leaf in task.expected_leaves(f['value'],c['lang'],records,key):
                    if leaf and leaf not in r['answer']:why.append('missing_content:'+key+':'+leaf)
        return {**c,'passed':not why,'reasons':why,'answer':r['answer'],'decision':trace,'elapsed_seconds':time.perf_counter()-start}
    with (BASE/'HTTP_PREVIEW_RESULTS.jsonl').open('x',encoding='utf-8') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            for n,r in enumerate(pool.map(one,qs),1):
                results.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n')
                if n%50==0:f.flush();print('HTTP previews '+str(n)+'/480',flush=True)
    records_ok=[]
    for rid in records:
        fetched=request('/api/record?id='+rid)
        records_ok.append({'record_id':rid,'matches':fetched['record']==records[rid]})
    if not store.still_current(snap):raise RuntimeError('Demo changed while testing')
    task.filejson('HTTP_SUMMARY.json',{'queries':len(results),'pass':sum(r['passed'] for r in results),'fail':sum(not r['passed'] for r in results),'records_checked':len(records_ok),'record_roundtrip_matches':sum(x['matches'] for x in records_ok),'database_epoch_unchanged':True,'scope':'real owner API /api/preview, no WordPress or LLM','demo_only':True})
def pipeline_checks():
    from app.pipeline.engine import answer_question_pipeline_debug
    store=task.CommonStore(task.DB);snap=store.snapshot();records=snap['release']['records'];reader=task.CommonAnswerer(store)
    qs=[c for c in task.cases(records) if c['style']=='all_fields'];rows=[]
    with (BASE/'ACTUAL_CHAT_PIPELINE_RESULTS.jsonl').open('x',encoding='utf-8') as f:
        for n,c in enumerate(qs,1):
            # Do not fall back to real legacy facts for the fictional dataset.
            gate=reader.answer(c['question'],locale=c['lang'],history=c['history'],at=task.AT)
            if gate is None:
                r={**c,'passed':False,'reasons':['common_miss; legacy fallback deliberately not invoked for demo'],'skipped':True,'answer':None}
            else:
                try:
                    ans=answer_question_pipeline_debug(c['question'],locale=c['lang'],recent_history=c['history'],experimental_allow_llm=False,experimental_rag_fallback=False,global_timeout_sec=20)
                    ok,why=task.score(ans,c,records);r={**c,'passed':ok,'reasons':why,'answer':ans.answer,'mode':ans.mode,'decision':ans.decision_artifact,'skipped':False}
                except Exception:r={**c,'passed':False,'reasons':['exception'],'exception':traceback.format_exc(),'skipped':False}
            rows.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n')
            if n%50==0:f.flush();print('actual pipeline '+str(n)+'/480',flush=True)
    task.filejson('ACTUAL_CHAT_PIPELINE_SUMMARY.json',{'queries':len(rows),'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'skipped':sum(r['skipped'] for r in rows),'scope':'actual AnswerQualityPipeline entry; no LLM/no live WordPress','demo_environment_only':True})
if __name__=='__main__':
    if sys.argv[1]=='api':api_checks()
    elif sys.argv[1]=='pipeline':pipeline_checks()
    else:raise SystemExit('Use api or pipeline')
