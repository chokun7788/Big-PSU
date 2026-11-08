"""Assemble the delivery report only after completed gates and source audit."""
import json
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
def link(label,p):return '['+label+']('+p.resolve().as_posix()+')'
run=R/'verification/comparison06';s=read(run/'analysis/SUMMARY.json');done=read(run/'TEST_COMPLETE.json')
assert done['complete'] and done['executions']==2940 and done['source_and_code_unchanged'] and done['model_identity_verified']
audit_path=max(R.glob('DELIVERY_AUDIT_*.json'),key=lambda p:p.stat().st_mtime);audit=read(audit_path)
assert audit['frozen_run']=='comparison06' and not audit['changed_reference_files'] and not audit['changed_frozen_files']
assert all(v==0 for v in audit['candidate_approval_tables'].values())
scope_path=max((R/'verification').glob('SCOPE_PROTOCOL*.json'),key=lambda p:p.stat().st_mtime);scope=read(scope_path);assert scope['passed'] and scope['tests']==26
gates=[('Scope และ LLM protocol',26,scope_path)]
for name,tag,count in [('Native schema/ราคา/บริบท', 'native_contracts09',20),('Owner add/edit/publish/withdraw','owner_lifecycle05',13),('Actual owner + published HTTP','http_contracts05',9),('Live binding/freshness/follow-up','live_bindings06',12)]:
    p=R/'verification'/tag/'SUMMARY.json';x=read(p);assert x['passed']==count and not x['failed'];gates.append((name,count,p))
