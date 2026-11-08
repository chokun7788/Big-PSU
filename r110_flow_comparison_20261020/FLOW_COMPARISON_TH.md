# เปรียบเทียบ Flow ที่มีจากผลเก็บไว้

จัดทำ 2026-10-20T23:44:13.261716+07:00 — อ่านผลเดิมเท่านั้น ไม่รันแชท ไม่เรียก LLM ไม่เปลี่ยน source หรือผลทดสอบเดิม

## 1. คำตอบสั้น

- Flow เดิม Legacy มีคะแนน positive literal checkpoints สูงสุดในผล full ที่เก็บไว้: 23,517/24,909 = 94.41%
- ใน Flow กลางที่มี full test: R95 สูงกว่า R88 บน checker/positive grades ชุดเดียวกัน (74.59% เทียบ 72.10%)
- R106 พัฒนาโครงสร้างและผ่านเฉพาะส่วนได้ดี แต่ full corpus ยังต่ำกว่า R95 บน shared grade identities: 69.25% เทียบ 73.42% ภายใต้ตัววิเคราะห์ R106
- R108/R109 เป็นข้อมูลที่เพิ่งรับ ไม่ใช่ runtime Flow ใหม่ จึงไม่มีคะแนนหลังใส่ข้อมูลและไม่มีหลักฐานพอจะให้ประมาณเป็น 80/90/95%
- คะแนนในรายงานนี้เป็นการผ่านเกณฑ์ข้อความ/ข้อกำหนด ไม่ใช่เปอร์เซ็นต์คำตอบที่มนุษย์ตรวจความหมายว่าถูกทั้งหมด

## 2. Full Test — 20,554 request keys / 55,811 grades

| Flow ที่รันทดสอบจริง | Positive/checkpoint score | Strict score | แหล่ง |
|---|---:|---:|---|
| Legacy เดิม — R64 LLM ON | 23,517/24,909 = 94.41% | 42,601/55,811 = 76.33% | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json) |
| Common — R88 LLM ON | 17,960/24,909 = 72.10% | 5,033/55,811 = 9.02% | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json) |
| Common ผสม — R95 LLM ON | 18,579/24,909 = 74.59% | 5,030/55,811 = 9.01% | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r95_merged_flow_implementation_20261018/full_analysis/ANALYSIS_FINAL.json) |
| Common Flow V2 ที่พัฒนาต่อ — R106 LLM ON | 17,238/24,891 = 69.25% | 5,019/55,811 = 8.99% | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r106_complete_flow_20261020/full_analysis/SCORES.json) |

Legacy/R88/R95 ใช้ 24,909 positive grades ตาม literal checker ฝั่ง R88/R95 โดย Legacy/R88 เทียบตรงกันใน R89. R106 มี positive denominator 24,891 ตามการวิเคราะห์เดิม และวิธี partition ไม่เท่ากับ literal R95 ทุกเงื่อนไข ตารางนี้เป็น dashboard ผลที่รายงานไว้ ไม่ใช่การจัดอันดับจาก grader เดียวกันทุกแถว

### Strict ของ Common รุ่นแรก R64

Legacy ปิด LLM 42,410/55,811 = 75.99%; เปิด LLM 42,601/55,811 = 76.33%. Common ปิด LLM 16,998/55,811 = 30.46%; เปิด LLM 12,517/55,811 = 22.43%. เป็น strict compatibility ดั้งเดิม ไม่ใช่ positive content score และไม่เอา 22.43% ไปเทียบกับ 74.59% ว่าเป็นเกณฑ์เดียวกัน
[รายงาน R64](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/FINAL_FULL_TEST_REPORT.md)

## 3. แยกภาษา — Full Test

| Flow | ไทย | อังกฤษ | Auto |
|---|---:|---:|---:|
| Legacy เดิม — R64 LLM ON | 95.47% | 96.00% | 81.83% |
| Common — R88 LLM ON | 73.61% | 70.79% | 68.88% |
| Common ผสม — R95 LLM ON | 77.67% | 71.36% | 70.27% |
| Common Flow V2 ที่พัฒนาต่อ — R106 LLM ON | 71.19% | 67.37% | 65.96% |

