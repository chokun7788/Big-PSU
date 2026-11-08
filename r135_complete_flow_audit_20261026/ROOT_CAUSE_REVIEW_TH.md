# ตรวจสาเหตุคำตอบที่เปลี่ยน — ยังไม่ครบ

รายการนี้เป็นการตรวจรายกรณีโดยเทียบคำตอบที่บันทึกกับข้อมูลต้นทางและหลักฐานของรุ่นที่เกี่ยวข้อง ยังไม่ใช่ผลตรวจครบ 750 กรณี หรือผลยืนยัน Flow ทั้งระบบ

- **Tekken 8: จำนวนเกมต่อแมตช์** — คำตอบ R132 ยกจำนวนรอบต่อเกม จึงยังไม่ตอบจำนวนเกมต่อแมตช์ ต้นทางที่อ้างในคำตอบมีหัวข้อ FT2 แต่เนื้อหามีเฉพาะ R3; ข้อมูลอีกฉบับของรายการเดียวกันระบุผู้ชนะต้องชนะ 2 เกมก่อนและมีเกมตัดสินเมื่อเสมอ 1–1 การตรวจแหล่งข้อมูลของ candidate พบข้อความดังกล่าวแล้ว แต่ยังต้องตรวจขอบเขตรายการ อำนาจและความครบของกฎ ตลอดจนผลคำขอจริง ดูรายละเอียด revision, locator, hash และข้อจำกัดที่ `ROOT_REVIEW_TEK_KEN_FORMAT_20261028.json` การตรวจ route/evidence ID และเวลาในเกณฑ์เดิมต้องแยกจากข้อบกพร่องเชิงเนื้อหานี้

กรณีอื่นยังต้องตรวจและบันทึกทีละรายการ ไม่ถือว่าคำตอบเปลี่ยนเป็นการปรับปรุงโดยอัตโนมัติ

- **ผู้มาเยือนถามสมาชิกและบัตรประจำตัว** — R132 ตอบสิทธิ์ผู้มาเยือนทั่วไป แต่ยังไม่ตอบเงื่อนไขสมาชิกและเอกสารที่ถาม แหล่งข้อมูลที่บันทึกมีข้อความเฉพาะทั้งสองเรื่องและมีรายการเอกสารต่างกัน Candidate ตรวจแยกสองคำขอแล้ว แต่ช่วงเวลามีผลและขอบเขตเอกสารยังต้องตรวจ ดู `ROOT_REVIEW_GUEST_MEMBERSHIP_ID_20261028.json`

- **CS2 ตารางและเวลาแข่งขัน** — R132 คืนเพียงชื่อกฎ แหล่งข้อมูลรายการเดียวกันมีข้อกำหนดเรื่องประกาศสาย ยืนยันเข้าร่วมและเงื่อนไขการมาสาย Candidate ดึงข้อความต้นทางที่ตรงเรื่องได้แล้ว โดยยังต้องตรวจอำนาจ ความครบและช่วงมีผล ดู `ROOT_REVIEW_CS2_SCHEDULE_20261028.json`

- **VALORANT การบูสต์ผู้เล่น** — R132 ตอบกฎบัคทั่วไปและหัวข้อย่อย แต่ไม่ตอบเงื่อนไขบูสต์ที่ถาม ต้นทาง section025 ระบุห้ามบูสต์เหนือระดับกระโดดปกติและกำหนดให้พิจารณาโทษตามเจตนาและผลกระทบ Candidate ดึงข้อความเฉพาะแล้ว ยังต้องตรวจอำนาจและช่วงมีผล ดู `ROOT_REVIEW_VALORANT_BOOST_20261028.json`

- **Warzone บน PC #01** — R132 และ candidate ระบุว่ายังไม่ยืนยันเครื่องเฉพาะ ต้นทางมีความสัมพันธ์เกมกับบริการ PC #03–#10 แต่ไม่พบความสัมพันธ์สำหรับ PC #01–#02 การไม่พบไม่ยืนยันว่าเครื่องไม่มีเกมหรือสถานะสด ดู `ROOT_REVIEW_WARZONE_MACHINE_20261028.json`


