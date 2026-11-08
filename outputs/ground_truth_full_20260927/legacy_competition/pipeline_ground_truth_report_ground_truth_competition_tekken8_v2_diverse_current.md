# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 40
- PASS: 10
- FAIL: 30
- ERROR: 0
- Pass rate: 25.00%
- Average latency: 1.2691s
- P95 latency: 1.5959s
- Keyword fail: 29
- Source fail: 27
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:structured_game_detail`: 19
- `pipeline:competition_source_rag`: 12
- `pipeline:no_answer`: 3
- `pipeline:competition_facet_not_covered_no_answer`: 2
- `pipeline:structured_game_controls`: 1
- `pipeline:game_name_mention_detail_fast_path`: 1
- `pipeline:hybrid_guarded_rerank`: 1
- `pipeline:boundary_safety_redirect`: 1

## Route Category Distribution

- `games`: 24
- `competition_rules`: 15
- `no_answer`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_tekken8_v2_004 | competition_rules | `games` | ชนะครบ 2 เกม; competition_rules_tekken8_psu_esports | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_tekken8_v2_005 | competition_rules | `games` | เกมตัดสิน; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_006 | competition_rules | `competition_rules` | 3 รอบ | คำตอบ: กติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: • แข่งขันแบบ ออฟไลน์ (Offline) • ใช้เครื่องเกม PlayStation 5 • แข่งขันแบบ เดี่ยว (1v1) • รูปแบบการแข่งขัน: อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้... |
| competition_tekken8_v2_007 | competition_rules | `games` | 60 วินาที; competition_rules_tekken8_psu_esports | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_tekken8_v2_008 | competition_rules | `games` | No advantage; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_009 | competition_rules | `games` | Random; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_010 | competition_rules | `games` | ยกเว้น; DLC; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_011 | competition_rules | `games` | ทุกตัว; ยกเว้น; DLC; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_012 | competition_rules | `games` | ห้าม; ปรับแต่ง; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_013 | competition_rules | `games` | สกินมาตรฐาน; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_014 | competition_rules | `games` | อนุญาต; Assist; competition_rules_tekken8_psu_esports | TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 • Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว • Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมื... |
| competition_tekken8_v2_015 | competition_rules | `games` | ห้าม; Bug; Glitch; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_018 | competition_rules | `games` | ยินยอม; อุปกรณ์ขัดข้อง; เหตุฉุกเฉิน; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_019 | competition_rules | `games` | ปรับแพ้ทันที; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_020 | competition_rules | `games` | ออกจากเกมก่อนจบ; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_023 | competition_rules | `competition_rules` | คำตัดสิน; กรรมการ; competition_rules_tekken8_psu_esports | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_tekken8_v2_024 | competition_rules | `games` | ปรับเปลี่ยนกฎ; ไม่ต้องแจ้ง; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_025 | competition_rules | `games` | ถือเป็นที่สิ้นสุด; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_026 | competition_rules | `games` | ผู้ดูแล; กรรมการ; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_027 | competition_rules | `games` | ผู้จัดการแข่งขัน; ทันที; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_028 | competition_rules | `competition_rules` | ออฟไลน์; PlayStation 5; 1v1; FT2 | คำตอบ: * รูปแบบการแข่งขัน: แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports |
| competition_tekken8_v2_029 | competition_rules | `games` | DLC; ปรับแต่ง; สกินมาตรฐาน; competition_rules_tekken8_psu_esports | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_tekken8_v2_030 | competition_rules | `competition_rules` | Pause; ยินยอม; ปรับแพ้ | สรุปหัวข้อกติกา Tekken 8 ที่พบในเอกสาร: • การหยุดเกม • ตัวละครและการตั้งค่า อ้างอิงจากกติกา: Tekken 8 แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports |
| competition_tekken8_v2_031 | competition_rules | `games` | 3 รอบ; 60 วินาที; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_032 | competition_rules | `games` | Random; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_034 | competition_rules | `games` | ห้าม; เอฟเฟกต์; ออร่า; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_036 | competition_rules | `no_answer` | competition_rules_tekken8_psu_esports | ถ้าเป็นเหตุฉุกเฉิน ให้หยุดใช้งาน แจ้งเจ้าหน้าที่ทันที และปฏิบัติตามทางหนีไฟหรือคำแนะนำของหน่วยฉุกเฉินครับ ระบบยังไม่มีขั้นตอนฉุกเฉินเฉพาะของสาขาที่ยืนยันได้ |
| competition_tekken8_v2_037 | competition_rules | `competition_rules` | เปลี่ยนแปลง; กฎระเบียบ; competition_rules_tekken8_psu_esports | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_tekken8_v2_039 | competition_rules | `games` | DLC; Assist; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_tekken8_v2_040 | competition_rules | `games` | เดี่ยว; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_ground_truth_competition_tekken8_v2_diverse_current.jsonl`