Auto คือ locale ที่ขอให้ระบบเลือก ไม่ใช่ภาษาที่สาม ทุกแถวอ้างอิง metric ของแต่ละรายงานดังข้อ 2

## 4. R95 ↔ R106 บน grade identities เดียวกัน

| Locale | R95 ภายใต้ checker R106 | R106 | ต่างกี่ percentage points |
|---|---:|---:|---:|
| th | 9,915/13,126 (75.54%) | 9,344/13,126 (71.19%) | -4.35 |
| en | 6,720/9,465 (71.00%) | 6,377/9,465 (67.37%) | -3.63 |
| auto | 1,639/2,300 (71.26%) | 1,517/2,300 (65.96%) | -5.30 |
| total | 18,274/24,891 (73.42%) | 17,238/24,891 (69.25%) | -4.16 |

R95 74.59% ในข้อ 2 กับ R95 73.42% ในข้อนี้เป็นคำตอบชุด R95 เดียวกัน แต่ตัวแยกผ่าน/ไม่ผ่านและ positive denominator คนละแบบ ไม่ใช่ R95 ถูกนำไปรันใหม่แล้วลดลง
R106 มี watchdog exception 18 requests; input มี positive assertions 18 grades ที่ถูกตัดจาก denominator โดยระบบเดิม หากนับเป็นไม่ผ่านบน denominator เดิม 24,909 จะเป็น 17,238/24,909 = 69.20%. ยังมี taxonomy defect เช่น keyword timeout/latency ถูกจัด performance และบาง wrong_category ถูกจัด content ดังนั้นไม่อ้าง metric นี้เป็น semantic accuracy
การเทียบนี้ยังมีข้อมูล migration/metadata ต่างรุ่นกัน จึงไม่ใช่ผลของ algorithm Flow ล้วน ๆ
[รายละเอียดข้อบกพร่อง metric และสาเหตุ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r106_complete_flow_20261020/full_analysis/ROOT_CAUSE_REVIEW_TH.md)

## 5. ผลครึ่งชุด/สุ่ม — แยกจาก Full Test

| Flow | ขอบเขต | คะแนน positive | ข้อจำกัด |
|---|---|---:|---|
| Common หลังย้ายข้อมูล — R70 | 10,277 requests | 8,630/12,481 (69.15%) | ครึ่งชุด; model transport 0/253 จึงเป็น ON setting ที่ไม่ได้ยืนยัน inference จริง ห้ามจัดอันดับข้าม full corpus [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r70_half_common_llm_20261016/ANALYSIS_FINAL.json) |
| R92 — วัดใน R93 สุ่ม 1,000 | 1,000 requests | 765/1,140 (67.11%) | 1,000 request keys / 998 ข้อความ; supplement อีก 2 requests แยกจากตารางหลัก ไม่เทียบ full R88 72.10 โดยตรง; R88 cohort เดียวกัน 758/1140=66.49% [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/REPORT_FINAL_TH.md) |

R93 cohort เดียวกัน: retained R88 758/1,140 = 66.49%; R92 765/1,140 = 67.11%; R95 795/1,140 = 69.74%. เทียบสามตัวนี้บน sample เดียวกันได้ แต่ใช้ sample สรุปเป็น full 20,554 ไม่ได้

## 6. รุ่น R98–R105: ชุดพัฒนา 91 และ holdout 192