### Resident Evil 4: ราคาและช่วงเวลาที่ใช้ได้ (ตรวจบางส่วน)
คำตอบ R132 เพิ่มข้อความว่าไม่ยืนยันอัตราสำหรับ 16 ต.ค. 2026 ก่อนแสดงตัวเลขเดิม และยังระบุการยืนยันล่าสุด 20 ต.ค. หลักฐานที่ส่งเป็น evaluation draft และ common_approved=false จึงยังต้องตรวจความสัมพันธ์เกมกับบริการ อำนาจแหล่งข้อมูล และช่วงเวลาที่ราคาใช้จริง ผล grader เรื่องชื่อเกมและ route แยกจากความถูกต้องของราคา ดู ROOT_REVIEW_RESIDENT_EVIL_PRICE_20261028.json; คง review_required ไม่ regrade หรืออ้างว่าแก้แล้ว

ตรวจ frozen active records เพิ่ม: ความสัมพันธ์ Resident Evil 4 กับ VR 30/60 และ PS5 มีใน migrated source รุ่น 1; ทั้ง 9 rate records รุ่น 2 ที่ตรวจมี unit เป็น unknown แต่คำตอบแสดงต่อคน จึงต้องตรวจต้นฉบับ billing basis และพฤติกรรม candidate เพิ่มก่อนสรุปว่าเป็น bug หรือไม่ ไม่ยืนยันสถานะติดตั้งจริงหรืออำนาจแหล่งข้อมูล

ตรวจต้นทางหน่วยคิดเพิ่ม: owner108:Q049 ระบุทั้งหมดคิดต่อคน มีข้อจำกัดเรื่องราคาเหมาห้องและเศษเวลา และ R114 confirmation อ้างคำตอบดังกล่าว จึงไม่สรุปว่า “ต่อคน” เป็น bug จาก unit unknown เพียงอย่างเดียว คำยืนยัน 20 ต.ค. และ production_applied=false ไม่พิสูจน์ผลย้อนหลัง 16 ต.ค.; candidate และ authority ยังต้องตรวจ

ตรวจการผูก confirmation กับค่าอัตราทั้ง 9 รายการใน frozen source พบ hash ตรง 9/9 และทดลอง candidate ด้วย source snapshot แยกที่เวลา 16 ต.ค. โดยปิด HTTP/model ได้คำตอบที่คงคำเตือนช่วงเวลายังไม่ยืนยัน ดู ROOT_REVIEW_RESIDENT_EVIL_PRICE_20261028.json และ resident_evil_price_source_probe_1793149361991892600/DETAILS.json; เป็นการตรวจ source-only ไม่ใช่ผลโมเดลใหม่ ความใช้ได้ย้อนหลังและ production authority ยังคง review_required


### Luigi’s Mansion 3: คำถามแนวเกม (ตรวจบางส่วน)
R132 เปลี่ยนตำแหน่งหัวข้อแต่คง summary และ genre จาก source draft revision 8; route failure แยกจากเนื้อหา ต้นทางภาษาอังกฤษระบุ mansion แต่ภาษาไทยระบุโรงแรม จึงยังต้องตรวจความถูกต้องและ authority. Candidate source-only probe ซ้ำคำถามและ genre ใน compound output ต้องตรวจการแยกงานและ controls ก่อนสรุปหรือแก้ ดู ROOT_REVIEW_LUIGI_OVERVIEW_20261028.json; ไม่มี model inference ใหม่

ตรวจ artifact เพิ่มพบ definition review สร้าง task summary และ independent verifier เติม task genre; executor แรกส่งทั้ง summary และ genre แล้ว ทำให้การประกอบคำตอบซ้ำ heading/genre ต้องแก้แบบคง coverage และ receipts ของคำถามหลายส่วน ยังไม่ได้แก้ candidate

