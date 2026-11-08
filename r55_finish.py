import json,collections,statistics,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r55_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def read(n):return json.loads((OUT/n).read_text(encoding='utf-8'))
def save(n,s):
    with (OUT/n).open('x',encoding='utf-8') as f:f.write(s)
def metrics(rows):
    a=sorted(r['elapsed_sec'] for r in rows)
    return dict(requests=len(a),median=round(statistics.median(a),3),p95=round(a[math.ceil(.95*len(a))-1],3),max=round(a[-1],3),mean=round(statistics.mean(a),3))
web=read('web_final6.json');near=read('near_final7.json');controls=read('controls_final7.json');units=read('units_final8.json');audit=read('final7_PRESERVATION_AUDIT.json')
ca=read('controls_semantic_audit_v2.json')
summary=dict(runtime='2026.10.10-service-r55.7',units=units,web_candidate6=dict(verdicts=dict(collections.Counter(r['verdict'] for r in web)),failures=sum(bool(r['errors']) for r in web),latency=metrics(web)),followups_candidate7=dict(requests=len(near['rows']),checks=len(near['checks']),failures=sum(bool(c['errors']) for c in near['checks']),latency=metrics(near['rows'])),controls_candidate7=dict(requests=len(controls),failures=sum(bool(r['errors']) for r in controls),source_content_checks=len(ca['checks']),source_content_failures=sum(bool(c['errors']) for c in ca['checks']),latency=metrics(controls)),preservation=audit)
save('SUMMARY.json',json.dumps(summary,ensure_ascii=False,indent=2))
flow='''# Flow ฉบับปรับปรุง r55: คำถามบริการ เกม ราคา การจอง และประวัติสนทนา

## 1. เป้าหมายและแหล่งที่เชื่อถือได้

แก้จากคำถามร้านเกมจริงใน r54 และผลผิดที่พบในแต่ละรอบของ r55 ใช้ข้อมูลเจ้าของ 18 claims ใน user_service_facts_20261008.json, ตารางราคา/เช่าเหมาเดิม, catalog เกม, rulebooks และ API จองที่ผ่านเงื่อนไขสด ไม่แก้ตัวเลขหรือข้อยกเว้นของศูนย์เพื่อให้คำตอบผ่าน test

ขอบเขตรอบนี้คือการเลือกข้อมูลและรักษาสิ่งที่ผู้ใช้ถาม ไม่มีการเปลี่ยนจำนวน worker หรือความสามารถ GPU; งานพร้อมกันของโมเดลยังใช้ระบบ queue เดิม

## 2. ขั้นตอนก่อนแก้และก่อนเปิด candidate

1. อ่าน handoff และผล r54 ตรวจโปรเจกต์จริงก่อนแก้
2. ขอสิทธิ์เขียน ROOT ผ่านระบบ สำรอง source 324 ไฟล์และ hash
3. เก็บ candidate, stdout/stderr, raw responses และผล test เป็นชื่อใหม่ทุกครั้ง
4. หลังแก้ ตรวจ owner hashes 38 ไฟล์ และ source ของ app ใน candidate เทียบ ROOT
5. หาก Git ใช้ไม่ได้ ให้เก็บ diff จาก snapshot ห้าม reset หรือ clean เพื่อทำให้ checkout ดูสะอาด

## 3. รับข้อความและประวัติ

รับ question + locale + session ID + turn ID + last_seen_response_id

- Normalize Unicode/ช่องว่างตามระบบเดิม; typo recovery ที่เพิ่มต้องมี subject ช่วย เช่น สลิปผิด ไม่เปลี่ยนเลขเครื่อง เวลา วัน ราคา หรือคำปฏิเสธ
- เก็บ original_question และ resolved_question แยกกัน
- ใช้ประวัติ session เดียวที่เข้าเงื่อนไข context และ ACK เท่านั้น; timeout/ข้อความที่ใช้เป็น context ไม่ได้ต้องไม่สร้าง target
- คำถามใหม่ที่ระบุเกมหรือ operation ชัดเจนชนะหัวข้อก่อนหน้า
- คำตอบสั้น PC/ทั้งหมด/กลุ่มผู้ใช้/PC2 ใช้งานเดิมเมื่อมี pending slot หรือ scope ที่ยืนยันได้ ไม่เลือกจากตัวอย่างเกมหลายชื่อที่บอทเขียนเอง

## 4. ตรวจคำถามหลายส่วนก่อน handler ที่ตอบทันที

แยก clause ตาม grammar และ operation ที่เห็นจริง จำกัด adapter ใหม่ 2–3 ส่วน; หากแยกไม่ได้ส่งให้ระบบเดิม

แต่ละส่วนเก็บ subject/target/customer group/duration/people/date/time ของตัวเอง เช่น

| คำถาม | สิ่งที่ต้องตอบ |
|---|---|
| PC มีเกมอะไร แล้วบุคคลทั่วไปสองชั่วโมงกี่บาท | เกม PC และราคา PC กลุ่มที่ระบุ 120 นาที |
| วันนี้ PC1 10โมง และ PC2 11โมงว่างไหม | PC1 10:00 และ PC2 11:00 วันที่เดียวกัน |
| ชำระเงินยังไง แล้วจ่ายเงินสดได้ไหม | วิธีโอนจาก source และ cash policy ที่ยังไม่ยืนยัน |

ห้าม price plan ฝั่ง server เขียนคำถามหลายส่วนให้เหลือเรื่องราคาเรื่องเดียว ก่อน pipeline ได้รับข้อความ

## 5. แยก entity และหน่วย

- หมายเลขเครื่องต้องไม่มี colon/หน่วยเวลา/หน่วยเงิน/จำนวนคนตามหลัง; PC1 ต่างจาก PC10 และ PC 10:00
- แยก ISO date ก่อนอ่านช่วงเวลา; ห้ามอ่าน 9:00-9:30 เป็น 00:00-09:00
- แปลงคำระยะเวลาไทย/อังกฤษเฉพาะข้างหน่วย เช่น สองชั่วโมง/two hours = 120 นาที
- จำนวนคนใช้กรอง package capacity เช่น Nintendo 4 คน ไม่ใช้ราคา package 1–2 คน
- VR ช่วงระบุ 09:00–09:30 ตรวจการครองรอบ 09:00–10:00 ตามที่ผู้ใช้ยืนยัน; นาทีต่อแพ็กเกจสำหรับคิดเงินยังเป็นค่าจากตารางราคา

## 6. เลือกข้อมูลตาม operation

| Operation | ตัวทำงาน | ข้อจำกัดที่ต้องแสดง |
|---|---|---|
| Policy/ข้อมูลบริการ | owner claims ก่อน semantic retrieval | ไม่มีคำยืนยันของ field ที่ถามต้องตอบ unknown |
| ราคา | typed plan และ fee calculator เดิม | กลุ่ม/บริการขาดให้ถามเฉพาะ slot; แสดง validity ของราคา |
| งบประมาณ | integer packages = floor(budget/unit fee) | แสดงเงินเหลือ, capacity, eligibility; ราคา 0 ไม่หมายถึงเวลาไม่จำกัด |
| เกมทั้งหมด/เกมในโซน/จำนวนเกม | catalog เดิม | deduplicate ชื่อข้ามโซน; ไม่เปลี่ยน install permission เป็น list เกม |
| เวลาปกติ | calendar/schedule adapter เดิม | ไม่ใช่ข้อมูลเครื่องว่าง; วันปิดพิเศษชนะตารางปกติ |
| สถานะจอง | booking API + date/freshness/source guards | unavailable/stale/wrong date ไม่ใช่ว่าง |
| กฎภาพรวม | explicit game + broad request parser | ปี/หัวข้อเฉพาะต้องไม่ถูกล้างทิ้ง; ภาพรวมไม่ใช่กฎครบทุกข้อ |
| กฎครบทุกข้อ/ต่อหน้า | rulebook coverage + ACK cursor | returned union = expected IDs, ไม่มีซ้ำ |
| ปุ่มควบคุม | control catalog resolver + structured handler เดิม | ไม่เดา family/version/ปุ่มที่ไม่มี และคงคำเตือนแหล่งรอง |
| สเปก PC | local hardware facts เดิม | Home inventory ไม่ได้ยืนยันองค์ประกอบภายในเครื่อง |

ค่าความมั่นใจ .98/.9 เป็นคะแนน routing ตาม heuristic ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก 98%/90%

## 7. ข้อกำหนดก่อนเรียกว่า complete

ตรวจ target, operation, units, negation, จำนวนส่วนที่ผู้ใช้ถาม และ evidence ก่อนปิดงาน

- ถ้าขอทั้งหมด ต้องบอก scope: เกมทั้งโซน / ทุกบริการ / กฎทั้งเอกสาร
- ภาพรวมกฎต้องตอบหลายหัวข้อตาม source ไม่เลือก clause เดียวแล้วเรียกว่าครบ
- ในคำถามหลายส่วนต้องตอบทุกส่วน; unknown ของ cash ไม่ทำให้วิธีโอนหาย
- English ใช้ข้อเท็จจริง/เงื่อนไขเดียวกับไทย ตัวเลข/ราคา/วัน/IDs ต้องตรง ไม่ถือว่าคนอนุมัติคำแปลแล้วเพียงเพราะ test ผ่าน
- แก้คำปนภาษาอาหรับในแถว Tekken ที่รู้ provenance เฉพาะข้อความแสดงผล; เก็บ raw source เดิม

## 8. สถานะและ diagnostics

แยก transport_complete, checked_content, safe_unconfirmed, live_without_oracle, review_pending

timeout ต้องคืน partial_progress ราย request: ขั้นตอนล่าสุดและ events ที่ส่งแล้ว; cause_confirmed=false จนกว่าจะมีหลักฐานสาเหตุ ไม่เรียกขั้นตอนล่าสุดว่าเป็น root cause ทันที

performance cache จำกัด 64 requests และ 16 events/request ไม่เก็บข้อความถามตอบไว้ใน cache นี้

## 9. Loop ที่ใช้จริง

baseline → unit ของ parser/slot และ negative controls → fixture ที่รู้ผล → candidate ใหม่ → HTTP jobs + session ACK → อ่าน answer/trace → ตรวจ omission → แก้เงื่อนไขที่ยืนยันได้ → test ส่วนที่เกี่ยวข้องอีกครั้ง

ตรวจทาน 10 จุด: เลขเครื่อง/เวลา, policy subject, กลุ่มราคา, จำนวนคน, affordability, หลาย clause, scope เกม, rule cursor, language/source, timeout diagnostics; เพิ่มรอบหลังอ่านคำตอบพบ broad RoV ถูกตอบเป็น clause เดียว และ adapter ปุ่มใช้ session alias list คนละชุดกับ catalog

อย่าถือว่า test ที่ตรวจแค่ชื่อเกมพิสูจน์ความครบ ต้องเพิ่ม oracle โดยเก็บผลเก่าไว้ ตัวอย่าง c124 เพิ่ม broad_rules_need_overview หลังพบ omission แม้เกณฑ์เดิมผ่าน

## 10. Release gates และผลรอบนี้

อ่าน RESULTS_ANALYSIS_TH.md และ SUMMARY.json สำหรับตัวเลขจริงตาม candidate ไม่รวมผลคนละรุ่นเป็น accuracy ของรุ่นเดียว

unit/fixture ผ่านไม่แทนสถานะจริงทุกช่องทุกวัน; เจ้าของเคยแจ้งว่าตรวจสถานะจริงแล้วถูกต้อง แต่ fixture รอบนี้เป็นหลักฐานแยกต่างหาก

## 11. ข้อจำกัดที่ยังต้องติดตาม

ไม่รับประกัน typo ใหม่ทุกแบบหรือ compound เกิน 3 ส่วน และยังไม่มี load test หลายคนของ r55; อายุข้อมูลราคา กฎ ปุ่ม และนโยบายที่ไม่มีข้อมูลต้องให้เจ้าของยืนยัน รายละเอียดคำถามเฉพาะอยู่ในรายงานท้ายรอบ
'''
save('FLOW_FINAL.md',flow)
qc=[]
for r in web:
    c=r['case'];z=r['job'].get('result') or {}
    qc.append(f"## {c['id']} · {c['locale']}\n\n**คำถาม:** {c['question']}\n\n**ผล:** {r['verdict']} / {r['elapsed_sec']:.3f}s / {z.get('mode')}\n\n**Checks:** {', '.join(r['checks'])}\n\n{z.get('answer','')}\n")