| Flow/รอบ | ชุดคำถาม | คะแนน positive | แหล่ง |
|---|---|---:|---|
| R98 subset02 | 91 requests | 61/72 (84.72%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r98_flow_v2_implementation_20261019/subset02/COMPARISON.json) |
| R100 subset05 | 91 requests | 63/72 (87.50%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r100_contract_flow_implementation_20261019/subset05/COMPARISON.json) |
| R101 release_subset09 | 91 requests | 65/72 (90.28%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r101_complete_flow_20261019/release_subset09/ANALYSIS.json) |
| R103 retained_91 | 91 requests | 66/72 (91.67%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r103_complete_revision_20261020/analysis_integrated02/retained_91_SCORES.json) |
| R103 retained_holdout192 | 192 requests | 150/249 (60.24%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r103_complete_revision_20261020/analysis_integrated02/retained_holdout192_SCORES.json) |
| R104 retained_91 | 91 requests | 62/72 (86.11%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r104_complete_flow_20261020/analysis_integrated03/retained_91_SCORES.json) |
| R104 retained_holdout192 | 192 requests | 148/249 (59.44%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r104_complete_flow_20261020/analysis_integrated03/retained_holdout192_SCORES.json) |
| R105 retained_91 | 91 requests | 62/72 (86.11%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r105_complete_flow_20261020/analysis_integrated04/retained_91_SCORES.json) |
| R105 retained_holdout192 | 192 requests | 148/249 (59.44%) | [หลักฐาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r105_complete_flow_20261020/analysis_integrated04/retained_holdout192_SCORES.json) |

91 ข้อเป็นชุดที่ใช้พัฒนาซ้ำ จึงมี selection/adaptation bias. R98 รอบแรก 55/72 เท่ากับ R95 cohort เดิม และ subset02 ภายหลังเป็น 61/72. R100 subset01 61/72; subset02/03/05 63/72. แสดงรอบหลังตาม lineage พร้อมเก็บข้อมูลรอบก่อน ไม่เลือกค่าสูงสุดมาทำนาย full accuracy
R103 ได้ 66/72 บนชุดพัฒนา แต่ holdout 150/249 ≈ 60.24%; R104/R105 เหลือ 62/72 และ holdout 148/249 ≈ 59.44%. ความต่างระหว่างชุดพัฒนากับชุดกว้าง/holdout เป็นหลักฐานว่าคะแนนสูงของชุดเล็กยังใช้รับรองภาพรวมไม่ได้
R102 มี integrated01 19 lanes ที่รันแล้ว แต่หน่วยของแต่ละ lane ต่างกัน ไม่สร้างคะแนนเฉลี่ยรวมขึ้นเอง; R101 361/361 assertions และ 3/3 LLM toy-game probes ไม่ใช้แทนเปอร์เซ็นต์คำถามจริงทั้งระบบ

## 7. Acceptance tests ของงานเฉพาะส่วน

| รุ่น | ผ่าน assertions ใน R97 acceptance | เปอร์เซ็นต์ |
|---|---:|---:|
| R103 | 399/444 | 89.86% |
| R104 | 441/444 | 99.32% |
| R105 | 444/444 | 100.00% |
| R106 | 444/444 | 100.00% |

นี่เป็น 37 scenarios × 3 locales × 4 variants รวม 444 assertions/เคสตาม suite ไม่ใช่สุ่มจาก full corpus และไม่ใช่ 444 independent user questions. R105 ตรวจ integrated 19 lanes ส่วน R106 ตรวจเฉพาะ branch ที่แก้ตาม LINEAGE แล้วทำ full test. การผ่าน acceptance 100% อยู่ร่วมกับ full positive 69.25% ได้ เพราะโจทย์และเกณฑ์คนละขอบเขต

## 8. แต่ละ Flow เปลี่ยนอะไร และผลบอกอะไร

