# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 80
- PASS: 35
- FAIL: 45
- ERROR: 0
- Pass rate: 43.75%
- Average latency: 0.9186s
- P95 latency: 1.2040s
- Keyword fail: 43
- Source fail: 32
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:competition_source_rag`: 47
- `pipeline:structured_game_detail`: 15
- `pipeline:competition_facet_not_covered_no_answer`: 11
- `pipeline:no_answer`: 3
- `pipeline:game_control_missing_game_context`: 1
- `pipeline:competition_fact_card`: 1
- `pipeline:competition_target_clarification`: 1
- `pipeline:rag_direct_curated`: 1

## Route Category Distribution

- `competition_rules`: 60
- `games`: 19
- `penalty`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| competition_challenger_cs2_001 | competition_rules | `competition_rules` | ไม่มีการเปลี่ยนแปลงสมาชิก; ตลอดระยะเวลาการแข่งขัน | คำตอบ: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง รายละเอียดที่เกี่ยวข้อง: • 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง... |
| competition_challenger_cs2_005 | competition_rules | `games` | ภาษาไทย; ประท้วง; competition_rules_cs2_psu_phuket_2026 | ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไ... |
| competition_challenger_cs2_006 | competition_rules | `competition_rules` | 1 วัน; PSU Esports Studio; ภูเก็ต; competition_rules_cs2_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_cs2_010 | competition_rules | `competition_rules` | แมตช์ | คำตอบ: การใช้บัค รายละเอียดที่เกี่ยวข้อง: • 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ • หยุดเกมโดยไม่ได้รับอนุญาต • การด่าทอ/ใช้ความรุนแรงทางวาจา • 3. ห้าม... |
| competition_challenger_cs2_013 | competition_rules | `competition_rules` | Nuke; Train | คำตอบ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026 |
| competition_challenger_cs2_015 | competition_rules | `competition_rules` | quality first sentence mismatch: ต่างกัน | คำตอบ: Counter-Strike 2: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_ph... |
| competition_challenger_cs2_019 | competition_rules | `competition_rules` | ผู้เล่น 5 คน | คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น รายละเอียดที่เกี่ยวข้อง: • 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร อ้างอิงจากกติกา: Counter-Stri... |
| competition_challenger_cs2_020 | competition_rules | `competition_rules` | PSU Esports Studio; ภูเก็ต; competition_rules_cs2_psu_phuket_2026 | ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT |
| competition_challenger_rov_001 | competition_rules | `games` | 15 นาที; ปรับแพ้; competition_rules_rov_blueket_2025_men | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_challenger_rov_005 | competition_rules | `competition_rules` | 18 ตัว; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_rov_009 | competition_rules | `competition_rules` | Default Skin; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_rov_010 | competition_rules | `competition_rules` | First Blood; 2 นาที; เริ่มเกมใหม่; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_rov_011 | competition_rules | `competition_rules` | First Blood; ห้าม; อนุญาต; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_rov_012 | competition_rules | `penalty` | แจ้งทีมงาน; ดุลยพินิจ; กรรมการ; competition_rules_rov_blueket_2025_men | ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| competition_challenger_rov_013 | competition_rules | `competition_rules` | Resume | คำตอบ: 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังก... |
| competition_challenger_rov_014 | competition_rules | `competition_rules` | ปรับแพ้ | คำตอบ: 6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รับการร้องเรียนจากผู้อื่น ทีมงานจะมีมาตรการลงโทษผู้เข้าแข่งขันที่ฝ่าฝืนกติกา โดยตัดสิทธิ์การเข้าร่วมแข่งขัน รายละเอียดที่เกี่ยวข้อง: • 6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกท... |
| competition_challenger_rov_016 | competition_rules | `competition_rules` | ปรับ; แพ้ | คำตอบ: 4.4. เวลาพัก รายละเอียดที่เกี่ยวข้อง: • 4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม • 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือ... |
| competition_challenger_rov_018 | competition_rules | `competition_rules` | PSU Esports Studio; อาคาร 5; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_rov_020 | competition_rules | `competition_rules` | ห้าม; หยาบคาย; เสียดสี; competition_rules_rov_blueket_2025_men | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_valorant_001 | competition_rules | `competition_rules` | 5 คน; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_valorant_002 | competition_rules | `games` | คีย์บอร์ด; เมาส์; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_003 | competition_rules | `games` | Snap Tap; SOCD; อนุญาต; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_challenger_valorant_004 | competition_rules | `games` | ห้าม; Macros; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_005 | competition_rules | `competition_rules` | ติดตั้งโปรแกรม | คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) รายละเอียดที่เกี่ยวข้อง: • เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้... |
| competition_challenger_valorant_006 | competition_rules | `competition_rules` | social media; เว็บไซต์สื่อสาร | คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) รายละเอียดที่เกี่ยวข้อง: • เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้... |
| competition_challenger_valorant_007 | competition_rules | `competition_rules` | ไม่เกิน 6; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_valorant_008 | competition_rules | `competition_rules` | ห้าม; โทรศัพท์มือถือ; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_valorant_009 | competition_rules | `games` | หัวหน้าทีม; เอกสาร; กรรมการ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_010 | competition_rules | `games` | น้ำดื่ม; ปิดสนิท; หมากฝรั่ง; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_014 | competition_rules | `games` | ปิด; Blood; Bodies; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_015 | competition_rules | `competition_rules` | ห้าม; FPS; Latency; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| competition_challenger_valorant_016 | competition_rules | `games` | โยนเหรียญ; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_018 | competition_rules | `competition_rules` | 13-0 | คำตอบ: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing) รายละเอียดที่เกี่ยวข้อง: • 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนท... |
| competition_challenger_valorant_023 | competition_rules | `games` | Play Through; เล่นต่อ; Challenge; competition_rules_valorant_psu_phuket_2026 | VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือ... |
| competition_challenger_valorant_024 | competition_rules | `games` | ห้าม; Cypher; Texture; competition_rules_valorant_psu_phuket_2026 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| competition_challenger_tekken8_003 | competition_rules | `competition_rules` | 3 รอบ; R3 | คำตอบ: กติกาการแข่งขัน รายละเอียดที่เกี่ยวข้อง: • แข่งขันแบบ ออฟไลน์ (Offline) • ใช้เครื่องเกม PlayStation 5 • แข่งขันแบบ เดี่ยว (1v1) • รูปแบบการแข่งขัน: อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้... |
| competition_challenger_tekken8_005 | competition_rules | `games` | competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_006 | competition_rules | `games` | Random; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_007 | competition_rules | `games` | DLC; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_008 | competition_rules | `games` | ห้าม; Customization; ชุด; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_010 | competition_rules | `games` | อุปกรณ์ขัดข้อง; เหตุฉุกเฉิน; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_011 | competition_rules | `games` | ห้าม; ปรับแพ้ทันที; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_013 | competition_rules | `games` | สงวนสิทธิ์; เปลี่ยนแปลง; ไม่ต้องแจ้ง; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_014 | competition_rules | `games` | เกมตัดสิน; competition_rules_tekken8_psu_esports | TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อส... |
| competition_challenger_tekken8_015 | competition_rules | `competition_rules` | FT2; R3; 60 วินาที; PlayStation 5 | คำตอบ: กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ รายละเอียดที่เกี่ยวข้อง: • รูปแบบการแข่งขัน: • แข่งขันแบบ เดี่ยว (1v1) • แข่งขันแบบ ออฟไลน์ (Offline) • ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติ... |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_ground_truth_competition_challenger_v1_weird_user_questions_current.jsonl`
