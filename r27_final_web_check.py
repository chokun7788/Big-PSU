import json, time, sys, urllib.request, uuid
from pathlib import Path

base='http://127.0.0.1:'+sys.argv[1]
run=sys.argv[2]
report=Path(Path(__file__).with_name('r27_report_path.txt').read_text(encoding='utf-8'))
for attempt in range(30):
    try:
        health=json.load(urllib.request.urlopen(base+'/health',timeout=2))
        break
    except OSError:
        if attempt==29:raise
        time.sleep(.5)
assert health['runtime']['version']=='2026.10.01-competition-contract-r27-final'
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
cases.extend([
 ('th-technical-communication','th','VALORANT technical pause สื่อสารได้ไหม','valorant_psu_phuket_2026','focused'),
 ('en-technical-communication','en','Can players communicate during a VALORANT technical pause?','valorant_psu_phuket_2026','focused'),
 ('th-cs2-table','th','ขอตารางบทลงโทษ CS2','cs2_psu_phuket_2026','focused'),
 ('en-cs2-table','en','Show the CS2 penalty table','cs2_psu_phuket_2026','focused'),
 ('th-tekken-settings','th','Tekken 8 การตั้งค่าเกมเป็นยังไง','tekken8_psu_esports','focused'),
 ('en-tekken-settings','en','What are the Tekken 8 in-game settings?','tekken8_psu_esports','focused'),
 ('en-rov-ipad','en','Can I use a tablet or iPad in the RoV tournament?','rov_blueket_2025_men','focused'),
 ('en-cs2-team','en','How many players are in a CS2 team?','cs2_psu_phuket_2026','focused'),
 ('th-technical-duration','th','VALORANT technical pause ได้กี่นาที','valorant_psu_phuket_2026','focused'),
 ('en-technical-duration','en','How long is a VALORANT technical pause?','valorant_psu_phuket_2026','focused'),
 ('en-valo-penalties','en','What do the VALORANT tournament rules say about penalties?','valorant_psu_phuket_2026','focused'),
])
history=[];records=[];session='r26-web-'+uuid.uuid4().hex
cases.extend([
 ('th-age-gap','th','กติกา Tekken 8 อายุขั้นต่ำเท่าไร','','sourcegap'),
 ('en-age-gap','en','What is the Tekken 8 tournament minimum age requirement?','','sourcegap'),
 ('th-valo-penalties','th','กติกา VALORANT มีบทลงโทษประเภทไหนบ้าง','valorant_psu_phuket_2026','focused'),
 ('th-valo-penalties-typo','th','กติกกา VALORANT มีบทลงโทษประเภทไหนบ้าง','valorant_psu_phuket_2026','focused'),
 ('en-tournament-format-typo','en','Hi, What is the Tekken 8 tournamment format?','tekken8_psu_esports','focused'),
 ('en-tournament-ipad-typo','en','Hi, Can I use a tablet or iPad in the RoV tournamment?','rov_blueket_2025_men','focused'),
])
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
    elif kind=='sourcegap':
        if 'no_answer' not in mode:errors.append('source gap has fact answer mode')
        if response.get('route_category')!='competition_rules':errors.append('source gap wrong category')
        if '18' in answer:errors.append('age invented')
    elif kind=='catalog':
        if '42 เกม' not in answer:errors.append('catalog regression')
    elif kind=='booking':
        if response.get('route_intent')!='live_booking_status':errors.append('booking route regression')
        if 'ศูนย์ไม่เปิด' not in answer and 'ยังยืนยัน' not in answer:errors.append('closed day incorrectly free')
    first=answer.splitlines()[0] if answer else ''
    if kind=='focused' and key not in ('th-technical-duration','en-technical-duration') and not first.startswith('Answer:' if locale=='en' else 'คำตอบ:'):errors.append('first line is not a direct answer')
    if key.endswith('technical-communication'):
        required=('ห้าม','สื่อสาร','เว้นแต่ได้รับอนุญาต') if locale=='th' else ('may not communicate','unless permitted')
        if any(term not in first for term in required):errors.append('missing communication prohibition/exception in first line')
        if any(term in answer for term in ('60','Overtime','Tactical','Major Bug','10 นาที','10 minutes')):errors.append('wrong pause subtype details')
        if answer.casefold().count('สื่อสาร' if locale=='th' else 'communicate')!=1:errors.append('duplicate communication rule')
    if key.endswith('technical-duration'):
        if any(term in answer for term in ('60','2 timeouts','10 minutes','10 นาที','Tactical')):errors.append('unsupported technical duration borrowed from another pause type')
        if ('ยังไม่พบข้อกฎ' if locale=='th' else 'could not find a clause') not in answer:errors.append('missing explicit unsupported detail answer')
    if key=='en-valo-penalties':
        if any(answer.count(term)!=1 for term in ('Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit')):errors.append('missing/duplicate penalty type')
        if 'intent cannot be determined' not in answer:errors.append('missing rollback condition')
    if key.startswith('th-valo-penalties'):
        if any(answer.count(term)!=1 for term in ('Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit')):errors.append('missing/duplicate Thai penalty type')
        if any(term not in answer for term in ('ระบุเจตนาไม่ได้','เจตนาใช้ช่องโหว่','ความผิดครั้งแรก','ความผิดซ้ำ','ล็อกผล')):errors.append('missing Thai penalty condition')
    if key=='en-tournament-format-typo' and ('FT2' not in answer or 'two games' not in answer or not any(term in first for term in ('1v1','FT2'))):errors.append('lost direct tournament format after typo')
    if key=='en-tournament-ipad-typo' and ('may not be used' not in first or 'disqualification' not in first):errors.append('lost iPad prohibition after typo')
    if kind=='overview' and rulebook=='cs2_psu_phuket_2026' and '•    หยุดเกมโดยไม่ได้รับอนุญาต' in answer:errors.append('table cell used as independent rule')
    if key.endswith('cs2-table'):
        table=[line for line in answer.splitlines() if line.startswith('|')][2:]
        if len(table)!=9:errors.append('not nine complete table pairs')
        expected='| การหมิ่นศาสนา | แบนถาวร |' if locale=='th' else '| Offensive religious remarks | Permanent ban |'
        if not table or table[-1]!=expected:errors.append('missing/mismatched final penalty')
    if key.endswith('tekken-settings'):
        if '3' not in first or ('60 วินาที' if locale=='th' else '60 seconds') not in answer:errors.append('missing settings values')
    if key=='en-rov-ipad' and ('may not be used' not in first or 'disqualification' not in first):errors.append('not direct iPad prohibition')
    if key=='en-cs2-team' and '5 players' not in first:errors.append('missing first-line team size')
    if elapsed>20:errors.append('too slow')
    if response.get('validation_ok') is False:errors.append('validation rejected')
    history.extend([{'role':'user','text':question},{'role':'assistant','text':answer,'route_category':response.get('route_category'),'route_intent':response.get('route_intent'),'answer_language':locale}])
    records.append({'case':key,'question':question,'elapsed_sec':elapsed,'failures':errors,'response':response})
    print(json.dumps({'case':key,'elapsed_sec':elapsed,'mode':mode,'failures':errors,'answer':answer[:1100] if key.startswith('user-') else answer[:240]},ensure_ascii=False),flush=True)
result={'health':health,'cases':records,'passed':sum(not r['failures'] for r in records),'total':len(records)}
with (report/f'http_{run}.json').open('x',encoding='utf-8') as handle:json.dump(result,handle,ensure_ascii=False,indent=2)
if result['passed']!=result['total']:raise SystemExit(1)
