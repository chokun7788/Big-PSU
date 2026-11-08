import json,time,uuid,urllib.request,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r57_current_path.txt').read_text());URL='http://127.0.0.1:8093';rows=[]
cases=[('Where can I eat food in the studio?','en',['designated','areas']),('Can I bring food into the studio?','en',['may bring','designated']),('กินอาหารตรงไหนในศูนย์ได้บ้าง','th',['พื้นที่']),('เอาอาหารเข้าศูนย์ได้ไหม','th',['เข้ามาได้','เฉพาะพื้นที่']),('ถามอะไรได้บ้าง','th',['เกม','ค่าบริการ','จอง']),('What can you help me with?','en',['games','booking'])]
def req(path,p=None):
 r=urllib.request.Request(URL+path,data=json.dumps(p,ensure_ascii=False).encode() if p else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(r,timeout=35) as f:return json.load(f)
health=req('/health');assert health['runtime']['version']=='2026.10.10-service-r57.4'
for q,l,terms in cases:
 s='r57-positive-'+uuid.uuid4().hex;start=time.perf_counter();job=req('/api/chat/jobs',dict(question=q,locale=l,debug=True,experimental_rag_fallback=True,client_session_id=s,client_turn_id=uuid.uuid4().hex));deadline=time.monotonic()+100
 while job.get('status') in ('queued','running') and time.monotonic()<deadline:
  time.sleep(.15);job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+s)
 r=job.get('result') or {};a=r.get('answer','');errors=[]
 if job.get('status')!='completed':errors.append('transport')
 if r.get('mode')=='pipeline:studio_scope_no_answer':errors.append('valid_studio_query_blocked')
 for w in terms:
  if w.casefold() not in a.casefold():errors.append('missing:'+w)
 row=dict(question=q,locale=l,job=job,elapsed_sec=time.perf_counter()-start,errors=errors);rows.append(row);print(q,r.get('mode'),errors,flush=True)
with (OUT/'positive_boundaries_web_final.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
sys.exit(int(any(r['errors'] for r in rows)))
