import sys,json,time,uuid,re,urllib.request,urllib.error
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r57_current_path.txt').read_text())
LABEL=sys.argv[1];URL='http://127.0.0.1:8093'
cases=[]
def add(id,q,l='th',contains=(),forbid=(),scenario=None):
    cases.append(dict(id=id,question=q,locale=l,contains=list(contains),forbid=list(forbid),scenario=scenario))
add('n01','PC มีเกมอะไรบ้าง; บุคคลทั่วไปเล่น PC สองชั่วโมงเท่าไหร่; ต้องสมัครสมาชิกไหม; มีที่จอดรถไหม',contains=['VALORANT','140','สมาชิก','จอดรถ'])
add('n02','What games are on PC; how much is PC for two hours for a general adult; do I need membership; is there parking?', 'en',['VALORANT','140','membership','parking'])
add('n03','ไม่เอาราคา ขอรายชื่อเกม PC ทั้งหมด',contains=['VALORANT','Warzone'],forbid=['70 บาท'])
add('n04','I do not want prices, just list all PC games','en',['VALORANT','Warzone'],['70 THB'])
add('n05','ไม่ใช่กฎแข่ง ขอปุ่มยิงกับรีโหลด CS2',contains=['Left Mouse Button','รีโหลด'],forbid=['Single Elimination'])
add('n06','Not tournament rules. How do I shoot and reload in CS2?','en',['Left Mouse Button','Reload'],['Single Elimination'])
add('n07','บุคคลทั่วไป PC สองชั่วโมงราคาเท่าไหร่; อยู่ตึกอะไร; ต้องแสดงบัตรอะไร; จ่ายเงินสดได้ไหม',contains=['140','อาคาร 5','บัตร','เงินสด','ยืนยัน'])
add('n08','PC for a general adult two hours: how much; which building; what ID do I bring; can I pay cash?','en',['140','Building 5','ID','cash','confirmed'])
add('n09','สมาชิกจำเป็นไหม; มีที่จอดรถไหม; เช็คอินใช้บัตรอะไร; ไปนั่งดูเพื่อนได้ไหม',contains=['สมาชิก','จอดรถ','บัตร','ดู'])
add('n10','PC มีเกมอะไรบ้าง; ผู้ใหญ่ทั่วไปเล่น PC หนึ่งชั่วโมงเท่าไหร่; VR บุคคลทั่วไป 30 นาทีราคาเท่าไหร่; มีที่จอดรถไหม; ศูนย์อยู่ตึกอะไร',contains=['VALORANT','70','525','จอดรถ','อาคาร 5'])
add('n11','มีงบ 200 บาท บุคคลทั่วไปเล่น Nintendo 4 คนได้ไหม',contains=['280','0'])
add('n12','General adult, Nintendo Switch, four people, budget 200 THB. Can we afford one session?','en',['280','0'])
add('n13','ผมไม่ใช่นักศึกษา เล่น PC ชั่วโมงเดียวคิดกี่บาท',contains=['0','70','สิทธิ์'],forbid=['25 บาท'])
add('n14','I am not a student. How much is one hour on PC?','en',['0','70','eligibility'],['25 THB'])
add('n15','ไม่เอา PS5 ขอ PC บุคคลทั่วไปสองชั่วโมงราคาเท่าไหร่',contains=['140'],forbid=['150 บาท'])
add('n16','Not PS5. PC for a general adult for two hours please, how much?','en',['140'],['150 THB'])
add('n17','ขอราคาคนภายนอก',scenario='price_choice',contains=['PC','VR'])
add('n18','PC',scenario='price_choice',contains=['25','70'])
add('n19','เฉพาะบุคคลทั่วไป',scenario='price_choice',contains=['70'],forbid=['25 บาท'])
add('n20','แล้วสองชั่วโมงล่ะ',scenario='price_choice',contains=['140'])
add('n21','ถ้า VR 30 นาทีล่ะ',scenario='price_choice',contains=['525','2026-03-31'])
add('n22','What are the rates for external users?','en',['PC','VR'],scenario='en_choice')
add('n23','PC','en',['25','70'],scenario='en_choice')
add('n24','General adults only','en',['70'],['25 THB'],scenario='en_choice')
add('n25','And two hours?','en',['140'],scenario='en_choice')
add('n26','What about VR for 30 minutes?','en',['525','2026-03-31'],scenario='en_choice')
add('n27','ขอกฎการแข่งขัน CS2',contains=['Counter-Strike 2','5 คน'])
add('n28','ขอกฎแข่ง Tekken 8 ทั้งหมด',contains=['7/7','FT2','60'])
add('n29','Can I install a new game myself on the PC?','en',['confirmed'],['You can install'])
add('n30','เอาจอยตัวเองมาใช้ ไม่ใช่เมาส์นะ ได้ไหม',contains=['ยังไม่ได้ยืนยัน','จอย'])
add('n31','ไม่ใช่เครื่องค้าง แค่ลืม logout ต้องทำยังไง',contains=['ยังไม่ได้ยืนยัน'])
add('n32','Which games are on Cockpit and what does one hour cost for a general adult?','en',['Gran Turismo 7','200','2026-03-31'])
add('n33','Nintendo มีเกมอะไรบ้าง แล้วผู้ใหญ่ทั่วไป 4 คนหนึ่งชั่วโมงเท่าไหร่',contains=['Mario Kart 8 Deluxe','280','3-4'])
add('n34','ศูนย์อยู่ตึกอะไร แล้วมีที่จอดรถไหม',contains=['อาคาร 5','จอดรถ'])
add('n35','ผมจองชื่อผมแต่คนเล่นไม่มีชื่อในรายการได้ไหม',contains=['คนเล่น','รายชื่อ'])
add('n36','May I watch my friends, and is there a spectator admission fee?','en',['watch','confirmed'])
add('n37','มีที่จอดรถรถยนต์กับมอเตอร์ไซค์ไหม แล้วค่าจอดเท่าไหร่',contains=['รถยนต์','มอเตอร์ไซค์','ยังไม่ได้ระบุ'])
add('n38','Can I use my own mouse, and can I change the time of my booking?','en',['not','email','book'])
def req(path,data=None):
    r=urllib.request.Request(URL+path,data=json.dumps(data,ensure_ascii=False).encode() if data is not None else None,headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(r,timeout=35) as s:return s.status,json.load(s)
    except urllib.error.HTTPError as s:return s.code,json.load(s)
health=req('/health')[1]; assert health['runtime']['version'].startswith(('2026.10.10-service-r57.',))
sessions={};ack={};rows=[]
for c in cases:
    key=c.get('scenario') or c['id'];session=sessions.setdefault(key,'r56-'+uuid.uuid4().hex);start=time.perf_counter()
    status,job=req('/api/chat/jobs',dict(question=c['question'],locale=c['locale'],debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id=uuid.uuid4().hex,last_seen_response_id=ack.get(key,'')))
    deadline=time.monotonic()+100
    while job.get('status') in ('running','queued') and time.monotonic()<deadline:
        time.sleep(.15);_,job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
    result=job.get('result') or {};ack[key]=result.get('request_id','');answer=result.get('answer','');errors=[]
    if job.get('status')!='completed' or not result.get('ok'):errors.append('transport')
    compact=re.sub(r'\s+','',answer).casefold()
    for w in c['contains']:
        if re.sub(r'\s+','',w).casefold() not in compact:errors.append('missing:'+w)
    for w in c['forbid']:
        if re.sub(r'\s+','',w).casefold() in compact:errors.append('forbidden:'+w)
    row=dict(case=c,job=job,elapsed_sec=time.perf_counter()-start,errors=errors,runtime=health['runtime']['version']);rows.append(row)
    with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(c['id'],round(row['elapsed_sec'],2),result.get('mode'),errors,flush=True)
with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print('TOTAL',len(rows),'FAILED',sum(bool(r['errors']) for r in rows),flush=True)
