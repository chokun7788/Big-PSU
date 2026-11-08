# R117 — เพิ่มการเข้าใจบริบทและเจตนาก่อนอ่านข้อมูล

## สิ่งที่ปรับแล้ว

1. วิเคราะห์ทั้งคำถามเป็น operation + domain + facet + target + constraints ก่อนเลือก reader ไม่เริ่มจากชื่อเกมหรือคำสำคัญอย่างเดียว
2. เก็บบริบท current turn ก่อน explicit_request_focus ตัดประโยคเกริ่น เพื่อรักษาชื่อเกม รายการแข่ง และกลุ่มผู้ใช้ที่เกี่ยวข้อง
3. ใช้ QueryPlanTask/operations และตัวตรวจแผนจาก Flow เดิม ร่วมกับ heuristic และ control/competition frames เดิมเป็นตัวตรวจอิสระ ไม่ยกคำตอบจากฐานเก่ามาใช้
4. ตรวจ quote/target/เงื่อนไขกับข้อความจริง ผูกกลุ่มผู้ใช้กับ audience directory ปัจจุบัน และแปลงหน่วยภาษาที่ระบุ เช่น one hour เป็นหน่วยที่ตัวอ่านใช้ได้
5. ให้แผนใช้กับตัวอ่านจริง: list-all ปุ่มครบชุด, เกมไปโซนตาม graph, confirmed subset สำหรับหลายโซน, partial unit rates เมื่อกฎคำนวณยังขาด
6. แผนที่มีเจตนาชัดแต่ source/target ไม่รองรับจะไม่เปลี่ยนไปตอบข้อมูลคนละเรื่องผ่าน compatibility fallback พร้อมบันทึก diagnostic เมื่อ fallback มีผลลัพธ์
7. รักษา source/validity/permission guards และเพิ่ม public_scope guard ให้ domain reader สอดคล้องกับ complete_flow โดยไม่แก้ approvals

```text
คำถามและบริบทเต็ม → แผนความหมาย → ตรวจแผนกับกฎเดิม/ข้อความจริง
→ เลือกงานและหมวด → อ่าน field / set / relation → ตรวจหลักฐานและเงื่อนไข
→ ตอบตรงจุด หรือระบุส่วนที่ยังยืนยันไม่ได้
```

## ตรวจด้วยคำถามเดิมเท่านั้น

- ใช้ 48 unique keys จาก Full เดิม: 40 seeded regressions จาก 10 หมวดหลักและ 8 known failures ไม่เพิ่มคำถามใหม่
- ตรวจ 48 keys เดิมใน 3 revisions แรก รวม 144 HTTP attempts จากนั้น revision04 แก้การรับระยะเวลาที่โมเดลลืมส่งและข้อความถามเพิ่ม ตรวจซ้ำเฉพาะ 8 keys ที่เกี่ยวข้อง รวมงานนี้ 152 HTTP attempts แต่มีคำถามไม่ซ้ำ 48 ข้อ ไม่ใช่ Full Test หรือ blind holdout
- ใช้ saved R115 ของ keys เดียวกัน ไม่รัน R115 หรือ Legacy ใหม่ Source/clock/locale/grade entries ตรงกับ saved R115 cohort นี้
- Contract checks 22/22 รวม malformed model output, source-bound slots, การอ่านครบทั้ง set, context frames, ระยะเวลาที่โมเดลลืมส่ง และการไม่ข้ามกฎคำนวณราคา

## ผลตรวจคำ/ข้อความที่คาดหวังในชุดพัฒนานี้

| รุ่น | Positive literal/clause grades | Requests ที่ผ่าน positive ทุกแถว |
|---|---:|---:|
| Saved R115 | 25/62 (40.32%) | 7/18 (38.89%) |
| R117 revision01 | 26/62 (41.94%) | 7/18 (38.89%) |
| R117 revision02 | 32/62 (51.61%) | 10/18 (55.56%) |
| R117 revision03 | 40/62 (64.52%) | 12/18 (66.67%) |

