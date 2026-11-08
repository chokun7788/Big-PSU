from pathlib import Path
import json,time,sys,urllib.request,uuid

W=Path(__file__).parent
port=int(sys.argv[1]);variant=sys.argv[2]
out=W/('share_checks_'+variant+'_'+time.strftime('%Y%m%d_%H%M%S'))
out.mkdir()
with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=5) as f:health=json.load(f)
assert health['runtime']['version']=='2026.10.03-share-r37.2-'+variant
assert health['llm_preflight']['ok'] and health['warmup']['ok']
assert all(w['ready'] and w['alive'] for w in health['pipeline_workers']['workers'])
(out/'health.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),encoding='utf-8')
rows=[]
with (out/'questions.jsonl').open('x',encoding='utf-8') as log:
    for locale,cases in [('th',[('มีเกมอะไรให้แข่งมั่ง','catalog'),('valorant','rules')]),('en',[('What games can I compete in?','catalog'),('VALORANT','rules')])]:
        history=[];sid='share-smoke-'+uuid.uuid4().hex
        for q,kind in cases:
            payload=dict(question=q,locale=locale,client_session_id=sid,recent_history=history,debug=True,experimental_rag_fallback=True)
            req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
            started=time.perf_counter()
            with urllib.request.urlopen(req,timeout=35) as f:x=json.load(f)
            errors=[]
            if not x.get('answer') or x.get('timed_out'):errors.append('empty_or_timeout')
            if kind=='catalog' and x.get('route_intent')!='competition_rulebook_catalog':errors.append('catalog_route')
            if kind=='rules' and (x.get('route_category')!='competition_rules' or not x.get('sources') or not all('competition_rules_valorant_' in s['url'] for s in x['sources'])):errors.append('rules_source_or_route')
            row={'question':q,'locale':locale,'passed':not errors,'errors':errors,'elapsed_sec':round(time.perf_counter()-started,3),'result':x}
            rows.append(row);log.write(json.dumps(row,ensure_ascii=False)+'\n');log.flush()
            history.extend([{'role':'user','text':q},{'role':'assistant','text':x['answer'],'route_category':x.get('route_category'),'route_intent':x.get('route_intent'),'sources':x.get('sources',[])}])
summary={'variant':variant,'total':len(rows),'passed':sum(r['passed'] for r in rows),'runtime':health['runtime']['version'],'directory':str(out)}
(out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary),flush=True)
if summary['total']!=summary['passed']:sys.exit(1)
