import sys,json,uuid,urllib.request,time
from pathlib import Path
root=Path(__file__).parent;r=Path((root/'r31_report_path.txt').read_text().strip());old=Path((root/'r29_report_path.txt').read_text().strip());base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2]
cases=[('TH-PC','วันนี้ตอน10โมง PC1 ว่างไหม','th'),('TH-broad','ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง','th'),('TH-cockpik','cockpik ว่างไหม','th'),('TH-switch','Nintendo ว่างไหม','th'),('EN-PC','Is PC1 free at 10:00 today?','en'),('EN-broad','Which equipment is available at 3 pm today?','en'),('EN-cockpik','Is cockpik available now?','en'),('EN-switch','Is Nintendo available now?','en')]
fixtures=json.loads((old/'blocked36_fixture.json').read_text(encoding='utf-8'))['cases'];rows=[]
with (r/(run+'_path_guard.jsonl')).open('x',encoding='utf-8') as f:
    for group,entries in [('live_path',cases),('guard',[(c['id'],c['question'],c['locale']) for c in fixtures])]:
        for id,q,l in entries:
            payload={'question':q,'locale':l,'recent_history':[],'client_session_id':'r30-'+uuid.uuid4().hex,'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True};start=time.perf_counter()
            try:
                response=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));mode=response.get('mode','');errors=[]
                if group=='live_path':
                    if 'live_booking' not in mode:errors.append('live_path_not_observed:'+mode)
                    scope='path_transport_only_no_occupancy_oracle'
                else:
                    c=next(x for x in fixtures if x['id']==id);blocked=('input_quality' in mode or 'keyboard_layout' in mode or mode=='input_guard_layout_retype')
                    if blocked!=c['expected_blocked']:errors.append('wrong_guard_outcome:'+mode)
                    scope='guard_only_not_semantic_answer_correctness'
                if response.get('validation_ok') is False:errors.append('validation_rejected')
            except Exception as e:response={'error':type(e).__name__+':'+str(e)};errors=['http_or_transport_failure'];scope=group
            row={'id':id,'group':group,'question':q,'locale':l,'scope':scope,'real_occupancy_verified':False,'elapsed':time.perf_counter()-start,'failures':errors,'response':response};rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
            if errors:print(json.dumps({'id':id,'errors':errors}),flush=True)
with (r/(run+'_path_guard_summary.json')).open('x',encoding='utf-8') as f:json.dump({'total':len(rows),'passed':sum(not x['failures'] for x in rows),'by_group':{g:{'total':sum(x['group']==g for x in rows),'passed':sum(x['group']==g and not x['failures'] for x in rows)} for g in ['live_path','guard']},'real_booking_correctness_verified':False},f,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(rows),'passed':sum(not x['failures'] for x in rows)}),flush=True)
