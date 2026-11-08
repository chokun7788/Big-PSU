# ผลข้อ2ละเอียดและทดสอบ10%ทุกหมวด — R131

งานวินิจฉัยและชุดทดสอบที่ผู้ใช้สั่งเสร็จแล้ว **2,111 unique request keys / 5,584 grade identities** ครบทุกตัว ไม่มีขาดหรือซ้ำ ใช้คำถามเดิมจาก Full ทั้ง14หมวด ปัดขึ้น10%ราย stratum และเติมตามหมวดของ input โดยเลือกก่อนรันและไม่ใช้ผลคะแนนเลือกคำถาม

**คำตอบทั้ง2,111ข้อเหมือน saved R130 เดิมทุกข้อ** รอบนี้ไม่มีการแก้ runtime หรือฝึกโมเดลใหม่ จึงเป็นหลักฐานการเกิดซ้ำของปัญหา ไม่ใช่ผลคุณภาพดีขึ้นหลังแก้ Flow

วินิจฉัยก่อนเริ่มทดสอบ: อ่านกลไกจาก raw เดิมครบ20,554คำถาม/55,811เกณฑ์ และตรวจ source/trace รายกรณี72ข้อก่อนเปิด gate ระหว่างรอผลตรวจเพิ่มรวม167 unique keys ที่อ่าน source รายกรณีหรือทดลอง reader เฉพาะในหน่วยความจำ ยืนยันตัวอย่างผิดเรื่อง/ผิดขอบเขต/ตอบขาด117 keys ตัวอย่างนี้เลือกเพื่อวินิจฉัย จึงไม่ใช้คำนวณ accuracy หรือแทนจำนวนผิดทั้งหมด อีก20,387 keys ยังไม่ตัดสิน semantic รายข้อ

ใน sample มี16keys ตรงกับทะเบียนตรวจ source และคำตอบเกิดซ้ำครบ16keys รวมตัวอย่างปัญหาที่เคยยืนยัน13keys ดู[ALL_REVIEWED_CASE_REPRODUCTION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/ALL_REVIEWED_CASE_REPRODUCTION.json)

## คะแนนตามภาษาที่ร้องขอ

Strict รวมข้อกำหนด route/intent/mode/source/ข้อความ/เวลา ตาม grader เดิม Positive literal ตรวจเพียงข้อกำหนดข้อความด้านบวกที่มีอยู่ ทั้งสองค่า **ไม่ใช่ semantic accuracy** ตารางใช้ denominator เดียวกันในแต่ละภาษา; unassessed ของ baseline เก็บอยู่ใน denominator ไม่ตัดทิ้ง

| ผลที่บันทึก/รันใหม่ | ภาษา | Strict ผ่าน/ทั้งหมด | Positive literal ผ่าน/eligible | Literal% | Unassessed |
|---|---|---:|---:|---:|---:|
| R64_saved | th | 1809/2492 (72.59%) | 1274/1315 | 96.88% | 3 |
| R64_saved | en | 2252/2728 (82.55%) | 951/994 | 95.67% | 0 |
| R64_saved | auto | 236/364 (64.84%) | 200/247 | 80.97% | 13 |
| R95_saved | th | 225/2492 (9.03%) | 998/1315 | 75.89% | 0 |
| R95_saved | en | 287/2728 (10.52%) | 696/994 | 70.02% | 0 |
| R95_saved | auto | 51/364 (14.01%) | 177/247 | 71.66% | 0 |
| R130_saved | th | 24/2492 (0.96%) | 1041/1315 | 79.16% | 0 |
| R130_saved | en | 92/2728 (3.37%) | 752/994 | 75.65% | 0 |
| R130_saved | auto | 47/364 (12.91%) | 165/247 | 66.80% | 0 |
| R130_repeat_10pct | th | 23/2492 (0.92%) | 1041/1315 | 79.16% | 0 |
| R130_repeat_10pct | en | 95/2728 (3.48%) | 752/994 | 75.65% | 0 |
| R130_repeat_10pct | auto | 46/364 (12.64%) | 165/247 | 66.80% | 0 |

Strict ของ repeat ต่างจาก saved R130 จำนวน9 grade identities: 5เปลี่ยนเป็นผ่านและ4เปลี่ยนเป็นไม่ผ่าน ทุกข้อแตกต่างเพียง latency_ceiling และคำตอบเหมือนเดิม จึงไม่อ้าง semantic ดีขึ้น/แย่ลงจากความต่างคะแนนนี้ ดู[STRICT_ONLY_CHANGES_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/STRICT_ONLY_CHANGES_REVIEW.json)

## ทุกหมวดตาม input

หมวดเป็น metadata เพื่อเลือกและรายงาน coverage ไม่ใช่คำตัดสินว่า planner ตี intent ถูก คำถามเดียวอยู่หลายหมวดได้ จึงบวกจำนวนแต่ละแถวเป็น unique total ไม่ได้

