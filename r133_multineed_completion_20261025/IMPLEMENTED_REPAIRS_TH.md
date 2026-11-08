# Flow ที่ใส่ใช้งานแล้ว และขอบเขตที่ยังต้องตรวจ

รุ่นที่ตัวเปิดแชทเดิมเรียกใช้ตอนนี้คือ **R133** ที่ `PSU_Esports_Chat_Current_R133` พอร์ต8115 ตัวแก้ข้อมูลพอร์ต8116อ่านฐานเดียวกัน ตรวจทั้ง process, installation identity, loaded-source fingerprint และไฟล์จริงแล้ว ดู `INSTALLATION_RECEIPT.json`, `INSTALLATION_VERIFIED.json` ตัวเปิดR78เดิมส่งต่อมายังรุ่นนี้ มีสำรองตัวเปิดและฐานR78ครบ ไม่ได้เขียนทับระบบ/ฐานเก่า

การสั่งให้เลือกสิ่งที่ดีกว่าเป็น authorization ให้ลงการแก้ที่มีหลักฐานได้แล้ว การหยุดไว้แค่รายงานทั้งที่แก้และตรวจรับได้เป็นการทำงานไม่ครบตามเจตนาผู้ใช้ รอบนี้จึงแก้ ตรวจ และเชื่อมเข้าตัวเปิดใช้งานจริง ส่วนความถูกต้องทั้ง76ข้อยังไม่ถูกปิดด้วยผลทดสอบบางส่วน

## โมเดลที่เลือก

Typhoon2.5 Qwen3 4B (`typhoon-ai/typhoon2.5-qwen3-4b`) ผ่านHF NF4 double quant/BF16 alias `psu-r129:latest` ใช้R121 retained LoRAเฉพาะcontext planner ส่วนselector/genericใช้base ตามหลักฐานการเลือกR130 adapterใหม่ที่เคยถอยด้านwalk-in/receipt/bookingยังไม่ถูกpromote ไม่ใช้ชื่อaliasเป็นหลักฐานweights: มีbase revision, adapter SHA และprofile digestใน `../r132_flow_repairs_20261025/MODEL_BEFORE.json` และตรวจreturned provenanceระหว่างทดสอบ

ตัวบังคับJSONที่เตรียมไว้ในR132ยังไม่ได้เปิดจริง จึงไม่อ้างว่าทำให้ผลดีขึ้นแล้ว Backendเดิมยังไม่บังคับformat ตัวparserตรวจquote/target/edgeตามเดิม และใช้adapterที่ประกาศชัดเพื่อแก้เฉพาะเลขtask idแบบหนึ่งต่อหนึ่งกับroot constraintsที่เป็นรายการว่าง ไม่แก้semantic fields ไม่รับtargetที่แต่งขึ้น ไม่ถือadapted schemaผ่านเป็นraw wireผ่านหรือsemanticถูก

## รายการสาเหตุและการแก้

