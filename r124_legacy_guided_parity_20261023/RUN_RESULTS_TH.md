# ผลดำเนินงานและการตรวจ R124

## ผล pipeline จริงที่เก็บไว้

| ชุด | ระบบ | จำนวน | สถานะ |
|---|---|---:|---|
| [teacher01](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher01/COMPLETE.json>) | legacy pilot | 11 | completed=True; LLM allowed=True |
| [candidate01](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate01/COMPLETE.json>) | early candidate pilot | 11 | completed=True; LLM allowed=True |
| [teacher02](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/COMPLETE.json>) | legacy baseline | 61 | completed=True; LLM allowed=True |
| [candidate02](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate02/COMPLETE.json>) | candidate iteration | 61 | completed=True; LLM allowed=True |
| [candidate03](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate03/COMPLETE.json>) | R03 focused | 12 | completed=True; LLM allowed=True |
| [candidate04_final](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/COMPLETE.json>) | R03 selected full61 | 61 | completed=True; LLM allowed=True |
| [candidate05_final_checks](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/COMPLETE.json>) | R04 focused14 | 14 | completed=True; LLM allowed=True |

คำว่า full61 ในชื่อข้างต้นหมายถึงครบชุดคัดเลือก61ข้อ ไม่ใช่ Full Test20554keys/55811grades. Source framesที่ชัดใช้0generationcallsได้แม้LLMON ไม่ได้บังคับโมเดลทุกข้อ. การprofile function callsเพิ่มlatency จึงไม่ใช้เวลาCLIเป็นเวลาproductionAPI

## HTTP API รุ่นสุดท้าย

R05: http://127.0.0.1:12422 · 13 requestsจริง =3liveWordPress+10retained · verification 8/8

[คำตอบและnativepipelineจริง](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [API checks](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_VERIFICATION.json>) · [runtime health](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/HEALTH_VERIFIED.json>)

ข้อมูลสดเป็นbookingserviceที่providerรายงานพร้อมclock/cache/สถานะปิด ไม่ใช่การตรวจหน้างานทุกเครื่อง. Providertransport, modeltransport และคำตอบถูกต้องเป็นคนละเรื่อง

## Invariant gates

| Gate | ผ่าน | หลักฐาน |
|---|---:|---|
| foundation | 35/35 | [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/verification_1792759369401833100/VERIFICATION.json>) |
| live | 16/16 | [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_verification_1792759001732273600/VERIFICATION.json>) |
| source guards | 19/19 | [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/source_guard_verification_1792759149021397500/VERIFICATION.json>) |
| stable FAQ | 5/5 | [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/exact_faq_verification_1792759004078514600/VERIFICATION.json>) |

รวม75 invariant assertions ไม่ใช่accuracy75คำถาม และไม่ใช่100%semanticaccuracy. FAQ54question-languagepairsเป็นการเข้าถึงsource ไม่ใช่holdout. Live16checksใช้controlledaggregatefixturesแยกจาก3realWordPresscalls

## การแก้ที่ตรวจพบระหว่างรัน

- เก็บผลR03ที่mapไปอุปกรณ์, modifierถูกลดเหลือR, historicalbinding falsegap ไว้ ไม่แก้logย้อนหลัง
- R04แก้mapก่อนequipment, heading+child7maps, chordidentity, bindingwallclock และpartialofficial
- R05แก้inventoryexistenceไม่เป็นcollection และaliasหลายeditionให้ถามเลือก ไม่ส่งNintendocatalogueทั้งชุด
- API R05รอบแรกเก็บfailureedition_clarification=falseไว้ แล้วแก้source matching/routeและเปิดprocessใหม่; startupครั้งหนึ่งWinError10061เพราะhealthเรียกก่อนserverพร้อม ไม่มีคำถามส่งสำเร็จในattemptนั้น

## ขอบเขตและงานที่ยังมีข้อจำกัด

- ยังไม่มีคะแนนFullTestใหม่หรือfreshholdout จึงยังบอกไม่ได้ว่าเท่าหรือดีกว่าlegacyทั้งระบบกี่เปอร์เซ็นต์
- teacherกับcandidateต่างmodelprofile/sourceversion; GPU/roleใหม่ไม่ใช่causalgainของFlowล้วน
- open_periodsจริง5วันยังขัดกัน เก็บrawsourceไว้และตอบจากrecordedplaycalendar
- HadesII, physicalfilmingpermission, exactinstalledpreset และความครบทุกcollectionยังต้องsourceยืนยัน
- bookingprocedureหลายvariantsยังซ้ำ/ยาว และPartIIฐานกับRemasteredยังไม่รวมrelationเอง
- candidateใช้draftmigrationpreview ไม่ownerapprovedpublication และไม่ติดตั้งทับR78

[ตรวจoriginal/frozen unchanged](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/FINAL_PACKAGE_REVISION05.json>) · [final hashes](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/FINAL_SOURCE_REVISION05.json>)