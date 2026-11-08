# วิเคราะห์ข้อผิดพลาด R88 — Format กลาง / LLM ON (ผลบางส่วน)

## การอ่านผล

อ่านผลที่มีแล้ว 1,911 unique requests ไม่รันคำถามซ้ำ ไม่แก้คำตอบหรือ oracle สถานะครบ: False

การจัดกลุ่มนี้เป็นการวินิจฉัยอัตโนมัติจาก trace/plan/expected contract เพื่อจัดคิวตรวจ ไม่ใช่หลักฐานว่ารู้ root cause ทุกข้อหรือรับรองความหมายโดยมนุษย์ Request หนึ่งอาจมีหลายเกณฑ์และหลายปัญหา ตารางกลุ่มหลักเลือกเหตุที่ควรตรวจแรก แต่ฐานหลักฐานเก็บความไม่ผ่านทุกเกณฑ์ไว้ครบ

## ลำดับตรวจและสาเหตุที่เป็นไปได้

| ระดับ | กลุ่ม | Requests | วิเคราะห์และแนวทาง |
|---|---|---:|---|
| Compatibility | protocol_only_no_literal_failure | 992 | ไม่ผ่านเฉพาะ route/intent/mode เดิม โดยไม่มี literal mismatch ที่พบ ไม่สรุปว่าเนื้อหาถูกครบถ้าไม่มี positive contract |
| P1 | clarification_or_topic_confirmation | 390 | ระบบเลือกขอความชัดเจน/ยืนยันหัวข้อแทนตอบทันที แยกการถามเพิ่มที่จำเป็นออกจาก false clarification โดยดู candidate scope, rejected_candidate, review clauses และ common_read_state |
| Compatibility/ต้องตรวจเนื้อหา | protocol_outcome_or_lineage_needs_review | 162 | route/outcome หรือรหัส evidence เปลี่ยน ต้องตาม source_id/locator/record lineage ก่อนสรุปว่าอ้างผิดเกม การไม่มี literal mismatch ไม่ใช่ความถูกต้องที่มนุษย์รับรอง |
| ตรวจ oracle/source date | source_validity_guard_vs_historical_oracle | 51 | ระบบพบราคา/ข้อมูลไม่อยู่ในช่วงมีผล ต้องเทียบ validity ใน source กับ reference date ของโจทย์ เกณฑ์เก่าที่ต้องการตัวเลขอาจขัดกับการป้องกันข้อมูลหมดอายุ ไม่ต่ออายุหรือเดาราคาศูนย์เอง |
| P1 | source_selection_field_coverage_or_wording | 46 | มีเนื้อหาที่ oracle กำหนดแต่ไม่พบ ต้องดูว่าตัวเลือกไปผิด record, เลือก field ไม่ครบ, แผนทิ้ง proposition หรือเป็นคำพ้อง/การแปลที่ checker ไม่รับ ไม่อ้างเป็น root cause ที่ยืนยันแล้วทั้งหมด |
| ต้องทบทวน | native_grader_failure_needs_content_review | 40 | native grader ไม่ผ่านแต่ literal เพิ่มเติมไม่มีหลักฐานพอ ต้องอ่าน expected case และ grader_detail ก่อนจัดว่าเป็นความผิดของเนื้อหา |
| P1 | competition_clause_scope_or_wording | 25 | มี literal/source clause ที่คาดแต่ไม่ปรากฏ อาจเป็นการเลือกเล่ม/facet/proposition, ตัดเงื่อนไขไม่ครบ หรือถ้อยคำแปลต่าง ต้องดู selected_ids/requested_fields/obligations และ expected clauses คู่กัน |
| P0 | model_transport_failure | 22 | มี HTTP ไปโมเดลแล้วเชื่อมไม่สำเร็จจริง แยก permission/refused/timeout ตาม model_http_calls ไม่อ้างว่า source ไม่ครบเพียงเพราะโมเดลล่ม |
| P1 | price_scope_validity_or_wording | 9 | ตรวจ service/resource/zone/audience/period และ source revision อย่าคิดรายชั่วโมงหรือแพ็กเกจเองเพื่อให้ได้ตัวเลขใน oracle |
| P0 | execution_or_watchdog | 2 | พบ exception/watchdog จริง ต้องดู traceback และช่วง deadline ก่อนตีความคำตอบ แก้ตัวรัน/เส้นทางที่ล้ม ไม่แก้ owner facts |
| เงื่อนไขทดสอบ | controlled_booking_unavailable | 2 | ตัวทดสอบตั้ง Booking เป็น unavailable เพื่อกันสถานะสดเปลี่ยน ไม่ใช่หลักฐานว่า WordPress จริงล่ม และไม่ใช่การยืนยันว่าง/ถูกจอง |
| P1 | retry_or_data_model_guard | 1 | คำตอบถูกพักด้วย retry/data/model guard ต้องอ่าน reason ไม่ถือ flag LLM ON ว่า inference สำเร็จทุกข้อ |

## เหตุใดเปิด LLM แล้วยังอาจตอบผิด

- ON เปิดความสามารถตาม routing ไม่ได้บังคับทุกคำถามให้ใช้ LLM หรือข้าม evidence/validity checks
- HTTP สำเร็จ หมายถึงขนส่งสำเร็จ; schema ผ่าน หมายถึงรูปแบบแผนผ่าน; binding ผ่าน หมายถึงผูก schema ได้ สิ่งเหล่านี้ไม่ใช่คำรับรองว่าตีความเจตนาหรือเลือก source ถูก
- deterministic bridge ก็มี coverage limit; โมเดลอาจได้รับ candidates ที่ยังไม่ครอบคลุม หรือแผนที่อ่านได้เพียงบาง field จึงยังต้องวัดเนื้อหาที่ตอบจริง
- raw score รวมชื่อ route/รหัสเดิมและเงื่อนไขเก่า จึงรายงาน raw/literal/source/outcome/model transport แยกกัน ไม่ตัดเกณฑ์ทิ้งเพื่อให้คะแนนดี

## ตัวอย่างคำถาม คำตอบจริง สิ่งที่คาด และเหตุที่เลือก

### protocol_only_no_literal_failure

ไม่ผ่านเฉพาะ route/intent/mode เดิม โดยไม่มี literal mismatch ที่พบ ไม่สรุปว่าเนื้อหาถูกครบถ้าไม่มี positive contract

#### TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง

ภาษา: th / หมวด: compound_context_boundary / key: `5070c43c2755d2994c0c0dd04a1018e80e9a857b5f26b72c01c14f5c7137e202`

**คำตอบที่ผู้ใช้จะได้**

ข้อมูลเกม: Resident Evil Village

ข้อมูลเกม: TEKKEN 8

