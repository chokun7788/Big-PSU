import json,re,sys,hashlib,urllib.request,platform
from pathlib import Path
import r42_probe
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
RELEASE=Path((OUT/'release_r42_4_path.txt').read_text(encoding='utf-8'))
def latest(pattern):return max(OUT.glob(pattern),key=lambda p:p.stat().st_mtime)
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,data):
    with (OUT/name).open('x',encoding='utf-8') as f:
        if isinstance(data,str):f.write(data)
        else:json.dump(data,f,ensure_ascii=False,indent=2)
def link(p,label=None):return f'[{label or p.name}]({p.as_posix()})'
groups=[]
for label,pattern in [('กลับหัวข้อหลัก','final_r42_4_main*_summary.json'),('สำนวน/หลายข้อ/ขอบเขต','final_r42_4_variations*_summary.json'),('บริบท r41','final_r42_4_r41_main*_summary.json'),('ขอบบริบท r41','final_r42_4_r41_variations*_summary.json'),('สองรอบราคา/กฎ/ปุ่ม','adjacent_http_*_summary.json'),('แยกเงื่อนไขจอง','final_r42_4_policy*_summary.json'),('คำขอซ้ำ/ชนกัน','final_r42_4_identity*_summary.json')]:
    p=latest(pattern);s=read(p);assert s['passed']==s['executed_cases'],p
    if s.get('health'):assert s['health']['runtime']['version']=='2026.10.06-domain-resume-r42.4',p
    groups.append((label,p,s))
assert groups[4][1].stat().st_mtime>=groups[0][1].stat().st_mtime,'Adjacent results must follow this final run'
unit_file=latest('source_regression_*.json');units=read(unit_file);assert len(units)==8 and all(u['returncode']==0 for u in units)
unit_methods=sum(int(re.search(r'Ran (\d+) tests?',(OUT/u['evidence']).read_text(encoding='utf-8')).group(1)) for u in units)
audit=read(OUT/'SOURCE_AUDIT_R42_4.json');assert all(audit['protected_unchanged'].values()) and all(p['equal'] for p in audit['app_web_parity'])
with urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=8) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.06-domain-resume-r42.4'
save('FINAL_HEALTH_R42_4.json',health)
baseline=[]
for pattern in ('baseline_source_*summary.json','baseline_http_*summary.json'):
    p=latest(pattern);old=read(p);rows=[r42_probe.grade(c,r['records']) for c,r in zip(r42_probe.cases(),old['results'])]
    baseline.append(dict(evidence=p.name,original_passed=old['passed'],regraded_passed=sum(r['passed'] for r in rows),total=len(rows),results=rows))
save('BASELINE_REGRADED_R42.json',baseline)
cases=sum(s['executed_cases'] for _,_,s in groups);requests=sum(s['requests'] for _,_,s in groups)
all_records=[r for _,_,s in groups for c in s['results'] for r in c['records']]
latencies=sorted(r['elapsed_sec'] for r in all_records if r['status']==200)
quantile=lambda p:latencies[min(len(latencies)-1,int((len(latencies)-1)*p))]
knowledge=[]
for folder in ('data/curated','data/rules'):
    for p in (ROOT/folder).iterdir():
        if p.is_file() and p.suffix in ('.json','.jsonl'):
            rel=p.relative_to(ROOT);other=RELEASE/rel
            knowledge.append(dict(file=rel.as_posix(),equal=other.is_file() and hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(other.read_bytes()).digest()))
save('KNOWLEDGE_PARITY_R42_4.json',knowledge)
gates=dict(version=health['runtime']['version'],http_cases=cases,http_requests=requests,http_passed=cases,source_unit_methods=unit_methods,source_unit_passed=unit_methods,
    groups=[dict(name=label,evidence=p.name,cases=s['executed_cases'],requests=s['requests'],passed=s['passed']) for label,p,s in groups],unit_evidence=unit_file.name,
    source_audit='SOURCE_AUDIT_R42_4.json',health='FINAL_HEALTH_R42_4.json',knowledge_equal=sum(r['equal'] for r in knowledge),knowledge_checked=len(knowledge),
    latency_successful_requests=dict(p50=quantile(.5),p95=quantile(.95),max=max(latencies)),owner_approval=False,live_booking_real_oracle=False,clean_machine=False,full_corpus_run=False,unseen_holdout=False)
