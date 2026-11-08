import json,re,statistics
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r43_current_path.txt').read_text());OLD=Path((BASE/'r42_current_path.txt').read_text())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,value):
 with (OUT/name).open('x',encoding='utf-8') as f:
  if isinstance(value,str):f.write(value)
  else:json.dump(value,f,ensure_ascii=False,indent=2)
summaries=[(p,read(p)) for p in sorted(OUT.glob('final_r43_3_*_summary.json'))];assert len(summaries)==4
assert all(j['passed']==j['executed_cases'] and j['health']['runtime']['version']=='2026.10.06-readiness-schedule-r43.3' for _,j in summaries)
units=read(sorted(OUT.glob('source_regression_*.json'))[-1]);assert len(units)==10 and all(r['returncode']==0 for r in units)
counts=[int(re.search(r'Ran (\d+) tests?',(OUT/r['evidence']).read_text()).group(1)) for r in units];assert sum(counts)==159
audit=read(OUT/'SOURCE_AUDIT_R43_FINAL.json');assert not audit['unexpected_changes'] and all(audit['protected_unchanged'].values()) and all(r['returncode']==0 for r in audit['git'])
reuse=read(OUT/'REAL_REUSE_R43_3.json');assert all(reuse['checks'].values());health=reuse['after']
cases=sum(j['executed_cases'] for _,j in summaries);requests=sum(j['requests'] for _,j in summaries);assert (cases,requests)==(72,131)
latencies=[r['elapsed_sec'] for _,j in summaries for case in j['results'] for r in case['records'] if r['status']==200]
latencies.sort();metrics=dict(median=statistics.median(latencies),p95=latencies[int(.95*(len(latencies)-1))],maximum=max(latencies))
save('FINAL_AUTOMATED_GATES_R43.json',dict(version=health['runtime']['version'],unit_methods=159,http_scenarios=72,http_requests=131,http_passed=72,source_audit='SOURCE_AUDIT_R43_FINAL.json',real_reuse='REAL_REUSE_R43_3.json',unit_results=units,http_evidence=[p.name for p,_ in summaries],latency_sec=metrics,not_proven=['MemoryError sole root cause or recovery under load','all-corpus semantic completeness','real occupancy oracle','current owner policy','clean-machine portable distributions']))
table='\n'.join(f"| {j['label']} | {j['passed']}/{j['executed_cases']} | {j['requests']} | [{p.name}]({p.as_posix()}) |" for p,j in summaries)
save('FLOW_R43_FINAL.md','''# Flow r43 ฉบับตรวจทาน: Runtime พร้อมจริงและ Scope ของตารางภาษาอังกฤษ

## หลักฐานที่ใช้และขอบเขต

ใช้ source/calendar เดิมและคำยืนยันเดิมว่า 12:00–13:00 ไม่มีให้จอง ไม่แก้ตารางเจ้าของ ราคา หรือกฎการแข่งขัน การทำงานเป็น local candidate บนเครื่องนี้ ไม่ใช่การรับรองชุดแจกหรือข้อเท็จจริงปัจจุบันทั้งหมด

```mermaid
flowchart TD
    A[อ่าน source และสำรองไฟล์/hash] --> B[เลือก Python และตรวจรุ่น/64-bit]
    B --> C{มีเว็บของชุดเดียวกันหรือไม่}
    C -->|มี| D[ตรวจ package + Python + warmup + preflight + worker]
    C -->|ไม่มี| E[เปิด child ด้วย Python ที่เลือก เก็บ log ใหม่]
    E --> D
    D -->|ไม่ผ่าน| F[บันทึกเหตุผล ไม่เปิด browser เก็บ process/log]
    D -->|ผ่าน| G[POST คำถามจริงใน synthetic session]
    G --> H{ตอบ oracle 1 ชั่วโมงจริง ไม่ timeout และ validation ผ่าน}
    H -->|ไม่ผ่าน| F
    H -->|ผ่าน| I[เปิดเว็บหรือใช้ process เดิม]
    I --> J[รับคำถามและตรวจ operation ที่ระบุชัดก่อนตีคำว่า all/every]
    J --> K{เรื่องเวลา หรือคำตอบเติมราคา}
    K -->|opening/service hours| L[render timetable จาก regular_service_slots]
    K -->|all services 2 hours| M[เติม service scope + duration ใน price task]
    K -->|all ไม่มีบริบท| N[ถาม scope ที่ยังขาด]
    L --> O[วันที่เฉพาะใช้ closure override; แยกตารางจากจองสด]
    M --> P[ตรวจ task/targets/units และคำตอบ]
    O --> Q[Targeted HTTP + source regressions + วิเคราะห์ failures]
    P --> Q
    Q -->|พบปัญหา| J
    Q -->|ผ่าน| R[freeze release ใหม่ + parity + report + backlog]
```

## การเลือก Python

ลำดับ explicit `-PythonPath` → `PSU_PYTHON_EXE` → bundled runtime → manifest binding → PATH/fallback ตรวจด้วย executable จริง แล้วส่ง path เดิมผ่าน Background → Open → Start ตัว Python ตรวจรุ่น 3.11+ และ 64-bit การตรวจผ่านยังไม่รับรอง dependencies/ทุก Python รุ่นบนเครื่องใหม่

health แสดง executable path fingerprint, version, bitness, PID และ system memory โดยไม่แสดง absolute interpreter path ใน health ตัว diagnostic launcher สำหรับผู้ดูแลเก็บ path จริง Manifest ของ r43.3 ผูก Ready Python 3.12.14 บนเครื่องนี้ จึงห้ามอ้างว่าโฟลเดอร์ local นี้แจกไปใช้ได้ทันทีบนเครื่องอื่น

## Readiness และการใช้เว็บเดิม

ต้องผ่านชื่อบริการ version installation fingerprint Python identity parent warmup/preflight และ worker alive/ready แล้ว POST คำถาม `How far ahead must I book?` ด้วย Session ID `startup-probe-*` คำตอบต้องเป็น booking_advance_time, rule_en, validation_ok และมี at least 1 hour พร้อม source URL HTTP 200 หรือ confidence สูงไม่ใช่เกณฑ์ผ่าน

ใช้หนึ่ง oracle ที่มีอยู่ใน source เพื่อเช็กการตอบจริงผ่าน HTTP/worker ไม่ยืนยันทุก intent หรือว่า LLM ยังใช้ได้ในคำขอถัดไป Probe เป็น audit exchange แยก session แต่เก็บใน log จึงต้องแยก prefix นี้เมื่อวิเคราะห์ผู้ใช้

ถ้า instance ของชุดเดียวกันไม่พร้อม ตัวเปิดรายงานสาเหตุและไม่สร้าง instance เพิ่มโดยเงียบ ไม่ฆ่า process ที่เปิดอยู่ หาก process ที่เพิ่งเปิดไม่พร้อม จะเก็บไว้พร้อม diagnostic ให้ตรวจ การกู้/cleanup อัตโนมัติแบบตรวจ ownership และ worker-stage ยังเป็นงานต่อ

## การรักษา scope

คำว่า all/every ใช้กับ operation ที่ระบุในคำถาม ห้ามตีเป็นราคาโดยไม่มีหลักฐาน เช่น opening hours for every day ต้องเป็นตาราง ทั้งกรณีถามครั้งแรกและหลังคุยราคา ส่วน all services 2 hours หลังราคาเป็นราคาเดิมพร้อม duration ไม่ใช้ hours เพียงคำเดียวเป็นตัวเปลี่ยนไปหมวด schedule

ตารางประจำอังกฤษแสดง 7 วันจาก shared calendar: slot เปิดและ maintenance แยกกัน พักกลางวัน 12:00–13:00 ไม่มีเล่น/จอง และ no regular service สำหรับเสาร์/อาทิตย์ วันที่เฉพาะใช้ recorded closure override โดย public holiday ไม่ทำให้ปิดอัตโนมัติ ตารางนี้ไม่ใช่ความว่างของแต่ละเครื่อง

## รอบตรวจทานและปรับ Flow

1. Baseline: generic English hours ไม่มีช่วงเวลาครบ จึงเปลี่ยน renderer ใช้ shared slots; fixture พบ PowerShell 5.1 ทำ quote ของ Python หาย แก้ native argument ที่รองรับทั้ง 5.1/7; ปัญหา temp directory ของ sandbox แก้เฉพาะ harness
2. Review runtime: health อย่างเดียวไม่พอ เพิ่ม actual POST/oracle, runtime identity และ memory snapshot; ทดลองใน sandbox แล้ว HTTP หายหลัง tool จบ จึงเปิด persistent runtime ผ่าน permission ระบบ และตรวจ HTTP หลังจบคำสั่งอีกครั้ง
3. HTTP r43.2: ผ่าน 14/15 แต่ every day ถูก price plan แย่ง scope เพิ่ม explicit schedule operation signals พร้อม negative guard สำหรับ duration ราคา; r43.3 ผ่าน 17/17 กลุ่มตาราง และชุดเกี่ยวข้องรวม 72/72; source/fixture 159/159 พร้อม reuse process จริง
4. Review ส่งมอบ: แก้คู่มือให้ตรงการรันเบื้องหลัง ตรวจ Git EOF/parity/hash แยก local binding จาก portable และคง failed artifacts/release เดิมไว้ ไม่เปลี่ยน owner facts

## สิ่งที่ต้องพัฒนาต่อ

worker warmup บาง exception ยังถูก catch แล้ว ready.set; probe static หนึ่งข้อไม่รับรอง retrieval/LLM ทุกเส้นทาง ต้องเพิ่ม stage diagnostics และ controlled recovery ภายหลัง การสรุป root cause MemoryError ต้องเก็บ resource/error ใกล้เหตุการณ์ ไม่ใช้การ restart ผ่านแทนข้อพิสูจน์ Operation/scope ownership ของหมวดอื่นต้องตรวจ holdout ที่ไม่ใช้พัฒนา และ content completeness ต้องมี oracle ราย fact
''')
save('CASE_ANALYSIS_R43_TH.md','''# วิเคราะห์ปัญหา r43 จากหลักฐานจริง

## 1. ข้อมูลเวลาอยู่ครบ แต่ generic English ตอบไม่ครบ

Baseline `_answer_schedule` ใช้ branch weekday=None ซึ่งตอบเพียง Monday-Friday และให้เลือกวัน คำตอบไม่เข้าถึง renderer ของ slot รายวัน ข้อมูลไม่ได้ขาดและไม่มีเหตุให้ผู้ใช้ระบุวันเพิ่มเมื่อเขาขอตารางทั้งหมด แก้เป็นสรุป 7 วันจาก regular_service_slots พร้อม maintenance/lunch/closure guards

## 2. ระบุ “every day” แล้วกลับถาม scope

HTTP r43.2 เคส `Please list opening hours for every day.` ให้ `All of which topic or service would you like to see?` mode conversation_scope_clarification, confidence ของ guard ไม่ใช่คะแนนว่าข้อมูลปฏิทินผิด request_plan มี act=ambiguous, tasks=[], missing=scope และ metadata context_domain=service_fee ไม่มี source hits

สาเหตุ: price conversation planner มี ALL regex ที่ตรง every แต่ OTHER_TASK รับ open ไม่รับ opening/hour schedule เมื่อ price=False จึงเข้าสาขา all_selected ไม่มีบริบทก่อนเข้าตัวตอบ schedule ทำให้ไม่ได้อ่านข้อมูลเวลาเลย ควรตอบตารางประจำทุกวันพร้อมช่วงเปิด/maintenance ไม่ใช่ถามว่าทั้งหมดเรื่องอะไร

แก้ด้วย explicit schedule operation signals ก่อนใช้ all/every เพื่อเลือกราคา ไม่เพิ่ม alias ของทั้งประโยค และไม่ใช้คำ hours เดี่ยวเพื่อเปลี่ยนหมวด เพราะ 2 hours อาจเป็น duration ของราคา ทดสอบทั้งถามเดี่ยว ถามหลังราคา และ all services 2 hours เพื่อไม่แก้เคสหนึ่งแล้วทำอีกเคสเสีย

## 3. เปิดเว็บจาก health ผ่าน แต่ยังไม่พิสูจน์ตอบได้

ตัวเปิดเก่าตรวจ service/version/installation เท่านั้น จึง reuse instance ที่ warmup/preflight/worker/Python ไม่เหมาะสมได้ เพิ่ม guards และ POST ผ่าน worker จริง Fixture HTTP500, HTTP200 timeout, คำตอบจำนวนชั่วโมงผิด, validation false, wrong installation/Python, warmup/preflight fail และ worker ตาย ต้องไม่เปิด browser หรือ reuse แบบ ready

Readiness เป็น snapshot ของ source oracle ข้อเดียว พิสูจน์จริงว่าคำขอนี้ตอบถูก แต่ยังไม่ใช่ความถูกต้องของทุกคำถาม/current booking/LLM จึงคงงาน content/load/recovery แยกไว้

## 4. Windows PowerShell 5.1 กับ Python command quoting

โค้ด Python สำหรับตรวจ identity ใช้ double quoted literals ภายใน -c ซึ่ง PowerShell 5.1 native argument forwarding ทำเครื่องหมาย quote หาย ทั้งที่รันผ่าน PowerShell 7 ได้ เปลี่ยนเป็น single quoted Python literals แล้วทดสอบผ่าน powershell.exe จริง Path ที่มีช่องว่างไม่ถูกแยก และ explicit path ถูกส่งผ่านสามตัวเปิด

## 5. แยก environment/harness ออกจากบั๊กตอบคำถาม

Fixture รอบแรกสร้าง temp ใต้ AppContainer temp แล้วเขียนไฟล์ไม่ได้ เป็นปัญหาสิทธิ์ harness แก้ให้ใช้ test output root ที่เขียนได้ ไม่ใช่ chatbot ตอบผิด การเปิด sandbox r43.1 ผ่าน readiness แต่หลัง tool จบเชื่อม HTTP ไม่ได้ จึงเปิด r43.2/3 ผ่านระบบ permission แล้วตรวจซ้ำหลัง tool จบเพื่อยืนยัน process อยู่จริง

Git ใน sandbox อ่าน parent repository root ไม่ได้ เก็บ output fatal เดิมไว้ ใช้ read-only escalation แล้วตรวจ diff พบ blank EOF ในคู่มือที่เพิ่ม แก้เฉพาะ newline ก่อน freeze r43.3; Git status/diff-check สุดท้าย exit0

หน่วยความจำจริงระหว่างร43ใช้สูง 94–96% จึงเพิ่ม available physical/commit snapshot ใน health ไม่อ้างว่า Python 3.13 เป็นสาเหตุเดียว หรือ pin 3.12 แล้ว MemoryError ถูกแก้ถาวร

## ตัวอย่างคำตอบจริงของเคสที่แก้และเคสกัน regression

'''+ '\n\n'.join('### '+c['id']+'\n\nคำถาม: '+ ' → '.join(c['turns'] if 'turns' in c else [r['payload']['question'] for r in c['records']])+'\n\nMode: '+str(c['mode'])+'\n\n'+c['answer'] for p,j in summaries if 'schedule' in j['label'] for c in j['results']))
backlog=read(OLD/'BACKLOG_STATUS_R42.json')
notes={'B001':'r43.3 ตรวจ installation+version+Python และ actual readiness ก่อน reuse; ยังมีไฟล์รุ่นเก่าให้ผู้ใช้เปิดได้',
 'B002':'สร้าง local r43.3 ใหม่เท่านั้น ชุดแจก WithModels/DownloadModels ยังไม่ rebuild',
 'B004':'คู่มือ local และพฤติกรรมตัวเปิดปรับตรงกัน ผ่าน launch/reuse จริง; คู่มือของชุดเก่าไม่ได้ทับ',
 'B007':'แก้ price planner แย่ง all/every ของ explicit schedule; ยังไม่ใช่ typed ownership ทุก operation',
 'B019':'ตารางประจำอังกฤษครบ 7 วัน/maintenance/lunch และ targeted questions; ยังไม่ครอบคลุมอังกฤษทุกหมวด'}
