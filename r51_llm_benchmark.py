import json,time,uuid,sys,math,statistics,collections,threading,concurrent.futures,urllib.request,urllib.error
from pathlib import Path
BASE=Path(__file__).resolve().parent
if sys.argv[1]=='prepare':
 out=BASE/('r51_llm_benchmark_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);out.mkdir();(BASE/'r51_current_path.txt').write_text(str(out));print(out);sys.exit()
OUT=Path((BASE/'r51_current_path.txt').read_text());CHAT='http://127.0.0.1:8091';OLLAMA='http://127.0.0.1:11434';MODEL='scb10x/typhoon2.5-qwen3-4b';lock=threading.Lock()
CASES=[
 ('definition','th','อธิบายว่า ping ในเครือข่ายคืออะไรแบบสั้นๆ','ping'),('definition','en','Explain network latency in one short paragraph.','latency'),
 ('comparison','th','อธิบายความแตกต่างระหว่าง CPU และ GPU แบบเข้าใจง่าย','cpu'),('comparison','en','Compare TCP and UDP, including one advantage and one disadvantage of each.','tcp'),
 ('cause','th','ทำไมการเชื่อมต่อ Wi-Fi บางครั้งถึงมีความหน่วงมากกว่าสาย LAN',''),('cause','en','Why can high frame rate still feel choppy? Explain frame pacing briefly.','frame'),
 ('steps','th','ช่วยอธิบายวิธีฝึกพิมพ์สัมผัสสำหรับมือใหม่เป็นขั้นตอนสั้นๆ',''),('steps','en','Give three steps for learning touch typing.',''),
 ('translation','th','แปลประโยค Please check your network connection เป็นภาษาไทย',''),('translation','en','Translate the Thai sentence กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต into English.',''),
 ('writing','th','ช่วยเขียนข้อความสั้นๆชวนเพื่อนมาซ้อมทำงานกลุ่มช่วงเย็น',''),('writing','en','Write a friendly two-sentence invitation to a group study session.',''),
 ('reasoning','th','กล่อง A มีลูกบอล 3 ลูก กล่อง B มี 5 ลูก ย้ายจาก B ไป A 2 ลูก ตอนนี้แต่ละกล่องมีกี่ลูก อธิบายสั้นๆ',''),('reasoning','en','Box A has 3 balls and box B has 5. Move 2 from B to A. How many are in each box? Explain briefly.',''),
 ('long','th','อธิบายความแตกต่างระหว่าง RAM กับ SSD พร้อมข้อดีข้อเสียและตัวอย่างการใช้งาน ขอประมาณ 500 คำ','ram'),('long','en','Explain how a computer network works, from DNS lookup to receiving a web page. Include TCP, TLS, HTTP and latency. Aim for 500 words.','')]
def get(url):
 with urllib.request.urlopen(url,timeout=10) as r:return json.load(r)
def health():return get(CHAT+'/health')
def write(name,obj):
 with (OUT/name).open('x',encoding='utf-8') as f:json.dump(obj,f,ensure_ascii=False,indent=2)
def append(name,obj):
 with lock:
  with (OUT/name).open('a',encoding='utf-8') as f:f.write(json.dumps(obj,ensure_ascii=False)+'\n')
def llm_metadata(body):
 found=[]
 def walk(x,path=''):
  if isinstance(x,dict):
   if x.get('llm_kind') and (x.get('llm_elapsed_ms',0)>0 or x.get('llm_attempted') or x.get('ollama_eval_count')):found.append(dict(path=path,**x))
   for k,v in x.items():walk(v,path+'/'+k)
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,path+'/'+str(i))
 walk(body.get('trace',[]));return found