p=R/'verification/real_model02/RESULT.json';m=read(p);assert len(m['checks'])==5 and all(m['checks'].values());gates.append(('โมเดลจริง 3 items / 5 checks',5,p))
smoke=R/'verification/actual_native_http02';assert read(smoke/'COMPLETE.json')['completed']==10
groups={(x['arm'],x['category'],x['locale']):x for x in s['groups']}
auto=groups[('automatic_routing','ALL','all')];hint=groups[('same_source_hinted','ALL','all')];new=groups[('reserved_automatic','ALL','all')]
assert auto['strict']==1388 and new['strict']==134
total_gates=sum(n for _,n,_ in gates);assert total_gates==85
status={'phase':'steps_1_to_5_complete_candidate_verified','steps_completed':[1,2,3,4,5],'candidate_system':str((R/'system').resolve()),
 'final_comparison':'verification/comparison06','executions':2940,'unique_same_source_questions':1400,'additional_questions':140,
 'same_source_strict':{'saved_R113':1136,'R114_automatic':1388,'denominator':1400},'additional_strict':{'passed':134,'denominator':140},
 'acceptance_checks_passed':85,'actual_native_http_inspections':10,'source_unchanged':True,'model_identity_verified':True,
 'production_installed':False,'approvals_created_in_candidate':0,'full_20554_request_test_run':False,
 'remaining_review':['6 rulebook heading/paragraph-granularity cases','weekday opening source conflicts/unknown effective interval','real live provider binding unavailable in candidate','English source translation coverage','VR and other billing eligibility require owner review before publication'],
 'completed_at':datetime.now().astimezone().isoformat()}
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
lines=['# R114 — รายงานพัฒนาและตรวจครบขั้น 1–5','',
 '## สถานะส่งมอบ','',
 '**ทำ implementation และ gates ของทั้งห้าขั้นครบใน candidate R114 แล้ว** ระบบเดิม R78 ยังไม่ถูกติดตั้งทับ ไม่มีการสร้าง approvals ของข้อมูลจริง และยังไม่เริ่ม Full Test 20,554 requests / 55,811 grades รอบใหม่',
 '', 'รอบสุดท้าย `comparison06` ครบ 2,940 executions: คำถามเดิม 1,400 ข้อแบบระบุหมวด + 1,400 ข้อแบบเลือกหมวดอัตโนมัติ + คำถามเพิ่มเติม 140 ข้อ ใช้โมเดลเดิมและ read model เดียวกับ saved R113 ไม่รัน baseline ใหม่',
 '', '## 1. สิ่งที่ทำครบตามห้าขั้น','',
 '| ขั้น | สิ่งที่เปลี่ยน | หลักฐาน |','|---|---|---|',
 '| 1 ขอบเขตคำตอบ | ตรวจ entity/resource/service/field/year ก่อนเลือกหลักฐาน ปฏิเสธ unknown target และห้ามเลือกหลักฐานทั้งหมวดเมื่อยัง bind entity ไม่ได้ | 26 scope/protocol invariants และคำถาม negative ใน corpus |',
 '| 2 ตัวอ่านเฉพาะงาน | 14 domains; catalog จาก offerings ทั้งชุด, rate/rental จาก FK, เงื่อนไขนโยบายครบ, กติกาพร้อม dependencies, calendar/live ใช้ typed adapters | Native schema checks และ source-contract comparison |',
 '| 3 LLM protocol | Schema/indexed items, salvage ข้อที่ดี, แยก transport/schema/model identity, budget ไม่เกิน 2 calls ต่อ request | โมเดลจริง + malformed-response fixtures |',
 '| 4 เชื่อมแชทจริง/owner | CommonAnswerer ใช้ snapshot/release/epoch ใหม่; เพิ่ม/แก้/ถอนโดยข้อมูล; draft แยก published; multi-need ใช้ snapshot/cache/budget ร่วม; financial follow-up เก็บเพียง intent | Owner HTTP, chat HTTP, lifecycle และ native candidate HTTP |',
 '| 5 เทียบก่อน/หลัง | อ่าน saved winner ของ R113 รายหมวด เปรียบเทียบทั้ง hinted และ automatic พร้อมคำถามเพิ่มเติมและเก็บทุก strict fail | รอบ comparison06 และรายงานทุกข้อที่ไม่ผ่าน |',
 '',link('Flow เต็ม 14 หมวด พร้อม diagram',R/'FLOW_COMPLETE_TH.md'),'',
 '## 2. ผลเปรียบเทียบ','',
 '| ชุด/วิธี | ผล strict | ความหมาย |','|---|---:|---|',
 '| Saved R113 winner รายหมวด | 1,136/1,400 = **81.14%** | ให้หมวดอยู่แล้ว เลือก winner จากผลเดิม ไม่รันใหม่ |',
 '| R114 ระบุหมวด | 1,388/1,400 = **99.14%** | เปรียบตัวอ่านบน source เดียวกัน |',
 '| R114 เลือกหมวดเอง | 1,388/1,400 = **99.14%** | เพิ่ม router จริง โดยไม่ส่ง category ให้ engine |',
 '| คำถามเพิ่มเติม | 134/140 = **95.71%** | หลังตรวจ/พัฒนาแล้วเป็น development validation ไม่ใช่ blind holdout |',
 '', '**ห้ามอ่านตัวเลขนี้เป็นเปอร์เซ็นต์ความถูกต้องของผู้ใช้จริง:** strict ตรวจ source IDs, values, evidence, scope และ expected state แบบ exact ชุดเดิมถูกใช้พัฒนาแล้ว ชุดเพิ่มเติมก็ถูกเปิดดูหลังรอบแรกแล้ว ต้องมีชุดที่ยังไม่เคยใช้พัฒนาและ human adjudication ก่อนอ้าง generalization',
 '', 'ชุดเดิมแบบ automatic มี positive content exact 1,120/1,120 และรวม unknown 1,400/1,400 เมื่อแยกสถานะออก เป็นผลของเกณฑ์เดิมเท่านั้น ไม่ใช่การตรวจ semantic อิสระ ชุดเพิ่มเติม positive content exact **78/84** จึงไม่ควรอ้างว่าแก้คำถามใหม่ได้ครบ',
 '', '### แยกภาษา/locale ของชุดเดิม','', '| locale | strict R114 automatic |','|---|---:|']
