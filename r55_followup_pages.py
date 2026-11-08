import sys,json,time,uuid,urllib.request,urllib.error
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r55_current_path.txt').read_text());LABEL=sys.argv[1];URL='http://127.0.0.1:8093'
rows=[];ack={};sessions={}
def request(path,payload=None):
    req=urllib.request.Request(URL+path,data=json.dumps(payload,ensure_ascii=False).encode() if payload else None,headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=35) as f:return f.status,json.load(f)
    except urllib.error.HTTPError as f:return f.code,json.load(f)
def run(q,l,key):
    session=sessions.setdefault(key,'r55-near-'+uuid.uuid4().hex);start=time.perf_counter()
    code,job=request('/api/chat/jobs',dict(question=q,locale=l,debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id=uuid.uuid4().hex,last_seen_response_id=ack.get(key,'')))
    if code==202:
        limit=time.monotonic()+60
        while job.get('status') in ('running','queued') and time.monotonic()<limit:
            time.sleep(.15);_,job=request('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
    r=job.get('result') or {};ack[key]=r.get('request_id','');row=dict(question=q,locale=l,scenario=key,elapsed_sec=time.perf_counter()-start,job=job)
    rows.append(row)
    with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(l,key,round(row['elapsed_sec'],2),r.get('mode'),flush=True);return r,row
checks=[]
for l,initial,more in [('th','ขอกติกา CS2 ทั้งหมดทุกข้อ','ต่อ เอากฎที่เหลือ'),('en','Show all competition rules for CS2.','Continue with the remaining rules.')]:
    seen=set();expected=None;errors=[];key='full-rules-'+l
    for i in range(12):
        r,row=run(initial if not i else more,l,key);c=r.get('rule_coverage') or {}
        if not c:errors.append('missing_coverage');break
        returned=set(c.get('returned_ids',[]));expected=set(c.get('expected_ids',[]))
        if seen&returned:errors.append('repeated_sections')
        seen |= returned
        if seen==expected:break
    checks.append(dict(kind='pagination',locale=l,covered=len(seen),expected=len(expected or []),errors=errors+([] if seen==expected and len(seen)==56 else ['coverage_incomplete'])))
cases=[
 ('งบ 100 บาทเล่น PC ได้กี่ชั่วโมง','บุคคลทั่วไป','th',['1 แพ็กเกจ','เหลือ 30']),
 ('I have 100 THB for PC','general adult','en',['1 whole package','30 THB']),
 ('PC มีเกมไรให้เล่น','ทั้งหมดเลย','th',['VALORANT','Counter-Strike']),
 ('Which games are on Nintendo Switch?','all of them','en',['Mario Kart','Nintendo Switch']),
 ('2026-10-13 PC1 at 10:00 available?','what about PC2?','en',['PC #02','10:00']),
 ('Service prices for external users','PC','en',['70','25']),
 ('ขอราคาบุคคลทั่วไป','ทุกบริการ','th',['PC','PlayStation','Nintendo','Cockpit','VR']),
]
for i,(a,b,l,terms) in enumerate(cases):
    run(a,l,'dialogue-'+str(i));r,row=run(b,l,'dialogue-'+str(i))
    checks.append(dict(kind='dialogue',question=b,errors=['missing:'+t for t in terms if t.casefold() not in r.get('answer','').casefold()]))
single=[
 ('เงินมี100บาท คนทั่วไปจะเล่นคอมได้กี่รอบ','th',['1 แพ็กเกจ','เหลือ 30']),
 ('With a 100 baht budget, what can a general adult play?','en',['PC','30 THB']),
 ('I uploaded the incorrect payment slip. Where do I send the correct one?','en',['facebook.com/psuesportsphuket']),
 ('เพื่อนยังไม่ครบ เช็กอินแทนทั้งกลุ่มก่อนเลยได้มั้ย','th',['รายคน','มาก่อน']),
 ('We are a group of four. Which service do you recommend?','en',['Nintendo Switch']),
 ('Which identification documents should I take to the studio?','en',['passport']),
 ('ไปถึงเอาเอกสารอะไรเช็กอิน','th',['Passport']),
 ('คอมมีเกมไรบ้าง แล้วบุคคลทั่วไปเล่นสามชั่วโมงกี่บาท','th',['VALORANT','210']),
 ('What games are on PC and what is the general adult cost for three hours?','en',['VALORANT','210']),
 ('ชำระเงินยังไง แล้วจ่ายเงินสดได้หรือเปล่า','th',['ธนาคาร','ยังไม่มีข้อมูลยืนยัน']),
 ('Can I watch friends without playing, and does watching cost anything?','en',['watch','not been confirmed']),
 ('ติดตั้งเกม Minecraft เองได้มั้ย','th',['ยังไม่ได้ยืนยัน']),
 ('Can I install Minecraft myself?','en',['not been confirmed']),
 ('Can a player not listed on my booking take my place?','en',['named']),
 ('How do I reload my weapon in CS2?','en',['R: Reload']),
 ('ขอปุ่ม Tekken 8 ทั้งหมด','th',['ตัวละครทั่วไป']),
]
for i,(q,l,terms) in enumerate(single):
    r,row=run(q,l,'new-'+str(i));answer=r.get('answer','')
    errors=['missing:'+t for t in terms if t.casefold() not in answer.casefold()]
    if 'بشكل' in answer:errors.append('source_language_contamination')
    checks.append(dict(kind='paraphrase',question=q,errors=errors))
with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as f:json.dump(dict(rows=rows,checks=checks),f,ensure_ascii=False,indent=2)
print('CHECKS',len(checks),'FAIL',sum(bool(c['errors']) for c in checks),flush=True)
