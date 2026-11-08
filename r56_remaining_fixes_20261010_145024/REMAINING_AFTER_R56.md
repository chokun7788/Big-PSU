# สถานะประเด็นค้างหลัง r56.7

นี่ไม่ใช่รายการบั๊กที่ยังเกิดทั้งหมด: แยกแก้เฉพาะขอบเขตแล้ว, ตรวจจำกัด, source gap และ feature ที่ยังไม่ได้ทำ

## สถานะ T01–T35 ทุกข้อจาก inventory เดิม

| ID | สถานะและขอบเขต |
|---|---|
| T01 | เพิ่ม frozen content contract 156 ข้อแล้ว: 145 ตรวจเนื้อหาตามเกณฑ์ +11 live truth unverified; ไม่ใช่ accuracy ทุก claim |
| T02 | เพิ่มตรวจ required facts/source units/fee child binding และ mutation 11/11; semantic completeness ทุกประโยคยังไม่ครอบคลุม |
| T03 | รัน 156 +38 บน r56.7 รุ่นเดียวแล้ว; source units 110 ผ่าน |
| T04 | แก้ oracle 3 จุดในชุดใหม่ตาม source และแยก v1/v2; legacy ทุกชุดยังไม่ได้ audit |
| T05 | เพิ่มสำนวน 38 เคส; หลังใช้แก้ code เป็น regression แล้ว ยังต้อง external untouched holdout |
| T06 | tests typo/service/calendar ที่เลือกผ่าน; ไม่รับรอง subject+action+ชื่อเกมเสียหนักทุกแบบ |
| T07 | ยังมี ambiguity จริง; ต้องถามยืนยันเมื่อขาด anchor ไม่บังคับ fuzzy เป็นคำใกล้สุด |
| T08 | แก้ scoped equipment negation และ explicit topic correction; nested not only/exception ยังจำกัด |
| T09 | registry รวมทุกเกม/ภาคยังไม่ได้ refactor; preserve known controls/resolver |
| T10 | ขยาย explicit clauses 2–6 พร้อม child source evidence; เกิน6/mixed translation+booking+rules ยังต้องพัฒนา |
| T11 | หลาย target/ทั้งหมดและราคา group/duration ในชุดที่เลือกผ่าน; scope ซ้อนทุกมิติยังไม่รับรอง |
| T12 | เพิ่ม price filter changes หลาย turn และ named selection; TTL/topic shift ทุกลำดับยังไม่ทดสอบ |
| T13 | 8 game/locale source ID coverage ผ่าน CS2 56, RoV12, Tekken7, VALORANT25; RoV partial และ missing facets ยังอยู่ |
| T14 | TH/EN regression และ hash-bound RoV fragment translation; ไม่มี human-approved EN ของ fragment และ Thai word count ยังไม่ตรวจเต็ม |
| T15 | แก้ snapshot ต่อ question/date/transport; parallel fixture fetch ครั้งเดียว; ไม่เปลี่ยน cache policy ของ owner |
| T16 | fault fixtures wrongdate/HTML/401/timeout/empty services ผ่าน; sustained upstream faults ยังไม่ตรวจครบ |
| T17 | shared LLM1 คงไว้; finite fast/LLM/mixed load มีผลเวลาจริง; ไม่ได้ GPU simultaneous all หรือ certified capacity |
| T18 | finite bursts ตรวจแล้ว; sustained fairness/starvation endurance ยังไม่ได้พิสูจน์ |
| T19 | แสดง elapsed/admission/last dispatch/deadline แยกใน API/UI; running-job suspension เกินTTL ยังต้อง audit เพิ่ม |
| T20 | queue idempotency/ambiguous network no replay/admission retry fixtures ผ่าน; live hard-kill ทุกจังหวะยังไม่ทำ |
| T21 | bundled model hashes และ actual portable launch เครื่องนี้ตรวจแล้ว; clean Windows/RAM ต่ำยังไม่ได้พิสูจน์ |
| T22 | compound source evidence และ job timing เพิ่มแล้ว; ไม่สรุป GPU cause จาก stage ล่าสุดอย่างเดียว |
| T23 | ยังไม่มี controlled ablation ทุก layer; รายงาน finite load มี sample/caveat |
| T24 | เพิ่ม readonly storage diagnostic; retention/cleanup ยังไม่เปิดเพราะต้องกำหนดอายุและbackupก่อน |
| T25 | anonymous refresh behavior เดิมตั้งใจ; ไม่ได้ restore session/history โดยเดา |
| T26 | สร้าง DownloadModels/WithModels รุ่น r56.7 ใหม่ source/data hashes ตรง; R50 เก็บเดิม |
| T27 | same-machine actual portable smoke ผ่าน; clean VM/path long/ZIP/download failure ยังรอตรวจ (long output copy เคย fail จึงใช้ short package root) |
| T28 | manifest/version/source/data hash sync ตรวจแล้ว; URL/โฟลเดอร์เก่ายังเป็นรุ่นเก่า ไม่ sync ข้อมูล owner ข้ามชุดเอง |
| T29 | snapshot/diffs/new candidates preserved; ยังไม่ใช่ state migration/rollback updater |
| T30 | Git metadata ยัง broken; ไม่ reset/clean/ซ่อม linkage เพราะต้องจัด provenance ก่อน |
| T31 | local source viewer ยังไม่ได้ทำ; source/fragment labels มีในคำตอบและ trace |
| T32 | owner admin UI publish ทุกหมวดยังไม่ทำ เป็น feature ต่อไป |
| T33 | on-demand WordPress ไม่ต้องเปิด Dashboard; chatbot/server/เครื่องต้องเปิด, service deployment mode ยังต้องเลือก |
| T34 | แก้ creative 80-word routing/repair ที่เกี่ยวร้านเกม; บทความ500คำ/Thai exact words ยังนอก priority |
| T35 | general translation/reasoning ซับซ้อนไม่รับรองครบ; guard ไม่ยอมคืน rejected draft |

