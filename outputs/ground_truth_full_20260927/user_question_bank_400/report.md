# User Question Bank Evaluation

- Generated at: 2026-09-27T00:36:57
- Total questions: 400
- Total wall time: 211.807s

## Summary By Strategy
- fastpath/rulebase: 70
- no_answer: 3
- pipeline: 53
- rag/vector: 274

## Results

### GR-001 game_rules ข้อ 1
- Question: ROV คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:game_detail_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 3.3874s | Wall: 3.4581s
- Sources: competition_rules: data/competition_rules
- Answer: RoV / Arena of Valor: RoV หรือ Arena of Valor คือเกม MOBA บนมือถือที่ผู้เล่นแบ่งเป็นทีม เลือกฮีโร่ และร่วมกันทำลายป้อม/ฐานของฝ่ายตรงข้าม แนวเกม: เกม MOBA แบบทีม วิธีเล่นโดยสรุป: โดยทั่วไปผู้เล่นต้องเลือกตำแหน่งและฮีโร่ให้เหมาะกับทีม เก็บเลเวล คุมแผนที่ ช่วยทีม...

### GR-002 game_rules ข้อ 2
- Question: ROV เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:game_name_mention_detail_fast_path`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 2.2018s | Wall: 2.202s
- Sources: competition_rules: data/competition_rules
- Answer: RoV / Arena of Valor: RoV หรือ Arena of Valor คือเกม MOBA บนมือถือที่ผู้เล่นแบ่งเป็นทีม เลือกฮีโร่ และร่วมกันทำลายป้อม/ฐานของฝ่ายตรงข้าม แนวเกม: เกม MOBA แบบทีม วิธีเล่นโดยสรุป: โดยทั่วไปผู้เล่นต้องเลือกตำแหน่งและฮีโร่ให้เหมาะกับทีม เก็บเลเวล คุมแผนที่ ช่วยทีม...

### GR-003 game_rules ข้อ 3
- Question: ROV มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.7305s | Wall: 0.7306s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s01_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใ...

### GR-004 game_rules ข้อ 4
- Question: ROV แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3219s | Wall: 0.3221s
- Sources: competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้  รายละเอียดที่เกี่ยวข้อง: •    4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด...

### GR-005 game_rules ข้อ 5
- Question: ROV มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2904s | Wall: 0.2906s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-006 game_rules ข้อ 6
- Question: ROV ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.275s | Wall: 0.2752s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-007 game_rules ข้อ 7
- Question: ROV ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3191s | Wall: 0.3193s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-008 game_rules ข้อ 8
- Question: ROV ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.4023s | Wall: 0.4024s
- Sources: competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ  รายละเอียดที่เกี่ยวข้อง: •    4.6.2.2. ห้ามมิให้ผู้เข้าร่วมกา...

### GR-009 game_rules ข้อ 9
- Question: ROV มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3775s | Wall: 0.3777s
- Sources: competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที  รายละเอียดที่เกี่ยวข้อง: •    6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันท...

### GR-010 game_rules ข้อ 10
- Question: ROV ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2872s | Wall: 0.2873s
- Sources: competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s02_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น  รายละเอียดที่เกี่ยวข้อง: •    6.2.1.ห้ามผู้เข้าแข่งขันทุกคนใช้โปรแกรมช่วยหรือในการเล่นใด ๆ ทั้งสิ้น •    6.2.2.ห้าม...

### GR-011 game_rules ข้อ 11
- Question: ROV ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2992s | Wall: 0.2993s
- Sources: competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s04_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s05_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลักฐานและยุติการแข่งขันในทันที แต่หากมีการ...

### GR-012 game_rules ข้อ 12
- Question: ROV รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3196s | Wall: 0.3198s
- Sources: competition_rules_rov_blueket_2025_men_s05_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 3. รูปแบบการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    3.2. แข่ง Best of 3 (BO3) ทุกรอบ •    4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) •    3.1. แข่งแบบออฟไลน์ •    4. ระเบียบ...

### GR-013 game_rules ข้อ 13
- Question: ROV รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2368s | Wall: 0.237s
- Sources: competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s05_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s04_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s01_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: · เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3  รายละเอียดที่เกี่ยวข้อง: •    เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3 •    เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3 •    เวลา 12.30-...

### GR-014 game_rules ข้อ 14
- Question: ROV มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3079s | Wall: 0.3081s
- Sources: competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick  รายละเอียดที่เกี่ยวข้อง: •    6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที •    6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รับการร้องเรียนจากผู้อื่น ทีมงานจะมีมาตรการลงโทษผู้เข้าแข่งขันที่ฝ่า...

### GR-015 game_rules ข้อ 15
- Question: ROV ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3544s | Wall: 0.3546s
- Sources: competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    5.1. อุปกรณ์โทรศัพท์มือถือและอินเตอร์เน็ตส่วนตัว และ/หรืออินเทอร์เน็ตของทางมหาวิทยาลัย •    5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว •    5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์...

### GR-016 game_rules ข้อ 16
- Question: ROV เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Strategy: `rag/vector`
- Latency: 0.3217s | Wall: 0.3219s
- Sources: Members: https://esports.phuket.psu.ac.th/about-us/Members
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### GR-017 game_rules ข้อ 17
- Question: ROV ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3317s | Wall: 0.3319s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-018 game_rules ข้อ 18
- Question: ROV ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2081s | Wall: 0.2083s
- Sources: competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s01_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4. ระเบียบและกติกาการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    4.1. กติกาพื้นฐาน •    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น •    4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ...

### GR-019 game_rules ข้อ 19
- Question: ROV ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.293s | Wall: 0.2932s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s03_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใ...

### GR-020 game_rules ข้อ 20
- Question: ROV ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.0847s | Wall: 0.0848s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-021 game_rules ข้อ 21
- Question: ROV มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2572s | Wall: 0.2574s
- Sources: competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s04_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที  รายละเอียดที่เกี่ยวข้อง: •    5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว •    5. ชุดแข่งขันและอุปกรณ์การแข่งขัน...

### GR-022 game_rules ข้อ 22
- Question: ROV ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2959s | Wall: 0.2963s
- Sources: competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที  รายละเอียดที่เกี่ยวข้อง: •    6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที •    6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทัน...

### GR-023 game_rules ข้อ 23
- Question: ROV มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.4125s | Wall: 0.4127s
- Sources: competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.4.หาก...

### GR-024 game_rules ข้อ 24
- Question: ROV ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3126s | Wall: 0.3128s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-025 game_rules ข้อ 25
- Question: ROV แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.272s | Wall: 0.2722s
- Sources: competition_rules_rov_blueket_2025_men_s06_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c03: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s06_c04: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s08_c02: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s01_c01: local://competition_rules/competition_rules_rov_blueket_2025_men | competition_rules_rov_blueket_2025_men_s07_c01: local://competition_rules/competition_rules_rov_blueket_2025_men
- Answer: คำตอบ: 4. ระเบียบและกติกาการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    4.1. กติกาพื้นฐาน •    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น •    4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ...

### GR-026 game_rules ข้อ 26
- Question: VALORANT คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5709s | Wall: 0.5711s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-027 game_rules ข้อ 27
- Question: VALORANT เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.632s | Wall: 0.6322s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-028 game_rules ข้อ 28
- Question: VALORANT มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3835s | Wall: 0.3836s
- Sources: competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร  รายละเอียดที่เกี่ยวข้อง: •    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง •    ข้อจำกัดเนื้อหาใหม่ •    เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitiv...

### GR-029 game_rules ข้อ 29
- Question: VALORANT แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.345s | Wall: 0.3452s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-030 game_rules ข้อ 30
- Question: VALORANT มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2029s | Wall: 0.203s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-031 game_rules ข้อ 31
- Question: VALORANT ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2484s | Wall: 0.2486s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-032 game_rules ข้อ 32
- Question: VALORANT ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2516s | Wall: 0.2517s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-033 game_rules ข้อ 33
- Question: VALORANT ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3562s | Wall: 0.3563s
- Sources: competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s22_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s23_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s20_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s21_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้ •    Major Bug บั๊กที่ส่งผลกระทบต่อก...

### GR-034 game_rules ข้อ 34
- Question: VALORANT มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2174s | Wall: 0.2175s
- Sources: competition_rules_valorant_psu_phuket_2026_s10_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s14_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s25_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: ประเภทบทลงโทษในเกม  รายละเอียดที่เกี่ยวข้อง: •    3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ •    4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผน...

### GR-035 game_rules ข้อ 35
- Question: VALORANT ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.5941s | Wall: 0.5942s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ VALORANT เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-036 game_rules ข้อ 36
- Question: VALORANT ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2106s | Wall: 0.2108s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-037 game_rules ข้อ 37
- Question: VALORANT รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2302s | Wall: 0.2303s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-038 game_rules ข้อ 38
- Question: VALORANT รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.167s | Wall: 0.1671s
- Sources: -
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม, กติกาการแข่งขัน

### GR-039 game_rules ข้อ 39
- Question: VALORANT มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.6981s | Wall: 0.6982s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ VALORANT เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-040 game_rules ข้อ 40
- Question: VALORANT ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.9762s | Wall: 0.9766s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-041 game_rules ข้อ 41
- Question: VALORANT เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.85s | Wall: 0.8502s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-042 game_rules ข้อ 42
- Question: VALORANT ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.77s | Wall: 0.7701s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-043 game_rules ข้อ 43
- Question: VALORANT ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.6335s | Wall: 0.6336s
- Sources: VALORANT: https://esports.computing.psu.ac.th/reservation
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### GR-044 game_rules ข้อ 44
- Question: VALORANT ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2142s | Wall: 0.2144s
- Sources: competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร  รายละเอียดที่เกี่ยวข้อง: •    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง •    ข้อจำกัดเนื้อหาใหม่ •    เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitiv...

### GR-045 game_rules ข้อ 45
- Question: VALORANT ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.0241s | Wall: 0.0243s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-046 game_rules ข้อ 46
- Question: VALORANT มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3547s | Wall: 0.3548s
- Sources: competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s16_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s17_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)  รายละเอียดที่เกี่ยวข้อง: •    อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช...

### GR-047 game_rules ข้อ 47
- Question: VALORANT ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2511s | Wall: 0.2512s
- Sources: competition_rules_valorant_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s14_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s10_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s25_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)  รายละเอียดที่เกี่ยวข้อง: •    3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ •    4. การปรับแพ้ในแผนที่ (Map Forfeit...

### GR-048 game_rules ข้อ 48
- Question: VALORANT มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2907s | Wall: 0.2909s
- Sources: competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s22_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause)  รายละเอียดที่เกี่ยวข้อง: •    2. Technical Pause •    ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์ •    ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต  อ้างอิงจากกติกา:...

### GR-049 game_rules ข้อ 49
- Question: VALORANT ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2746s | Wall: 0.2747s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-050 game_rules ข้อ 50
- Question: VALORANT แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2208s | Wall: 0.2209s
- Sources: competition_rules_valorant_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s02_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s07_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026 | competition_rules_valorant_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- Answer: คำตอบ: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด  รายละเอียดที่เกี่ยวข้อง: •    การใช้สกิลเอเจนท์ •    ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่ •    ห้ามใช้สกิลในพื้นที่นอกขอ...

### GR-051 game_rules ข้อ 51
- Question: CS2 คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.4729s | Wall: 0.473s
- Sources: Counter-Strike 2: https://esports.computing.psu.ac.th/reservation
- Answer: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็ง...

### GR-052 game_rules ข้อ 52
- Question: CS2 เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.583s | Wall: 0.5831s
- Sources: Counter-Strike 2: https://esports.computing.psu.ac.th/reservation
- Answer: Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม แนวเกม: เกมยิง Tactical FPS วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็ง...

### GR-053 game_rules ข้อ 53
- Question: CS2 มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.5658s | Wall: 0.566s
- Sources: competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s19_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs...

### GR-054 game_rules ข้อ 54
- Question: CS2 แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.838s | Wall: 0.8382s
- Sources: competition_rules_cs2_psu_phuket_2026_s18_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s23_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน  รายละเอียดที่เกี่ยวข้อง: •    1. โหมด Competitive (5v5)  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### GR-055 game_rules ข้อ 55
- Question: CS2 มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.225s | Wall: 0.2251s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-056 game_rules ข้อ 56
- Question: CS2 ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2778s | Wall: 0.2779s
- Sources: competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s45_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s41_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s43_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s58_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s46_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s38_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s50_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: •    1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Cros...

### GR-057 game_rules ข้อ 57
- Question: CS2 ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3306s | Wall: 0.3307s
- Sources: competition_rules_cs2_psu_phuket_2026_s38_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s30_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง  รายละเอียดที่เกี่ยวข้อง: •    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที •    4. ขั้นตอนการดำเนินการแข่งขัน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket...

### GR-058 game_rules ข้อ 58
- Question: CS2 ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2884s | Wall: 0.2885s
- Sources: competition_rules_cs2_psu_phuket_2026_s34_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time  รายละเอียดที่เกี่ยวข้อง: •    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 202...

### GR-059 game_rules ข้อ 59
- Question: CS2 มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2826s | Wall: 0.2827s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s35_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 8. ตารางบทลงโทษ (Penalties)  รายละเอียดที่เกี่ยวข้อง: •    5. พฤติกรรมและบทลงโทษ •    บทลงโทษ •    7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ •    ตักเตือน → ปรับแพ้ในรอบ...

### GR-060 game_rules ข้อ 60
- Question: CS2 ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2594s | Wall: 0.2596s
- Sources: competition_rules_cs2_psu_phuket_2026_s50_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s41_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s34_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s42_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s18_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s52_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### GR-061 game_rules ข้อ 61
- Question: CS2 ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2506s | Wall: 0.2508s
- Sources: competition_rules_cs2_psu_phuket_2026_s17_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s12_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s16_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s57_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s52_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s38_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s34_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น  รายละเอียดที่เกี่ยวข้อง: •    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร •    2. คุณสมบัติของทีมและผู้เล่น  อ้างอิงจากกติกา: Counter-Strik...

### GR-062 game_rules ข้อ 62
- Question: CS2 รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2947s | Wall: 0.2948s
- Sources: competition_rules_cs2_psu_phuket_2026_s19_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s20_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s21_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. รูปแบบทัวร์นาเมนต์ Single Elimination  รายละเอียดที่เกี่ยวข้อง: •    3. รูปแบบการแข่งขัน •    1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/c...

### GR-063 game_rules ข้อ 63
- Question: CS2 รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2358s | Wall: 0.2359s
- Sources: competition_rules_cs2_psu_phuket_2026_s21_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s19_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s20_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s50_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s45_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s01_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s23_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)  รายละเอียดที่เกี่ยวข้อง: •    1. รูปแบบทัวร์นาเมนต์ Single Elimination •    3. รูปแบบการแข่งขัน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/c...

### GR-064 game_rules ข้อ 64
- Question: CS2 มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.337s | Wall: 0.3371s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s37_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s35_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s28_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s55_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s49_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ •    3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ •    กา...

### GR-065 game_rules ข้อ 65
- Question: CS2 ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3522s | Wall: 0.3523s
- Sources: competition_rules_cs2_psu_phuket_2026_s37_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s52_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s46_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s51_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### GR-066 game_rules ข้อ 66
- Question: CS2 เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Strategy: `rag/vector`
- Latency: 0.217s | Wall: 0.2171s
- Sources: Members: https://esports.phuket.psu.ac.th/about-us/Members
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### GR-067 game_rules ข้อ 67
- Question: CS2 ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3287s | Wall: 0.3288s
- Sources: competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s30_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### GR-068 game_rules ข้อ 68
- Question: CS2 ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2332s | Wall: 0.2334s
- Sources: competition_rules_cs2_psu_phuket_2026_s34_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s50_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s09_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s26_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### GR-069 game_rules ข้อ 69
- Question: CS2 ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2726s | Wall: 0.2727s
- Sources: competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s36_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s51_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s05_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs...

### GR-070 game_rules ข้อ 70
- Question: CS2 ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.0759s | Wall: 0.076s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-071 game_rules ข้อ 71
- Question: CS2 มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2539s | Wall: 0.2541s
- Sources: competition_rules_cs2_psu_phuket_2026_s42_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s40_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s39_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s51_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s41_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s43_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s46_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s58_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 1. อุปกรณ์ที่อนุญาต  รายละเอียดที่เกี่ยวข้อง: •    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง •    6. อุปกรณ์และการตั้งค่าเกม  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...

### GR-072 game_rules ข้อ 72
- Question: CS2 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3291s | Wall: 0.3294s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s13_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s35_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์  รายละเอียดที่เกี่ยวข้อง: •    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์ •    ปรับแพ้ในแมตช์นั้น •    ปรับแพ้ในรอบนั้น  อ้างอิงจากกติกา: Counter-...

### GR-073 game_rules ข้อ 73
- Question: CS2 มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.4076s | Wall: 0.4078s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-074 game_rules ข้อ 74
- Question: CS2 ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3162s | Wall: 0.3164s
- Sources: competition_rules_cs2_psu_phuket_2026_s38_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s30_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s33_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s08_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s06_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s49_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง  รายละเอียดที่เกี่ยวข้อง: •    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที •    4. ขั้นตอนการดำเนินการแข่งขัน  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket...

### GR-075 game_rules ข้อ 75
- Question: CS2 แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2454s | Wall: 0.2455s
- Sources: competition_rules_cs2_psu_phuket_2026_s54_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s03_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s15_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s36_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s45_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s04_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s52_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026 | competition_rules_cs2_psu_phuket_2026_s58_c01: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- Answer: คำตอบ: 8. ตารางบทลงโทษ (Penalties)  รายละเอียดที่เกี่ยวข้อง: •    การละเมิด •    บทลงโทษ •    การด่าทอ/ใช้ความรุนแรงทางวาจา •    ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์  อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://co...

### GR-076 game_rules ข้อ 76
- Question: TEKKEN 8 คือเกมอะไร
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.5568s | Wall: 0.557s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-077 game_rules ข้อ 77
- Question: TEKKEN 8 เป็นเกมแนวไหน
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.6352s | Wall: 0.6354s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-078 game_rules ข้อ 78
- Question: TEKKEN 8 มีข้อมูลกติกาการแข่งขันไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.6045s | Wall: 0.6046s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: กติกาการแข่งขัน  รายละเอียดที่เกี่ยวข้อง: •    แข่งขันแบบ ออฟไลน์ (Offline) •    ใช้เครื่องเกม PlayStation 5 •    แข่งขันแบบ เดี่ยว (1v1) •    รูปแบบการแข่งขัน:  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_...

### GR-079 game_rules ข้อ 79
- Question: TEKKEN 8 แข่งขันใช้ผู้เล่นกี่คน
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.268s | Wall: 0.2681s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-080 game_rules ข้อ 80
- Question: TEKKEN 8 มีตัวสำรองได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2416s | Wall: 0.2418s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-081 game_rules ข้อ 81
- Question: TEKKEN 8 ถ้ามาสายจะเกิดอะไรขึ้น
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3158s | Wall: 0.3159s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-082 game_rules ข้อ 82
- Question: TEKKEN 8 ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.5955s | Wall: 0.5956s
- Sources: competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข  รายละเอียดที่เกี่ยวข้อง: •    ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด •    คำตัดสินของกรรมการถือเป็นที่สิ้นสุด •    กรรมกา...

### GR-083 game_rules ข้อ 83
- Question: TEKKEN 8 ขอ pause ระหว่างแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3293s | Wall: 0.3295s
- Sources: competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน  รายละเอียดที่เกี่ยวข้อง: •    ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ •    ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปร...

### GR-084 game_rules ข้อ 84
- Question: TEKKEN 8 มีบทลงโทษอะไรบ้าง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3146s | Wall: 0.3147s
- Sources: competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น  รายละเอียดที่เกี่ยวข้อง: •    ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น...

### GR-085 game_rules ข้อ 85
- Question: TEKKEN 8 ใช้โปรแกรมช่วยเล่นได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.6546s | Wall: 0.6548s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ TEKKEN 8 เล่นได้ที่ PC Zone - PC #01-#02, PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-086 game_rules ข้อ 86
- Question: TEKKEN 8 ถ้าทีมไม่ครบลงแข่งได้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3215s | Wall: 0.3217s
- Sources: competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ  รายละเอียดที่เกี่ยวข้อง: •    หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที •    การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน...

### GR-087 game_rules ข้อ 87
- Question: TEKKEN 8 รูปแบบการแข่งขันเป็นแบบไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3755s | Wall: 0.3757s
- Sources: competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * รูปแบบการแข่งขัน:  รายละเอียดที่เกี่ยวข้อง: •    แข่งขันแบบ เดี่ยว (1v1) •    หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน •    แข่งขันแบบ ออฟไลน์ (Offline) •    ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ) •    FT2: ผู้ชน...

### GR-088 game_rules ข้อ 88
- Question: TEKKEN 8 รอบชิงเล่นกี่เกม
- Expected: competition_rules
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1857s | Wall: 0.1859s
- Sources: -
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม, กติกาการแข่งขัน

### GR-089 game_rules ข้อ 89
- Question: TEKKEN 8 มีการแบนตัวละครหรือแผนที่ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.8042s | Wall: 0.8044s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ TEKKEN 8 เล่นได้ที่ PC Zone - PC #01-#02, PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-090 game_rules ข้อ 90
- Question: TEKKEN 8 ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 1.2014s | Wall: 1.2015s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-091 game_rules ข้อ 91
- Question: TEKKEN 8 เปลี่ยนสมาชิกทีมได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.8553s | Wall: 0.8555s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-092 game_rules ข้อ 92
- Question: TEKKEN 8 ถ้าพบ bug ต้องแจ้งใคร
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.7649s | Wall: 0.765s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-093 game_rules ข้อ 93
- Question: TEKKEN 8 ใช้ voice chat ได้ไหม
- Expected: competition_rules
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.5709s | Wall: 0.5711s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### GR-094 game_rules ข้อ 94
- Question: TEKKEN 8 ถ้าคู่แข่งไม่มาต้องทำยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3363s | Wall: 0.3365s
- Sources: competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: ข้อตกลงและข้อปฏิบัติ  รายละเอียดที่เกี่ยวข้อง: •    ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข •    ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า •    คำตัดสินของกรรมการถือเป็นที่ส...

### GR-095 game_rules ข้อ 95
- Question: TEKKEN 8 ต้องเช็คอินก่อนแข่งไหม
- Expected: competition_rules
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.1224s | Wall: 0.1226s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GR-096 game_rules ข้อ 96
- Question: TEKKEN 8 มีข้อห้ามเรื่องอุปกรณ์ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2855s | Wall: 0.2856s
- Sources: competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน  รายละเอียดที่เกี่ยวข้อง: •    ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ •    ใช้เครื่องเกม PlayStation 5 •    หากออกจากเกมโดยไ...

### GR-097 game_rules ข้อ 97
- Question: TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.407s | Wall: 0.4072s
- Sources: competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที  รายละเอียดที่เกี่ยวข้อง: •    ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น •    ผู้เข้า...

### GR-098 game_rules ข้อ 98
- Question: TEKKEN 8 มีกติกาเรื่อง remake หรือ restart ไหม
- Expected: competition_rules
- Mode: `pipeline:competition_facet_not_covered_no_answer`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.5636s | Wall: 0.5638s
- Sources: -
- Answer: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### GR-099 game_rules ข้อ 99
- Question: TEKKEN 8 ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.5211s | Wall: 0.5212s
- Sources: competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข  รายละเอียดที่เกี่ยวข้อง: •    ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด •    คำตัดสินของกรรมการถือเป็นที่สิ้นสุด •    กรรมกา...

### GR-100 game_rules ข้อ 100
- Question: TEKKEN 8 แหล่งข้อมูลกติกามาจากไหน
- Expected: competition_rules
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.3561s | Wall: 0.3563s
- Sources: competition_rules_tekken8_psu_esports_s06_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s02_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s05_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s08_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s01_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s04_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: ข้อตกลงและข้อปฏิบัติ  รายละเอียดที่เกี่ยวข้อง: •    ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข •    ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า •    คำตัดสินของกรรมการถือเป็นที่ส...

### PBC-001 play_booking_controls ข้อ 1
- Question: จอง PS5 ต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.3969s | Wall: 0.3971s
- Sources: booking_selection_ps5: https://esports.computing.psu.ac.th/
- Answer: จอง PlayStation 5 ต้องเลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการครับ •    ข้อมูลค่าบริการที่มีระบุ PlayStation 5 ต่อ 60 นาที สำหรับ 1-2 คน •    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง แหล่งข้อมูล: https://esports.computing.p...

### PBC-002 play_booking_controls ข้อ 2
- Question: จอง Nintendo Switch ต้องเลือกอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5619s | Wall: 0.5621s
- Sources: booking_selection_nintendo: https://esports.computing.psu.ac.th/
- Answer: จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ •    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons •    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons •    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันก...

### PBC-003 play_booking_controls ข้อ 3
- Question: จอง VR ครึ่งชั่วโมงได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5833s | Wall: 0.5834s
- Sources: rule_edit_booking::th::answer: https://esports.computing.psu.ac.th/ | rule_reservation_quick_summary::th::answer: https://esports.computing.psu.ac.th/ | rule_service_schedule::th::answer: https://esports.computing.psu.ac.th/
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-004 play_booking_controls ข้อ 4
- Question: จอง Cockpit ต้องจองล่วงหน้ากี่ชั่วโมง
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5288s | Wall: 0.5289s
- Sources: booking_selection_cockpit: https://esports.computing.psu.ac.th/
- Answer: ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ •    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel •    เกมที่ยืนยันได้คือ Gran Turismo 7 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-005 play_booking_controls ข้อ 5
- Question: จอง PC ต้องกรอกข้อมูลอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:mixed_reservation_fast`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.8028s | Wall: 0.803s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-006 play_booking_controls ข้อ 6
- Question: หลังจองต้องจ่ายเงินภายในกี่นาที
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.9675s | Wall: 0.9676s
- Sources: payment_timeout: https://esports.computing.psu.ac.th/
- Answer: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่ แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-007 play_booking_controls ข้อ 7
- Question: ถ้าจองผิดเวลาต้องแก้ยังไง
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/schedule_query`
- Strategy: `rag/vector`
- Latency: 0.58s | Wall: 0.5802s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-008 play_booking_controls ข้อ 8
- Question: ยกเลิกการจองต้องทำก่อนกี่ชั่วโมง
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5693s | Wall: 0.5695s
- Sources: cancel_booking: https://esports.computing.psu.ac.th/
- Answer: การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-009 play_booking_controls ข้อ 9
- Question: ตอนเช็คอินต้องใช้บัตรอะไร
- Expected: in_kb
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.3073s | Wall: 0.3074s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-010 play_booking_controls ข้อ 10
- Question: เช็คอินล่วงหน้าได้กี่นาที
- Expected: in_kb
- Mode: `pipeline:checkin_fast_path`
- Route: `reservation/count`
- Strategy: `rag/vector`
- Latency: 0.5918s | Wall: 0.5919s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-011 play_booking_controls ข้อ 11
- Question: จองได้สูงสุดกี่ session ต่อครั้ง
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5108s | Wall: 0.5109s
- Sources: booking_max_sessions: https://esports.computing.psu.ac.th/
- Answer: การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions สำหรับ PlayStation 5: 1 session = 1 ชั่วโมง ดังนั้น 3 sessions = สูงสุด 3 ชั่วโมงต่อการจอง 1 ครั้ง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-012 play_booking_controls ข้อ 12
- Question: ถ้าแนบสลิปผิดต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.7099s | Wall: 0.71s
- Sources: booking_steps: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองโดยสรุป: •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลาที่ต้องการ •    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ •    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง •    หลังจองต้องชำระเงินภายใน 10...

### PBC-013 play_booking_controls ข้อ 13
- Question: จองแทนเพื่อนได้ไหม
- Expected: in_kb
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 11.6483s | Wall: 11.6485s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### PBC-014 play_booking_controls ข้อ 14
- Question: ถ้าไม่จ่ายเงินหลัง booking จะเกิดอะไรขึ้น
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.6946s | Wall: 0.6947s
- Sources: payment_timeout: https://esports.computing.psu.ac.th/
- Answer: หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่ แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-015 play_booking_controls ข้อ 15
- Question: อยากจองเครื่องเล่นเกมกับเพื่อนต้องเริ่มตรงไหน
- Expected: in_kb
- Mode: `pipeline:booking_howto_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 22.7462s | Wall: 22.7463s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน...

