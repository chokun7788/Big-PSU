# เคสที่เคยไม่ผ่านและหลักฐาน r49

อ่านร่วมกับ SERVICE_DIALOGUE_REPORT_R49.md; count ของ checks อาจซ้ำในเคสเดียว

## Baseline source


### th-new-membership-1

คำถาม: ต้องสมัครสมาชิคก่อนเข้าเล่นไหม

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ต้องสมัครสมาชิคก่อนเข้าเล่นไหม",
  "context_resolution": {
    "original_question": "ต้องสมัครสมาชิคก่อนเข้าเล่นไหม",
    "resolved_question": "ต้องสมัครสมาชิคก่อนเข้าเล่นไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ต้องสมัครสมาชิคก่อนเข้าเล่นไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ต้องสมัครสมาชิคก่อนเข้าเล่นไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 205.89,
        "elapsed_sec": 0.2059
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-membership-0

คำถาม: Do nonmembers need to sign up first?

ไม่ผ่าน: english_no_thai, required_content, claims_traced

Mode: `pipeline:structured_members_source_th`

```text
Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3D Developer (นักศึกษาสหกิจ Game and 3D Developer) - College of Computing, Prince of Songkla University, Phuket Campus
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: Cooperative education student — Web & AI Developer (นักศึกษาสหกิจ Web & AI Developer) - College of Computing, Prince of Songkla University, Phuket Campus
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: Super AI SS6 project intern — AI Chat Bot Developer (นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer) - IoT System and Information Engineering, King Mongkut's Institute of Technology Ladkrabang
- นายษุภากรณ์ จิราจินดากุล: Chairperson (ประธาน)
- นายนพัทธ์ ฝอยทอง: Vice Chairperson (รองประธาน)
- นายปัณณวิชญ์ หนูเรือง: Secretary (เลขานุการ)
- นายภูจิตร จิรวิริยาภรณ์: Treasurer (เหรัญญิก)
- นายธนชาติ เอ่งฉ้วน: Public relations officer (ประชาสัมพันธ์)
- นางสาวกมลวรรณ นวลสาย: Committee member (กรรมการ)
- นางสาวชญาภา จันทร์เอิบ: Committee member (กรรมการ)
- นางสาวณัฐธิดา คำทะเนตร์: Committee member (กรรมการ)
- นางสาวสุภาสินี ธนภพ: Committee member (กรรมการ)
- นางสาวอาทิตยา แดงประดับ: Committee member (กรรมการ)
- นายณัฐพนธ์ อินทรสังขนาวิน: Committee member (กรรมการ)
- นายอภิวิชญ์ เลิศกมลรักษ์: Committee member (กรรมการ)
- นายอรรถนนท์ สุขแก้ว: Committee member (กรรมการ)
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Do nonmembers need to sign up first?",
  "context_resolution": {
    "original_question": "Do nonmembers need to sign up first?",
    "resolved_question": "Do nonmembers need to sign up first?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "do nonmembers need to sign up first?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Do nonmembers need to sign up first?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.47,
        "elapsed_sec": 0.0205
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-membership-1

คำถาม: Do I need a membrship to play?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Do I need a membrship to play?",
  "context_resolution": {
    "original_question": "Do I need a membrship to play?",
    "resolved_question": "Do I need a membrship to play?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "do i need a membrship to play?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Do I need a membrship to play?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 692.04,
        "elapsed_sec": 0.692
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-spectators-0

คำถาม: Am I allowed to watch a friend without playing?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for schedule.
```


Context / selection trace:

```json
{
  "resolved_question": "Am I allowed to watch a friend without playing?",
  "context_resolution": {
    "original_question": "Am I allowed to watch a friend without playing?",
    "resolved_question": "Am I allowed to watch a friend without playing?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "am i allowed to watch a friend without playing?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Am I allowed to watch a friend without playing?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 61.36,
        "elapsed_sec": 0.0614
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-spectators-1

คำถาม: Can I just waatch my friend play?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for schedule.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I just waatch my friend play?",
  "context_resolution": {
    "original_question": "Can I just waatch my friend play?",
    "resolved_question": "Can I just waatch my friend play?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i just waatch my friend play?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I just waatch my friend play?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 44.6,
        "elapsed_sec": 0.0446
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-walk_in-0

คำถาม: ไปหน้าร้านเลย ยังต้องจองมั้ย

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:no_answer`

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ
```


Context / selection trace:

```json
{
  "resolved_question": "ไปหน้าร้านเลย ยังต้องจองมั้ย",
  "context_resolution": {
    "original_question": "ไปหน้าร้านเลย ยังต้องจองมั้ย",
    "resolved_question": "ไปหน้าร้านเลย ยังต้องจองมั้ย",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ไปหน้าร้านเลย ยังต้องจองมั้ย",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ไปหน้าร้านเลย ยังต้องจองมั้ย"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.86,
        "elapsed_sec": 0.0239
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-walk_in-0

คำถาม: Can I turn up without reserving?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I turn up without reserving?",
  "context_resolution": {
    "original_question": "Can I turn up without reserving?",
    "resolved_question": "Can I turn up without reserving?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i turn up without reserving?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I turn up without reserving?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.53,
        "elapsed_sec": 0.0235
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-walk_in-1

คำถาม: Can I walkk in without a booking?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rule_en`

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Can I walkk in without a booking?",
  "context_resolution": {
    "original_question": "Can I walkk in without a booking?",
    "resolved_question": "Can I walkk in without a booking?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i walkk in without a booking?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I walkk in without a booking?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 18.33,
        "elapsed_sec": 0.0183
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-parking-0

คำถาม: ขับมอไซค์ไป จอดตรงไหน

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rag_direct_curated`

```text
PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us, https://esports.computing.psu.ac.th/
```


Context / selection trace:

```json
{
  "resolved_question": "ขับมอไซค์ไป จอดตรงไหน",
  "context_resolution": {
    "original_question": "ขับมอไซค์ไป จอดตรงไหน",
    "resolved_question": "ขับมอไซค์ไป จอดตรงไหน",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ขับมอไซค์ไป จอดตรงไหน",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ขับมอไซค์ไป จอดตรงไหน"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 29.86,
        "elapsed_sec": 0.0299
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-parking-0

คำถาม: Can I park my motorcycle there?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I park my motorcycle there?",
  "context_resolution": {
    "original_question": "Can I park my motorcycle there?",
    "resolved_question": "Can I park my motorcycle there?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i park my motorcycle there?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I park my motorcycle there?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 18.92,
        "elapsed_sec": 0.0189
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-parking-1

คำถาม: Is there parkinng for a car?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:games_unknown_target_en`

```text
I could not find parkinng for a car in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Is there parkinng for a car?",
  "context_resolution": {
    "original_question": "Is there parkinng for a car?",
    "resolved_question": "Is there parkinng for a car?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "is there parkinng for a car?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Is there parkinng for a car?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 21.67,
        "elapsed_sec": 0.0217
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-location-1

คำถาม: Which buillding is the studio in?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Which buillding is the studio in?",
  "context_resolution": {
    "original_question": "Which buillding is the studio in?",
    "resolved_question": "Which buillding is the studio in?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "which buillding is the studio in?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Which buillding is the studio in?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 29.72,
        "elapsed_sec": 0.0297
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-map-1

คำถาม: ขอลิงค์แผนทีไปศูนย์

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?
```


Context / selection trace:

```json
{
  "resolved_question": "ขอลิงค์แผนทีไปศูนย์",
  "context_resolution": {
    "original_question": "ขอลิงค์แผนทีไปศูนย์",
    "resolved_question": "ขอลิงค์แผนทีไปศูนย์",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ขอลิงค์แผนทีไปศูนย์",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ขอลิงค์แผนทีไปศูนย์"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.28,
        "elapsed_sec": 0.0233
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ลิงก์แผนที่ศูนย์: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-map-1

คำถาม: Can I get a maap link to the studio?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I get a maap link to the studio?",
  "context_resolution": {
    "original_question": "Can I get a maap link to the studio?",
    "resolved_question": "Can I get a maap link to the studio?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i get a maap link to the studio?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I get a maap link to the studio?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.47,
        "elapsed_sec": 0.0205
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-checkin_documents-0

คำถาม: เช็กอินใช้พาสปอร์ตได้ปะ

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:no_answer`

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```


Context / selection trace:

```json
{
  "resolved_question": "เช็กอินใช้พาสปอร์ตได้ปะ",
  "context_resolution": {
    "original_question": "เช็กอินใช้พาสปอร์ตได้ปะ",
    "resolved_question": "เช็กอินใช้พาสปอร์ตได้ปะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "เช็กอินใช้พาสปอร์ตได้ปะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "เช็กอินใช้พาสปอร์ตได้ปะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 35.18,
        "elapsed_sec": 0.0352
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-checkin_documents-1

คำถาม: ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์",
  "context_resolution": {
    "original_question": "ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์",
    "resolved_question": "ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.76,
        "elapsed_sec": 0.0248
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-checkin_documents-1

คำถาม: What ID do I need to show on arrival?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "What ID do I need to show on arrival?",
  "context_resolution": {
    "original_question": "What ID do I need to show on arrival?",
    "resolved_question": "What ID do I need to show on arrival?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what id do i need to show on arrival?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What ID do I need to show on arrival?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 25.34,
        "elapsed_sec": 0.0253
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-change_machine-0

คำถาม: เผลอเลือกเครื่องผิดตอนจองแก้ยังไง

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:structured_reservation_fact`

```text
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```


Context / selection trace:

```json
{
  "resolved_question": "เผลอเลือกเครื่องผิดตอนจองแก้ยังไง",
  "context_resolution": {
    "original_question": "เผลอเลือกเครื่องผิดตอนจองแก้ยังไง",
    "resolved_question": "เผลอเลือกเครื่องผิดตอนจองแก้ยังไง",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "เผลอเลือกเครื่องผิดตอนจองแก้ยังไง",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "เผลอเลือกเครื่องผิดตอนจองแก้ยังไง"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.34,
        "elapsed_sec": 0.0243
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-change_machine-1

คำถาม: จองผืดเครื่อง เปลี่ยนได้มั้ย

ไม่ผ่าน: claims_traced

Mode: `pipeline:rag_direct_curated`

```text
เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```


Context / selection trace:

```json
{
  "resolved_question": "จองผืดเครื่อง เปลี่ยนได้มั้ย",
  "context_resolution": {
    "original_question": "จองผืดเครื่อง เปลี่ยนได้มั้ย",
    "resolved_question": "จองผืดเครื่อง เปลี่ยนได้มั้ย",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "จองผืดเครื่อง เปลี่ยนได้มั้ย",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "จองผืดเครื่อง เปลี่ยนได้มั้ย"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 30.43,
        "elapsed_sec": 0.0304
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-change_machine-0

คำถาม: I picked the wrong console in my reservation. How do I fix it?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rule_en`

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "I picked the wrong console in my reservation. How do I fix it?",
  "context_resolution": {
    "original_question": "I picked the wrong console in my reservation. How do I fix it?",
    "resolved_question": "I picked the wrong console in my reservation. How do I fix it?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "i picked the wrong console in my reservation. how do i fix it?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "I picked the wrong console in my reservation. How do I fix it?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.68,
        "elapsed_sec": 0.0247
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you booked the wrong machine, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-change_machine-1

คำถาม: I booked the wrong machne. How do I fix it?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for reservation.
```


Context / selection trace:

```json
{
  "resolved_question": "I booked the wrong machne. How do I fix it?",
  "context_resolution": {
    "original_question": "I booked the wrong machne. How do I fix it?",
    "resolved_question": "I booked the wrong machne. How do I fix it?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "i booked the wrong machne. how do i fix it?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "I booked the wrong machne. How do I fix it?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 31.68,
        "elapsed_sec": 0.0317
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you booked the wrong machine, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-change_time-0

คำถาม: อยากย้ายเวลาที่จองไว้ทำไง

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:no_answer`

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ
```


Context / selection trace:

```json
{
  "resolved_question": "อยากย้ายเวลาที่จองไว้ทำไง",
  "context_resolution": {
    "original_question": "อยากย้ายเวลาที่จองไว้ทำไง",
    "resolved_question": "อยากย้ายเวลาที่จองไว้ทำไง",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "topic_shift",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "อยากย้ายเวลาที่จองไว้ทำไง",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "อยากย้ายเวลาที่จองไว้ทำไง"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.22,
        "elapsed_sec": 0.0232
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
หากต้องการเปลี่ยนเวลาจอง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-change_time-0

คำถาม: Can I move my reservation to a different time?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rule_en`

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Can I move my reservation to a different time?",
  "context_resolution": {
    "original_question": "Can I move my reservation to a different time?",
    "resolved_question": "Can I move my reservation to a different time?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i move my reservation to a different time?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I move my reservation to a different time?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.31,
        "elapsed_sec": 0.0243
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
To change the booking time, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-personal_keyboard_mouse-0

คำถาม: เอาเม้าส์ของผมไปเสียบได้ปะ

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "เอาเม้าส์ของผมไปเสียบได้ปะ",
  "context_resolution": {
    "original_question": "เอาเม้าส์ของผมไปเสียบได้ปะ",
    "resolved_question": "เอาเม้าส์ของผมไปเสียบได้ปะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "เอาเม้าส์ของผมไปเสียบได้ปะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "เอาเม้าส์ของผมไปเสียบได้ปะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 25.14,
        "elapsed_sec": 0.0251
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-personal_keyboard_mouse-1

คำถาม: เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย",
  "context_resolution": {
    "original_question": "เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย",
    "resolved_question": "เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.87,
        "elapsed_sec": 0.0249
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-personal_keyboard_mouse-1

คำถาม: Can I bring my own keyboarrd?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I bring my own keyboarrd?",
  "context_resolution": {
    "original_question": "Can I bring my own keyboarrd?",
    "resolved_question": "Can I bring my own keyboarrd?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i bring my own keyboarrd?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I bring my own keyboarrd?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 18.71,
        "elapsed_sec": 0.0187
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-wrong_slip-0

คำถาม: ส่งรูปหลักฐานโอนผิด แก้ตรงไหน

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rag_direct_curated`

```text
PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us
```


Context / selection trace:

```json
{
  "resolved_question": "ส่งรูปหลักฐานโอนผิด แก้ตรงไหน",
  "context_resolution": {
    "original_question": "ส่งรูปหลักฐานโอนผิด แก้ตรงไหน",
    "resolved_question": "ส่งรูปหลักฐานโอนผิด แก้ตรงไหน",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ส่งรูปหลักฐานโอนผิด แก้ตรงไหน",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ส่งรูปหลักฐานโอนผิด แก้ตรงไหน"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.06,
        "elapsed_sec": 0.0231
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-wrong_slip-1

คำถาม: แนบสะลิปผิดรูปทำไง

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "แนบสะลิปผิดรูปทำไง",
  "context_resolution": {
    "original_question": "แนบสะลิปผิดรูปทำไง",
    "resolved_question": "แนบสะลิปผิดรูปทำไง",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "no_matching_context_resolution",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "แนบสะลิปผิดรูปทำไง",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "แนบสะลิปผิดรูปทำไง"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.48,
        "elapsed_sec": 0.0205
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-wrong_slip-0

คำถาม: I attached the incorrect transfer receipt image. How can I replace it?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:user_service_facts`

```text
The procedure for obtaining a quotation or receipt has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "I attached the incorrect transfer receipt image. How can I replace it?",
  "context_resolution": {
    "original_question": "I attached the incorrect transfer receipt image. How can I replace it?",
    "resolved_question": "I attached the incorrect transfer receipt image. How can I replace it?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "i attached the incorrect transfer receipt image. how can i replace it?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "I attached the incorrect transfer receipt image. How can I replace it?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 24.16,
        "elapsed_sec": 0.0242
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "missing",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [],
        "source_items": [],
        "missing_fields": [
          "quotation_receipt_procedure"
        ],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "no_answer",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-wrong_slip-1

คำถาม: Uploaded the wrong payment sllip, how do I fix it?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Uploaded the wrong payment sllip, how do I fix it?",
  "context_resolution": {
    "original_question": "Uploaded the wrong payment sllip, how do I fix it?",
    "resolved_question": "Uploaded the wrong payment sllip, how do I fix it?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "uploaded the wrong payment sllip, how do i fix it?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Uploaded the wrong payment sllip, how do I fix it?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.5,
        "elapsed_sec": 0.0235
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-combined_transfer-0

คำถาม: จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:structured_reservation_fact`

```text
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```


Context / selection trace:

```json
{
  "resolved_question": "จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม",
  "context_resolution": {
    "original_question": "จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม",
    "resolved_question": "จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 26.45,
        "elapsed_sec": 0.0264
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-combined_transfer-1

คำถาม: จองหลายเครื่องโอนครังเดียวได้ปะ

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:rag_direct_curated`

```text
ตอนจองต้องกรอกรหัส ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และแนบสลิปหลังโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```


Context / selection trace:

```json
{
  "resolved_question": "จองหลายเครื่องโอนครังเดียวได้ปะ",
  "context_resolution": {
    "original_question": "จองหลายเครื่องโอนครังเดียวได้ปะ",
    "resolved_question": "จองหลายเครื่องโอนครังเดียวได้ปะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "จองหลายเครื่องโอนครังเดียวได้ปะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "จองหลายเครื่องโอนครังเดียวได้ปะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 21.46,
        "elapsed_sec": 0.0215
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-combined_transfer-1

คำถาม: Can I pay multiple bookings with one transferr?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I pay multiple bookings with one transferr?",
  "context_resolution": {
    "original_question": "Can I pay multiple bookings with one transferr?",
    "resolved_question": "Can I pay multiple bookings with one transferr?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i pay multiple bookings with one transferr?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I pay multiple bookings with one transferr?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 29.27,
        "elapsed_sec": 0.0293
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-group_checkin-0

คำถาม: Can I check everyone in before my friends arrive?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for schedule.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I check everyone in before my friends arrive?",
  "context_resolution": {
    "original_question": "Can I check everyone in before my friends arrive?",
    "resolved_question": "Can I check everyone in before my friends arrive?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i check everyone in before my friends arrive?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I check everyone in before my friends arrive?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.2,
        "elapsed_sec": 0.0202
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-group_checkin-1

คำถาม: Can I check-in for the whoole group?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for reservation.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I check-in for the whoole group?",
  "context_resolution": {
    "original_question": "Can I check-in for the whoole group?",
    "resolved_question": "Can I check-in for the whoole group?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i checkin for the whoole group?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I check-in for the whoole group?",
          "can i checkin for the whoole group?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 9.51,
        "elapsed_sec": 0.0095
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-rest_seating-0

คำถาม: มีโซนให้นั่งรอพักไหม

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:structured_equipment_catalog`

```text
อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```


Context / selection trace:

```json
{
  "resolved_question": "มีโซนให้นั่งรอพักไหม",
  "context_resolution": {
    "original_question": "มีโซนให้นั่งรอพักไหม",
    "resolved_question": "มีโซนให้นั่งรอพักไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "มีโซนให้นั่งรอพักไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "มีโซนให้นั่งรอพักไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.53,
        "elapsed_sec": 0.0205
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่นั่งพักตรงโซนกลางห้องครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-new-rest_seating-1

คำถาม: มีที่นังพักไหม

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "มีที่นังพักไหม",
  "context_resolution": {
    "original_question": "มีที่นังพักไหม",
    "resolved_question": "มีที่นังพักไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "มีที่นังพักไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "มีที่นังพักไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 22.68,
        "elapsed_sec": 0.0227
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่นั่งพักตรงโซนกลางห้องครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-rest_seating-0

คำถาม: Is there a waiting area where I can rest?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:games_unknown_target_en`

```text
I could not find waiting area where I can rest in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Is there a waiting area where I can rest?",
  "context_resolution": {
    "original_question": "Is there a waiting area where I can rest?",
    "resolved_question": "Is there a waiting area where I can rest?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "is there a waiting area where i can rest?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Is there a waiting area where I can rest?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 31.24,
        "elapsed_sec": 0.0312
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Rest seating is available in the central area of the room.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-new-rest_seating-1

คำถาม: Is there a reest area?

ไม่ผ่าน: required_content, claims_traced

Mode: `pipeline:games_unknown_target_en`

```text
I could not find reest area in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Is there a reest area?",
  "context_resolution": {
    "original_question": "Is there a reest area?",
    "resolved_question": "Is there a reest area?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "is there a reest area?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Is there a reest area?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 42.41,
        "elapsed_sec": 0.0424
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Rest seating is available in the central area of the room.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-multi-mouse-controller

คำถาม: เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ

ไม่ผ่าน: missing_fields

Mode: `pipeline:user_service_facts`

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ",
  "context_resolution": {
    "original_question": "เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ",
    "resolved_question": "เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "no_matching_context_resolution",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 29.14,
        "elapsed_sec": 0.0291
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "personal_keyboard_mouse"
        ],
        "source_items": [
          27
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-parking-moto

คำถาม: มีที่จอดรถไหม → แล้วมอเตอร์ไซค์ล่ะ

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:candidate_margin_clarification`

```text
ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วมอเตอร์ไซค์ล่ะ",
  "context_resolution": {
    "original_question": "แล้วมอเตอร์ไซค์ล่ะ",
    "resolved_question": "แล้วมอเตอร์ไซค์ล่ะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "no_matching_context_resolution",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "แล้วมอเตอร์ไซค์ล่ะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "แล้วมอเตอร์ไซค์ล่ะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.94,
        "elapsed_sec": 0.0239
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-parking-free

คำถาม: มีที่จอดรถไหม → ฟรีไหม

ไม่ผ่าน: required_content, claims_traced, missing_fields, context_used

Mode: `pipeline:rag_direct_curated`

```text
ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```


Context / selection trace:

```json
{
  "resolved_question": "ฟรีไหม",
  "context_resolution": {
    "original_question": "ฟรีไหม",
    "resolved_question": "ฟรีไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ฟรีไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ฟรีไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 12.42,
        "elapsed_sec": 0.0124
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

ยังไม่ได้ระบุค่าจอดรถ จึงยืนยันว่าจอดฟรีไม่ได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-map-after-location

คำถาม: ศูนย์อยู่ตรงไหน → ขอลิงก์หน่อย

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ขอลิงก์หน่อย",
  "context_resolution": {
    "original_question": "ขอลิงก์หน่อย",
    "resolved_question": "ขอลิงก์หน่อย",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ขอลิงก์หน่อย",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ขอลิงก์หน่อย"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 15.86,
        "elapsed_sec": 0.0159
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ลิงก์แผนที่ศูนย์: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-passport

คำถาม: ตอนมาถึงต้องแสดงหลักฐานอะไร → passport ล่ะ

ไม่ผ่าน: context_used

Mode: `pipeline:user_service_facts`

```text
เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "passport ล่ะ",
  "context_resolution": {
    "original_question": "passport ล่ะ",
    "resolved_question": "passport ล่ะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "passport ล่ะ",
      "metadata": {
        "language_hint": "mixed_th_en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "passport ล่ะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 23.79,
        "elapsed_sec": 0.0238
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "checkin_documents"
        ],
        "source_items": [
          17
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-own-mouse

คำถาม: เอาคีย์บอร์ดส่วนตัวมาได้ไหม → แล้วเมาส์ล่ะ

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:ambiguity_clarification`

```text
คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วเมาส์ล่ะ",
  "context_resolution": {
    "original_question": "แล้วเมาส์ล่ะ",
    "resolved_question": "แล้วเมาส์ล่ะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "no_matching_context_resolution",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "แล้วเมาส์ล่ะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "แล้วเมาส์ล่ะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 15.57,
        "elapsed_sec": 0.0156
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-own-controller

คำถาม: เอาคีย์บอร์ดส่วนตัวมาได้ไหม → แล้วจอยล่ะ

ไม่ผ่าน: missing_fields, context_used

Mode: `pipeline:ambiguity_clarification`

```text
คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วจอยล่ะ",
  "context_resolution": {
    "original_question": "แล้วจอยล่ะ",
    "resolved_question": "แล้วจอยล่ะ",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "no_matching_context_resolution",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "แล้วจอยล่ะ",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "แล้วจอยล่ะ"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 14.41,
        "elapsed_sec": 0.0144
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-transfer-note

คำถาม: จองหลายเครื่องโอนครั้งเดียวได้ไหม → ต้องเขียนอะไรใน note

ไม่ผ่าน: required_content, claims_traced, missing_fields, context_used

Mode: `pipeline:no_answer`

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```


Context / selection trace:

```json
{
  "resolved_question": "ต้องเขียนอะไรใน note",
  "context_resolution": {
    "original_question": "ต้องเขียนอะไรใน note",
    "resolved_question": "ต้องเขียนอะไรใน note",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ต้องเขียนอะไรใน note",
      "metadata": {
        "language_hint": "mixed_th_en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ต้องเขียนอะไรใน note"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 65.69,
        "elapsed_sec": 0.0657
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-slip-contact

คำถาม: แนบสลิปผิดรูปแก้ยังไง → ส่งที่ไหน

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ส่งที่ไหน",
  "context_resolution": {
    "original_question": "ส่งที่ไหน",
    "resolved_question": "ส่งที่ไหน",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ส่งที่ไหน",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ส่งที่ไหน"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 14.09,
        "elapsed_sec": 0.0141
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-waiting-point

คำถาม: มีที่นั่งพักไหม → ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม

ไม่ผ่าน: context_used

Mode: `pipeline:user_service_facts`

```text
มีที่นั่งพักตรงโซนกลางห้องครับ

ยังไม่ได้ยืนยันว่าโซนกลางห้องเป็นจุดรอรอบจองโดยเฉพาะครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม",
  "context_resolution": {
    "original_question": "ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม",
    "resolved_question": "ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม",
      "metadata": {
        "language_hint": "th",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.99,
        "elapsed_sec": 0.021
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "partial",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "rest_seating"
        ],
        "source_items": [
          50
        ],
        "missing_fields": [
          "designated_waiting_point"
        ],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_partial",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่นั่งพักตรงโซนกลางห้องครับ

ยังไม่ได้ยืนยันว่าโซนกลางห้องเป็นจุดรอรอบจองโดยเฉพาะครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-scope-steam-member

คำถาม: Steam ต้องเป็นสมาชิกก่อนไหม

ไม่ผ่าน: separate_scope

Mode: `pipeline:user_service_facts`

```text
ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "Steam ต้องเป็นสมาชิกก่อนไหม",
  "context_resolution": {
    "original_question": "Steam ต้องเป็นสมาชิกก่อนไหม",
    "resolved_question": "Steam ต้องเป็นสมาชิกก่อนไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "steam ต้องเป็นสมาชิกก่อนไหม",
      "metadata": {
        "language_hint": "mixed_th_en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Steam ต้องเป็นสมาชิกก่อนไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 21.91,
        "elapsed_sec": 0.0219
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "membership"
        ],
        "source_items": [
          2
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
```

### th-scope-team-member

คำถาม: สมาชิกทีม VALORANT ต้องมีกี่คน

ไม่ผ่าน: separate_scope

Mode: `pipeline:user_service_facts`

```text
ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "สมาชิกทีม VALORANT ต้องมีกี่คน",
  "context_resolution": {
    "original_question": "สมาชิกทีม VALORANT ต้องมีกี่คน",
    "resolved_question": "สมาชิกทีม VALORANT ต้องมีกี่คน",
    "used_context": false,
    "context_game": "VALORANT",
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "question_has_explicit_game",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "สมาชิกทีม valorant ต้องมีกี่คน",
      "metadata": {
        "language_hint": "mixed_th_en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "สมาชิกทีม VALORANT ต้องมีกี่คน"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 42.16,
        "elapsed_sec": 0.0422
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "membership"
        ],
        "source_items": [
          2
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
```

### th-scope-dl-games

คำถาม: โหลดเกมเองลง PC ได้ไหม

ไม่ผ่าน: missing_fields

Mode: `pipeline:no_answer`

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```


Context / selection trace:

```json
{
  "resolved_question": "โหลดเกมเองลง PC ได้ไหม",
  "context_resolution": {
    "original_question": "โหลดเกมเองลง PC ได้ไหม",
    "resolved_question": "โหลดเกมเองลง PC ได้ไหม",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "not_followup",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "โหลดเกมเองลง pc ได้ไหม",
      "metadata": {
        "language_hint": "mixed_th_en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "โหลดเกมเองลง PC ได้ไหม"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 60.06,
        "elapsed_sec": 0.0601
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ยังไม่ได้ยืนยันว่าให้ขอลงเกมเพิ่มหรือติดตั้งเกม โปรแกรม หรือ mod เองได้หรือไม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-multi-mouse-controller

คำถาม: Can I bring my own mouse, and what about my own controller?

ไม่ผ่าน: missing_fields

Mode: `pipeline:user_service_facts`

```text
Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "Can I bring my own mouse, and what about my own controller?",
  "context_resolution": {
    "original_question": "Can I bring my own mouse, and what about my own controller?",
    "resolved_question": "Can I bring my own mouse, and what about my own controller?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i bring my own mouse, and what about my own controller?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I bring my own mouse, and what about my own controller?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 81.88,
        "elapsed_sec": 0.0819
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "personal_keyboard_mouse"
        ],
        "source_items": [
          27
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Personal keyboards and mice are not allowed for general studio use.



The confirmed restriction covers personal keyboards and mice. Permission to bring a personal controller has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-parking-moto

คำถาม: Is there parking? → What about motorcycles?

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "What about motorcycles?",
  "context_resolution": {
    "original_question": "What about motorcycles?",
    "resolved_question": "What about motorcycles?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what about motorcycles?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What about motorcycles?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 25.84,
        "elapsed_sec": 0.0258
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-parking-free

คำถาม: Is there parking? → Is it free?

ไม่ผ่าน: required_content, claims_traced, missing_fields, context_used

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Is it free?",
  "context_resolution": {
    "original_question": "Is it free?",
    "resolved_question": "Is it free?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "is it free?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Is it free?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 14.64,
        "elapsed_sec": 0.0146
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Parking fees have not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-map-after-location

คำถาม: Where is the studio? → Can I get the link?

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I get the link?",
  "context_resolution": {
    "original_question": "Can I get the link?",
    "resolved_question": "Can I get the link?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i get the link?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I get the link?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 22.21,
        "elapsed_sec": 0.0222
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-passport

คำถาม: What identification do I show on arrival? → And a passport?

ไม่ผ่าน: context_used

Mode: `pipeline:user_service_facts`

```text
At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "And a passport?",
  "context_resolution": {
    "original_question": "And a passport?",
    "resolved_question": "And a passport?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "and a passport?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "And a passport?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 19.95,
        "elapsed_sec": 0.02
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "checkin_documents"
        ],
        "source_items": [
          17
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-own-mouse

คำถาม: Can I bring my own keyboard? → What about a mouse?

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:structured_equipment_catalog_en`

```text
Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about a mouse?",
  "context_resolution": {
    "original_question": "What about a mouse?",
    "resolved_question": "What about a mouse?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what about a mouse?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What about a mouse?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 21.08,
        "elapsed_sec": 0.0211
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-own-controller

คำถาม: Can I bring my own keyboard? → What about a controller?

ไม่ผ่าน: missing_fields, context_used

Mode: `pipeline:structured_games_catalog_en`

```text
There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 games)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about a controller?",
  "context_resolution": {
    "original_question": "What about a controller?",
    "resolved_question": "What about a controller?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what about a controller?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What about a controller?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 20.72,
        "elapsed_sec": 0.0207
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The confirmed restriction covers personal keyboards and mice. Permission to bring a personal controller has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-transfer-note

คำถาม: Can I make one transfer for multiple machines? → What should I write in the note?

ไม่ผ่าน: required_content, claims_traced, missing_fields, context_used

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "What should I write in the note?",
  "context_resolution": {
    "original_question": "What should I write in the note?",
    "resolved_question": "What should I write in the note?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what should i write in the note?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What should I write in the note?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 17.97,
        "elapsed_sec": 0.018
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.

You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.



A note is required at booking for studio verification, but the exact wording or note format has not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-slip-contact

คำถาม: How do I fix a wrong slip image? → Where should I send it?

ไม่ผ่าน: required_content, claims_traced, context_used

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Where should I send it?",
  "context_resolution": {
    "original_question": "Where should I send it?",
    "resolved_question": "Where should I send it?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "where should i send it?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Where should I send it?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 36.55,
        "elapsed_sec": 0.0366
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-waiting-point

คำถาม: Is there a rest area? → Can I wait there before my booking?

ไม่ผ่าน: required_content, claims_traced, missing_fields, context_used

Mode: `pipeline:rule_en`

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Can I wait there before my booking?",
  "context_resolution": {
    "original_question": "Can I wait there before my booking?",
    "resolved_question": "Can I wait there before my booking?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can i wait there before my booking?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can I wait there before my booking?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 19.77,
        "elapsed_sec": 0.0198
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Rest seating is available in the central area of the room.

The central rest seating has not been confirmed as the designated waiting point for an upcoming booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-time-shift-date

คำถาม: Can I change my booking time? → What about changing the date?

ไม่ผ่าน: missing_fields

Mode: `pipeline:structured_game_detail_en`

```text
Verified English information:
The Last of Us Part I / Part II
Genre: Action-Adventure / Survival
Overview: The Last of Us is an adventure survival game that emphasizes storytelling, stealth, and resource management.
How to play: Explore, seize opportunities stealthily, fight, gather resources, and progress through various missions
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about changing the date?",
  "context_resolution": {
    "original_question": "What about changing the date?",
    "resolved_question": "What about changing the date?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "what about changing the last of us part i / part ii?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "What about changing The Last of Us Part I / Part II?",
          "What about changing the date?",
          "What about changing the date? The Last of Us Part I / Part II"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 32.71,
        "elapsed_sec": 0.0327
      }
    },
    {
      "stage": "preprocess",
      "decision": "kept_original_query",
      "confidence": 0.88,
      "detail": "What about changing The Last of Us Part I / Part II?",
      "metadata": {
        "candidates": [
          {
            "query": "What about changing the date?",
            "category": "games",
            "intent": "games_lookup",
            "confidence": 0.88
          },
          {
            "query": "What about changing the date? The Last of Us Part I / Part II",
            "category": "games",
            "intent": "games_lookup",
            "confidence": 0.88
          }
        ]
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The supplied answers say a paid booking with the wrong date can change date, but also say rescheduling instead of a refund is not allowed. The exception and processing channel still need clarification.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-scope-steam-member

คำถาม: Does Steam require membership?

ไม่ผ่าน: separate_scope

Mode: `pipeline:user_service_facts`

```text
Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "Does Steam require membership?",
  "context_resolution": {
    "original_question": "Does Steam require membership?",
    "resolved_question": "Does Steam require membership?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "does steam require membership?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Does Steam require membership?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 29.75,
        "elapsed_sec": 0.0297
      }
    },
    {
      "stage": "user_service_facts",
      "decision": "answered",
      "confidence": 0.98,
      "detail": "do not infer unanswered policies",
      "metadata": {
        "claim_ids": [
          "membership"
        ],
        "source_items": [
          2
        ],
        "missing_fields": [],
        "basis": "user_provided_in_this_chat",
        "english_status": "agent_translation_from_user_confirmed_thai",
        "outcome": "answered_complete",
        "recorded_rule_ids": []
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.
```

### en-scope-other-payer

คำถาม: Can my friend pay for multiple machines using their account?

ไม่ผ่าน: missing_fields

Mode: `pipeline:rule_en`

```text
Payment is made by bank transfer via Siam Commercial Bank, account name PSU Esports Studio - Phuket, account number 795-276244-1, with the payment slip uploaded.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Can my friend pay for multiple machines using their account?",
  "context_resolution": {
    "original_question": "Can my friend pay for multiple machines using their account?",
    "resolved_question": "Can my friend pay for multiple machines using their account?",
    "used_context": false,
    "context_game": null,
    "context_domain": null,
    "context_operation": null,
    "context_topic": null,
    "reason": "english_context_preserved_without_rewrite",
    "selected_requests": [],
    "selection_errors": []
  },
  "trace": [
    {
      "stage": "preprocess",
      "decision": "normalized",
      "confidence": 1.0,
      "detail": "can my friend pay for multiple machines using their account?",
      "metadata": {
        "language_hint": "en",
        "nonsemantic_preface_removed": false,
        "query_variants": [
          "Can my friend pay for multiple machines using their account?"
        ],
        "competition_name_recovery": [],
        "elapsed_ms": 22.14,
        "elapsed_sec": 0.0221
      }
    }
  ]
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Payment from a friend's bank account has not been confirmed. Permission for one transfer covering multiple machines does not establish who may pay.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

## HTTP debug=False r49.1


### th-follow-parking-moto

คำถาม: มีที่จอดรถไหม → แล้วมอเตอร์ไซค์ล่ะ

ไม่ผ่าน: content

Mode: `pipeline:candidate_margin_clarification`

```text
ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วมอเตอร์ไซค์ล่ะ",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-parking-free

คำถาม: มีที่จอดรถไหม → ฟรีไหม

ไม่ผ่าน: content, missing_is_explicit, not_complete

Mode: `pipeline:rag_direct_curated`

```text
ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```


Context / selection trace:

```json
{
  "resolved_question": "ฟรีไหม",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

ยังไม่ได้ระบุค่าจอดรถ จึงยืนยันว่าจอดฟรีไม่ได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-map-after-location

คำถาม: ศูนย์อยู่ตรงไหน → ขอลิงก์หน่อย

ไม่ผ่าน: content

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ขอลิงก์หน่อย",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ลิงก์แผนที่ศูนย์: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-own-mouse

คำถาม: เอาคีย์บอร์ดส่วนตัวมาได้ไหม → แล้วเมาส์ล่ะ

ไม่ผ่าน: content

Mode: `pipeline:ambiguity_clarification`

```text
คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วเมาส์ล่ะ",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-own-controller

คำถาม: เอาคีย์บอร์ดส่วนตัวมาได้ไหม → แล้วจอยล่ะ

ไม่ผ่าน: missing_is_explicit, not_complete

Mode: `pipeline:ambiguity_clarification`

```text
คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`
```


Context / selection trace:

```json
{
  "resolved_question": "แล้วจอยล่ะ",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-transfer-note

คำถาม: จองหลายเครื่องโอนครั้งเดียวได้ไหม → ต้องเขียนอะไรใน note

ไม่ผ่าน: content

Mode: `pipeline:user_service_facts`

```text
ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "ต้องเขียนอะไรใน note",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-slip-contact

คำถาม: แนบสลิปผิดรูปแก้ยังไง → ส่งที่ไหน

ไม่ผ่าน: content

Mode: `pipeline:candidate_margin_clarification`

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```


Context / selection trace:

```json
{
  "resolved_question": "ส่งที่ไหน",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-ambiguity-free

คำถาม: มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม → ฟรีไหม

ไม่ผ่าน: clarification

Mode: `pipeline:rag_direct_curated`

```text
ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```


Context / selection trace:

```json
{
  "resolved_question": "ฟรีไหม",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
ต้องการถามว่าอะไรฟรีครับ: ที่จอดรถ / การนั่งดูเพื่อน?
```

### th-select-parking-fee

คำถาม: มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม → ฟรีไหม → ที่จอดรถ

ไม่ผ่าน: missing_is_explicit, not_complete

Mode: `pipeline:user_service_facts`

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "ที่จอดรถ",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

ยังไม่ได้ระบุค่าจอดรถ จึงยืนยันว่าจอดฟรีไม่ได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-watch-free

คำถาม: นั่งดูเพื่อนได้ไหม → ฟรีไหม

ไม่ผ่าน: content, missing_is_explicit, not_complete

Mode: `pipeline:rag_direct_curated`

```text
ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 140 บาท. Nintendo Switch 1 ชั่วโมง 3-4 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 100 บาท, General Adult 280 บาท. Cockpit 1 ชั่วโมง 1 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 65 บาท, General Adult 200 บาท. VR 30 นาที 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท. VR 1 ชั่วโมง 1-5 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท. ภาพนี้ระบุว่าค่าบริการมีผลตั้งแต่ 1 February 2026 ถึง 31 March 2026 และไม่ปรากฏราคา PC
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```


Context / selection trace:

```json
{
  "resolved_question": "ฟรีไหม",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
สามารถมานั่งดูเพื่อนเล่นได้ครับ

ยังไม่ได้ระบุค่าเข้าชมหรือยืนยันว่าเข้าดูเพื่อนฟรีครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-parking-moto

คำถาม: Is there parking? → What about motorcycles?

ไม่ผ่าน: content

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "What about motorcycles?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-parking-free

คำถาม: Is there parking? → Is it free?

ไม่ผ่าน: content, missing_is_explicit

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Is it free?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Parking fees have not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-map-after-location

คำถาม: Where is the studio? → Can I get the link?

ไม่ผ่าน: content

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Can I get the link?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-own-mouse

คำถาม: Can I bring my own keyboard? → What about a mouse?

ไม่ผ่าน: content

Mode: `pipeline:structured_equipment_catalog_en`

```text
Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about a mouse?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-own-controller

คำถาม: Can I bring my own keyboard? → What about a controller?

ไม่ผ่าน: missing_is_explicit, not_complete

Mode: `pipeline:structured_games_catalog_en`

```text
There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 games)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about a controller?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The confirmed restriction covers personal keyboards and mice. Permission to bring a personal controller has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-transfer-note

คำถาม: Can I make one transfer for multiple machines? → What should I write in the note?

ไม่ผ่าน: content

Mode: `pipeline:user_service_facts`

```text
A note is required at booking for studio verification, but the exact wording or note format has not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "What should I write in the note?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.

You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.



A note is required at booking for studio verification, but the exact wording or note format has not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-slip-contact

คำถาม: How do I fix a wrong slip image? → Where should I send it?

ไม่ผ่าน: content

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Where should I send it?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-waiting-point

คำถาม: Is there a rest area? → Can I wait there before my booking?

ไม่ผ่าน: content, missing_is_explicit, not_complete

Mode: `pipeline:rule_en`

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "Can I wait there before my booking?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Rest seating is available in the central area of the room.

The central rest seating has not been confirmed as the designated waiting point for an upcoming booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-follow-time-shift-date

คำถาม: Can I change my booking time? → What about changing the date?

ไม่ผ่าน: missing_is_explicit, not_complete

Mode: `pipeline:structured_game_detail_en`

```text
Verified English information:
The Last of Us Part I / Part II
Genre: Action-Adventure / Survival
Overview: The Last of Us is an adventure survival game that emphasizes storytelling, stealth, and resource management.
How to play: Explore, seize opportunities stealthily, fight, gather resources, and progress through various missions
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```


Context / selection trace:

```json
{
  "resolved_question": "What about changing the date?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
The supplied answers say a paid booking with the wrong date can change date, but also say rescheduling instead of a refund is not allowed. The exception and processing channel still need clarification.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-ambiguity-free

คำถาม: Is there parking and can I watch my friends? → Is it free?

ไม่ผ่าน: clarification

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Is it free?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Which item do you mean is free: parking / watching friends?
```

### en-select-parking-fee

คำถาม: Is there parking and can I watch my friends? → Is it free? → parking

ไม่ผ่าน: missing_is_explicit, not_complete

Mode: `pipeline:user_service_facts`

```text
Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```


Context / selection trace:

```json
{
  "resolved_question": "parking",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
Parking for cars and motorcycles is available in front of Building 5.

Parking fees have not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### en-watch-free

คำถาม: Can I watch my friends? → Is it free?

ไม่ผ่าน: content, missing_is_explicit

Mode: `pipeline:english_no_answer`

```text
I could not find verified PSU Esports Studio - Phuket information for this question.
```


Context / selection trace:

```json
{
  "resolved_question": "Is it free?",
  "context_resolution": null,
  "trace": []
}
```


คำตอบหลังแก้ r49.2 (ผ่าน=True):

```text
You may sit and watch your friends play.

A spectator fee or free admission has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```
