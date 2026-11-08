import json,urllib.request,uuid,time
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());base='http://127.0.0.1:8091'
rows=[]
for loc,q,terms in [('th','CS2 แข่งกี่วันและแข่งที่ไหน',['1 วัน','PSU Esports Studio']),('th','CS2 แข่งกี่วันแล้วจัดที่ไหน แบบสรุป',['1 วัน','PSU Esports Studio']),('en','How many days does the CS2 tournament last and where is it held?',['1 day','PSU Esports Studio'])]:
    start=time.perf_counter();payload={'question':q,'locale':loc,'recent_history':[],'client_session_id':'r30-event-'+uuid.uuid4().hex,'debug':True,'experimental_allow_llm':True,'experimental_rag_fallback':True}
    raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));missing=[v for v in terms if v.casefold() not in raw.get('answer','').casefold()]
    rows.append({'question':q,'locale':loc,'response':raw,'elapsed':time.perf_counter()-start,'missing_content':missing,'scope':'recorded CS2 rulebook s08_c01 content; not current event schedule'})
with (r/'PRODUCTION_EVENT_DETAILS_PROBE_G5.json').open('x',encoding='utf-8') as out:json.dump(rows,out,ensure_ascii=False,indent=2)
print(json.dumps([{k:x[k] for k in ['question','elapsed','missing_content']}|{'answer':x['response'].get('answer'),'mode':x['response'].get('mode')} for x in rows],ensure_ascii=False),flush=True)
