import json,time,uuid,urllib.request,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());URL='http://127.0.0.1:8096';LABEL=sys.argv[1] if len(sys.argv)>1 else 'package_smoke7'
def req(path,p=None):
 r=urllib.request.Request(URL+path,data=json.dumps(p,ensure_ascii=False).encode() if p else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(r,timeout=30) as f:return json.load(f)
health=req('/health');assert health['runtime']['version']=='2026.10.10-service-r56.7';rows=[]
for q,locale,terms in [('บุคคลทั่วไปเล่น PC สองชั่วโมงราคาเท่าไหร่','th',['140']),('Do I need membership to play?','en',['not required']),('ศูนย์อยู่ตึกไหน แล้วมีที่จอดรถไหม','th',['อาคาร 5','มอเตอร์ไซค์'])]:
 s='r56-portable-'+uuid.uuid4().hex;start=time.perf_counter();job=req('/api/chat/jobs',dict(question=q,locale=locale,client_session_id=s,client_turn_id=uuid.uuid4().hex,debug=True));deadline=time.monotonic()+100
 while job['status'] in ('queued','running') and time.monotonic()<deadline:
  time.sleep(.2);job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+s)
 answer=(job.get('result') or {}).get('answer','');errors=[x for x in terms if x.casefold() not in answer.casefold()]
 if job['status']!='completed':errors.append(job['status'])
 rows.append(dict(question=q,locale=locale,job=job,elapsed_sec=time.perf_counter()-start,errors=errors));print(q,errors,flush=True)
with (OUT/(LABEL+'_answers.json')).open('x',encoding='utf-8') as f:json.dump(dict(health=health,rows=rows,meaning='portable bundled runtime same-machine smoke, not full capacity or clean-machine proof'),f,ensure_ascii=False,indent=2)
sys.exit(int(any(x['errors'] for x in rows)))
