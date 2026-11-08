import sys,json,uuid,time
from pathlib import Path
from r52_web_cases import request
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r54_current_path.txt').read_text());session='r54rules-'+uuid.uuid4().hex;seen='';rows=[]
for page in range(10):
 q='ขอกฎการแข่งขัน CS2 ทั้งหมดทุกหัวข้อ' if page==0 else 'ต่อ เอากฎที่เหลือ'
 start=time.perf_counter();status,job=request('/api/chat/jobs',dict(question=q,locale='th',debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id='r54-'+uuid.uuid4().hex,last_seen_response_id=seen))
 if status==202:
  end=time.monotonic()+60
  while job['status'] in ('queued','running') and time.monotonic()<end:
   time.sleep(.25);_,job=request('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
 result=job.get('result') or {};seen=result.get('request_id','');coverage=result.get('rule_coverage') or {}
 row=dict(case=dict(id='p'+str(page+1),question=q,category='rule_pagination',locale='th'),elapsed_sec=time.perf_counter()-start,job=job,coverage=coverage);rows.append(row)
 with (OUT/'rule_pages_raw.jsonl').open('a',encoding='utf-8') as s:s.write(json.dumps(row,ensure_ascii=False)+'\n')
 print('page',page+1,'mode',result.get('mode'),'returned',len(coverage.get('returned_ids',[])),'remaining',len(coverage.get('remaining_ids',[])),flush=True)
 if not coverage or not coverage.get('remaining_ids'):break
returned=[x for r in rows for x in r['coverage'].get('returned_ids',[])];expected=set(rows[0]['coverage'].get('expected_ids',[]))
summary=dict(pages=len(rows),expected=len(expected),unique_returned=len(set(returned)),duplicates=len(returned)-len(set(returned)),missing=sorted(expected-set(returned)),complete=bool(expected) and expected==set(returned),source_owner_confirmed=rows[0]['coverage'].get('owner_confirmed'))
with (OUT/'rule_pages.json').open('x',encoding='utf-8') as s:json.dump({'summary':summary,'rows':rows},s,ensure_ascii=False,indent=2)
print(summary)