### PBC-016 play_booking_controls ข้อ 16
- Question: ถ้าไม่มีบัตรนักศึกษาตอนจองทำยังไง
- Expected: in_kb
- Mode: `pipeline:protected_public_access`
- Route: `reservation/public_access`
- Strategy: `pipeline`
- Latency: 0.0309s | Wall: 0.031s
- Sources: reservation_public_access_reviewed_20260924: https://esports.computing.psu.ac.th/
- Answer: ใช้บัตรประชาชนครับ คนภายนอกจองได้โดยกรอกเลขในช่อง National ID ตอนจอง และแสดงบัตรประชาชนเมื่อเช็กอิน ไม่ต้องใช้รหัสนักศึกษา PSU แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-017 play_booking_controls ข้อ 17
- Question: จอง VR 1 ชั่วโมงกับ 30 นาทีต่างกันยังไง
- Expected: in_kb
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 1.1435s | Wall: 1.1436s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### PBC-018 play_booking_controls ข้อ 18
- Question: จอง Nintendo สำหรับ 4 คนต้องเลือกแบบไหน
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5595s | Wall: 0.5596s
- Sources: booking_selection_nintendo: https://esports.computing.psu.ac.th/
- Answer: จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ •    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons •    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons •    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันก...

### PBC-019 play_booking_controls ข้อ 19
- Question: อยากเล่นพวงมาลัยต้องจองโซนอะไร
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.3532s | Wall: 0.3533s
- Sources: booking_selection_cockpit: https://esports.computing.psu.ac.th/
- Answer: ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ •    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel •    เกมที่ยืนยันได้คือ Gran Turismo 7 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-020 play_booking_controls ข้อ 20
- Question: ถ้าไปถึงช้ากว่าเวลาจองจะยังเล่นได้ไหม
- Expected: in_kb
- Mode: `pipeline:no_answer`
- Route: `reservation/schedule_query`
- Strategy: `rag/vector`
- Latency: 5.5817s | Wall: 5.5818s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### PBC-021 play_booking_controls ข้อ 21
- Question: จองแล้วเปลี่ยนคนเล่นได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 3.3589s | Wall: 3.3591s
- Sources: rule_edit_booking::th::answer: https://esports.computing.psu.ac.th/ | rule_schedule_monday_play_window::th::answer: https://esports.computing.psu.ac.th/ | rule_schedule_morning_time::th::answer: https://esports.computing.psu.ac.th/
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-022 play_booking_controls ข้อ 22
- Question: จองแล้วขอเลื่อนวันได้ไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.7268s | Wall: 0.727s
- Sources: rule_edit_booking::th::answer: https://esports.computing.psu.ac.th/ | rule_schedule_monday_play_window::th::answer: https://esports.computing.psu.ac.th/ | rule_schedule_morning_time::th::answer: https://esports.computing.psu.ac.th/
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-023 play_booking_controls ข้อ 23
- Question: ระบบจองออนไลน์อยู่ที่ไหน
- Expected: in_kb
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 3.5719s | Wall: 3.5721s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### PBC-024 play_booking_controls ข้อ 24
- Question: ก่อนเข้าใช้บริการต้องทำอะไรบ้าง
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.9398s | Wall: 0.9399s
- Sources: rule_booking_steps::th::answer: https://esports.computing.psu.ac.th/ | rule_en_booking_steps_natural::th::answer: https://esports.computing.psu.ac.th/ | rule_user_info_and_slip::th::answer: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-025 play_booking_controls ข้อ 25
- Question: ถ้าจะจองหลายอุปกรณ์พร้อมกันต้องทำยังไง
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 1.2275s | Wall: 1.2277s
- Sources: booking_steps: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองโดยสรุป: •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลาที่ต้องการ •    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ •    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง •    หลังจองต้องชำระเงินภายใน 10...

