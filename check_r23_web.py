from pathlib import Path
import json, re, sys, time, urllib.request, uuid

report=Path(Path(__file__).with_name('r23_report_path.txt').read_text(encoding='utf-8'))
base='http://127.0.0.1:'+sys.argv[1]
run=sys.argv[2]
for attempt in range(20):
    try:
        health=json.load(urllib.request.urlopen(base+'/health',timeout=2))
        break
    except OSError:
        if attempt==19:raise
        time.sleep(.5)
assert health['runtime']['version']=='2026.10.01-available-equipment-r23'
transport=health['runtime']['booking']['fetch_mode']
assert transport in ('wordpress','dashboard')
cases=[
 ('user-exact','th','ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง','free'),
 ('thai-time-word','th','ตอนบ่ายสามมีอุปกรณ์อะไรว่างให้เล่นบ้าง','free'),
 ('english-equivalent','en','Which devices are free at 3pm?','free'),
 ('zone-status','th','PC ว่างไหมตอนบ่าย3','zone'),
 ('friday-maintenance','th','พรุ่งนี้ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง','closed'),
 ('static-inventory','th','มีอุปกรณ์อะไรบ้าง','static'),
]
records=[]
for key,locale,query,kind in cases:
    payload={'question':query,'locale':locale,'client_session_id':'r23-'+uuid.uuid4().hex,'recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
    req=urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode('utf-8'),{'Content-Type':'application/json; charset=utf-8'})
    started=time.perf_counter()
    response=json.load(urllib.request.urlopen(req,timeout=25))
    elapsed=round(time.perf_counter()-started,4)
    answer=response.get('answer','')
    trace=[t for t in response.get('trace',[]) if t['stage']=='live_booking_status']
    failures=[]
    if kind!='static':
        if response.get('mode')!='pipeline:live_booking_status_fast_path':failures.append('wrong live route')
        if not trace or trace[-1]['metadata'].get('transport')!=transport or trace[-1]['metadata'].get('cached') is not False or trace[-1]['metadata'].get('source')!='remote_csv_live':failures.append('not fresh data from the selected source')
        if '15:00-16:00' not in answer:failures.append('wrong time')
    if kind=='free':
        if 'ถูกจอง' in answer or ': booked' in answer or 'Gaming Monitor' in answer:failures.append('contains occupied resource or inventory')
        count=re.search(r':\s*(\d+)\s*(?:รายการ|resources)',answer)
        names=[line.strip().removeprefix('•').strip() for line in answer.splitlines() if line.strip().startswith('•')]
        if not count or int(count.group(1))!=len(names):failures.append('free count does not match list')
    elif kind=='closed':
        if 'ศูนย์ไม่เปิด' not in answer or '•' in answer:failures.append('closed period listed equipment')
    elif kind=='zone':
        if 'โซน PC' not in answer or 'PC #01' not in answer or 'PC #10' not in answer:failures.append('zone no longer lists all PCs')
    elif kind=='static':
        if trace or 'Gaming Monitor' not in answer:failures.append('inventory misrouted')
    if elapsed>20:failures.append('slow response')
    records.append({'case':key,'kind':kind,'question':query,'http_wall_sec':elapsed,'failures':failures,'response':response})
    print(json.dumps({'case':key,'mode':response.get('mode'),'http_wall_sec':elapsed,'failures':failures,'answer':answer if kind=='free' else answer[:600]},ensure_ascii=False),flush=True)
result={'health':health,'cases':records,'passed':sum(not r['failures'] for r in records),'total':len(records)}
(report/f'http_{run}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
if result['passed']!=result['total']:sys.exit(1)
