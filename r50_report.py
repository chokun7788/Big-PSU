import json,collections,re,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text());SHARE=Path((OUT/'share_path.txt').read_text())
def read(name):return json.loads((OUT/name).read_text(encoding='utf-8-sig'))
def save(name,value):
 with (OUT/name).open('x',encoding='utf-8') as f:f.write(value)
def link(name):return f'[{name}](<{OUT/name}>)'
baseline=next(OUT.glob('R50_LOAD_BASELINE_*summary.json'));final=next(OUT.glob('R50_LOAD_FINAL_*summary.json'));confirm=next(OUT.glob('R50_LOAD_MIXED_CONFIRM_*summary.json'))
loads=[read(x.name) for x in [baseline,final,confirm]]
aggregate=[]
for load in loads:
 raw=[json.loads(line) for line in (OUT/load['raw_file']).read_text(encoding='utf-8').splitlines()]
 errors=collections.Counter((x['profile'],str(x['status']),x['response'].get('timing_status',''),x['response'].get('error','')) for x in raw if x['status']!=200)
 aggregate.append(dict(label=load['label'],requests=len(raw),correct=sum(x['correct'] for x in raw),errors=[dict(profile=k[0],http=k[1],timing=k[2],error=k[3],count=v) for k,v in errors.items()],levels=load['profiles']))
save('LOAD_ANALYSIS_R50.json',json.dumps(aggregate,ensure_ascii=False,indent=2))
# Public debug=False responses intentionally omit context_resolution. Regrade
# existing answers against the public resolved question and content; preserve
# the original failed oracle and all network evidence without rerunning.
context=read('HTTP_PARALLEL_CONTEXT_R50.json');regraded=[]
for row in context['results']:
 a=row['follow'];b=a['response'];en=row['en'];parking=row['parking']
 expected=('not been specified' if en else 'ยังไม่ได้ระบุค่าจอดรถ') if parking else ('not been confirmed' if en else 'ยังไม่ได้ยืนยันสิทธิ์นำจอย')
 checks=dict(http=a['status']==200,content=expected in b.get('answer',''),session=b.get('session_id')==a['payload']['client_session_id'],resolved_topic=('parking' in b.get('resolved_question','').lower() or 'ค่าจอดรถ' in b.get('resolved_question','')) if parking else ('controller' in b.get('resolved_question','').lower() or 'จอย' in b.get('resolved_question','')),no_timeout=not b.get('timed_out'))
 regraded.append(dict(session_id=a['payload']['client_session_id'],checks=checks,passed=all(checks.values()),elapsed_sec=a['elapsed_sec'],answer=b.get('answer'),resolved_question=b.get('resolved_question')))
save('HTTP_PARALLEL_CONTEXT_REGRADED_R50.json',json.dumps(dict(original_file='HTTP_PARALLEL_CONTEXT_R50.json',original_oracle_error='Required debug-only context_resolution in debug=False HTTP responses; original 0/4 is an oracle error. No application code or network records changed.',total=4,passed=sum(x['passed'] for x in regraded),results=regraded),ensure_ascii=False,indent=2))
assert all(x['passed'] for x in regraded),regraded
def table(load):
 lines=['| ประเภท | คนส่งพร้อมกัน | ถูกต้อง/คำขอ | p50 (s) | p95 (s) | สูงสุด (s) | HTTP 503 | PID เปลี่ยน | ผ่านเกณฑ์ |','|---|---:|---:|---:|---:|---:|---:|---|---|']
 for x in load['profiles']:
  lines.append(f"| {x['profile']} | {x['users']} | {x['correct']}/{x['requests']} | {x['success_p50']:.2f} | {x['success_p95']:.2f} | {x['success_max']:.2f} | {x['http_errors'].get('503',0)} | {'ใช่' if x['worker_pids_before']!=x['worker_pids_after'] else 'ไม่'} | {'ผ่าน' if x['acceptable'] else 'ไม่ผ่าน'} |")
 return '\n'.join(lines)
v1=read(next(OUT.glob('R50_SOURCE_V1_*summary.json')).name);v2=read(next(OUT.glob('R50_SOURCE_V2_*summary.json')).name)
failure_details=[]
for before in v1['results']:
 if before['passed']:continue
 after=next(x for x in v2['results'] if x['id']==before['id'])
 failure_details.append(f"### {before['id']}\n\n- คำถาม: {before['records'][-1]['payload']['question']}\n- ก่อนแก้: `{before['mode']}` — {before['answer']}\n- หลังแก้: `{after['mode']}` — {after['answer']}\n- เกณฑ์ที่ไม่ผ่านก่อนแก้: {', '.join(k for k,v in before['checks'].items() if not v)}\n")