for loc in ['th','en','auto']:
    x=groups[('automatic_routing','ALL',loc)];lines.append(f"| {loc} | {x['strict']}/{x['n']} = {100*x['strict']/x['n']:.2f}% |")
lines+=['', 'auto คือค่าที่ผู้ใช้ส่งมา ไม่ใช่ภาษาที่สาม ชุดเพิ่มเติมทั้งหมดเป็นภาษาไทย ยังไม่มี English holdout ใหม่',
 '',link('ตารางครบทุกหมวดและคะแนนแยกภาษา',run/'analysis/COMPARISON_REPORT_TH.md'),'',
 '## 3. ข้อที่ยังไม่ผ่าน strict และการตรวจสาเหตุ','',
 '- **12 คำถาม C12 × 2 วิธี = 24 rows:** source claim/value/evidence ตรงทุกข้อ แต่ oracle เดิมคาด `answer` เมื่อมีทั้งสถานะพร้อมกับ stale/unavailable ในคำถามเดียวกัน R114 ส่ง `partial` เก็บคะแนน strict fail ตามเดิม ไม่เปลี่ยน expected เพื่อยกคะแนน เหล่านี้เป็นสถานะของ provider fixture ไม่ใช่ model transport failure และไม่ใช่ผลตรวจสถานะเครื่องจริง',
 '- **6 คำถามกติกาเพิ่มเติม:** ถามทั้งหัวข้อ แต่ oracle เลือกเพียงย่อหน้าเดียว ตรวจแล้วทุกย่อหน้าที่คืนเพิ่มอยู่ในเอกสารและหัวข้อเดียวกับ expected ไม่มี missing claim/wrong value/evidence mismatch อย่างไรก็ตามยังต้องอ่าน semantic scope เป็นรายข้อ จึงคง fail และไม่เพิ่มคะแนนแบบปรับ oracle',
 '- ไม่มี missing claim/wrong value/evidence mismatch หรือ extra claim ในชุดเดิมรอบสุดท้ายตาม grader เดิม ข้อนี้ไม่ได้ยืนยันว่าเนื้อหา original source ถูกต้องสมบูรณ์หรืออ่านภาษาคนได้ทุกกรณี',
 '', link('รายละเอียด strict fail ทุกข้อ พร้อมคำถาม คำตอบ expected และ source refs',run/'analysis/FAILURES_DETAIL_TH.md'),
 '', link('ผลตรวจเอกสาร/หัวข้อและ state ของทั้ง 30 rows',run/'analysis/SOURCE_BASED_FAILURE_REVIEW.json'),'',
 '## 4. ปัญหาที่พบระหว่างพัฒนาและแก้แล้ว','',
 '| ปัญหา | สาเหตุ | การแก้ |','|---|---|---|',
 '| คำถามต่างหมวดได้คำตอบใกล้เคียงแต่ผิดเรื่อง | ให้ generic คำว่า studio/play/price ชนะ business action และส่ง evidence ทั้งหมวดให้ LLM | จัด task/entity priority; scope pool ตาม field; ไม่ส่ง unbound entity ให้โมเดล |',
 '| ตรวจเลขจองกลับได้วิธีแก้การจอง | เลือก C08 policy แทน predicate ตรวจสถานะรายการ | แยก opaque reservation reference เป็น C12; ไม่มี observation ก็ยืนยันไม่ได้ |',
 '| ระหว่างถูกมองว่าเครื่องว่าง | จับ substring ว่าง ในคำว่า ระหว่าง | เพิ่มขอบเขตความหมายของ availability |',
 '| คำถามหลายส่วนทำเงื่อนไขหลุด | แยกเครื่องหมาย ; ทุกแห่ง | เก็บ trailing qualifier กับคำถามเดิม เช่น I am not External Visitors |',
 '| คิดกลุ่ม/คน/เวลาไม่ชัด | หน่วยราคาไม่เหมือนกัน และ duration ต่อรอบถูกปนกับ total duration | ใช้ typed unit; แยก explicit per-session duration; ไม่เดากฎปัด; source ไม่พอถามเพิ่ม |',
 '| เหมา PC ได้ราคาหลายโซนใน native DB | tuple match เจอ audience/period หลายรายการแต่ไม่ได้กรอง FK zone | ใช้ rental_pool จาก zone/service/audience/period; เก็บ exact subject สำหรับ imported references |',
 '| ตอบคำถามเติมนาที/กลุ่มไม่ได้ | missing-slot reply ไม่เก็บ intent ที่ส่งจริง | เก็บ r114_pending ใน server-produced delivered state; อ่าน snapshot ใหม่ ไม่เก็บราคาใน history; ไม่รับ undelivered context |',
 '| กติกาบางคำถามช้า ~16 วินาที | ตีความปีซ้ำหลายร้อยครั้ง พร้อมสแกนชื่อเกมทุกชื่อ | compile ชื่อเกมที่มี edition year ต่อ snapshot index; ไม่ cache คำตอบธุรกิจ |',
 '| ข้อที่ model plan หายทำให้ข้อดีถูกทิ้ง | ถือ batch เป็นผลเดียว | validate ราย item; duplicate/missing บล็อกเฉพาะ item; แยก identity จาก transport |',
 '| สถานะสดในคำถามรวมไม่ผ่าน native adapter | ใช้ static engine path เมื่อมีหลาย need | ใช้ native calendar/live ต่อ need พร้อม shared snapshot/provider cache/model budget; เก็บ need ledger |',
 '| ข้อมูลใหม่ไม่ปรากฏหรือเก่ายังอยู่ | รายการเกมต้องมี offering; cache/withdrawal ต้องผูก epoch | compile relation จาก snapshot ปัจจุบัน; เพิ่ม/แก้/ถอนมี acceptance gate |',
 '| debug ยังอาจมี claim เก่าเมื่อ snapshot เปลี่ยน | delivery invalidation ล้างเฉพาะ body/hits | ล้าง claims/receipts/query details ที่อาจฟื้นข้อมูลเก่าและส่ง retry |',
 '', '## 5. Gates ที่ผ่าน','', '| Gate | ผ่าน | หลักฐาน |','|---|---:|---|']
