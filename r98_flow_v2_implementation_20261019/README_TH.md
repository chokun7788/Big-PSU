# R98 Flow V2 candidate

1. อ่าน [ผลและปัญหาคงเหลือ](RESULTS_TH.md)
2. อ่าน [Flow ที่ลงมือทำจริง + สถานะเทียบ R97](IMPLEMENTED_FLOW_TH.md)
3. ดู [เปรียบเทียบ 91 คำถามกับ R95 retained](subset02/COMPARISON.json)
4. ดู [คำถามลูกค้าพร้อมคำตอบเต็ม LLM ON](final_on02/ANSWERS.jsonl)

ยังไม่ได้ติดตั้งทับระบบใช้งานจริง และยังไม่ได้รัน full test ของ R98

## ตัวอย่างเรียก focused test

รันจาก workspace หลัก ใช้ tag ใหม่ทุกครั้งเพื่อไม่เขียนทับผลเดิม:

```powershell
.\PSU_Esports_Chat_New_R69\runtime\python\python.exe -B -X utf8 r98_flow_v2_implementation_20261019/probe.py --tag my_new_probe --llm
```

โค้ดที่แก้อยู่ใน `system/app/knowledge/common` และ `system/app/pipeline/migrated_chat.py` ข้อมูลทดลองทุกชุดอยู่ใต้ `verification` แยกจาก common database ของ candidate

ไม่ต้องรันซ้ำเพื่ออ่านรายงาน มี logs และ manifests เก็บไว้แล้ว
