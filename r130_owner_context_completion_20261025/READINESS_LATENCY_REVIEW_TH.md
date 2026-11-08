# Latency ของ owner50 ผ่าน APIจริง — R130/retained

คำถามเดิม50ข้อเปิดLLMแบบอนุญาตให้เลือกใช้ ผ่านการคงคำตอบจากsource-readและpartial statusทุกข้อ ไม่ใช่benchmarksemanticaccuracy

- Median 0.474s; p95 0.608s; max 41.187s
- 49/50ต่ำกว่า1s; 1/50เกิน20s

## ข้อที่ยังช้า

ข้อ6: อยู่ตึกอะไร ชั้นไหน? ใช้41.187s ทั้งที่ข้อมูลcenter_psu_phuketมีbuilding5/floor1อยู่แล้ว และหลังfallbackอ่านtyped fieldsได้ถูกต้อง

logยืนยันcontext_understandingเรียกretainedประมาณ40.469s HTTP/identityผ่าน แต่rawversion1.0และroot fieldsผิดwire (r121_root_fields) แล้วจึงfallbackไปtyped building/floor ไม่ใช่ไม่มีAPIวันเวลา ไม่ใช่ไม่มีข้อมูล ไม่ใช่providerล่ม และไม่ใช่คำตอบhallucination

## แนวแก้ที่ต้องแยกรอบอย่างถูกต้อง

- เพิ่มsource-backed native recognition/field-set dispatchสำหรับคำถามอาคาร+ชั้นที่ระบุได้ครบอยู่แล้วก่อนเรียกcontext model โดยตรวจบริบทไม่ให้สับสนlocationของเกม/อุปกรณ์
- หรือใช้FAQ/source-owned question aliasที่ยืนยันจากowner50ข้อ6 โดยไม่เดาที่อยู่ใหม่ แต่ต้องอยู่ในcandidate/freezeรอบถัดไป
- แก้explicit JSON/version/backendformat enforcementและnative-fallback arbitrationเป็นงานแยกที่ตรึงprompt/backendให้เปรียบเทียบได้ ไม่แก้weights/sourceของFullที่กำลังรัน

Full Testเริ่มหลังAPIreadinessแล้ว ห้ามใช้ข้อดีmedianไปอ้างว่าทุกคำถามเร็วหรือแก้latencyหมด และห้ามแก้frozen candidateระหว่างวัด

หลักฐาน: OWNER50_API_ACCEPTANCE.jsonl/OWNER50_API_COMPLETE.json ในAPIoutputที่ระบุในREADINESS_LATENCY_REVIEW.json และevent/provenanceของข้อ6

