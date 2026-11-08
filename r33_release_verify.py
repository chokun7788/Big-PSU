import sys,json,time,urllib.request,uuid,hashlib
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
for attempt in range(30):
 try:
  health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=3))
  assert health['ok'] and health['runtime']['version']=='2026.10.02-usable-task-frames-r33'
  assert all(w['ready'] and w['alive'] for w in health['pipeline_workers']['workers'])
  break
 except Exception:
  if attempt==29:raise
  time.sleep(2)
cases=[
 ('th','ขออีเมลและเบอร์โทรติดต่อศูนย์หน่อย',['psuesportspkt@gmail.com','7627 6004','7627 6045']),
 ('en','Could you please help me with thus: What are the studio rules',['Key studio rules']),
 ('en','What is the studio policy for transfer booking',['cannot be transferred']),
 ('en','How do I pay by bank transfer for a booking',['795-276244-1']),
 ('th','PS5 บุคคลทั่วไป 3 ชั่วโมงราคาเท่าไหร่',['450']),
 ('th','ที่ศูนย์มี Minecraft ไหม',['ยังไม่พบ Minecraft','รายการเกม']),
 ('en','Do you ship gaming equipment to my house?',['could not find verified','home']),
 ('th','กฏตอนเเข่ง cs2 มีอะไรมั่ง',['Counter-Strike 2']),
 ('en','What are the studio ruls?',['Key studio rules']),
 ('th','สามารถถามอะไรดไ้บ้าง',['ราคา','จอง']),
]
rows=[]
for loc,q,words in cases:
 start=time.perf_counter();payload=dict(question=q,locale=loc,recent_history=[],client_session_id='r33-release-'+uuid.uuid4().hex,debug=True)
 try:
  r=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8090/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30))
  errors=['missing:'+word for word in words if word.casefold() not in r.get('answer','').casefold()]
  if not r.get('validation_ok',True):errors.append('validation_rejected')
 except Exception as e:r=dict(exception=str(e));errors=['transport:'+str(e)]
 rows.append(dict(question=q,locale=loc,response=r,elapsed=time.perf_counter()-start,passed=not errors,errors=errors))
 print(json.dumps(dict(question=q,passed=not errors,errors=errors,answer=r.get('answer','')[:140]),ensure_ascii=False),flush=True)
ui={}
for url,file in [('/','index.html'),('/chat_request.js','chat_request.js')]:
 raw=urllib.request.urlopen('http://127.0.0.1:8090'+url,timeout=10).read()
 local=(P/'web_chat'/file).read_bytes();ui[file]=dict(sha256=hashlib.sha256(raw).hexdigest(),matches_project=raw==local)
summary=dict(url='http://127.0.0.1:8090/',health=health,total=len(rows),passed=sum(x['passed'] for x in rows),rows=rows,ui=ui,scope='Final installed package HTTP smoke; no real booking occupancy collected')
with (R/'RELEASE_FINAL_I_VERIFICATION.json').open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
print(dict(total=len(rows),passed=summary['passed'],ui=ui));sys.exit(summary['passed']!=len(rows) or not all(x['matches_project'] for x in ui.values()))
