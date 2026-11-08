import json,uuid,time,urllib.request,urllib.error,threading,concurrent.futures
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text());URL='http://127.0.0.1:8091'
def ask(p):
 t=time.perf_counter();req=urllib.request.Request(URL+'/api/chat',data=json.dumps(p,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=25) as response:status=response.status;b=json.load(response)
 except urllib.error.HTTPError as e:status=e.code;b=json.loads(e.read().decode())
 return dict(payload=p,response=b,status=status,elapsed_sec=time.perf_counter()-t)
rows=[]
for en in (False,True):
 for parking in (True,False):
  p=dict(question=('Is there parking?' if en else 'มีที่จอดรถไหม') if parking else ('Can I bring my own keyboard?' if en else 'เอาคีย์บอร์ดส่วนตัวมาได้ไหม'),locale='en' if en else 'th',client_session_id='r50-isolation-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex,debug=False)
  a=ask(p);assert a['status']==200 and a['response']['mode']=='pipeline:user_service_facts';p['last_seen_response_id']=a['response']['request_id'];ack=ask(p);assert ack['response']['request_id']==a['response']['request_id']
  rows.append(dict(seed=a,ack=ack,parking=parking,en=en))
barrier=threading.Barrier(4)
def follow(row):
 en=row['en'];parking=row['parking'];p=row['ack']['payload'].copy();p['question']=('Is it free?' if en else 'ฟรีไหม') if parking else ('What about a controller?' if en else 'แล้วจอยล่ะ');p['client_turn_id']=uuid.uuid4().hex
 barrier.wait(timeout=8);a=ask(p);b=a['response'];expected=('not been specified' if en else 'ยังไม่ได้ระบุค่าจอดรถ') if parking else ('not been confirmed' if en else 'ยังไม่ได้ยืนยันสิทธิ์นำจอย')
 return dict(**row,follow=a,passed=a['status']==200 and expected in b.get('answer','') and b.get('session_id')==p['client_session_id'] and b.get('context_resolution',{}).get('used_context') is True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(follow,rows))
with (OUT/'HTTP_PARALLEL_CONTEXT_R50.json').open('x',encoding='utf-8') as f:json.dump(dict(total=4,passed=sum(x['passed'] for x in results),results=results,scope='4 simultaneous acknowledged followups, two domains, TH/EN, separate sessions, no retry'),f,ensure_ascii=False,indent=2)
print('Parallel context',sum(x['passed'] for x in results),'/ 4')