**รุ่นโค้ดสุดท้ายคือ revision04:** ตาราง 48 ข้อด้านบนเป็น revision03 ที่เก็บ code snapshot ไว้ครบ หลังแก้สุดท้ายตรวจเฉพาะ 8 ข้อที่กระทบ ไม่อ้างว่ามีผล 48 ข้อใหม่ของ revision04

ผล 8 ข้อที่ตรวจซ้ำด้วยเกณฑ์เดิม: saved R115 5/6 (83.33%); revision04 6/6 (100.00%) — ไม่ใช่คะแนน Full หรือ semantic accuracy

**ห้ามใช้ตารางนี้เป็นเปอร์เซ็นต์ความเข้าใจทุกคำถาม:** มีเพียง 18/48 requests ที่มี positive contracts รวม 62 grades; ชุดนี้เลือกบางข้อจาก failures ที่รู้แล้ว และเป็น development corpus ตัวตรวจ literal ยังอาจผ่านข้อความ unit rate แม้คำถาม total price ตอบได้เพียง partial จึงไม่ถือว่าทั้งคำถามตอบสมบูรณ์เพียงเพราะผ่าน keyword

ผลนี้ใช้เทียบกับ R115 บน 48 keys เท่านั้น ไม่เทียบเปอร์เซ็นต์ตรง ๆ กับ 67.90% ของ R116 ทั้ง 2,108 keys หรือ 96.46% ของชุด template ก่อนหน้า เพราะเป็นคนละ cohort/metric และไม่อ้างว่ารุ่นนี้เท่า Legacy แล้ว

## ตัวอย่างก่อน–หลัง พร้อมข้อจำกัด

### ปุ่มทั้งหมด: Warzone

What are all the buttons in Call of Duty: Warzone

**R115**

```text
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S1]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S2]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S5]
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S6]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S7]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S8]
```

**R117 revision04**

```text
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S1]
Call of Duty: Warzone / PlayStation / PS5 — Crouch/Prone/Slide: Circle — Press to change stance or slide your knee while running [S2]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Campaign, Multiplayer or Co-Op specific: D-Pad — Optional commands depending on game mode such as ping or kill streak [S5]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S6]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S7]
Call of Duty: Warzone / PlayStation / PS5 — Use Tactical Equipment: L1 — Use smoke grenades, flashbangs, or support devices [S8]
Call of Duty: Warzone / PlayStation / PS5 — Use Lethal Equipment: R1 — Use destruction explosives [S9]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S10]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S11]
Call of Duty: Warzone / PlayStation / PS5 — Sprint/Tactical Sprint/Steady Aim: L3 — Press to sprint or hold breath while aiming through scope [S12]
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S13]
```

**แผนที่ใช้**

```json
{
  "reason": "independent_context_frame",
  "tasks": [
    {
      "quote": "what are all the buttons in call of duty: warzone",
      "domain": "game_controls",
      "category": "C05",
      "operation": "list",
      "facet": "input_bindings",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "model_schema_ok": true,
  "independent_review": {
    "basis": "legacy_control_frame_and_current_source_target",
    "model_plan_accepted": true,
    "model_reason": "validated_interpretation_proposal",
    "prior_tasks": [
      {
        "quote": "what are all the buttons in call of duty: warzone",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "game_catalog",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "business_facts_added": false
  }
}
```

### ปุ่มทั้งหมด: God of War Ragnarök

God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง

**R115**

```text
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S3]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S4]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S5]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S6]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S7]
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S8]
```

**R117 revision03**