| หมวด | ประชากรเดิม | เลือก/รันครบ | Strict% | Positive literal ผ่าน/eligible | Literal% |
|---|---:|---:|---:|---:|---:|
| C00 ทั่วไป/กำกวม/นอกขอบเขต | 1048 | 111 | 39.31% | 32/59 | 54.24% |
| C01 ศูนย์/ติดต่อ | 1266 | 135 | 13.25% | 145/155 | 93.55% |
| C02 บุคลากร | 796 | 81 | 8.00% | 145/153 | 94.77% |
| C03 อุปกรณ์ | 1568 | 172 | 3.34% | 175/316 | 55.38% |
| C04 เกม | 4617 | 475 | 0.93% | 632/724 | 87.29% |
| C05 การควบคุม | 2228 | 223 | 0.59% | 498/548 | 90.88% |
| C06 ราคาปกติ | 1880 | 197 | 0.95% | 196/278 | 70.50% |
| C07 เหมา | 6 | 1 | 0.00% | 0/1 | 0.00% |
| C08 จอง | 3969 | 414 | 0.77% | 293/422 | 69.43% |
| C09 ชำระเงิน | 92 | 10 | 0.00% | 24/24 | 100.00% |
| C10 กฎศูนย์ | 1546 | 166 | 3.34% | 126/167 | 75.45% |
| C11 ตาราง | 2346 | 246 | 0.00% | 91/177 | 51.41% |
| C12 สถานะจริง | 1106 | 113 | 0.00% | 20/38 | 52.63% |
| C13 แข่งขัน | 4508 | 452 | 1.29% | 3/90 | 3.33% |
| C14 ข่าว/กิจกรรม | 63 | 11 | 5.88% | 0/14 | 0.00% |

**ข้อจำกัดหมวด:** C07 มีประชากรเดิม6คำถาม เลือก1 ส่วนใหญ่เป็น offsite จึงยังไม่ครอบคลุม rental onsite ทุก operation; C14 ไม่มี source ข่าวจริง และผล literal100% ของหมวดเล็ก เช่น C09 ไม่ยืนยัน semantic ถูก100%

## การยืนยันการรันและกลไก

- ตรวจ frozen files2,371ไฟล์และ logical source digest ก่อน/หลังผ่าน รวม source/input/code/prompt/weights ข้อมูลต้นฉบับและ approvals ไม่เปลี่ยน
- ตรวจ returned provenance ของ model calls ที่สำเร็จ30ครั้ง: retained24/base6 ไม่มี profile/adapter/base revision/messages/schema/stage/precision/model mismatch
- Actual base: typhoon-ai/typhoon2.5-qwen3-4b; alias psu-r129:latest; HF NF4 double quant BF16; context ใช้ retained R121 adapter ส่วน selector/generic ใช้ base ไม่ promote new adapter ที่ไม่ผ่าน critical review
- Model HTTP attempts54 / transport successes30 / ไม่สำเร็จ24 events จำนวน requests ไม่เท่าจำนวน events และ HTTPสำเร็จไม่ได้แปลว่าคำตอบถูก
- พบ admission denial926 requests, schema/version rejection25 requests และ gateway transport failure22 requests เป็นจำนวนกลไกที่เกิดซ้ำ กลุ่มซ้อนทับและบางข้อถูก typed reader กู้ได้ จึงไม่รวมเป็น semantic failures
- Median0.639s / P953.614s / P9946.360s / max150.723s; 37requests เกิน20s

Live ใช้ controlled unavailable fixture จึงไม่ใช่คำยืนยันสถานะ provider จริง การเทียบ saved R64/R95 มี source/backend/precision/clock/deadline confounds ไม่มี baseline inference/regrading ใหม่ และไม่อ้าง causal Flow effect ระหว่าง sample มี offline forensic work ร่วมบางช่วง จึงไม่อ้าง performance effect แบบควบคุมจากเวลาต่างกัน

## สาเหตุและลำดับแก้

ต้นเหตุที่ยืนยันได้รวมการผูก entity ไทยผิด, event scope หาย, verifier ปฏิเสธ clause ที่มีสาระเพราะข้อความเท่ากับ heading, reader ตอบชื่อเอกสารแทนรูปแบบแข่งขัน และ need บางส่วนหาย ปัญหาเหล่านี้หลายข้อเกิดก่อนเรียกโมเดลหรือที่ reader/verifier จึงยังไม่มีเหตุผลให้ฝึก weights เพิ่มแทนการแก้จุดเหล่านี้

- [ทะเบียน15ต้นเหตุ พร้อมผลกระทบและเกณฑ์แก้](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/ITEM02_FINAL_REGISTER_TH.md)
- [รายงานข้อ2ละเอียดที่เสร็จก่อนเริ่มเทส](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/ITEM02_DETAILED_DIAGNOSIS_TH.md)
- [หลักฐานรายกรณี167keys พร้อม source/trace/คำตัดสิน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/CONSOLIDATED_SOURCE_REVIEW.json)
- [ลำดับแก้และเกณฑ์ตรวจรับ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/REPAIR_ACCEPTANCE_PLAN_TH.md)

## สิ่งที่ยังไม่ปิด

งานข้อ2และsampleเสร็จ แต่ยังไม่มี runtime fixes และยังไม่ปิด semantic acceptance ของ Flow ทั้ง76requirements/14หมวด คงข้อที่ยังตัดสินไม่ได้เป็น review_required ห้ามอ่านคะแนน literal เป็นความถูกต้องทางความหมาย Candidateยังไม่ติดตั้งทับR78

## หลักฐานการตรวจรับรอบนี้

- [DIAGNOSIS_PRETEST_COMPLETE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/DIAGNOSIS_PRETEST_COMPLETE.json)
- [SELECTION_FREEZE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/SELECTION_FREEZE.json)
- [EXECUTION_COMPLETE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/EXECUTION_COMPLETE.json)
- [COVERAGE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/COVERAGE.json)
- [SCORES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/SCORES.json)
- [MODEL_AND_MECHANISM_AUDIT.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/MODEL_AND_MECHANISM_AUDIT.json)
- [CHANGED_ANSWER_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/CHANGED_ANSWER_REVIEW.json)
- [REQUIREMENTS_SCOPE_PRESERVATION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/REQUIREMENTS_SCOPE_PRESERVATION.json)
- [REQUEST_COMPLETION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r131_diagnostic_review_20261025/REQUEST_COMPLETION.json)
