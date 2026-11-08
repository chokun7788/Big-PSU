import sys,json,uuid,urllib.request,urllib.error,threading,concurrent.futures
from pathlib import Path
import r50_probe as r
URL='http://127.0.0.1:8091'
suffix='_V2' if sys.argv[1].endswith('2') else ''
def health():return json.load(urllib.request.urlopen(URL+'/health',timeout=8))
def ask(payload):
 req=urllib.request.Request(URL+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=25) as response:return json.load(response)
 except urllib.error.HTTPError as error:
  body=json.loads(error.read().decode());body['http_status']=error.code;return body
if sys.argv[1].startswith('before'):
 rows=[]
 for i in range(10):
  en=i%2==1;parking=i%4<2;q=('Is there parking?' if en else 'มีที่จอดรถไหม') if parking else ('Can I bring my own keyboard?' if en else 'เอาคีย์บอร์ดส่วนตัวมาได้ไหม')
  p=dict(question=q,locale='en' if en else 'th',client_session_id='r50-restart-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex,debug=False)
  answer=ask(p);assert answer['mode']=='pipeline:user_service_facts';p['last_seen_response_id']=answer['request_id'];replay=ask(p);assert replay['request_id']==answer['request_id'] and replay['conversation_state']['survives_server_restart']
  rows.append(dict(payload=p,response=answer,replay=replay,parking=parking))
 with (r.OUT/f'HTTP_RESTART_SEED{suffix}.json').open('x',encoding='utf-8') as f:json.dump(dict(health=health(),cases=rows),f,ensure_ascii=False,indent=2)
 print('Seeded and ACKed',len(rows),'sessions',flush=True)
else:
 seed=json.loads((r.OUT/f'HTTP_RESTART_SEED{suffix}.json').read_text(encoding='utf-8'));h=health();assert h['runtime']['python']['pid']!=seed['health']['runtime']['python']['pid'];assert h['runtime']['version']==seed['health']['runtime']['version']
 barrier=None if suffix else threading.Barrier(len(seed['cases']))
 def recover(old):
  p=old['payload'].copy();en=p['locale']=='en';parking=old['parking'];p['question']=('Is it free?' if en else 'ฟรีไหม') if parking else ('What about a controller?' if en else 'แล้วจอยล่ะ');p['client_turn_id']=uuid.uuid4().hex
  if barrier:barrier.wait(timeout=8)
  b=ask(p);a=b.get('answer','');expected=('not been specified' if en else 'ยังไม่ได้ระบุค่าจอดรถ') if parking else ('not been confirmed' if en else 'ยังไม่ได้ยืนยันสิทธิ์นำจอย')
  passed=b.get('mode')=='pipeline:user_service_facts' and expected in a and b['conversation_state']['survives_server_restart'] and b.get('session_id')==p['client_session_id']
  print(p['locale'],'parking' if parking else 'controller','PASS' if passed else 'FAIL',flush=True)
  return dict(payload=p,response=b,passed=passed)
 if suffix:rows=[recover(old) for old in seed['cases']]
 else:
  with concurrent.futures.ThreadPoolExecutor(max_workers=len(seed['cases'])) as pool:rows=list(pool.map(recover,seed['cases']))
 # A fresh session cannot inherit the recovered parking topic.
 p=dict(question='ฟรีไหม',locale='th',client_session_id='r50-unrelated-'+uuid.uuid4().hex,client_turn_id=uuid.uuid4().hex,debug=False);b=ask(p)
 rows.append(dict(payload=p,response=b,passed='หน้าตึก 5' not in b.get('answer','') and b.get('mode')!='pipeline:user_service_facts'))
 with (r.OUT/f'HTTP_RESTART_RESULT{suffix}.json').open('x',encoding='utf-8') as f:json.dump(dict(health_before=seed['health'],health_after=h,total=len(rows),passed=sum(x['passed'] for x in rows),results=rows),f,ensure_ascii=False,indent=2)
 print('SUMMARY',sum(x['passed'] for x in rows),len(rows),flush=True)
