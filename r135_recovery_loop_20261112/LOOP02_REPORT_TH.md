# ผลวงรอบ02 — การผูกกลุ่มผู้ใช้ก่อนระบุราคา

วันที่รายงาน: 12 พฤศจิกายน 2026, Asia/Bangkok; code baseก่อนแก้ e4f0b1a9 เก็บ Loop01/parent/frozen/ข้อมูลเจ้าของไว้ ไม่มีการเปลี่ยนโมเดลหรือน้ำหนัก

## ก่อนแก้และสาเหตุร่วม

source-only natural probe6คำถามก่อนแก้ ผ่าน4/6controls สองกรณีคือ `นักศึกษาต่งามหาลัย` และ `นักศึกษา` ไม่ระบุสถาบัน ส่งทั้ง3audiences/6rates รวมPSU0บาท แทนการถามว่าต้องใช้กลุ่มใด ราคาแต่ละกลุ่มอาจเป็นข้อมูลจริง แต่ไม่ใช่การผูกกลุ่มที่ผู้ใช้พยายามระบุให้สำเร็จ

`financial.audience_mentions` หาsource aliasesตรงข้อความ และrate_poolเปิดทุกกลุ่มเมื่อไม่พบpositiveaudience การเปิดทุกกลุ่มเหมาะกับคำถามขอทุกกลุ่ม แต่ยังแยกจากกลุ่มที่ระบุไม่สำเร็จไม่พอ จึงแก้เหตุร่วมนี้ด้วยการขอข้อมูลเพิ่ม ไม่เดาคำผิดเป็นPSUหรือราคาฟรี

ระหว่างอ่านผลจริงพบอีกจุด: aliasนำเข้าของ General Adult มี `ไม่ใช่นักศึกษา` และ `ไม่ได้เป็นนักศึกษา` จึงไปตรงกับส่วนต้นของ `ไม่ใช่นักศึกษา PSU` แล้วเลือกAdultด้วย แม้การปฏิเสธPSUกลุ่มหนึ่งยังไม่ยืนยันว่าเป็นAdult โค้ดใหม่นับการผูกpositiveด้วยaliasรูปปฏิเสธอย่างเดียวร่วมกับnegativeอีกกลุ่มเป็นความกำกวม โดยไม่แก้aliasหรือrecordจริง

## สิ่งที่แก้ใน candidate

- เพิ่ม `audience_role_scope.py`: monetary requestที่ผูกบริการต้นทางได้ แต่student role/negative groupยังไม่ยืนยันpositive ให้ถามกลุ่มจากaudience recordsที่มี
- source-name maskingป้องกันกรณีบริการชื่อ Student Lounge ไม่ให้กลายเป็นคำยืนยันว่าผู้ถามเป็นนักศึกษา ไม่แก้raw question/ชื่อ/ตัวเลข
- คำถามexplicitทุกกลุ่มและกลุ่มที่ผูกได้ เช่นPSU/นักศึกษาต่างสถาบัน/บุคคลทั่วไป ยังตอบได้ ไม่ห้ามหลายอัตราทั้งหมด
- readerคืนmissing_inputแบบlocked, receipt verifierปฏิเสธการบังคับส่งrateขณะroleยังไม่ชัด และcompatibility final guardขอความชัดเจนก่อนส่งprice
- การประกอบคำถามปกติที่ราคาไม่ชัดแต่จองตอบได้ ยังคงขั้นตอนจอง ไม่รายงานว่าได้ตอบครบทุกส่วน

หลักการมาจากselective QA/coverage และsource-bound contractsใน RESEARCH_FOLLOWUP_TH.md: ลดความเสี่ยงโดยถามเฉพาะambiguity แต่ต้องรักษาnormal positives ไม่อ้างว่าทำcalibrated semantic confidenceแล้ว

## ตรวจซ้ำจากช่องโหว่ระหว่างทาง

guardฉบับแรกผ่าน6naturalcontrols แต่controlเดิมของnegationตรวจเพียงไม่ส่งPSU จึงยังยอมให้Adultหลุดได้ ต้องอ่านคำตอบจริงแล้วเพิ่มcontrolที่ไม่ยอมให้เดาrateใดจากnegativeอย่างเดียว เก็บผลฉบับแรกไว้ ไม่ยกผลผ่านเก่ามารับรองคุณภาพทุกบรรทัด