### PBC-026 play_booking_controls ข้อ 26
- Question: จอง PlayStation 5 ใช้เวลารอบละกี่นาที
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5343s | Wall: 0.5345s
- Sources: booking_selection_ps5: https://esports.computing.psu.ac.th/
- Answer: จอง PlayStation 5 ต้องเลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการครับ •    ข้อมูลค่าบริการที่มีระบุ PlayStation 5 ต่อ 60 นาที สำหรับ 1-2 คน •    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง แหล่งข้อมูล: https://esports.computing.p...

### PBC-027 play_booking_controls ข้อ 27
- Question: จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.4908s | Wall: 0.4909s
- Sources: booking_selection_nintendo: https://esports.computing.psu.ac.th/
- Answer: จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ •    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons •    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons •    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันก...

### PBC-028 play_booking_controls ข้อ 28
- Question: ถ้าระบบจองไม่ขึ้นควรถามใคร
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.8197s | Wall: 0.8198s
- Sources: booking_steps: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองโดยสรุป: •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลาที่ต้องการ •    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ •    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง •    หลังจองต้องชำระเงินภายใน 10...

### PBC-029 play_booking_controls ข้อ 29
- Question: จองแล้วต้องตรวจสอบอีเมลไหม
- Expected: in_kb
- Mode: `pipeline:rag_direct_curated`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.9228s | Wall: 0.9229s
- Sources: rule_edit_booking::th::answer: https://esports.computing.psu.ac.th/ | rule_en_booking_required_information::th::answer: https://esports.computing.psu.ac.th/ | rule_user_info_and_slip::th::answer: https://esports.computing.psu.ac.th/
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-030 play_booking_controls ข้อ 30
- Question: จ่ายเงินผ่านบัญชีอะไร
- Expected: in_kb
- Mode: `pipeline:payment_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.6556s | Wall: 0.6557s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงินครับ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-031 play_booking_controls ข้อ 31
- Question: สอนขั้นตอนจองแบบสั้นๆ
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.4356s | Wall: 0.4358s
- Sources: booking_steps: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองโดยสรุป: แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-032 play_booking_controls ข้อ 32
- Question: ถ้าอยากเล่นวันนี้ต้องจองทันทีได้ไหม
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5103s | Wall: 0.5104s
- Sources: booking_selection_general: https://esports.computing.psu.ac.th/
- Answer: ถ้าจะเข้าใช้บริการเพื่อเล่นเกมที่ PSU Esports Studio - Phuket ต้องจองผ่านระบบก่อนครับ •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-033 play_booking_controls ข้อ 33
- Question: walk in ได้ไหมหรือต้องจองก่อน
- Expected: in_kb
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5334s | Wall: 0.5336s
- Sources: booking_advance: https://esports.computing.psu.ac.th/
- Answer: ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-034 play_booking_controls ข้อ 34
- Question: จองแล้วลืมเช็คอินจะเป็นอะไรไหม
- Expected: in_kb
- Mode: `pipeline:protected_checkin_required`
- Route: `reservation/checkin_required`
- Strategy: `pipeline`
- Latency: 0.0252s | Wall: 0.0253s
- Sources: reservation_rule_2_1_checkin_required: https://esports.computing.psu.ac.th/
- Answer: ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-035 play_booking_controls ข้อ 35
- Question: ต้องชำระเงินก่อนเล่นไหม
- Expected: in_kb
- Mode: `pipeline:booking_payment_before_play_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.6696s | Wall: 0.6697s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ต้องชำระเงินก่อนเข้าใช้บริการครับ •    หลังจองต้องชำระเงินภายใน 10 นาที •    ชำระโดยโอนเข้าบัญชีที่ระบบแจ้ง แล้วแนบสลิปเพื่อยืนยันการจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-036 play_booking_controls ข้อ 36
- Question: ถ้าอยากเล่น PS5 กับเพื่อนสองคนต้องจองยังไง
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5629s | Wall: 0.5631s
- Sources: booking_selection_ps5: https://esports.computing.psu.ac.th/
- Answer: จอง PlayStation 5 ต้องเลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการครับ •    ข้อมูลค่าบริการที่มีระบุ PlayStation 5 ต่อ 60 นาที สำหรับ 1-2 คน •    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง แหล่งข้อมูล: https://esports.computing.p...

### PBC-037 play_booking_controls ข้อ 37
- Question: ถ้าอยากเล่น Switch สี่คนต้องจองยังไง
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.518s | Wall: 0.5182s
- Sources: booking_selection_nintendo: https://esports.computing.psu.ac.th/
- Answer: จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ •    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons •    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons •    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันก...

### PBC-038 play_booking_controls ข้อ 38
- Question: ถ้าอยากลอง VR ครั้งแรกควรจองแบบไหน
- Expected: in_kb
- Mode: `pipeline:booking_vr_first_time_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.5866s | Wall: 0.5868s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ถ้าอยากลอง VR ครั้งแรก แนะนำจอง VR Station แบบ 30 นาทีก่อนครับ •    เลือกบริการ VR Station ในระบบจอง •    เลือกรอบ 30 นาทีหรือ 1 ชั่วโมงตามที่ต้องการ •    ก่อนเล่นควรให้เจ้าหน้าที่ช่วยแนะนำการใส่แว่นและคอนโทรลเลอร์ แหล่งข้อมูล: https://esports.computing.psu.ac...

### PBC-039 play_booking_controls ข้อ 39
- Question: ถ้าอยากเล่นเกมขับรถต้องจองอะไร
- Expected: in_kb
- Mode: `pipeline:structured_booking_selection`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 4.4303s | Wall: 4.4304s
- Sources: booking_selection_cockpit: https://esports.computing.psu.ac.th/
- Answer: ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ •    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel •    เกมที่ยืนยันได้คือ Gran Turismo 7 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### PBC-040 play_booking_controls ข้อ 40
- Question: ถ้าจองผิดชื่อแก้ไขได้ไหม
- Expected: in_kb
- Mode: `pipeline:booking_fast_path`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 0.7117s | Wall: 0.7119s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### PBC-041 play_booking_controls ข้อ 41
- Question: TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.6052s | Wall: 0.6053s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว •    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (...

### PBC-042 play_booking_controls ข้อ 42
- Question: TEKKEN 8 ปุ่มเตะขวากดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.5149s | Wall: 0.515s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-043 play_booking_controls ข้อ 43
- Question: TEKKEN 8 ปุ่มต่อยซ้ายคือปุ่มไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.5838s | Wall: 0.584s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว •    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counte...

### PBC-044 play_booking_controls ข้อ 44
- Question: TEKKEN 8 ปุ่มเปิด Heat คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.5095s | Wall: 0.5097s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร •    R1 (While in Heat): ฮีทสแมช - ปลดปล่อยท่าโจมตีเผด็จศึกอันทรงพลังปิดฉากคอมโบ โดยจะใช้เ...

### PBC-045 play_booking_controls ข้อ 45
- Question: TEKKEN 8 ปุ่ม pause คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:competition_source_rag`
- Route: `competition_rules/competition_rules_lookup`
- Strategy: `rag/vector`
- Latency: 0.2168s | Wall: 0.217s
- Sources: competition_rules_tekken8_psu_esports_s03_c01: local://competition_rules/competition_rules_tekken8_psu_esports | competition_rules_tekken8_psu_esports_s07_c01: local://competition_rules/competition_rules_tekken8_psu_esports
- Answer: คำตอบ: * การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน  รายละเอียดที่เกี่ยวข้อง: •    อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ •    เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ •    หากมีการกด...

### PBC-046 play_booking_controls ข้อ 46
- Question: Mario Kart 8 Deluxe ปุ่มเร่งเครื่องคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4345s | Wall: 0.4347s
- Sources: game_controls_mariokart8deluxe: https://gameinputdatabase.com/game/57
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    A: เร่งเครื่อง - กดค้างไว้ตลอดเพื่อเร่งเครื่องยนต์ให้รถวิ่งไปข้างหน้า แหล่งข้อมูล: https://gameinputdatabase.com/game/57

### PBC-047 play_booking_controls ข้อ 47
- Question: Mario Kart 8 Deluxe ปุ่มดริฟต์กดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3997s | Wall: 0.3999s
- Sources: game_controls_mariokart8deluxe: https://gameinputdatabase.com/game/57
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    ZR: ดริฟต์ - ใช้กระโดดและดริฟต์ขณะเข้าโค้งเพื่อทำความเร็ว หรือใช้ทำท่าผาดโผนเมื่อกระโดดออกจากเนินเร่งความเร็ว แหล่งข้อมูล: https://gameinputdatabase.com/game/57

### PBC-048 play_booking_controls ข้อ 48
- Question: Mario Kart 8 Deluxe ปุ่มใช้ไอเทมคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3763s | Wall: 0.3764s
- Sources: game_controls_mariokart8deluxe: https://gameinputdatabase.com/game/57
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    ZL: ใช้ไอเทม / บีบแตร - ใช้ไอเทมที่เก็บมาจากกล่องสุ่ม หากไม่มีไอเทมจะเป็นการบีบแตรรถ แหล่งข้อมูล: https://gameinputdatabase.com/game/57

