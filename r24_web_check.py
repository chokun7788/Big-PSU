import json, time, sys, urllib.request, uuid
from pathlib import Path

base='http://127.0.0.1:'+sys.argv[1]
run=sys.argv[2]
report=Path(Path(__file__).with_name('r24_report_path.txt').read_text(encoding='utf-8'))
for attempt in range(30):
    try:
        health=json.load(urllib.request.urlopen(base+'/health',timeout=2))
        break
    except OSError:
        if attempt==29:raise
        time.sleep(.5)
assert health['runtime']['version']=='2026.10.01-competition-r24'
cases=[
 ('user-cs2','th','กฏตอนเเข่ง cs2 มีอะไรมั่ง','cs2_psu_phuket_2026','overview'),
 ('user-rov','th','กฏตอนเเข่ง rov มีอะไรมั่ง','rov_blueket_2025_men','overview'),
 ('user-tekken','th','กฏตอนเเข่ง tekken 8 มีอะไรมั่ง','tekken8_psu_esports','overview'),
 ('user-valo','th','กฏตอนแข่งวาโลมีอะไรมั่ง','valorant_psu_phuket_2026','overview'),
 ('history-valo-to-tekken','th','กฏตอนเเข่ง tekken 8 มีอะไรมั่ง','tekken8_psu_esports','overview'),
 ('cs2-wrong-title-expansion','th','อยากทราบว่า สรุปกฎการแข่งขัน cs2 ทั้งหมด ครับ','cs2_psu_phuket_2026','overview'),
 ('rov-task-duplicate','th','อยากทราบว่า กติกกา rov มีอะไรบ้าง ครับ','rov_blueket_2025_men','overview'),
 ('en-cs2','en','What are the CS2 tournament rules?','cs2_psu_phuket_2026','overview'),
 ('en-rov','en','What are the RoV tournament ruls?','rov_blueket_2025_men','overview'),
 ('en-tekken','en','Tekken 8 rules overview please.','tekken8_psu_esports','overview'),
 ('en-valo','en','VALORANT ruules overview please.','valorant_psu_phuket_2026','overview'),
 ('en-settings','en','What do the CS2 tournament rules say about in-game settings?','cs2_psu_phuket_2026','focused'),
 ('en-tekken-identity','en','For Tekken 8, can you verify the rule on the rulebook scope and tournament identity?','tekken8_psu_esports','focused'),
 ('th-settings-prefix','th','สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ','tekken8_psu_esports','focused'),
 ('th-rov-disconnect-prefix','th','สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ','rov_blueket_2025_men','focused'),
 ('no-game-team','en','How many players can a team have?','','clarification'),
 ('ambiguous-procedure','en','What do the CS2 tornament rules say about in-march procedure','','clarification'),
 ('normal-catalog','th','มีเกมอะไรบ้าง','','catalog'),
 ('booking-regression','th','พรุ่งนี้ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง','','booking'),
]
history=[];records=[];session='r24-web-'+uuid.uuid4().hex
for key,locale,question,rulebook,kind in cases:
    payload={'question':question,'locale':locale,'recent_history':history[-10:] if key.startswith('user-') or key.startswith('history-') else [],'client_session_id':session,'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
    started=time.perf_counter()
    response=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
    elapsed=round(time.perf_counter()-started,4);answer=response.get('answer','');mode=response.get('mode','');errors=[]
    urls=[source.get('url','') for source in response.get('sources',[])]
    if kind in ('overview','focused'):
        if response.get('route_category')!='competition_rules':errors.append('wrong category')
        if not urls or not all('competition_rules_'+rulebook in url for url in urls):errors.append('wrong or missing game source')
        if '42 เกม' in answer or '42 games' in answer or 'English below' in answer:errors.append('metadata/catalog answer')
        if kind=='overview' and (mode!='pipeline:competition_rule_overview_source' or answer.count('•')<3):errors.append('not substantive overview')
    elif kind=='clarification':
        if 'clarif' not in mode:errors.append('not clarification')
    elif kind=='catalog':
        if '42 เกม' not in answer:errors.append('catalog regression')
    elif kind=='booking':
        if response.get('route_intent')!='live_booking_status':errors.append('booking route regression')
        if 'ศูนย์ไม่เปิด' not in answer and 'ยังยืนยัน' not in answer:errors.append('closed day incorrectly free')
    if elapsed>20:errors.append('too slow')
    if response.get('validation_ok') is False:errors.append('validation rejected')
    history.extend([{'role':'user','text':question},{'role':'assistant','text':answer,'route_category':response.get('route_category'),'route_intent':response.get('route_intent'),'answer_language':locale}])
    records.append({'case':key,'question':question,'elapsed_sec':elapsed,'failures':errors,'response':response})
    print(json.dumps({'case':key,'elapsed_sec':elapsed,'mode':mode,'failures':errors,'answer':answer[:1100] if key.startswith('user-') else answer[:240]},ensure_ascii=False),flush=True)
result={'health':health,'cases':records,'passed':sum(not r['failures'] for r in records),'total':len(records)}
with (report/f'http_{run}.json').open('x',encoding='utf-8') as handle:json.dump(result,handle,ensure_ascii=False,indent=2)
if result['passed']!=result['total']:raise SystemExit(1)
