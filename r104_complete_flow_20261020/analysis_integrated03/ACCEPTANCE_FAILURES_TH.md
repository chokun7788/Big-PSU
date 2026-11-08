# ทุก acceptance variant ที่ไม่ผ่าน

ข้อที่ C07 เปลี่ยน oracle ให้รายงานแยกจากการเทียบ R102; ห้ามอ้างว่าทุกคะแนนที่เพิ่มมาจาก runtime

## C04_en_3

คำถาม: Please tell me: Can I get a refund?. Please be brief.

ไม่ผ่าน: runtime validation

```text
**Relevant information**
• Confirmed information: Synthetic refund policy REFUND_FACT, except the stated exception. [S1]

English translation is machine generated and has not been reviewed by the owner.

Some parts of your question are still unclear; please specify: please be brief
```

validation: {"ok": false, "errors": ["unresolved_query_clause"], "warnings": []}

## C16_en_3

คำถาม: Are you open today?. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null

## C17_en_3

คำถาม: Are you open today?. Please be brief.

ไม่ผ่าน: answer exists

```text
(ไม่มีผลลัพธ์)
```

validation: null
