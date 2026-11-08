# ทุก acceptance variant ที่ไม่ผ่าน

ข้อที่ C07 เปลี่ยน oracle ให้รายงานแยกจากการเทียบ R102; ห้ามอ้างว่าทุกคะแนนที่เพิ่มมาจาก runtime

## C01_en_2

คำถาม: All prcies for external visitors?

ไม่ผ่าน: exhaustive two service price scope

```text
**Service rate**
• Price: 100.00 THB [S1]
• Service: PC [S2]
• User group: External Visitors [S3]
• currency: THB [S4]
• Billing unit: per_hour [S5]
• Duration (minutes): 60 [S6]
• Calculation rule: Confirmed proportional calculation [S7]

**Service rate**
• Price: 120.00 THB [S8]
• Service: VR [S9]
• User group: External Visitors [S10]
• currency: THB [S11]
• Billing unit: per_hour [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Confirmed proportional calculation [S14]

English translation is machine generated and has not been reviewed by the owner.
```

validation: {"ok": true, "errors": [], "warnings": []}

## C08_th_0

คำถาม: ROV

ไม่ผ่าน: precondition game selection pending, disconnect scope inherited

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**เกมหลุด**
fx_event [S1]
เกมหลุด [S2]
เกมหลุดให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง ยกเว้นกรรมการอนุญาต RULE_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C08_th_1

คำถาม: ขอถามหน่อย ROV ครับ

ไม่ผ่าน: precondition game selection pending, disconnect scope inherited

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**เกมหลุด**
fx_event [S1]
เกมหลุด [S2]
เกมหลุดให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง ยกเว้นกรรมการอนุญาต RULE_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C08_th_2

คำถาม: ROV?

ไม่ผ่าน: precondition game selection pending, disconnect scope inherited

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**เกมหลุด**
fx_event [S1]
เกมหลุด [S2]
เกมหลุดให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง ยกเว้นกรรมการอนุญาต RULE_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C08_th_3

คำถาม: ROV ตอบสั้น ๆ

ไม่ผ่าน: precondition game selection pending, disconnect scope inherited

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**เกมหลุด**
fx_event [S1]
เกมหลุด [S2]
เกมหลุดให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง ยกเว้นกรรมการอนุญาต RULE_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C10_th_0

คำถาม: ขอเกมทั้งหมด

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_th_1

คำถาม: ขอถามหน่อย ขอเกมทั้งหมด ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_th_2

คำถาม: ขอเกมทั้งหมด?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_th_3

คำถาม: ขอเกมทั้งหมด ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_auto_0

คำถาม: ขอเกมทั้งหมด

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_auto_1

คำถาม: ขอถามหน่อย ขอเกมทั้งหมด ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_auto_2

คำถาม: ขอเกมทั้งหมด?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C10_auto_3

คำถาม: ขอเกมทั้งหมด ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C12_th_0

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_th_1

คำถาม: ขอถามหน่อย ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_th_2

คำถาม: ราาคาและวิธีจอง PC สำหรับบุคคลภายนอก?

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_th_3

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_auto_0

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_auto_1

คำถาม: ขอถามหน่อย ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_auto_2

คำถาม: ราาคาและวิธีจอง PC สำหรับบุคคลภายนอก?

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C12_auto_3

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_th_0

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_th_1

คำถาม: ขอถามหน่อย กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ครับ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_th_2

คำถาม: กฏ ROV ก่อนกับหลัง First Blood ต่างกันยังไง?

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_th_3

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ตอบสั้น ๆ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_en_0

คำถาม: ROV competition rules before and after First Blood

ไม่ผ่าน: before/after linked clauses preserved

```text
Rulebook — ROV Fixture Tournament

**After First Blood**
fx_event [S1]
After First Blood [S2]
After First Blood do not restart unless the referee permits it. AFTER_EXCEPTION [S3]
complete [S4]
None (confirmed) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_en_1

คำถาม: Could you help me with this: ROV competition rules before and after First Blood

ไม่ผ่าน: before/after linked clauses preserved

```text
Rulebook — ROV Fixture Tournament