save('FINAL_AUTOMATED_GATES_R42.json',gates)
backlog=read(BASE/'r41_task_memory_20261006_142223_26da94/BACKLOG_STATUS_R41.json')
notes={
 'B001':'เปิด r42.4 ที่ 8090; 8092/8093 เดิมยังอยู่ ต้องเลือก URL ที่ระบุรุ่นถูก',
 'B002':'มี candidate local ใหม่; WithModels/DownloadModels ยังไม่ rebuild',
 'B007':'เพิ่มหมวด schedule/reservation/members/contact/game details และ typed replay; ไม่ใช่ schema ทุกเรื่องครบ',
 'B008':'ตรวจ 1–4 รอบ/TTL/cross-session; บทสนทนายาวและทุกสำนวนยังไม่ครบ',
 'B011':'TH/EN resume หมวดเพิ่ม รวมหลาย child และ missing child ผ่านชุดที่เลือก',
 'B014':'ป้องกัน fuzzy ทับคำไทยที่ถูก; typo-all-domains ยังต้อง holdout',
 'B019':'เพิ่มสำนวน return/นับกลุ่มสมาชิก/เงื่อนไขการจองอังกฤษ; ไม่ใช่ทุกภาษาอังกฤษครบ',
 'B033':'fixture free→busy fetch ใหม่ผ่าน; ยังไม่ใช่สถานะจริงที่คนตรวจ',
 'B037':'แยก ISO date จาก hour range ผ่านไทย/อังกฤษ; network/day-rollover อื่นยังไม่ครบ',
 'B041':'เพิ่ม oracle กลุ่มสมาชิก/ขั้นต่ำ-สูงสุด/ยกเลิก/จำนวนเครื่อง; คำตอบเหมือนเดิมเมื่อ resume ไม่รับรองเนื้อหาทุกข้อครบ',
 'B042':'variations ใช้พัฒนาแล้ว จึงไม่เรียก unseen holdout',
 'B043':'store complete immutable + concurrent callbacks และ HTTP replay/conflict; crash/late delivery ทุกจังหวะยังไม่ครบ',
 'B044':'concurrent same-turn เป็น invariant check; ไม่ใช่หลายผู้ใช้ load benchmark',
 'B045':'Git status/diff-check รอบสุดท้าย exit 0; การเรียกครั้งแรก safe.directory ผิดราก เก็บ failure ไว้',
 'B050':'backup/diff/immutable releases/parity ผ่าน; automated update/rollback workflow ยังไม่ครบ',
 'B055':'same-operation compound archive/replay เก็บทุก child และแยก missing; ครบทุก combination ยังไม่ยืนยัน',
 'B057':'explicit ISO date+clock ไม่ปน; resume availability execute ใหม่; relative/pronounsทุกแบบยังไม่ครบ',
 'B060':'3 member groups แยกจาก 25 people และ Sessions แยกจากจำนวนเครื่อง; unit conversion/countsทุกหมวดยังไม่ครบ',
 'B062':'generic replay ใช้ domain จริง ไม่ติดป้ายราคา; logs/trace หลาย schema ยังต้องปรับต่อ',
 'B066':'เริ่มระบบเคย MemoryError/500 และ interpreter ต่างกันตาม PATH; pinned launch ล่าสุดตรวจผ่าน ไม่ปิด root cause หรือ fresh-machine gate'}
for row in backlog:
    row['r42_status']='partially_implemented_or_targeted_verified' if row['id'] in notes else 'not_reassessed_in_this_round'
    row['r42_note']=notes.get(row['id'],'คงสถานะและหลักฐานเดิม; ไม่มีหลักฐานใหม่ว่าปิดงานนี้ครบใน r42')
