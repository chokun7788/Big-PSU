import json,sys,time,urllib.request,uuid
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
run=sys.argv[1];port=sys.argv[2]
questions=[('th','ขออีเมลและเบอร์โทรติดต่อศูนย์หน่อย'),('th','ขอสอบถามหน่อยครับ ขอข้อมูลที่ยืนยันได้หน่อยครับ: ที่ศูนย์มี Minecraft ไหม'),('en','Is Minecraft available to play at the studio?'),('th','Minecraft เป็นเกมแนวไหน'),('en','Do you ship gaming equipment to my house?'),('en','Who is Mr. Stduio Man?')]
rows=[]
for loc,q in questions:
 start=time.perf_counter()
 payload=dict(question=q,locale=loc,recent_history=[],client_session_id='r33-probe-'+uuid.uuid4().hex,debug=True)
 try:r=json.load(urllib.request.urlopen(urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=35))
 except Exception as e:r=dict(exception=str(e))
 x=dict(question=q,locale=loc,elapsed=time.perf_counter()-start,response=r);rows.append(x)
 print(json.dumps(dict(question=q,elapsed=x['elapsed'],answer=r.get('answer'),mode=r.get('mode'),exception=r.get('exception')),ensure_ascii=False),flush=True)
with (R/(run+'_probe.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
