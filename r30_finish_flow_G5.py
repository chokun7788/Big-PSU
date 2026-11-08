import json
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());f=p/'docs/130_full_improvement_r30_flow_20261002.md'
assert (r/'final_G5_all_summary.json').exists()
with (r/'flow_before_final_G5.md').open('xb') as out:out.write(f.read_bytes())
s=f.read_text(encoding='utf-8').replace('ฉบับทบทวน 3','ฉบับทบทวน 4 ฉบับสมบูรณ์ของรอบนี้').replace('2026.10.02-full-improvement-r30-G2','2026.10.02-full-improvement-r30-G5')
s=s.replace('| P2 | EN fallback','| P1 | ชื่อเกมมี The/of/It จนคำถามไทยถูกนับเป็น EN | แยกชื่อหลายคำ/ชื่อย่อยของเกมใน catalog ออกจากหลักฐานภาษาเฉพาะ mixed input โดยไม่แก้ข้อความ | คำถามไทยใช้ TH; ประโยค EN จริงและ toggle ยังใช้ EN; detected ยังคง mixed |\n| P1 | คำถามเวอร์ชัน/แก้ client/เพิ่มรายชื่อ/สกิน/จำนวนรอบไม่เข้า detail หรือชนคำนาม | ผูก proposition กับเกมและข้อ literal; roster action แยกจากหัวข้อ roster; protest-language รองรับลำดับคำสองทิศ | ไม่ตอบ catalog/เสียงดัง/ปุ่มแทนกฎ; คำถามรวมต้องครบ eligibility, count, registration |\n| P1 | PC1 และ available ทำให้ policy กับ occupancy ปนกัน | ตรวจเลขเครื่องและสถานะ; available for booking days/time periods ที่ไม่ระบุเครื่องหรือเวลาจริงเป็น weekly policy | PC1/status ใช้สด; weekly policy ไม่อ้างเครื่องว่าง; วันปิดพิเศษยังมีผลก่อน |\n| P2 | EN fallback')
s=s.replace('C[ผูกภาษา ใช้ทิศทางแป้นเฉพาะเมื่อจำแนก mismatch แล้ว]','C[ผูกภาษา ใช้เฉพาะ mismatch ที่จำแนก แยกชื่อเกมจากหลักฐานภาษา]')
s=s.replace('G[ตรวจคำถามหลายประเด็นและบริบท]','G[ตรวจประเด็น บริบท และแยกนโยบายประจำสัปดาห์จากสถานะเครื่อง]')
s=s.replace('ข้อจำกัดของ Flow ปัจจุบัน: การจับประเด็น implicit และการรักษาเกมหลัง splitter ยังไม่ครบทุกประโยค รายละเอียดในข้อ 5; validator บางเส้นทางยังตรวจ route/source มากกว่าเนื้อหาทุก proposition ไม่กล่าวว่าการต่อกล่องในภาพพิสูจน์ครบแล้ว','ข้อจำกัด: ประโยค implicit ที่ไม่ได้อยู่ใน concept vocabulary ยังอาจหลุดไป fallback; ไม่รับรองว่าจับทุกประโยคได้ การจับ roster/action และ protest-language ที่พบในรอบนี้แก้และมี regression tests แล้ว validator เส้นทางทั่วไปยังไม่ได้พิสูจน์ทุก proposition; รายละเอียดงานต่อในข้อ 5')
s=s.replace('snapshot เพิ่มก่อน D/E/F/G/G2','snapshot เพิ่มก่อน D/E/F/G/G2/G3/G4/G4b/G4c/G5/G5b')
s=s.replace('G 37 → G2 43 การนับนี้เป็นรอบทดสอบจริง ไม่แต่งจำนวน loop','G 37 (รวม assertion body/bodies ผิด 3 ข้อ) → G2/G3/G4 43 ตาม fixture v2; source contracts ใหม่ G3 15/27 → G4 27/27 และ G5 เพิ่ม regression/guard controls เป็น 39 ข้อ การนับเป็นรอบที่รันจริง ไม่แต่งจำนวน loop')
s=s.replace('ทุกโมดูล 411 ข้อ','ทุกโมดูล 424 ข้อ')
s=s.replace('รุ่น G2 ใช้ locale binding','รุ่น G2/G3/G4/G5 ใช้ locale binding')
s=s.replace('79 + 43 + 280 + 320 + 128 = 850 เคส','79 + 43 + 8 + 39 + 280 + 320 + 128 = 897 เคส (8 ข้อตรวจภาษา; ส่วน live-required ตรวจ path ไม่ใช่ occupancy)')
s=s.replace('พบ splitter หลุด target ในชุดเก่า บันทึกเป็นปัญหาจริงที่ยังต้องแก้','พบ action/count, scope และลำดับ protest-language ชนกัน แก้ข้อที่ยืนยันและเพิ่มการตรวจคำถามรวม; ความครบทุก proposition ทั่วไปยังเป็นงานต่อ')
s=s.replace('candidate คะแนนต่ำมีผลผิด จึงเพิ่ม classified direction gate','candidate คะแนนต่ำมีผลผิด จึงเพิ่ม classified direction gate และแยก source game titles จากหลักฐานภาษา')
start=s.index('### P1-A:');end=s.index('### P1-B:',start)
s=s[:start]+'''### P1-A: การจับประเด็น/เป้าหมาย — สิ่งที่แก้และงานที่ยังเหลือ

ข้อผิดสี่ตัวอย่างที่ revision 3 เก็บไว้ตรวจข้อกฎต้นฉบับและแก้ใน G4 แล้ว:

| คำถาม | สาเหตุเดิม | คำตอบที่ต้องมีตาม source | การแก้และขอบ |
|---|---|---|---|
| CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม | ส่วนที่สองไม่เข้ากฎและแตกไปกฎเสียงดัง | Steam/latest CS2 และห้ามดัดแปลงที่ไม่ได้รับอนุญาต | version/client proposition ผูกเกมเดียว; ไม่ตีความเป็นห้ามทุก modification |
| CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ | roster noun เลือก count แทน action หลังปิดรับ | ไม่อนุญาตลงทะเบียนผู้เล่นหลังปิดรับสมัคร | ขยาย closed-registration ลำดับคำ; count ต้องมี size/composition หรือหัวข้อ roster ที่แยกจริง |
| RoV ใช้สกินพิเศษได้หรือเปล่า | implicit permission ไม่เข้า detail | 4.2.5 ใช้ Default เท่านั้น | target-bound skin permission; คำถาม catalog สกินยังไม่เหมารวมเป็นกฎ |
| เทคเคนแต่ละเกมแข่งกี่รอบ | ชื่อ franchise/round-count หลุดไปหัวข้อกว้าง | จำนวนรอบต่อเกม 3 ของเอกสาร Tekken 8 | infer เฉพาะ franchise ที่มี registered edition เดียวและไม่มีรุ่นอื่นระบุ พร้อม qualifier ว่าเอกสาร Tekken 8 ที่มี |

G4 full tests ทำให้พบ regression จริงสองข้อ จึงแก้ G5:

- `eligibility, roster, and registration` ต้องมีทั้งสามประเด็น: รักษา roster ที่เป็นหัวข้อคั่นด้วย comma และ count ขณะที่ after-closed action ไม่ถูกเพิ่ม count แทนคำตอบ
- `Which days and time periods are available for PC booking?` เป็น weekly policy; available ในวลีนี้ไม่ใช่ยืนยันเครื่องว่าง แต่ `Which PC1 booking slots are available...` ต้องดึงสด

ชุด legacy เพิ่มทำให้พบอีกสองข้อและแก้ G5:

- `รายการ CS2 ใช้เวอร์ชันเกมแบบไหน`: context gate เดิมไม่เห็น tournament; preprocess เพิ่ม Call of Duty: Warzone แล้ว target lock คะแนน 1.0 ทั้งที่ชื่อไม่ได้อยู่ใน raw คำถาม เพิ่ม event/version context ที่ผูก CS2 ให้กฎมีผลก่อน catalog lock ยังต้องตรวจการขยายชื่อในเส้นทางอื่นต่อ
- `CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย`: route จับกฎได้ แต่ language concept จับเฉพาะ “ภาษา...ประท้วง”; เมื่อไม่พบ detail ไปชน “บังคับ” ของเกม เพิ่ม concept ตามลำดับคำสองทิศและผูก source ภาษาทางการ ไม่สร้างกฎภาษาใหม่

Flow ต่อสำหรับประโยคที่ยังไม่ครอบคลุม: raw + trace → รักษา target/date/เลข/ปฏิเสธ → แยก requested propositions → clause ledger ที่มี source hash + scope + condition/result → ถ้าขาดประเด็นให้ partial/clarification → ตรวจ target, first line, missing clauses และ forbidden claims → clean/noisy same oracle → full regression ที่เกี่ยวข้อง ไม่มี whole-question alias เป็นทางหลัก

''' +s[end:]
start=s.index('### P1-C:');end=s.index('### P2:',start)
s=s[:start]+'''### P1-C: Schedule policy กับ live status — แก้ขอบที่ยืนยันแล้ว

G4 แก้คำถาม Maintenance ทั่วไปให้ใช้ตารางเดิมแม้ dependency unavailable และตรวจ numbered resources; G5 แก้ available for generic booking days/time periods ที่ถูกกันผิด การถามเครื่องว่างหรือวัน/เวลาจริงยังเป็น live path สถานะเชื่อมได้และคำตอบ booked/free ต้องรายงานแยกกัน

Flow ต่อ: classify policy / resource-status / date override → generic policy ให้ regular slots + special-closure disclaimer → actual slot fetch WordPress read-only → source freshness/วัน/เครื่อง/ช่วง → overlap ตาม fixture (VR 30 นาทีครองชั่วโมง) → response ตอบเฉพาะสถานะที่ข้อมูลรองรับ → API transport มีหลักฐาน fetch แต่ occupancy ต้องมี oracle อีกขั้น ไม่เปลี่ยนตารางหรือข้อมูลเจ้าของ

''' +s[end:]
s+='''
## 7. Flow วิเคราะห์ข้อไม่ผ่านทุกชุดและการใช้คะแนน

1. เก็บ original result/grade ก่อนเสมอ ทุก unique input เชื่อมกลับ raw line, source IDs, route, candidate scores, validation และ trace ได้
2. เทียบ expected กับ source ปัจจุบัน: keyword รูปแบบเก่า เช่น `3 รอบ` เทียบ literal `จำนวนรอบต่อเกม (Round): 3` ไม่ใช่หลักฐานว่าเลขผิด; ห้ามลบ fail รวมทั้งหมวด
3. จำแนก: confirmed wrong target/action/content; incomplete propositions; source missing/conflict; old mode/heading/keyword; grader implementation; locale/proper names; controlled dependency; loaded latency; observation without oracle
4. route .97, resolver 1.0, capability .999 เป็นคะแนนเลือกตามเงื่อนไขและข้อความที่ขั้นก่อนส่งมา ไม่ใช่ความน่าจะเป็นว่าคำตอบจริงถูก ตัวอย่าง false appended title แสดงว่าคะแนนสูงยังเลือกผิดได้
5. “ต้องมีเนื้อหา” หมายถึงคำถามสามเรื่องต้องมีข้ออ้างที่รองรับครบสามเรื่อง เช่น eligibility + 5 players + no late registration การมี source CS2 หรือคำว่า registration เพียงอย่างเดียวไม่ทำให้คำตอบครบ
6. จัดปัญหาที่พิสูจน์จาก trace/source ก่อน → เพิ่ม content/negative contract → แก้ operation/target/qualifier ตามสาเหตุ → focused → full corpus → actual API → วัด loaded/idle แยก → source preservation → release → replay
7. ถ้า test เก่าล้ม ให้เก็บคะแนนเก่าและเพิ่ม diagnostic/source overlay แยก พร้อม scope; human_review/English reference ที่ยังไม่มี oracle เป็น observations และ pending approval

## 8. หลักฐานและความเสี่ยงที่ยังเหลือ

- Complete root sweeps F/G2/G3/G4/G5 เก็บแยก; A/B ที่หยุดกลางคันไม่นับครบ; 20,327 unique requests กับ 55,583 grades มี historical/split/alias จึงไม่บวกเป็น answer accuracy เดียว
- Extra corpus 970 unique requests, 981 grades; by-game subsets ตรวจ alias; 120 human-review observations ไม่มีคำเฉลยคนและไม่นับ correct answers
- Strong competition composition/content/new-question 728 cases ตรวจ clause/source/first line ครบตาม oracle ที่เขียน ไม่ใช่ผู้จัดรับรองทุกกฎปัจจุบัน
- Guard runtime G2/G3 ได้ 498/500 policy actions; สองเคส mixed wrong layout ควรขอพิมพ์ใหม่ตาม oracle G5 เพิ่มการตรวจร่วม: accidental repeat ที่มีหลักฐาน candidate_seen/gain จาก corpus และอยู่นอก source game title exact → ประเมิน layout ใน residual หลังนำชื่อออกจากหลักฐาน → คะแนนอย่างน้อย max(.65, configured threshold) จึงขอพิมพ์ใหม่ ไม่ส่งข้อความที่แก้ไปตอบ ไม่เปลี่ยน global thresholds ตรวจ runtime 500 ซ้ำและมี negative controls ประโยคอังกฤษ/ไทย/ชื่อเกมเลขโรมัน ผลล่าสุดอยู่ final_G5_runtime_guard500_summary.json ไม่ใช่ answer accuracy หรือ independent holdout
- คู่ clean/noisy 2,000 ใช้ V2 content overlay และเก็บ Gold เดิม มี noisy regression ที่ต้องแยก target/recovery/abstention/contract ตาม trace ไม่ปรับ threshold จาก pass rate อย่างเดียว
- Worker หนึ่งตัว queue wait 3 วินาทีอาจได้ 503 ใน loaded concurrency; ต้องเปิดผล idle แยกพร้อม error body ไม่กล่าวว่าทุก 503 เกิดจาก WordPress หรือภาษา
- ไม่มี source ใหม่ที่ผู้จัดรับรอง ไม่มี real booked/free oracle ตามคำขอพักเก็บข้อมูล ไม่กรอกนโยบายแทนเจ้าของ

Static sweep 20,327 ใช้ binding ภาษาแบบ server แต่เรียก pipeline โดยตรง การ short-circuit ของ runtime guard ตรวจใน runtime500/กรณี guard และ API จริงแยก ไม่เรียก static sweep ว่าการทดสอบ HTTP ครบ 20,327 คำถาม

ผลจำนวนสุดท้ายดู `FINAL_RESULTS_TH.md`, `FINAL_G5_DETAILED_CAUSE_ANALYSIS_TH.md`, `FINAL_G5_FULL_ANALYSIS_SUMMARY.json` และ `release_preflight_G5.json` ใน reports/r30_full_improvement_20261002_020311_6374c0
'''
f.write_text(s,encoding='utf-8',newline='\n')
with (r/'flow_final_G5.md').open('x',encoding='utf-8') as out:out.write(s)
assert all(v in s for v in ['P1-A','P1-B','P1-C','424','897','เจ้าของ','proposition'])
print(str(f))
