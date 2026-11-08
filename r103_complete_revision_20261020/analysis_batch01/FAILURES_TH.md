# R102 รอบรวมแรก: หลักฐานก่อนแก้

รันครบ 19 lanes แต่ไม่ใช่ผ่านครบ: acceptance 265/444 (59.68%) ตัวทดสอบใหม่หยุดหลัง 13 checks จาก fixture conditions_all ผิดชนิดข้อมูล; real live provider blocked ต้องแยกจากความถูกต้องคำตอบ

ไฟล์ต้นฉบับและฐานข้อมูลจริงไม่เปลี่ยนระหว่างรัน ไม่รวม assertions ต่างชนิดเป็นคะแนนเดียว

## C01 9/12

### C01_th_2

คำถาม: ขอราาคาบุคคลภายนอกทั้งหมด?

ไม่ผ่าน: exhaustive two service price scope

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 120.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: VR [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C01_en_2

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

### C01_auto_2

คำถาม: ขอราาคาบุคคลภายนอกทั้งหมด?

ไม่ผ่าน: exhaustive two service price scope

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 120.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: VR [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

## C02 12/12

## C03 12/12

## C04 5/12

### C04_th_0

คำถาม: ขอถามหน่อย ขอคืนเงินได้ไหม

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย
```

### C04_th_1

คำถาม: ขอถามหน่อย ขอถามหน่อย ขอคืนเงินได้ไหม ครับ

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย ขอถามหน่อย ครับ
```

### C04_th_2

คำถาม: ขอถามหน่อย ขอคืนเงินได้ไหม?

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย
```

### C04_en_3

คำถาม: Please tell me: Can I get a refund?. Please be brief.

ไม่ผ่าน: runtime validation

```text
**Relevant information**
• Confirmed information: Synthetic refund policy REFUND_FACT, except the stated exception. [S1]

English translation is machine generated and has not been reviewed by the owner.

Some parts of your question are still unclear; please specify: please be brief
```

### C04_auto_0

คำถาม: ขอถามหน่อย ขอคืนเงินได้ไหม

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย
```

### C04_auto_1

คำถาม: ขอถามหน่อย ขอถามหน่อย ขอคืนเงินได้ไหม ครับ

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย ขอถามหน่อย ครับ
```

### C04_auto_2

คำถาม: ขอถามหน่อย ขอคืนเงินได้ไหม?

ไม่ผ่าน: runtime validation

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ [S1]

ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ขอถามหน่อย
```

## C05 5/12

### C05_th_1

คำถาม: ขอถามหน่อย วันอังคารตอนเย็นเปิดถึงกี่โมง ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C05_th_3

คำถาม: วันอังคารตอนเย็นเปิดถึงกี่โมง ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C05_en_1

คำถาม: Could you help me with this: What time does the studio close on Tuesday?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C05_en_2

คำถาม: Waht time does the studio close on Tuesday??

ไม่ผ่าน: closing source selected

```text
**Nebula Fixture Studio**
• operator: Fixture University [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### C05_en_3

คำถาม: What time does the studio close on Tuesday?. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C05_auto_1

คำถาม: ขอถามหน่อย วันอังคารตอนเย็นเปิดถึงกี่โมง ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C05_auto_3

คำถาม: วันอังคารตอนเย็นเปิดถึงกี่โมง ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

## C06 12/12

## C07 8/12

### C07_th_1

คำถาม: ขอถามหน่อย ROV ถ้าเกมหลุดทำยังไง ครับ

ไม่ผ่าน: material context question

```text
ข้อมูลเกม: ROV

**ROV**
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: วิธีเล่น ROV_FACT_PLAY [S1]
```

### C07_th_3

คำถาม: ROV ถ้าเกมหลุดทำยังไง ตอบสั้น ๆ

ไม่ผ่าน: runtime validation, material context question

```text
ข้อมูลเกม: ROV

ขั้นตอนที่ผู้ใช้ต้องทำ (เรียงลำดับ): ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

### C07_auto_1

คำถาม: ขอถามหน่อย ROV ถ้าเกมหลุดทำยังไง ครับ

ไม่ผ่าน: material context question

```text
ข้อมูลเกม: ROV

**ROV**
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: วิธีเล่น ROV_FACT_PLAY [S1]
```

### C07_auto_3

คำถาม: ROV ถ้าเกมหลุดทำยังไง ตอบสั้น ๆ

ไม่ผ่าน: runtime validation, material context question

```text
ข้อมูลเกม: ROV

ขั้นตอนที่ผู้ใช้ต้องทำ (เรียงลำดับ): ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

## C08 0/12

### C08_th_0

คำถาม: ROV

ไม่ผ่าน: disconnect scope inherited

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เกมหลุด เช่น ภาพรวมกติกา / กติกาทั้งหมด / กฎเฉพาะเรื่อง?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

### C08_th_1

คำถาม: ขอถามหน่อย ROV ครับ

ไม่ผ่าน: disconnect scope inherited

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เกมหลุด เช่น ภาพรวมกติกา / กติกาทั้งหมด / กฎเฉพาะเรื่อง?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

### C08_th_2

คำถาม: ROV?

ไม่ผ่าน: disconnect scope inherited

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เกมหลุด เช่น ภาพรวมกติกา / กติกาทั้งหมด / กฎเฉพาะเรื่อง?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

### C08_th_3

คำถาม: ROV ตอบสั้น ๆ

ไม่ผ่าน: disconnect scope inherited

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เกมหลุด เช่น ภาพรวมกติกา / กติกาทั้งหมด / กฎเฉพาะเรื่อง?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

### C08_en_0

คำถาม: ROV

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
Game: ROV

**ROV**
• title: ROV [S1]
• summary: Overview ROV_FACT [S2]
• how to play: Play instructions ROV_FACT_PLAY [S3]

English translation is machine generated and has not been reviewed by the owner.
```

### C08_en_1

คำถาม: Could you help me with this: ROV

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
Game: ROV

**ROV**
• title: ROV [S1]
• summary: Overview ROV_FACT [S2]
• how to play: Play instructions ROV_FACT_PLAY [S3]

English translation is machine generated and has not been reviewed by the owner.
```

### C08_en_2

คำถาม: ROV?

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
Game: ROV

**ROV**
• title: ROV [S1]
• summary: Overview ROV_FACT [S2]
• how to play: Play instructions ROV_FACT_PLAY [S3]

English translation is machine generated and has not been reviewed by the owner.
```

### C08_en_3

คำถาม: ROV. Please be brief.

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
Game: ROV

**ROV**
• summary: Overview ROV_FACT [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### C08_auto_0

คำถาม: ROV

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
ข้อมูลเกม: ROV

**ROV**
• ชื่อเกมอย่างเป็นทางการ: ROV [S1]
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S2]
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: วิธีเล่น ROV_FACT_PLAY [S3]
```

### C08_auto_1

คำถาม: ขอถามหน่อย ROV ครับ

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

### C08_auto_2

คำถาม: ROV?

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
ข้อมูลเกม: ROV

**ROV**
• ชื่อเกมอย่างเป็นทางการ: ROV [S1]
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S2]
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: วิธีเล่น ROV_FACT_PLAY [S3]
```

### C08_auto_3

คำถาม: ROV ตอบสั้น ๆ

ไม่ผ่าน: disconnect scope inherited

```text
The requested topic is unclear. Which part of Disconnection do you need: rules overview / all rules / a specific rule topic?
```

```text
ข้อมูลเกม: ROV

**ROV**
• เกมเกี่ยวกับอะไร: ภาพรวม ROV_FACT [S1]
```

## C09 0/12

### C09_th_0

คำถาม: กฎ CS2

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_th_1

คำถาม: ขอถามหน่อย กฎ CS2 ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_th_2

คำถาม: กฏ CS2?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_th_3

คำถาม: กฎ CS2 ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_en_0

คำถาม: CS2 competition rules

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_en_1

คำถาม: Could you help me with this: CS2 competition rules

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_en_2

คำถาม: CS2 competition rules?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_en_3

คำถาม: CS2 competition rules. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_auto_0

คำถาม: กฎ CS2

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_auto_1

คำถาม: ขอถามหน่อย กฎ CS2 ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_auto_2

คำถาม: กฏ CS2?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C09_auto_3

คำถาม: กฎ CS2 ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

## C10 0/12

### C10_th_0

คำถาม: ขอเกมทั้งหมด

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_th_1

คำถาม: ขอถามหน่อย ขอเกมทั้งหมด ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_th_2

คำถาม: ขอเกมทั้งหมด?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_th_3

คำถาม: ขอเกมทั้งหมด ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_en_0

คำถาม: List all games

ไม่ผ่าน: full offering catalog not top K

```text
The selected source does not directly confirm the requested detail.
```

### C10_en_1

คำถาม: Could you help me with this: List all games

ไม่ผ่าน: full offering catalog not top K

```text
The selected source does not directly confirm the requested detail.
```

### C10_en_2

คำถาม: List all games?

ไม่ผ่าน: full offering catalog not top K

```text
The selected source does not directly confirm the requested detail.
```

### C10_en_3

คำถาม: List all games. Please be brief.

ไม่ผ่าน: full offering catalog not top K

```text
The selected source does not directly confirm the requested detail.
```

### C10_auto_0

คำถาม: ขอเกมทั้งหมด

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_auto_1

คำถาม: ขอถามหน่อย ขอเกมทั้งหมด ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_auto_2

คำถาม: ขอเกมทั้งหมด?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C10_auto_3

คำถาม: ขอเกมทั้งหมด ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

## C11 0/12

### C11_th_0

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_th_1

คำถาม: ขอถามหน่อย มีเกมใน PS5 กับ Switch อะไรบ้าง ครับ

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_th_2

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง?

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_th_3

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง ตอบสั้น ๆ

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_en_0

คำถาม: What games are offered on PS5 and Switch?

ไม่ผ่าน: offering scopes read

```text
The selected source does not directly confirm the requested detail.
```

### C11_en_1

คำถาม: Could you help me with this: What games are offered on PS5 and Switch?

ไม่ผ่าน: offering scopes read

```text
The selected source does not directly confirm the requested detail.
```

### C11_en_2

คำถาม: Waht games are offered on PS5 and Switch??

ไม่ผ่าน: offering scopes read

```text
The selected source does not directly confirm the requested detail.
```

### C11_en_3

คำถาม: What games are offered on PS5 and Switch?. Please be brief.

ไม่ผ่าน: offering scopes read

```text
The selected source does not directly confirm the requested detail.
```

### C11_auto_0

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_auto_1

คำถาม: ขอถามหน่อย มีเกมใน PS5 กับ Switch อะไรบ้าง ครับ

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_auto_2

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง?

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C11_auto_3

คำถาม: มีเกมใน PS5 กับ Switch อะไรบ้าง ตอบสั้น ๆ

ไม่ผ่าน: offering scopes read

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

## C12 5/12

### C12_th_0

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C12_th_1

คำถาม: ขอถามหน่อย ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C12_th_3

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C12_en_2

คำถาม: PC prcie for external visitors and how do I book PC??

ไม่ผ่าน: runtime validation, independent booking survives price gap

```text
**Service rate — PC / External Visitors**
Current price is not confirmed: the source has no confirmed effective period.

English translation is machine generated and has not been reviewed by the owner.

Some parts of your question are still unclear; please specify: how do i book
```

### C12_auto_0

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C12_auto_1

คำถาม: ขอถามหน่อย ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### C12_auto_3

คำถาม: ราคาและวิธีจอง PC สำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: independent booking survives price gap

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

## C13 8/12

### C13_en_0

คำถาม: With a 100 THB budget, how long can external visitors play PC?

ไม่ผ่าน: no derived hours from unknown current price

```text
**PC**
• Play time per session: 60 [S1]
• Booking occupancy: 60 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### C13_en_1

คำถาม: Could you help me with this: With a 100 THB budget, how long can external visitors play PC?

ไม่ผ่าน: no derived hours from unknown current price

```text
**PC**
• Play time per session: 60 [S1]
• Booking occupancy: 60 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### C13_en_2

คำถาม: With a 100 THB budget, how long can external visitors play PC??

ไม่ผ่าน: no derived hours from unknown current price

```text
**PC**
• Play time per session: 60 [S1]
• Booking occupancy: 60 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### C13_en_3

คำถาม: With a 100 THB budget, how long can external visitors play PC?. Please be brief.

ไม่ผ่าน: no derived hours from unknown current price

```text
**PC**
• Play time per session: 60 [S1]
• Booking occupancy: 60 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

## C14 3/12

### C14_th_0

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

### C14_th_1

คำถาม: ขอถามหน่อย PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

### C14_th_2

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก?

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
**PC**
• เวลาเล่นต่อรอบ: 60 [S1]
• เวลาที่กันช่องจอง: 60 [S2]

**VR**
• เวลาเล่นต่อรอบ: 30 [S3]
• เวลาที่กันช่องจอง: 30 [S4]
```

### C14_th_3

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

### C14_en_2

คำถาม: PC prcie for 2 hours and VR prcie for 30 minutes for external visitors?

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
**Service rate**
• Price: 100.00 THB [S1]
• Service: PC [S2]
• User group: External Visitors [S3]
• currency: THB [S4]
• Billing unit: per_hour [S5]
• Duration (minutes): 60 [S6]
• Calculation rule: Confirmed proportional calculation [S7]

No confirmed price for VR

English translation is machine generated and has not been reviewed by the owner.
```

### C14_auto_0

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

### C14_auto_1

คำถาม: ขอถามหน่อย PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก ครับ

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

### C14_auto_2

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก?

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
**PC**
• เวลาเล่นต่อรอบ: 60 [S1]
• เวลาที่กันช่องจอง: 60 [S2]

**VR**
• เวลาเล่นต่อรอบ: 30 [S3]
• เวลาที่กันช่องจอง: 30 [S4]
```

### C14_auto_3

คำถาม: PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก ตอบสั้น ๆ

ไม่ผ่าน: two bound tuples retained, amounts reflect PC2h and VR30m

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ บุคคลภายนอก เช่น รายการเกม / อุปกรณ์และสเปก / ราคา / สถานะจอง?
```

## C15 12/12

## C16 7/12

### C16_th_1

คำถาม: ขอถามหน่อย วันนี้เปิดไหม ครับ

ไม่ผ่าน: date and confirmed opening

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: 09:00–17:00 [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C16_th_3

คำถาม: วันนี้เปิดไหม ตอบสั้น ๆ

ไม่ผ่าน: date and confirmed opening

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: 09:00–17:00 [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C16_en_3

คำถาม: Are you open today?. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C16_auto_1

คำถาม: ขอถามหน่อย วันนี้เปิดไหม ครับ

ไม่ผ่าน: date and confirmed opening

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: 09:00–17:00 [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C16_auto_3

คำถาม: วันนี้เปิดไหม ตอบสั้น ๆ

ไม่ผ่าน: date and confirmed opening

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: 09:00–17:00 [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

## C17 7/12

### C17_th_1

คำถาม: ขอถามหน่อย วันนี้เปิดไหม ครับ

ไม่ผ่าน: bookability does not assert closed

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C17_th_3

คำถาม: วันนี้เปิดไหม ตอบสั้น ๆ

ไม่ผ่าน: bookability does not assert closed

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C17_en_3

คำถาม: Are you open today?. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C17_auto_1

คำถาม: ขอถามหน่อย วันนี้เปิดไหม ครับ

ไม่ผ่าน: bookability does not assert closed

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

### C17_auto_3

คำถาม: วันนี้เปิดไหม ตอบสั้น ๆ

ไม่ผ่าน: bookability does not assert closed

```text
**ตารางเวลาบริการ**
• ช่วงที่จองได้: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S1]
• ช่วงบำรุงรักษา: ไม่มีรายการในช่องนี้ (ยืนยันแล้ว) [S2]
• เขตเวลา: Asia/Bangkok [S3]
• เลือกวันในสัปดาห์: 1 [S4]
• โซนที่ใช้ตารางนี้: ทุกโซน [S5]
```

## C18 12/12

## C19 12/12

## C20 10/12

### C20_en_2

คำถาม: Waht is Game A Fixture and what is Game B Fixture??

ไม่ผ่าน: both same task subjects answered

```text
Game: Game A Fixture

**Game A Fixture**
• summary: Overview GAME_A [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### C20_en_3

คำถาม: What is Game A Fixture and what is Game B Fixture?. Please be brief.

ไม่ผ่าน: both same task subjects answered

```text
1. what is game a fixture
Game: Game A Fixture

**Game A Fixture**
• summary: Overview GAME_A [S1]

English translation is machine generated and has not been reviewed by the owner.

2. what is game b fixture?. please be brief
The requested topic is unclear. Which part of Game B Fixture do you need: game overview / how to play / controls / services offering this game?
```

## C21 0/12

### C21_th_0

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_th_1

คำถาม: ขอถามหน่อย กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ครับ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_th_2

คำถาม: กฏ ROV ก่อนกับหลัง First Blood ต่างกันยังไง?

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_th_3

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ตอบสั้น ๆ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_en_0

คำถาม: ROV competition rules before and after First Blood

ไม่ผ่าน: before/after linked clauses preserved

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C21_en_1

คำถาม: Could you help me with this: ROV competition rules before and after First Blood

ไม่ผ่าน: before/after linked clauses preserved

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C21_en_2

คำถาม: ROV competition rules before and after First Blood?

ไม่ผ่าน: before/after linked clauses preserved

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C21_en_3

คำถาม: ROV competition rules before and after First Blood. Please be brief.

ไม่ผ่าน: before/after linked clauses preserved

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C21_auto_0

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_auto_1

คำถาม: ขอถามหน่อย กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ครับ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_auto_2

คำถาม: กฏ ROV ก่อนกับหลัง First Blood ต่างกันยังไง?

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

### C21_auto_3

คำถาม: กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง ตอบสั้น ๆ

ไม่ผ่าน: before/after linked clauses preserved

```text
กติกา ROV — แข่ง ROV ทดลอง

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก
```

## C22 2/12

### C22_th_0

คำถาม: ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C22_th_1

คำถาม: ขอถามหน่อย ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน ครับ

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C22_th_3

คำถาม: ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน ตอบสั้น ๆ

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C22_en_0

คำถาม: I am not PSU staff. Which PC price applies?

ไม่ผ่าน: negated audience not quoted

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
• Price: 50.00 THB [S8]
• Service: PC [S9]
• User group: PSU Staff [S10]
• currency: THB [S11]
• Billing unit: per_hour [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Confirmed proportional calculation [S14]

English translation is machine generated and has not been reviewed by the owner.
```

### C22_en_1

คำถาม: Could you help me with this: I am not PSU staff. Which PC price applies?

ไม่ผ่าน: negated audience not quoted

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
• Price: 50.00 THB [S8]
• Service: PC [S9]
• User group: PSU Staff [S10]
• currency: THB [S11]
• Billing unit: per_hour [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Confirmed proportional calculation [S14]

English translation is machine generated and has not been reviewed by the owner.
```

### C22_en_2

คำถาม: I am not PSU staff. Which PC prcie applies??

ไม่ผ่าน: negated audience not quoted

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
• Price: 50.00 THB [S8]
• Service: PC [S9]
• User group: PSU Staff [S10]
• currency: THB [S11]
• Billing unit: per_hour [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Confirmed proportional calculation [S14]

English translation is machine generated and has not been reviewed by the owner.
```

### C22_en_3

คำถาม: I am not PSU staff. Which PC price applies?. Please be brief.

ไม่ผ่าน: negated audience not quoted

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
• Price: 50.00 THB [S8]
• Service: PC [S9]
• User group: PSU Staff [S10]
• currency: THB [S11]
• Billing unit: per_hour [S12]
• Duration (minutes): 60 [S13]
• Calculation rule: Confirmed proportional calculation [S14]

English translation is machine generated and has not been reviewed by the owner.
```

### C22_auto_0

คำถาม: ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C22_auto_1

คำถาม: ขอถามหน่อย ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน ครับ

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

### C22_auto_3

คำถาม: ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน ตอบสั้น ๆ

ไม่ผ่าน: negated audience not quoted

```text
**ค่าบริการ**
• ราคา: 100.00 THB [S1]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S2]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคคลภายนอก [S3]
• สกุลเงิน: THB [S4]
• หน่วยคิดราคา: per_hour [S5]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S6]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S7]

**ค่าบริการ**
• ราคา: 50.00 THB [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: PC [S9]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: บุคลากร PSU [S10]
• สกุลเงิน: THB [S11]
• หน่วยคิดราคา: per_hour [S12]
• ระยะเวลาที่ครอบคลุม (นาที): 60 [S13]
• วิธีคิดราคา: คำนวณตามสัดส่วนที่ระบุ [S14]
```

## C23 10/12

### C23_th_2

คำถาม: ราาคา PC สำหรับบุคคลภายนอก?

ไม่ผ่าน: cross-source conflict detected

```text
ข้อมูลที่มีผลในขอบเขตเดียวกันขัดกัน จึงยังยืนยันค่าที่ถูกต้องไม่ได้ครับ กรุณาให้ผู้ดูแลตรวจข้อขัดแย้งนี้ก่อน
```

### C23_auto_2

คำถาม: ราาคา PC สำหรับบุคคลภายนอก?

ไม่ผ่าน: cross-source conflict detected

```text
ข้อมูลที่มีผลในขอบเขตเดียวกันขัดกัน จึงยังยืนยันค่าที่ถูกต้องไม่ได้ครับ กรุณาให้ผู้ดูแลตรวจข้อขัดแย้งนี้ก่อน
```

## C24 12/12

## C25 12/12

## C26 12/12

## C27 0/12

### C27_th_0

คำถาม: มีอุปกรณ์ไหม

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_th_1

คำถาม: ขอถามหน่อย มีอุปกรณ์ไหม ครับ

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_th_2

คำถาม: มีอุปกรณ์ไหม?

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_th_3

คำถาม: มีอุปกรณ์ไหม ตอบสั้น ๆ

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_en_0

คำถาม: Is there any equipment?

ไม่ผ่าน: known empty exact scope

```text
No equipment is listed in the confirmed inventory for Nebula Fixture Studio. [S1]
```

### C27_en_1

คำถาม: Could you help me with this: Is there any equipment?

ไม่ผ่าน: known empty exact scope

```text
No equipment is listed in the confirmed inventory for Nebula Fixture Studio. [S1]
```

### C27_en_2

คำถาม: Is there any equipment??

ไม่ผ่าน: known empty exact scope

```text
No equipment is listed in the confirmed inventory for Nebula Fixture Studio. [S1]
```

### C27_en_3

คำถาม: Is there any equipment?. Please be brief.

ไม่ผ่าน: known empty exact scope

```text
No equipment is listed in the confirmed inventory for Nebula Fixture Studio. [S1]
```

### C27_auto_0

คำถาม: มีอุปกรณ์ไหม

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_auto_1

คำถาม: ขอถามหน่อย มีอุปกรณ์ไหม ครับ

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_auto_2

คำถาม: มีอุปกรณ์ไหม?

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

### C27_auto_3

คำถาม: มีอุปกรณ์ไหม ตอบสั้น ๆ

ไม่ผ่าน: known empty exact scope

```text
ในขอบเขต ศูนย์เนบิวลาทดลอง ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ [S1]
```

## C28 4/12

### C28_th_0

คำถาม: มีอุปกรณ์ไหม

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_th_1

คำถาม: ขอถามหน่อย มีอุปกรณ์ไหม ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_th_2

คำถาม: มีอุปกรณ์ไหม?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_th_3

คำถาม: มีอุปกรณ์ไหม ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_auto_0

คำถาม: มีอุปกรณ์ไหม

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_auto_1

คำถาม: ขอถามหน่อย มีอุปกรณ์ไหม ครับ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_auto_2

คำถาม: มีอุปกรณ์ไหม?

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

### C28_auto_3

คำถาม: มีอุปกรณ์ไหม ตอบสั้น ๆ

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

## C29 4/12

### C29_th_0

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

### C29_th_2

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน?

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

### C29_en_0

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

### C29_en_1

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

### C29_en_2

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

### C29_en_3

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

### C29_auto_0

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

### C29_auto_2

คำถาม: เกมเอทดลอง เล่นได้ที่ไหน?

ไม่ผ่าน: runtime validation

```text
ข้อมูลเกม: เกมเอทดลอง (Game A Fixture)

ยังไม่มีข้อมูลยืนยันในส่วน เกมที่ศูนย์มีให้เล่นจริง สำหรับขอบเขตนี้

offered: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

service id: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก

installed resource ids: ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก
```

## C30 0/12

### C30_th_0

คำถาม: อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_th_1

คำถาม: ขอถามหน่อย อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ ครับ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_th_2

คำถาม: อธิบายกฏ ROV เรื่องเกมหลุดเป็นอังกฤษ?

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_th_3

คำถาม: อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ ตอบสั้น ๆ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_en_0

คำถาม: Explain ROV competition disconnection rules in English

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_en_1

คำถาม: Could you help me with this: Explain ROV competition disconnection rules in English

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_en_2

คำถาม: Explain ROV competition disconnection rules in English?

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_en_3

คำถาม: Explain ROV competition disconnection rules in English. Please be brief.

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_auto_0

คำถาม: อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_auto_1

คำถาม: ขอถามหน่อย อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ ครับ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_auto_2

คำถาม: อธิบายกฏ ROV เรื่องเกมหลุดเป็นอังกฤษ?

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

### C30_auto_3

คำถาม: อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ ตอบสั้น ๆ

ไม่ผ่าน: exception survives English output

```text
Competition rules: ROV — ROV Fixture Tournament

No verified clause for this topic was found in the selected rulebook.

English translation is machine generated and has not been reviewed by the owner.
```

## C31 12/12

## C32 12/12

## C33 12/12

## C34 12/12

## C35 0/12

### C35_th_0

คำถาม: VALORANT ใช้ผู้เล่นกี่คน

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_th_1

คำถาม: ขอถามหน่อย VALORANT ใช้ผู้เล่นกี่คน ครับ

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_th_2

คำถาม: VALORANT ใช้ผู้เล่นกี่คน?

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_th_3

คำถาม: VALORANT ใช้ผู้เล่นกี่คน ตอบสั้น ๆ

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_en_0

คำถาม: How many players does VALORANT use?

ไม่ผ่าน: broken mode relation does not assert count

```text
The linked data is invalid or outside its allowed scope, so this detail cannot be confirmed.
```

### C35_en_1

คำถาม: Could you help me with this: How many players does VALORANT use?

ไม่ผ่าน: broken mode relation does not assert count

```text
The linked data is invalid or outside its allowed scope, so this detail cannot be confirmed.
```

### C35_en_2

คำถาม: How many players does VALORANT use??

ไม่ผ่าน: broken mode relation does not assert count

```text
The linked data is invalid or outside its allowed scope, so this detail cannot be confirmed.
```

### C35_en_3

คำถาม: How many players does VALORANT use?. Please be brief.

ไม่ผ่าน: broken mode relation does not assert count

```text
The linked data is invalid or outside its allowed scope, so this detail cannot be confirmed.
```

### C35_auto_0

คำถาม: VALORANT ใช้ผู้เล่นกี่คน

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_auto_1

คำถาม: ขอถามหน่อย VALORANT ใช้ผู้เล่นกี่คน ครับ

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_auto_2

คำถาม: VALORANT ใช้ผู้เล่นกี่คน?

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### C35_auto_3

คำถาม: VALORANT ใช้ผู้เล่นกี่คน ตอบสั้น ๆ

ไม่ผ่าน: broken mode relation does not assert count

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

## C36 12/12

## C37 10/12

### C37_th_2

คำถาม: ศูนย์อยู่ที่ไหน แล้วราาคาเท่าไร?

ไม่ผ่าน: supported address and scoped price question

```text
**ศูนย์เนบิวลาทดลอง**
• ที่อยู่เต็ม: อาคารทดลอง 5 ชั้น 1 ADDRESS_FACT [S1]
```

### C37_auto_2

คำถาม: ศูนย์อยู่ที่ไหน แล้วราาคาเท่าไร?

ไม่ผ่าน: supported address and scoped price question

```text
**ศูนย์เนบิวลาทดลอง**
• ที่อยู่เต็ม: อาคารทดลอง 5 ชั้น 1 ADDRESS_FACT [S1]
```
