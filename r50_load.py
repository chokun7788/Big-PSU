import json,time,uuid,sys,threading,urllib.request,urllib.error,statistics,concurrent.futures,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text());URL='http://127.0.0.1:'+sys.argv[1];LABEL=sys.argv[2]
FAST=[('th','มีที่จอดรถไหม',['รถยนต์','มอเตอร์ไซค์','5']),('en','Can I bring my own keyboard?',['not allowed','keyboards']),('th','แนบสลิปผิดรูปแก้ยังไง',['สลิป','facebook.com/psuesportsphuket']),('en','Do I need membership to use the studio?',['not required']),('th','ศูนย์อยู่ตรงไหน',['อาคาร 5','ชั้น 1','83120']),('en','Can I walk in without a booking?',['book','system'])]
MIXED=[('th','ปุ่มยิง CS2 ใช้เมาส์ปุ่มไหน',['Counter-Strike 2','Left Mouse Button']),('th','กฎการแข่งขัน VALORANT ใช้เมาส์ส่วนตัวได้ไหม',['เมาส์','VALORANT','competition_rules_valorant']),('en','What games are available in PC?',['PC Zone','VALORANT']),('en','Can I bring my own keyboard?',['not allowed','keyboards'])]
def health():
 with urllib.request.urlopen(URL+'/health',timeout=8) as response:return json.load(response)
def ask(payload):
 started=time.perf_counter();header=''
 try:
  req=urllib.request.Request(URL+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=25) as response:status=response.status;body=json.load(response);header=response.headers.get('Content-Language','')
 except urllib.error.HTTPError as error:
  status=error.code;body=json.loads(error.read().decode());header=error.headers.get('Content-Language','')
 except Exception as error:status=0;body={'error':repr(error)}
 return dict(payload=payload,status=status,response=body,elapsed_sec=round(time.perf_counter()-started,4),content_language=header)
def pct(values,p):
 return sorted(values)[max(0,min(len(values)-1,math.ceil(len(values)*p)-1))] if values else None
def run_profile(name,levels,waves):
 queries=FAST if name=='fast' else MIXED;rows=[];overload=0
 for n in levels:
  h0=health();level=[];wave_wall=[]
  for wave in range(waves):
   barrier=threading.Barrier(n);started=time.perf_counter()
   def user(i):
    locale,q,expected=queries[(i+wave)%len(queries)];payload=dict(question=q,locale=locale,client_session_id='r50-load-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex,debug=False)
    barrier.wait(timeout=8);record=ask(payload);b=record['response'];answer=b.get('answer','')
    record.update(profile=name,users=n,wave=wave,user=i,expected_content=expected,correct=record['status']==200 and b.get('ok') is True and not b.get('timed_out') and all(x.casefold() in answer.casefold() for x in expected) and b.get('session_id')==payload['client_session_id'] and record['content_language']==locale)
    with lock:
     with raw.open('a',encoding='utf-8') as stream:stream.write(json.dumps(record,ensure_ascii=False)+'\n')
    return record
   with concurrent.futures.ThreadPoolExecutor(max_workers=n) as pool:records=list(pool.map(user,range(n)))
   wall=time.perf_counter()-started;level.extend(records);wave_wall.append(wall)
   print(name,n,'wave',wave+1,'correct',sum(x['correct'] for x in records),'/',n,'wall',round(wall,3),flush=True)
  successful=[x['elapsed_sec'] for x in level if x['correct']];all_times=[x['elapsed_sec'] for x in level];h1=health()
  item=dict(profile=name,users=n,waves=waves,requests=len(level),correct=sum(x['correct'] for x in level),http_errors={str(code):sum(x['status']==code for x in level) for code in set(x['status'] for x in level) if code!=200},timeout_count=sum(bool(x['response'].get('timed_out')) for x in level),content_failures=sum(x['status']==200 and not x['correct'] for x in level),success_p50=statistics.median(successful) if successful else None,success_p95=pct(successful,.95),success_max=max(successful) if successful else None,all_p50=statistics.median(all_times),all_p95=pct(all_times,.95),all_max=max(all_times),worker_pids_before=[x['pid'] for x in h0['pipeline_workers']['workers']],worker_pids_after=[x['pid'] for x in h1['pipeline_workers']['workers']],memory_after=h1['runtime']['system_memory'])
  item['acceptable']=item['correct']==item['requests'] and not item['timeout_count'] and item['success_p95']<=20 and item['worker_pids_before']==item['worker_pids_after']
  item['wave_wall_sec']=wave_wall;item['successful_answers_per_sec']=item['correct']/sum(wave_wall);item['modes']={mode:sum(x['response'].get('mode')==mode for x in level) for mode in {x['response'].get('mode') for x in level}}
  rows.append(item);overload=overload+1 if not item['acceptable'] else 0
  with (OUT/f'{LABEL}_{RUN}_{name}_{n}_level.json').open('x',encoding='utf-8') as stream:json.dump(item,stream,ensure_ascii=False,indent=2)
  if overload>=2 or item['timeout_count']>=max(2,n//2) or not all(x['alive'] and x['ready'] for x in h1['pipeline_workers']['workers']) or h1['runtime']['system_memory'].get('available_physical_mb',2000)<600:
   print('STOP',name,'bounded capacity/health stop at',n,flush=True);break
 return rows
RUN=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6];raw=OUT/f'{LABEL}_{RUN}_raw.jsonl';lock=threading.Lock()
initial=health();assert initial['runtime']['version'].startswith(('2026.10.09-service-dialogue-r49','2026.10.09-flow-r50'))
profiles=sys.argv[3:] or ['fast','mixed'];rows=[]
for profile in profiles:rows.extend(run_profile(profile,[1,2,4,8,12,16,24,32] if profile=='fast' else [1,2,4,6,8,12],3 if profile=='fast' else 2))
with (OUT/f'{LABEL}_{RUN}_summary.json').open('x',encoding='utf-8') as stream:json.dump(dict(label=LABEL,health_before=initial,health_after=health(),raw_file=raw.name,profiles=rows,scope='same host simultaneous first-attempt HTTP requests; local workload; no WordPress burst; no retry'),stream,ensure_ascii=False,indent=2)
print('SUMMARY',[(x['profile'],x['users'],x['correct'],x['requests'],x['acceptable'],x['success_p95']) for x in rows],flush=True)
