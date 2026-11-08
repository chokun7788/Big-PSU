# R118 — ข้อมูลที่ยังจำกัดคำตอบ

ตรวจ snapshot เดียวกับ R117 revision04 โดยไม่แก้ source หรือ approvals การนับช่อง not_applicable/unknown/conflicted ไม่ใช่การนับคำตอบผิดหรือจำนวนคำถามที่ตอบไม่ได้

- Records 806; projected facts ก่อนเพิ่ม metadata R118 1444
- Person public_scope states: {'unknown': 25}
- Rate calculation_rule states: {'unknown': 18, 'known': 6}
- เกมที่มีบริการยืนยัน 42; มีเส้นทางยืนยันถึงโซน 23; ขาดเส้นทาง 19

## เกมที่ยืนยันบริการได้แต่ยังเชื่อมไปถึงโซนไม่ได้

| เกม | บริการที่มีหลักฐาน |
|---|---|
| Animal Crossing: New Horizons | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Beat Saber | VR Station 30 นาที; VR Station 1 ชั่วโมง |
| Horizon Call of the Mountain | VR Station 30 นาที; VR Station 1 ชั่วโมง |
| It Takes Two | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Little Nightmares II | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Luigi's Mansion 3 | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Mario Kart 8 Deluxe | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Mario Party Superstars | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Monster Hunter Rise | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Moving Out 2 | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| New Super Mario Bros. U Deluxe | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Overcooked 2 | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Ring Fit Adventure | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Super Mario Odyssey | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Super Smash Bros Ultimate | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Nintendo Switch Sports | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| The Legend of Zelda: Breath of the Wild | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Overcooked! | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |
| Pokémon Champions | Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) |

## ความหมายต่อการแก้ Flow

1. ห้ามเอาชื่อ platform ที่ตรงกับชื่อโซนมาแทน relation ที่ขาด ควรเติม service.resource_ids และ resource.zone_id พร้อมหลักฐานถ้ามีข้อมูลต้นฉบับยืนยันจริง
2. public_scope ต้องมาจากสถานะเจ้าของข้อมูลที่ถูกต้อง ตัวอ่าน inverse ช่วยหาเจอ แต่ไม่ใช่ใบอนุญาตเผยแพร่
3. สูตรคำนวณต้องตรงหน่วย/ช่วงเวลา/กลุ่ม การมีราคา 60 นาทีไม่รับรองว่าจะคิด 30 นาทีหรือหลายชั่วโมงแบบ linear เสมอ
4. calendar open_periods ที่ขัดแย้งไม่ใช่ bookable_periods ไม่มีรายการจองไม่เท่ากับศูนย์ปิด
5. ชื่อฉบับเกมและฉบับการแข่งขันต้องยืนยัน ID ให้ตรง ห้ามเลือกอีก edition เพราะมีข้อมูลมากกว่า
6. กรณี keyword/clause fail ให้ดู source และคำตอบรายข้อก่อนนับเป็น content failure

รายการทุกช่องและ source evidence ดู SOURCE_GAPS.json โดย source ที่ใช้เป็น draft snapshot ไม่ใช่สถานะเผยแพร่ production