# Broad Usage Eval v1

- Generated at: 2026-09-27T00:38:37
- Cases: 679
- Turn checks: 691
- Passed: 653
- Failed: 38
- Pass rate: 0.945
- Total wall sec: 312.188
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 25/25 pass, 0 fail
- competition_rules: 61/75 pass, 14 fail
- compound: 15/15 pass, 0 fail
- equipment: 57/58 pass, 1 fail
- game_controls: 157/171 pass, 14 fail
- games: 150/158 pass, 8 fail
- members: 47/47 pass, 0 fail
- reservation: 20/20 pass, 0 fail
- schedule: 10/10 pass, 0 fail
- service_fee: 87/88 pass, 1 fail
- session_followup: 24/24 pass, 0 fail

## By Strategy
- clarification: 42
- compound: 15
- fast/rule: 68
- no_answer: 1
- pipeline: 2
- rag/retrieval: 89
- structured: 474

## Common Problems
- route_category expected ['games'], got clarification: 21
- mode expected prefix ['pipeline: 10
- route_category expected ['competition_rules'], got games: 6
- route_category expected ['competition_rules'], got reservation: 5
- route_category expected ['competition_rules'], got clarification: 3
- missing 'The Last of Us Part I': 2
- missing 'The Legend of Zelda': 2
- missing 'ปุ่ม': 2
- missing any of ['L (Left Stick)', 'เคลื่อนที่']: 2
- missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']: 2
- missing 'Pokémon Champions': 1
- missing 'The Last of Us Part I / Part II': 1
- missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['Horizon Call of the Mountain', 'ปุ่ม', 'จอย', 'คอนโทรล']: 1
- missing any of ['Horizon Call of the Mountain', 'วิธีเล่น', 'เล่นได้ที่']: 1
- missing any of ['L (Left Stick)', 'เคลื่อนที่ / เดินสไลด์ข้าง']: 1
- missing any of ['L3 (Click Left Stick)', 'ย่อตัว']: 1
- missing any of ['Nintendo Switch', 'เล่นได้ที่']: 1
- missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['The Last of Us Part I / Part II', 'วิธีเล่น', 'เล่นได้ที่']: 1
- missing any of ['The Last of Us Part I', 'ปุ่ม', 'จอย', 'คอนโทรล']: 1
- missing any of ['The Last of Us Part II (Remastered)', 'ปุ่ม', 'จอย', 'คอนโทรล']: 1
- missing any of ['The Legend of Zelda', 'ปุ่ม', 'จอย', 'คอนโทรล']: 1
- missing any of ['The Legend of Zelda', 'วิธีเล่น', 'เล่นได้ที่']: 1
- missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['แนวเกม', 'เกม Action-Adventure']: 1
- missing any of ['แนวเกม', 'เกม Open-world Adventure']: 1
- route_category expected ['equipment', 'clarification'], got games: 1
- route_category expected ['service_fee'], got clarification: 1

## Top Failures

### SF-078 service_fee
- Question: The Last of Us Part I / Part II ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['service_fee'], got clarification, missing 'The Last of Us Part I'
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-043 games
- Question: Horizon Call of the Mountain เล่นยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['Horizon Call of the Mountain', 'วิธีเล่น', 'เล่นได้ที่']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-077 games
- Question: The Last of Us Part I / Part II คือเกมอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing 'The Last of Us Part I / Part II'
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-079 games
- Question: The Last of Us Part I / Part II เล่นยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['The Last of Us Part I / Part II', 'วิธีเล่น', 'เล่นได้ที่']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-080 games
- Question: The Last of Us Part I / Part II เป็นเกมแนวไหน
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['แนวเกม', 'เกม Action-Adventure']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-137 games
- Question: The Legend of Zelda: Breath of the Wild คือเกมอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing 'The Legend of Zelda'
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-138 games
- Question: The Legend of Zelda: Breath of the Wild เล่นได้ที่ไหน
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['Nintendo Switch', 'เล่นได้ที่']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-139 games
- Question: The Legend of Zelda: Breath of the Wild เล่นยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['The Legend of Zelda', 'วิธีเล่น', 'เล่นได้ที่']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### G-140 games
- Question: The Legend of Zelda: Breath of the Wild เป็นเกมแนวไหน
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['แนวเกม', 'เกม Open-world Adventure']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-048 game_controls
- Question: Horizon Call of the Mountain ใช้จอยยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['Horizon Call of the Mountain', 'ปุ่ม', 'จอย', 'คอนโทรล']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-111 game_controls
- Question: Pokémon Champions ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Problems: mode expected prefix ['pipeline:structured_game_controls'], got pipeline:game_control_missing_game_context, missing 'Pokémon Champions'
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### GC-141 game_controls
- Question: The Last of Us Part I ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing 'The Last of Us Part I', missing 'ปุ่ม'
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-142 game_controls
- Question: The Last of Us Part I ใช้จอยยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['The Last of Us Part I', 'ปุ่ม', 'จอย', 'คอนโทรล']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-143 game_controls
- Question: The Last of Us Part I ปุ่มเคลื่อนที่กดอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing any of ['L (Left Stick)', 'เคลื่อนที่']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-144 game_controls
- Question: The Last of Us Part I ปุ่มหันมองจุดสนใจกดอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-145 game_controls
- Question: The Last of Us Part II (Remastered) ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:ambiguity_clarification
- Answer: คำถามนี้ยังไม่ชัดว่าหมายถึงเกมไหนครับ เพราะมีหลายเกมที่ตรงกับคำถาม ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    The Last of Us Part II (Remastered) (PlayStation 5 Zone) •    The Last of Us Part I (PlayStation 5 Zone)  พิมพ์ต่อได้ เช่น `The Last of U...

### GC-146 game_controls
- Question: The Last of Us Part II (Remastered) ใช้จอยยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['The Last of Us Part II (Remastered)', 'ปุ่ม', 'จอย', 'คอนโทรล']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-147 game_controls
- Question: The Last of Us Part II (Remastered) ปุ่มเคลื่อนที่กดอะไร
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:ambiguity_clarification, missing any of ['L (Left Stick)', 'เคลื่อนที่']
- Answer: คำถามนี้ยังไม่ชัดว่าหมายถึงเกมไหนครับ เพราะมีหลายเกมที่ตรงกับคำถาม ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    The Last of Us Part II (Remastered) (PlayStation 5 Zone) •    The Last of Us Part I (PlayStation 5 Zone)  พิมพ์ต่อได้ เช่น `The Last of U...

### GC-148 game_controls
- Question: The Last of Us Part II (Remastered) ปุ่มหันมองจุดสนใจกดอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-149 game_controls
- Question: The Legend of Zelda: Breath of the Wild ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing 'The Legend of Zelda', missing 'ปุ่ม'
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-150 game_controls
- Question: The Legend of Zelda: Breath of the Wild ใช้จอยยังไง
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, missing any of ['The Legend of Zelda', 'ปุ่ม', 'จอย', 'คอนโทรล']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-151 game_controls
- Question: The Legend of Zelda: Breath of the Wild ปุ่มเคลื่อนที่ / เดินสไลด์ข้างกดอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing any of ['L (Left Stick)', 'เคลื่อนที่ / เดินสไลด์ข้าง']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### GC-152 game_controls
- Question: The Legend of Zelda: Breath of the Wild ปุ่มย่อตัวกดอะไร
- Resolved: -
- Mode: `pipeline:english_clarification`
- Route: `clarification/missing_target_clarification`
- Problems: route_category expected ['games'], got clarification, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:english_clarification, missing any of ['L3 (Click Left Stick)', 'ย่อตัว']
- Answer: I could not reliably understand that input. It may use the wrong keyboard layout. Please type the question again in Thai or English.

### E-006 equipment
- Question: Nintendo Switch Zone มีอะไรให้ใช้บ้าง
- Resolved: -
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['equipment', 'clarification'], got games
- Answer: เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:  EA Sports FC 24 •    แนวเกม: เกมฟุตบอล •    เล่นได้ที่: PlayStation 5 Zone  Nintendo Switch Sports •    แนวเกม: เกมกีฬา Motion Control •    เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.phu...

### CR-008 competition_rules
- Question: VALORANT รอบชิงเล่นกี่เกม
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['competition_rules'], got clarification
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม, กติกาการแข่งขัน

### CR-011 competition_rules
- Question: VALORANT ถ้าใช้ bug จะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['competition_rules'], got games
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### CR-012 competition_rules
- Question: VALORANT ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-014 competition_rules
- Question: VALORANT แผนที่มีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Problems: route_category expected ['competition_rules'], got games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### CR-027 competition_rules
- Question: CS2 ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-038 competition_rules
- Question: Counter-Strike 2 รอบชิงเล่นกี่เกม
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['competition_rules'], got clarification
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม, กติกาการแข่งขัน

### CR-041 competition_rules
- Question: Counter-Strike 2 ถ้าใช้ bug จะโดนอะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['competition_rules'], got games
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### CR-042 competition_rules
- Question: Counter-Strike 2 ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-044 competition_rules
- Question: Counter-Strike 2 แผนที่มีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['competition_rules'], got games
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### CR-053 competition_rules
- Question: TEKKEN 8 รอบชิงเล่นกี่เกม
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['competition_rules'], got clarification
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม, กติกาการแข่งขัน

### CR-056 competition_rules
- Question: TEKKEN 8 ถ้าใช้ bug จะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['competition_rules'], got games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### CR-057 competition_rules
- Question: TEKKEN 8 ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-059 competition_rules
- Question: TEKKEN 8 แผนที่มีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Problems: route_category expected ['competition_rules'], got games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### CR-072 competition_rules
- Question: ROV ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/