```text
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — พลังสปาร์ตัน: L3 + R3 — ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต [S3]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S4]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S5]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S6]
God of War Ragnarök / PlayStation / PS5 — ป้องกัน (กดค้าง): L1 (Hold) — ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic [S7]
God of War Ragnarök / PlayStation / PS5 — โจมตีเบา / รูนเบา / ขว้าง: R1 — โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1 [S8]
God of War Ragnarök / PlayStation / PS5 — โจมตีหนัก / รูนหนัก: R2 — โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1 [S9]
God of War Ragnarök / PlayStation / PS5 — เรียกขวานกลับ / ชาร์จพลังอาวุธ: Triangle — เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1 [S10]
God of War Ragnarök / PlayStation / PS5 — โต้ตอบ / ใช้งานรีลิค: Circle — สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1 [S11]
God of War Ragnarök / PlayStation / PS5 — คู่หูโจมตี: Square — สั่งคู่หูยิงธนูสนับสนุน [S12]
God of War Ragnarök / PlayStation / PS5 — สเตปหลบ / กลิ้งหลบ: Cross — กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ [S13]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S14]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S15]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธที่สาม: D-Pad Down — ชักหอก Draupnir Spear [S16]
God of War Ragnarök / PlayStation / PS5 — เปลี่ยนชนิดลูกธนู: D-Pad Up — สลับลูกธนูของคู่หู [S17]
God of War Ragnarök / PlayStation / PS5 — หยุดเกม: Options — หยุดเกมและเปิดเมนูหลัก [S18]
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S19]
```

**แผนที่ใช้**

```json
{
  "reason": "validated_interpretation_proposal",
  "tasks": [
    {
      "quote": "god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง",
      "domain": "game_controls",
      "category": "C05",
      "operation": "list",
      "facet": "input_bindings",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "model_schema_ok": true,
  "independent_review": null
}
```

### ถามโซนของเกม

Please answer from verified studio information: Which studio zone has TEKKEN 8

**R115**

```text
TEKKEN 8 — studio services offering this game: PC #01-#02; PlayStation 5 #01-#02 [S1]
```

**R117 revision03**

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

**แผนที่ใช้**

```json
{
  "reason": "validated_interpretation_proposal",
  "tasks": [
    {
      "quote": "which studio zone has tekken 8",
      "domain": "games",
      "category": "C04",
      "operation": "detail",
      "facet": "zone",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "model_schema_ok": true,
  "independent_review": null
}
```

### ถามเกมที่เล่นได้หลายโซน

เกมไหนเล่นได้หลายโซน

**R115**

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