### PBC-049 play_booking_controls ข้อ 49
- Question: Mario Kart Live Home Circuit ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls_no_current_game`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4556s | Wall: 0.4558s
- Sources: service_game_availability: https://esports.computing.psu.ac.th/
- Answer: ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Ma...

### PBC-050 play_booking_controls ข้อ 50
- Question: Mario Kart Live Home Circuit ปุ่มเร่งเครื่องกดอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls_no_current_game`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.431s | Wall: 0.4312s
- Sources: service_game_availability: https://esports.computing.psu.ac.th/
- Answer: ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Ma...

### PBC-051 play_booking_controls ข้อ 51
- Question: Call of Duty ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1154s | Wall: 0.1156s
- Sources: -
- Answer: Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    Call of Duty: Modern Warfare III (PlayStation 5 Zone) •    Call of Duty: Warzone (PC Zone)  พิมพ์ต่อได้ เช่น `Call of Duty:...

### PBC-052 play_booking_controls ข้อ 52
- Question: Call of Duty ปุ่มยิงคือปุ่มไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.0933s | Wall: 0.0934s
- Sources: -
- Answer: Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    Call of Duty: Modern Warfare III (PlayStation 5 Zone) •    Call of Duty: Warzone (PC Zone)  พิมพ์ต่อได้ เช่น `Call of Duty:...

### PBC-053 play_booking_controls ข้อ 53
- Question: Call of Duty ปุ่มเล็งคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1181s | Wall: 0.1183s
- Sources: -
- Answer: Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    Call of Duty: Modern Warfare III (PlayStation 5 Zone) •    Call of Duty: Warzone (PC Zone)  พิมพ์ต่อได้ เช่น `Call of Duty:...

### PBC-054 play_booking_controls ข้อ 54
- Question: Call of Duty ปุ่มรีโหลดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1217s | Wall: 0.1218s
- Sources: -
- Answer: Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    Call of Duty: Modern Warfare III (PlayStation 5 Zone) •    Call of Duty: Warzone (PC Zone)  พิมพ์ต่อได้ เช่น `Call of Duty:...

### PBC-055 play_booking_controls ข้อ 55
- Question: Naruto X Boruto ปุ่มโจมตีคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3639s | Wall: 0.364s
- Sources: game_controls_narutoxborutoultimateninjastormconnections: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-ninja-storm-connections
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Circle: โจมตีระยะประชิด - ต่อย/เตะ ทำคอมโบกระบวนท่า แหล่งข้อมูล: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-ninja-...

### PBC-056 play_booking_controls ข้อ 56
- Question: Naruto X Boruto ปุ่มคาถานินจาคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4294s | Wall: 0.4296s
- Sources: game_controls_narutoxborutoultimateninjastormconnections: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-ninja-storm-connections
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Triangle: คาถานินจา / จักระ - รีดเร้นจักระเพื่อใช้คาถาหรือท่าไม้ตายลับ (Secret Technique) •    L2: คาถาสลับร่าง - สลับร่างหลบการโจมตี (ใช้เกจหลบหลีก) •    D-Pad: ใช้อุป...

### PBC-057 play_booking_controls ข้อ 57
- Question: Naruto X Boruto ปุ่มสลับร่างคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.397s | Wall: 0.3972s
- Sources: game_controls_narutoxborutoultimateninjastormconnections: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-ninja-storm-connections
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    L2: คาถาสลับร่าง - สลับร่างหลบการโจมตี (ใช้เกจหลบหลีก) แหล่งข้อมูล: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-nin...

### PBC-058 play_booking_controls ข้อ 58
- Question: Little Nightmares II ปุ่มวิ่งคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4306s | Wall: 0.4308s
- Sources: game_controls_littlenightmaresii: https://gameinputdatabase.com/game/304
- Answer: Little Nightmares II ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Square: วิ่งเร็ว - กดเพื่อวิ่งสปรินต์ ใช้เพิ่มความเร็วในการเคลื่อนที่หรือวิ่งหนี •    Circle: ไฟฉาย / รีโมท - ใช้เปิดหรือปิดไฟฉายพกพา และใช้กดรีโมททีวี แหล่งข้อมูล: https://gameinputdatabase.com/g...

### PBC-059 play_booking_controls ข้อ 59
- Question: Little Nightmares II ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4031s | Wall: 0.4032s
- Sources: game_controls_littlenightmaresii: https://gameinputdatabase.com/game/304
- Answer: Little Nightmares II ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Cross: กระโดด / ขว้าง / โจมตี - ใช้สำหรับกระโดด ขว้างไอเทม หรือใช้เหวี่ยงอาวุธโจมตี •    Circle: ไฟฉาย / รีโมท - ใช้เปิดหรือปิดไฟฉายพกพา และใช้กดรีโมททีวี แหล่งข้อมูล: https://gameinputdatabase.co...

### PBC-060 play_booking_controls ข้อ 60
- Question: It Takes Two ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3407s | Wall: 0.3408s
- Sources: game_controls_ittakestwo: https://gameinputdatabase.com/game/90
- Answer: It Takes Two ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Cross (กากบาท): กระโดด - ใช้กระโดดข้ามสิ่งกีดขวาง (สามารถประยุกต์ใช้เพื่อ Double Jump ได้) แหล่งข้อมูล: https://gameinputdatabase.com/game/90

### PBC-061 play_booking_controls ข้อ 61
- Question: It Takes Two ปุ่มโต้ตอบคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3569s | Wall: 0.357s
- Sources: game_controls_ittakestwo: https://gameinputdatabase.com/game/90
- Answer: It Takes Two ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Triangle (สามเหลี่ยม): โต้ตอบ - ใช้โต้ตอบกับสิ่งแวดล้อม เช่น ดึงคันโยก, หมุนวาล์ว, หรือคุยกับ NPC แหล่งข้อมูล: https://gameinputdatabase.com/game/90

### PBC-062 play_booking_controls ข้อ 62
- Question: Overcooked 2 ปุ่มหยิบของคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3424s | Wall: 0.3425s
- Sources: game_controls_overcooked2: https://volx.jp/overcooked-2-keyboard-controller-setting/
- Answer: Overcooked! 2 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Cross: หยิบ / วาง - หยิบหรือวางสิ่งของ แหล่งข้อมูล: https://volx.jp/overcooked-2-keyboard-controller-setting/

### PBC-063 play_booking_controls ข้อ 63
- Question: Overcooked 2 ปุ่มหั่นของคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3205s | Wall: 0.3206s
- Sources: game_controls_overcooked2: https://volx.jp/overcooked-2-keyboard-controller-setting/
- Answer: Overcooked! 2 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Square: หั่น / ขว้าง - หั่นวัตถุดิบหรือขว้างสิ่งของ แหล่งข้อมูล: https://volx.jp/overcooked-2-keyboard-controller-setting/

### PBC-064 play_booking_controls ข้อ 64
- Question: Super Smash Bros Ultimate ปุ่มโจมตีคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4109s | Wall: 0.4111s
- Sources: game_controls_supersmashbrosultimate: https://gameinputdatabase.com/game/46
- Answer: Super Smash Bros. Ultimate ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    R (Right Stick): โจมตีสแมช - ก้านอนาล็อกขวาใช้สำหรับปล่อยท่า Smash Attack ไปตามทิศทางที่ดันอย่างรวดเร็ว •    A: โจมตีปกติ - การโจมตีพื้นฐาน (Jab/Tilt/Aerial) ขึ้นอยู่กับทิศทางของอนาล็อกซ้าย •...

### PBC-065 play_booking_controls ข้อ 65
- Question: Super Smash Bros Ultimate ปุ่มกระโดดคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4334s | Wall: 0.4335s
- Sources: game_controls_supersmashbrosultimate: https://gameinputdatabase.com/game/46
- Answer: Super Smash Bros. Ultimate ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    R (Right Stick): โจมตีสแมช - ก้านอนาล็อกขวาใช้สำหรับปล่อยท่า Smash Attack ไปตามทิศทางที่ดันอย่างรวดเร็ว •    X / Y: กระโดด - ใช้กระโดด สามารถกดพร้อมปุ่มโจมตีเพื่อทำ Aerial Attack ได้ แหล่งข้อม...

### PBC-066 play_booking_controls ข้อ 66
- Question: Nintendo Switch Sports ใช้จอยยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.2658s | Wall: 0.2659s
- Sources: game_controls_nintendoswitchsports: https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq
- Answer: Nintendo Switch Sports มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    Joy-Con motion: เล่นท่ากีฬาด้วยการขยับ Joy-Con - เกมใช้ Joy-Con หรือ Joy-Con 2 ตามชนิดกีฬาที่เลือก โดยการออกท่าจะขึ้นกับกีฬานั้น ๆ •    X Button on sport-selection screen: เลือกโหมดสายรัดขาใ...

### PBC-067 play_booking_controls ข้อ 67
- Question: Beat Saber เล่นยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4079s | Wall: 0.4081s
- Sources: Beat Saber: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง แนวเกม: เกม VR Rhythm วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง เล่นได้ที่: VR Zone แหล่งข้อมูล: https://e...

### PBC-068 play_booking_controls ข้อ 68
- Question: Gran Turismo 7 ใช้พวงมาลัยยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4285s | Wall: 0.4286s
- Sources: Gran Turismo 7: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: Gran Turismo 7: Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง แนวเกม: เกมแข่งรถ / Driving Simulator วิธีเล่นโดยสรุป: ใน Cockpit Zone เล่นโดยใช้พวงมาลัย คันเร่ง เบรก และชุดเบาะจำลองการขับรถ เป้าหมายคือขับให้เร็วและค...

### PBC-069 play_booking_controls ข้อ 69
- Question: เกมนี้มีปุ่มอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0791s | Wall: 0.0792s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-070 play_booking_controls ข้อ 70
- Question: เล่นยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0421s | Wall: 0.0422s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ หรือหมายถึงวิธีเล่นเกมไหน/วิธีเข้าใช้บริการ/จอง ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III ถ้าถามวิธีเล่น/ปุ่ม ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 เล่นยังไง` หรือ `Mario Kart...

### PBC-071 play_booking_controls ข้อ 71
- Question: วิธีใช้จอย
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0448s | Wall: 0.0449s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-072 play_booking_controls ข้อ 72
- Question: มีปุ่มอะไรบ้างถ้ายังไม่ได้บอกชื่อเกม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1582s | Wall: 0.1583s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-073 play_booking_controls ข้อ 73
- Question: ปุ่มทั้งหมดของเกมที่เพิ่งถามคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1372s | Wall: 0.1373s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-074 play_booking_controls ข้อ 74
- Question: ถ้าถามต่อว่าใช้จอยยังไงระบบจำเกมเดิมไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1833s | Wall: 0.1834s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-075 play_booking_controls ข้อ 75
- Question: ถามปุ่มเฉพาะของเกมที่ไม่มีข้อมูลจะตอบยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1898s | Wall: 0.19s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-076 play_booking_controls ข้อ 76
- Question: Minecraft มีปุ่มอะไรบ้างในศูนย์
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.2558s | Wall: 0.2559s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-077 play_booking_controls ข้อ 77
- Question: ROV มีปุ่มในเครื่องศูนย์ไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.2059s | Wall: 0.206s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-078 play_booking_controls ข้อ 78
- Question: เกมที่ไม่มีชื่อชัดเจนควรตอบปุ่มไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1508s | Wall: 0.151s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-079 play_booking_controls ข้อ 79
- Question: ถ้าอยากรู้ปุ่มของ PS5 ต้องถามแบบไหน
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1155s | Wall: 0.1156s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-080 play_booking_controls ข้อ 80
- Question: controller ของ Nintendo ใช้ยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1076s | Wall: 0.1077s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-081 play_booking_controls ข้อ 81
- Question: ปุ่ม Options ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4289s | Wall: 0.4291s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Options: หยุดเกม - หยุดเกมชั่วคราวเพื่อเข้าสู่หน้าต่างเมนู เช่น การเช็ก Move List (รายการท่า) หรือการตั้งค่าอื่น ๆ แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-082 play_booking_controls ข้อ 82
- Question: ปุ่ม Cross ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4273s | Wall: 0.4275s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-083 play_booking_controls ข้อ 83
- Question: ปุ่ม Circle ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4198s | Wall: 0.42s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-084 play_booking_controls ข้อ 84
- Question: ปุ่ม Triangle ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4586s | Wall: 0.4588s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter) แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-085 play_booking_controls ข้อ 85
- Question: ปุ่ม Square ใน TEKKEN 8 ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4189s | Wall: 0.4192s
- Sources: game_controls_tekken8: https://gameinputdatabase.com/game/83
- Answer: TEKKEN 8 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### PBC-086 play_booking_controls ข้อ 86
- Question: D-Pad ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4442s | Wall: 0.4443s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### PBC-087 play_booking_controls ข้อ 87
- Question: L1 ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4518s | Wall: 0.452s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### PBC-088 play_booking_controls ข้อ 88
- Question: R1 ใน TEKKEN 8 ใช้ทำอะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4347s | Wall: 0.4349s
- Sources: TEKKEN 8: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง แนวเกม: เกมต่อสู้ 1v1 วิธีเล่นโดยสรุป: เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน เล่นไ...

### PBC-089 play_booking_controls ข้อ 89
- Question: Mario Kart Live ปุ่มจัดการแผนที่คืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls_no_current_game`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4123s | Wall: 0.4125s
- Sources: service_game_availability: https://esports.computing.psu.ac.th/
- Answer: ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Ma...

### PBC-090 play_booking_controls ข้อ 90
- Question: Mario Kart Live ปุ่มดูข้อมูลรถคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls_no_current_game`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3484s | Wall: 0.3486s
- Sources: service_game_availability: https://esports.computing.psu.ac.th/
- Answer: ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน เกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: Mario Kart 8 Deluxe, Mario Party Superstars, New Super Ma...

