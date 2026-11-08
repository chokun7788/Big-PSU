# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 48
- PASS: 19
- FAIL: 29
- ERROR: 0
- Pass rate: 39.58%
- Average latency: 0.7573s
- P95 latency: 1.0572s
- Keyword fail: 29
- Source fail: 22
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_source_rag`: 23
- `pipeline:structured_game_detail`: 16
- `pipeline:competition_facet_not_covered_no_answer`: 3
- `pipeline:hybrid_guarded_rerank`: 2
- `pipeline:no_answer`: 1
- `pipeline:protected_food_consumption`: 1
- `pipeline:chatbot_identity_fast_path`: 1
- `pipeline:competition_fact_card`: 1

## Route Category Distribution

- `competition_rules`: 29
- `games`: 17
- `rules`: 1
- `knowledge`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_valorant_v2_001 | competition_rules | `competition_rules` | 5 คน; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_valorant_v2_002 | competition_rules | `games` | ตัวจริง 5 คน; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_valorant_v2_003 | competition_rules | `competition_rules` | ไม่เกิน 6; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_valorant_v2_005 | competition_rules | `games` | หัวหน้าทีม; กรรมการ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_006 | competition_rules | `rules` | น้ำดื่ม; ปิดสนิท; หมากฝรั่ง; competition_rules_valorant_psu_phuket_2026 | อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_valorant_v2_008 | competition_rules | `games` | 2 สัปดาห์; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_010 | competition_rules | `competition_rules` | เลือด; ศพ; OFF | คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_202... |
| competition_valorant_v2_011 | competition_rules | `competition_rules` | ห้าม; FPS; Latency; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_valorant_v2_012 | competition_rules | `knowledge` | 7; Abyss; Sunset; competition_rules_valorant_psu_phuket_2026 | ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ ผมช่วยตอบคำถามเกี่ยวกับ: • เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน • ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน • อุปกรณ์และโซนบริกา... |
| competition_valorant_v2_013 | competition_rules | `competition_rules` | Lotus; Sunset | คำตอบ: * การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่ รายละเอียดที่เกี่ยวข้อง: • The map pool consists of the following 7 maps • แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Comp... |
| competition_valorant_v2_015 | competition_rules | `games` | โยนเหรียญ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_016 | competition_rules | `games` | เจ้าหน้าที่; บันทึกผล; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_017 | competition_rules | `competition_rules` | 13-0 | คำตอบ: 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น รายละเอียดที่เกี่ยวข้อง: • 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match f... |
| competition_valorant_v2_018 | competition_rules | `competition_rules` | Tactical | คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause) รายละเอียดที่เกี่ยวข้อง: • 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause) • การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน • ขอได้ 1 ครั้งต่อแผนที่ • บั๊กคือข้... |
| competition_valorant_v2_027 | competition_rules | `games` | ไม่ส่งผลกระทบ; เล่นต่อ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_028 | competition_rules | `games` | Major Bug; Challenge; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_030 | competition_rules | `games` | ก่อน; ดาเมจ; ย้อนรอบ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_031 | competition_rules | `games` | damage; ไม่; Challenge; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_032 | competition_rules | `games` | ผิด; ได้เปรียบ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_033 | competition_rules | `games` | ห้าม; Cypher; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_034 | competition_rules | `games` | ห้าม; นอกขอบเขต; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_035 | competition_rules | `games` | KAY/O; ZERO/POINT; Texture; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_036 | competition_rules | `games` | ห้าม; กระโดด; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_037 | competition_rules | `games` | Warning; ตักเตือน; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_042 | competition_rules | `games` | Snap Tap; SOCD; permitted; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_043 | competition_rules | `games` | ห้าม; Macros; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_valorant_v2_045 | competition_rules | `competition_rules` | social media | คำตอบ: * ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ รายละเอียดที่เกี่ยวข้อง: • ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์ • อุปกรณ์อิเล็ก... |
| competition_valorant_v2_047 | competition_rules | `competition_rules` | 2 สัปดาห์; แผนที่ใหม่; 4 สัปดาห์; Abyss | สรุปหัวข้อกติกา VALORANT ที่พบในเอกสาร: • ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร • Pre-Game Process (Before Game Start to Agent Selection) อ้างอิงจากกติกา: VALORANT แหล่งข้อมูล: local://competition_rules/competit... |
| competition_valorant_v2_048 | competition_rules | `competition_rules` | Warning; Round Rollback; Round Loss; Map Forfeit; Match Forfeit | สรุปหัวข้อกติกา VALORANT ที่พบในเอกสาร: • ประเภทบทลงโทษในเกม • การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด อ้างอิงจากกติกา: VALORANT แหล่งข้อมูล: local://competition_rules/compet... |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_ground_truth_competition_valorant_v2_diverse_current.jsonl`