save('FAILURE_DETAILS_R50.md','# คำถามที่ผิดก่อนแก้และคำตอบหลังแก้ r50\n\n'+ '\n'.join(failure_details))
flow='''# Flow ฉบับสุดท้าย r50: คำตอบตามขอบเขต ความจำ และโหลดพร้อมกัน

วันที่ 2026-10-09 เวลาไทย · Runtime 2026.10.09-flow-r50.2

## 1. สถานะและเป้าหมาย

- สถานะจองจริง: ผู้ใช้ยืนยันว่าตรวจถูกต้องแล้ว เก็บคำยืนยันแยกจากผลอัตโนมัติ
- ภาษาอังกฤษ: ผู้ใช้แจ้งผ่านแล้ว งานนี้เพิ่ม regression TH/EN เฉพาะส่วนที่แก้
- เป้าหมาย: ให้คำถามเดิมหลายสำนวนเข้าหัวข้อถูก รักษาเงื่อนไขคำถามต่อ ฟื้นบริบทหลัง restart และวัดโหลดบนเครื่องจริง
- ใช้สำเนารุ่นใหม่และหลักฐานใหม่ เก็บโค้ดที่ Git ยังไม่บันทึกและ log ก่อนหน้าไว้ ไม่แก้นโยบาย/ข้อมูลเจ้าของเพื่อให้คะแนนดีขึ้น

## 2. Flow เมื่อรับข้อความ

```mermaid
flowchart TD
 A[รับ input + locale + session ID + turn ID] --> B[ตรวจ duplicate / session conflict / deadline]
 B --> C[อ่าน state ของ session จาก server]
 C --> D[ACK และบริบทที่ยืนยันว่าผู้ใช้ได้รับ]
 D --> E[แก้คำผิดแบบมีคำหลักรองรับ รักษาเลข วันที่ เครื่อง และคำปฏิเสธ]
 E --> F{ข้อความต่อหรือกลับหัวข้อชัดเจน?}
 F -->|ใช่| G[ผูกกับ task ที่ตรงในประวัติ session เดียว]
 F -->|ไม่| H[จำแนกหัวข้อและสิ่งที่ขอ]
 G --> I{หลายหัวข้อ / ไม่มีบริบท / เงื่อนไขไม่ครบ?}
 I -->|ใช่| J[ถามให้เลือกหรือเติมข้อมูล]
 I -->|ไม่| H
 H --> K{สมาชิกทีมแข่งขัน หรือสมาชิกศูนย์?}
 K -->|ทีมเกมที่ระบุ| L[game target + facet + rule source coverage]
 K -->|สมาชิกศูนย์| M[คำตอบบริการจากข้อมูลที่ยืนยัน]
 K -->|หัวข้ออื่น| N[handler ตามหัวข้อ]
 L --> O{มี clause รองรับประเด็นนี้?}
 O -->|มี| P[ตอบสาระพร้อมแหล่งข้อมูลและเงื่อนไข]
 O -->|ไม่มี| Q[ระบุช่องว่างข้อมูลเฉพาะเรื่อง ห้ามยืมเกมอื่น]
 M --> P
 N --> P
 P --> R[ตรวจเนื้อหาที่จำเป็น ภาษา และ task outcome]
 Q --> R
 J --> R
 R --> S[complete state + SQLite transaction]
 S --> T[ส่ง output แล้วรอ ACK สำหรับการใช้งานบริบทถัดไป]
```

การตอบหลายประเด็นต้องแยกสิ่งที่ตอบได้/ไม่ทราบออกจากกัน `validation_ok` และ `task_contract` ไม่ใช่หลักฐานว่าข้อเท็จจริงทุกข้อถูก ต้องมี oracle ตรวจเนื้อหาจริงด้วย

## 3. P0 Routing ของกติกา — ทำแล้ว

1. อ่าน input, trace, route, mode, source และ expected answer คู่กัน
2. เมื่อมีเกมแข่งขันที่ระบุ + team/member + จำนวน ให้ส่งเข้า competition_rules ก่อน guard สมาชิกบริการทั่วไป
3. ตรวจ facet ว่าคือ team_size, roster_composition หรือ pause_timeout จากเจตนาที่ขอ ไม่ใช้คำว่า team ตัดสินทั้งหมด
4. CS2: อ้าง clause s18_c01 ที่ระบุผู้เล่น 5 คน ตอบ 5 โดยไม่แต่งจำนวนสำรอง
5. VALORANT: source ที่นำเข้ายังไม่รองรับจำนวน starter/substitute/team_size; ตอบช่องว่าง ไม่ตีความ Match Prep ไม่เกิน 6 คนเป็น roster
6. Tactical timeout: จับสำนวน “ทีมขอเวลานอกได้กี่ครั้ง” ให้ตรง clause 2 ครั้งต่อแผนที่และครั้งละ 60 วินาที พร้อมขอบเขตที่ source ระบุ
7. แยก Steam/account membership และจำนวนกลุ่มสมาชิกออกจากคำถามสมัครสมาชิกศูนย์
8. ตรวจ source/localization ที่ใช้งานจริงและ negative cases ไทย/อังกฤษ

เกณฑ์: mode/game/facet ถูก + ตัวเลขและเงื่อนไขถูก + มี source; missing source ผ่านได้เมื่อระบุว่าไม่ทราบตรงประเด็น ไม่ถือว่าข้อมูลเรื่องนั้นครบ

## 4. P1 คำผิดและคำถามต่อ — ทำแล้วในขอบเขตที่ทดสอบ

1. Vocabulary canonical + distance ที่มี anchor บริการ รองรับ “เครือง” ร่วมกับการจอง/โอน
2. แก้หลายจุดเฉพาะที่สอดคล้องกันและมี edit budget; เก็บ query ก่อน/หลัง ไม่แก้ตัวเลข ID วันเวลา
3. ตัดคำสุภาพท้ายคำถามต่อเฉพาะขอบข้อความ เช่น อะครับ/อ่ะครับ/please เพื่อจับ motorbike/mouse followup
4. คำกลับเรื่องชัดเจนค้น history ไม่เกิน 16 messages/8 turns และใช้เฉพาะ server turn ที่ ACK
5. กลับเรื่องที่จอดรถหลังถามเกม: ใช้คำถามที่เคย resolve พร้อมเงื่อนไขเดิม
6. หากต้นเรื่อง compound หรือ pending price อย่าเลือก subtask เอง; ชี้แจงให้เลือก
7. ไม่พบประวัติเรื่องนั้น: ถามให้ระบุ ห้ามยืมประวัติคนอื่น
8. คำถามระบุสถานที่อื่นชัดเจน เช่น กรุงเทพ ต้องไม่ตอบว่าเป็นที่จอดรถของตึก 5 ภูเก็ต

ขอบเขต: return marker/สถานที่/คำผิดที่รองรับยังเป็นแบบ bounded ไม่ใช่ semantic correction ครบทุกประโยค การเพิ่มคำควรขยายชุดทดสอบจากความผิดจริงพร้อม negative cases ไม่เพิ่ม alias เพื่อกลบทุกคำผิด

## 5. P2 ความจำหลัง restart — ทำแล้ว

1. State DB ใหม่ `dialogue_state_v1.sqlite3` แยกจาก transcript; SQLite WAL + transactions ปิด connection ทุกครั้ง
2. เก็บ session snapshot เฉพาะ server-created state, ACK, completed turns, active task และ bounded history
3. Default TTL 1,800 วินาที ใช้ wall clock ข้าม restart; สูงสุด 512 sessions; ต้องเป็น session ID เดิมและยังไม่หมดอายุ
4. Turn ที่ pending ห้ามยกระดับเป็น complete; restore ต้องให้ประมวลผลใหม่
5. Duplicate completed turn replay ได้ตาม protocol; conflicting payload กับ turn ID เดิมต้อง conflict
6. ไม่ replay live booking answer จาก disk; ถามใหม่ต้องดึงสถานะใหม่
7. DB เสีย/เขียนไม่ได้ใช้ memory fallback และ health ระบุ last_error/survives_server_restart=false
8. Unit tests ตรวจ TTL/corrupt/unacknowledged/pending/live/idempotency/isolation; HTTP restart จริงตรวจ 10 sessions ตามลำดับ + fresh session 1
9. HTTP followups 4 sessions พร้อมกันตรวจสาระและ resolved question ของ public response

ความจำนี้ไม่รับรองการเริ่ม session ใหม่ การล้างข้อมูล browser การย้ายไปโฟลเดอร์ใหม่ หรือทุก domain หลัง restart ผล HTTP รอบนี้ครอบคลุม parking/personal peripherals

## 6. P3 Release และโฟลเดอร์ใช้/ส่งต่อ — ทำแล้วพร้อมขอบเขตตรวจ

1. Freeze รุ่น r50.2 ใหม่ สำรองก่อนแก้ เก็บ source diff และ hash; รุ่นเก่าคงอยู่
2. ตรวจ source/release 217 ไฟล์ และ full app/web/data ทั้งสองโฟลเดอร์ส่งต่อ
3. มี 01_Download_Models และ 02_With_Models รวม Python/Ollama/launcher/code/data
4. ไม่แนบ log, state DB หรือ session ของผู้จัดทำให้ผู้รับ
5. ตรวจ bundled Python sqlite3/ssl และโมเดลสองไฟล์ด้วย streamed SHA-256
6. รัน HTTP บน candidate รุ่นที่ freeze พร้อม health identity; โฟลเดอร์ส่งต่อยืนยัน equality กับ candidate
7. ตรวจ cold start ทั้งสองแบบบนเครื่องผู้รับใหม่: ยังไม่ได้ทำ จึงไม่ถือว่า file checks เป็นผล cold boot
8. ใช้ `Start-Chatbot.cmd` ของทั้งโฟลเดอร์; with models ไม่ต้องดาวน์โหลดน้ำหนัก, live WordPress ต้องเชื่อมอินเทอร์เน็ต

## 7. P4 ผู้ใช้พร้อมกัน — ทำแล้ว

### ออกแบบ

- แต่ละคนมี session/turn ID แยก ใช้ barrier เริ่ม HTTP พร้อมกัน; debug=false; ไม่ retry
- Fast: ที่จอดรถ/สมาชิก/สถานที่/คีย์บอร์ด/สลิป/walk-in; 3 waves ที่ 1,2,4,8,12,16,24,32 คน
- Mixed: CS2 controls, VALORANT personal mouse competition rule, PC games EN, personal keyboard EN; 2 waves ที่ 1,2,4,6,8,12 คน
- Runtime ใช้ worker เดียว, admission cap 16, queue wait 3s, global deadline 20s; คง setting จริง
- เก็บทุกคำขอ ทั้งคำตอบ เนื้อหาที่ต้องมี ภาษาจริง status เวลา session ID; แยก successful latency จาก rejected latency
- เกณฑ์ผ่าน: ทุก request ตรง oracle, ไม่มี timeout, PID ไม่เปลี่ยนในระดับนั้น, p95<=20s; หยุดเมื่อสองระดับต่อกันไม่ผ่าน
- ไม่ยิง load burst ใส่ WordPress และไม่ถือว่า selected mixed เป็น worst-case LLM ทุกหมวด

### ปรับ Flow จากผลจริง

1. Baseline พบ 503 ที่ fast16/mixed8 เก็บไว้ก่อนแก้
2. Final fast16 ผ่านครบ; mixed8 มี planned recycle ปนอยู่ — อ่าน event worker_recycle warming/promoted และ launcher threshold 250
3. ทดสอบ mixed ซ้ำแยกเมื่อ worker ยังมี completed count ต่ำ ไม่มี PID เปลี่ยนทุกระดับ
4. ใช้ mixed repeat เป็นหลักฐาน capacity ที่แยกปัจจัย recycle; เก็บ final ที่มี recycle เพื่อแสดง long-running behavior
5. การทดสอบ restart เริ่มยิง 10 พร้อมกันทำ harness หยุดที่503: แยก functional recovery เป็น sequential กับ load benchmark เก็บข้อมูลพลาดเดิมไว้
6. Public debug=false ไม่คืน debug-only context_resolution: ตรวจ resolved_question/content/session ใน oracle ห้ามแก้ระบบเพียงเพื่อให้ test ผ่าน

ข้อสรุป: Fast สูงสุดที่ทดสอบแล้วผ่านทั้งหมด 16 คน; Mixed สูงสุดที่ผ่านทั้งรอบหลักและรอบแยก recycle 6 คน ยังไม่ได้วัด 7 หรือ 17–23 จึงไม่อ้าง exact maximum แนะนำเผื่อแรง 12 fast หรือ 4–6 mixed สำหรับ workload นี้

## 8. Review / feedback loop

ใช้ 10 มิติตรวจทาน: evidence, source/locale, scope, completeness, context/ACK, persistence/TTL, restart/failure, load/recycle, package/preservation, acceptance/remaining work รายละเอียดอยู่ REVIEW_LOG_R50.md

รอบแก้จริง: source V1 → แก้ routing/facet/scope → V2 → พบ regression member group → แก้ → freeze r50.2 → HTTP/regression → restart → load → พบ recycle confound → mixed confirm → public context oracle regrade → final docs ไม่มีการอ้างว่ารันแก้โค้ด 10 รอบเต็ม

## 9. งานถัดไปตามสิ่งที่ยังพบ

1. หากต้องรองรับเกิน 6 mixed ให้แยก performance trace ต่อ stage และวัด sustained load/queue wait ตาม SLA ที่ต้องการ ก่อนปรับจำนวน workers; RAM เครื่องนี้มีแรงกดดันสูงอยู่แล้ว
2. Planned recycle ให้พิจารณา schedule/warmup/resource contention จาก event จริง; ยังไม่สรุปว่า recycle มีบั๊กจาก PID เปลี่ยนเพียงอย่างเดียว
3. ถ้ามีคำถามกติกา VALORANT roster จริง ต้องได้เอกสารจำนวนตัวจริง/สำรองของรายการนี้ ไม่ใช้กติกาทั่วไปแทน
4. เก็บ unseen input/return marker ที่ผิดจริง ขยาย bounded recovery และ scope negative fixtures
5. Cold startup/reinstall บนเครื่องผู้รับ + sustained requests + live booking load เป็นขั้นแยกที่ยังไม่ได้รับผลในรอบนี้

ทุกครั้งที่แก้ให้มี failing example → trace/source analysis → expected content → narrow fix → focused TH/EN regression → version+evidence ใหม่ ห้ามนับการเชื่อม API ได้เป็น factual correctness
'''
save('FLOW_FINAL_R50.md',flow)
review='''# บันทึกตรวจทาน 10 มิติ r50

วันที่ 2026-10-09; นี่คือ 10 มิติที่ตรวจพร้อม feedback iterations จริง ไม่ใช่การอ้าง 10 cycles แก้โค้ด/ทดสอบเต็มชุด

| รอบตรวจ | สิ่งที่ตรวจ / สิ่งที่พบ | การปรับและหลักฐาน | ขอบเขตที่เหลือ |
|---|---|---|---|
| 1 Evidence | ข้อมูลจริง/อังกฤษผู้ใช้ยืนยันแล้ว; ห้ามนับเป็น test ใหม่ | USER_CONFIRMATIONS แยก human/auto | ยืนยันเฉพาะขอบเขตที่ผู้ใช้แจ้ง |
| 2 Source/locale | CS2 source มี 5; VAL roster ไม่มี; timeout TH ไม่ติด facet | source V1 15/22 → V2 22/22 | VAL team_size ยัง missing |
| 3 Scope | สมาชิกทีมติด guard; member groups ติด membership answer; Bangkok ติด Phuket parking | game/team count delegation, member directory delegation, location guard; r42 17/18→18/18 | ไม่ใช่ universal place resolver |
| 4 Completeness | API200/validationok อาจตอบคนละเรื่อง; unknown fields ห้ามเดา | assertion ตัวเลข/หมวด/source/required text; unknown typed answers | Oracle lexical+route ไม่เท่ากับ human audit ทุกข้อความ |
| 5 Context/ACK | ต้องกลับเรื่องชัดและใช้ ACK server history; compound คลุมเครือ | bounded return marker + polite followup; HTTP focused; parallel4 content/resolved/session ผ่าน | หลายหัวข้ออาจถามเพิ่มตาม ambiguity |
| 6 Persistence/TTL | memory เดิมไม่อยู่หลัง reboot; pending/live ห้าม replay | SQLite WAL/snapshot/TTL; unit12 ผ่าน | session เดิม/TTL1800/pathเดิม |
| 7 Restart/failure | sandbox temp test ใช้ไม่ได้; concurrent10 restart harness หยุด503 | fixture dirใหม่เก็บไว้; real reboot sequential10+fresh1=11/11; failed evidence เก็บ | ไม่อ้าง10 simultaneous restorationผ่าน |
| 8 Load/recycle | fast16 latestผ่าน; mixed8final PIDเปลี่ยน; threshold250 | เก็บ worker event; mixedconfirm ไม่มี PIDเปลี่ยน แยกcapacity/recycle | sustained/public/livebooking/unseenLLMยังไม่ได้วัด |
| 9 Package/preserve | long path/share hardlink sandbox buildแรกไม่สำเร็จ; READMEเก่าอ้างr37 | short pathใหม่, hashes+full data equality, READMEรุ่นใหม่; audit9existing+2new,data unchanged | coldmachinebootยังไม่ได้ทำ; partialfolderห้ามส่ง |
| 10 Acceptance | ทดสอบครบเฉพาะเกี่ยวข้อง; debugfalse contextfieldไม่ได้คืน | public oracle regrade, final docsแสดงทั้งfail/pass/limits | 6mixedเป็นhighesttestedไม่ใช่universalmaximum |

## ข้อผิดพลาดของเครื่องมือวัดที่เก็บไว้

- HTTP_PARALLEL_CONTEXT_R50.json ประเมิน 0/4 เพราะ oracle เรียก context_resolution ซึ่งไม่มีใน debug=false; คำตอบทั้ง4ถูกและ session/หัวข้อ resolved ถูก
- HTTP_PARALLEL_CONTEXT_REGRADED_R50.json ตรวจ evidence เดิมด้วย public contract: 4/4 ไม่มี rerun หรือแก้ network response
- ข้อมูล first restart concurrent ใช้ retrospective committed state เท่านั้น เพราะ harness แรกไม่มี HTTP error log ครบ; ไม่แต่งจำนวน/เวลา failed requests
- Package build แรกในโฟลเดอร์ลึกไม่สำเร็จ เก็บ partial folder; buildสำเร็จอยู่ short pathที่รายงานเท่านั้น
'''
save('REVIEW_LOG_R50.md',review)
restart=read('HTTP_RESTART_RESULT_V2.json');audit=read('SOURCE_RELEASE_AUDIT_R50.json')
counts='\n'.join(f"- {a['label']}: {a['correct']}/{a['requests']} ถูกต้องทุกระดับรวม overload; errors {json.dumps(a['errors'],ensure_ascii=False)}" for a in aggregate)
fullchecks={name:json.loads((SHARE/name/'R50_FULL_RUNTIME_DATA_CHECKS.json').read_text())['equal_files'] for name in ['01_Download_Models','02_With_Models']}
report=f'''# รายงานผลพัฒนาและทดสอบ r50

2026-10-09 เวลาไทย · version 2026.10.09-flow-r50.2 · เว็บ candidate http://127.0.0.1:8091/

## สรุปงานที่ทำ

- วาง Flow, ตรวจ 10 มิติ, แก้ routing/facet/typo/followup และเพิ่มความจำ SQLite ข้าม restart
- ตรวจ source trace เริ่ม 15/22 ผ่าน หลังแก้ 22/22; HTTP ชุดใหม่ 22/22 (11TH/11EN), regression r49 110/110 และ r48 136/136 รวม 268/268 scenario ไม่ใช่ 268 request เพราะบาง scenario หลาย turn
- Unit ล่าสุด persistence12, dialogue10, taxonomy2, sourcefacet10, domainresume18: 52/52 tests; r42 เคยผิด1เรื่อง member groups แล้วแก้
- รีสตาร์ต server จริง 10 session ตามลำดับ + fresh-session isolation1: {restart['passed']}/{restart['total']}; HTTP followups พร้อมกัน4: 4/4 หลังแก้ oracle ให้ตรง public contract
- Data/nโยบายเจ้าของไม่เปลี่ยน; source audit: 9 existing files เปลี่ยน +2ใหม่, อีก {audit['all_other_before_files_unchanged']} ไฟล์ใน snapshot ไม่เปลี่ยน; source/release 217/217 ตรงกัน
- โฟลเดอร์ส่งต่อสองแบบมี full app/web/data ตรง release: {fullchecks}; bundledPythonผ่าน; withmodelsน้ำหนัก2ไฟล์ SHA256ผ่าน ไม่มี state/logsส่วนตัว

## แยกประเภทหลักฐาน

| เรื่อง | ผู้ใช้ยืนยัน | อัตโนมัติรอบนี้ | ยังไม่รับรอง |
|---|---|---|---|
| สถานะจองจริง | ผู้ใช้เช็คแล้วถูกต้อง | ไม่ยิง burst WordPress | throughput/status ทุกสภาวะเครือข่ายภายใต้โหลด |
| อังกฤษ | ผู้ใช้แจ้งผ่าน | focused/regression TH/EN ในส่วนแก้ | ไม่แก้ approval metadata ของทุกเอกสารย้อนหลัง |
| Dialogue correctness | ยังไม่มี human approve ทุก input | required content + mode/target/session/locale/timeout | ทุกสำนวนที่ไม่เคยทดสอบ |
| Restart | — | unit12, actual HTTP11, separate parallel4 | ทุก domain/cross browser/cross folder |
| Package | — | source/data equality, Python, model hash | fresh recipient machine cold startup ทั้ง2แบบ |

## ทำไมเคยตอบผิด

1. สมาชิกทีม CS2/VALORANT: route เดิมเริ่ม competition ถูก แต่ service_fact_scope_guard ที่ทำงานถัดมาจับคำสมาชิกและคืน clarification ก่อนอ่าน rule clause; จึงมีข้อมูลก็ไม่ได้ใช้ แก้ guard delegation เมื่อ game+team count ชัด
2. Team size VS timeout: สำนวนไทยเวลานอกไม่อยู่ taxonomy matching ขณะที่อังกฤษได้; เพิ่ม facet cue ของ tactical timeout ไม่ใช้ team keyword เป็น team_size เสมอ
3. Source gap VALORANT: ความไม่ครบของ source ที่นำเข้า ยังไม่มีจำนวนตัวจริง/สำรอง; แก้ให้ระบุ missing ชัด ไม่เอาตัวเลขผู้เข้า Match Prep มาเป็น roster
4. Member groups: guard เพิ่มแล้วพบ regression `How many member groups are there?` ถูกตอบไม่ต้องสมัครสมาชิก; เพิ่ม delegation ให้ directory count ไม่ใช่ membership admission
5. สำนวนผิดสองจุด/คำสุภาพ: ตัวจับ lexical noun/followup ไม่ครอบคลุมคำที่มี anchor ชัด; ขยาย canonical recovery และ suffix handling แบบ bounded ไม่เปลี่ยนเลขหรือวันเวลา
6. Return marker: ก่อนนี้ task memory ไม่รู้ว่าขอกลับ service topic เก่าชัดเจน; เพิ่ม lookup เฉพาะ acknowledged server turn ไม่ย้อนเรื่องเอง
7. Location: parking answer ถูกใช้กับ Bangkok; เพิ่ม guard เฉพาะการระบุสถานที่อื่นที่รู้จัก ผลผ่านมิได้หมายถึงแก้ place entity ทุกเมืองแล้ว
8. Restart: state อยู่ memory จึงหายเมื่อ parent processเปลี่ยน; SQLite snapshotแก้ persistence แต่ยังต้อง session/TTL/pathเดียว

ตัวอย่างคำถาม/คำตอบก่อนและหลังทั้งหมด: {link('FAILURE_DETAILS_R50.md')}

## วิธีวัดโหลด

ส่ง POST /api/chat บนเครื่องนี้ผ่าน loopback; barrierเริ่มพร้อมกัน; session/turnแยก; debugfalse; ไม่ retry; เก็บ first attempt เท่านั้น Fast3 waves/ระดับ Mixed2 waves/ระดับ เริ่ม1คนแล้วเพิ่ม RuntimeเปิดlocalLLM+semanticRAGจริง แต่หลายคำถามตอบstructuredตรงได้

- Fast = service facts 6รูปแบบ ไทย/อังกฤษ
- Mixed = CS2ยิง, VALORANTเมาส์แข่ง, PC gamesEN, personalkeyboardEN ไม่ใช่ worst-case LLMทั้งหมด
- worker1, activecap16, queuewait3s, answerdeadline20s, recycle250completed requests ตาม launcherจริง
- p50คือมัธยฐานเวลาแต่ละ request; p95 nearest-rank; จำนวนตัวอย่างน้อย บางระดับ p95จึงเท่าค่าสูงสุด ตารางlatencyเฉพาะคำตอบที่ถูกต้อง ไม่รวม503ที่ตอบเร็วกว่าจนทำให้เวลาดูดี
- RAMก่อนรอบfinal83% เหลือประมาณ2.69GB; หลังประมาณ85% เหลือ2.40GB; ขนาด/โหลดงานอื่นบนเครื่องมีผล

### Baseline r49.2

{table(loads[0])}

หลักฐาน: {link(baseline.name)}

### Final r50.2 — ทั้ง fast และ mixed ต่อเนื่อง

{table(loads[1])}

หลักฐาน: {link(final.name)}

mixed8มี PIDเปลี่ยน25756→35632; performance eventระบุ planned worker_recycle warming/promoted และ launcher threshold250 จึงไม่สรุปว่าเป็น crashหรือข้อจำกัดจำนวนคนอย่างเดียว mixed12ต่อจากworkerใหม่ยังมี503และtail16.51s แต่ต้องรายงานสภาพหลัง recycleด้วย

### ยืนยัน Mixed แยกจากรอบเปลี่ยน worker

{table(loads[2])}

หลักฐาน: {link(confirm.name)}

ทุกระดับนี้ PIDคงเดิม ไม่มี timeout/content mismatch; 503เป็น worker_queue_busy ไม่มีการretry ที่8คนได้15/16 ที่12ได้19/24 จึงยืนยันว่าคิวจำกัดก่อ rejectionได้แม้ไม่มี recycle จำนวน8ไม่ใช่ผ่านครบ

### สรุปจำนวนและเวลา

- Fast: สูงสุดที่ทดสอบผ่านทั้งหมด16คน (48/48), p50ประมาณ2.50s/p95 3.77s; baseline16เคย47/48จึงควรเผื่อที่12คน
- Mixed: สูงสุดที่ผ่านครบทั้งรอบหลักและรอบแยก6คน, p50ประมาณ2s และp95ประมาณ3.2–3.7s; 1–4คนรอบยืนยัน p95ประมาณ0.8–2.0s
- ยังไม่ได้ทดสอบ7คนหรือ17–23คน จึงเป็น highest tested passing level ไม่ใช่ exact maximum
- “คนพร้อมกัน” หมายถึงส่งคำถามในจังหวะเดียวกัน จำนวนคนเปิดแท็บค้างอาจมากกว่าได้ ผลนี้ไม่ใช่จำนวนผู้ใช้บริการตลอดวัน
- ถ้าต้องให้เลขเริ่มต้นสำหรับ workloadผสมนี้ ใช้4–6คำขอพร้อมกันและติดตาม503/queue; เพิ่มโหลดต้องวัด sustained/LLM-heavy/livebookingแยก
- ภาระเกินคิวเกิด503แบบให้ลองใหม่ ข้อมูลที่ตอบสำเร็จไม่พบเนื้อหาผิดตามoracle แต่ไม่ได้แปลว่าคำขอที่ถูกปฏิเสธให้บริการสำเร็จ

### ยอดคำขอและข้อผิดพลาดดิบ

{counts}

รวมรายละเอียดรายระดับ/ข้อผิดพลาด: {link('LOAD_ANALYSIS_R50.json')} ไม่มีการเอาเฉพาะคำขอสำเร็จมาคิด accuracyรวม

## การทดสอบที่พลาดและเหตุผลที่ไม่ลบทิ้ง

- Source V1ผิด7/22; r42ผิด1/18 เก็บbefore/after traceและผลเก่า
- Persistence testแรกใช้ sandbox Temp ที่SQLiteเข้าถึง/cleanupไม่ได้ เปลี่ยนfixtureไปartifactdirและเก็บfixture ไม่ลบไฟล์เดิม; unitล่าสุด12ผ่าน
- Restartครั้งแรกยิง10followupsพร้อมกัน harnessหยุดที่503 ไม่ได้เก็บHTTPครบ; retrospectiveอ่าน committed/pendingของ10sessionจากDBเก็บแยก ไม่อ้างว่าผ่าน10พร้อมกัน
- Restartครั้งถัดไปใช้seedใหม่/realPIDchangeและrecoveryตามลำดับ11/11เพื่อแยกfunctionalจากload
- Parallel context oracleแรก0/4เพราะrequiredebug-onlyfieldขณะdebugfalse; คำตอบ/networkเดิมทั้ง4ถูก ตรวจresolved_question+content+session แล้ว4/4 เก็บทั้งสองรายงาน
- Sharebuildแรกlongpath/hardlink permissionไม่สำเร็จ เก็บpartialfolderในartifactแต่ไม่ใช้ส่งต่อ; shortpathใหม่สร้างและตรวจครบ

## ส่งต่อและเปิดใช้งาน

โฟลเดอร์ใหม่: [{SHARE.name}](<{SHARE}>)

- [มีโมเดล เปิด Start-Chatbot.cmd](<{SHARE/'02_With_Models/Start-Chatbot.cmd'}>)
- [แบบดาวน์โหลดโมเดล เปิด Start-Chatbot.cmd](<{SHARE/'01_Download_Models/Start-Chatbot.cmd'}>)
- ต้องย้ายทั้งโฟลเดอร์ variant ไม่ย้ายเฉพาะcmd; อ่านREADMEรุ่นr50ที่ใส่ใหม่
- บนเครื่องนี้ immutablebinary/modelใช้hardlinkเพื่อประหยัดพื้นที่จริง แต่เมื่อคัดลอกไปเครื่องอื่น/ZIPเป็นfullbytesตามขนาดlogical ไม่ได้ลดไฟล์โมเดล
- ไม่ทับชุดเก่า ไม่มีZIPใหม่ในรอบนี้; package checksไม่เท่ากับcoldlaunchทั้งสองแบบบนเครื่องใหม่
- private conversation DB/logs ของการทดสอบอยู่เฉพาะartifactcandidate ไม่รวมในโฟลเดอร์ส่งต่อ

## สิ่งที่ยังต้องทำ/ถามอย่างเจาะจง

1. หากต้องการตอบ VALORANT roster: “รายการ PSU Phuket VALORANT 2026 ให้มีตัวจริงกี่คน สำรองกี่คน และโค้ชรวมอยู่ในจำนวนใด? ขอ clause/เอกสารของรายการนี้” ไม่จำเป็นต้องให้เจ้าของตอบ CS2 5คนซ้ำเพราะsourceมีแล้ว
2. Service fieldsที่ยังไม่ยืนยัน: ค่าจอดรถฟรีหรือคิดเท่าไร, อนุญาตจอยส่วนตัวหรือไม่, และรายการunknownเดิม ต้องตอบว่าไม่ทราบต่อไป
3. งานทำเองได้ต่อ: sustained load/LLM-heavy, stage latencyprofiling, recyclewarmup contention, coldrecipient test, unseen typo/return markers negativecases; จัดลำดับตามfailureจริง
4. ไม่ควรเพิ่มworkerโดยเดา: เครื่องมีRAMแรงกดดันและmodelเดียว ต้องวัดผลจริงหลังการปรับทีละค่า

Flowฉบับสุดท้าย: {link('FLOW_FINAL_R50.md')} · Review10มิติ: {link('REVIEW_LOG_R50.md')} · Audit: {link('SOURCE_RELEASE_AUDIT_R50.json')}
'''
save('REPORT_FINAL_R50.md',report.replace('Data/nโยบาย','Data/นโยบาย'))
for name in ['01_Download_Models','02_With_Models']:
 folder=SHARE/name;old=(folder/'README_TH.md').read_text(encoding='utf-8-sig')
 with (folder/'README_HISTORICAL_PRE_R50.md').open('x',encoding='utf-8') as f:f.write(old)
 bundled=name=='02_With_Models';checks=fullchecks[name]
 latest=f'''# PSU Esports Chatbot r50 — {'มีโมเดลครบ' if bundled else 'ดาวน์โหลดโมเดลก่อนใช้'}

รุ่น 2026.10.09-flow-r50.2 · 2026-10-09

## เริ่มใช้

1. คัดลอกทั้งโฟลเดอร์นี้ไปไว้ในที่เขียนไฟล์ได้บน Windows x64 ห้ามเปิดจากในZIP
2. ดับเบิลคลิก **Start-Chatbot.cmd** รอเตรียมระบบและเว็บเปิดเอง
3. {'น้ำหนักโมเดลอยู่ในชุดนี้ครบ ไม่ต้องดาวน์โหลดโมเดล' if bundled else 'การเปิดครั้งแรกต้องเชื่อมอินเทอร์เน็ตเพื่อดาวน์โหลดโมเดลตามรุ่นที่กำหนด'}; PythonและOllamaรวมในชุดแล้ว
4. พิมพ์ไทย/อังกฤษได้ ข้อมูลจองสดต้องใช้อินเทอร์เน็ตและWordPressพร้อม
5. Stop-Chatbot.cmdใช้หยุด, View-Chat-Logs.cmdใช้ดูประวัติของชุดนี้ ปิดแท็บอย่างเดียวไม่หยุดserver

เว็บนี้ตอบข้อมูล/สถานะ ไม่ส่งการจองหรือชำระเงินแทนผู้ใช้ ระบบเลือกพอร์ตว่าง8090–8099 เครื่องต้องเปิดระหว่างใช้งาน

## ผลตรวจล่าสุดและขอบเขต

- โค้ด/dataตรงcandidateที่ทดสอบ HTTP {checks}ไฟล์; bundledPython/sqlite3/sslผ่าน {'; โมเดล2ไฟล์ SHA256ผ่าน' if bundled else '; ชุดนี้ไม่มีน้ำหนักโมเดลเต็ม'}
- candidateHTTP focused22/22, regression110/110และ136/136, unitหลัก52/52
- restart10sessionตามลำดับ+freshsession1ผ่าน11/11; followups4sessionพร้อมกันผ่าน4/4ตามเนื้อหา/session/resolvedquestion
- บนเครื่องผู้จัดทำ Fast16คำขอพร้อมกันผ่านครบp95~3.77s; Mixed6ผ่านครบp95~3.2–3.7s; เกินระดับนั้นพบ503 ไม่รับรองจำนวนเดียวกันบนเครื่องอื่น
- ยังไม่ได้coldbootทั้งสองvariantsบนเครื่องใหม่ ห้ามตีความfilechecksเป็นการทดสอบนั้น
- stateอยู่data/logs/dialogue_state_v1.sqlite3เมื่อเริ่มใช้; TTL30นาทีและsessionIDเดิม; ไม่ใช่ความจำทุกบทสนทนาถาวร
- ไม่แนบlog/stateส่วนตัวของผู้จัดทำ ข้อมูล/นโยบายเจ้าของไม่ได้เปลี่ยนในr50
- VALORANTจำนวนตัวจริง/สำรองยังไม่มีsourceรองรับในชุดข้อมูลที่นำเข้า; ค่าจอดรถ/จอยส่วนตัวยังไม่ยืนยัน

## เครื่องและไฟล์

ใช้ Windows10/11 x64; แนะนำRAM16GBขึ้นไป ผลความเร็วขึ้นอยู่กับCPU/GPU/driver/งานอื่นบนเครื่อง ไม่ได้benchmarkทุกเครื่อง
ต้องมีพื้นที่ทั้งโฟลเดอร์และเพิ่มสำหรับlog/โมเดล เก็บทั้งruntimeและsystemไว้ด้วยกัน
Logอยู่system/PSU_Esports_Chatbot_Local/data/logs/ ตรวจlauncherlogหากเปิดไม่ได้

TEST_RESULTS_R50_TH.mdคือผลรุ่นล่าสุด; README_HISTORICAL_PRE_R50.mdและTEST_RESULTS_TH.mdเป็นหลักฐานเก่าที่เก็บไว้ ไม่ใช่สถานะรุ่นล่าสุด
'''
 (folder/'README_TH.md').write_text(latest,encoding='utf-8')
 with (folder/'TEST_RESULTS_R50_TH.md').open('x',encoding='utf-8') as f:f.write(latest.split('## ผลตรวจล่าสุดและขอบเขต')[1])
 shutil.copyfile(OUT/'FLOW_FINAL_R50.md',folder/'FLOW_FINAL_R50.md')
