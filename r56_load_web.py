import json,time,uuid,urllib.request,urllib.error,sys,statistics
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());URL='http://127.0.0.1:8093';LABEL=sys.argv[1];stages=[]
def req(path,p=None):
 r=urllib.request.Request(URL+path,data=json.dumps(p,ensure_ascii=False).encode() if p is not None else None,headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(r,timeout=35) as f:return f.status,json.load(f)
 except urllib.error.HTTPError as f:return f.code,json.load(f)
health=req('/health')[1];assert health['runtime']['version'].startswith('2026.10.10-service-r56.')
fast=[('PC บุคคลทั่วไปสองชั่วโมงกี่บาท','th','140'),('Do I need membership to play?','en','not required'),('ศูนย์อยู่ตึกอะไร แล้วมีที่จอดรถไหม','th','อาคาร 5'),('All PC games please','en','VALORANT')]
llm=[('ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน แบบเป็นกันเองสั้นๆ 80 คำ','th',''),('Write a short friendly invitation for friends to play video games together, about 80 words.','en',''),('ช่วยเขียนบทสนทนาสั้นๆระหว่างเพื่อนสองคนที่นัดมาเล่นเกม ใช้ประมาณ 80 คำ','th',''),('Write an 80 word scene where two friends arrange to play video games together.','en','')]
def run(item):
 q,l,term,kind=item;s='r56-load-'+uuid.uuid4().hex;start=time.perf_counter();errors=[]
 try:
  code,job=req('/api/chat/jobs',dict(question=q,locale=l,debug=True,experimental_rag_fallback=True,experimental_allow_llm=True,client_session_id=s,client_turn_id=uuid.uuid4().hex))
  deadline=time.monotonic()+110
  while job.get('status') in ('queued','running') and time.monotonic()<deadline:
   time.sleep(.2);_,job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+s)
  r=job.get('result') or {};a=r.get('answer','')
  if job.get('status')!='completed' or r.get('timed_out') or not a:errors.append('no_completed_answer')
  if term and term.casefold() not in a.casefold():errors.append('required_content_missing')
  if kind=='llm' and 'general_llm' not in r.get('mode',''):errors.append('not_actual_general_llm')
  return dict(question=q,locale=l,kind=kind,elapsed_sec=time.perf_counter()-start,job=job,errors=errors)
 except Exception as e:return dict(question=q,locale=l,kind=kind,elapsed_sec=time.perf_counter()-start,errors=[type(e).__name__+':'+str(e)])
for kind,levels in [('fast',[1,2,4,8]),('llm',[1,2,4,6]),('mixed',[8])]:
 for n in levels:
  items=[(*((fast if kind=='fast' or kind=='mixed' and i%2==0 else llm)[i%4]),'fast' if kind=='fast' or kind=='mixed' and i%2==0 else 'llm') for i in range(n)]
  start=time.perf_counter()
  with ThreadPoolExecutor(n) as pool:rows=list(pool.map(run,items))
  elapsed=time.perf_counter()-start;values=sorted(r['elapsed_sec'] for r in rows)
  stage=dict(kind=kind,simultaneous=n,wall_sec=elapsed,median_sec=statistics.median(values),p95_sec=values[min(len(values)-1,int(.95*len(values)))],max_sec=max(values),failures=sum(bool(r['errors']) for r in rows),rows=rows,health_after=req('/health')[1]);stages.append(stage)
  with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(stage,ensure_ascii=False)+'\n')
  print(kind,n,'median',round(stage['median_sec'],2),'max',round(stage['max_sec'],2),'fail',stage['failures'],flush=True)
with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as f:json.dump(dict(runtime=health['runtime']['version'],stages=stages,meaning='finite warm-machine batches, not sustained capacity or factual LLM accuracy'),f,ensure_ascii=False,indent=2)
