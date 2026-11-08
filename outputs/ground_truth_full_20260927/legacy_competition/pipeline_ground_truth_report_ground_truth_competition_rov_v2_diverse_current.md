# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 48
- PASS: 28
- FAIL: 20
- ERROR: 0
- Pass rate: 58.33%
- Average latency: 0.5949s
- P95 latency: 0.6774s
- Keyword fail: 20
- Source fail: 13
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_source_rag`: 34
- `pipeline:competition_facet_not_covered_no_answer`: 11
- `pipeline:no_answer`: 1
- `pipeline:structured_members_group_list`: 1
- `pipeline:competition_fact_card`: 1

## Route Category Distribution

- `competition_rules`: 46
- `penalty`: 1
- `overview`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_rov_v2_009 | competition_rules | `competition_rules` | อาคาร 5; ชั้น 1; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_011 | competition_rules | `competition_rules` | BO3; ทุกรอบ | คำตอบ: 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) รายละเอียดที่เกี่ยวข้อง: • 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เ... |
| competition_rov_v2_012 | competition_rules | `competition_rules` | Best of 3; ทุกรอบ | คำตอบ: 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) รายละเอียดที่เกี่ยวข้อง: • 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสั... |
| competition_rov_v2_015 | competition_rules | `competition_rules` | หมายเลขห้อง; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_016 | competition_rules | `competition_rules` | 15 นาที; ปรับแพ้; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_017 | competition_rules | `competition_rules` | ล่าช้า; ปรับแพ้; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_018 | competition_rules | `competition_rules` | 18 ตัว; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_022 | competition_rules | `competition_rules` | Default Skin; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_023 | competition_rules | `competition_rules` | 5 ครั้ง; 1 นาที | คำตอบ: 4.6.3.1. ครั้งที่ 1: ตักเตือน รายละเอียดที่เกี่ยวข้อง: • 4.6.3.2. ครั้งที่ 2: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 1 ครั้ง • 4.6.3.3. ครั้งที่ 3: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 2 ครั้ง • 4.3.... |
| competition_rov_v2_024 | competition_rules | `competition_rules` | Resume | คำตอบ: 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีก... |
| competition_rov_v2_025 | competition_rules | `penalty` | แจ้งทีมงาน; ดุลยพินิจ; กรรมการ; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| competition_rov_v2_026 | competition_rules | `competition_rules` | First Blood; 2 นาที; เริ่มเกมใหม่; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_027 | competition_rules | `competition_rules` | First Blood; อนุญาต; คู่แข่ง; กรรมการ; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_030 | competition_rules | `competition_rules` | ปรับ; แพ้ | คำตอบ: 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม รายละเอียดที่เกี่ยวข้อง: • 4.4. เวลาพัก • 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี... |
| competition_rov_v2_031 | competition_rules | `overview` | 10 นาที; เริ่มเกมใหม่; competition_rules_rov_blueket_2025_men | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| competition_rov_v2_042 | competition_rules | `competition_rules` | ปรับแพ้; ตัดสิทธิ์ | คำตอบ: 6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลั... |
| competition_rov_v2_043 | competition_rules | `competition_rules` | เล่นแทน; ห้าม; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_044 | competition_rules | `competition_rules` | ออฟไลน์; BO3; PSU Esports Studio; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_rov_v2_046 | competition_rules | `competition_rules` | pause; First Blood; 2 นาที | คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ... |
| competition_rov_v2_047 | competition_rules | `competition_rules` | 5v5; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_ground_truth_competition_rov_v2_diverse_current.jsonl`