direct forced flat compatibilityของคำถามราคา+จองยังเคยผ่านguardที่ยกเว้นcompound โดยยังเหลือ20source hitsของrate เก็บ `AUDIENCE_COMPOUND_GUARD_BEFORE.json` แล้วเพิ่มการระงับflat compoundที่ยังมีunselected rate hits กรณีนี้เป็นการบังคับresultเพื่อทดสอบguard ไม่ใช่หลักฐานว่าทางnaturalส่งผิดในรอบHTTP

ผลnaturalcompoundยังรักษาbooking sibling ส่วนunsafe flat fallbackที่แยกข้อความของแต่ละclaimไม่ได้อาจถูกถอนทั้งก้อนและถามกลุ่ม ไม่อ้างว่าrecoverทุกverified siblingจากflat proseได้แล้ว

## ผลสุดท้ายและตัวหาร

ชื่อโฟลเดอร์/hash/phaseอยู่ใน LOOP02_MANIFEST.json:

- natural6กรณีเดิมหลังแก้ผ่าน6/6 ตามเกณฑ์เฉพาะนั้น
- controls21ผ่าน รวมnormalPSU/ต่างมหาลัย/Adult,explicitall,unknownservice,non-price,source-name Student Lounge,forcedreceipts,forcedsingle/compoundcompatibility,negation และnaturalprice+booking
- affected regressions: alternative-duration20, currency12, boundedbudget6, source/scope/edit/withdraw22 และmatrix27คำถามผ่าน
- source/replay/regressionรวม87checks ซึ่งรวม6naturalcontrolsและ21controls; matrix27คำถามเป็นอีกตัวหาร มีพฤติกรรมซ้ำกัน ไม่ใช่accuracy
- HTTPจริง7คำถามเรียงทีละข้อผ่าน19assertions: ขอroleแทนunselectedprices,normalPSU0,foreign50,explicitallและbookingpartial
- follow-up HTTPเพิ่ม2คำขอผ่าน5checks: ใช้server sessionที่ถามroleจริงแล้วตอบนักศึกษาต่างมหาลัย จึงอ่านราคาNintendoของกลุ่มนั้นได้ และsessionใหม่ไม่ยืมราคา/บริการจากsessionก่อน

ชุดแรกก่อนcompoundhardeningและชุดfinalเก็บผลแยก ตัวเลขข้างต้นเป็นfinalชุดเดียว ไม่บวกattemptซ้ำให้ดูจำนวนมากขึ้น ไม่มี200/2111ใหม่ ไม่มีการแก้คะแนนliteralเดิม

## ข้อจำกัดและงานต่อ

- เป็นbounded lexical ambiguity guardร่วมกับsource scopes ไม่ใช่ independent semantic interpretation ทุกชนิด; selector/verifierใช้helperร่วม ต้องไม่เรียกผลตรงกันว่าsemantic proofอิสระ
- roleที่สะกดผิดจนไม่เหลือคำว่าstudent/นักศึกษา,หลายroleในประโยคเดียว,roleหนึ่งรู้แล้วอีกรายการไม่ชัด และnegationของส่วนย่อยในกลุ่มที่รวมStudent/Staffยังไม่รับรองครบ
- source aliasesเป็นข้อมูลที่อาจมีscopeกว้างเกินคำถาม การผ่านschemaไม่ทำให้aliasมีความหมายถูกทุกบริบท และรอบนี้ไม่แก้approval/publication/วันที่มีผลของข้อมูล
- finalguardของcompoundรองรับobserved rate hits; ไม่พิสูจน์semanticตรวจข้อความราคาในFAQ/flat proseทุกชนิด
- follow-upที่พิสูจน์คือเลือกกลุ่มนักศึกษาต่างสถาบันจากsingle clarificationเท่านั้น ไม่ใช่ทุกชนิดของcontext/history/role correction
- source-name mutationเป็นparsercontrol ไม่ใช่actualowner HTTP edit การเพิ่มแก้ถอนทุกชนิดยังเป็นงานค้าง
- guardมีงานตรวจเพิ่ม ไม่อ้างว่ารอบนี้ทำให้เร็วขึ้นหรือแก้rootcausecooldown/timeout;hard deadline/model admission/complete76requirementsยังไม่ปิด
- preview8144เป็น R135-Recovery-loop02,ownDB/logs; protectedmodel12921,parent8143และผลfrozenไม่เปลี่ยน ไม่deployproduction

งานถัดไปเลือกactualfailureของcompletion/outputซ้ำและdiagnostic/recoveryของmodel cooldown พร้อมตรวจuntyped price prose/source-roleambiguityที่ยังไม่ครอบคลุม ไม่วนเพิ่มnegativeหรือรันbenchmarkใหญ่เมื่อไม่มีchange