## ลำดับที่ควรทำต่อเอง

1. หาก load_final7 ยังมี rejected outputs ให้เก็บ reason/draft/repair/provider timings แล้วแก้เฉพาะ generation หรือ validator ที่ผิดจริง ไม่รวมเป็น HTTP failure
2. ข้อความเกิน 6 งาน: ออกแบบ bounded task graph หรือ explicit clarification ที่แจ้งทุกส่วนไม่ให้คำตอบดูครบทั้งที่ตกส่วนใด; เพิ่ม oracle รายส่วนก่อนแก้
3. บริบท/negation/real-word typo: untouched holdout โดยไม่ใช้พัฒนาก่อน, ตรวจ false corrections และลำดับ 8–12 turns; ไม่ขยาย alias เป็นหลัก
4. คิวจริง: sustained fairness, process suspension/deadline, hard-kill mid-generation โดยทำใน runtime แยก; ห้าม replay ambiguous completion
5. แพ็กเกจ: clean Windows VM, RAM ต่ำ, download failure, path/ZIP และ migration rehearsal
6. Source viewer, registry รวม, owner publish UI เป็นงานเพิ่มที่มีขอบเขตใหญ่ ไม่ใช่ defect ที่ต้องเดานโยบายเพื่อปิด

## คำถามที่ต้องมี source หรือการตัดสินใจจากเจ้าของ

- **RoV**: ขอข้อความต้นฉบับเต็มของข้อ 6.1.5 และ 6.1.5.1 โดยเฉพาะท้ายที่หยุดคำว่า “ออกจาก…”; ผล/บทลงโทษที่ตามมาคืออะไร? ไฟล์ raw ที่ metadata อ้างอิงไม่พบ จึงขอไฟล์ใหม่ ไม่เติมเอง
- **ราคา non-PC**: ตารางปัจจุบันสิ้นสุด 31 มี.ค. 2026; หลังวันนั้นใช้ตารางเดิมหรือมีฉบับใหม่ พร้อมวันที่เริ่ม/สิ้นสุด? แสดงอัตราในไฟล์เดิมพร้อม caveat ไม่เปลี่ยนวันหมดอายุเอง
- **เปลี่ยนวันหลังจ่าย**: “จองผิดวันแต่จ่ายแล้วเปลี่ยนได้” กับ “เลื่อนแทนคืนเงินไม่ได้” ใช้ต่างกรณีอย่างไร ต้องติดต่อช่องทางใด/ก่อนกี่ชั่วโมง? ไม่รวมเป็นสิทธิ์เลื่อนได้ทุกกรณี
- **Tekken pause**: clause ที่มีค่าปรับ/เงื่อนไขไม่ตรงกันในเอกสาร ให้ระบุฉบับ/ข้อที่มีผลก่อนตอบยืนยันเดียว
- **เก็บข้อมูล**: job terminal results/log เก็บกี่วัน backup ที่ใด และใครมีสิทธิ์ดู? Diagnostic ทำแล้ว แต่ยังไม่ลบข้อมูลจริง
- **ใช้งานต่อเนื่อง**: ใช้คอมเครื่องนี้แบบเปิดเอง หรือเครื่องบริการที่เปิดตลอด/Windows service? ยังไม่ตั้ง auto-start โดยเดา

