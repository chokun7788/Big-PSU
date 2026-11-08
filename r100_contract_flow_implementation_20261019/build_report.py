"""Build a report only from completed saved runs. No tests are launched here."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent
def read(p):return json.loads((R/p).read_text('utf8'))
run=read('subset05/RUN_FINISHED.json')
if not run.get('coverage_complete') or run['completed']!=91:raise SystemExit('Subset incomplete')
comparison=read('subset05/COMPARISON.json');old=comparison['r98_retained'];new=comparison['r100_candidate']
probes=read('CUSTOMER_PROBE_ANALYSIS.json');on=read('final_on04/RESULT.json');off=read('final_off04/RESULT.json');integrity=read('INTEGRITY_FINAL.json')
suites=[('New contract/binding/predicate checks','contract_final03'),('Existing task/readiness/snapshot checks','legacy_contract_final01'),('V2 source fixtures','v2_final01'),('Owner lifecycle','owner02'),('Rental source fixture','rental02'),('Competition source fixture','rules01')]
table=[];total=0;passed=0
for label,tag in suites:
 s=read('verification/'+tag+'/SUMMARY.json');total+=s['count'];passed+=s['passed'];table.append(f'| {label} | {s["passed"]}/{s["count"]} | [ผล](verification/{tag}/SUMMARY.json) |')
o=old['totals'];n=new['totals'];changes=comparison['changes'];regressions=[c for c in changes if c['regressed']]
review=read('subset05/CONTENT_REVIEW.json')
def frac(a,b):return f'{a}/{b} ({100*a/b:.2f}%)'
locales='\n'.join(f'| {loc} | {frac(old["locales"][loc]["passed"],old["locales"][loc]["total"])} | {frac(new["locales"][loc]["passed"],new["locales"][loc]["total"])} |' for loc in ('th','en','auto'))
text=f'''# R100 — ผลพัฒนา Flow ต่อจาก R97 ของ Astra / review R99

สถานะ: implementation candidate แยก ไม่ได้ติดตั้งทับระบบจริง และไม่ได้รัน full test 20,554 requests

## 1. สิ่งที่ลงโค้ดแล้ว

- Canonical task/predicate + RequestPlan V3 และผลราย Need ใน migrated dispatcher รวม fallback/rejection
- Pending binding จากตัวเลือกจริง พร้อม origin ราย slot สำหรับราคา service/เหมา/edition selection
- Typed predicate coverage guard ที่แยกคำตอบมี citation ออกจากคำตอบตรงสิ่งที่ถาม
- แยก booking steps, bookable periods, booking-required policy และ game/service selection
- Game edition ambiguity จากชื่อในข้อมูล, เลือกชื่อสั้นรอบสอง, explicit unknown mention และการรักษาเงื่อนไขเดิม
- ป้องกัน current facts ข้ามปีโดยไม่มี temporal applicability read และแก้ nested deadline/model budget reset
- Policy consumption/bring partial scope;แก้ประโยค quota ที่หลุดไปอยู่ทุก scope limit

Flow และสถานะที่ยังทำได้บางส่วนดู [IMPLEMENTED_FLOW_TH.md](IMPLEMENTED_FLOW_TH.md) มีตาราง P01–P14 เทียบ R99 ไม่ถือว่าครบทุกหมวดเพียงเพราะมี V3 wrapper

## 2. ผล focused tests

| ชุด | ผ่าน | หลักฐาน |
|---|---:|---|
{chr(10).join(table)}

รวม **{passed}/{total} contract checks ผ่าน** เป็น assertions รวม มีทั้ง schema/readiness, adversarial injection และ lifecycle ไม่ใช่ {total} คำถามลูกค้าอิสระหรือ accuracy 100% ของทุกคำถาม

ตารางใช้รอบผ่านล่าสุดของแต่ละ suite ระหว่างพัฒนา ชุดที่ตรึง source สุดท้ายตรวจด้วย `contract_final03`, `final_on04`, `final_off04` และ `subset05`;ไม่ได้อ้างว่า rerun ทุก fixture หลังการแก้ metadata ครั้งสุดท้าย

- Customer probes ปิด LLM: **{probes['summary']['final_off04']['contract_passed']}/23**
- Customer probes เปิด LLM: **{probes['summary']['final_on04']['contract_passed']}/23**
- [คำถามและคำตอบเต็ม ON](final_on04/ANSWERS.jsonl), [OFF](final_off04/ANSWERS.jsonl), [contract verdicts](CUSTOMER_PROBE_ANALYSIS.json)
- Fixtures owner/source ใช้ฐานทดสอบแยกและ approvals จำลอง ไม่มี facts ใหม่ถูกเพิ่มในฐานจริง
- ชุดทั้งหมดใช้พัฒนา/แก้โค้ดแล้ว จึงไม่ใช่ untouched holdout

## 3. เปรียบเทียบ 91 request keys เดิมกับ R98 retained

91 requests / 162 grades;เป็น development regression subset เดิม ใช้ checker และ GT เดิม ไม่รัน R98 ใหม่

| มิติ | R98 retained | R100 สุดท้าย |
|---|---:|---:|
| Positive literal/clause | {frac(o['positive_literal_passed'],o['positive_grades'])} | **{frac(n['positive_literal_passed'],n['positive_grades'])}** |
| Strict รวม protocol | {o['strict_passed']}/{o['grades']} | {n['strict_passed']}/{n['grades']} |
| Protocol failure reasons | {old['failure_reasons']['protocol']} | {new['failure_reasons']['protocol']} |
| Outcome failure reasons | {old['failure_reasons']['outcome']} | {new['failure_reasons']['outcome']} |
| Content failure reasons | {old['failure_reasons']['content']} | {new['failure_reasons']['content']} |
| Exceptions / empty | {o['exceptions']} / {o['empty_answers']} | {n['exceptions']} / {n['empty_answers']} |

| ภาษา | R98 | R100 |
|---|---:|---:|
{locales}

Requests ที่ positive text เปลี่ยน: {len(changes)};มี positive literal regression ในรอบสุดท้าย {len(regressions)} requests

หลักฐาน [COMPARISON.json](subset05/COMPARISON.json) มีคำตอบก่อน/หลังและ grades รายข้อ

คะแนน strict ที่ยังเท่าเดิมสะท้อนว่าปัญหา protocol/route expectations ยังไม่จบ ไม่ใช่เหตุให้ตัด protocol ทิ้ง ส่วน positive text เป็นเพียง keyword/clause contracts ไม่ใช่ independent semantic judgement

Outcome reasons เปลี่ยนจาก {old['failure_reasons']['outcome']} เป็น {new['failure_reasons']['outcome']} ต้องตรวจชนิดคำตอบตามสถานการณ์ร่วมกับเนื้อหา ไม่ประกาศว่าดีขึ้นทั้งหมดเพียงเพราะคะแนนข้อความเพิ่ม ดู [OUTCOME_CHANGES.json](subset05/OUTCOME_CHANGES.json)

**ไม่ใช้เปอร์เซ็นต์นี้แทน full-system accuracy** และไม่เทียบกับ full-test รุ่นก่อนโดยไม่คงชุดคำถามเดียวกัน

## 4. Loop ที่ทำและเหตุผลที่แก้

1. รอบแรกพบ FAQ ใหม่ถูกจัดเป็น game overview เพราะ What is ชนะ policy context → ให้ explicit task semantics มาก่อนคำเกริ่น;owner FAQ ใหม่/แก้ไขกลับมาผ่าน
2. Rental price again ถูกมองเป็น current hourly rate → rental pending adapter ผูก task เดิมก่อนตรวจ predicate;อ่านราคา revision ล่าสุดได้
3. ชื่อ edition ที่เลือกถูก lowercase ใน provenance → เก็บ raw question และ rebind source span จากข้อความจริง
4. Shared alias สั้นทำให้แทนชื่อเหลือ duty ซ้ำ → รวม title prefixes และเลือก ambiguous mention ที่ครบกว่า
5. หลังเลือก edition ปี 2027 ยังเคยได้ current offering → คง original qualified query และ reject เมื่อปีที่ถามยังไม่ผูกกับ source applicability
6. ใน subset รอบแรก “เกมนี้ต้องจองอะไร” ถูก booking-steps guard ปฏิเสธ → แยก purpose/service-selection predicate แล้วอ่าน game-service relation
7. อ่านคำตอบเต็มพบ unrelated per-booking quota ในคำตอบ alcohol → scope-limit renderer ต้องตรวจชนิด per_day/per_booking ไม่ใช่มี scope_limits แล้วใส่ quota ทุกครั้ง
8. VR without booking ถูกเข้า booking_steps → เพิ่ม booking_required policy contract แยกจากวิธีจอง คืนข้อความ source ที่ตรงคำถามได้
9. ตรวจ outcome แยกแล้วพบ equipment location พึ่งโมเดลเพราะ grammar ไม่รับ the หลังลบชื่อ → แยก equipment location จาก center location และให้ typed reader รองรับ determiner;catalog miss ระบุ public no-answer kind โดยยังเก็บ source status=missing_source
10. Compound results เคย remap เฉพาะแถว NeedResult แต่ receipt ภายในยังมี child-local n1 → remap receipts ทุกชั้นให้ผูกกับ parent Need ID และเพิ่ม assertion สำหรับสองเกม

เก็บผลที่ล้มและคำตอบก่อนแก้ไว้ใน `verification/contract01..04`, `owner01`, `rental01`, `subset01`, `subset02` ไม่แก้ log เดิมให้ผ่าน

## 5. ข้อที่ยังไม่ผ่าน checker และการตีความ

รอบสุดท้ายมี {len(review)} requests ที่ยังมี content reasons;อ่านเต็มใน [CONTENT_REVIEW.json](subset05/CONTENT_REVIEW.json)

- **ข้อมูลนอกเว็บ/ไม่ระบุหัวข้อ:** fallback ยังกว้างและไม่ตรง alternatives ของ GT;ไม่พบการสร้าง facts แต่ควรแยก missing topic กับ source unavailable ให้ชัดขึ้น
- **food/noise/damage:** summary ยังไม่ตอบ fine clause 100–500 THB ที่ GT รอ ต้องตรวจว่าเงินนี้ผูก action ใดก่อนนำมาใช้ ไม่เติมจำนวนเงินเพื่อผ่านคะแนน
- **alcohol:** source ยืนยันห้าม consume alcoholic beverages แต่ GT รอวลี alcohol consumption;คำตอบต้องยังคงขอบเขต bring ที่ source ไม่ยืนยัน ไม่เติมข้อห้ามนำเข้าเอง
- **VR without booking:** คืนกฎต้องจองก่อนใช้บริการแล้ว แต่ GT ยังรอประโยคปฏิเสธแบบตรงตัวและ one hour ซึ่งคำถามไม่ได้ถาม duration;ต้อง adjudicate clause relevance
- **Super Mario Odyssey zone:** ตอบ Switch service variants แต่ GT รอชื่อ Switch Zone ควรทำ relation projection ให้ตรงระดับ zone ที่ผู้ใช้ถาม
- **server/client:** ต้องตรวจ source/ขอบเขตที่ owner ตั้งใจให้รองรับ ไม่เปิด general-world answer เพียงเพื่อไล่คะแนน
- **คนนอกเล่นได้ทุกเกม:** universal eligibility claim ยังไม่ครบ ต้องแยก all catalog members กับ all members eligible และตอบ source gap ให้ตรงประเด็น
- **ราคาคนทั่วไป PC:** validity ยัง unknown และ audience narrowing ยังต้องปรับ ไม่อ้างตัวเลขเป็นราคาปัจจุบันโดยยืดอายุ source เอง

รายการนี้มีทั้ง content/capability gaps, source validity และ literal mismatch ไม่ใช่ทั้งหมดเป็นความผิดทางเนื้อหาแบบเดียวกัน

## 6. การเรียก LLM และเวลา

- Final ON probes: {on['model_attempts']} HTTP generate attempts / {on['model_response_opened']} response opened;เปิด LLM จริง แต่ deterministic tasks ไม่จำเป็นต้องเรียกทุกข้อ
- Final OFF probes: {off['model_attempts']} attempts
- 91-request run: {n['model_attempts']} attempts / {n['model_response_opened']} response opened;runtime exceptions {n['exceptions']}
- response opened ไม่พิสูจน์ว่าตีความถูก/schema ผ่าน/อ่าน body สำเร็จทุกขั้น
- median probe latency ON {probes['summary']['final_on04']['median_seconds']:.2f}s / OFF {probes['summary']['final_off04']['median_seconds']:.2f}s เป็น development observation ไม่ใช่ concurrency SLA
- รอบพัฒนาก่อน final (`focused_on01`) เคยมี TimeoutError 1 attempt จาก 2;เก็บไว้ ไม่รวมเป็น content failure และไม่ลบประวัติเพราะรอบ final ผ่าน
- reference clock real-data fixtures คือ 2026-10-16 ตาม baseline;ไม่ใช่วันปัจจุบันของผู้ใช้
- Live booking controlled unavailable จึงไม่ได้ตรวจความถูกต้องของ occupancy จริง

## 7. Integrity และขอบเขตส่งมอบ

[INTEGRITY_FINAL.json](INTEGRITY_FINAL.json) ยืนยัน R98 {integrity['baseline_files_verified']} source files unchanged, candidate database unchanged และ runtime ตรง final frozen source

แก้ source เดิม {len(integrity['candidate_changed_paths'])} ไฟล์ เพิ่ม modules {len(integrity['candidate_added_paths'])} ไฟล์ ไม่มีการแก้ข้อมูลหรือ approvals ในฐานจริง และยังไม่ติดตั้งทับ R78

นี่เป็น R100 implementation candidate **ยังไม่ใช่ portable production package** เอกสารเก่า R97/R98/R99 และ logs ก่อนหน้าเก็บไว้

## 8. งานถัดไปที่ยังจำเป็น

1. Generic grounded semantic RequestPlan ให้ typed/Legacy/LLM interpreters ใช้ contract เดียวทุก domain;ยังมี sensitive/fullmatch gates เดิม
2. Full required/optional/any_of read graph, typed claim values/units และ policy dependency/entailment ทุกชนิด
3. Pending kinds อื่น, universal eligibility และ zone-level offering projection
4. Future-date applicability executor;guard ปัจจุบันป้องกันคำตอบผิด แต่ยังไม่ทำ future inventory solver
5. Owner readiness/UI ให้บอก task gaps ชัด;ยืนยันข้อมูลวันมีผลราคาและ mode counts ที่ source ยังไม่มี
6. Protocol compatibility + untouched holdout ก่อน full test/ติดตั้งจริง

ไม่เรียกว่าแก้ R99 ครบทั้ง 14 ข้อแล้ว รายการที่ทำได้บางส่วนแจกแจงใน IMPLEMENTED_FLOW_TH.md
'''
(R/'RESULTS_TH.md').write_text(text,'utf8')
(R/'IMPLEMENTATION_STATUS.json').write_text(json.dumps({'candidate':'R100','base_flow':'R97 Astra, confirmed by user','runtime_base':'R98','contract_checks':{'passed':passed,'total':total},'focused_on':on,'focused_off':off,'same_key_subset':{'requests':91,'grades':n['grades'],'positive_literal_passed':n['positive_literal_passed'],'positive_grades':n['positive_grades'],'strict_passed':n['strict_passed']},'all_r99_items_complete':False,'full_test_executed':False,'production_installed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'report':str(R/'RESULTS_TH.md'),'checks':f'{passed}/{total}','positive_literal':f'{n["positive_literal_passed"]}/{n["positive_grades"]}','remaining_content_requests':len(review)},ensure_ascii=False))