**เรสซิเดนต์อีวิลวิลเลจ**
• ปุ่มควบคุม: L (Left Stick) | เคลื่อนที่ | บังคับทิศทางการเดินและการเคลื่อนไหวของตัวละคร Ethan Winters
L3 (Click Left Stick) | วิ่งเร็ว / สปรินต์ | กดลงไปในขณะเคลื่อนที่เพื่อเร่งความเร็วในการวิ่งหนีหรือเข้าหาที่กำบัง
R (Right Stick) | ควบคุมมุมมอง / หันกล้อง | หมุนเพื่อกวาดสายตา หันหัวตัวละคร มองรอบๆ หรือใช้ในการเล็งเป้า
R3 (Click Right Stick) | ย่อตัว | กดเพื่อย่อตัวลงต่ำ ใช้สำหรับลอดช่องแคบ ซ่อนตัว หรือหลบการโจมตีระดับสายตา
L2 | เล็งเป้า / เล็งปืน | ยกอาวุธปืนขึ้นมาเล็งเพื่อบีบเป้าให้แคบลงและเพิ่มความแม่นยำในการยิง
L1 | ยกการ์ด / ป้องกัน | ยกแขนขึ้นมาตั้งการ์ดบังการโจมตีของศัตรูเพื่อลดความเสียหาย (หากกดถูกจังหวะจะสามารถผลักศัตรูให้เสียหลักได้)
R2 | โจมตี / ยิงปืน | เหนี่ยวไกยิงปืนที่กำลังถืออยู่ หรือเหวี่ยงอาวุธประชิด (เช่น มีด) เพื่อโจมตีศัตรู
R1 | ฟื้นฟูพลังชีวิต / ใช้ยา | ใช้ยารักษาฉีด/เทรดบาดแผลเพื่อฟื้นฟูเกจพลังชีวิตทันทีเมื่อได้รับบาดเจ็บ
Triangle | เปิดกระเป๋าเก็บของ | เปิดหน้าต่างสัมภาระเพื่อตรวจสอบไอเทม อาวุธ กระสุน ผสมไอเทม หรือกดใช้งานสิ่งของ
Square | รีโหลด / บรรจุกระสุน | ใส่กระสุนปืนกล่องใหม่เข้าไปในอาวุธที่กำลังถืออยู่
Circle | ยกเลิก / ย้อนกลับ | ใช้กดเพื่อปิดหน้าต่างเมนู ย้อนกลับ หรือยกเลิกคำสั่งที่เลือกไว้
Cross | โต้ตอบ / สำรวจ | กดเพื่อเปิดประตู เก็บไอเทม ไขปริศนา คุยกับตัวละคร หรือตรวจสอบสิ่งของในฉาก
D-Pad (Up / Down / Left / Right) | ติดตั้งอาวุธด่วน | กดปุ่มทิศทางเพื่อสลับเปลี่ยนอาวุธที่เซ็ตไว้ในช่องทางลัดทันที โดยไม่ต้องเปิดกระเป๋า
Options | หยุดเกม | หยุดหน้าจอเกมชั่วคราวเพื่อเข้าสู่เมนูหลักหรือตั้งค่าระบบ
Touch Pad | แผนที่ | เปิดดูแผนที่จำลองของพื้นที่หรือหมู่บ้าน เพื่อเช็กเส้นทางและห้องที่ยังสำรวจไม่ครบ [S1]
• แพลตฟอร์ม: PlayStation / PS5 [S2]
• สถานะข้อมูลปุ่ม: ข้อมูลจากแหล่งรอง ยังไม่ได้ยืนยันผังปุ่มบนเครื่องศูนย์ [S3]