- **Legacy เดิม:** ตัวเลือกหัวข้อ/ข้อมูล/answer contract ถูกทำเฉพาะโดเมนจำนวนมากและตรงกับ oracle ที่สร้างจากระบบเดิม จึงตอบ corpus เก่าได้สูงกว่า แต่ไม่ได้พิสูจน์ว่าเพิ่มข้อมูลชนิดใหม่แล้วตอบได้โดยไม่แก้ parser และไม่ได้ยืนยันข้อมูลนโยบาย ณ วันนี้
- **Common ช่วง R58–R70:** เพิ่ม schema/ฐานกลางและย้ายข้อมูล ปัญหาเป็นทั้ง mapping/English/relations/selector/transport ไม่ใช่ดูเพียงจำนวน records ที่ย้าย จึงใช้ข้อมูลครบอย่างเดียวอธิบายคะแนนไม่ได้
- **R88 (R87 stage 2):** เชื่อมพฤติกรรมเก่าบางส่วนเข้ากับข้อมูลกลาง ผล full positive 72.10%; ยังติดราคา/เวลาจอง/คำถามหลายเรื่อง/กฎ
- **R95:** ผสม typed execution/Task contract กับ compatibility parsers; improved 783 regressed 164 positive grades เทียบ R88 สุทธิ +619 หรือ +2.49 points. คะแนนสูงสุดในกลุ่ม common ที่มีหลักฐาน full ภายใต้ checker เดียวกับ R88
- **R96/R97:** เป็นงานวิจัย/แผน Flow V2 ไม่มี runtime full score แยกของตัวแผน R97; การทำจริงเป็น R98–R106 ไม่สามารถให้เปอร์เซ็นต์ว่า Astra plan ถูก 95% จากตัวแผนอย่างเดียว
- **R98–R101:** ลง implementation ทีละส่วนจน shared context/plan, tasks, owner lifecycle, semantic planner, conflict/live/rental routes; ชุดพัฒนาดีขึ้น แต่ยังต้องพิสูจน์การเลือก task บนคำถามกว้าง
- **R102–R106:** ทำ coverage/need selection/dependency/validity/field evidence/unknown checks มากขึ้น แต่ full R106 ยังมี gate กฎไม่ตอบแม้มีข้อความ, เลือก maintenance แทนเปิดบริการ, เลือก facet ผิด, fallback ยาว, multi-need ไม่ครบ และ nested English leakage
- **R107/R108/R109:** แบบฟอร์มและข้อมูลเจ้าของ เริ่มปิด source gaps เช่นเวลาเช่า/จอย/ราคาแยกกลุ่ม/กติกา Pause; ยังไม่ใช่การทดสอบ Flow หลังใช้ข้อมูลนั้น และไม่อ้างว่าการรับคำตอบทำให้คะแนนสูงขึ้นแล้ว

## 9. ควรอ่านผลอย่างไรในตอนนี้

1. ถ้าถามว่าใครตอบชุดเก่าดีที่สุด: Legacy มีหลักฐาน positive checkpoints 94.41% สูงสุดใน saved full runs ที่เทียบนี้ แต่ไม่ใช่ semantic correctness ของวันนี้
2. ถ้าถามว่า common ตัวไหนมีหลักฐาน full ดีที่สุด: R95 ดีกว่า R88 บน checker เดียวกัน และ R95 ดีกว่า R106 บน R106 shared-grade analysis
3. ถ้าถามว่าโครงสร้างรองรับข้อมูลเจ้าของตัวไหนใหม่กว่า: สาย R97→R106 มีงานด้านนี้เพิ่ม แต่คะแนนภาพรวมยังไม่ชนะ จึงต้องแก้จุดติด source-to-answer และทดสอบหลังรวมข้อมูลก่อนตัดสิน
4. ยังไม่มีเปอร์เซ็นต์ semantic accuracy ที่ตรวจโดยมนุษย์อย่างอิสระครบระบบของทุก Flow จึงไม่ให้ตัวเลขคาดเดาว่าตัวล่าสุดจะ 90% แล้ว
5. การข้ามหน่วยโทษ Pause Tekken ตามคำสั่งใน R109 เป็นข้อยกเว้นของงานทดสอบอนาคต ไม่ลบโจทย์/ปรับเปอร์เซ็นต์ historical results ในรายงานนี้

## 10. บัญชีรุ่นที่พบทั้งหมด

บาง R number เป็นแผน วิเคราะห์ ย้ายข้อมูล แบบฟอร์ม หรือ execution control ไม่ใช่ Flow ใหม่ทุกเลข ตารางนี้จึงระบุครบทุกรุ่นที่มีโฟลเดอร์ โดยเปอร์เซ็นต์ใช้ได้เฉพาะชุดหลักฐานข้างบน ไม่สร้าง % รวมจากรายงานการทำงานสำเร็จ