### PBC-091 play_booking_controls ข้อ 91
- Question: Mario Kart 8 ปุ่มเบรกคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3102s | Wall: 0.3103s
- Sources: game_controls_mariokart8deluxe: https://gameinputdatabase.com/game/57
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    B: เบรก / ถอยหลัง - แตะเพื่อเบรกชะลอความเร็ว หรือกดค้างไว้เมื่อรถหยุดนิ่งเพื่อขับถอยหลัง แหล่งข้อมูล: https://gameinputdatabase.com/game/57

### PBC-092 play_booking_controls ข้อ 92
- Question: Mario Kart 8 ปุ่มมองหลังคืออะไร
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.374s | Wall: 0.3741s
- Sources: game_controls_mariokart8deluxe: https://gameinputdatabase.com/game/57
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    B: เบรก / ถอยหลัง - แตะเพื่อเบรกชะลอความเร็ว หรือกดค้างไว้เมื่อรถหยุดนิ่งเพื่อขับถอยหลัง •    X: มองหลัง - หันมุมกล้องไปมองด้านหลังเพื่อเช็กระยะห่างของคู่แข่งหรือไอเทมที่ตามมา แหล่งข้อมูล: https://ga...

### PBC-093 play_booking_controls ข้อ 93
- Question: Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1174s | Wall: 0.1176s
- Sources: -
- Answer: Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน: •    Call of Duty: Modern Warfare III (PlayStation 5 Zone) •    Call of Duty: Warzone (PC Zone)  พิมพ์ต่อได้ เช่น `Call of Duty:...

### PBC-094 play_booking_controls ข้อ 94
- Question: Naruto X Boruto ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.4151s | Wall: 0.4152s
- Sources: game_controls_narutoxborutoultimateninjastormconnections: https://en.bandainamcoent.eu/naruto/news/5-tips-you-should-know-playing-naruto-x-boruto-ultimate-ninja-storm-connections
- Answer: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    LS (Left Stick): เคลื่อนที่ - บังคับทิศทางของตัวละคร •    RS (Right Stick) Left/Right: เปลี่ยนตัวละครหลัก - ดันซ้ายหรือขวาเพื่อสลับบังคับเพื่อนร่วมทีมทันที •    C...

### PBC-095 play_booking_controls ข้อ 95
- Question: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.372s | Wall: 0.3722s
- Sources: game_controls_overcooked2: https://volx.jp/overcooked-2-keyboard-controller-setting/
- Answer: Overcooked! 2 มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    Left Stick: เคลื่อนที่ - ควบคุมทิศทางเชฟ •    Square: หั่น / ขว้าง - หั่นวัตถุดิบหรือขว้างสิ่งของ •    Cross: หยิบ / วาง - หยิบหรือวางสิ่งของ •    Circle: พุ่งตัว - พุ่งตัวเพื่อเคลื่อนที่เร็ว •...

### PBC-096 play_booking_controls ข้อ 96
- Question: Super Smash Bros ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.423s | Wall: 0.4232s
- Sources: game_controls_supersmashbrosultimate: https://gameinputdatabase.com/game/46
- Answer: Super Smash Bros. Ultimate มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    L (Left Stick): เคลื่อนที่ - ใช้เดิน วิ่ง หรือย่อตัว รวมถึงกำหนดทิศทางการโจมตีท่าต่าง ๆ •    R (Right Stick): โจมตีสแมช - ก้านอนาล็อกขวาใช้สำหรับปล่อยท่า Smash Attack ไปตามทิศทางที่ดันอย...

### PBC-097 play_booking_controls ข้อ 97
- Question: It Takes Two ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.3619s | Wall: 0.3621s
- Sources: game_controls_ittakestwo: https://gameinputdatabase.com/game/90
- Answer: It Takes Two มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเคลื่อนที่และการเดินของตัวละคร •    L3 (Click Left Stick): วิ่งสปรินต์ - กดก้านอนาล็อกซ้ายลงไปเพื่อวิ่งสปรินต์ เพิ่มความเร็วในการเคลื่อนที่ •    R (Right...

### PBC-098 play_booking_controls ข้อ 98
- Question: Little Nightmares II ปุ่มทั้งหมดมีอะไรบ้าง
- Expected: game_controls_or_clarification
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Strategy: `rag/vector`
- Latency: 0.396s | Wall: 0.3961s
- Sources: game_controls_littlenightmaresii: https://gameinputdatabase.com/game/304
- Answer: Little Nightmares II มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดินและเคลื่อนที่ของตัวละคร •    R (Right Stick): มุมกล้อง - แพนมุมกล้องเพื่อดูสภาพแวดล้อม และใช้ควบคุมทิศทางของไฟฉาย •    Cross: กระโดด / ขว้าง /...

### PBC-099 play_booking_controls ข้อ 99
- Question: ถ้าไม่รู้ชื่อเกมแต่ถามปุ่ม ระบบควรถามกลับไหม
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1717s | Wall: 0.1719s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### PBC-100 play_booking_controls ข้อ 100
- Question: วิธีเล่นเกมที่ไม่อยู่ในรายการต้องตอบยังไง
- Expected: game_controls_or_clarification
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.1626s | Wall: 0.1627s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ หรือหมายถึงวิธีเล่นเกมไหน/วิธีเข้าใช้บริการ/จอง ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III ถ้าถามวิธีเล่น/ปุ่ม ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 เล่นยังไง` หรือ `Mario Kart...

### EGI-001 equipment_game_inside ข้อ 1
- Question: PC Zone มีอุปกรณ์อะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.2603s | Wall: 0.2605s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์ใน PC Zone: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) •    Gaming Monitor (10 Units) •    Gaming Keyboard •    Gaming Mouse •    Gaming Headset •    Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-002 equipment_game_inside ข้อ 2
- Question: PC Zone มีคอมกี่เครื่อง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2291s | Wall: 0.2292s
- Sources: equipment_gaming_pc: https://esports.phuket.psu.ac.th/home
- Answer: Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: •    เล่น VALORANT •    เล่น Counter-Strike 2 •    เล่น PUBG: BATTLEGROUNDS •    เล่น Call of Duty: W...

### EGI-003 equipment_game_inside ข้อ 3
- Question: PC Zone ใช้จออะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2345s | Wall: 0.2346s
- Sources: equipment_gaming_monitor: https://esports.phuket.psu.ac.th/home
- Answer: Gaming Monitor: จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: •    แสดงผลเกมและโปรแกรมบน PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-004 equipment_game_inside ข้อ 4
- Question: PC Zone มีเมาส์กับคีย์บอร์ดไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_target_ambiguous`
- Route: `games/game_availability_lookup`
- Strategy: `pipeline`
- Latency: 0.2024s | Wall: 0.2026s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### EGI-005 equipment_game_inside ข้อ 5
- Question: PC Zone มีหูฟังไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_target_ambiguous`
- Route: `games/game_availability_lookup`
- Strategy: `pipeline`
- Latency: 0.1251s | Wall: 0.1252s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### EGI-006 equipment_game_inside ข้อ 6
- Question: Cockpit Zone มีอุปกรณ์อะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3205s | Wall: 0.3207s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์ใน Cockpit Zone: Cockpit Zone •    Logitech G923 TRUEFORCE Racing Wheel (2 Units with Driving Force Shifter) •    Driving Force Shifter (2 Units with Logitech G923) •    Racezone Full Cockpit V3 (2 Units) •    Pulse Elite Wireless Headset (2 Units) •...

### EGI-007 equipment_game_inside ข้อ 7
- Question: Cockpit Zone มีพวงมาลัยรุ่นอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.253s | Wall: 0.2531s
- Sources: equipment_logitech_g923: https://esports.phuket.psu.ac.th/home
- Answer: Logitech G923 TRUEFORCE Racing Wheel: ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone จำนวน: 2 Units with Driving Force Shifter อยู่ที่: Cockpit Zone ใช้สำหรับ: •    เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว แหล่งข้อมูล: https://esports.phuket.p...

### EGI-008 equipment_game_inside ข้อ 8
- Question: Cockpit Zone มีทีวีกี่เครื่อง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2866s | Wall: 0.2867s
- Sources: equipment_tv_65: https://esports.phuket.psu.ac.th/home
- Answer: TV 65 นิ้ว: จอทีวีขนาด 65 นิ้วสำหรับแสดงภาพเกมขับรถใน Cockpit Zone จำนวน: 2 Units อยู่ที่: Cockpit Zone ใช้สำหรับ: •    แสดงผลเกม Gran Turismo 7 ใน Cockpit Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-009 equipment_game_inside ข้อ 9
- Question: Cockpit Zone เหมาะกับเกมอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_target_ambiguous`
- Route: `games/game_availability_lookup`
- Strategy: `pipeline`
- Latency: 0.1361s | Wall: 0.1362s
- Sources: -
- Answer: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### EGI-010 equipment_game_inside ข้อ 10
- Question: Cockpit Zone มีชุดขับรถกี่ชุด
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.3031s | Wall: 0.3032s
- Sources: equipment_racezone_cockpit_v3: https://esports.phuket.psu.ac.th/home
- Answer: Racezone Full Cockpit V3: ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ จำนวน: 2 Units อยู่ที่: Cockpit Zone ใช้สำหรับ: •    เล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-011 equipment_game_inside ข้อ 11
- Question: Nintendo Switch Zone มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.101s | Wall: 0.1012s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | home_equipment: https://esports.phuket.psu.ac.th/home | service_fee_image_2026: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | reservation: https://esports.computing.psu.ac.th/
- Answer: คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ Nintendo Switch Zone?  ข้อมูลย่อที่ยืนยันได้ตอนนี้: •    เกม: มี 18 เกม เช่น Animal Crossing: New Horizons, It Takes Two, Little Nightmares II, Luigi's Mansion 3 และอื่น ๆ | พิมพ์ `Nintendo Switch มีเกมอะไรบ้าง`...

### EGI-012 equipment_game_inside ข้อ 12
- Question: Nintendo Switch Zone มีทีวีขนาดเท่าไหร่
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `service_fee/service_fee_query`
- Strategy: `rag/vector`
- Latency: 0.6276s | Wall: 0.6278s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด service_fee ตอนนี้ครับ

### EGI-013 equipment_game_inside ข้อ 13
- Question: Nintendo Switch Zone มีโซฟากี่ตัว
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.29s | Wall: 0.2902s
- Sources: equipment_nintendo_switch_oled: https://esports.phuket.psu.ac.th/home
- Answer: Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: •    เล่น Mario Kart 8 Deluxe •    เล่น Overcooked 2 •    เล่น Super Smash Bros Ultimate •    เล่น Nintend...

### EGI-014 equipment_game_inside ข้อ 14
- Question: Nintendo Switch Zone มีเครื่อง Switch กี่เครื่อง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.3854s | Wall: 0.3856s
- Sources: equipment_nintendo_switch_oled: https://esports.phuket.psu.ac.th/home
- Answer: Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: •    เล่น Mario Kart 8 Deluxe •    เล่น Overcooked 2 •    เล่น Super Smash Bros Ultimate •    เล่น Nintend...

### EGI-015 equipment_game_inside ข้อ 15
- Question: Nintendo Switch Zone เล่นกับเพื่อนได้ไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.8984s | Wall: 0.8985s
- Sources: our_games_genre: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:  EA Sports FC 24 •    แนวเกม: เกมฟุตบอล •    เล่นได้ที่: PlayStation 5 Zone  Nintendo Switch Sports •    แนวเกม: เกมกีฬา Motion Control •    เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.phu...

### EGI-016 equipment_game_inside ข้อ 16
- Question: PlayStation 5 Zone มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.0566s | Wall: 0.0567s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | home_equipment: https://esports.phuket.psu.ac.th/home | service_fee_image_2026: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | reservation: https://esports.computing.psu.ac.th/
- Answer: คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PlayStation 5 Zone?  ข้อมูลย่อที่ยืนยันได้ตอนนี้: •    เกม: มี 26 เกม เช่น Beat Saber, Call of Duty: Modern Warfare III, Call of Duty: Warzone, Delta Force และอื่น ๆ | พิมพ์ `PS5 มีเกมอะไรบ้าง` •    อุปกรณ์: มี 1...

### EGI-017 equipment_game_inside ข้อ 17
- Question: PS5 Zone มีเครื่องกี่เครื่อง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2813s | Wall: 0.2814s
- Sources: equipment_playstation_5_slim: https://esports.phuket.psu.ac.th/home
- Answer: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive: เครื่องเกม PlayStation 5 สำหรับเล่นเกมคอนโซล และใช้เป็นฐานสำหรับ VR Zone บางชุด จำนวน: 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone อยู่ที่: PlayStation 5 Zone / VR Zone ใช้สำหรับ: •    เล่น Marvel's...

### EGI-018 equipment_game_inside ข้อ 18
- Question: PS5 Zone ใช้รุ่นอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2158s | Wall: 0.2159s
- Sources: equipment_playstation_5_slim: https://esports.phuket.psu.ac.th/home
- Answer: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive: เครื่องเกม PlayStation 5 สำหรับเล่นเกมคอนโซล และใช้เป็นฐานสำหรับ VR Zone บางชุด จำนวน: 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone อยู่ที่: PlayStation 5 Zone / VR Zone ใช้สำหรับ: •    เล่น Marvel's...

### EGI-019 equipment_game_inside ข้อ 19
- Question: PS5 Zone มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2335s | Wall: 0.2336s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้  PlayStation 5 #01-#02 (60 นาที, 1-2 คน) •    Call of Duty: Modern Warfare III •    Delta Force •    EA Sports FC 24 •    eFootball •    FINAL FANTASY XVI •    Fortnite •    God of War Ragnarok •    Hogwarts Legacy •...

