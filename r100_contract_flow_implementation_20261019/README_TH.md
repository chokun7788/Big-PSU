# R100 — Contract Flow candidate

- [ผลทดสอบ การแก้ และปัญหาคงเหลือ](RESULTS_TH.md)
- [Flow ที่ลงมือจริงและสถานะ P01–P14](IMPLEMENTED_FLOW_TH.md)
- [เปรียบเทียบ same-key subset กับ R98 retained](subset05/COMPARISON.json)
- [คำถามลูกค้าและคำตอบเต็ม เปิด LLM](final_on04/ANSWERS.jsonl)
- [Integrity](INTEGRITY_FINAL.json)

ยังไม่ติดตั้งทับระบบจริงและยังไม่ใช่ portable production package ไม่ต้องรัน test ซ้ำเพื่ออ่านผล

เมื่อจำเป็นต้องทำ focused run ใหม่ ให้ใช้ tag ใหม่จาก workspace หลัก:

```powershell
.\PSU_Esports_Chat_New_R69\runtime\python\python.exe -B -X utf8 r100_contract_flow_implementation_20261019/probe.py --tag another_probe --llm
```

ข้อมูลจริงที่คัดลอกมาอยู่ใน `system/data/knowledge/common.sqlite` ฐานทดสอบใหม่อยู่ใต้ `verification` แยกกัน ไม่คัดลอก fixture records กลับเข้าฐานจริง
