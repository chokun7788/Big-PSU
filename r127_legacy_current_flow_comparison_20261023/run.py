import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;config=json.loads((R/'PROCESS.json').read_text('utf8'))
for c in config.values():
 for n in range(50):
  try:
   with urllib.request.urlopen(c['url']+'/health',timeout=2) as f:health=json.load(f)
   break
  except OSError:time.sleep(1)
 else:raise RuntimeError('server unavailable '+c['url'])
cases=json.loads((R.parent/'r126_latency_audit_20261023/run_1792765098897050300/CASES.json').read_text('utf8'))
conversations=[
 ('game_reference',['God of War Ragnarök คือเกมอะไร','เล่นได้ที่โซนไหน','แล้วปุ่ม R2 ทำอะไร']),
 ('booking_reference',['จอง Cockpit ยังไง','แล้วถ้าต้องการยกเลิกล่ะ']),
 ('price_reference',['บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท','แล้วสองชั่วโมงล่ะ','เปลี่ยนเป็น PS5 ล่ะ']),
 ('date_clarification',['วันที่15เปิดไหม','พฤศจิกายน']),
 ('live_clarification',['วันที่27ว่างไหม','PC2']),
 ('topic_shift',['Beat Saber คืออะไร','พรุ่งนี้ศูนย์เปิดไหม','เกมนี้เล่นได้กี่คน']),
 ('multi_target',['PC กับ PS5 มีเกมอะไรบ้าง','อันที่สองราคาเท่าไร']),
 ('game_controls',['Tekken 8 คืออะไร','ปุ่มทั้งหมดมีอะไรบ้าง'])]
(R/'CONVERSATIONS.json').write_text(json.dumps(conversations,ensure_ascii=False,indent=2),'utf8')
def call(arm,kind,key,q,session,last='',turn=1):
 c=config[arm];OUT=Path(c['output']);payload={'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':session,'client_turn_id':'turn-'+uuid.uuid4().hex,'last_seen_response_id':last}
 before=time.perf_counter();row={'arm':arm,'kind':kind,'key':key,'turn':turn,'question':q,'started_at':time.time(),'request':payload}
 try:
  req=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=195) as f:row['response']=json.load(f)
 except Exception as e:row['error']=repr(e)
 row['wall_sec']=time.perf_counter()-before
 with (OUT/'HTTP_RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 (R/'PROGRESS.json').write_text(json.dumps({k:row[k] for k in ['arm','kind','key','turn','wall_sec']},indent=2),'utf8')
 print(json.dumps({k:row[k] for k in ['arm','kind','key','turn','wall_sec']}|{'answer':row.get('response',{}).get('answer','')[:180],'error':row.get('error')},ensure_ascii=False),flush=True)
 return row.get('response',{}).get('request_id','')
for category,q in cases:call('legacy','single',category,q,'r127-'+uuid.uuid4().hex)
for name,questions in conversations:
 for arm in ['legacy','current']:
  session='r127-'+uuid.uuid4().hex;last=''
  for turn,q in enumerate(questions,1):last=call(arm,'conversation',name,q,session,last,turn)
(R/'COMPLETE.json').write_text(json.dumps({'completed':True,'legacy_single':len(cases),'conversations_per_arm':len(conversations),'turns_per_arm':sum(len(q) for _,q in conversations),'new_single_results':'retained R126 actual HTTP, no replayed answers used for generation','full_test':False},indent=2),'utf8')
