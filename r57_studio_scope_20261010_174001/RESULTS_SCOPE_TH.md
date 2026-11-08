# ปรับขอบเขตตามผู้ใช้ · r57.4

## สิ่งที่ผู้ใช้ต้องการ

บอทตอบเรื่องร้านเกมและ PSU Esports Studio - Phuket โดยใช้ข้อมูลที่มีให้ครบตามส่วนที่ถาม ไม่ต้องเป็นผู้ช่วยความรู้ทั่วไป ไม่ต้องตอบไก่กับไข่/กินอะไรดี หรือแต่งบทความทั่วไป แม้คำขอเขียนจะมีคำว่าเกม

## การตอบที่ต้องได้

| คำถาม | พฤติกรรม |
|---|---|
| PC มีเกมอะไรบ้าง และบุคคลทั่วไปเล่น2ชั่วโมงกี่บาท | รายชื่อเกมครบตามsource + อัตรา/กลุ่ม/หน่วย/ยอดรวมที่เกี่ยวข้อง |
| ถามราคาแล้วเลือก PC / ทั้งหมด | รับตัวเลือกไปต่อกับคำถามเดิม ไม่เริ่มคำถามใหม่ |
| ศูนย์มีอะไร/อยู่ไหน/เปิดเมื่อไหร่/ต้องจองอย่างไร | แสดงข้อมูลบริการที่ยืนยันและเงื่อนไขครบ |
| กฎทั้งหมด/กฎเฉพาะหัวข้อของเกม | ใช้sourceเกม/รายการที่ตรง แบ่งหน้าหากยาวและแจ้งsource gap |
| ตอนนี้เครื่องใดว่าง | ดึงbookingตามระบบเดิม; ความผิดพลาดAPIไม่ใช่ว่าง |
| บริการที่ยังไม่มีข้อมูล | บอกว่าไม่ยืนยันตรงประเด็น ไม่แต่งนโยบาย |
| ไก่กับไข่/เย็นนี้กินอะไรดี/เขียนบทความทั่วไป | แจ้งขอบเขตสั้นๆ ไม่มีคำตอบความรู้ทั่วไปหรือgeneral LLM generation |
| กินอาหารตรงไหนในศูนย์ | ยังตอบข้อกำหนดอาหารจากsource ไม่ปิดเพราะมีคำว่ากิน |
| What can you help me with? | บอกหมวดข้อมูลศูนย์ที่ช่วยได้ ไม่ตอบno-answer |

## แก้อะไรจริง

1. ปิดทางgeneric translation/creationในproduct entry และfree general LLM fallbackเมื่อไม่มีstudio evidence; ใช้ข้อความแจ้งขอบเขตแทน การตอบศูนย์ภาษาไทย/อังกฤษจากsourceตามlocaleยังคงอยู่ งานแปลข้อความทั่วไปไม่อยู่ในscopeสินค้า
2. General requestที่ไม่ใช่studio informationไม่ใช้retrievalกว้างเพื่อเอาข้อมูลใกล้เคียงมาตอบ; missingstudioevidenceไม่ถูกเติมด้วยfreegeneration ส่วนRAG LLMที่มีverifiedcontextยังใช้ตามระบบเดิม
3. เพิ่มhigh-confidence unrelated task guardก่อนrouterสำหรับmeal choice/egg origin/non-studio writing/recipe โดยไม่ปิดคำถามที่มีบริบทบริการหรือเกมชัดเจน
4. ย้ายscope checkก่อนsoft-related birthday/party ไม่ตอบวิธีจองเพียงเพราะคำถามสูตรเค้กมีbirthday
5. เพิ่มclosed English capability grammarและใช้detectorร่วมในEnglishadapter; ไม่จับคำขอให้ช่วยจองPC/คำถามถึงstaffเป็นตัวบอท

## สิ่งที่พบในลูปและเหตุผล