for r in backlog:
 r['r43_status']='partially_implemented_or_targeted_verified' if r['id'] in notes else 'not_reassessed_in_this_round'
 r['r43_note']=notes.get(r['id'],'คงข้อมูลและสถานะเดิม; ไม่มีหลักฐาน r43 ว่าปิดรายการนี้ครบ')
save('BACKLOG_STATUS_R43.json',backlog)
remaining='''# รายการที่เหลือ r43 — แยกงานทำเองจากข้อเท็จจริงเจ้าของ

## ลำดับถัดไป

| ลำดับ | สิ่งที่ยังเหลือ | ทำเองได้ / ข้อมูลที่ต้องมี |
|---|---|---|
| P0 | MemoryError/แรงกดดันหน่วยความจำ และ worker warmup exception บางส่วนไม่แสดง health | ทำ stage diagnostics + controlled crash/recycle/cleanup/recovery ได้; ไม่เปลี่ยน pagefile หรือฆ่าโปรแกรมอื่นโดยเดา |
| P0 ข้อมูล | ราคาปัจจุบัน, Tekken pause conflict, RoV clauses ขาด, เพดานวันล่วงหน้า/จำนวนเครื่อง | ต้องต้นฉบับหรือเจ้าของ; guard missing/conflict ยังต้องอยู่ |
| P1 | Explicit scope ของหมวดอื่น และ required facts/units/conditions ในคำตอบ | เพิ่ม source oracles/holdout; schedule ผ่านไม่แปลว่าทุก all/every ถูกหมด |
| P1 | เพิ่มวันเวลาใหม่ตอนกลับไปเรื่องเก่า/ข้อความหลายหัวข้อ/ภาษาและ typo ที่ไม่เคยใช้พัฒนา | typed filters + semantic holdout และ negative cases; ไม่รัน full20k โดยไม่จำเป็น |
| P1/P2 | LLM/retrieval พร้อมทุกเส้นทางจริงและ concurrent load/recovery | static startup probe และ invariant tests ไม่เป็น SLA; ต้องทดสอบเฉพาะเส้นทางเพิ่มเติม |
| P2 | ชุดแจก WithModels/DownloadModels รุ่นใหม่ และ clean-machine launch | build ทำเองได้; local r43.3 ผูก Python absolute path ของเครื่องนี้ ไม่ใช่ portable package |
| P2 | log retention/หลายผู้ใช้/production permissions | log lifecycle fixture ทำได้เอง; นโยบายเก็บข้อมูลจริงต้องเจ้าของกำหนด |

## คำถามที่ยังต้องเจ้าของตอบ

1. เพดานการจองล่วงหน้าสูงสุดกี่วัน นับจากวันเวลาไทยหรือวันที่เปิดรอบ และต่างกันตามบริการหรือกลุ่มผู้ใช้ไหม?
2. หนึ่งรายการจองเลือกเครื่องพร้อมกันได้สูงสุดกี่เครื่อง? เพดาน 3 Sessions ใช้แทนจำนวนเครื่องไม่ได้
3. ราคาที่มีผลหลัง 31 มีนาคม 2026 ใช้ฉบับใด วันเริ่มใช้และข้อยกเว้นคืออะไร?
4. Tekken pause/penalty ใช้ข้อความฉบับใดเมื่อขัดกัน และ RoV 6.1.5–6.1.5.1 ฉบับเต็มเป็นอย่างไร?
5. เมื่อพร้อมเก็บจองจริง ขอ snapshot ที่ผูกวัน/เวลา/เครื่องกับเฉลยจากผู้ดูแล เพื่อพิสูจน์ว่าง/ถูกจอง ไม่ใช้ API200 เป็นเฉลย

## รายการ 66 ข้อเดิมที่รักษาไว้

ไม่ได้ประเมินซ้ำทุกข้อในร43 จึงไม่ใช้ targeted pass ลบรายการอื่นออก รายละเอียดและเหตุผลเดิมอยู่ใน BACKLOG_STATUS_R43.json

'''
remaining+='\n\n'.join(f"### {r['id']} — {r['title']}\n\n- การดำเนินการ: {r['disposition']}\n- สถานะร43: {r['r43_status']}\n- หลักฐาน/ขอบเขต: {r['r43_note']}\n- หมายเหตุจากงานเดิม: {r['execution_note']}" for r in backlog)
save('REMAINING_ISSUES_R43_TH.md',remaining)
save('REPORT_R43_3_TH.md',f'''# ผลงาน r43.3 — 6 ตุลาคม 2026 (Asia/Bangkok)

## แก้แล้ว

- ตัวเปิดเลือก Python หนึ่งตัวและส่ง path เดิมผ่านทุกขั้นตอน ทดสอบกับ Windows PowerShell 5.1 จริง แก้ native quoting ที่ทำให้ตรวจ Python ล้มเหลว
- ก่อนเปิดเว็บ/reuse ตรวจ package+Python+warmup+LLM preflight+worker แล้ว POST คำถามจริงพร้อม content oracle; HTTP200/health ok อย่างเดียวไม่ผ่าน
- health เพิ่ม Python version/bitness/PID/fingerprint และ available physical/commit memory; launcher เก็บ readiness diagnostic แยก run ID
- คำถามอังกฤษเวลาเปิดแบบกว้างตอบครบ 7 วัน ช่วงเปิด/maintenance พักเที่ยง และข้อยกเว้นจาก calendar เดิม
- แก้ `Please list opening hours for every day.` ที่ price planner แย่งคำว่า every จนถาม scope ทั้งที่ระบุเรื่องแล้ว พร้อมกัน regression สำหรับ `all services 2 hours`
- คู่มือ local ตรงการรันเบื้องหลังและการตรวจพร้อม ไม่ต้องคงหน้าต่างคำสั่งของตัวเปิดปกติ; เครื่องยังต้องเปิดอยู่

## ผลตรวจอัตโนมัติ

- Source/fixture 159/159 test methods ใน 10 ไฟล์ รอบสุดท้ายหลังแก้ source
- HTTP 72/72 scenarios / 131 requests บน r43.3 จริง โดยตรวจเนื้อหา/operation/scope ของเคสที่เกี่ยวข้อง ไม่รัน full20k
- เปิด launcher ซ้ำจริงผ่าน: server PID เดิม, worker PID เดิม, ไม่มี stdout log ของ launcher ใหม่ และ POST readiness ใหม่ผ่าน
- app/web parity 140/140, launcher/document parity 5/5, knowledge parity 22/22, owner/data/rates hash เดิม 5/5
- 7 ไฟล์เดิมเปลี่ยนเฉพาะ scope งาน + 3 ไฟล์ใหม่; backup 312 hashes, ไม่มีไฟล์ก่อนรอบหาย; Git status/diff-check ที่อ่านผ่านระบบ permission exit0

| ชุด HTTP | ผ่าน | Requests | หลักฐาน |
|---|---|---|---|
{table}

Latency คำขอในชุดนี้: median {metrics['median']:.3f}s / P95 {metrics['p95']:.3f}s / max {metrics['maximum']:.3f}s ไม่ใช่ SLA หลายผู้ใช้

## ข้อผิดพลาดที่พบและเก็บไว้

Baseline ตารางอังกฤษไม่ครบ; fixture เจอ PowerShell 5.1 quoting และ sandbox temp permissions; r43.2 HTTP ตาราง 14/15 เพราะ every day ถูก price plan; ทุก raw/summary/failed log และ release r43.1/r43.2 ยังอยู่ ไม่มีการทับเพื่อให้ผลดูผ่าน ดู CASE_ANALYSIS_R43_TH.md

## ยังไม่ได้ยืนยัน

เครื่องใช้หน่วยความจำสูงช่วงตรวจ 94–96% ยังไม่ได้พิสูจน์ root cause เดียวของ MemoryError หรือกู้ได้ทุกภาวะโหลด worker warmup บาง exception ยังถูก catch แล้วตั้ง ready; actual probe static หนึ่งข้อไม่รับรองทุก LLM/RAG path คงไว้เป็น P0 ต่อ

สถานะจองจริง/current prices/conflicting or incomplete rules/official English names ยังต้องหลักฐานเจ้าของ; fixture และ API connected ไม่เป็นความจริงการจองในปัจจุบัน ชุดแจก WithModels/DownloadModels และเครื่องสะอาดยังไม่ยืนยัน local manifest นี้ใช้ path Python ของเครื่องนี้

## ใช้งานรุ่นที่ตรวจ

- เว็บ [เปิด r43.3](http://127.0.0.1:8090/) — version `{health['runtime']['version']}`
- [ตัวเปิดเบื้องหลัง]({(OUT/'release_r43_3/PSU_Esports_Chatbot_Local/Open-PSU-Esports-Background.cmd').as_posix()})
- [Flow ฉบับสมบูรณ์]({(OUT/'FLOW_R43_FINAL.md').as_posix()})
- [วิเคราะห์สาเหตุและคำตอบจริง]({(OUT/'CASE_ANALYSIS_R43_TH.md').as_posix()})
- [รายการที่เหลือทั้งหมด]({(OUT/'REMAINING_ISSUES_R43_TH.md').as_posix()})
- [Gates]({(OUT/'FINAL_AUTOMATED_GATES_R43.json').as_posix()}) และ [Source audit]({(OUT/'SOURCE_AUDIT_R43_FINAL.json').as_posix()})
''')
print(OUT,'units',sum(counts),'http',cases,requests,'backlog',len(backlog),metrics)