for name,n,p in gates:lines.append(f'| {name} | {n}/{n} | {link(p.parent.name if p.name=="SUMMARY.json" else p.name,p)} |')
lines+=['', f'รวม **{total_gates}/{total_gates} acceptance checks** บนขอบเขตที่ระบุ มีการตรวจโมเดลจริงและ actual HTTP ส่วน lifecycle approvals ที่ทดสอบเกิดในฐานข้อมูล synthetic เท่านั้น',
 '', f"รอบเปรียบเทียบเรียกโมเดล **{s['model']['calls']} ครั้ง**: transport/schema ผ่าน {s['model']['transport_ok']}/{s['model']['schema_ok']} ไม่มี invalid item ในรอบนี้ การเปิด LLM ไม่บังคับเรียกโมเดลทุกคำถาม โมเดล digest ตรวจตรงก่อน/หลังทดสอบ",'',
 '## 6. ตรวจแชทกับข้อมูล candidate ที่ย้ายมาจริง','',
 'ตรวจ 10 HTTP turns เพิ่มเติมบนฐานข้อมูล R114 จริง โดยไม่มีการแก้ข้อมูลผ่าน API:',
 '', '- รายการเกม PS5 อ่าน offered catalog ครบตามข้อมูล; ที่อยู่/ตึก/ชั้นอ่านจาก field ที่มี source',
 '- เหมา PC Zone หน่วยงานภายนอกครึ่งวันตอบเฉพาะแพ็กเกจ **2,000 บาท** จาก record package_21',
 '- “บุคคลภายนอก” ไม่ยืนยันว่าอยู่กลุ่ม General Adult เพราะอาจเป็น General Student ให้เลือกจากกลุ่มจริงในตาราง',
 '- VR General Adult 2 คน 2 รอบ รอบละ 30 นาที คำนวณจาก rate ปัจจุบันที่ owner reaffirmed: 525 × 2 × 2 = **2,100 บาท** ภายใต้คำยืนยันหน่วยต่อคนของเจ้าของ ยังต้องให้เจ้าของ review ราคา/หน่วย/eligibility ก่อนอนุมัติเผยแพร่ ไม่ได้ยืนยันความว่างหรือจำนวนคนที่จองได้',
 '- ถ้าขาดนาทีต่อรอบ ระบบถามเพิ่ม และ HTTP turn ถัดไป “รอบละ 30 นาที” ใช้ service/audience เดิมแล้วอ่าน source ใหม่ได้',
 '- วันหมดอายุเครดิตไม่มีก็ไม่แต่ง; “วันนี้เปิดไหม” ไทย/อังกฤษตอบวันที่และยังยืนยันไม่ได้ตาม source conflict',
 '', link('Raw คำถาม/คำตอบ HTTP จริง 10 turns',smoke/'RESULTS.jsonl'),'',
 '### ปัญหาข้อมูลเปิดบริการที่ยังต้องยืนยัน','',
 '**เวลาเปิดวันจันทร์–ศุกร์ใน native schedule มีสถานะ `conflicted` และ value=null ทั้งห้าวัน** ขณะที่ bookable_periods เป็น known จึงไม่สามารถเอาเวลารับจองไปยืนยันว่าเปิดจริงในวันที่ถามได้ validity ของ schedule ทั้งเจ็ดวันยัง unknown วันเสาร์–อาทิตย์มี open_periods=[] แต่ไม่ได้ใช้เดาแทนวันธรรมดา',
 '', 'ควรให้เจ้าของยืนยัน open_periods และช่วงมีผลของแต่ละวัน รวมทั้งวันปิดพิเศษ หากมี source ที่ใหม่กว่าให้ผูก revision/source แทนการปลด conflicted โดยไม่มีหลักฐาน การตอบ unconfirmed ตรงนี้เป็น data gap ที่ตรวจพบจริง ไม่ใช่ข้อพิสูจน์ว่า code calendar ทำงานไม่ได้',
 '', link('ค่าฟิลด์และหลักฐานตารางเวลาต้นทางที่ตรวจ',smoke/'SCHEDULE_SOURCE_REVIEW.json'),'',
 '## 7. ข้อมูลและการรักษาของเดิม','',
 '- เพิ่ม 227 owner-backed/imported records ใน candidate รวม native rental_package 24 รายการ แล้วเพิ่ม current-rate affirmation อีก 1 record; affirmation revision ล่าสุดผูกคำยืนยันหน่วยต่อคนกับ hash ของ 24 rates เดิม',
 '- ถอน copied rental duplicates 24 รายการเฉพาะ candidate หลังตรวจ zone/audience/period/amount ตรงกัน เก็บ revision/history ไม่ลบต้นทาง',
 '- ขณะส่งมอบ draft heads ที่ไม่ถอน **806 records**; candidate approvals **0** และ active release ยังว่าง การอนุมัติ/เผยแพร่เป็นขั้นตอนของเจ้าของ',
 f"- ตรวจ reference files เดิม **{audit['reference_files']} ไฟล์** จาก R106/R113 ไม่พบการเปลี่ยน; ตรวจ frozen-run files {audit['frozen_files']} ไฟล์ตรงทั้งหมด และ parse Python {audit['candidate_python_files_parsed']} ไฟล์ผ่าน ไม่มีการแก้ R78 ในงานนี้ แต่ไม่มี pre-work R78 hash manifest จึงไม่อ้างว่าได้พิสูจน์ hash ทุกไฟล์ R78", 
 '- ชุดทดสอบไม่ถามหน่วยโทษ Tekken ที่เจ้าของสั่งงด ไม่สร้างข้อมูล/approvals แทนคำยืนยันที่ยังไม่มี',
 '',link('Delivery source/hash/approval audit ล่าสุด',audit_path),'',
 '## 8. ข้อจำกัดและสิ่งที่ต้องทำก่อนใช้งานจริง','',
 '1. Review หกข้อกติกาที่ granularity ของ oracle ไม่ตรงคำถาม; ยังไม่ถือว่าถูก semantic ครบและยังไม่เปลี่ยน expected',
 '2. ยืนยันเวลาเปิดวันธรรมดาที่ source ขัดกัน และช่วงมีผลจริง',
 '3. ให้เจ้าของ review ราคา หน่วยคิดเงิน ช่วงจำนวนคนและ eligibility โดยเฉพาะ VR ที่ต้นทางมีช่วงจำนวนคน 1–5 และมี owner affirmation ต่อคนเพิ่มเติม อย่าใช้ผลคำนวณแทนการยืนยัน booking eligibility',
 '4. Candidate ยังไม่มี live provider binding จริงที่ยืนยันใช้งานได้ ผล C12 fixture ไม่ใช่สถานะเครื่องปัจจุบัน',
 '5. ข้อความกติกาภาษาอังกฤษบางกรณียังใช้ต้นฉบับไทยและมี translation-missing flag; เกณฑ์ source exact ไม่ตรวจคุณภาพภาษา',
 '6. บาง policy/rules ยังคงใช้ scoped FAQ/prose และ common compatibility readers การมีข้อมูลครบไม่เท่ากับทุกเงื่อนไขถูกทำเป็น executable predicate ใหม่แล้ว',
 '7. ก่อนอ้างความแม่นยำจริง ต้องใช้คำถามผู้ใช้ที่ไม่เคยใช้พัฒนาและให้คนตรวจ semantic; Full Test 20,554 requests เป็น gate ถัดไปที่ยังไม่รันในงานนี้',
 '', '## 9. เปิดทดลอง/หยุด','',
 link('เปิด R114 preview และ owner editor',R/'START_R114_PREVIEW.cmd')+' — แชท 8134 / owner 8135; แยกจากระบบเดิมและแบบสอบถาม 8120',
 '',link('หยุด R114 preview',R/'STOP_R114_PREVIEW.cmd'),'',link('คู่มือเพิ่ม/แก้/ถอนข้อมูล',R/'OWNER_GUIDE_TH.md'),'',
 'การตรวจผ่านแชทจริงเสร็จแล้วและหยุด process ที่เริ่มไว้หลังตรวจ ไม่ทิ้ง server ชุดทดสอบค้าง ให้เปิดด้วย launcher เมื่อต้องการใช้งาน',
 '', '## 10. รอบระหว่างพัฒนา','',
 '- comparison01: completed revision แรก เก็บผลก่อนแก้ router และ pool',
 '- comparison02: หยุดเพื่อแก้ performance เก็บ **1,274 partial rows** และ ABORTED_FOR_FIX.json ไม่ถือว่าครบ',
 '- comparison03–05: completed intermediate revisions พร้อม frozen code archive เก็บความผิดพลาดไว้ ไม่ overwrite outputs',
 '- **comparison06: final frozen revision** ใช้กับคะแนนรายงานนี้เท่านั้น',
 '', 'ผลพัฒนาจากชุดที่เปิดดูแล้วมีโอกาส optimistic จึงรายงานข้อจำกัดไว้และไม่อ้างว่าได้ Flow ที่ดีที่สุดในทุกสถานการณ์', '']
(R/'FINAL_REPORT_TH.md').write_text('\n'.join(lines),'utf8')
print(json.dumps({'steps_completed':[1,2,3,4,5],'gates':total_gates,'strict_saved_R113':1136,'strict_R114':1388,'n':1400,'new_strict':134,'new_n':140,'report':str((R/'FINAL_REPORT_TH.md').resolve())},ensure_ascii=False))