รายการนโยบายเจ้าของ 26 fields และ additional gaps/competition facets จาก inventory เดิมแนบข้างล่างโดยคงความหมายเดิม ไม่ถือว่าคำแปลอังกฤษหรือ API success ทำให้นโยบายเหล่านี้ยืนยันแล้ว

## B. ข้อมูลบริการที่ runtime ระบุว่ายังไม่ยืนยัน 26 เรื่อง

แถวเหล่านี้เป็นข้อมูลขาดจริงใน handler ไม่ใช่ 26 คำตอบผิด เราทำ guard/fixture/คำถามยืนยันได้เอง แต่กำหนดนโยบายแทนเจ้าของไม่ได้

| ID | Field | สิ่งที่ยังไม่ทราบ |
|---|---|---|
| O01 | personal_controller_permission | ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ |
| O02 | combined_transfer_note_format | ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ |
| O03 | multiplayer_game_modes | มีรายการเกมของศูนย์ แต่ยังไม่ได้ยืนยันโหมดเล่นร่วมกันและจำนวนผู้เล่นของแต่ละเกมครับ ต้องการเล่นเกมหรือโซนไหน? |
| O04 | two_person_recommendation | ยังไม่ได้ยืนยันคำแนะนำเกมสำหรับเล่นพร้อมกันสองคนครับ ต้องการเล่นเกมหรือโซนไหน? |
| O05 | game_installation_permission | ยังไม่ได้ยืนยันว่าให้ขอลงเกมเพิ่มหรือติดตั้งเกม โปรแกรม หรือ mod เองได้หรือไม่ครับ |
| O06 | session_extension | ยังไม่ได้ยืนยันขั้นตอนต่อเวลาระหว่างเล่น ต้องจองเพิ่มหรือติดต่อเจ้าหน้าที่อย่างไรครับ |
| O07 | cross_zone_change | ยังไม่ได้ยืนยันขั้นตอนย้ายจาก PC ไป PS5 ระหว่างใช้บริการครับ ถ้าเป็นการจองผิดเครื่อง ข้อมูลข้อ 18 ระบุให้ยกเลิกผ่านอีเมลแล้วจองใหม่ แต่ยังสรุปไม่ได้ว่าใช้ขั้นตอนเดียวกันระหว่างเล่น |
| O08 | game_account_policy | ยังไม่ได้ยืนยันว่าศูนย์มีบัญชีเกมให้ใช้หรือต้องใช้บัญชี Steam ของตนเองครับ |
| O09 | technical_fault_compensation | ยังไม่ได้ยืนยันวิธีคิดหรือชดเชยเวลาที่เสียไปเมื่อเครื่องค้างหรือดับครับ |
| O10 | forgotten_logout_procedure | ติดต่อเพจศูนย์เพื่อแจ้งปัญหาได้ แต่ยังไม่ได้ยืนยันขั้นตอนออกจากบัญชีแทนผู้ใช้ครับ |
| O11 | photo_video_permission | ยังไม่ได้ยืนยันเงื่อนไขถ่ายรูปหรืออัดวิดีโอภายในศูนย์ครับ |
| O12 | streaming_permission | ยังไม่ได้ยืนยันว่าอนุญาตให้สตรีมจากเครื่องของศูนย์ได้หรือไม่ครับ |
| O13 | minor_guardian_policy | ยังไม่ได้ยืนยันข้อกำหนดอายุและการมีผู้ปกครองสำหรับเด็กครับ การเปิดให้บุคคลทั่วไปใช้บริการยังใช้ยืนยันข้อนี้ไม่ได้ |
| O14 | seat_capacity_definition | ข้อมูลจำนวนที่นั่งกับจำนวนเครื่องเป็นคนละช่องข้อมูล ยังไม่ได้ยืนยันว่าจำนวนที่นั่งหมายถึงผู้เล่นพร้อมกันครับ |
| O15 | quotation_receipt_procedure | ยังไม่ได้ยืนยันขั้นตอนขอใบเสนอราคาหรือใบเสร็จครับ |
| O16 | game_version_status | ยังไม่มีข้อมูลสดที่ยืนยันเวอร์ชันเกมบนเครื่องจริง จึงยืนยันว่าอัปเดตล่าสุดแล้วไม่ได้ครับ |
| O17 | update_time_charging | ยังไม่ได้ยืนยันว่าช่วงอัปเดตเกมคิดเวลาใช้บริการอย่างไรครับ |
| O18 | booking_phone_correction | ยังไม่ได้ยืนยันขั้นตอนแก้เบอร์โทรในรายการจองหรือว่าต้องจองใหม่ครับ |
| O19 | overpayment_resolution | ยังไม่ได้ยืนยันขั้นตอนจัดการเงินที่โอนเกินครับ ข้อมูลแก้สลิปไม่ได้ระบุเงื่อนไขคืนเงินส่วนเกิน |
| O20 | underpayment_resolution | ยังไม่ได้ยืนยันว่าโอนขาดต้องโอนเพิ่มหรือจองใหม่ครับ |
| O21 | special_closure_booking_resolution | ยังไม่ได้ยืนยันว่าถ้าศูนย์ปิดพิเศษหลังจองแล้ว จะคืนเงินหรือเลื่อนรายการอย่างไรครับ |
| O22 | capacity_rotation | ยังไม่ได้ยืนยันว่า 4 คนสลับเล่นเครื่องที่รองรับ 2 คนได้หรือไม่ครับ |
| O23 | weather_reschedule | ยังไม่ได้ยืนยันเงื่อนไขเปลี่ยนรอบเมื่อเดินทางไม่ได้เพราะสภาพอากาศครับ |
| O24 | active_session_machine_change | ยังไม่ได้ยืนยันขั้นตอนเปลี่ยนเครื่องระหว่างเล่นหรือระหว่างเกมอัปเดตครับ |
| O25 | payer_identity | ยังไม่ได้ยืนยันว่าใช้บัญชีธนาคารของเพื่อนชำระเงินได้หรือไม่ครับ ข้อมูลการโอนรวมหลายเครื่องไม่ครอบคลุมเรื่องเจ้าของบัญชี |
| O26 | name_matches_id | ยังไม่ได้ยืนยันว่าชื่อในรายการจองต้องตรงกับบัตรหรือแก้ไขอย่างไรครับ |