with (SHARE/'README_TH.md').open('x',encoding='utf-8') as f:f.write('''# PSU Esports Chatbot — โฟลเดอร์ส่งต่อ r50

2026.10.09-flow-r50.2

- 02_With_Models: มีโมเดล เปิด Start-Chatbot.cmd ได้หลังคัดลอกทั้งโฟลเดอร์
- 01_Download_Models: รวมตัวรัน/ข้อมูล แต่ครั้งแรกต้องดาวน์โหลดโมเดล
- อ่าน README_TH.md ของ variant ที่เลือก ผลล่าสุดอยู่ TEST_RESULTS_R50_TH.md
- แต่ละชุดเป็นเว็บlocal ผู้รับแต่ละเครื่องต้องรันserverของตัวเอง ไม่ใช่บริการpublicออนไลน์ที่โฮสต์ให้แล้ว
- สถานะจองสดต้องเชื่อมWordPress; ไม่จำเป็นต้องโหลดโมเดลเพิ่มในชุด With Models
- ชุดเก่าเก็บไว้ โฟลเดอร์นี้ไม่แนบประวัติ/stateของผู้จัดทำ ยังไม่ได้coldstartบนเครื่องผู้รับใหม่
''')
print('Documents and portable README saved; parallel public oracle regraded 4/4',flush=True)