### EGI-020 equipment_game_inside ข้อ 20
- Question: PS5 Zone เหมาะกับเกมแนวไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `games/game_catalog_lookup`
- Strategy: `rag/vector`
- Latency: 5.3305s | Wall: 5.3306s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### EGI-021 equipment_game_inside ข้อ 21
- Question: VR Zone มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.041s | Wall: 0.0411s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | home_equipment: https://esports.phuket.psu.ac.th/home | service_fee_image_2026: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | reservation: https://esports.computing.psu.ac.th/
- Answer: คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?  ข้อมูลย่อที่ยืนยันได้ตอนนี้: •    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง` •    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง...

### EGI-022 equipment_game_inside ข้อ 22
- Question: VR Zone มี PS5 กี่เครื่อง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.239s | Wall: 0.2391s
- Sources: equipment_sony_playstation_vr2: https://esports.phuket.psu.ac.th/home
- Answer: Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone จำนวน: 1 Unit อยู่ที่: VR Zone ใช้สำหรับ: •    เล่น Beat Saber •    เล่น Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-023 equipment_game_inside ข้อ 23
- Question: VR Zone ใช้แว่นรุ่นอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2134s | Wall: 0.2135s
- Sources: equipment_sony_playstation_vr2: https://esports.phuket.psu.ac.th/home
- Answer: Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone จำนวน: 1 Unit อยู่ที่: VR Zone ใช้สำหรับ: •    เล่น Beat Saber •    เล่น Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-024 equipment_game_inside ข้อ 24
- Question: VR Zone มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2344s | Wall: 0.2346s
- Sources: availability_vr_30: https://esports.computing.psu.ac.th/
- Answer: VR Station มีเกมที่ยืนยันได้ดังนี้ (รอบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน)  VR Station 30 นาที (30 นาที, 1-5 คน) •    Beat Saber •    Horizon Call of the Mountain •    Resident Evil 4 •    Resident Evil Village หมายเหตุ: VR Station แบบ 30 นาทีและ 1 ชั่ว...

### EGI-025 equipment_game_inside ข้อ 25
- Question: VR Zone เหมาะกับมือใหม่ไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:zone_suitability_fast_path`
- Route: `equipment/related_guidance`
- Strategy: `rag/vector`
- Latency: 0.4251s | Wall: 0.4252s
- Sources: home: https://esports.phuket.psu.ac.th/home | our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: VR Zone เหมาะกับมือใหม่ที่อยากลองประสบการณ์ VR ครับ •    แนะนำเริ่มจาก Beat Saber เพราะรูปแบบการเล่นเข้าใจง่ายกว่าเกมผจญภัย VR •    ควรให้เจ้าหน้าที่ช่วยแนะนำการใส่แว่นและคอนโทรลเลอร์ก่อนเริ่มเล่น เกมที่ยืนยันได้ในโซนนี้ •    Beat Saber: เกม VR Rhythm •    Hor...

### EGI-026 equipment_game_inside ข้อ 26
- Question: หน้า Home มีอุปกรณ์ทั้งหมดอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.7531s | Wall: 0.7532s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-027 equipment_game_inside ข้อ 27
- Question: อุปกรณ์บนหน้า Home แยกตามโซนให้หน่อย
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.372s | Wall: 0.3722s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-028 equipment_game_inside ข้อ 28
- Question: โซนไหนมีทีวีขนาด 86 นิ้ว
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2413s | Wall: 0.2415s
- Sources: equipment_tv_86: https://esports.phuket.psu.ac.th/home
- Answer: TV 86 นิ้ว: จอทีวีขนาด 86 นิ้วสำหรับเล่นเกม Nintendo Switch เป็นกลุ่ม จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: •    แสดงผลเกม Nintendo Switch เช่น Mario Kart, Overcooked, Super Smash Bros และ Switch Sports แหล่งข้อมูล: https://esports.phuket.psu....

### EGI-029 equipment_game_inside ข้อ 29
- Question: โซนไหนมีทีวี 65 นิ้ว
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.2735s | Wall: 0.2736s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-030 equipment_game_inside ข้อ 30
- Question: โซนไหนมี PlayStation VR2
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2192s | Wall: 0.2193s
- Sources: equipment_sony_playstation_vr2: https://esports.phuket.psu.ac.th/home
- Answer: Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone จำนวน: 1 Unit อยู่ที่: VR Zone ใช้สำหรับ: •    เล่น Beat Saber •    เล่น Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-031 equipment_game_inside ข้อ 31
- Question: โซนไหนมี Logitech G923
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2509s | Wall: 0.251s
- Sources: equipment_logitech_g923: https://esports.phuket.psu.ac.th/home
- Answer: Logitech G923 TRUEFORCE Racing Wheel: ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone จำนวน: 2 Units with Driving Force Shifter อยู่ที่: Cockpit Zone ใช้สำหรับ: •    เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว แหล่งข้อมูล: https://esports.phuket.p...

### EGI-032 equipment_game_inside ข้อ 32
- Question: โซนไหนมี Gaming PC
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2095s | Wall: 0.2096s
- Sources: equipment_gaming_pc: https://esports.phuket.psu.ac.th/home
- Answer: Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: •    เล่น VALORANT •    เล่น Counter-Strike 2 •    เล่น PUBG: BATTLEGROUNDS •    เล่น Call of Duty: W...

### EGI-033 equipment_game_inside ข้อ 33
- Question: โซนไหนมีโซฟา
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.1917s | Wall: 0.1918s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-034 equipment_game_inside ข้อ 34
- Question: โซนไหนมี Racezone Full Cockpit
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2172s | Wall: 0.2173s
- Sources: equipment_racezone_cockpit_v3: https://esports.phuket.psu.ac.th/home
- Answer: Racezone Full Cockpit V3: ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ จำนวน: 2 Units อยู่ที่: Cockpit Zone ใช้สำหรับ: •    เล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-035 equipment_game_inside ข้อ 35
- Question: โซนไหนมี Pulse Elite Headset
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2697s | Wall: 0.2698s
- Sources: equipment_pulse_elite_headset: https://esports.phuket.psu.ac.th/home
- Answer: Pulse Elite Wireless Headset: หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone จำนวน: 2 Units อยู่ที่: Cockpit Zone ใช้สำหรับ: •    ฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-036 equipment_game_inside ข้อ 36
- Question: ถ้าอยากเล่นเกมขับรถควรใช้โซนไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 4.7917s | Wall: 4.7918s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### EGI-037 equipment_game_inside ข้อ 37
- Question: ถ้าอยากเล่นเกมกับเพื่อนหลายคนควรใช้โซนไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 5.2033s | Wall: 5.2035s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### EGI-038 equipment_game_inside ข้อ 38
- Question: ถ้าอยากลอง VR ต้องใช้อุปกรณ์อะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3018s | Wall: 0.3019s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์ใน VR Zone: PlayStation 5 Zone / VR Zone •    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone) VR Zone •    Sony PlayStation VR2 (1 Unit) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-039 equipment_game_inside ข้อ 39
- Question: ถ้าอยากเล่นเกม PC/FPS มีโซนไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 2.9533s | Wall: 2.9535s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### EGI-040 equipment_game_inside ข้อ 40
- Question: ถ้าอยากเล่นเกมปาร์ตี้มีโซนไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `reservation/booking_policy`
- Strategy: `rag/vector`
- Latency: 3.5057s | Wall: 3.5059s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### EGI-041 equipment_game_inside ข้อ 41
- Question: PS5 มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2785s | Wall: 0.2786s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้  PlayStation 5 #01-#02 (60 นาที, 1-2 คน) •    Call of Duty: Modern Warfare III •    Delta Force •    EA Sports FC 24 •    eFootball •    FINAL FANTASY XVI •    Fortnite •    God of War Ragnarok •    Hogwarts Legacy •...

### EGI-042 equipment_game_inside ข้อ 42
- Question: Nintendo Switch มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.3491s | Wall: 0.3494s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: Nintendo Switch Zone มีเกมที่ยืนยันได้ดังนี้  Nintendo Switch (1-2 Persons) (60 นาที, 1-2 คน) •    Pokémon Champions •    Animal Crossing: New Horizons •    It Takes Two •    Little Nightmares II •    Luigi's Mansion 3 •    Mario Kart 8 Deluxe •    Mario Party...

### EGI-043 equipment_game_inside ข้อ 43
- Question: PC มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2535s | Wall: 0.2537s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: PC Zone แยกรายการเกมตามเลขเครื่องดังนี้  PC #01-#02 (60 นาที, 1 คน) •    TEKKEN 8 •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    VALORANT หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone หมายเหตุ: PC #01-#02 และ PC #0...

### EGI-044 equipment_game_inside ข้อ 44
- Question: VR มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2462s | Wall: 0.2464s
- Sources: availability_vr_30: https://esports.computing.psu.ac.th/
- Answer: VR Station มีเกมที่ยืนยันได้ดังนี้ (รอบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน)  VR Station 30 นาที (30 นาที, 1-5 คน) •    Beat Saber •    Horizon Call of the Mountain •    Resident Evil 4 •    Resident Evil Village หมายเหตุ: VR Station แบบ 30 นาทีและ 1 ชั่ว...

### EGI-045 equipment_game_inside ข้อ 45
- Question: Cockpit มีเกมอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.2811s | Wall: 0.2812s
- Sources: availability_cockpit_01_02: https://esports.computing.psu.ac.th/
- Answer: Cockpit Zone มีเกมที่ยืนยันได้ดังนี้  Cockpit #01-#02 (60 นาที, 1 คน) •    Gran Turismo 7 หมายเหตุ: Cockpit มี 2 เครื่อง และใช้รายการเกมเดียวกัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-046 equipment_game_inside ข้อ 46
- Question: เกมทั้งหมดในศูนย์มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.4253s | Wall: 0.4254s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### EGI-047 equipment_game_inside ข้อ 47
- Question: เกมทั้งหมดมีกี่เกม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.3236s | Wall: 0.3238s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### EGI-048 equipment_game_inside ข้อ 48
- Question: เกมแนว Racing มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.3475s | Wall: 0.3476s
- Sources: availability_cockpit_01_02: https://esports.computing.psu.ac.th/
- Answer: Cockpit Zone มีเกมที่ยืนยันได้ดังนี้  Cockpit #01-#02 (60 นาที, 1 คน) •    Gran Turismo 7 หมายเหตุ: Cockpit มี 2 เครื่อง และใช้รายการเกมเดียวกัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-049 equipment_game_inside ข้อ 49
- Question: เกมแนว MOBA มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.456s | Wall: 0.4562s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### EGI-050 equipment_game_inside ข้อ 50
- Question: เกมแนว FPS มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.4301s | Wall: 0.4302s
- Sources: our_games_genre: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: เกมแนว FPS / เกมยิง ที่พบในรายการเกมที่ยืนยันได้:  Call of Duty: Modern Warfare III •    แนวเกม: เกมยิง FPS •    เล่นได้ที่: PlayStation 5 Zone  Call of Duty: Warzone •    แนวเกม: เกมยิง Battle Royale •    เล่นได้ที่: PC Zone  Counter-Strike 2 •    แนวเกม: เกม...

### EGI-051 equipment_game_inside ข้อ 51
- Question: เกมแนว Fighting มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.4901s | Wall: 0.4902s
- Sources: our_games_genre: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: เกมแนว Fighting / เกมต่อสู้ ที่พบในรายการเกมที่ยืนยันได้:  NARUTO X BORUTO Ultimate Ninja Storm Connections •    แนวเกม: เกมต่อสู้จากอนิเมะ •    เล่นได้ที่: PlayStation 5 Zone  Super Smash Bros Ultimate •    แนวเกม: เกมต่อสู้แบบ Platform Fighter •    เล่นได้ที...

### EGI-052 equipment_game_inside ข้อ 52
- Question: เกมแนว Party มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.4447s | Wall: 0.4448s
- Sources: our_games_genre: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: เกมแนว Party / Co-op ที่พบในรายการเกมที่ยืนยันได้:  It Takes Two •    แนวเกม: เกม Co-op Adventure •    เล่นได้ที่: Nintendo Switch Zone  Mario Kart 8 Deluxe •    แนวเกม: เกมแข่งรถ Party Racing •    เล่นได้ที่: Nintendo Switch Zone  Mario Party Superstars •...

### EGI-053 equipment_game_inside ข้อ 53
- Question: เกมแนว Rhythm มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_genre_list`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.4557s | Wall: 0.4558s
- Sources: our_games_genre: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: เกมแนว Rhythm / เกมจังหวะ ที่พบในรายการเกมที่ยืนยันได้:  Beat Saber •    แนวเกม: เกม VR Rhythm •    เล่นได้ที่: VR Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### EGI-054 equipment_game_inside ข้อ 54
- Question: เกมแนว Survival มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_target_unknown`
- Route: `games/game_availability_lookup`
- Strategy: `pipeline`
- Latency: 0.1807s | Wall: 0.1808s
- Sources: -
- Answer: ยังไม่พบชื่อเกมที่ตรงกับข้อมูลที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ กรุณาตรวจสอบชื่อเกมหรือพิมพ์ชื่อเกมที่ต้องการถามอีกครั้ง