**After First Blood**
fx_event [S1]
After First Blood [S2]
After First Blood do not restart unless the referee permits it. AFTER_EXCEPTION [S3]
complete [S4]
None (confirmed) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_en_2

คำถาม: ROV competition rules before and after First Blood?

ไม่ผ่าน: before/after linked clauses preserved

```text
Rulebook — ROV Fixture Tournament

**After First Blood**
fx_event [S1]
After First Blood [S2]
After First Blood do not restart unless the referee permits it. AFTER_EXCEPTION [S3]
complete [S4]
None (confirmed) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_en_3

คำถาม: ROV competition rules before and after First Blood. Please be brief.

ไม่ผ่าน: before/after linked clauses preserved

```text
Rulebook — ROV Fixture Tournament

**After First Blood**
fx_event [S1]
After First Blood [S2]
After First Blood do not restart unless the referee permits it. AFTER_EXCEPTION [S3]
complete [S4]
None (confirmed) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_auto_0

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_auto_1

คำถาม: ขอถามหน่อย กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ครับ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_auto_2

คำถาม: กฏ ROV ก่อนกับหลัง First Blood ต่างกันยังไง?

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C21_auto_3

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ตอบสั้น ๆ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกาตามเอกสาร — แข่ง ROV ทดลอง

**หลัง First Blood**
fx_event [S1]
หลัง First Blood [S2]
หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION [S3]
complete [S4]
ไม่มี (ยืนยันแล้ว) [S5]
```

validation: {"ok": true, "errors": [], "warnings": []}

## C29_th_0

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_th_1

คำถาม: ขอถามหน่อย เกมเอทดลอง เล่นได้ที่ไหน ครับ

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_th_2

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน?

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_th_3

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน ตอบสั้น ๆ

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_en_0

คำถาม: Where can I play Game A Fixture?

ไม่ผ่าน: runtime validation

```text
Game: Game A Fixture

No confirmed game_service data for this scope.

offered: No confirmed answer for this detail in the selected scope.

service id: No confirmed answer for this detail in the selected scope.

installed resource ids: No confirmed answer for this detail in the selected scope.

English translation is machine generated and has not been reviewed by the owner.
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_en_1

คำถาม: Could you help me with this: Where can I play Game A Fixture?

ไม่ผ่าน: runtime validation

```text
Game: Game A Fixture

No confirmed game_service data for this scope.

offered: No confirmed answer for this detail in the selected scope.

service id: No confirmed answer for this detail in the selected scope.

installed resource ids: No confirmed answer for this detail in the selected scope.

English translation is machine generated and has not been reviewed by the owner.
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_en_2

คำถาม: Where can I play Game A Fixture??

ไม่ผ่าน: runtime validation

```text
Game: Game A Fixture

No confirmed game_service data for this scope.

offered: No confirmed answer for this detail in the selected scope.

service id: No confirmed answer for this detail in the selected scope.

installed resource ids: No confirmed answer for this detail in the selected scope.

English translation is machine generated and has not been reviewed by the owner.
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_en_3

คำถาม: Where can I play Game A Fixture?. Please be brief.

ไม่ผ่าน: runtime validation

```text
Game: Game A Fixture

No confirmed game_service data for this scope.

offered: No confirmed answer for this detail in the selected scope.

service id: No confirmed answer for this detail in the selected scope.

installed resource ids: No confirmed answer for this detail in the selected scope.

English translation is machine generated and has not been reviewed by the owner.
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_auto_0

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_auto_1

คำถาม: ขอถามหน่อย เกมเอทดลอง เล่นได้ที่ไหน ครับ

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_auto_2

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน?

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}

## C29_auto_3

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน ตอบสั้น ๆ

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

validation: {"ok": false, "errors": ["missing_requested_field:offered", "missing_requested_field:service_id", "missing_requested_field:installed_resource_ids"], "warnings": []}