def chat(case,debug=True):
 kind,locale,q,keyword=case;p=dict(question=q,locale=locale,debug=debug,experimental_rag_fallback=True,client_session_id='r51-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex);t=time.perf_counter()
 try:
  req=urllib.request.Request(CHAT+'/api/chat',data=json.dumps(p,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=25) as r:status=r.status;b=json.load(r)
 except urllib.error.HTTPError as e:status=e.code;b=json.loads(e.read().decode())
 except Exception as e:status=0;b={'error':repr(e)}
 calls=llm_metadata(b);mode=b.get('mode','');generated=('general_llm' in mode and 'unavailable' not in mode) or 'rag_llm_fallback' in mode
 return dict(kind=kind,locale=locale,payload=p,status=status,elapsed_sec=time.perf_counter()-t,response=b,llm_calls=calls,generated_answer=generated,transport_ok=status==200 and b.get('ok') is True,keyword_check=(keyword.lower() in b.get('answer','').lower()) if keyword else None)
def pct(v,p):return sorted(v)[min(len(v)-1,max(0,math.ceil(len(v)*p)-1))] if v else None
def stat(v):return dict(count=len(v),p50=statistics.median(v) if v else None,p95=pct(v,.95),max=max(v) if v else None)
def healthy(h):return h['runtime']['system_memory'].get('available_physical_mb',1000)>=600 and all(w['ready'] and w['alive'] for w in h['pipeline_workers']['workers'])
if sys.argv[1] in ('probe','probe2'):
 prefix='CHAT_PROBE_V2' if sys.argv[1]=='probe2' else 'CHAT_PROBE'
 if sys.argv[1]=='probe':write('ENVIRONMENT_BEFORE.json',dict(health=health(),ollama_ps=get(OLLAMA+'/api/ps'),models=get(OLLAMA+'/api/tags')))
 rows=[]
 for case in CASES:
  row=chat(case);rows.append(row);append(prefix+'_raw.jsonl',row);print(case[0],case[1],row['status'],round(row['elapsed_sec'],2),row['response'].get('mode'),[(x['llm_kind'],x.get('llm_elapsed_ms'),x.get('llm_response_chars')) for x in row['llm_calls']],flush=True)
  if not healthy(health()):print('STOP memory/health');break
 write(prefix+'_summary.json',dict(total=len(rows),generated=sum(x['generated_answer'] for x in rows),elapsed=stat([x['elapsed_sec'] for x in rows]),results=rows,health_after=health()))
elif sys.argv[1]=='chat_load':
 probe=json.loads((OUT/'CHAT_PROBE_V2_summary.json').read_text());candidates=[(x['kind'],x['locale'],x['payload']['question'],'') for x in probe['results'] if ('general_llm' in x['response'].get('mode','') and 'unavailable' not in x['response'].get('mode','')) and not x['response'].get('timed_out')];assert candidates,'No real generated answers: report probe failure rather than calling structured answers LLM.'
 profiles={name:[x for x in candidates if (x[0]=='long')==long] for name,long in [('standard',False),('long_request',True)]};levels=[]
 for name,cases in profiles.items():
  if not cases:continue
  failures=0
  for n in [1,2,4,6,8]:
   before=health();rows=[]
   for wave in range(2):
    barrier=threading.Barrier(n)
    def user(i):
     barrier.wait(timeout=8);r=chat(cases[(i+wave)%len(cases)]);r.update(profile=name,users=n,wave=wave,user=i);append('CHAT_LOAD_raw.jsonl',r);return r
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as pool:batch=list(pool.map(user,range(n)))
    rows.extend(batch);print(name,n,'wave',wave+1,'generated',sum(x['generated_answer'] for x in batch),'/',n,flush=True)
   after=health();good=[x for x in rows if x['transport_ok'] and x['generated_answer'] and not x['response'].get('timed_out')];pids=lambda h:[w['pid'] for w in h['pipeline_workers']['workers']]
   item=dict(profile=name,users=n,requests=len(rows),generated_ok=len(good),successful_latency=stat([x['elapsed_sec'] for x in good]),all_latency=stat([x['elapsed_sec'] for x in rows]),status_counts=dict(collections.Counter(str(x['status']) for x in rows)),mode_counts=dict(collections.Counter(x['response'].get('mode','') for x in rows)),timed_out=sum(bool(x['response'].get('timed_out')) for x in rows),worker_pids_before=pids(before),worker_pids_after=pids(after),health_after=after)
   item['acceptable']=len(good)==len(rows) and pids(before)==pids(after);levels.append(item);write(f'CHAT_LOAD_{name}_{n}.json',item);failures=0 if item['acceptable'] else failures+1
   if failures>=2 or not healthy(after):break
 write('CHAT_LOAD_summary.json',dict(profiles=levels,scope='actual chat HTTP debug=true with trace proof; no retry; capacity grade is generated response availability, not exhaustive factual correctness'))
elif sys.argv[1] in ('model_probe','model_load'):
 def model(case,num_predict=256,context_chars=0):
  kind,locale,q,_=case;prefix=('ตอบภาษาไทย' if locale=='th' else 'Answer in English')+' without a reasoning preamble. Answer only the user question.'
  if context_chars:prefix+='\nREFERENCE NOTES (synthetic benchmark context, not studio facts):\n'+(('network latency depends on transmission, propagation, processing and queueing. '*100)[:context_chars])
  p=dict(model=MODEL,prompt=prefix+'\nQuestion: '+q+'\nAnswer:',stream=True,think=False,keep_alive='30m',options=dict(temperature=.15,top_p=.8,num_predict=num_predict,num_ctx=3072));t=time.perf_counter();first=None;chunks=[];last={};status=0;error=''
  try:
   req=urllib.request.Request(OLLAMA+'/api/generate',data=json.dumps(p,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
   with urllib.request.urlopen(req,timeout=60) as response:
    status=response.status
    for raw in response:
     if time.perf_counter()-t>60:raise TimeoutError('benchmark total budget 60s')
     if not raw.strip():continue
     data=json.loads(raw);last=data;fragment=data.get('response','')
     if fragment:
      if first is None:first=time.perf_counter()-t
      chunks.append(fragment)
     if data.get('done'):break
  except Exception as e:error=repr(e)
  answer=''.join(chunks);ok=status==200 and bool(last.get('done')) and bool(answer) and not error;duration=last.get('eval_duration',0)
  return dict(kind=kind,locale=locale,question=q,num_predict=num_predict,prompt_chars=len(p['prompt']),synthetic_context_chars=context_chars,options=p['options'],think=False,status=status,elapsed_sec=time.perf_counter()-t,first_token_sec=first,answer=answer,done=last.get('done',False),done_reason=last.get('done_reason'),tokens=last.get('eval_count'),tokens_per_sec=last.get('eval_count',0)/(duration/1e9) if duration else None,provider={k:last.get(k) for k in ['total_duration','load_duration','prompt_eval_count','prompt_eval_duration','eval_count','eval_duration']},error=error,completed=ok)
 if sys.argv[1]=='model_probe':
  rows=[]
  jobs=[(c,256,0) for c in CASES if c[0] in ['definition','comparison','translation','writing','reasoning','steps']]
  jobs += [(c,n,0) for c in CASES if c[0]=='long' for n in [128,256,512]]
  jobs += [(c,128,5000) for c in CASES if c[0]=='definition']
  for c,n,ctx in jobs:
   row=model(c,n,ctx);rows.append(row);append('MODEL_PROBE_raw.jsonl',row);print('model',c[0],c[1],n,ctx,round(row['elapsed_sec'],2),row['tokens'],row['done_reason'],row['completed'],flush=True)
   if not healthy(health()):print('STOP memory/health');break
  write('MODEL_PROBE_summary.json',dict(results=rows,completed=sum(x['completed'] for x in rows),total=len(rows),scope='direct Ollama same model/think false; 60s harness budget; not chatbot product timings',health_after=health()))
 else:
  levels=[]
  for name,nump in [('short',128),('long',512)]:
   failures=0
   for n in [1,2,4,6]:
    rows=[];before=health()
    for wave in range(2):
     barrier=threading.Barrier(n)
     def user(i):
      case=CASES[(i+wave)%2] if name=='short' else CASES[-2+(i+wave)%2];barrier.wait(timeout=8);r=model(case,nump);r.update(profile=name,users=n,wave=wave,user=i);append('MODEL_LOAD_raw.jsonl',r);return r
     with concurrent.futures.ThreadPoolExecutor(max_workers=n) as pool:batch=list(pool.map(user,range(n)))
     rows.extend(batch);print('direct',name,n,'wave',wave+1,'completed',sum(x['completed'] for x in batch),'/',n,'max',round(max(x['elapsed_sec'] for x in batch),2),flush=True)
    good=[x for x in rows if x['completed']];item=dict(profile=name,users=n,requests=len(rows),completed=len(good),latency=stat([x['elapsed_sec'] for x in good]),first_token=stat([x['first_token_sec'] for x in good if x['first_token_sec'] is not None]),all_latency=stat([x['elapsed_sec'] for x in rows]),truncated=sum(x['done_reason']=='length' for x in rows),under_product_20sec=sum(x['completed'] and x['elapsed_sec']<=20 for x in rows),health_before=before,health_after=health());levels.append(item);write(f'MODEL_LOAD_{name}_{n}.json',item)
    failures=0 if len(good)==len(rows) and item['latency']['p95']<=20 else failures+1
    if failures>=2 or not healthy(item['health_after']):break
  write('MODEL_LOAD_summary.json',dict(profiles=levels,scope='direct Ollama concurrent streaming, bypasses chatbot gate and routing, no retry, 60s harness budget; completed does not imply full requested content'))
else:raise ValueError(sys.argv[1])