### EGI-055 equipment_game_inside ข้อ 55
- Question: VALORANT เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3038s | Wall: 0.3038s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ VALORANT เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-056 equipment_game_inside ข้อ 56
- Question: CS2 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3045s | Wall: 0.3046s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Counter-Strike 2 เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-057 equipment_game_inside ข้อ 57
- Question: PUBG เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3282s | Wall: 0.3283s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ PUBG: BATTLEGROUNDS เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-058 equipment_game_inside ข้อ 58
- Question: Warzone เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.455s | Wall: 0.4551s
- Sources: availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Call of Duty: Warzone เล่นได้ที่ PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-059 equipment_game_inside ข้อ 59
- Question: League of Legends เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3985s | Wall: 0.3987s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_pc_03_10: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ League of Legends เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-060 equipment_game_inside ข้อ 60
- Question: TEKKEN 8 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3493s | Wall: 0.3494s
- Sources: availability_pc_01_02: https://esports.computing.psu.ac.th/ | availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ TEKKEN 8 เล่นได้ที่ PC Zone - PC #01-#02, PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-061 equipment_game_inside ข้อ 61
- Question: Spider-Man 2 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3273s | Wall: 0.3275s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Marvel's Spider-Man 2 เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-062 equipment_game_inside ข้อ 62
- Question: Fortnite เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.345s | Wall: 0.3451s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Fortnite เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-063 equipment_game_inside ข้อ 63
- Question: God of War Ragnarok เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.399s | Wall: 0.3991s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ God of War Ragnarok เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-064 equipment_game_inside ข้อ 64
- Question: Overcooked 2 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3045s | Wall: 0.3047s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Overcooked! 2 เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-065 equipment_game_inside ข้อ 65
- Question: Gran Turismo 7 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3776s | Wall: 0.3777s
- Sources: availability_cockpit_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Gran Turismo 7 เล่นได้ที่ Cockpit Zone - Cockpit #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-066 equipment_game_inside ข้อ 66
- Question: Beat Saber เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3399s | Wall: 0.3401s
- Sources: availability_vr_30: https://esports.computing.psu.ac.th/ | availability_vr_60: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Beat Saber เล่นได้ที่ VR Zone - VR Station 30 นาที, VR Zone - VR Station 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-067 equipment_game_inside ข้อ 67
- Question: It Takes Two เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3247s | Wall: 0.3248s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ It Takes Two เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-068 equipment_game_inside ข้อ 68
- Question: Little Nightmares II เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4035s | Wall: 0.4036s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Little Nightmares II เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-069 equipment_game_inside ข้อ 69
- Question: Monster Hunter Rise เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4057s | Wall: 0.4059s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Monster Hunter Rise เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-070 equipment_game_inside ข้อ 70
- Question: EA Sports FC 24 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3645s | Wall: 0.3649s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ EA Sports FC 24 เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-071 equipment_game_inside ข้อ 71
- Question: Final Fantasy XVI เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3659s | Wall: 0.366s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ FINAL FANTASY XVI เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-072 equipment_game_inside ข้อ 72
- Question: Hogwarts Legacy เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4133s | Wall: 0.4135s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Hogwarts Legacy เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-073 equipment_game_inside ข้อ 73
- Question: Naruto X Boruto เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4256s | Wall: 0.4257s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ NARUTO X BORUTO Ultimate Ninja Storm Connections เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-074 equipment_game_inside ข้อ 74
- Question: Resident Evil 4 เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.3337s | Wall: 0.3338s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/ | availability_vr_30: https://esports.computing.psu.ac.th/ | availability_vr_60: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Resident Evil 4 เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02, VR Zone - VR Station 30 นาที, VR Zone - VR Station 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-075 equipment_game_inside ข้อ 75
- Question: Resident Evil Village เล่นได้ที่ไหน
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.4074s | Wall: 0.4076s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/ | availability_vr_30: https://esports.computing.psu.ac.th/ | availability_vr_60: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Resident Evil Village เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02, VR Zone - VR Station 30 นาที, VR Zone - VR Station 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-076 equipment_game_inside ข้อ 76
- Question: The Last of Us มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:no_answer`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.6335s | Wall: 0.6337s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### EGI-077 equipment_game_inside ข้อ 77
- Question: Uncharted มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3003s | Wall: 0.3004s
- Sources: availability_ps5_01_02: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Uncharted: Legacy of Thieves Collection เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-078 equipment_game_inside ข้อ 78
- Question: Mario Kart 8 Deluxe มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.321s | Wall: 0.3211s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Mario Kart 8 Deluxe เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-079 equipment_game_inside ข้อ 79
- Question: Mario Kart Live Home Circuit มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3731s | Wall: 0.3733s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Mario Kart 8 Deluxe เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-080 equipment_game_inside ข้อ 80
- Question: Super Smash Bros Ultimate มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3437s | Wall: 0.3439s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Super Smash Bros Ultimate เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-081 equipment_game_inside ข้อ 81
- Question: Nintendo Switch Sports มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.2573s | Wall: 0.2574s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Nintendo Switch Sports เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-082 equipment_game_inside ข้อ 82
- Question: Animal Crossing มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.2985s | Wall: 0.2986s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Animal Crossing: New Horizons เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-083 equipment_game_inside ข้อ 83
- Question: Luigi's Mansion 3 มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.322s | Wall: 0.3222s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Luigi's Mansion 3 เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-084 equipment_game_inside ข้อ 84
- Question: Mario Party Superstars มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3661s | Wall: 0.3663s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Mario Party Superstars เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-085 equipment_game_inside ข้อ 85
- Question: Moving Out 2 มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.2713s | Wall: 0.2714s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Moving Out 2 เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-086 equipment_game_inside ข้อ 86
- Question: Super Mario Odyssey มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3422s | Wall: 0.3423s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Super Mario Odyssey เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-087 equipment_game_inside ข้อ 87
- Question: Zelda Breath of the Wild มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.3664s | Wall: 0.3665s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ The Legend of Zelda: Breath of The Wild เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-088 equipment_game_inside ข้อ 88
- Question: Ring Fit Adventure มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.339s | Wall: 0.3392s
- Sources: availability_nintendo_1_2: https://esports.computing.psu.ac.th/ | availability_nintendo_1_4: https://esports.computing.psu.ac.th/
- Answer: ได้ครับ Ring Fit Adventure เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### EGI-089 equipment_game_inside ข้อ 89
- Question: Minecraft มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:games_known_unsupported_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.7194s | Wall: 0.7196s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ  ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •...

### EGI-090 equipment_game_inside ข้อ 90
- Question: Roblox มีไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:games_known_unsupported_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.4847s | Wall: 0.4849s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบ Roblox ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ  ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •...

### EGI-091 equipment_game_inside ข้อ 91
- Question: ROV มีให้เล่นในศูนย์ไหม
- Expected: in_kb_or_catalog
- Mode: `pipeline:games_known_unsupported_fast_path`
- Route: `games/game_availability_lookup`
- Strategy: `rag/vector`
- Latency: 0.4309s | Wall: 0.431s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games | Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบ RoV / Arena of Valor ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์ ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ  ตอนนี้มีเก...

### EGI-092 equipment_game_inside ข้อ 92
- Question: เกมไหนยังไม่มีข้อมูลบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_games_catalog`
- Route: `games/list`
- Strategy: `rag/vector`
- Latency: 0.3619s | Wall: 0.3621s
- Sources: our_games: https://esports.phuket.psu.ac.th/Services/our-games
- Answer: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    TEKKEN 8 •    VALORANT  PlayStation 5 Zone (17 เกม) •    Call of Duty: Modern Warfare III •    Delt...

### EGI-093 equipment_game_inside ข้อ 93
- Question: เกมไหนมีข้อมูลปุ่มครบ
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0825s | Wall: 0.0826s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### EGI-094 equipment_game_inside ข้อ 94
- Question: เกมที่เล่นได้บนทั้ง PS5 และ Nintendo มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3778s | Wall: 0.3779s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์ใน PlayStation 5 Zone: PlayStation 5 Zone / VR Zone •    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-095 equipment_game_inside ข้อ 95
- Question: เกมไหนเล่นได้ทั้ง PC และ PS5
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3186s | Wall: 0.3188s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์ใน PC Zone: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) •    Gaming Monitor (10 Units) •    Gaming Keyboard •    Gaming Mouse •    Gaming Headset •    Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-096 equipment_game_inside ข้อ 96
- Question: เกมสำหรับเล่นกับเพื่อนมีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3546s | Wall: 0.3547s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-097 equipment_game_inside ข้อ 97
- Question: เกมสำหรับเด็กหรือมือใหม่มีอะไรบ้าง
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3886s | Wall: 0.3888s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### EGI-098 equipment_game_inside ข้อ 98
- Question: เกมที่ใช้พวงมาลัยมีอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2102s | Wall: 0.2103s
- Sources: equipment_logitech_g923: https://esports.phuket.psu.ac.th/home
- Answer: Logitech G923 TRUEFORCE Racing Wheel: ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone จำนวน: 2 Units with Driving Force Shifter อยู่ที่: Cockpit Zone ใช้สำหรับ: •    เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว แหล่งข้อมูล: https://esports.phuket.p...

### EGI-099 equipment_game_inside ข้อ 99
- Question: เกมที่ต้องใช้ VR มีอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:structured_equipment_item`
- Route: `equipment/equipment_item_lookup`
- Strategy: `rag/vector`
- Latency: 0.2548s | Wall: 0.255s
- Sources: equipment_sony_playstation_vr2: https://esports.phuket.psu.ac.th/home
- Answer: Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone จำนวน: 1 Unit อยู่ที่: VR Zone ใช้สำหรับ: •    เล่น Beat Saber •    เล่น Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### EGI-100 equipment_game_inside ข้อ 100
- Question: เกมที่ใช้จอย PS5 มีอะไร
- Expected: in_kb_or_catalog
- Mode: `pipeline:game_control_missing_game_context`
- Route: `games/game_control_lookup`
- Strategy: `pipeline`
- Latency: 0.0866s | Wall: 0.0867s
- Sources: -
- Answer: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### OOS-001 out_of_scope ข้อ 1
- Question: สอนทำข้าวผัดแบบง่ายๆ
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `rag/vector`
- Latency: 0.2724s | Wall: 0.2725s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-002 out_of_scope ข้อ 2
- Question: วันนี้ฝนจะตกไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.1675s | Wall: 0.1676s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-003 out_of_scope ข้อ 3
- Question: ช่วยแปลประโยคนี้เป็นอังกฤษได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2556s | Wall: 0.2557s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-004 out_of_scope ข้อ 4
- Question: สูตรคำนวณพื้นที่วงกลมคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `service_fee/service_fee_query`
- Strategy: `rag/vector`
- Latency: 0.3194s | Wall: 0.3195s
- Sources: curated_service_fee_pc_unknown: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_general_adult::th::text: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_general_student::th::text: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- Answer: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-S...

### OOS-005 out_of_scope ข้อ 5
- Question: ขอไอเดียตั้งชื่อร้านกาแฟ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2215s | Wall: 0.2216s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-006 out_of_scope ข้อ 6
- Question: ช่วยเขียนคำอวยพรวันเกิดให้เพื่อน
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2472s | Wall: 0.2474s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-007 out_of_scope ข้อ 7
- Question: วิธีลดน้ำหนักที่ปลอดภัยควรเริ่มยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `rules/studio_rules`
- Strategy: `rag/vector`
- Latency: 0.416s | Wall: 0.4161s
- Sources: rule_en_report_problem_natural::th::answer: https://esports.computing.psu.ac.th/ | rule_report_problem::th::answer: https://esports.computing.psu.ac.th/ | curated_rule_trash_personal_items: https://esports.computing.psu.ac.th/
- Answer: หากพบปัญหาการใช้งาน พฤติกรรมไม่เหมาะสม หรือข้อกังวล ควรแจ้งเจ้าหน้าที่ทันที แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-008 out_of_scope ข้อ 8
- Question: อาการปวดหัวบ่อยควรทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2445s | Wall: 0.2448s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-009 out_of_scope ข้อ 9
- Question: หุ้นตัวไหนดีวันนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.1838s | Wall: 0.1839s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-010 out_of_scope ข้อ 10
- Question: ราคาทองวันนี้เท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:freshness_live_source_required`
- Route: `no_answer/freshness_live_source_required`
- Strategy: `pipeline`
- Latency: 0.0737s | Wall: 0.0739s
- Sources: -
- Answer: ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

### OOS-011 out_of_scope ข้อ 11
- Question: ข่าวการเมืองล่าสุดคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:freshness_live_source_required`
- Route: `no_answer/freshness_live_source_required`
- Strategy: `pipeline`
- Latency: 0.0268s | Wall: 0.0269s
- Sources: -
- Answer: ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

### OOS-012 out_of_scope ข้อ 12
- Question: ใครเป็นนายกรัฐมนตรีตอนนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:freshness_live_source_required`
- Route: `no_answer/freshness_live_source_required`
- Strategy: `pipeline`
- Latency: 0.0388s | Wall: 0.0389s
- Sources: -
- Answer: ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