save('BACKLOG_STATUS_R42.json',backlog)
priorities='''
| ลำดับ | ยังต้องทำ | ทำเองได้ / ต้องมีข้อมูล | ขั้นถัดไป |
|---|---|---|---|
| P0-1 | การเริ่มระบบเคย MemoryError/HTTP500 และเลือก Python ตาม PATH | ตรวจและแก้เองได้ | เก็บ executable/version/resource/worker-stage ทุก launch; pin interpreter, ทดสอบ recovery; ยังไม่สรุป root cause จาก restart ผ่าน |
| P0-2 | source facts บางเรื่องขาดหรือขัดกัน | ต้องต้นฉบับ/เจ้าของ | ราคาปัจจุบัน, Tekken pause, RoV ข้อขาด, เพดานวัน/จำนวนเครื่อง; คง missing/conflict guard |
| P1-1 | content completeness ยังไม่เป็น oracle ทุกหมวด | ทำเองจาก source ที่มีได้ | แยก required facts/units/conditions แล้วตรวจ output จริง ไม่ใช้ mode/confidence หรือความเหมือนของ answer แทนความถูกต้อง |
| P1-2 | สำนวน/typo และบทสนทนายาวที่ไม่เคยใช้พัฒนา | ทำเองได้ | ชุดสำรองแยกจาก training/debug; แยก typo/short choice/topic shift/negation/time filters; ไม่เปิด full20k ในงานนี้ |
| P1-3 | วันเวลาใหม่เมื่อ return ยังต้องถามบางกรณี | ทำเองได้ | รวม filter แบบ typed ที่ไม่ทิ้งวันเวลา; bare all หลายมิติยังต้องถามเจาะจง |
| P1-4 | version/package data/translation drift | ทำเองได้ | ตรวจ manifests และ source hashes ทุก publish; ไม่ใช้พอร์ตเก่าแทน candidate |
| P2-1 | ชุดแจกสองแบบและเครื่องใหม่ | ทำเองด้าน build ได้ | rebuild WithModels/DownloadModels, pin Python/dependencies, ตรวจ extraction/launch/model absent; ยังไม่ยืนยัน clean machine |
| P2-2 | load/recovery/log lifecycle | ทำเองแบบควบคุมได้ | multiuser queues, worker recycle/crash, disk full/log retention; invariant test ไม่เป็น load SLA |
'''
remaining='# รายการงานที่เหลือ r42.4\n\nวันที่ 6 ตุลาคม 2026 — Asia/Bangkok\n\nรายการ 66 ข้อเดิมรวมบั๊ก ข้อมูลขาด และฟังก์ชันเสริม ไม่ใช่ 66 บั๊กที่ยังเกิดอยู่ทั้งหมด รายงานนี้แยกสิ่งที่ตรวจเพิ่มในรอบนี้จากสิ่งที่ไม่ได้ประเมินซ้ำ\n\n## ลำดับถัดไป\n'+priorities+'\n## คำถามเจาะจงสำหรับเจ้าของ\n\n'
remaining+='1. เปิดให้จองล่วงหน้าได้สูงสุดกี่วัน นับจากเวลาไทยปัจจุบันหรือวันที่เปิดรอบ และต่างกันตามบริการ/กลุ่มผู้ใช้หรือไม่?\n2. หนึ่งรายการจองเลือกเครื่องได้สูงสุดกี่เครื่องพร้อมกัน? เพดาน 3 Sessions เป็นคนละหน่วย จึงใช้แทนจำนวนเครื่องไม่ได้\n3. อัตราราคาที่ใช้หลัง 31 มีนาคม 2026 คือฉบับใด มีวันเริ่มใช้และข้อยกเว้นอะไรบ้าง?\n4. Tekken ใช้ข้อ pause/บทลงโทษฉบับใดเมื่อข้อความต้นฉบับขัดกัน และ RoV 6.1.5–6.1.5.1 มีประโยคท้ายฉบับเต็มอย่างไร?\n5. เมื่อพร้อมเก็บสถานะจองจริง ต้องมี snapshot ผูกวัน/เวลา/เครื่องและผลที่ผู้ดูแลตรวจไว้สำหรับเทียบ ไม่ใช้ API200 เป็นเฉลย\n\n'
remaining+='## สถานะครบ 66 รายการเดิม\n\nรายละเอียดต้นฉบับ: '+link(BASE/'PSU_ESPORTS_REMAINING_WORK_R39_3_20261006.md')+'\n\n'
for row in backlog:
    remaining+=f"### {row['id']} — {row['title']}\n\n- สถานะก่อนรอบนี้: {row.get('r41_status',row['execution_status'])}\n- ลักษณะงาน: {row['disposition']}\n- r42: {row['r42_note']}\n\n"