- r57.2 scope baseline12ข้อ:5ข้อไม่ผ่านoraclemode/ข้อความ มี3ข้อความno-answerเดิมที่ไม่ตรงรูปแบบscopeใหม่ และ2routingผิดจริง: THอาหารไปclarification, ENอาหารไปfoodpolicyในศูนย์ ทั้งที่ถามเมนูชีวิตประจำวัน
- หลังearlytaskguard r57.3 scope12ผ่าน; service156และcontext38ไม่มีfailedchecks
- Positive6เคส: sourceปัจจุบันอนุญาตนำอาหารเข้ามาและกินเฉพาะพื้นที่ oracleเก่า2ข้อกลับคาดว่าunknown, THhelpใช้ค่าบริการแต่oracleจับราคาเป็นคำเดียว จึงเป็นfalse failures3; ไม่มีการเปลี่ยนowner policyเพื่อแก้คะแนน
- ENhelp1ข้อเป็นbugจริง:What can you help me with?ไม่เข้าความสามารถ เพราะmatcherรู้what can you doแต่ไม่มีhelp predicate; แก้subject/actiongrammar ไม่ใช้freeLLMเขียนความสามารถขึ้นมาเอง
- เก็บbaseline/rawผลเดิมกับเหตุผลแก้oracleไว้ ไม่ปรับคะแนนย้อนหลังเงียบๆ

## ผลตรวจอัตโนมัติ

- Latest source: **89 tests**, failure0/error0 รวมscope/bookingfaults/calendar/conversation/service/sourceguards
- Latest web r57.4: **56 requests** =นอกเรื่อง12 +positiveboundary6 +context/service38, failedchecks0
- Webr57.3ที่ตรวจหลังscopeguard:156 source contracts, failedchecks0;145 content-contractchecked+11 liveformat/truthunverified รุ่น4เปลี่ยนเฉพาะcapabilitydetector/Englishidentityadapterหลังจากนั้น มีunit+positive/contextwebใหม่ ไม่เรียก156ชุดนั้นว่าเพิ่งรันบนรุ่น4
- Latest12นอกเรื่องไม่มีgeneral_llmprovidergenerationในtrace; นี่ไม่รับรองว่าระบบไม่เรียกโมเดลเพื่อrouting/intentทุกชั้นในทุกข้อความ
- Sourceapp/webcandidateและ2ชุดแจกhashตรงROOT;data495ไฟล์ตรง;owner38ไฟล์ไม่เปลี่ยน;codeก่อนแก้/diff/baseline/logเดิมเก็บไว้

## ความหมายของคำตอบครบ

ต้องครบทุกส่วนที่มีข้อมูลยืนยัน เช่นบริการ/กลุ่ม/ราคา/หน่วย/ระยะเวลา/ข้อยกเว้น/วันที่ ไม่ใช่ให้บอทสร้างคำตอบยาวหรือเติมส่วนที่sourceไม่ได้บอก ถ้าขาดให้แสดงส่วนที่ตอบได้และส่วนที่ไม่ยืนยัน ไม่ลดguardเพื่อให้เหมือนตอบได้ทุกเรื่อง

## ส่วนที่ยังไม่ปิด

- งานหลายส่วนเกิน6/เจตนาซ้อนมาก/ข้อความเสียหนัก/บริบททุกลำดับยังไม่รับรองครบ
- RoVต้นฉบับขาด,priceexpiry/non-PC,ข้อขัดแย้งTekkenและownerfields26เรื่องยังต้องsourceเดิมตามรายการr56 ไม่สร้างข้อมูลเอง
- คำถามใหม่อาจยังหลุดไปหมวดใกล้เคียง ต้องเก็บoperation/target/sourceที่เลือกกับส่วนที่ผู้ใช้ถามจริง แล้วแก้ตามหลักฐาน
- Sustainedload/cleanWindowsVM/retention/publicdeploymentยังเป็นงานเดิม ไม่มีการทำเพิ่มในscopeรอบนี้
- งานเขียน80/500คำ/translationทั่วไปที่เคยทดสอบไม่ใช่เกณฑ์สินค้าแล้ว ไม่ไล่เพิ่มความสามารถนอกเรื่องเพื่อปิดT34/T35

## ใช้งานและหลักฐาน

เว็บล่าสุด http://127.0.0.1:8093/ รุ่น2026.10.10-service-r57.4;สองแพ็กเกจที่สร้างใหม่ในPSU_Esports_Share_R56_20261010อัปเดตmanifest/sourceเป็นr57.4แล้ว (ชื่อโฟลเดอร์คงเดิม,ดูruntimeversionจากhealth/manifest) R50เก็บเดิม

Scopeflow:FLOW_SCOPE.md;summary:SUMMARY.json;audit:SOURCE_PACKAGE_AUDIT.json;diff:source_changes.patch;raw:scope_web_latest.json/service_context_latest.json/positive_boundaries_web_final.json;servicecontract:service_web_final.json