### OOS-013 out_of_scope ข้อ 13
- Question: ช่วยแต่งกลอนสั้นๆ เรื่องทะเล
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2443s | Wall: 0.2444s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-014 out_of_scope ข้อ 14
- Question: Python list comprehension คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3142s | Wall: 0.3143s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-015 out_of_scope ข้อ 15
- Question: JavaScript promise คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2376s | Wall: 0.2377s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-016 out_of_scope ข้อ 16
- Question: ช่วยเขียน SQL select เบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2968s | Wall: 0.2969s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-017 out_of_scope ข้อ 17
- Question: วิธีสมัคร Gmail ทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2442s | Wall: 0.2443s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-018 out_of_scope ข้อ 18
- Question: แนะนำโน้ตบุ๊กเล่นเกมหน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2183s | Wall: 0.2184s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-019 out_of_scope ข้อ 19
- Question: iPhone รุ่นไหนคุ้มสุด
- Expected: general_llm_or_decline
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.3596s | Wall: 0.3598s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### OOS-020 out_of_scope ข้อ 20
- Question: เที่ยวภูเก็ต 1 วันไปไหนดี
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2411s | Wall: 0.2412s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-021 out_of_scope ข้อ 21
- Question: ร้านอาหารใกล้ฉันมีอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `rag/vector`
- Latency: 0.2618s | Wall: 0.2619s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-022 out_of_scope ข้อ 22
- Question: แผนที่ไปสนามบินภูเก็ต
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.2195s | Wall: 0.2196s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-023 out_of_scope ข้อ 23
- Question: วิธีทำพาสปอร์ต
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1709s | Wall: 0.171s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-024 out_of_scope ข้อ 24
- Question: ต่อภาษีรถต้องทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2177s | Wall: 0.2179s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-025 out_of_scope ข้อ 25
- Question: ยื่นภาษีบุคคลธรรมดายังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.23s | Wall: 0.2301s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-026 out_of_scope ข้อ 26
- Question: เขียน resume ภาษาอังกฤษยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2735s | Wall: 0.2737s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-027 out_of_scope ข้อ 27
- Question: ช่วยซ้อมสัมภาษณ์งานหน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2168s | Wall: 0.2169s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-028 out_of_scope ข้อ 28
- Question: คำว่า resilience แปลว่าอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2901s | Wall: 0.2903s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-029 out_of_scope ข้อ 29
- Question: ทำไมท้องฟ้าถึงเป็นสีฟ้า
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2014s | Wall: 0.2015s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-030 out_of_scope ข้อ 30
- Question: โลกร้อนเกิดจากอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.1744s | Wall: 0.1745s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-031 out_of_scope ข้อ 31
- Question: AI คืออะไรแบบง่ายๆ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1839s | Wall: 0.184s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-032 out_of_scope ข้อ 32
- Question: LLM ทำงานยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1743s | Wall: 0.1744s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-033 out_of_scope ข้อ 33
- Question: RAG คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1734s | Wall: 0.1735s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-034 out_of_scope ข้อ 34
- Question: Docker คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1535s | Wall: 0.1536s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-035 out_of_scope ข้อ 35
- Question: Git commit กับ push ต่างกันยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.3098s | Wall: 0.31s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-036 out_of_scope ข้อ 36
- Question: Vercel คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1599s | Wall: 0.16s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-037 out_of_scope ข้อ 37
- Question: Neon database คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2009s | Wall: 0.2011s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-038 out_of_scope ข้อ 38
- Question: SQLite ต่างจาก Postgres ยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2626s | Wall: 0.2628s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-039 out_of_scope ข้อ 39
- Question: ช่วยวางแผนอ่านหนังสือสอบ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2274s | Wall: 0.2276s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-040 out_of_scope ข้อ 40
- Question: วิธีจัดการเวลาให้ดีขึ้น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.213s | Wall: 0.2131s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-041 out_of_scope ข้อ 41
- Question: วิธีนอนให้หลับง่าย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1727s | Wall: 0.1728s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-042 out_of_scope ข้อ 42
- Question: ควรดื่มน้ำวันละเท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:protected_food_consumption`
- Route: `rules/food_consumption`
- Strategy: `pipeline`
- Latency: 0.0633s | Wall: 0.0634s
- Sources: rule_food_drink: https://esports.computing.psu.ac.th/
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-043 out_of_scope ข้อ 43
- Question: อาหารเช้าควรกินอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:protected_food_consumption`
- Route: `rules/food_consumption`
- Strategy: `pipeline`
- Latency: 0.0179s | Wall: 0.018s
- Sources: rule_food_drink: https://esports.computing.psu.ac.th/
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-044 out_of_scope ข้อ 44
- Question: วิธีปลูกต้นไม้ในห้อง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1768s | Wall: 0.1769s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-045 out_of_scope ข้อ 45
- Question: วิธีดูแลกล้องถ่ายรูปเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2249s | Wall: 0.225s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-046 out_of_scope ข้อ 46
- Question: วิธีดูแลคอมไม่ให้ช้า
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1465s | Wall: 0.1466s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-047 out_of_scope ข้อ 47
- Question: ทำไม Wi-Fi ช้า
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1644s | Wall: 0.1645s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-048 out_of_scope ข้อ 48
- Question: วิธีตั้งรหัสผ่านให้ปลอดภัย
- Expected: general_llm_or_decline
- Mode: `pipeline:boundary_no_answer_sensitive`
- Route: `no_answer/boundary_no_answer_sensitive`
- Strategy: `no_answer`
- Latency: 0.031s | Wall: 0.0311s
- Sources: -
- Answer: ขออภัยครับ ผมไม่มีช่องทางให้เบอร์โทรส่วนตัวหรือข้อมูลส่วนตัวเจ้าหน้าที่ และไม่สามารถเปิดเผยรหัสผ่านหรือพิกัดส่วนตัวได้ครับ

### OOS-049 out_of_scope ข้อ 49
- Question: phishing คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1784s | Wall: 0.1784s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-050 out_of_scope ข้อ 50
- Question: ช่วยคิด caption ลง Instagram
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2601s | Wall: 0.2602s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-051 out_of_scope ข้อ 51
- Question: เขียน bio โปรไฟล์ให้หน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2565s | Wall: 0.2566s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-052 out_of_scope ข้อ 52
- Question: ช่วยสรุปนิยายที่ฉันชอบได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2226s | Wall: 0.2227s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-053 out_of_scope ข้อ 53
- Question: วิธีทำบันทึกรายรับรายจ่าย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2236s | Wall: 0.2237s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-054 out_of_scope ข้อ 54
- Question: ขอไอเดียของขวัญรับปริญญา
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.2724s | Wall: 0.2725s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-055 out_of_scope ข้อ 55
- Question: ช่วยตั้งชื่อช่อง YouTube
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.2403s | Wall: 0.2406s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-056 out_of_scope ข้อ 56
- Question: วิธีฝึกวาดรูปเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2243s | Wall: 0.2245s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-057 out_of_scope ข้อ 57
- Question: วันนี้มีบอลคู่ไหน
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.1575s | Wall: 0.1576s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-058 out_of_scope ข้อ 58
- Question: ตาราง NBA วันนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.1711s | Wall: 0.1712s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-059 out_of_scope ข้อ 59
- Question: ผลพรีเมียร์ลีกล่าสุด
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 0.7385s | Wall: 0.7386s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-060 out_of_scope ข้อ 60
- Question: ค่าเงิน USD เป็น THB เท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.3061s | Wall: 0.3063s
- Sources: -
- Answer: ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

### OOS-061 out_of_scope ข้อ 61
- Question: Bitcoin ราคาเท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Strategy: `pipeline`
- Latency: 0.1268s | Wall: 0.1269s
- Sources: -
- Answer: ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

### OOS-062 out_of_scope ข้อ 62
- Question: ช่วยวางแผนเที่ยวญี่ปุ่น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2068s | Wall: 0.2069s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-063 out_of_scope ข้อ 63
- Question: ขอ checklist จัดกระเป๋าเดินทาง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3118s | Wall: 0.3119s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-064 out_of_scope ข้อ 64
- Question: วิธีจองตั๋วเครื่องบินราคาถูก
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `service_fee/service_fee_query`
- Strategy: `rag/vector`
- Latency: 0.374s | Wall: 0.3741s
- Sources: curated_service_fee_pc_unknown: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_service_fee_2026_full_table::th::text: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_psu_student_staff::th::text: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- Answer: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-S...

### OOS-065 out_of_scope ข้อ 65
- Question: ประกันสุขภาพเลือกยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2061s | Wall: 0.2062s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-066 out_of_scope ข้อ 66
- Question: บัตรเครดิตใบไหนดี
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1653s | Wall: 0.1654s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-067 out_of_scope ข้อ 67
- Question: กู้ซื้อบ้านต้องเตรียมอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.2154s | Wall: 0.2155s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-068 out_of_scope ข้อ 68
- Question: ดอกเบี้ยทบต้นคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2028s | Wall: 0.2029s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-069 out_of_scope ข้อ 69
- Question: วิธีเริ่มลงทุนกองทุนรวม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2261s | Wall: 0.2262s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-070 out_of_scope ข้อ 70
- Question: ช่วยเขียนอีเมลขอลางาน
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.1985s | Wall: 0.1986s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-071 out_of_scope ข้อ 71
- Question: ช่วยเขียนประกาศรับสมัครงาน
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/detail`
- Strategy: `fastpath/rulebase`
- Latency: 0.2126s | Wall: 0.2127s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-072 out_of_scope ข้อ 72
- Question: ช่วยทำสคริปต์นำเสนอ 3 นาที
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.2223s | Wall: 0.2224s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-073 out_of_scope ข้อ 73
- Question: สอนทำ PowerPoint ให้น่าสนใจ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3003s | Wall: 0.3004s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-074 out_of_scope ข้อ 74
- Question: วิธีอ่านงบการเงินเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2147s | Wall: 0.2148s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-075 out_of_scope ข้อ 75
- Question: เศรษฐกิจเงินเฟ้อคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2057s | Wall: 0.2058s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-076 out_of_scope ข้อ 76
- Question: ประวัติศาสตร์สงครามโลกครั้งที่สอง
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `rag/vector`
- Latency: 0.2787s | Wall: 0.2789s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-077 out_of_scope ข้อ 77
- Question: ดาวอังคารอยู่ไกลแค่ไหน
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2037s | Wall: 0.2039s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-078 out_of_scope ข้อ 78
- Question: ระบบสุริยะมีดาวอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2174s | Wall: 0.2175s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-079 out_of_scope ข้อ 79
- Question: ทำไมทะเลถึงเค็ม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.157s | Wall: 0.1572s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-080 out_of_scope ข้อ 80
- Question: ช่วยแก้โจทย์คณิตสมการกำลังสอง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2317s | Wall: 0.2318s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-081 out_of_scope ข้อ 81
- Question: วิธีจำศัพท์อังกฤษ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.1726s | Wall: 0.1727s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-082 out_of_scope ข้อ 82
- Question: ฝึกพูดอังกฤษด้วยตัวเองยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2376s | Wall: 0.2377s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-083 out_of_scope ข้อ 83
- Question: แปลไทยเป็นญี่ปุ่นได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2077s | Wall: 0.2078s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-084 out_of_scope ข้อ 84
- Question: ช่วยตรวจแกรมมาร์ประโยคอังกฤษ
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2413s | Wall: 0.2414s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-085 out_of_scope ข้อ 85
- Question: ทำไมคอมเปิดไม่ติด
- Expected: general_llm_or_decline
- Mode: `pipeline:structured_schedule`
- Route: `schedule/schedule_query`
- Strategy: `rag/vector`
- Latency: 0.2136s | Wall: 0.2137s
- Sources: reservation_schedule: https://esports.computing.psu.ac.th/
- Answer: เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00  รายละเอียดจากตาราง: •    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open •    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open •    วันพุธ: Morni...

### OOS-086 out_of_scope ข้อ 86
- Question: Windows update ค้างทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2767s | Wall: 0.2768s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-087 out_of_scope ข้อ 87
- Question: ลืมรหัสผ่าน Facebook ทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:boundary_no_answer_sensitive`
- Route: `no_answer/boundary_no_answer_sensitive`
- Strategy: `no_answer`
- Latency: 0.0829s | Wall: 0.0831s
- Sources: -
- Answer: ขออภัยครับ ผมไม่มีช่องทางให้เบอร์โทรส่วนตัวหรือข้อมูลส่วนตัวเจ้าหน้าที่ และไม่สามารถเปิดเผยรหัสผ่านหรือพิกัดส่วนตัวได้ครับ

### OOS-088 out_of_scope ข้อ 88
- Question: บัญชีโดนแฮกควรทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.235s | Wall: 0.2351s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-089 out_of_scope ข้อ 89
- Question: ทำ portfolio สมัครงานยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2623s | Wall: 0.2624s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-090 out_of_scope ข้อ 90
- Question: เรียนสาย data ต้องเริ่มจากอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:candidate_margin_clarification`
- Route: `clarification/candidate_margin_clarification`
- Strategy: `pipeline`
- Latency: 0.3357s | Wall: 0.3359s
- Sources: -
- Answer: ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### OOS-091 out_of_scope ข้อ 91
- Question: Data analyst ใช้เครื่องมืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.4633s | Wall: 0.4634s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### OOS-092 out_of_scope ข้อ 92
- Question: Machine learning ต่างจาก deep learning ยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3219s | Wall: 0.322s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-093 out_of_scope ข้อ 93
- Question: Prompt engineering คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2527s | Wall: 0.2528s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-094 out_of_scope ข้อ 94
- Question: ช่วยคิด business model ร้านชา
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2606s | Wall: 0.2607s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-095 out_of_scope ข้อ 95
- Question: วิธีทำแบบสอบถามออนไลน์
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2222s | Wall: 0.2224s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### OOS-096 out_of_scope ข้อ 96
- Question: ทำ infographic ด้วยเครื่องมืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Strategy: `rag/vector`
- Latency: 0.5935s | Wall: 0.5936s
- Sources: home_equipment: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### OOS-097 out_of_scope ข้อ 97
- Question: เพลงฮิตตอนนี้มีอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:freshness_live_source_required`
- Route: `no_answer/freshness_live_source_required`
- Strategy: `pipeline`
- Latency: 0.0292s | Wall: 0.0293s
- Sources: -
- Answer: ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

### OOS-098 out_of_scope ข้อ 98
- Question: หนังน่าดูปีนี้มีเรื่องอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:freshness_live_source_required`
- Route: `no_answer/freshness_live_source_required`
- Strategy: `pipeline`
- Latency: 0.0336s | Wall: 0.0337s
- Sources: -
- Answer: ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

### OOS-099 out_of_scope ข้อ 99
- Question: ช่วยคิดเมนูอาหารเย็น
- Expected: general_llm_or_decline
- Mode: `pipeline:boundary_no_answer_out_of_scope`
- Route: `no_answer/boundary_no_answer_out_of_scope`
- Strategy: `no_answer`
- Latency: 0.0329s | Wall: 0.033s
- Sources: -
- Answer: ตอนนี้ผมตอบได้เฉพาะข้อมูลของ PSU Esports Studio - Phuket เช่น เกม ปุ่ม อุปกรณ์ ราคา การจอง ตารางเวลา กฎ และสมาชิกครับ

### OOS-100 out_of_scope ข้อ 100
- Question: ทำกาแฟลาเต้เองที่บ้านยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.238s | Wall: 0.2381s
- Sources: -
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