**R117 revision03**

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S1]
```

**แผนที่ใช้**

```json
{
  "reason": "validated_interpretation_proposal",
  "tasks": [
    {
      "quote": "เกมไหนเล่นได้หลายโซน",
      "domain": "games",
      "category": "C04",
      "operation": "list",
      "facet": "zone",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "model_schema_ok": true,
  "independent_review": null
}
```

### ทราบระยะเวลาแล้ว แต่กฎคำนวณยังไม่ประกาศ

ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท

**R115**

```text
กรุณาระบุรายการและช่วงเวลาที่ต้องการตรวจสอบเพิ่มเติมครับ
```

**R117 revision04**

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]
PlayStation 5 #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 150 บาทต่อคน สำหรับ 60 นาที [S3]
```

**แผนที่ใช้**

```json
{
  "reason": "meaning_transport_or_protocol_failure",
  "tasks": [],
  "model_schema_ok": false,
  "independent_review": null
}
```

### รักษาบริบทการแข่งขัน

I am preparing for a AOV match. What is the policy for competition equipment and devices

**R115**

```text
Please specify the item and requested time.
```

**R117 revision04**

```text
Please specify the tournament or rulebook edition so I can match the rule you are asking about.
```

**แผนที่ใช้**

```json
{
  "reason": "validated_interpretation_proposal",
  "tasks": [
    {
      "quote": "i am preparing for a aov match. what is the policy for competition equipment and devices",
      "domain": "competition_rules",
      "category": "C13",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "model_schema_ok": true,
  "independent_review": null
}
```

## สิ่งที่ยังต้องพัฒนา

- การตีความของโมเดลและกฎอิสระยังผิดได้ ไม่ใช่ semantic proof; เงื่อนไขที่ซับซ้อนและการผูกเงื่อนไขให้ถูกคำถามย่อยยังต้องตรวจเพิ่ม
- ตัวคำนวณ count/group/compare/recommendation บางกรณียังไม่ครบ การเข้าใจเจตนาถูกไม่ได้ทำให้ reader ที่ยังไม่รองรับทำงานนั้นได้ทันที
- บางชื่อ/ความสัมพันธ์/metadata และ source validity ยังขาดหรือขัดแย้ง บุคลากร public_scope unknown ยังถูกกันไว้ ต้องให้เจ้าของยืนยันผ่านขั้นตอนข้อมูลจริง
- Billing arithmetic ที่ไม่ประกาศยังไม่คำนวณยอดรวมใหม่ การให้ recorded unit rates แบบ partial มีประโยชน์กว่าเดิม แต่ยังไม่ใช่คำตอบยอดรวมที่สมบูรณ์
- ยังมี compatibility paths สำหรับการตีความไม่สำเร็จหรือหมวด general จึงไม่อ้างว่ากำจัด unrelated retrieval/metadata presentation ได้ทุกแบบ
- การใช้โมเดลวิเคราะห์เพิ่มมีต้นทุนเวลา และ cold start อาจทำให้ model call timeout แม้ HTTP chat จะคืนคำตอบได้ ต้องอ่าน transport แยกจาก correctness
- Booking รอบนี้ยัง controlled unavailable ไม่มีการพิสูจน์สถานะเครื่องว่างจริง และ candidate ไม่ติดตั้งทับ R78

## เวลาและ transport ของรอบล่าสุด

```json
{
  "revision03_48_keys": {
    "median_sec": 3.6405000000000003,
    "p95_sec": 14.578
  },
  "saved_r115_same_48_keys_median_sec": 1.797,
  "revision03_model_transport": {
    "attempts": 59,
    "success": 58,
    "failures": 1
  },
  "revision03_integrity": {
    "complete": true,
    "unique_request_keys": 48,
    "grades": 164,
    "all_selected_keys_recorded": true,
    "source_code_inputs_unchanged": true,
    "original_sources_and_results_unchanged": true,
    "model_identity_verified": true,
    "new_questions": 0,
    "category_hints_sent": false,
    "stats": {
      "requests": 48,
      "http_ok": 48,
      "validation_ok": 48,
      "grades": 164,
      "strict_pass": 0,
      "positive_grades": 62,
      "positive_pass": 40,
      "positive_requests": 18,
      "positive_requests_pass": 12,
      "capture_mismatch": 0,
      "grader_errors": 0,
      "timed_out": 0,
      "empty_answers": 0
    },
    "elapsed_sec": 323.92,
    "completed_at": "2026-10-21T21:22:55.356575+07:00"
  },
  "revision04_final_integrity": {
    "complete": true,
    "unique_request_keys": 8,
    "grades": 26,
    "all_selected_keys_recorded": true,
    "source_code_inputs_unchanged": true,
    "original_sources_and_results_unchanged": true,
    "model_identity_verified": true,
    "new_questions": 0,
    "category_hints_sent": false,
    "stats": {
      "requests": 8,
      "http_ok": 8,
      "validation_ok": 8,
      "grades": 26,
      "strict_pass": 0,
      "positive_grades": 6,
      "positive_pass": 6,
      "positive_requests": 3,
      "positive_requests_pass": 3,
      "capture_mismatch": 0,
      "grader_errors": 0,
      "timed_out": 0,
      "empty_answers": 0
    },
    "elapsed_sec": 73.19,
    "completed_at": "2026-10-21T21:28:55.718950+07:00"
  }
}
```

## เอกสารและหลักฐาน

- [Flow และรายละเอียด implementation](FLOW_TH.md)
- [คำตอบและแผนทุกข้อของ revision03](http03/analysis/REPORT_TH.md)
- [คะแนน JSON](http03/analysis/COMPARISON.json)
- [Raw HTTP / PipelineAnswer / grades](http03/RESULTS.jsonl)
- [Contract checks 22 จุด](CONTRACT_CHECKS.json)
- [Raw ของ 8 ข้อหลังแก้สุดท้าย](http04/RESULTS.jsonl)
- [ยืนยันรอบสุดท้าย source/model unchanged](http04/TEST_COMPLETE.json)
- [revision01](full01/analysis/REPORT_TH.md), [revision02](http02/analysis/REPORT_TH.md) และ revision03 เก็บครบ พร้อม FROZEN_SYSTEM ที่ตรวจ hash ก่อนแก้รอบถัดไป
