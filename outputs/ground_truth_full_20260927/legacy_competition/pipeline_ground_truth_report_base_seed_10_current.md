# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 10
- PASS: 1
- FAIL: 9
- ERROR: 0
- Pass rate: 10.00%
- Average latency: 0.2654s
- P95 latency: 0.4085s
- Keyword fail: 5
- Source fail: 8
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:structured_service_game_availability`: 2
- `pipeline:candidate_margin_clarification`: 2
- `pipeline:studio_rules_overview_fast_path`: 1
- `pipeline:protected_food_bring_permission`: 1
- `pipeline:protected_damage_responsibility`: 1
- `pipeline:structured_equipment_item`: 1
- `pipeline:structured_equipment_catalog`: 1
- `pipeline:rule_en`: 1

## Route Category Distribution

- `rules`: 2
- `games`: 2
- `equipment`: 2
- `clarification`: 2
- `penalty`: 1
- `overview`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| rules_001 | rules | `rules` | Regulation; home | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| rules_002 | rules | `rules` | พื้นที่ที่กำหนด; Regulation; home | นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| rules_003 | rules | `penalty` | ค่าเสียหาย; Regulation; home | ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต... |
| games_001 | games | `games` | Gran Turismo 7; Popular Games; home | PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้ PlayStation 5 #01-#02 (60 นาที, 1-2 คน) • Call of Duty: Modern Warfare III • Delta Force • EA Sports FC 24 • eFootball • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Hog... |
| games_002 | games | `games` | Popular Games; home | Nintendo Switch Zone มีเกมที่ยืนยันได้ดังนี้ Nintendo Switch (1-2 Persons) (60 นาที, 1-2 คน) • Pokémon Champions • Animal Crossing: New Horizons • It Takes Two • Little Nightmares II • Luigi's Mansion 3 • Mario Kart 8 De... |
| equipment_001 | equipment | `equipment` | PLAYstation5 Zone | PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive: เครื่องเกม PlayStation 5 สำหรับเล่นเกมคอนโซล และใช้เป็นฐานสำหรับ VR Zone บางชุด จำนวน: 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone อยู่ที่: PlayStation 5 Zone... |
| equipment_002 | equipment | `clarification` | PlayStation VR; VR; VR Zone; home | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| contact_001 | contact | `clarification` | Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| no_answer_001 | no_answer | `equipment` | ไม่พบข้อมูล | อุปกรณ์ใน PC Zone: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) • Gaming Monitor (10 Units) • Gaming Keyboard • Gaming Mouse • Gaming Headset • Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.... |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_base_seed_10_current.jsonl`