| กลุ่ม | สิ่งที่ใส่ในระบบ | หลักฐานและข้อจำกัด |
|---|---|---|
| D01 การผูกentity | กันจอที่ซ่อนในจอง/การ์ดจอ แยกcomponentออกจากชื่อเครื่อง และกลับไปหาdevice typeที่ตรง | GPUเดิม13กรณีอ่านequipment_gaming_pc; ไม่ยืนยันฮาร์ดแวร์จริงทุกเครื่อง |
| D02 action/actor | คำถามชดใช้ไม่กลายเป็นinventory; ผู้ปกครอง/เอกสารมาก่อนสิทธิ์บุคคลทั่วไป; cancellationรักษาcustomer actor | APIจริงใช้damage responsibility, guardian, checkin documents; ไม่เอานโยบายเครื่องเสียเองมาตอบผู้ใช้ทำพัง |
| D03 event scope | ขอบเขตแข่งขันมาก่อนกฎศูนย์ และรักษาwatch stream/bug/macro/install/food | CS2ดูสตรีม+บัคอ่าน037/038; macroอ่าน046 ไม่ใช้คำตอบสตรีมของศูนย์ |
| D04 substantive clause | ยอมรับคำสั่งห้าม/อนุญาตเฉพาะ/จำนวนทีมที่เป็นประโยคครบ แม้ตรงheading และยังกันหัวข้อเปล่า | CS2settings045, macro046, food053, roster018; `2. Game Settings`ยังถูกปฏิเสธ |
| D05 format | เลือกข้อความรูปแบบจริงและliteral parent containment แทนชื่อเอกสาร | Tekken29กรณีอ่านsection002 FT2/R3/60S ไม่เลือกชื่อเอกสาร001 |
| D06 คำอ้างกลับ | เมื่อผูกitกับเกมได้ ให้ปรับambiguityที่แก้ได้แล้ว; เก็บplatformที่ยังต้องถาม | ราคาTekken+ปุ่มมีทั้งC06/C05 พร้อมคำเตือนsecondary controls source |
| D07 หลายneeds | ตรวจtopic coverageเทียบข้อความคำถาม เพิ่มชื่อfield brightness/resolution/crosshair และpreparation; เมื่อtopicไม่มีหลักฐานให้unknown | R132ยังตกsettings+macroและprep+food จึงเก็บR132frozenไว้และแก้ในR133; ไม่ถือtyped ledgerเท่ากับทุกneedครบเสมอ |
| D08 จำนวน | แยกเลขในชื่อเกมกับจำนวนปุ่มที่ขอ ถ้าsubsetไม่มีในsourceให้partial | seven buttonsในGranTurismo7ไม่อ้างว่าเลือก7ปุ่มที่ถูกต้องได้แล้ว |
| D09 service/resource scope | การมีเกมในโซนไม่เท่ากับติดตั้งทุกPC; offsiteไม่ใช้ราคาเหมาonsite | PC10ตอบยังไม่ยืนยัน; PC1positiveต้องมีinstallation relations/refs; rent laptop homeไม่ถามราคาเหมาโซนแทน |
| D10 authority/conflict | คงการอ่านsource revisionและexplicit supersession; เลือกliteral extensionได้เมื่อพิสูจน์จริง | cancellation/checkinยังอาจมีคำเตือนต่างฉบับที่กว้างเกิน ต้องตรวจconditions/authorityรายคู่ต่อ ไม่รวมกฎต่างถ้อยคำเอง |
| D11 admission/budget | จองงบหลังได้slot คืนslotเมื่อbudgetfail แยกattempted/transport complete/denied รอคิว15วินาทีภายในdeadline | controlled checksผ่าน แต่ภาระGPUและtail latencyจริงยังวัดอยู่ ไม่สรุปว่าหมดtimeoutแล้ว |
| D12 protocol | promptระบุJSON/version/rootชัด +lossless wire surface adapter พร้อมaudit | การบังคับgenerationยังไม่active; raw/conformant/adapted/semanticต้องแยก |
| D13 source gaps | คงunknownสำหรับnewsจริงที่ไม่มีsource และmode/installed-versionที่ยังไม่ยืนยัน | ไม่เติมข้อมูลธุรกิจจากความคุ้นเคยโมเดล และไม่ฝึกweightsใหม่เพื่อเพิ่มbusiness data |
| D14 applicability | ไม่ใช้confirmationOct20อ้างว่าราคาใช้ได้Oct16หรืออนาคตโดยไม่มีeffective interval | แสดงrecorded ratesพร้อมpartial/date warning ไม่ยืนยันยอดรวมที่ใช้ไม่ได้กับวันที่ถาม |
| D15 rendering/เวลา | แสดงเนื้อหาก่อนชื่อเอกสาร ย้ายบันทึกconfirmationหลังราคา เก็บwarningที่เปลี่ยนความหมายไว้ และลดmodel callในtyped questions | ตรวจAPIจริงแล้ว แต่performanceรวมและคำตอบทุกหมวดยังไม่ปิด |

## ตัวอย่างที่ตรวจคำถาม/คำตอบกับsourceจริง