save('ALL_QUESTIONS_ANSWERS_TH.md','# คำถามและคำตอบ 156 เคส · candidate r55.6\n\nCHECKED คือผ่านเฉพาะเกณฑ์ที่แสดง ไม่ใช่ owner approval; REVIEW ไม่มี oracle เนื้อหาครบ\n\n'+'\n'.join(qc))
v=summary['web_candidate6'];n=summary['followups_candidate7'];k=summary['controls_candidate7']
report=f'''# ผลการแก้ r55 และข้อจำกัดที่เหลือ · 10 ตุลาคม 2026

## สถานะ

แก้โปรเจกต์จริงแล้ว เปิด candidate 2026.10.10-service-r55.7 ที่ http://127.0.0.1:8093/ ใช้ Python/โมเดลที่มีบนเครื่องนี้ ไม่ได้อัปเดตแพ็กเกจแบบแจกสองชนิดจากรอบเก่าโดยอัตโนมัติ

## ผลตรวจ แยกประเภทหลักฐาน

| หลักฐาน | ผล | ความหมาย |
|---|---|---|
| unit + fixture 8 modules บน source ล่าสุด | {units['tests']} tests, {units['failures']} failures, {units['errors']} errors | parser/slot/context/queue/timeout/calendar/known booking fixture; ไม่ใช่ทุก legacy test |
| ร้านเกม 156 HTTP requests บน r55.6 | {v['failures']} failed checks; {v['verdicts'].get('CHECKED',0)} CHECKED, {v['verdicts'].get('REVIEW',0)} REVIEW | transport ครบ; CHECKED ผ่านเฉพาะ owner-answer/contains/forbid/route ที่แต่ละเคสมี |
| follow-up / paraphrase / full-rule pages บน r55.7 | {n['requests']} requests, {n['checks']} checks, {n['failures']} failed checks | ตรวจสองรอบ 7 บทสนทนา + 16 คำใหม่ + pagination 2 ภาษา |
| controls และกฎที่ได้รับผลจากการแก้ล่าสุด r55.7 | {k['requests']} requests, {k['failures']} failed checks | ตรวจซ้ำส่วนเปลี่ยนจาก r55.6; ไม่เรียกว่า rerun 156 ทั้งชุดบน r55.7 |
| CS2 full sections | TH 56/56, EN 56/56 ไม่ซ้ำ | ความครบตาม rulebook ในระบบ ไม่ยืนยันกติกาปีอื่น/รายการใหม่ |
| owner hash | 38/38 ไม่เปลี่ยน | ข้อมูลเจ้าของคงเดิม; candidate app hash ตรง ROOT |

REVIEW 47 ข้อบางข้อถูกอ่านตรวจแล้วว่าเข้ากับ source เช่น unknown policy และ catalog แต่ยังไม่มี oracle เนื้อหาครบของทุกข้อ จึงไม่แปลงเป็น accuracy 100% จาก HTTP 200 หรือจากคำที่ตรงบางคำ

ผล unit เดิมที่ผิดยังอยู่ในไฟล์ loop* / final*: มีข้อผิดจริงเรื่อง VR ที่แก้แล้ว, environment tmpdir ของ runner ที่แก้แล้ว และ calendar assertion ที่แยก A/a/Thai/ thai การแก้ assertion รอบท้าย casefold ทั้ง expected และ actual รักษาข้อความเงื่อนไขนโยบายเดิม ไม่ลดเกณฑ์ข้อเท็จจริง

## ทำไมข้อมูลครบแต่เลือกตอบผิด และสิ่งที่แก้

| ลำดับ | สาเหตุที่พบ | การแก้ | สิ่งที่ควรตอบ / หลักฐาน |
|---|---|---|---|
| P0 | เลขเวลาถูกอ่านเป็นเลขเครื่อง; นาทีใน 9:00-9:30 ถูกอ่านเป็นช่วง 00-9 | boundary/unit guards และ parse date ก่อน time | VR 09–09:30 ตรวจ 09–10; fixture ครึ่งหลัง busy ต้องไม่บอกว่าว่าง |
| P0 | semantic handler ชนะก่อนตรวจข้อมูลเจ้าของ; subject ผิดสลิป/เปลี่ยนรอบ/รายชื่อไม่ครบไม่เข้า claim | bounded owner claims ก่อน generic retrieval; subject+operation+negation | ผิดสลิปส่งเพจ; เปลี่ยนรอบยกเลิกทางอีเมลแล้วจองใหม่; เช็กอินรายคน |
| P0 | typed plan ทำ customer group/คำระยะเวลา/จำนวนคนหาย | retain group, number words, people count | PC บุคคลทั่วไป 2h = 140 บาท; Nintendo 4 คนใช้ package 3–4 คน |
| P1 | server early price rewrite ลบส่วนเกม/คำถามอื่น | split operations ก่อน server price plan และก่อน early return | ต้องได้รายการเกม PC และราคาในคำตอบเดียว |
| P1 | คำตอบสั้น ทั้งหมด/PC ไม่ผูก pending task; PC2 ไม่เก็บเวลาเดิม | task memory/eligible context + scope/date/time ที่ยืนยัน | หลังถามราคาแล้วตอบ PC ต้องได้ราคา; PC2 ต้องคงวันที่/เวลาเดิม |
| P1 | Continue with the remaining rules ไม่ตรง grammar ทำ cursor ไม่เดิน | bounded continuation grammar + ACK IDs | TH/EN ต่อจนได้ครบ 56 ส่วนไม่ซ้ำ |
| P1 | งบถูกตีความเป็น price question; ราคา 0 เสี่ยงตีความเป็นไม่จำกัด | integer affordability จาก package เดิม + capacity/group/expiry caveats | 100 บาท PC adult ได้ 1h เหลือ 30; missing group ถามกลับ |
| P1 | คำถามเกม/permission/identity/hours/control ใกล้กันถูกเลือกคนละหมวด | scoped catalog/hours/control/spec adapters และ pending installation guard | ขอ install Minecraft ต้องไม่ตอบว่าเกมมี/ไม่มีแทนสิทธิ์ติดตั้ง |
| P1 | broad กฎแข่ง ROV ล่ะ ถูกตอบ clause 4.1.1 ข้อเดียว | เติม discourse particle ใน broad-rule grammar; ปี/facet เฉพาะยังอยู่; เพิ่ม overview oracle | ตอบภาพรวมหลายหัวข้อ RoV พร้อมชื่อรายการ/source ไม่ใช่ clause เดียว |
| P2 | control preflight ใช้ session alias registry ที่หา CS2 ไม่เจอ และนับ Tekken variants เป็น 2 เกม | ใช้ existing control catalog resolver เฉพาะเกมเดียว; guards หลายเกม | คำถามปุ่มตรง source ลดการเรียก LLM; warning แหล่งรองยังอยู่ |
| P2 | ข้อความแถว Tekken มีคำอาหรับปน | cleanup ตอน render เฉพาะแถวที่รู้ provenance; raw source ไม่เปลี่ยน | ข้อความไทยอ่านได้; ไม่อ้างตรวจ controller จริงแล้ว |
| P2 | timeout สูญเสีย trace ตอน worker replacement | bounded partial progress แนบ timeout response/log ก่อนเปลี่ยน worker | รู้ขั้นตอนล่าสุด แต่ cause_confirmed=false จนพิสูจน์สาเหตุ |

คะแนน routing/candidate confidence เป็น heuristic ไม่ใช่ค่าความถูกต้องของคำตอบ การเลือก game target ถูกยังไม่พิสูจน์ว่า facet/coverage/ปีถูกทั้งหมด

## Loop และการปรับเกณฑ์จากผลจริง

1. web_loop1: 156 requests พบ failed checks 5 ข้อ (เปลี่ยนรอบ, Steam policy, catalog continuation timeout, multi-clause TH/EN)
2. web_loop2: 34 requests พบ 1 timeout ของคำถามนับเกม; partial trace ยืนยันขั้นตอนล่าสุด แต่ไม่พิสูจน์ root cause เดียว
3. near_loop3: full-rule TH/EN ครบแล้ว แต่พบ 3 checks ผิดจากราคา group-only, เกม+กี่บาท, install ชื่อเกมโดยไม่มีคำว่า game
4. web_final / near_final: แก้ 3 จุดจนผ่าน checks เดิม อ่านคำตอบเพิ่มแล้วพบ c124 ยังตอบไม่ครบ แม้ชื่อเกมตรง
5. web_final6: เพิ่ม broad_rules_need_overview แล้วผ่านทั้ง 156; กฎ ROV ล่ะจากประมาณ 14s เหลือประมาณ 0.9s
6. controls_final7 / near_final7 + units_final8: แก้ตัวค้นชื่อเกมใน control preflight และตรวจ subset ที่ได้รับผล พร้อม 92 unit/fixture tests

ทุก raw result คงชื่อเดิมไว้ ไม่มีการ rescore ไฟล์เก่าให้ดูเหมือนระบบรันใหม่

controls_semantic_audit.json รอบแรกกำหนด heading “ข้อห้าม” ให้ภาพรวม RoV โดยไม่มีเหตุผลจาก formatter จึงเกิด false failure เพิ่ม รอบ v2 ตรวจ format/equipment/pause/penalty และ metadata หลาย source sections แทน เก็บผลรอบแรกไว้ ชี้แจง oracle_revision และไม่เรียก offline audit ว่ารัน pipeline ใหม่

## เวลาในเครื่องนี้

- 156 เคส sequential r55.6: median {v['latency']['median']}s, P95 {v['latency']['p95']}s, max {v['latency']['max']}s
- subset ปุ่ม/กฎ r55.7: median {k['latency']['median']}s, max {k['latency']['max']}s
- followups/pages r55.7: median {n['latency']['median']}s, P95 {n['latency']['p95']}s, max {n['latency']['max']}s

เป็นเวลาบนเครื่องนี้หลัง warmup แบบ sequential และ query set เฉพาะ ไม่ใช่ SLA หรือผลใช้พร้อมกันหลายคน กฎที่ต้อง retrieval/LLM จริงและ WordPress network ยังมี latency เปลี่ยนตามภาระ

## สิ่งที่ยังยืนยันเองไม่ได้ และคำถามที่ต้องถามเจ้าของ

1. **ราคา non-PC:** ตารางเดิมมีผลถึง 31 มีนาคม 2026 อัตราปัจจุบันเหมือนเดิมหรือไม่? มีผลเริ่ม/สิ้นสุดเมื่อใด และอนุมัติข้อความราคาใด?
2. **เปลี่ยนวันเมื่อจ่ายแล้ว:** ข้อ 45 อนุญาตเปลี่ยนวันเมื่อจองผิดวัน แต่ข้อ 46 ไม่อนุญาตเลื่อนแทนคืนเงิน แยกสองกรณีอย่างไร? ติดต่อช่องทางใด ต้องแจ้งล่วงหน้ากี่ชั่วโมง?
3. **เงินสด/ค่าจอดรถ/คนดู:** รับเงินสดหรือไม่? ที่จอดรถและนั่งดูเพื่อนมีค่าใช้จ่ายหรือไม่? เงื่อนไขเป็นอย่างไร?
4. **บัญชีเกม/ติดตั้ง:** ต้องใช้ Steam/บัญชีส่วนตัวหรือมีบัญชีศูนย์? ขอเพิ่มเกม/ติดตั้งเอง/mod/โปรแกรมได้ไหม ใครเป็นผู้ทำ?
5. **เด็ก/อุปกรณ์ส่วนตัว/สตรีม:** อายุขั้นต่ำและผู้ปกครอง? จอยส่วนตัว/กล้อง/การสตรีมและถ่ายภาพอนุญาตในกรณีใด? (keyboard/mouse มีคำตอบว่าไม่อนุญาตแล้ว ไม่ถามซ้ำ)
6. **เวลาเสียไป/สาย:** เกมอัปเดตหรือเครื่องค้างเริ่มนับเวลาเมื่อใด ชดเชยอย่างไร? มี grace period หรือข้อยกเว้นสาย 15 นาทีจากกฎเดิมหรือไม่?
7. **เช่าเหมา:** ครึ่งวัน/เต็มวันเป็นกี่ชั่วโมง เริ่ม/จบเวลาใด? ใช้วิธีจอง/ชำระเงินเดียวกับรายเครื่องหรือไม่? ราคาใน workbook มี validity เมื่อใด?
8. **กฎและปุ่ม:** เอกสาร rulebook ที่ใช้เป็นฉบับที่จะให้ตอบในการแข่งขันครั้งถัดไปหรือไม่? ข้อยกเว้น pause ของ Tekken ใช้อย่างไร? ปุ่มแหล่งรองตรงกับเกม/เครื่องที่ศูนย์ตั้งค่าจริงไหม?

ระบบตอบส่วนที่มีหลักฐานก่อน และระบุเฉพาะ field ที่ยังไม่ยืนยัน ไม่สร้างนโยบายจากการอนุมาน คำถาม owner pending ไม่ได้ขัดขวางการใช้ส่วนที่แก้แล้ว

## งานเทคนิคที่ยังติดตามได้โดยไม่ต้องให้เจ้าของตอบ

- ขยาย semantic oracles ของ REVIEW 47 ข้อจาก source ไม่ใช้ชื่อเกม/เลขเพียงอย่างเดียว; r55 เพิ่ม regression สำคัญแล้ว แต่ชุดนี้ยังไม่ได้พิสูจน์ทุก wording
- คำถามหลายส่วนเกิน 3 ส่วนและการปฏิเสธ/เปรียบเทียบซับซ้อนยังไม่ได้ตรวจครบ ไม่ควรแก้ grammar กว้างจากตัวอย่างเดียว
- ตรวจใหม่เมื่อเปลี่ยน corpus/models/worker policy; รอบนี้ไม่ได้เพิ่ม model concurrency หรือทำ load test r55
- อัปเดต portable packages สองชนิดด้วย version/hash ใหม่เมื่อจะนำแจก; candidate นี้อาศัย runtime/model ที่มีในเครื่อง จึงไม่ใช่แพ็กเกจแจกใหม่
- Git checkout ยังขึ้น fatal ที่ path Learn-LLM; เก็บ snapshot/diff แล้ว ไม่ reset/clean หรือซ่อม metadata ของ Git โดยเดา

## ไฟล์หลักฐาน

FLOW_FINAL.md, SUMMARY.json, ALL_QUESTIONS_ANSWERS_TH.md, web_final6.json/raw.jsonl, controls_final7.json/raw.jsonl, near_final7.json/raw.jsonl, units_final8.txt/json, final7_PRESERVATION_AUDIT.json, final7_SOURCE_CHANGES.patch และ HANDOFF_R55.md
'''
save('RESULTS_ANALYSIS_TH.md',report)
handoff=f'''# Handoff r55 · 2026-10-10

อ่าน FLOW_FINAL.md และ RESULTS_ANALYSIS_TH.md ทั้งหมดก่อนแก้ต่อ

- ROOT: {ROOT}
- Artifact folder: {OUT}
- Active candidate: {OUT/'candidate_7/PSU_Esports_Chatbot_Local'}
- Runtime: 2026.10.10-service-r55.7, http://127.0.0.1:8093/
- Launcher: Open-PSU-Esports-Chatbot.ps1 (background process identity ถูกตรวจ; อย่าปิด user Ollama/Dashboard/8091)
- Python: C:\\Users\\Chokhun\\Documents\\Codex\\PSU Esports Chatbot Ready 20261003\\runtime\\python\\python.exe
- เก็บ source backup/diff แล้ว Git ยังใช้ไม่ได้; ห้าม reset/clean, owner data 38 hash unchanged
- สิทธิ์ ROOT ของรอบนี้เป็น turn scope ขอผ่านระบบอีกครั้งถ้ารอบถัดไปไม่มีสิทธิ์เขียน
- Final units 92/92; full web 156 บน r55.6 (109 checked/47 review); latest r55.7 controls subset+44 followup/page requests ตาม SUMMARY.json
- หน้าตา API /api/chat/jobs ต้อง poll และ ACK last_seen_response_id สำหรับ context/cursor; /health แสดง version
- ไม่รัน full 20k ไม่ทำ concurrent load test รอบนี้ ไม่แก้ owner source/policy/Gold เพื่อให้คะแนนผ่าน
- จุดแก้ทั้งหมดและ unknown owner questions อยู่ในรายงาน อย่าเรียก safe unknown หรือ live without oracle ว่าตอบผิด/ถูกจริงทุกช่อง
- root module ใหม่ app/pipeline/service_query_completion.py และ tests/test_service_repairs_r55.py; 13 existing app files และ calendar casefold assertion มี diff
- English owner translations/test pass ไม่เท่ากับ human approval ทุกคำแปล; current tournament/controller/source validity ต้องยืนยันตามรายงาน
- Portable old packages ยังไม่อัปเดตจาก r55; user can try local candidate 8093

Scripts ใน BASE: r55_units.py, r55_web_tests.py, r55_followup_pages.py, r55_candidate.py, r55_swap.ps1, r55_audit.py, r55_finish.py
อย่ารัน refine*.py ซ้ำ (ใช้แก้ตาม marker เก่า) และอย่าใช้ label/output/candidate ID เดิม เพราะผลเดิมต้องคงอยู่
'''
save('HANDOFF_R55.md',handoff)
print(json.dumps(summary,ensure_ascii=False,indent=2))