Candidate แก้การแสดงซ้ำเฉพาะ status และคำถามเดียวกัน เมื่อทุกบรรทัดและ claims เป็น subset ที่แสดงแล้ว คง ledger/receipts; controls source จริง 6 ข้อผ่าน รวม owner edit แยก/forgery/unknown และ dependency request coverage 12 + rules 11 ผ่าน ดู luigi_dedup_regression_1793152967764860400/RESULT.json ทั้งนี้ยังต้องตรวจ authority และข้อความ mansion/hotel โดยไม่อ้างผลโมเดลจริงหรือปิดหมวด C04


### Gaming Chair อยู่โซนไหน
R132 เปลี่ยนลำดับชื่อกับคำตอบ แต่ทั้งเก่าและใหม่ระบุ PC Zone ตรงกับ specifications ใน source revision 6; source เป็น migrated draft legacy_unreviewed ไม่ยืนยันตำแหน่งปัจจุบันหรือ authority. Candidate source-only ได้คำตอบเดียวกัน ไม่มี model/HTTP; route grader แยกจาก content ไม่ regrade. หลักฐาน ROOT_REVIEW_GAMING_CHAIR_LOCATION_20261028.json


### AOV รูปแบบการแข่งขันที่ไม่ระบุรายการ (ตรวจบางส่วน)
R132 ส่ง offline BO3 ตรง draft Blueket Games 2025 ทีมชาย section005 revision4 แต่คำถามไม่ระบุรายการ จึงยังไม่ยืนยันว่าใช้กับแมตช์ผู้ถาม; candidate source-only เพิ่มคำเตือนความครบแต่ยังต้องตรวจการระบุ event/authority แยกจาก route/legacy fact-ID grader. เก็บหลักฐาน ROOT_REVIEW_AOV_COMPETITION_FORMAT_20261028.json ไม่มี model/HTTP ใหม่

ตรวจ artifact เพิ่ม: rule reader เลือก event เดียวที่เหลือหลังกรองเกม ทั้งที่ผู้ถามไม่ได้ระบุ event; receipt ระบุ category_only_no_source_target_bound และ target_binding_verified=false แม้ scope verified=true. สถานะ partial มาจากความครบ dependency ไม่ได้ยืนยัน applicability ของ event จึงต้องแก้/ทดสอบการเปิดเผยหรือถามรายการแยก โดยรักษากรณีผู้ใช้ระบุ event และการเทียบหลายรายการ

Candidate เพิ่มคำเตือนให้ตรวจว่ากติกาของรายการที่แสดงใช้กับแมตช์ผู้ถามเมื่อส่งกติกาจาก event; source controls 5 ผ่าน รวม event ที่ระบุ/แก้ source จริง/ปลอม/คำถามราคา, dependency rule 11 และ coverage 12 ผ่าน. ยังไม่พิสูจน์ event binding หรือ authority และไม่ได้แก้ความหมาย receipt category-only; ไม่อ้าง C13 ปิดหรือ model inference. ดู event_applicability_controls_1793156621374401200/RESULT.json


### คำถามนโยบาย e-mail (ตรวจบางส่วน)
R132 ตอบขอ target โดยไม่มี source hits ใช้เวลา 48.65 วินาที; source draft สามรายการระบุอีเมลติดต่อ แต่คำถาม policy ไม่ได้ยืนยันว่าถามที่อยู่อีเมล จึงห้ามแทน policy ด้วย address โดยไม่มีหลักฐาน. Candidate source-only ระบุไม่มี source ต้องตรวจ clarification ที่ตรงประเด็นและ optional contact ที่แยกชัดเจนต่อ ดู ROOT_REVIEW_EMAIL_POLICY_20261028.json; แยก latency/route จาก semantic ไม่ regrade