- “เครื่อง PC ใช้การ์ดจอรุ่นอะไร” → NVIDIA GeForce RTX5060 8GB จาก`equipment_gaming_pc` facet specifications ไม่ใช่Gaming Monitor
- “อยู่ตึกอะไร ชั้นไหน?” → อาคาร5 ชั้น1 จากtyped `center_psu_phuket` เดิมหลุดไปโมเดลแล้วตอบไม่ยืนยัน
- “เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองหรือเปล่า?” → source `r114_q032_owner_policy` เรื่องคำแนะนำผู้ปกครอง/เซ็นยินยอม ไม่ใช้policyบุคคลภายนอกแทน
- “กติกาCS2 ปรับBrightness Resolution Crosshairที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม” → section045บอกปรับเฉพาะในเกมและหน้าจอ +046ห้ามสคริปต์/มาโคร ไม่ตกครึ่งแรก
- “how many players may prepare and what food or drinks are permitted?” → section050ไม่เกิน6คนระหว่างเตรียมตัว +053น้ำดื่มปิดสนิท/หมากฝรั่ง; ไม่เอา6ไปตอบขนาดทีมแข่งขัน
- “How many players must a Counter-Strike2 team have?” → section018ทีม5คน ส่วนVALORANT starting rosterที่ไม่มีsourceยืนยันในsnapshotต้องunknown ไม่ใช้timeout per teamตอบแทน

RawQ/A/selected IDs/receiptsอยู่ใน `installed_acceptance_*/RESULTS.jsonl` การตรวจรับ19กรณีนี้ผ่านหลังอ่านsaved responseแก้assertionของตัวตรวจหนึ่งจุด: APIใช้ชื่อsource field `amount_minor` ส่วนtyped claim facetคือ`amount` จึงไม่ยิงHTTPซ้ำหรือแก้คำตอบเก่า ดู `INSTALLED_ACCEPTANCE_ADJUDICATED.json`

## การทดสอบและสิ่งที่ยังไม่เสร็จ

R133ผ่านcore54, followup9, extended42, owner-scope34 และsource-guard19checks ไม่ใช่จำนวนคำถามอิสระที่บวกเป็นaccuracyได้ ตรวจsource/probeเดิม167กรณีอีกครั้งโดยไม่เรียกโมเดล เก็บคำตอบและข้อจำกัดทุกกรณี ยังไม่เรียก152คำตอบที่เปลี่ยนว่า152คำตอบที่แก้ถูกทั้งหมด

ชุดวัดหลังแก้R132กำลังรันเพียงรอบเดียว **2111unique request keys/5584grade identities** ใช้ชุดR131ที่เลือกก่อนเห็นผลเดิม ครบmembershipC01–C14 คงsource/input/weightsและclockเดิม เมื่อพบข้อบกพร่องหลังfreezeจึงทำR133แยก ไม่แก้ผลR132 ไม่มีbaseline inference/regradeใหม่

ต้องตรวจcoverageทั้งหมด, returned model identity, frozen inputs/model assets, grade identities, changed answers/source regressionsและsemantic unknownต่อ แล้วทำpaired deterministic replayส่วนที่R133เปลี่ยนบนinputsเดิมหรือใช้raw model outputที่ตรงwireจริงเท่านั้น ห้ามเรียกผลR132ว่าเป็นfresh full executionของR133

ต้องรายงานstrictกับpositive-literalแยกไทย/อังกฤษ/autoตามrequested_locale แยกunknown/unassessedและsource-confirmed content failureจากkeyword/first-line/complete-clause/protocol/transport/validity gaps ไม่ใช้keyword failเหมารวมว่าเนื้อหาผิด และไม่ใช้HTTP200เหมารวมว่าถูก

C07ในsampleมีเพียง1จากประชากรเดิม6 ส่วนC14ไม่มีnewsจริง จึงไม่ใช่หลักฐานครบทุกoperationในหมวด การเปรียบsavedR64/R95/R130มีsource/backend/precision/clock/deadlineและภาระเครื่องร่วม รวมการปิดAPIทดลองระหว่างรัน จึงไม่อ้างcausalFlow effectจากคะแนนหรือเวลา

`REQUIREMENTS_TRACEABILITY.json`คง76ข้อ/14หมวดและข้อความ/hashเดิมทั้งหมด เพิ่มหลักฐานและสถานะตรวจรับที่ยังเปิด ไม่มีเปอร์เซ็นต์Flowที่คำนวณขึ้นเอง ไม่มีการประกาศ100%semantic

## กลับไปใช้ตัวเปิดเก่าได้

สำเนาอยู่ในโฟลเดอร์ที่`INSTALLATION_RECEIPT.json`ระบุ: ตัวเปิดR78เดิมและSQLite backup ข้อมูลระบบเก่ายังคงอยู่ที่เดิม การเปลี่ยนรอบนี้เป็นการส่งต่อentrypointsไปbundleใหม่ ไม่มีการยกสิทธิ์อนุมัติหรือpublishข้อมูลให้อัตโนมัติ