## C. ข้อมูล/ขอบเขตอื่นที่ต้องมีหลักฐานเพิ่ม

| ID | เรื่อง | คำถามเจาะจง/สิ่งที่ต้องได้ |
|---|---|---|
| D01 | ราคา PS5/Switch/Cockpit/VR ปัจจุบัน | ตารางเดิมหมดอายุ31/03/2026 ยังใช้ราคาเดิมหรือไม่ เริ่ม/สิ้นสุดวันไหน? |
| D02 | เปลี่ยนวันหลังจ่าย vs เลื่อนแทนคืนเงิน | สองกรณีข้อ45/46 ต่างกันอย่างไร ติดต่อช่องทางใดและมีกำหนดเวลาอะไร? |
| D03 | เงินสด | รับเงินสดไหม และรายการจองที่ยังไม่โอนต้องทำอย่างไร? |
| D04 | ค่าจอดรถ | ฟรีหรือมีค่าบริการ แยกประเภท/เจ้าของพื้นที่ไหม? |
| D05 | ค่าเข้าดูเพื่อน | ต้องจ่ายหรือฟรี มีข้อจำกัดจำนวนคน/พื้นที่ไหม? |
| D06 | มาก่อนเวลาจอง | ใช้ที่นั่งโซนกลางรอได้หรือมีจุดรอเฉพาะ? มีที่นั่งพักไม่ได้ยืนยันขั้นตอนรอก่อนจองโดยอัตโนมัติ |
| D07 | เช่าเหมา | ครึ่งวัน/เต็มวันเป็นกี่ชั่วโมง ช่วงเวลาใด วิธีจอง/จ่ายและ validity ราคาเป็นอย่างไร? |
| D08 | จองล่วงหน้า/หลายเครื่อง | จองล่วงหน้ากี่วัน และหนึ่งรายการเลือกเครื่องพร้อมกันกี่เครื่อง? 3 sessions ใช้แทนสองหน่วยนี้ไม่ได้ |
| D09 | Tekken pause | เลือกข้อความข้อห้าม/ข้อยกเว้นและบทลงโทษฉบับใดเมื่อ source ขัดกัน? |
| D10 | RoV ข้อ6.1.5–6.1.5.1 | ประโยคท้ายฉบับเต็มคืออะไร ต้องมีเอกสารต้นฉบับเพื่อเติม ไม่เขียนเอง |
| D11 | กติกา/อุปกรณ์ปัจจุบัน | rulebook ใดใช้ในรายการถัดไป และปุ่ม/รุ่น/setting ที่ติดตั้งจริงตรงแหล่งรองไหม? |
| D12 | อาหารและสิทธิ์ตามกิจกรรม | ข้อยกเว้นเรื่องนำอาหารเข้ากับรับประทาน และบริการทั่วไปกับการแข่งขันยังต้องมี clause ตรง; ไม่ถามซ้ำ public access/ID ที่ผู้ใช้ยืนยันแล้ว |
| D13 | ชื่อภาษาอังกฤษทางการ | ชื่อบุคคล/กิจกรรมที่ไม่มีชื่ออังกฤษยืนยัน ให้คงชื่อเดิม ไม่แต่ง romanization เป็นชื่อทางการ |
| D14 | อายุ/ค่าสมัครแข่ง | ข้อกำหนดแต่ละรายการแยกจากอายุใช้บริการทั่วไป ต้องมี source ของรายการนั้น |

