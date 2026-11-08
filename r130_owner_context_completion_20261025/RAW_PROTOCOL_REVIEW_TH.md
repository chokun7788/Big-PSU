# ตรวจ protocol จาก raw330 ที่บันทึกไว้

อ่านผลที่มีอยู่ ไม่รันคำถามหรือโมเดลใหม่ ไม่แก้ frozen runtime/weights/prompt และไม่ regrade คำตอบ baseline

| แขน | JSON parse ได้ | Wire ผ่าน | จำนวน |
|---|---:|---:|---:|
| base | 0 | 0 | 110 |
| retained | 95 | 0 | 110 |
| new | 110 | 90 | 110 |

## ข้อวินิจฉัยก่อนเลือกน้ำหนัก

- ค่า wire0 ของ base/retained ไม่ใช่คำตอบถูก0%: baseส่งข้อความคล้ายYAML ส่วนretainedส่วนใหญ่ส่งJSONแต่ผิดversion/โครงสร้างและมีgraph fieldsปะปน
- SYSTEMไม่ได้ระบุชัดว่าให้ส่งJSONและversion literal ขณะที่backendรับformatเพื่อบันทึกhash แต่ไม่ได้ใช้grammar/schema constrained decodingในgenerate ตัวแปรนี้เหมือนกันทั้ง3แขน จึงวัดการถ่ายโอนprotocolภายใต้backendนี้ได้ แต่ห้ามอธิบายทั้งหมดว่าเข้าใจบริบทไม่ได้
- newผ่านwire90/110 แต่ยังต้องตรวจoperation/target/slot/critical-domain และคำตอบกับsourceจริงของR130ก่อนเลือก ห้ามpromoteเพียงเพราะJSONผ่าน
- ตัวอย่างselectorบางรายการส่งรูปinputกลับมา แม้JSONparseได้ก็ไม่ใช่การเลือกevidenceที่ผ่านcontract จำนวนที่สำรวจจากlogยังเปลี่ยนระหว่างreplay ต้องอ่านเป็นหลักฐานระหว่างรัน
- Backendดั้งเดิมที่ใช้Ollama/GGUFมีพฤติกรรมenforceformatต่างกัน การเทียบsavedlegacyต้องระบุbackend/source/clock/deadlineconfounds

## งานที่ต้องทำใน adjudication

1. ใช้ R130/paired_replay03 ที่ครบแล้ว ไม่ใช้คะแนน execution R129 ทดแทน
2. อ่านทุก execution regression และกลุ่มcriticalกับsource/คำถาม/คำตอบ ไม่ถือreceiptที่ถูกว่าsemanticถูกทั้งคำถาม
3. แยกprotocol adaptation, invalid proposal fallback, selector-contract failure และ actual source/content failures
4. หากเลือกnewต้องมีเหตุผลจากexecutionและcriticalreviewเพิ่มเติมตามpromotion gates; ระบุข้อจำกัดprotocolนี้ในรายงานสุดท้าย
5. การแก้prompt/decoderในอนาคตต้องเป็นinput/backendรุ่นใหม่ที่ตรึงแยกกัน ไม่แก้รอบfrozenหรือแอบใช้rawเก่ากับpromptใหม่

## หลักฐานโค้ดและ raw

- `system/app/knowledge/common/domain_flow/graph_protocol.py`: SYSTEM/messages/extend_schema
- `../r129_full_plan_completion_20261024/serve_model.py`: apply_chat_template/model.generate/provenance
- `../r129_full_plan_completion_20261024/three_arm02/RESULTS.jsonl`
- `RAW_PROTOCOL_REVIEW.json`: ตัวอย่างrawและprovenanceแยกแขน/selector