remaining+='## ประเด็นใหม่ที่ยังไม่ปิดครบ\n\n- R42-N1: maximum lead days และ maximum devices ไม่มี source ยืนยัน แม้ minimum booking notice/cancellation เป็น 1 ชั่วโมงและ max Sessions เป็น 3 ตามไฟล์\n- R42-N2: startup ready ไม่รับรอง API request สำเร็จ พบ warmup ผ่านแล้ว HTTP500 ในรอบเริ่มเดิม ต้องตรวจเชื่อม health กับ actual request และ memory recovery ต่อ\n- R42-N3: current generic English opening-hours answer ยังขอวันสำหรับ play window; resume equivalence ผ่านไม่ได้พิสูจน์ว่าได้ตารางทั้งหมดตามที่ผู้ใช้ต้องการ ต้องเพิ่ม content oracle ของ schedule\n'
save('REMAINING_ISSUES_R42_TH.md',remaining)
flow='''# Flow แก้บริบทและเงื่อนไขคำตอบ r42 — ฉบับตรวจทาน

## ขอบเขตและสิ่งที่ต้องรักษา

- อ่าน source และคำตอบ/trace จริง สำรอง uncommitted files ก่อน patch ไม่ reset/stash/แก้ log เก่า
- กติกา ราคา และตารางเจ้าของเปลี่ยนได้เมื่อมีหลักฐานเท่านั้น Missing fact ต้องตอบ missing; API connected ไม่เป็น real booking oracle
- เก็บ requested query เพื่อ execute ใหม่ ห้าม archive answer แล้วนำสถานะสดเก่ามาตอบ
- ไม่รัน full corpus20k; เคสพัฒนาและ regression เป็นหลักฐานตามขอบเขต ไม่เรียก unseen holdout

## 1. แยกคำถามเป็นงานที่ชัดเจน

1. รักษา raw input แล้วแยก locale, domain, operation, target, user group, date/time, quantity/unit และ negation
2. คำถามอังกฤษที่มี interrogative ทั้งสอง clause แยกงานแม้ operation เหมือนกัน; bare noun lists/ชื่อเกมยังเป็นหนึ่งคำถาม
3. เก็บ child question แต่ละข้อใน array ห้ามใช้ comma เป็นตัวแบ่ง target labels
4. จำกัด replay 1–4 child requests และ query ≤2000 chars; เกินขอบเขตถามแบ่งงาน ไม่ตัดท้าย

## 2. การแก้คำผิดและคำสั่งกลับหัวข้อ

1. Keyword fuzzy correction ต้องไม่ทับช่วงคำที่สะกดถูกแล้ว เช่น เปิดปิด
2. Return parser ใช้ NFC/casefold/Thai digits โดยไม่ใช้ fuzzy rewrite ทั้งประโยคซ้ำ
3. รองรับ please ก่อน/หลัง return และสำนวนกลับหัวข้อที่ระบุจริง
4. มีชื่อใหม่ เลข วันเวลาใหม่ หรือ negation ให้เส้นทางปกติรักษาข้อมูลนั้น; เงื่อนไขใหม่ที่รวมไม่ได้ถาม scope ไม่ลบทิ้ง

## 3. requested-task memory

1. แต่ละ task มี schema_version/domain/operation/query/targets/offered_options/status/provenance/response_id
2. เก็บเฉพาะผลที่ server complete แล้วและ client acknowledged; แยก session, TTL30นาที, ≤8 operation/session
3. เพิ่ม schedule, booking policy/navigation/live availability, members, contact และ game details นอกเหนือจาก price/controls/rules/catalog/equipment
4. หมวด booking กว้างที่มีหลาย operation เก่าถามว่า status/process/page ไม่เดาเลือกงานแรก
5. parent compound รวม same-operation ทุก child โดยเก็บ queries/request_targets; unknown child ยังอยู่ใน scope
6. ราคาใช้ schema เฉพาะและรักษา customer filters; หลาย price requests ที่ขัดกันต้อง clarification

## 4. execute หลัง resume

1. Single request ใช้ archived user query รัน pipeline ใหม่
2. Multiple requests ส่ง dialogue_resume_v1 ที่ตรวจ schema/version/domain+operation/จำนวนและชนิด requests
3. ห้าม fallback plan ที่ schema ผิดไปเป็น unrelated answer
4. Status สด fetch ใหม่ทุกครั้งตาม runtime cache0; explicit date/time คงไว้ Relative now/today resolve ใหม่
5. Mask ISO date ใน clock parser เท่านั้น ไม่เปลี่ยน date parser: 2026-09-17 at14:00 ต้องเป็น14:00 ไม่ใช่09–17
6. Generic plan/API/log ต้องบอก domain จริง; positive valid_price_task เท่านั้นที่จัดเป็นราคา

## 5. policy fields และคำตอบที่ตรงคำถาม

| Field | source ที่มี / gap | สิ่งที่ต้องตอบ |
|---|---|---|
| minimum booking notice | reservation_rules rule_booking_advance | อย่างน้อย1ชั่วโมง พร้อม source |
| maximum days ahead | ยังไม่มี source ยืนยัน | missing ของเพดานวัน ไม่ตอบ minimum hour หรือ weekly schedule |
| cancellation notice | rule_cancel_advance | อย่างน้อย1ชั่วโมง ไม่ตอบตารางเปิดศูนย์ |
| maximum Sessions | rule_booking_max_sessions | 3 Sessions ไม่เรียก3เครื่อง |
| maximum devices per booking | ยังไม่มี source ยืนยัน | missing จำนวนเครื่อง; ไม่ใช้ Sessions แทน |
| check-in | rule_checkin_advance | ล่วงหน้าสูงสุด30นาทีและก่อนเริ่มรอบ |
| payment deadline | rule_payment_10_minutes | ภายใน10นาทีพร้อมผลตามข้อกำหนดใน source |
| member count | structured members | 3กลุ่มแยกจาก25 member records |

Weekly schedule path ต้องไม่กลืน cancellation/payment/check-in/advance-offset fields จากคำว่า days/hours/book เพียงอย่างเดียว และ missing response ยังต้องผ่าน validator เดิม

## 6. state commit และ retry

1. ตรวจ turn identity/fingerprint/revision ก่อนเขียน
2. complete ครั้งแรกเป็น authoritative response; complete ซ้ำ returnFalse ไม่ overwrite archive/ack/history
3. API replay ใช้ original response ID/answer; changed input ที่ใช้turn IDเดิมเป็น client_turn_conflict409
4. same-session in-flight request อาจ session_busy409 มี retry_after_ms; retryด้วยturn IDเดิมหลังข้อแรกเสร็จ ต้องได้ response เดิม
5. Concurrent invariant ไม่เป็น multiuser load proof; late callbacks/crash ทุกจังหวะยังอยู่ backlog

## 7. เกณฑ์ตรวจที่แยกกัน

- Transport: HTTP status/ok/version/worker availability
- State: acknowledged history, domain/operation/scope/session/revision และ cache identity
- Execution: expected/executed/pending/answered/missing children; all executed ไม่รับรองทุก fact ถูก
- Content: actual requested quantity/unit/source clause และ missing policy อย่างเจาะจง; resume answerเหมือนเดิมอย่างเดียวไม่เป็น semantic oracle
- Real-world: เจ้าของยืนยัน policy/current prices และ booking snapshot ที่ตรวจไว้ แยกจาก fixtures

## 8. วงรอบที่ทำจริงและจุดแก้เกณฑ์

1. Baseline resume source/HTTP6จาก16; เพิ่ม domains/typed replay/immutable completion
2. Source14จาก16 →16จาก16 หลังแก้คำไทยเปิดปิดและ missing-policy response ให้ผ่าน validator
3. Variations9จาก12 →12จาก12 หลังรับ please และแยก same-intent English clauses; fixture time/date เปิดเผยบั๊ก ISO date ส่วน assertion booked/None เป็น oracle ที่ตั้งผิด แก้เกณฑ์แยกและเก็บ failure เดิม
4. Negative policy facets เปิดเผย helper จัดขั้นต่ำ/ยกเลิก/จำนวนเครื่องเป็น maximum days; ตรวจ actual answers แล้วแก้ weekly path/English ahead/source gap ไม่หยุดที่ predicate score
5. API duplicate caseแรก concurrent409session_busy เป็นการกันงานซ้อนตามโค้ด ไม่ใช่ client_turn_conflict; เก็บผลเดิม แล้วเพิ่ม retry oracle ที่เจาะจง error code
6. Runtime warmup/HTTP500 เก็บเป็น operational failure แยกจาก content score; pin interpreter ที่ตรวจและตรวจ APIจริงอีกครั้ง ไม่รับรอง root cause เพราะ restart ผ่าน

## 9. การปล่อยและทวนเอกสาร

1. สร้าง releaseใหม่แต่ละminorไม่ overlayตัวเก่า; app/web hashตรง source
2. Hash calendar/policy/competition chunks/review queue/rates ก่อนหลัง; เก็บ diffเทียบbackupรอบนี้
3. ตรวจ /health รุ่น/preflight/warmup และ actual chat request; healthokอย่างเดียวไม่พอ
4. รัน targeted source+HTTP ที่เกี่ยวข้อง; stop-on-first-failed-gateเพื่อไม่เพิ่มโหลดหลัง runtime failure
5. ชุด local ใช้ runtime/models ในเครื่องนี้; rebuildชุดแจกสองแบบ/clean-machineยังแยกเป็นงานค้าง
6. รายงานต้องระบุ testsพัฒนาไม่ใช่holdout, fixtureไม่ใช่real occupancy, และทุก66รายการที่ไม่ตรวจซ้ำไม่ตีว่าปิดแล้ว
'''
save('FLOW_R42_FINAL.md',flow)
analysis='# วิเคราะห์สาเหตุและคำตอบรายเคส r42.4\n\nConfidence ของ route/tool เป็นคะแนนภายใน ไม่ใช่ความน่าจะเป็นว่าข้อเท็จจริงถูก ไม่ใช้คะแนนสูงหรือ API200 เป็นเฉลย\n\n'
analysis+='## สาเหตุที่ยืนยันจาก code/trace\n\n| ปัญหา | เหตุที่เลือกคำตอบเดิม | ควรตอบ/ทำอย่างไร | แก้แล้ว/ข้อจำกัด |\n|---|---|---|---|\n'
for row in [
 ('กลับหมวดที่ไม่ได้ archive','task_from_response/selector ยังไม่รู้ operation นั้น จึง route คำสั้นใหม่','ค้น acknowledged requested task แล้ว execute query เดิม','เพิ่ม6หมวด; ไม่รับรองทุกสำนวน'),
 ('compound หาย child','keydomain/operation เดียวถูกแทนหรือ archiveแค่ข้อแรก','replay ทุก child รวม missing','typed requestsarray1–4'),
 ('เปิดปิดถูกแก้ให้ผิด','fuzzy span คร่อมคำที่ถูกข้างกัน','รักษาคำที่ถูกก่อนกู้คำผิด','exact span protection'),
 ('English pleaseไม่เข้าcontext','RETURNregex ต้องเริ่มที่return markerทันที','ยอมรับคำสุภาพแล้วตรวจtail/conditions','ยังจำกัดexplicitgrammar'),
 ('สองคำถามoperationเดียว','splitterมีกฎleft_intent==right_intentให้คืน1part','แยกเมื่อทั้งสองฝั่งมีquestion head','barelistยัง1part'),
 ('maximumdaysตอบminimum/schedule','จองล่วงหน้าถูกmaprule_booking_advance; Englishdaysกระตุ้นweeklywindow','แยกmax-days fieldซึ่งยังmissing','ไม่สร้างpolicyใหม่'),
 ('ขั้นต่ำ/ยกเลิกยังผิดหลังguard','predicateกันmaxแล้ว แต่weeklydaysหรือgenericbookingstepsยังชนะ','ขั้นต่ำ/ยกเลิกใช้source1hour','ตรวจoutputจริงเพิ่ม ไม่ใช้predicatepassแทน'),
 ('maximumdevicesตอบขั้นตอน','ไม่มีfacetจำนวนเครื่องและfallbackbookingsteps','ระบุsourcegapไม่ใช้3Sessionsเป็น3เครื่อง','ownerfactยังmissing'),
 ('กลุ่มสมาชิกตอบจำนวนคน','regexcountmembersชนะเพราะmemberอยู่ในmembergroups','3กลุ่มพร้อมแยก25records','sourcecountผ่าน ไม่รับรองofficialENnames'),
 ('ISOdateถูกอ่านช่วงclock','09-17ใน2026-09-17เข้าregexช่วงชั่วโมงก่อน14:00','dateคงเดิม clockเป็น14:00–15:00ตามslotfixture','TH/EN clocktest +freshfetchfixture'),
 ('completeซ้ำเปลี่ยนhistory','ไม่มีcheckresponsealreadycompletedก่อนappend','ครั้งแรกชนะ คงresponseID/history/ack','latentstorebug; HTTPมีsessionlockเดิม'),
 ('warmupผ่านแต่HTTP500','พบMemoryErrorและเปิดhelperprocessไม่ได้; defaultPythonต่างตามPATH','เก็บfailedrun+ตรวจrequestจริงและinterpreter/resource','pinnedrecoveryผ่านไม่ได้ระบุrootcauseครบ')]:
    analysis+='|'+'|'.join(row)+'|\n'