| รุ่น/โฟลเดอร์ | กลุ่ม | คะแนนที่เปรียบเทียบในรายงานนี้ | เอกสารระดับโฟลเดอร์ |
|---|---|---|---|
| r36_focused_conversation_20261003_165903 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | ดูไฟล์ในโฟลเดอร์ |
| r36_focused_conversation_20261003_170011 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r36_focused_conversation_20261003_170011/ACTUAL_CHAT_ANALYSIS_TH.md) |
| r37_conversation_tests_20261003_171632 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r37_conversation_tests_20261003_171632/FINAL_REPORT_TH.md) |
| r40_targeted_flow_20261006_022135_9e5ad7 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/CASE_ANALYSIS_R40_3_TH.md) |
| r41_task_memory_20261006_142223_26da94 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/CASE_ANALYSIS_R41_TH.md) |
| r42_domain_resume_20261006_152553_b21f30 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/CASE_ANALYSIS_R42_TH.md) |
| r43_readiness_schedule_20261006_180143_00b40d | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/CASE_ANALYSIS_R43_TH.md) |
| r44_package_fees_20261006_185245_2ae7a0 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r44_package_fees_20261006_185245_2ae7a0/FLOW_R44_FINAL.md) |
| r45_rental_cases_20261007_110336_e4eaa3 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r45_rental_cases_20261007_110336_e4eaa3/CASE_ANALYSIS_R45_ALL_TH.md) |
| r46_english_rental_20261007_e6fc8fe4 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r46_english_rental_20261007_e6fc8fe4/CASE_ANALYSIS_R46_ENGLISH_TH.md) |
| r47_answer_content_20261007_91dd6684 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r47_answer_content_20261007_91dd6684/CASE_ANALYSIS_R47_TH.md) |
| r48_user_facts_20261008_08f5235b | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r48_user_facts_20261008_08f5235b/ANALYSIS_SERVICE_50_R48.md) |
| r49_service_dialogue_20261008_7d6cf466 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r49_service_dialogue_20261008_7d6cf466/FAILED_CASE_ANALYSIS_R49.md) |
| r50_flow_load_20261009_66d96bb7 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r50_flow_load_20261009_66d96bb7/REPORT_FINAL_R50.md) |
| r51_llm_benchmark_20261009_173746_93dfb5 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r51_llm_benchmark_20261009_173746_93dfb5/LLM_TIMING_REPORT_R51.md) |
| r52_research_flow_20261009_191123 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r52_research_flow_20261009_191123/FLOW.md) |
| r53_semantic_research_20261009_222545 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r53_semantic_research_20261009_222545/FLOW.md) |
| r54_shop_cases_20261009_235038 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r54_shop_cases_20261009_235038/ALL_QUESTIONS_ANSWERS.md) |
| r55_service_fixes_20261010_030151 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r55_service_fixes_20261010_030151/ALL_QUESTIONS_ANSWERS_TH.md) |
| r56_remaining_fixes_20261010_145024 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r56_remaining_fixes_20261010_145024/FLOW_FINAL.md) |
| r57_studio_scope_20261010_174001 | Flow เดิม/การแก้เฉพาะงานก่อน migration | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r57_studio_scope_20261010_174001/01_Download_Models_README_before.md) |
| r58_common_content_20261010 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/DELIVERY_TH.md) |
| r58_examples_20sets_20261012 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/README_TH.md) |
| r58_examples_240_20261012 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_audience.md) |
| r59_schema_repair_20261012 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r59_schema_repair_20261012/RESULTS_TH.md) |
| r60_generalization_20261012 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r60_generalization_20261012/RESULTS_TH.md) |
| r61_implementation_20261013 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r61_implementation_20261013/RESULTS_TH.md) |
| r61_solution_plan_20261013 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r61_solution_plan_20261013/FLOW_SOLUTIONS_TH.md) |
| r62_completion_20261013 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r62_completion_20261013/RESULTS_TH.md) |
| r63_legacy_migration_20261013 | schema กลาง/แผน/ย้ายข้อมูลก่อน R64 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r63_legacy_migration_20261013/RESULTS_TH.md) |
| r64_full_comparison_20261013 | full comparison/วิเคราะห์/ซ่อมข้อมูล | Legacy เดิม — R64 LLM ON | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/FINAL_FULL_TEST_REPORT.md) |
| r65_detailed_failure_analysis_20261014 | full comparison/วิเคราะห์/ซ่อมข้อมูล | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r65_detailed_failure_analysis_20261014/ALL_CORPUS_INDEX.md) |
| r66_common_repair_20261014 | full comparison/วิเคราะห์/ซ่อมข้อมูล | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/R66_FINAL_REPORT_TH.md) |
| r67_migration_parity_20261015 | full comparison/วิเคราะห์/ซ่อมข้อมูล | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/FINAL_REPORT_R67_TH.md) |
| r68_source_completion_20261016 | full comparison/วิเคราะห์/ซ่อมข้อมูล | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r68_source_completion_20261016/FINAL_REPORT_R68_TH.md) |
| r70_half_common_llm_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | Common หลังย้ายข้อมูล — R70 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r70_half_common_llm_20261016/REPORT_FINAL_TH.md) |
| r71_repair_flow_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r71_repair_flow_20261016/FLOW_COMMON_REPAIR_R71_TH.md) |
| r72_flow_implementation_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r72_flow_implementation_20261016/FLOW_R72_TH.md) |
| r73_scope_completion_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/FLOW_R73_TH.md) |
| r74_semantic_profile_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r74_semantic_profile_20261016/FLOW_R74_TH.md) |
| r75_profile_confirmation_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r75_profile_confirmation_20261016/FLOW_R75_TH.md) |
| r76_rejection_rephrase_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r76_rejection_rephrase_20261016/FLOW_R76_TH.md) |
| r77_qualified_confirmation_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r77_qualified_confirmation_20261016/FLOW_R77_TH.md) |
| r78_web_session_check_20261016 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/FLOW_R78_TH.md) |
| r79_connection_diagnostics_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r79_connection_diagnostics_20261017/FINDINGS_TH.md) |
| r80_open_status_reply_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r80_open_status_reply_20261017/REPORT_R80_TH.md) |
| r81_selector_latency_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r81_selector_latency_20261017/FLOW_R81_TH.md) |
| r82_automatic_llm_check_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r82_automatic_llm_check_20261017/DELIVERY_STATUS.md) |
| r83_selector_topic_repair_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r83_selector_topic_repair_20261017/FLOW_R83_TH.md) |
| r84_correction_scope_rental_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r84_correction_scope_rental_20261017/FLOW_R84_TH.md) |
| r85_legacy_common_flow_audit_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r85_legacy_common_flow_audit_20261017/LEGACY_VS_COMMON_FLOW_ANALYSIS_TH.md) |
| r86_flow_semantic_contract_audit_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r86_flow_semantic_contract_audit_20261017/FLOW_DIFFERENCE_ROOT_CAUSE_TH.md) |
| r87_common_behavior_bridge_20261017 | Flow กลางซ่อมหมวดและการเชื่อมระบบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r87_common_behavior_bridge_20261017/FLOW_R87_TH.md) |
| r88_full_common_llm_20261017 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | Common — R88 LLM ON | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/REPORT_FINAL_TH.md) |
| r89_saved_full_comparison_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r89_saved_full_comparison_20261018/COMPARISON_TH.md) |
| r90_full_flow_analysis_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/01_FULL_FLOW_LEGACY_TH.md) |
| r91_common_task_flow_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/01_PROPOSED_COMMON_FLOW_TH.md) |
| r92_common_flow_implementation_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | R92 — วัดใน R93 สุ่ม 1,000 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/IMPLEMENTATION_REPORT_TH.md) |
| r93_random_1000_common_on_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | R92 — วัดใน R93 สุ่ม 1,000 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/REPORT_FINAL_TH.md) |
| r94_merged_common_flow_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r94_merged_common_flow_20261018/01_MERGED_COMMON_FLOW_TH.md) |
| r95_merged_flow_implementation_20261018 | Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ | Common ผสม — R95 LLM ON | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r95_merged_flow_implementation_20261018/FLOW_REVIEW_ADDENDUM_TH.md) |
| r96_paper_informed_flow_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r96_paper_informed_flow_20261019/01_RESEARCH_AND_DIAGNOSIS_TH.md) |
| r97_flow_reassessment_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r97_flow_reassessment_20261019/01_R96_GAP_REVIEW_TH.md) |
| r98_flow_v2_implementation_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R98 subset02 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r98_flow_v2_implementation_20261019/IMPLEMENTED_FLOW_TH.md) |
| r99_flow_review_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r99_flow_review_20261019/RECOMMENDED_FLOW_TH.md) |
| r100_contract_flow_implementation_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R100 subset05 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r100_contract_flow_implementation_20261019/IMPLEMENTED_FLOW_TH.md) |
| r101_complete_flow_20261019 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R101 release_subset09 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r101_complete_flow_20261019/IMPLEMENTED_FLOW_TH.md) |
| r102_full_flow_plan_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r102_full_flow_plan_20261020/FULL_FLOW_TH.md) |
| r103_complete_revision_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R103 retained_91; R103 retained_holdout192 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r103_complete_revision_20261020/FULL_FLOW_TH.md) |
| r103_execution_control_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R103 retained_91; R103 retained_holdout192 | ดูไฟล์ในโฟลเดอร์ |
| r104_complete_flow_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R104 retained_91; R104 retained_holdout192 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r104_complete_flow_20261020/FULL_FLOW_TH.md) |
| r104_execution_control_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R104 retained_91; R104 retained_holdout192 | ดูไฟล์ในโฟลเดอร์ |
| r105_complete_flow_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R105 retained_91; R105 retained_holdout192 | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r105_complete_flow_20261020/FULL_FLOW_TH.md) |
| r105_execution_control_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | R105 retained_91; R105 retained_holdout192 | ดูไฟล์ในโฟลเดอร์ |
| r106_complete_flow_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | Common Flow V2 ที่พัฒนาต่อ — R106 LLM ON | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r106_complete_flow_20261020/FULL_FLOW_TH.md) |
| r106_execution_control_20261020 | งานวิจัย/R97 V2/การพัฒนา R98–R106 | Common Flow V2 ที่พัฒนาต่อ — R106 LLM ON | ดูไฟล์ในโฟลเดอร์ |
| r107_owner_questions_20261020 | แบบฟอร์มและรับข้อมูลเจ้าของ ไม่ใช่ Flow ที่วัดใหม่ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r107_owner_questions_20261020/QUESTIONS_TH.md) |
| r108_owner_intake_20261020 | แบบฟอร์มและรับข้อมูลเจ้าของ ไม่ใช่ Flow ที่วัดใหม่ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r108_owner_intake_20261020/INTAKE_REVIEW_TH.md) |
| r109_owner_answers_20261020 | แบบฟอร์มและรับข้อมูลเจ้าของ ไม่ใช่ Flow ที่วัดใหม่ | ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้ | [เอกสาร](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r109_owner_answers_20261020/RECEIPT_AND_UPDATES_TH.md) |

## หลักฐานเครื่องอ่านและความคงเดิม

COMPARISON.json เก็บ numerator/denominator/locale/source hashes ทุกตัวที่ใช้คำนวณ รวม snapshot metric R64 และบัญชีทุกโฟลเดอร์ อ่านข้อมูลผลเท่านั้น ไม่แก้ oracle/approvals/database/คำตอบผู้ใช้ ไม่ได้ทำ full test, baseline rerun หรือเรียก LLM เพิ่มในรอบนี้