Candidate ทดลองถามเจาะจงนโยบายหรือที่อยู่อีเมลเมื่อ source ไม่พบ; controls รอบแรก 2/3 ผ่าน แต่ direct contact email กลับตอบที่อยู่ทางกายภาพและ missing source ต้องตรวจสาเหตุ/เทียบก่อนแก้ แล้วแก้และทดสอบเพิ่ม; เก็บ failed email_policy_clarification_1793158374459396700 ไม่อ้างผ่าน

พบสาเหตุ direct contact: location detector จับคำ email address เป็นที่อยู่กายภาพ และ FAQ intent contact_email ยังไม่ถูก project เป็น typed email channel; แก้ candidate ทั้งสองจุดโดยใช้ intent จาก source, clarification เดิมคงไว้. รอบใหม่ 3 checks ผ่าน email_policy_clarification_1793159340565152700 แต่ยังต้อง source edit/forgery/compound และ dependency controls; เก็บ failed รอบก่อน

ทดสอบ source controls 6 ข้อผ่าน รวมแก้ source จริงบนสำเนา, ปลอม snapshot, คำถามรวม physical address + email, direct email และ policy ที่กำกวม; dependency phone 11/contact matrix 27/core 54 ผ่าน โดยไม่มี model/HTTP หรือแก้ owner data. ไม่ถือว่าข้อมูลติดต่อปัจจุบัน/authority หรือ C01 ทั้งหมวดผ่าน ดู email_policy_clarification_1793160164370680200/RESULT.json


### Animal Crossing คำถามแนวเกมสะกดผิด
R132 ให้ genre ตรง draft revision9 แทนคำตอบ service unavailable ก่อนหน้า; candidate source-only แสดง summary+genre พร้อมแจ้ง translation ยังไม่ผ่าน owner review. ข้อมูลและ translation ยังต้องตรวจ factual/authority; แยก route failure และ latency 46.868 วินาทีจาก content ไม่ rerun หรือ regrade. ROOT_REVIEW_ANIMAL_CROSSING_GENRE_20261028.json เก็บ revision/hash/locator และ probe


### Gaming PC ใช้ทำอะไร (ตรวจบางส่วน)
R132 เปลี่ยนลำดับ heading แต่คง usage/type/location/quantity จาก draft revision11; source draft ไม่ยืนยัน configuration หรือเกมสด. Candidate source-only gaming_pc_usage_source_probe_1793162428549078600 มีคำถามซ้ำและคำตอบ unconfirmed เพิ่ม ต้องตรวจ polite frame/compound และ receipts ก่อนแก้หรือสรุป. หลักฐาน ROOT_REVIEW_GAMING_PC_USAGE_20261028.json ไม่มี HTTP/model ใหม่

สาเหตุคำตอบเพิ่มคือ independent observer จับ gaming เป็น C04 summary ทั้งที่เป็นคำถาม usage ของอุปกรณ์. Candidate กรองเฉพาะ gaming PC use ที่ไม่มี game noun หรือ source-bound ชื่อเกม; source controls 4 ผ่านรวม compound เกมแยก/owner edit/forgery และ request coverage 12 ผ่าน. ยังไม่ยืนยัน hardware สดหรือปิด C03/C04 ดู gaming_pc_usage_controls_1793163378382980900/RESULT.json


### FINAL FANTASY XVI ราคา
R132 เพิ่มคำเตือนใช้วันที่ 16 ต.ค. ไม่ยืนยันโดยคงราคา PS5 สามกลุ่ม; draft game_service revision1 ผูกเกมกับ PS5 และ rate confirmation hashes 3/3 ตรงจากการตรวจ Resident Evil ก่อนหน้า. คำยืนยัน 20 ต.ค. ไม่พิสูจน์วันก่อนหน้า, authority/currentness ยัง review_required; candidate source-only คงคำเตือน ไม่ regrade หรือ inference. ROOT_REVIEW_FFXVI_PRICE_20261028.json
