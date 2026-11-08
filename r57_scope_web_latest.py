import json,time,uuid,urllib.request,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r57_current_path.txt').read_text());URL='http://127.0.0.1:8093';rows=[]
cases=[('ไก่กับไข่อะไรเกิดก่อนกัน','th'),('เย็นนี้กินอะไรดี','th'),('ช่วยเขียนบทความเรื่องจักรวาล 500 คำ','th'),('ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน 80 คำ','th'),('ช่วยเขียนบทสนทนาสั้นๆระหว่างเพื่อนสองคนที่นัดมาเล่นเกม ใช้ประมาณ 80 คำ','th'),('แปลเป็นอังกฤษ: เย็นนี้กินอะไรดี','th'),('Which came first, chicken or egg?','en'),('What should I eat tonight?','en'),('Write an 80 word scene where two friends play video games.','en'),('Translate to Thai: What should I eat tonight?','en'),('Explain quantum gravity.','en'),('Tell me a birthday cake recipe.','en')]
def req(path,p=None):
 r=urllib.request.Request(URL+path,data=json.dumps(p,ensure_ascii=False).encode() if p else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(r,timeout=35) as f:return json.load(f)
health=req('/health');assert health['runtime']['version'].startswith('2026.10.10-service-r57.')
def free_generation(node):
 if isinstance(node,dict):
  if node.get('llm_kind')=='general_llm' and node.get('llm_provider_attempted'):return True
  return any(free_generation(x) for x in node.values())
 if isinstance(node,list):return any(free_generation(x) for x in node)
 return False
for q,l in cases:
 s='r57-scope-'+uuid.uuid4().hex;start=time.perf_counter();job=req('/api/chat/jobs',dict(question=q,locale=l,debug=True,experimental_rag_fallback=True,experimental_allow_llm=True,client_session_id=s,client_turn_id=uuid.uuid4().hex));deadline=time.monotonic()+100
 while job.get('status') in ('queued','running') and time.monotonic()<deadline:
  time.sleep(.15);job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+s)
 r=job.get('result') or {};errors=[]
 if job.get('status')!='completed':errors.append('transport')
 if r.get('mode') not in ('pipeline:studio_scope_no_answer','pipeline:boundary_no_answer_out_of_scope'):errors.append('not_scope_response:'+r.get('mode',''))
 if free_generation(r.get('trace',[])):errors.append('generic_generation_attempted')
 if 'PSU Esports Studio' not in r.get('answer',''):errors.append('missing_product_scope')
 row=dict(question=q,locale=l,job=job,elapsed_sec=time.perf_counter()-start,errors=errors,runtime=health['runtime']['version']);rows.append(row)
 with (OUT/'scope_web_latest_raw.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(q,r.get('mode'),errors,flush=True)
with (OUT/'scope_web_latest.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
sys.exit(int(any(r['errors'] for r in rows)))