## D. Competition source gaps ที่ manifest ปัจจุบันระบุ

แสดงตาม imported source ไม่ใช่การยืนยันว่าเกมจริงไม่มีกฎเรื่องนั้น บางหมวดซ้ำกับรายการด้านบน ต้องได้ clause ของรายการแข่งขันก่อนตอบ

| เกม | Facet | เหตุผลที่ยังตอบยืนยันไม่ได้ |
|---|---|---|
| valorant | conduct | Active VALORANT rulebook import has no direct conduct or fair-play clause; do not infer one from technical-match sections. |
| valorant | in_match_operations | Active VALORANT rulebook import has no direct instruction naming an official/staff contact for a general in-match issue. |
| valorant | roster_composition | Match Prep allows up to six people in the area but does not establish a starters-and-substitutes roster policy. |
| valorant | team_size | Active VALORANT rulebook import does not directly establish the number of starting players required in the competition roster. |
| valorant | eligibility_registration | Active VALORANT rulebook import does not state a minimum participant age or another direct eligibility requirement. |
| valorant | registration | Active VALORANT rulebook import does not state a roster submission or registration deadline. |
| cs2 | roster_composition | Active CS2 import establishes five players but not a formal starters-and-substitutes roster policy. |
| rov | pre_match_on_site | Active RoV import has tournament rules but no direct on-site arrival or check-in procedure. |
| rov | roster_composition | Active RoV import establishes 5v5 play but not a formal starters-and-substitutes roster policy. |

## E. เมื่อเลือกเปิดให้เครื่องอื่น/คนภายนอกใช้

เป็นเงื่อนไขของการ deploy ใหม่ ไม่ใช่ข้อผิดของ localhost ที่กำลังใช้: ต้องกำหนด session/access ของผู้ดูแลและ log, TLS/network exposure, retention/backup/consent, rate limits และ capacity ของบริการจริงก่อนเปิดออกเครือข่าย ไม่มีการเปิด public ในรอบนี้

