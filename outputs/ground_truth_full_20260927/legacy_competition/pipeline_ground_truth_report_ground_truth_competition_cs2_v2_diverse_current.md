# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 48
- PASS: 30
- FAIL: 18
- ERROR: 0
- Pass rate: 62.50%
- Average latency: 0.8106s
- P95 latency: 1.0984s
- Keyword fail: 18
- Source fail: 10
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_source_rag`: 36
- `pipeline:competition_facet_not_covered_no_answer`: 5
- `pipeline:no_answer`: 1
- `pipeline:multi_question_splitter`: 1
- `pipeline:game_multi_name_mention_fast_path`: 1
- `pipeline:structured_members_group_list`: 1
- `pipeline:game_control_missing_game_context`: 1
- `pipeline:guarded_vector_direct`: 1
- `pipeline:protected_food_consumption`: 1

## Route Category Distribution

- `competition_rules`: 42
- `games`: 3
- `multi_question`: 1
- `overview`: 1
- `rules`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_cs2_v2_004 | competition_rules | `games` | 5 คน; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_cs2_v2_006 | competition_rules | `games` | ล่าสุด; CS2; Steam; competition_rules_cs2_psu_phuket_2026 | พบชื่อเกมที่ตรงกับคำถามมากกว่า 1 เกมครับ • Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม เล่นได้ที่: PC Zone • Call... |
| competition_cs2_v2_009 | competition_rules | `competition_rules` | 1 วัน; PSU Esports Studio; Phuket; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_cs2_v2_010 | competition_rules | `competition_rules` | PSU Esports Studio; Phuket; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_cs2_v2_013 | competition_rules | `overview` | ไม่มีการเปลี่ยนแปลง; competition_rules_cs2_psu_phuket_2026 | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| competition_cs2_v2_017 | competition_rules | `competition_rules` | ล่วงหน้า; 1 วัน | คำตอบ: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง รายละเอียดที่เกี่ยวข้อง: • 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง... |
| competition_cs2_v2_020 | competition_rules | `competition_rules` | รอบชิง | คำตอบ: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3) รายละเอียดที่เกี่ยวข้อง: • 3. รูปแบบการแข่งขัน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_... |
| competition_cs2_v2_026 | competition_rules | `games` | ฝั่งละ 3 รอบ; 4 ใน 6; $10,000; competition_rules_cs2_psu_phuket_2026 | ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไ... |
| competition_cs2_v2_028 | competition_rules | `competition_rules` | Ancient; Anubis; Dust 2; Train | • แผนที่ในการแข่งขัน แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026 |
| competition_cs2_v2_029 | competition_rules | `competition_rules` | Mirage; Nuke | คำตอบ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG รายละเอียดที่เกี่ยวข้อง: • 3. แผนที่ในการแข่งขัน • 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuke... |
| competition_cs2_v2_040 | competition_rules | `competition_rules` | PC; จอภาพ; โต๊ะ; เก้าอี้; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_cs2_v2_041 | competition_rules | `competition_rules` | Crosshair; Resolution; Brightness | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: • 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นร... |
| competition_cs2_v2_042 | competition_rules | `competition_rules` | สคริปต์; มาโคร | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: • 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นร... |
| competition_cs2_v2_043 | competition_rules | `competition_rules` | ห้าม; ติดตั้งโปรแกรม | คำตอบ: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้ รายละเอียดที่เกี่ยวข้อง: • 6. อุปกรณ์และการตั้งค่าเกม... |
| competition_cs2_v2_044 | competition_rules | `competition_rules` | โซเชียลมีเดีย | คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ รายละเอียดที่เกี่ยวข้อง: • 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นร... |
| competition_cs2_v2_045 | competition_rules | `competition_rules` | ไม่เกิน 6 คน; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_cs2_v2_047 | competition_rules | `competition_rules` | หัวหน้าทีม; กรรมการ; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_cs2_v2_048 | competition_rules | `rules` | น้ำดื่ม; ปิดสนิท; หมากฝรั่ง; competition_rules_cs2_psu_phuket_2026 | อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_ground_truth_competition_cs2_v2_diverse_current.jsonl`