analysis+='\n## ประวัติ failed gates และการแก้ oracle\n\n- เก็บ source/HTTP baseline และ source rounds ทุกชุด ไม่แก้rawเก่า\n- booked assertionเดิมผิดกับคำตอบที่ถูกว่าnot available for full period; fixtureยังตรวจสถานะPC1ที่14:00–15:00และfetch2ครั้ง\n- date-only requestใช้ snapshot current timeโดยexplicit=False ไม่ควรassertNone; date substringต้องไม่กลายเป็นexplicit clock\n- concurrent409ในรอบแรกเป็นsession_busy ไม่ใช่ข้อความเปลี่ยน; oracleใหม่รับเฉพาะretryablebusyและตรวจreplayIDเดิมหลังretry\n- รอบ r42.4 แรกเกิดHTTP500: ถือtransport/runtime failure ไม่จัดว่าทั้ง16คำตอบsemanticผิด และไม่ลบผล0/16นั้น\n\n'
for label,p,s in [groups[0],groups[1],groups[5],groups[6]]:
    analysis+=f'## {label}\n\nหลักฐาน: {link(p)}\n\n'
    for c in s['results']:
        analysis+=f"### {c['id']}\n\nผลตามเกณฑ์: ผ่าน — {json.dumps(c.get('checks',{}),ensure_ascii=False)}\n\n"
        for record in c['records']:
            b=record['response'];cr=b.get('context_resolution') or {};contract=b.get('task_contract') or {}
            analysis+=f"- input: {record['payload']['question']}\n- HTTP: {record['status']}; route: `{b.get('route_category')}/{b.get('route_intent')}`; mode: `{b.get('mode')}`\n- resolved: {b.get('resolved_question')}; context reason: {cr.get('reason')}; used: {cr.get('used_context')}\n- outcome: {contract.get('outcome')}; children: {[(t.get('question'),t.get('status')) for t in contract.get('tasks',[])]}\n\n"
        analysis+='คำตอบสุดท้าย:\n\n'+c['records'][-1]['response'].get('answer',c['records'][-1]['response'].get('error',''))+'\n\n'