**เทคเคน 8**
• ปุ่มควบคุม: Square | หมัดซ้าย / ต่อยซ้าย | ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว
Triangle | หมัดขวา / ต่อยขวา | ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)
Cross | ลูกเตะซ้าย | ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู
Circle | ลูกเตะขวา | ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง
D-Pad Up | กระโดด | ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ
D-Pad Left | ถอยหลัง / บล็อก | บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพื่อ "บล็อก (Guard)" การโจมตีระดับสูงและระดับกลางของศัตรู
D-Pad Down | ย่อตัว / ก้มหลบ | สั่งให้ตัวละครย่อตัวต่ำ ใช้ก้มหลบหมัดหรือการโจมตีระดับสูง (High) และใช้บล็อกการโจมตีระดับต่ำ (Low)
L (Left Stick) | เคลื่อนที่ | ขยับทิศทางของตัวละคร بشكلทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง
L1 | สเปเชียลสไตล์ | กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบและท่าไม้ตายของตัวละครนั้นๆ ได้ง่ายด้วยปุ่มเดียว
R1 | เปิดใช้งาน Heat | ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร
R1 (While in Heat) | ฮีทสแมช | ปลดปล่อยท่าโจมตีเผด็จศึกอันทรงพลังปิดฉากคอมโบ โดยจะใช้เกจ Heat ที่เหลืออยู่ทั้งหมดทิ้งทันที
Options | หยุดเกม | หยุดเกมชั่วคราวเพื่อเข้าสู่หน้าต่างเมนู เช่น การเช็ก Move List (รายการท่า) หรือการตั้งค่าอื่นๆ [S4]
• แพลตฟอร์ม: PlayStation / PS5 [S5]
• สถานะข้อมูลปุ่ม: ข้อมูลจากแหล่งรอง ยังไม่ได้ยืนยันผังปุ่มบนเครื่องศูนย์ [S6]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "game_detail_resident_evil_village",
    "game_detail_tekken_8"
  ],
  "requested_fields": [
    "bindings"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['games', 'multi_question']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-04874",
    "question": "TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง",
    "expected_route_categories": [
      "games",
      "multi_question"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "TEKKEN 8",
        "Resident Evil Village",
        "ปุ่ม"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['games', 'multi_question']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-04874",
    "question": "TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง",
    "expected_route_categories": [
      "games",
      "multi_question"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "TEKKEN 8",
        "Resident Evil Village",
        "ปุ่ม"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Fortnite ราคาเท่าไหร่

ภาษา: th / หมวด: service_fee / key: `c42fafb19394b0b1b06620bfc90cfce671ddc9f1083a43f6eab8bfa1ce151b35`

**คำตอบที่ผู้ใช้จะได้**

ข้อมูลเกม: Fortnite

**ค่าบริการ — PlayStation 5 #01-#02 / General Adult**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — PlayStation 5 #01-#02 / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — PlayStation 5 #01-#02 / PSU Student and Staff**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_not_current",
  "method": "exact",
  "selected_ids": [
    "game_detail_fortnite"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/broad_usage_eval_v1.json",
  "failures": [
    "route:knowledge expected:['service_fee']"
  ],
  "expected": {
    "id": "SF-066",
    "question": "Fortnite ราคาเท่าไหร่",
    "expected_category": "service_fee",
    "must_contain": [
      "Fortnite"
    ],
    "must_contain_any": [],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "route:knowledge expected:['service_fee']"
  ],
  "expected": {
    "id": "MB-0066-SF-066",
    "question": "Fortnite ราคาเท่าไหร่",
    "expected_category": "service_fee",
    "must_contain": [
      "Fortnite"
    ],
    "must_contain_any": [],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Ring Fit Adventure utton confirmation for selecting an option

ภาษา: en / หมวด: game_controls / key: `6efd22288f8fd67b5959977ff028d3c0fac2523d146989f94c01eadffa2865eb`

**คำตอบที่ผู้ใช้จะได้**

Game: Ring Fit Adventure

**Ring Fit Adventure**
• Controls: Joy-Con (R) Control Stick | Move cursor | Move the cursor in menus using the Joy-Con (R), which is inserted into the Ring-Con
X Button | Confirm selection | Confirm selections in menus
A Button | Cancel selection | Cancel or return from menu selections
Ring-Con tilt | Move menu cursor | Hold the Ring-Con like a steering wheel and tilt left/right or up/down to move the cursor
Press Ring-Con inward | Confirm with Ring-Con | Press the Ring-Con inward to confirm a selection
Pull Ring-Con outward | Cancel with Ring-Con | Pull Ring-Con out to deselect [S1]
• Platform: Nintendo Switch [S2]
• Source limitations: Official Nintendo support documents menu navigation and Ring-Con/Leg Strap control concepts. In-game actions vary by exercise and are shown on screen. [S3]
• Control information status: Partial official information; not a complete button map [S4]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "game_detail_ring_fit_adventure"
  ],
  "requested_fields": [
    "bindings"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
  "failures": [
    "route:knowledge expected:['games']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-03254",
    "question": "Ring Fit Adventure utton confirmation for selecting an option",
    "expected_route_categories": [
      "games"
    ],
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### clarification_or_topic_confirmation

ระบบเลือกขอความชัดเจน/ยืนยันหัวข้อแทนตอบทันที แยกการถามเพิ่มที่จำเป็นออกจาก false clarification โดยดู candidate scope, rejected_candidate, review clauses และ common_read_state

#### How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo

ภาษา: en / หมวด: compound_context_boundary / key: `adabcf3a2ca3d695a117988e02e1a5d00467f9748ec8580c159142c2058ab6f4`

**คำตอบที่ผู้ใช้จะได้**

I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:migrated_clarification",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
  "failures": [
    "route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation']",
    "status:clarification expected:answer_available"
  ],
  "expected": {
    "id": "MASTER-GT-EN-04963",
    "question": "How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo",
    "expected_route_categories": [
      "equipment",
      "games",
      "multi_question",
      "reservation"
    ],
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### What is the studio policy for friday maintenance

ภาษา: en / หมวด: reservation_policy / key: `0f863c96fa66427e13a97dfc9cee137ef81ab4fb72879dd12509054269c858de`

**คำตอบที่ผู้ใช้จะได้**

The requested topic is unclear. Which part of Friday — maintenance do you need: question / Confirmed information / topic?

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_clarification",
  "method": "bounded_fuzzy",
  "selected_ids": [
    "migrated_faq_rule_schedule_friday_maintenance"
  ],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['reservation']",
    "status:clarification expected:answer_available"
  ],
  "expected": {
    "id": "MASTER-GT-EN-00417",
    "question": "What is the studio policy for friday maintenance",
    "expected_route_categories": [
      "reservation"
    ],
    "expected_intent": "schedule_friday_maintenance",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['reservation', 'schedule']",
    "status:clarification expected:answer_available"
  ],
  "expected": {
    "id": "MASTER-GT-EN-01262",
    "question": "What is the studio policy for friday maintenance",
    "expected_route_categories": [
      "reservation",
      "schedule"
    ],
    "expected_intent": "schedule_friday_maintenance",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Resident Evil Village ราคเท่าไหร่

ภาษา: th / หมวด: service_fee / key: `b59d525cecb3762f0833e0cd0d5c3f26aa2ef477da2b90d0aa7db6de53d95e24`

**คำตอบที่ผู้ใช้จะได้**

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Resident Evil Village เช่น ชื่อเกมอย่างเป็นทางการ?

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_clarification",
  "method": "exact",
  "selected_ids": [
    "game_detail_resident_evil_village"
  ],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "status:clarification expected:answer_available"
  ],
  "expected": {
    "id": "MASTER-GT-TH-00099",
    "question": "Resident Evil Village ราคเท่าไหร่",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [
        "Resident Evil Village"
      ],
      "must_contain_any": [],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### competition_clause_scope_or_wording

มี literal/source clause ที่คาดแต่ไม่ปรากฏ อาจเป็นการเลือกเล่ม/facet/proposition, ตัดเงื่อนไขไม่ครบ หรือถ้อยคำแปลต่าง ต้องดู selected_ids/requested_fields/obligations และ expected clauses คู่กัน

#### Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?

ภาษา: en / หมวด: unclassified / key: `ed920c5962389f0a735cda26e46615e40a01037708c074b3858de0cc02e3ce19`

**คำตอบที่ผู้ใช้จะได้**

Competition rules: TEKKEN 8 — PSU Esports ปะทะมันส์ สนั่นจอ

**Etiquette in Competition**
• Rule topic: Etiquette in Competition [S1]
• Rule details: Sportsmanship
* No conduct shall be exhibited that shows lack of respect toward athletes, such as mockery, disparagement, or any unsuitable verbal or physical behavior toward others. Any violation will result in an immediate loss with no exceptions.
* Competitors must show respect to referees and other competitors. No conduct showing disrespect or lack of courtesy shall be tolerated under any circumstances. Any violation will result in an immediate loss with no exceptions. [S2]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_tekken8_psu_esports"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": [
    "missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.",
    "missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception."
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_content_contract_r27_320_20261001.json",
  "failures": [
    "route_mismatch",
    "missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.",
    "missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.",
    "first_line_off_topic"
  ],
  "expected": {
    "id": "R27-tekken8-conduct-en-1",
    "question": "Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?",
    "required_clauses": [
      "Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.",
      "Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception."
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Under CS2 tournamment rules, what exception applies to social media access?

ภาษา: en / หมวด: unclassified / key: `eb0a7ba6e14542bba455e0b05664f61d676be44d6ecd0444e756eed8817954a7`

**คำตอบที่ผู้ใช้จะได้**

Competition rules: Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer.**
• Rule topic: 5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer. [S1]
• Rule details: 5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer. [S2]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": [
    "missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers."
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_new_questions_r27_128_20261001.json",
  "failures": [
    "route_mismatch",
    "missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers.",
    "first_line_off_topic"
  ],
  "expected": {
    "id": "R27-new-cs2-social-exception-en-1",
    "question": "Under CS2 tournamment rules, what exception applies to social media access?",
    "required_clauses": [
      "5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers."
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Under VALORANT tournamment ruls, how many players may be in match preparation and how many regulation Tactical Timeouts are allowed with what duration?

ภาษา: en / หมวด: composite / key: `74cdfb76eb55e64fd08d7609ac14e36d667a4fd94e260568ef1495cbb5cebfb5`

**คำตอบที่ผู้ใช้จะได้**

Competition rules: VALORANT — PSU Phuket VALORANT 2026 Tournament

**Game pauses are divided into 3 main types for different reasons.**
• Rule topic: Game pauses are divided into 3 main types for different reasons. [S1]
• Rule details: Game pauses are divided into 3 main types for different reasons. [S2]

**1. Tactical Timeout**
• Rule topic: 1. Tactical Timeout [S3]
• Rule details: 1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over. [S4]

**2. Technical Pause**
• Rule topic: 2. Technical Pause [S5]
• Rule details: 2. Technical Pause
* Used when there is equipment malfunction, disconnection issues, or software problems.
* Players are prohibited from communicating with each other (either verbally or in writing) unless authorized. [S6]

**3. Player Emergency Pause (Emergency Stop)**
• Rule topic: 3. Player Emergency Pause (Emergency Stop) [S7]
• Rule details: 3. Player Emergency Pause
* 1 request per map.
* Total time must not exceed 10 minutes per match. If exceeded, that player may lose eligibility to continue and must be replaced by a substitute.
Bug rules
Bugs are unintended game errors. They are classified to determine the procedure:
* Play Through Bug: a bug with no significant effect on fairness. Players must continue and cannot request a Challenge.
* Major Bug: a bug with a major effect on gameplay or game mechanics and no immediate workaround. The team may request a Challenge for review.
* Game Breaking Bug: a bug that destroys the fairness of the round so its winner cannot be determined.
* Round Rollback:
* If a bug occurs before any damage is dealt, officials may roll back the round.
* After damage has been dealt, there is no rollback except through the Challenge procedure.
* For a Game Breaking Bug, officials will immediately roll back to the start of that round.
Exploit Adjudication [S8]

**There are three main types of pauses, each for different purposes**
• Rule topic: There are three main types of pauses, each for different purposes [S9]
• Rule details: There are three main types of pauses, each for different purposes [S10]

**1. Tactical Timeout**
• Rule topic: 1. Tactical Timeout [S11]
• Rule details: 1. Tactical Timeout
* Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds.
* During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over. [S12]

**2. Technical Pause**
• Rule topic: 2. Technical Pause [S13]
• Rule details: 2. Technical Pause
* Used in cases of hardware malfunction, disconnection, or software issues.
* Players may not communicate (voice or text) unless permitted by officials. [S14]

**3. Player Emergency Pause**
• Rule topic: 3. Player Emergency Pause [S15]
• Rule details: 3. Player Emergency Pause
* Each team may request 1 pause per map.
* Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
Bug Regulations [S16]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_valorant_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": [
    "missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present.",
    "missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each."
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_composition_r28_280_20261001.json",
  "failures": [
    "wrong_category",
    "missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present.",
    "missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each.",
    "first_line_off_topic"
  ],
  "expected": {
    "id": "R28-valorant-prep-timeout-en-2",
    "question": "Under VALORANT tournamment ruls, how many players may be in match preparation and how many regulation Tactical Timeouts are allowed with what duration?",
    "clauses": [
      "Personnel: During Match Prep, no more than 6 players may be present.",
      "2 requests per map during regulation (first 24 rounds), 60 seconds each."
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### protocol_outcome_or_lineage_needs_review

route/outcome หรือรหัส evidence เปลี่ยน ต้องตาม source_id/locator/record lineage ก่อนสรุปว่าอ้างผิดเกม การไม่มี literal mismatch ไม่ใช่ความถูกต้องที่มนุษย์รับรอง

#### ช่วยดูหน่อย กำลังจะลงแข่ง CS2 อยากรู้เรื่องขั้นตอนระหว่างการเเข่งขัน ครับ

ภาษา: th / หมวด: unclassified / key: `dc5e988db700686f3b77ba8bb6bc1235e95105659371e2cfe8e1cababd3715fb`

**คำตอบที่ผู้ใช้จะได้**

กติกา Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**4. ขั้นตอนการดำเนินการแข่งขัน**
• หัวข้อกติกา: 4. ขั้นตอนการดำเนินการแข่งขัน [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 4. ขั้นตอนการดำเนินการแข่งขัน [S2]

**3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที**
• หัวข้อกติกา: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที [S4]

**8. ตารางบทลงโทษ (Penalties)**
• หัวข้อกติกา: 8. ตารางบทลงโทษ (Penalties) [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 8. ตารางบทลงโทษ (Penalties)
การละเมิด
บทลงโทษ
การด่าทอ/ใช้ความรุนแรงทางวาจา
ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
การโกงทุกรูปแบบ
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
ดูสตรีมระหว่างแข่ง
ปรับแพ้ในแมตช์นั้น
หยุดเกมโดยไม่ได้รับอนุญาต
ปรับแพ้ในรอบนั้น
การใช้บัค
ปรับแพ้ในรอบหรือแมตช์นั้น
พฤติกรรมผิดจริยธรรม
ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์
การพิมพ์แชทในเกมที่ไม่เหมาะสม
ปรับแพ้ในรอบหรือแมตช์นั้น
การหมิ่นศาสนา [S6]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_user_r24_2000_20261001.jsonl",
  "failures": [
    "route expected ['competition_rules'], got knowledge",
    "retrieval evidence did not match the allowed canonical fact/rule IDs"
  ],
  "expected": {
    "id": "R24-TH-cs2-162",
    "question": "ช่วยดูหน่อย กำลังจะลงแข่ง CS2 อยากรู้เรื่องขั้นตอนระหว่างการเเข่งขัน ครับ",
    "expected_route_categories": [
      "competition_rules"
    ],
    "expected_answer_status": "answer_available",
    "expected_game_id": "cs2"
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการประท้วงและข้อพิพาท หน่อย

ภาษา: th / หมวด: unclassified / key: `d6da1b655ceab367f28df738b23c94ba0e9fe508bd542be74756b80096b3aa5e`

**คำตอบที่ผู้ใช้จะได้**

กติกา Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น**
• หัวข้อกติกา: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น [S2]

**9. การบริหารจัดการและผู้ตัดสิน**
• หัวข้อกติกา: 9. การบริหารจัดการและผู้ตัดสิน [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 9. การบริหารจัดการและผู้ตัดสิน [S4]

**1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม**
• หัวข้อกติกา: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม [S6]

**2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น**
• หัวข้อกติกา: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น [S8]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_rules_rag_ground_truth_v1.jsonl",
  "failures": [
    "route expected ['competition_rules'], got knowledge",
    "retrieval evidence did not match the allowed canonical fact/rule IDs"
  ],
  "expected": {
    "id": "COMP-RAG-TH-015",
    "question": "ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการประท้วงและข้อพิพาท หน่อย",
    "expected_route_categories": [
      "competition_rules"
    ],
    "expected_answer_status": "answer_available",
    "expected_game_id": "cs2"
  }
}
```

```json
{
  "corpus": "data/eval/competition_user_r24_2000_20261001.jsonl",
  "failures": [
    "route expected ['competition_rules'], got knowledge",
    "retrieval evidence did not match the allowed canonical fact/rule IDs"
  ],
  "expected": {
    "id": "R24-TH-cs2-019",
    "question": "ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการประท้วงและข้อพิพาท หน่อย",
    "expected_route_categories": [
      "competition_rules"
    ],
    "expected_answer_status": "answer_available",
    "expected_game_id": "cs2"
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Is the studio open today

ภาษา: en / หมวด: schedule_calendar / key: `460763a318a386072fae91965f522b50db35451ecfd91f76226ed28a97f554d4`

**คำตอบที่ผู้ใช้จะได้**

Today, 16 October 2026, the studio is open.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "common_calendar_open_status",
  "selected_ids": [
    "migrated_schedule_4"
  ],
  "requested_fields": [
    "bookable_periods"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['reservation', 'schedule']",
    "status:answer expected:live_lookup_required"
  ],
  "expected": {
    "id": "MASTER-GT-EN-01251",
    "question": "Is the studio open today",
    "expected_route_categories": [
      "reservation",
      "schedule"
    ],
    "expected_intent": "date_aware_schedule",
    "expected_answer_status": "live_lookup_required",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['reservation', 'schedule']",
    "status:answer expected:live_lookup_required"
  ],
  "expected": {
    "id": "MASTER-GT-EN-01251",
    "question": "Is the studio open today",
    "expected_route_categories": [
      "reservation",
      "schedule"
    ],
    "expected_intent": "date_aware_schedule",
    "expected_answer_status": "live_lookup_required",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### native_grader_failure_needs_content_review

native grader ไม่ผ่านแต่ literal เพิ่มเติมไม่มีหลักฐานพอ ต้องอ่าน expected case และ grader_detail ก่อนจัดว่าเป็นความผิดของเนื้อหา

#### กติกกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน

ภาษา: th / หมวด: single / key: `a3b8eac6809bfca58e368d7ca8a12697a582e3f3691cd8e25d827496708b79b0`

**คำตอบที่ผู้ใช้จะได้**

กติกา Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด**
• หัวข้อกติกา: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด [S2]

**2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์**
• หัวข้อกติกา: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ [S4]

**1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น**
• หัวข้อกติกา: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S6]

**8. ตารางบทลงโทษ (Penalties)**
• หัวข้อกติกา: 8. ตารางบทลงโทษ (Penalties) [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 8. ตารางบทลงโทษ (Penalties)
การละเมิด
บทลงโทษ
การด่าทอ/ใช้ความรุนแรงทางวาจา
ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
การโกงทุกรูปแบบ
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
ดูสตรีมระหว่างแข่ง
ปรับแพ้ในแมตช์นั้น
หยุดเกมโดยไม่ได้รับอนุญาต
ปรับแพ้ในรอบนั้น
การใช้บัค
ปรับแพ้ในรอบหรือแมตช์นั้น
พฤติกรรมผิดจริยธรรม
ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์
การพิมพ์แชทในเกมที่ไม่เหมาะสม
ปรับแพ้ในรอบหรือแมตช์นั้น
การหมิ่นศาสนา [S8]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_composition_r28_280_20261001.json",
  "failures": [
    "wrong_category",
    "first_line_off_topic"
  ],
  "expected": {
    "id": "R28-cs2-custom-settings-th-2",
    "question": "กติกกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน",
    "clauses": [
      "1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Please check: How many starting players must a VALORANT team field? please.

ภาษา: en / หมวด: unclassified / key: `864bd598097acf52516da1f737b8ea89803aee391e4e161ecf307091c5f8ecb8`

**คำตอบที่ผู้ใช้จะได้**

Competition rules: VALORANT — PSU Phuket VALORANT 2026 Tournament

**Steps from before the game starts until character selection**
• Rule topic: Steps from before the game starts until character selection [S1]
• Rule details: Steps from before the game starts until character selection
* Check-in time: Players must arrive at the competition venue at least 30 minutes prior to the scheduled start time.
* New content restrictions
* New agents will be restricted and unavailable for approximately 2 weeks after being released in Competitive mode.
* New maps will be restricted and unavailable for approximately 4 weeks after being released in Competitive mode.
* Game settings
* Players must turn OFF Blood and Bodies visuals.
* No FPS or Latency display is allowed during competition.
* Map Pool: Consists of 7 maps as specified below:
* Abyss
* Ascent
* Bind
* Corrode
* Haven
* Lotus
* Sunset
* Team selection
* Use a coin toss method.
* Map banning
* Ban until only 3 maps remain. [S2]

**Competition Area and Regulations**
• Rule topic: Competition Area and Regulations [S3]
• Rule details: Competition Area and Regulations
* Personnel during Match Preparation
* No more than 6 players are allowed in the match preparation area.
* Electronic devices
* Mobile phones, tablets, and smartwatches are strictly prohibited in the competition area until the match has concluded.
* Documents and notes
* Players may not bring notes or documents into the competition area.
* The team captain is allowed to bring documents, which must be submitted to the referee before the match.
* Food and beverages
* Only drinking water in a sealed container and chewing gum are permitted.
Match Procedure [S4]

**Pre-Game Process (Before Game Start to Agent Selection)**
• Rule topic: Pre-Game Process (Before Game Start to Agent Selection) [S5]
• Rule details: Pre-Game Process (Before Game Start to Agent Selection)
* Check-in time
* Teams must arrive at the venue at least 30 minutes before the scheduled match time.
* New Content Restrictions
* New agents are restricted for approximately 2 weeks after being released in Competitive mode.
* New maps are restricted for approximately 4 weeks after being released in Competitive mode.
* Game Settings
* Players must turn OFF blood and body displays.
* Displaying FPS or latency graphs during competition is prohibited.
* Map Pool
* The map pool consists of the following 7 maps
- Abyss
- Ascent
- Bind
- Corrode
- Haven
- Lotus
- Sunset
* Map Ban
* Ban maps until 3 maps remain [S6]

**3. Player Emergency Pause**
• Rule topic: 3. Player Emergency Pause [S7]
• Rule details: 3. Player Emergency Pause
* Each team may request 1 pause per map.
* Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
Bug Regulations [S8]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_valorant_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_user_r24_2000_20261001.jsonl",
  "failures": [
    "route expected ['competition_rules', 'no_answer'], got knowledge",
    "outcome expected no_answer_expected, got answer",
    "source-gap no-answer attached evidence or did not abstain safely"
  ],
  "expected": {
    "id": "R24-EN-valorant-125",
    "question": "Please check: How many starting players must a VALORANT team field? please.",
    "expected_route_categories": [
      "competition_rules",
      "no_answer"
    ],
    "expected_answer_status": "no_answer_expected",
    "expected_game_id": "valorant"
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม

ภาษา: th / หมวด: composite / key: `0c25d981c16244f8fe17020eaa9c404ed3481cb7c21cd832073e36db18f420d5`

**คำตอบที่ผู้ใช้จะได้**

กติกา Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**1. การเลือกแผนที่ ใช้ MAPBAN.GG**
• หัวข้อกติกา: 1. การเลือกแผนที่ ใช้ MAPBAN.GG [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG [S2]

**2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์**
• หัวข้อกติกา: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ [S4]

**3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง**
• หัวข้อกติกา: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง [S6]

**8. ตารางบทลงโทษ (Penalties)**
• หัวข้อกติกา: 8. ตารางบทลงโทษ (Penalties) [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 8. ตารางบทลงโทษ (Penalties)
การละเมิด
บทลงโทษ
การด่าทอ/ใช้ความรุนแรงทางวาจา
ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
การโกงทุกรูปแบบ
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
ดูสตรีมระหว่างแข่ง
ปรับแพ้ในแมตช์นั้น
หยุดเกมโดยไม่ได้รับอนุญาต
ปรับแพ้ในรอบนั้น
การใช้บัค
ปรับแพ้ในรอบหรือแมตช์นั้น
พฤติกรรมผิดจริยธรรม
ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์
การพิมพ์แชทในเกมที่ไม่เหมาะสม
ปรับแพ้ในรอบหรือแมตช์นั้น
การหมิ่นศาสนา [S8]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/competition_composition_r28_280_20261001.json",
  "failures": [
    "wrong_category",
    "first_line_off_topic"
  ],
  "expected": {
    "id": "R28-cs2-bug-stream-th-0",
    "question": "กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม",
    "clauses": [
      "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์",
      "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### execution_or_watchdog

พบ exception/watchdog จริง ต้องดู traceback และช่วง deadline ก่อนตีความคำตอบ แก้ตัวรัน/เส้นทางที่ล้ม ไม่แก้ owner facts

#### เอาอาหารเข้าได้ไหม

ภาษา: auto / หมวด: rules / key: `b0b908e3789f04a2084a19d2b8c00c722d72f1e606a56da60dbe80fb380f15e3`

**คำตอบที่ผู้ใช้จะได้**

(ว่าง/exception)

**แผนที่เลือกจริง**

```json
{
  "mode": "execution_exception",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": [
    "missing required: อาหาร",
    "missing required: เครื่องดื่ม",
    "missing required: พื้นที่ที่กำหนด",
    "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/answer_quality_cases.jsonl",
  "failures": [
    "pipeline_exception"
  ],
  "expected": {
    "id": "AQ-RULE-001",
    "question": "เอาอาหารเข้าได้ไหม",
    "expected_category": "rules",
    "must_contain": [
      "อาหาร",
      "เครื่องดื่ม",
      "พื้นที่ที่กำหนด"
    ],
    "must_not_contain": []
  }
}
```

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "pipeline_exception"
  ],
  "expected": {
    "id": "MB-1248-PSR-005",
    "question": "เอาอาหารเข้าได้ไหม",
    "expected_category": [
      "rules",
      "penalty"
    ],
    "must_contain": [],
    "must_contain_any": [
      "เปิด",
      "ปิด",
      "จอง",
      "ยกเลิก",
      "นาที",
      "อาหาร",
      "ปรับ",
      "กติกา"
    ],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Could you please help me with this: What kind of game is Hogwarts Legacy

ภาษา: en / หมวด: game_detail / key: `f83db6c956054229bb20d767bdd6d607d4e42e4ad9bda6a2f2d53c78fd59eeb8`

**คำตอบที่ผู้ใช้จะได้**

(ว่าง/exception)

**แผนที่เลือกจริง**

```json
{
  "mode": "execution_exception",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": [
    "missing all alternatives: ['Hogwarts Legacy']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "pipeline_exception"
  ],
  "expected": {
    "id": "MASTER-GT-EN-02357",
    "question": "Could you please help me with this: What kind of game is Hogwarts Legacy",
    "expected_route_categories": [
      "games"
    ],
    "expected_intent": "game_detail_lookup",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Hogwarts Legacy"
      ],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "pipeline_exception"
  ],
  "expected": {
    "id": "MASTER-GT-EN-02451",
    "question": "Could you please help me with this: What kind of game is Hogwarts Legacy",
    "expected_route_categories": [
      "games"
    ],
    "expected_intent": "game_detail_lookup",
    "expected_answer_status": "localization_pending",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Hogwarts Legacy"
      ],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### source_validity_guard_vs_historical_oracle

ระบบพบราคา/ข้อมูลไม่อยู่ในช่วงมีผล ต้องเทียบ validity ใน source กับ reference date ของโจทย์ เกณฑ์เก่าที่ต้องการตัวเลขอาจขัดกับการป้องกันข้อมูลหมดอายุ ไม่ต่ออายุหรือเดาราคาศูนย์เอง

#### General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท

ภาษา: th / หมวด: service_fee / key: `f3ae278c43764dbda15c79671b61aafde8de0a50342a5abd5f1daf94becd847f`

**คำตอบที่ผู้ใช้จะได้**

**ค่าบริการ — VR Station 30 นาที / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_not_current",
  "method": "exact",
  "selected_ids": [
    "availability_vr_30",
    "availability_vr_60",
    "audience_psu_alumni_general_student"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-00232",
    "question": "General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "บาท",
        "บาท",
        "ฟรี"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-00232",
    "question": "General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "บาท",
        "บาท",
        "ฟรี"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Could you please help me with this: Please tell me: How much is VR for 30 minutes? Please answer briefly

ภาษา: en / หมวด: service_fee / key: `82ea2ad580f324c379e94820288468eaad71df763b80e72e261ab5cbf643695b`

**คำตอบที่ผู้ใช้จะได้**

**Service rate — VR Station 30 minutes / General Adult**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

**Service rate — VR Station 30 minutes / PSU Alumni and General Student**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

**Service rate — VR Station 30 minutes / PSU Student and Staff**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

**Service rate — VR Station 1 hour / General Adult**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

**Service rate — VR Station 1 hour / PSU Alumni and General Student**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

**Service rate — VR Station 1 hour / PSU Student and Staff**
This revision or a referenced record is not effective at the query time; no current fact is asserted. (recorded validity: 2026-02-01T00:00:00+07:00 until (exclusive) 2026-04-01T00:00:00+07:00)

The current price cannot be confirmed from expired rates.

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_not_current",
  "method": "exact",
  "selected_ids": [
    "availability_vr_30",
    "availability_vr_60"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing required: THB"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing required: THB"
  ],
  "expected": {
    "id": "MASTER-GT-EN-00336",
    "question": "Could you please help me with this: Please tell me: How much is VR for 30 minutes? Please answer briefly",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [
        "30 minutes",
        "THB"
      ],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing required: THB"
  ],
  "expected": {
    "id": "MASTER-GT-EN-00336",
    "question": "Could you please help me with this: Please tell me: How much is VR for 30 minutes? Please answer briefly",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [
        "30 minutes",
        "THB"
      ],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### General Adult เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท

ภาษา: th / หมวด: service_fee / key: `1c8fae506d088419b4e0c583ea42375ef0f2be28bdca84cbcb7e2e1133112ce4`

**คำตอบที่ผู้ใช้จะได้**

**ค่าบริการ — VR Station 30 นาที / General Adult**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / General Adult**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_not_current",
  "method": "exact",
  "selected_ids": [
    "availability_vr_30",
    "availability_vr_60",
    "audience_general_adult"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-00266",
    "question": "General Adult เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "บาท",
        "บาท",
        "ฟรี"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-00266",
    "question": "General Adult เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "บาท",
        "บาท",
        "ฟรี"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### model_transport_failure

มี HTTP ไปโมเดลแล้วเชื่อมไม่สำเร็จจริง แยก permission/refused/timeout ตาม model_http_calls ไม่อ้างว่า source ไม่ครบเพียงเพราะโมเดลล่ม

#### A question about the studio: Can an external visitor use the VR headset?

ภาษา: en / หมวด: equipment_access_trap / key: `eed9942c1154f47b25b1348687772419742fe9b3824eecec167f1a1a3bb58cb5`

**คำตอบที่ผู้ใช้จะได้**

The requested topic is unclear. Which part of VR Zone do you need: Service / platform / Play time per session / Booking occupancy?

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_clarification",
  "method": "exact",
  "selected_ids": [
    "zone_vr",
    "availability_vr_30",
    "availability_vr_60"
  ],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification']"
  ],
  "expected": {
    "id": "INTENT-TRAP-EN-0417",
    "question": "A question about the studio: Can an external visitor use the VR headset?",
    "expected_route_categories": [
      "reservation",
      "rules",
      "no_answer",
      "clarification"
    ],
    "expected_answer_status": "route_only",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": [
        "อุปกรณ์บนหน้า Home",
        "Verified equipment:"
      ]
    }
  }
}
```

```json
{
  "corpus": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification']"
  ],
  "expected": {
    "id": "INTENT-TRAP-EN-0417",
    "question": "A question about the studio: Can an external visitor use the VR headset?",
    "expected_route_categories": [
      "reservation",
      "rules",
      "no_answer",
      "clarification"
    ],
    "expected_answer_status": "route_only",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": [
        "อุปกรณ์บนหน้า Home",
        "Verified equipment:"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Logitech G923 TRUEFORCE Racing Wheel คืออะไร

ภาษา: th / หมวด: equipment / key: `e32ea1ac912477ed288c80c8cf24d53c85fa6ec5c43da33391bdcc3867221fb3`

**คำตอบที่ผู้ใช้จะได้**

**Logitech G923 TRUEFORCE Racing Wheel**
• ชื่อรุ่นอุปกรณ์: Logitech G923 TRUEFORCE Racing Wheel [S1]
• ประเภทอุปกรณ์: wheel [S2]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "exact",
  "selected_ids": [
    "equipment_logitech_g923"
  ],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['equipment']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-03399",
    "question": "Logitech G923 TRUEFORCE Racing Wheel คืออะไร",
    "expected_route_categories": [
      "equipment"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Logitech",
        "Cockpit"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['equipment']"
  ],
  "expected": {
    "id": "MASTER-GT-TH-03399",
    "question": "Logitech G923 TRUEFORCE Racing Wheel คืออะไร",
    "expected_route_categories": [
      "equipment"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Logitech",
        "Cockpit"
      ],
      "must_not_contain": [
        "Local LLM"
      ]
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### How do I use the TV 65 นิ้ว

ภาษา: en / หมวด: equipment / key: `c61b12870f5cf1d3e64591d79e56b7156865a81f87f7c994a9f7090a60c223f6`

**คำตอบที่ผู้ใช้จะได้**

The requested topic is unclear. Which part of TV 65 inches do you need: name / device type?

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_clarification",
  "method": "exact",
  "selected_ids": [
    "equipment_tv_65"
  ],
  "requested_fields": [],
  "literal_failures": [
    "missing all alternatives: ['TV 65 นิ้ว']",
    "missing all alternatives: ['TV 65 นิ้ว', 'TV 65-inch']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['equipment']",
    "status:clarification expected:answer_available",
    "missing all alternatives: ['TV 65 นิ้ว']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-03343",
    "question": "How do I use the TV 65 นิ้ว",
    "expected_route_categories": [
      "equipment"
    ],
    "expected_intent": "equipment_detail_lookup",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "TV 65 นิ้ว"
      ],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['equipment']",
    "status:clarification expected:answer_available",
    "missing all alternatives: ['TV 65 นิ้ว', 'TV 65-inch']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-03343",
    "question": "How do I use the TV 65 นิ้ว",
    "expected_route_categories": [
      "equipment"
    ],
    "expected_intent": "equipment_detail_lookup",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "TV 65 นิ้ว",
        "TV 65-inch"
      ],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### source_selection_field_coverage_or_wording

มีเนื้อหาที่ oracle กำหนดแต่ไม่พบ ต้องดูว่าตัวเลือกไปผิด record, เลือก field ไม่ครบ, แผนทิ้ง proposition หรือเป็นคำพ้อง/การแปลที่ checker ไม่รับ ไม่อ้างเป็น root cause ที่ยืนยันแล้วทั้งหมด

#### Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild

ภาษา: en / หมวด: game_detail / key: `98db8777d79361985fa4635a167d2f2e0d063c5676110287b61664cc4a997d44`

**คำตอบที่ผู้ใช้จะได้**

Confirmed game records: The Legend of Zelda: Breath of the Wild

• Confirmed source scope: Nintendo Switch (1-2 Persons) [S1][S2][S3]

• Confirmed source scope: Nintendo Switch (1-4 Persons) [S4][S5][S6]

This confirms game offerings/installations, not live booking availability.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "declared_game_installation_scope",
  "selected_ids": [
    "game_detail_zelda_breath_of_the_wild",
    "availability_nintendo_1_2",
    "availability_nintendo_1_4"
  ],
  "requested_fields": [],
  "literal_failures": [
    "missing all alternatives: ['Nintendo Switch Zone']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['games']",
    "missing all alternatives: ['Nintendo Switch Zone']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-02564",
    "question": "Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild",
    "expected_route_categories": [
      "games"
    ],
    "expected_intent": "game_detail_lookup",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Nintendo Switch Zone"
      ],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_en_5000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['games']",
    "missing all alternatives: ['Nintendo Switch Zone']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-02564",
    "question": "Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild",
    "expected_route_categories": [
      "games"
    ],
    "expected_intent": "game_detail_lookup",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [
        "Nintendo Switch Zone"
      ],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบประโยคเดียว

ภาษา: th / หมวด: general_llm / key: `526a1f09da3f334fbff914bcb7eae7e4a3aac3eeea2ac84e2fca82105ccc7a45`

**คำตอบที่ผู้ใช้จะได้**

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: Mission ของศูนย์คือการยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต ผ่านสิ่งอำนวยความสะดวกและอุปกรณ์ที่ช่วยเสริมสร้างการเรียนรู้ให้กับนักเล่นเกม นักศึกษา และผู้สนใจ โดยศูนย์ก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ [S1]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "bounded_fuzzy",
  "selected_ids": [
    "migrated_faq_rule_overview_mission"
  ],
  "requested_fields": [
    "answer"
  ],
  "literal_failures": [
    "missing all alternatives: ['กิจกรรม']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "missing all alternatives: ['กิจกรรม']"
  ],
  "expected": {
    "id": "MB-1552-GL-227",
    "question": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบประโยคเดียว",
    "expected_category": [
      "general",
      "knowledge"
    ],
    "must_contain": [],
    "must_contain_any": [
      "กิจกรรม"
    ],
    "must_not_contain": []
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี

ภาษา: th / หมวด: compound / key: `bfadcb838b54982715e5360f143c5219b26c6355868455e333cf6ff1a846a984`

**คำตอบที่ผู้ใช้จะได้**

**ผศ.ดร.นิวัติ แก้วประดับ**
• ชื่อที่อนุญาตให้เผยแพร่: ผศ.ดร.นิวัติ แก้วประดับ [S1]
• ทีม/หน่วยงาน: Members [S2]
• ตำแหน่ง/หน้าที่: อธิการบดี [S3]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_answer",
  "method": "common_people_directory",
  "selected_ids": [
    "member_ce4590ddc09c0f4e"
  ],
  "requested_fields": [
    "display_name",
    "team",
    "role"
  ],
  "literal_failures": [
    "missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/broad_usage_eval_v1.json",
  "failures": [
    "route:knowledge expected:['multi_question']",
    "missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']",
    "legacy_mode_prefix:['pipeline:multi_question_splitter']"
  ],
  "expected": {
    "id": "C-007",
    "question": "สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี",
    "expected_category": "multi_question",
    "must_contain": [],
    "must_contain_any": [
      "คำถามที่",
      "ราคา",
      "ปุ่ม",
      "Zone",
      "จอง"
    ],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "route:knowledge expected:['multi_question']",
    "missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']",
    "legacy_mode_prefix:['pipeline:multi_question_splitter']"
  ],
  "expected": {
    "id": "MB-0618-C-007",
    "question": "สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี",
    "expected_category": "multi_question",
    "must_contain": [],
    "must_contain_any": [
      "คำถามที่",
      "ราคา",
      "ปุ่ม",
      "Zone",
      "จอง"
    ],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### price_scope_validity_or_wording

ตรวจ service/resource/zone/audience/period และ source revision อย่าคิดรายชั่วโมงหรือแพ็กเกจเองเพื่อให้ได้ตัวเลขใน oracle

#### General Adult เล่น PC 3 ชั่วโมง เสียกี่บาท

ภาษา: th / หมวด: service_fee / key: `2bb0c205e2d1403e46980c19121c44b0c09178b675e757a3bdf390ce116951b9`

**คำตอบที่ผู้ใช้จะได้**

**ค่าบริการ**
• ราคา: 70.00 THB [S1]
• ระยะเวลา 180 นาที: คิด 3 รอบ รวม 210.00 THB
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #01-#02 [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: General Adult [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_session [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S7]

**ค่าบริการ**
• ราคา: 70.00 THB [S8]
• ระยะเวลา 180 นาที: คิด 3 รอบ รวม 210.00 THB
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #03-#10 [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: General Adult [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_session [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S14]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_partial_answer",
  "method": "exact",
  "selected_ids": [
    "availability_pc_01_02",
    "availability_pc_03_10",
    "audience_general_adult"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ],
  "expected": {
    "id": "MB-1077-SF-108",
    "question": "General Adult เล่น PC 3 ชั่วโมง เสียกี่บาท",
    "expected_category": "service_fee",
    "must_contain": [],
    "must_contain_any": [
      "บาท",
      "บาท",
      "ฟรี"
    ],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### PC ราคาเท่าไหร่

ภาษา: th / หมวด: service_fee / key: `156ac1d75e2b17300c0499d41db91259eb16df502eebf1d8b27ee1a1d5826770`

**คำตอบที่ผู้ใช้จะได้**

**ค่าบริการ**
• ราคา: 70.00 THB [S1]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #01-#02 [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: General Adult [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_session [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S7]

**ค่าบริการ**
• ราคา: 25.00 THB [S8]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #01-#02 [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: PSU Alumni and General Student [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_session [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S14]

**ค่าบริการ**
• ราคา: 0.00 THB [S15]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #01-#02 [S16]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: PSU Student and Staff [S17]
• สกุลเงิน: THB [S18]
• หน่วยคิดราคา: per_session [S19]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S20]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S21]

**ค่าบริการ**
• ราคา: 70.00 THB [S22]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #03-#10 [S23]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: General Adult [S24]
• สกุลเงิน: THB [S25]
• หน่วยคิดราคา: per_session [S26]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S27]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S28]

**ค่าบริการ**
• ราคา: 25.00 THB [S29]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #03-#10 [S30]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: PSU Alumni and General Student [S31]
• สกุลเงิน: THB [S32]
• หน่วยคิดราคา: per_session [S33]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S34]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S35]

**ค่าบริการ**
• ราคา: 0.00 THB [S36]
• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน
• เลือกตัวเลือกบริการบนหน้าจอง: PC #03-#10 [S37]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: PSU Student and Staff [S38]
• สกุลเงิน: THB [S39]
• หน่วยคิดราคา: per_session [S40]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S41]
• วิธีคิดราคา: คิดเต็มรอบ ปัดขึ้นตามระยะเวลา [S42]

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_partial_answer",
  "method": "exact",
  "selected_ids": [
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing required: 0 บาท",
    "missing required: 25 บาท"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/broad_usage_eval_v1.json",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing required: 0 บาท",
    "missing required: 25 บาท"
  ],
  "expected": {
    "id": "SF-001",
    "question": "PC ราคาเท่าไหร่",
    "expected_category": "service_fee",
    "must_contain": [
      "PC",
      "0 บาท",
      "25 บาท"
    ],
    "must_contain_any": [],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

```json
{
  "corpus": "data/eval/model_benchmark_1500.json",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing required: 0 บาท",
    "missing required: 25 บาท"
  ],
  "expected": {
    "id": "MB-0001-SF-001",
    "question": "PC ราคาเท่าไหร่",
    "expected_category": "service_fee",
    "must_contain": [
      "PC",
      "0 บาท",
      "25 บาท"
    ],
    "must_contain_any": [],
    "must_not_contain": [
      "Local LLM"
    ]
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### What is the one-hour PC price for a general adult? Please use verified information

ภาษา: en / หมวด: service_fee / key: `420b09c1fec771b6435b2c095a50408d2b481249921363c7d8c1192a43382ff9`

**คำตอบที่ผู้ใช้จะได้**

**Service rate**
• Price: 70.00 THB [S1]
• Effective period of this recorded rate: not specified in the source; current applicability is not confirmed.
• Service: PC #01-#02 [S2]
• User group: General Adult [S3]
• currency: THB [S4]
• Billing unit: per_session [S5]
• Duration (minutes): 60 [S6]
• Calculation rule: Round up to a whole billing session [S7]

**Service rate**
• Price: 70.00 THB [S8]
• Effective period of this recorded rate: not specified in the source; current applicability is not confirmed.
• Service: PC #03-#10 [S9]
• User group: General Adult [S10]
• currency: THB [S11]
• Billing unit: per_session [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Round up to a whole billing session [S14]

English translation is machine generated and has not been reviewed by the owner.

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_partial_answer",
  "method": "exact",
  "selected_ids": [
    "availability_pc_01_02",
    "availability_pc_03_10",
    "audience_general_adult"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "literal_failures": [
    "missing required: 70 THB"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']",
    "missing required: 70 THB"
  ],
  "expected": {
    "id": "MASTER-GT-EN-00015",
    "question": "What is the one-hour PC price for a general adult? Please use verified information",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [
        "70 THB"
      ],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

```json
{
  "corpus": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
  "failures": [
    "route:knowledge expected:['service_fee']"
  ],
  "expected": {
    "id": "MASTER-GT-EN-00015",
    "question": "What is the one-hour PC price for a general adult? Please use verified information",
    "expected_route_categories": [
      "service_fee"
    ],
    "expected_intent": "",
    "expected_answer_status": "localization_pending",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### retry_or_data_model_guard

คำตอบถูกพักด้วย retry/data/model guard ต้องอ่าน reason ไม่ถือ flag LLM ON ว่า inference สำเร็จทุกข้อ

#### ขอสอบถามหน่อยครับ Arena of Valor แข่งจริง กฎเกี่ยวกับขอบเขตและข้อมูลชองรายการ เป็นแบบไหน

ภาษา: th / หมวด: competition_rules / key: `9551544e4d16d4ab50366a455e556e9f02dedb50b9014a0166b5ebd4bfcf7f11`

**คำตอบที่ผู้ใช้จะได้**

ระบบยังไม่พร้อมเลือกข้อมูลสำหรับคำถามนี้ กรุณาลองอีกครั้งครับ

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:common_retry",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
  "failures": [
    "route:knowledge expected:['competition_rules']",
    "latency_ceiling"
  ],
  "expected": {
    "id": "MASTER-GT-TH-04426",
    "question": "ขอสอบถามหน่อยครับ Arena of Valor แข่งจริง กฎเกี่ยวกับขอบเขตและข้อมูลชองรายการ เป็นแบบไหน",
    "expected_route_categories": [
      "competition_rules"
    ],
    "expected_answer_status": "answer_available",
    "answer_contract": {
      "must_contain": [],
      "must_contain_any": [],
      "must_not_contain": []
    }
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

### controlled_booking_unavailable

ตัวทดสอบตั้ง Booking เป็น unavailable เพื่อกันสถานะสดเปลี่ยน ไม่ใช่หลักฐานว่า WordPress จริงล่ม และไม่ใช่การยืนยันว่าง/ถูกจอง

#### What is the PC price, and how many sessions can be booked?

ภาษา: en / หมวด: multi_question / key: `92d7f3be508bc992b24bbd0ff7523f1464d7f7f52636ae132d0fdea2fbdb3685`

**คำตอบที่ผู้ใช้จะได้**

For 2026-10-16 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:live_booking_status_unavailable",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": []
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/english_shadow_1600_machine_20260908.jsonl",
  "failures": [
    "route:reservation expected:['multi_question']",
    "legacy_mode_prefix:['pipeline:multi_question_splitter']"
  ],
  "expected": {
    "id": "EN-SHADOW-0623",
    "question": "What is the PC price, and how many sessions can be booked?",
    "question_en": "What is the PC price, and how many sessions can be booked?",
    "expected_category": "multi_question"
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

#### Which PC is available now? I need the official answer.

ภาษา: en / หมวด: booking / key: `c11e29cce20964a6a1abbb79c3f8cc4288db9a72d153cfa67749d46a5545be8b`

**คำตอบที่ผู้ใช้จะได้**

For 2026-10-16 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

**แผนที่เลือกจริง**

```json
{
  "mode": "pipeline:live_booking_status_unavailable",
  "method": null,
  "selected_ids": [],
  "requested_fields": [],
  "literal_failures": [
    "missing required: not connected"
  ]
}
```

**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**

```json
{
  "corpus": "data/eval/english_gold_400_20260902.jsonl",
  "failures": [
    "route:reservation expected:['no_answer']",
    "missing required: not connected"
  ],
  "expected": {
    "id": "EN-GOLD-0236",
    "question": "Which PC is available now? I need the official answer.",
    "expected_answer_status": "safe_no_answer",
    "must_contain": [
      "not connected"
    ],
    "must_contain_any": [],
    "must_not_contain": []
  }
}
```

คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง

## หลักฐานทั้งหมด

- REPORT_FINAL_TH.md และ ANALYSIS_FINAL.json: coverage/ภาษา/หมวด/transport แยกกัน
- FAILURE_EVIDENCE_EARLY01.sqlite: request_failures และ grade_failures ของทุกแถวที่ไม่ผ่าน พร้อมคำตอบ expected case แผน sources และ model diagnostics
- full01/RESULTS_*.jsonl.gz: ผลจริงทั้งข้อผ่านและไม่ผ่าน พร้อม trace และค่าการตรวจ
- DEEP_ANALYSIS_EARLY01.json: กลุ่มเหตุและตัวอย่าง; diagnostics ยังต้องตรวจ source สำหรับข้อสรุปเชิงความหมาย
- CONFIG.json / RUN_SCOPE_R88_TH.md: ขอบเขตที่ตรึงและ source hashes

ไม่ได้แก้ production data หรือเพิ่มนโยบายจากการอนุมาน ชุดนี้ไม่ใช่ load benchmark หรือ owner approval
