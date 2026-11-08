import json,time,uuid,urllib.request,urllib.error,sys,os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
URL=os.getenv('R52_TEST_URL','http://127.0.0.1:8093');LABEL=sys.argv[1]
def request(path,payload=None):
    r=urllib.request.Request(URL+path,data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None,headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(r,timeout=30) as response:return response.status,json.load(response)
    except urllib.error.HTTPError as response:return response.code,json.load(response)
def run(q,locale='en',session=None):
    session=session or 'r52-session-'+uuid.uuid4().hex;turn='r52-turn-'+uuid.uuid4().hex
    start=time.perf_counter();status,job=request('/api/chat/jobs',dict(question=q,locale=locale,debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id=turn))
    admitted=time.perf_counter()-start;states=[]
    if status==202:
        while job['status'] in ('queued','running'):
            if not states or states[-1]!=job['status']:states.append(job['status'])
            time.sleep(.25);_,job=request('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
    elapsed=time.perf_counter()-start
    result=job.get('result') or {};mode=result.get('mode','')
    row=dict(question=q,locale=locale,session_id=session,status=status,ack_sec=admitted,elapsed_sec=elapsed,states=states,job=job,
             transport_completed=job.get('status')=='completed',model_answer_delivered='general_llm_' in mode and 'unavailable' not in mode,within_20_sec=elapsed<=20)
    print(locale,round(elapsed,2),mode,q,flush=True)
    return row
if __name__=='__main__':
    cases=[
        ('อธิบายว่า ping ในเครือข่ายคืออะไรแบบสั้นๆ','th'),
        ('Explain network latency in one short paragraph.','en'),
        ('Why can high frame rate still feel choppy? Explain frame pacing briefly.','en'),
        ('Give three steps for learning touch typing.','en'),
        ('แปลประโยค Please check your network connection เป็นภาษาไทย','th'),
        ('Translate the Thai sentence กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต into English.','en'),
        ('Write a friendly two-sentence invitation to a group study session.','en'),
        ('Compare TCP and UDP, including one advantage and one disadvantage of each.','en'),
        ('Box A has 3 balls and box B has 5. Move 2 from B to A. How many are in each box? Explain briefly.','en'),
        ('อธิบายความแตกต่างระหว่าง RAM กับ SSD พร้อมข้อดีข้อเสีย ขอประมาณ 500 คำ','th'),
        ('Explain DNS, TCP, TLS, HTTP and latency in approximately 500 words.','en'),
    ]
    if LABEL.startswith('load'):
        n=int(sys.argv[2]);cases=[('Explain network latency briefly.','en')]*n
        with ThreadPoolExecutor(max_workers=n) as pool:rows=list(pool.map(lambda x:run(*x),cases))
    else:
        rows=[]
        for q,l in cases:
            row=run(q,l);rows.append(row)
            with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as stream:stream.write(json.dumps(row,ensure_ascii=False)+'\n')
        for l,q in [('th','ต้องการรู้ราคาการใช้บริการของบุคคลภายนอก'),('en','Service prices for external users')]:
            for follow in ['PC', 'all services' if l=='en' else 'ทั้งหมด']:
                session='r52-dialogue-'+uuid.uuid4().hex
                rows.append(run(q,l,session));rows.append(run(follow,l,session))
    with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as stream:json.dump(rows,stream,ensure_ascii=False,indent=2)
    print('transport',sum(r['transport_completed'] for r in rows),'model_answers',sum(r['model_answer_delivered'] for r in rows),'of',len(rows),flush=True)