save('CASE_ANALYSIS_R42_TH.md',analysis)
table='| ชุด | ผ่าน/ทั้งหมด | คำขอ | หลักฐาน |\n|---|---:|---:|---|\n'
for label,p,s in groups:table+=f"| {label} | {s['passed']}/{s['executed_cases']} | {s['requests']} | {link(p)} |\n"
report=f'''# รายงาน r42.4 — สิ่งที่แก้และงานที่เหลือ

วันที่ตรวจ: 6 ตุลาคม2026 — Asia/Bangkok

## สิ่งที่แก้แล้วในรอบนี้

1. กลับหัวข้อเวลา/การจอง/สมาชิก/อุปกรณ์/รายละเอียดเกม/ติดต่อหลังเปลี่ยนเรื่อง ไทยและอังกฤษ
2. เก็บหลายchildของoperationเดียว ไม่ข้ามเกมที่ไม่มีข้อมูล; รองรับpleaseและคำถามอังกฤษสองclause
3. completed turnเขียนครั้งเดียว ไม่ซ้ำhistoryหรือแทนresponseที่ผู้ใช้เห็นแล้ว
4. รักษาคำไทยเปิดปิดที่ถูก ไม่ให้fuzzyแก้ทับ และแยกISOdateจากเวลาที่ถาม
5. แยกขั้นต่ำจอง/ยกเลิก1ชั่วโมง, max3Sessions, payment10นาที, check-in30นาที; maxdays/maxdevicesตอบsourcegap
6. สมาชิก3กลุ่มไม่ถูกตอบเป็น25คน; API/logของgenericreplayไม่ติดป้ายราคา

แก้source9ไฟล์ เพิ่มtest1ไฟล์ ไม่มีไฟล์ก่อนรอบนี้หาย; backup/diff/log/releaseเก่าคงไว้

## ผลอัตโนมัติบนเว็บจริง

{table}
รวม **{cases}/{cases} scenarios/conversations — {requests} HTTP requests** (รวมbusy/conflictที่ตั้งใจทดสอบ ไม่ใช่ทุกrequest200) และ source **{unit_methods}/{unit_methods} test methods** ตาม {link(unit_file)}.

เกณฑ์ resume หลายหมวดตรวจoperation/scope/answerเหมือนqueryเดิม; semanticoraclesเจาะสมาชิกและbookingfields/fixtures รวมกับregressionsเดิม ไม่ใช่fact completenessทุกหมวดและไม่ใช่unseenholdout.

Baseline r41.3 regradeด้วยเกณฑ์เดียวกัน: source {baseline[0]['regraded_passed']}/{baseline[0]['total']}, HTTP {baseline[1]['regraded_passed']}/{baseline[1]['total']}. หลักฐานเดิมยังอยู่ที่ {link(OUT/'BASELINE_REGRADED_R42.json')}.

ความเร็วHTTP200ในชุดนี้: p50{quantile(.5):.3f}s / p95{quantile(.95):.3f}s / max{max(latencies):.3f}s. ไม่ใช่SLAทุกคำถามหรือหลายผู้ใช้.

## ปัญหารันไทม์ที่พบระหว่างทำ

พบstartupMemoryError/LLM500และr42.4รอบแรกwarmupผ่านแต่chatHTTP500 รวมถึงhelperprocessเปิดไม่ได้หนึ่งครั้ง เก็บfailedrawทั้งหมดไว้ ไม่รวมเป็นsemanticwrong16เคส. Pythonที่ถูกเลือกตามPATHต่างกัน: startupแรกเคยใช้CodexPython3.12 แต่escalatedlauncherเลือกinstalledPython3.13; source testsใช้ReadyPython.

เริ่มใหม่ด้วยPythonเดียวกับsource testsโดยปรับPATHเฉพาะprocess; healthสุดท้ายwarmup={health.get('warmup',{}).get('ok')} / LLMpreflight={health.get('llm_preflight',{}).get('ok')} และตรวจAPIจริงตามตาราง. นี่เป็นการกู้ระบบและทำให้interpreterแน่นอน ยังไม่พิสูจน์ว่าPythonversionเป็นสาเหตุเดียวหรือปิดmemory/rootcauseครบ.

## การรักษา source และข้อมูล

- app/webตรงcandidate {sum(p['equal'] for p in audit['app_web_parity'])}/{len(audit['app_web_parity'])}ไฟล์
- calendarเจ้าของ/servicepolicy/competitionchunks/reviewqueue/rates hashเหมือนเดิม5/5
- curated/rulesที่เทียบต้นทางกับcandidate {sum(r['equal'] for r in knowledge)}/{len(knowledge)}ไฟล์ (ผลต่างถ้ามีอยู่ในJSON ไม่เดาว่าแก้ข้อมูลแล้ว)
- Gitstatusและdiff-checkรอบตรวจถูกroot exit0; failedsafe.directoryครั้งแรกเก็บแยก
- {link(OUT/'SOURCE_CHANGE_R42_4.diff')} และ {link(OUT/'SOURCE_AUDIT_R42_4.json')}

## ที่ยังเหลือ เรียงลำดับ
{priorities}
สถานะครบ66รายการและคำถามเจ้าของ: {link(OUT/'REMAINING_ISSUES_R42_TH.md')}. ไม่มีข้อสรุปว่าทั้ง66รายการปิดครบ.

## ใช้งานรุ่นที่ตรวจ

- เว็บ: [เปิดแชท r42.4](http://127.0.0.1:8090/)
- version: `2026.10.06-domain-resume-r42.4`
- ตัวเปิดที่pinPythonสำหรับเครื่องนี้: {link(OUT/'Open-Verified-R42.cmd')}
- Flow: {link(OUT/'FLOW_R42_FINAL.md')}
- วิเคราะห์: {link(OUT/'CASE_ANALYSIS_R42_TH.md')}
- Gates: {link(OUT/'FINAL_AUTOMATED_GATES_R42.json')}

ชุดlocalนี้พึ่งPython/Ollama/modelsที่มีในเครื่อง ชุดแจกWithModels/DownloadModelsยังไม่rebuildและไม่ตรวจcleanmachine. สถานะจองจริงและราคาปัจจุบันยังต้องหลักฐานเจ้าของ; fixture free→busyพิสูจน์freshfetchไม่ใช่occupancyจริง.
'''
save('REPORT_R42_4_TH.md',report)
python_dir=BASE.parent.parent/'PSU Esports Chatbot Ready 20261003/runtime/python'
# Resolve the explicitly verified runtime, not a similarly named directory.
python_dir=Path(r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python')
save('Open-Verified-R42.ps1',f'''$ErrorActionPreference='Stop'
$taskPythonDir='{python_dir}'
if (-not (Test-Path -LiteralPath (Join-Path $taskPythonDir 'python.exe'))) {{throw 'The verified local Python runtime is missing. This launcher is for this computer.'}}
$env:Path=$taskPythonDir+';'+$env:Path
& '{RELEASE / 'Open-PSU-Esports-Background.ps1'}'
''')
save('Open-Verified-R42.cmd','@echo off\npowershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Open-Verified-R42.ps1"\n')
assert len(backlog)==66 and unit_methods==135
print('REPORT',cases,requests,unit_methods,'healthy',health.get('warmup',{}).get('ok'),health.get('llm_preflight',{}).get('ok'))
