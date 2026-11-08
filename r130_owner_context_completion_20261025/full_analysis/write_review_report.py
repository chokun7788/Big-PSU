"""Publish agent-authored adjudications of saved cases and source evidence.

No automatic semantic scoring: only the explicit adjudications below are
decided. All other cases retain their previous unadjudicated status.
"""
import collections,gzip,hashlib,json,re,sqlite3
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
rows=[json.loads(s) for s in gzip.open(O/'REVIEW_SPECIMENS.jsonl.gz','rt',encoding='utf8')]
source=load(O/'REVIEW_SOURCE_INDEX.json');records=source['records']
con=sqlite3.connect('file:'+str((R/'system/data/knowledge/common.sqlite').resolve()).replace('\\','/')+'?mode=ro',uri=True)

# prefix, decision, diagnosis, repair, additional source record IDs.
reviews=[
('db84ae34','confirmed_actual_content_failure',
 'ถาม PC #10 แต่ตอบเพียง PC Zone/PS5 Zone ไม่ตอบเครื่องที่ระบุ ทั้งที่ relation ของ TEKKEN 8 ระบุ installed_resource_ids เป็น PC01/PC02 และ PS5 ไม่ใช่ PC10 การไม่มี relation PC10 ยังไม่ใช่หลักฐานว่าเครื่องจริงไม่มีเกม แต่คำตอบนี้ละข้อจำกัดหลักและไม่แจ้งว่าศูนย์ยังไม่ยืนยัน PC10',
 'รักษา resource identity ตั้งแต่ตีโจทย์ถึง join game_service→installed_resource_ids; ถ้าไม่ยืนยัน PC10 ต้องระบุส่วนที่ไม่ทราบ ไม่ใช้ zone-level fact ปิด obligation',
 ['migrated_link_availability_pc_01_02_game_detail_tekken_8','migrated_link_availability_ps5_01_02_game_detail_tekken_8']),
('0c25d981','confirmed_actual_content_failure',
 'ถามห้ามใช้บัคและดูสตรีมระหว่างแข่ง CS2 แต่เลือกนโยบายอนุญาตให้สตรีมเกมในศูนย์ทั่วไป C10; ถาม watching กลับตอบ broadcasting และทิ้งคำถามเรื่องบัค Source CS2 sections037/038 ระบุห้ามทั้งสองเรื่องอย่างชัดเจน เป็น scope/predicate failure ที่ยืนยันได้ ไม่ใช่ keyword fail อย่างเดียว',
 'ล็อก event/edition และ action ดู/ถ่ายทอดก่อนเลือก policy; แตกสอง obligations; ห้าม studio FAQ ข้ามมาทับ tournament constraints',
 ['competition_competition_rules_cs2_psu_phuket_2026_section_037','competition_competition_rules_cs2_psu_phuket_2026_section_038']),
('eede3e9b','confirmed_actual_content_failure',
 'Source section045 มีประโยคอนุญาตปรับ Brightness/Resolution/Crosshair เฉพาะในเกมและจอครบแล้ว และ reader เลือก source ถูก แต่ verifier ถือว่า text เท่ากับ heading จึงไม่ substantive และซ่อนคำตอบจริง นี่คือ false rejection จาก verifier ไม่ใช่ข้อมูลหาย',
 'แทนการทดสอบ text!=heading ด้วย clause type/atomic predicate+conditions; ประโยคกติกาเต็มที่ถูกใช้เป็น heading ด้วยต้องอ่านได้ เก็บ source hierarchy และ provenance',
 ['competition_competition_rules_cs2_psu_phuket_2026_section_045']),
('41bef879','confirmed_actual_content_failure',
 'ต้องตอบทั้งสถานที่ปรับ setting และข้อห้าม macro แต่แผนรวมทั้งหมดเป็นหนึ่ง task เลือกเพียง045 แล้วถูก substantive guard ตัดทิ้ง ส่วน046เรื่องห้าม macro ไม่ได้ส่งมา ทั้งข้อมูล045และ046อยู่ใน snapshot',
 'สร้าง need coverage ก่อนเลือก clause และตรวจครบทุก predicate ข้าม section; อย่าให้ receipt ของ clause เดียวปิดคำถามสองส่วน',
 ['competition_competition_rules_cs2_psu_phuket_2026_section_045','competition_competition_rules_cs2_psu_phuket_2026_section_046']),
('cc40820b','confirmed_actual_content_failure',
 'ถาม competition format ของ Tekken8 แต่ตอบแค่ชื่อเอกสาร section001 ทั้งที่ section002 มี Offline/PS5/1v1/FT2/R3/60S และเกมตัดสินครบ Ledger supported จึงไม่ใช่หลักฐานว่าตอบ format แล้ว; กรณีนี้ grader fail แค่ route ด้วยซ้ำ จึงมี false comfort จาก literal checks',
 'แยก document title ออกจาก substantive format facts และ dependency closure; ตรวจ required format predicates แทนการมี record ID หรือคำว่า format',
 ['competition_competition_rules_tekken8_psu_esports_section_001','competition_competition_rules_tekken8_psu_esports_section_002']),
('f6a75fef','confirmed_actual_content_failure',
 'คำตอบบอกไม่มีสเปก GPU แต่ equipment_gaming_pc.specifications มี GPU=NVIDIA GeForce RTX5060 8GB ชัดใน snapshot เป็น binding/projection failure ที่มีข้อมูลอยู่แล้ว ไม่ควรขอให้เจ้าของกรอก GPU ซ้ำ ส่วนสาเหตุย่อยว่า pool ผูกอุปกรณ์ใดต้องตรวจ binding trace เพิ่ม precision.equipment จะ fallback device_type เฉพาะ pool ว่าง',
 'ตรวจ candidate pool และ field facet completeness; เลือก equipment identity จากคำว่า PC ก่อนกรอง component; ห้าม nonempty pool ที่ผิดชนิดตัด fallback ที่ถูกต้อง',
 ['equipment_gaming_pc']),
('7e3ed641','confirmed_actual_content_failure',
 'Which game is available in the Cockpit Zone เป็นคำถาม catalog แต่ไป live booking unavailable เพราะ available ถูกตีเป็นความว่างขณะนี้ ทั้งที่ relation Cockpit→GranTurismo7 มีอยู่ เป็นการเรียก dependency ผิดประเภท',
 'แยก static offering กับ temporal occupancy ด้วย target predicate และเวลาที่ถาม; ตัดสิน catalog ก่อน live gate เมื่อเป็น which game โดยไม่มีเวลา/รอบ',
 ['migrated_link_availability_cockpit_01_02_game_detail_gran_turismo_7','availability_cockpit_01_02']),
('b9fa6734','confirmed_actual_content_failure',
 'ส่วนแรกถามราคา Tekken8 ส่วนหลัง it อ้างกลับเกมเดียวกัน Compiler เก็บ explicit_anaphor และ bound controls_ps5_tekken_8 แล้ว แต่ยังคง ambiguity legacy_meaning_requires_clarification ส่งผลถามชื่อเกมซ้ำ เป็นการส่งต่อบริบทที่ resolve แล้วไปไม่ถึง reader',
 'หลัง binding ผ่านต้อง reconcile ambiguity กับ slot provenance และส่ง target เข้า executor; รักษา ambiguity เรื่อง platform หากจำเป็น แต่ไม่ถาม game identity ที่ผูกแล้ว',
 ['controls_ps5_tekken_8']),
('21fe7ed0','confirmed_actual_content_failure',
 'คำถามภายใต้ VALORANT tournament ถาม macro และอาหาร ส่วน macro อ่านเอกสารตรง แต่คำถามอาหารที่ละ event ถูกแยกไปกฎศูนย์ทั่วไป designated area ทั้งที่ source tournament002 อนุญาตเฉพาะน้ำภาชนะปิดและหมากฝรั่ง ไม่ถือว่ารวมหลาย tasks แล้วเข้าใจ shared scope ครบ',
 'สืบทอด event/edition scope ไป coordinated need ที่ยังอยู่ในบริบทการแข่งขัน พร้อมตรวจไม่มี override ก่อนเปลี่ยนเป็นกฎศูนย์',
 ['competition_competition_rules_valorant_psu_phuket_2026_section_002','migrated_faq_curated_rule_food_drinks']),
('bf6817cf','confirmed_actual_content_failure',
 'ถามจำนวนผู้เล่นทีม CS2 กลับอ่าน game_detail_cs2 แล้วบอก relation ไม่มี ทั้งที่ competition CS2 section018 มี team5players การใช้คำว่า team ไม่ควรไป players_max ของเกมทั่วไป ต้องตรวจชื่อรายการหากมีหลายฉบับจริง',
 'แยก team composition จาก game mode/maxplayers; route ไป competition source และถาม edition เฉพาะเมื่อมีหลายแหล่งที่ทำให้ผลต่าง',
 ['competition_competition_rules_cs2_psu_phuket_2026_section_018','game_detail_cs2']),
('4dc69c73','confirmed_actual_content_failure',
 'ถามยืนยันเชิงปฏิเสธว่ายกเลิกการจองไม่ได้ใช่ไหม แต่ไม่ตอบเงื่อนไขยกเลิก ทั้งที่เลือก FAQ cancel1hour อยู่แล้ว อีก variant กลับอ้างการที่ศูนย์ยกเลิกเพราะผิดกฎ ซึ่งคนละ actor; ข้อสรุปนี้คือ omission/wrong predicate ไม่ใช่การตัดสินว่าทุก policy ปัจจุบันไม่มี conflict',
 'แยก customer cancellation กับ studio cancellation และ polarity; เปรียบ scope/actor/condition ของ source แล้วตอบเฉพาะเงื่อนไขที่ยืนยัน ไม่ให้ negation เปลี่ยน actor',
 ['migrated_faq_curated_cancel_1_hour','migrated_faq_rule_cancel_advance','migrated_faq_rule_booking_cancel_invalid_info']),
('f44d6445','confirmed_actual_content_failure',
 'members of the public หมายถึงผู้ใช้ทั่วไป แต่ระบบเลือก person records และแจ้ง conditional_task_scope ทั้งที่ r114_q037_owner_policy ยืนยันบุคคลภายนอกใช้บริการทั่วไปได้ ข้อความ answer only that point เป็น style instruction ไม่ควรถูกเป็นเงื่อนไขข้อเท็จจริง',
 'วิเคราะห์ noun phrase และ predicate use studio ก่อนจับ token members; แยก style-only qualifiers และเก็บ eligibility scope ไม่ขยายไปการแข่งขัน',
 ['r114_q037_owner_policy','migrated_owner_claim_membership']),
('4a52eaf2','confirmed_actual_content_failure',
 'ถามเช่า laptop กลับบ้าน แต่ตอบราคาเหมาโซน24แพ็กเกจ เป็น scope substitution ระหว่าง offsite equipment rental กับ onsite venue rental ข้อมูลราคา package อ้างถูก source ก็ยังตอบผิดเรื่อง',
 'ต้องมี relation ระหว่าง requested item/service/location กับ rental package ก่อนใช้ราคา; หากไม่รองรับ offsite notebook ให้บอกไม่มีข้อมูล ไม่เสนอราคาเหมาแทน',
 ['package_0']),
('864bd598','confirmed_actual_content_failure',
 'ถาม starting players ของ VALORANT แต่ตอบขั้นตอนจองบริการ6ขั้น เป็น actual off-topic answer แม้เกณฑ์เดิมจะคาด no_answer; ไม่สรุปจำนวนผู้เล่นจริงจาก Match Prep6ซึ่งคนละ predicate',
 'ตรวจ entailment ระหว่าง selected procedure กับ task predicate ก่อน render และคง competition scope; ถ้า source ไม่ยืนยัน starting lineup ต้อง abstain ตรงเรื่อง',
 ['migrated_faq_curated_booking_steps','competition_competition_rules_valorant_psu_phuket_2026_section_002']),
('06563f1a','confirmed_actual_content_failure',
 'ถาม CS2 scripts/macros แต่ไม่ตอบทั้งที่ section046 ระบุห้ามชัดเจน สาเหตุเดียวกับ substantive guard false rejection พบใน traceการเลือก clause; ไม่ต้องเพิ่มข้อมูลหรือน้ำหนักเพื่อทดแทนประโยคที่มีอยู่',
 'แก้ clause verifier และครบเงื่อนไขการเลือก source ตามเดียวกับ case Brightness โดยวัดบนคำถามเดิมแยกรอบ',
 ['competition_competition_rules_cs2_psu_phuket_2026_section_046']),
('7dc03c3b','source_supported_fact_protocol_mismatch',
 'ชื่อ/ทีม/บทบาทประธานที่ตอบตรง person fields ใน snapshot แต่ route knowledge ไม่เหมือน legacy members/overview; ไม่ใช้ route fail ตัดสินว่าชื่อผิด ทั้งนี้ sourceเป็นร่างและไม่ยืนยันว่าบุคคลนี้ยังดำรงตำแหน่งจริง ณวันนี้',
 'แยก protocol scoring จาก source claim scoring; rendererใช้หัวข้อเป็นมิตรและต้องคง validity/publication caveat',
 ['member_1d884f11f3890dea']),
('c42fafb1','source_supported_fact_with_presentation_and_validity_review',
 'ตัวเลขPS5 0/50/150 ต่อ60นาทีตรง rate fields และมี Fortnite→PS5 offering จึงไม่ถือ missingFortnite keyword ว่าราคาผิด แต่คำตอบไม่เขียนว่าเป็นค่าใช้บริการเล่นเกม ไม่ใช่ราคาซื้อเกม และ owner reaffirmed10/20ช้ากว่า workloadclock10/16 ความใช้ได้ตามเวลายังต้องreview',
 'คง game→service ในหัวคำตอบ ระบุฐานคิดราคา/กลุ่มผู้ใช้ และกำหนด effective interval ของอัตราโดยเจ้าของ ไม่อนุมานวันเริ่มจากวันที่ยืนยัน',
 ['migrated_link_availability_ps5_01_02_game_detail_fortnite']),
('63072015','source_supported_requested_clauses_literal_mismatch',
 'คำตอบ RoV ระบุ upper bracketทีมblue เกมแรก ผู้แพ้เลือกข้างเกมถัดไป และGlobalBan/Pickครบตามsource006 แต่ wordingภาษาอังกฤษไม่ตรงcomplete_clauseที่graderกำหนด การขึ้นหัวเอกสารยาวทำfirst_lineไม่ตรง ไม่พบความหมายผิดในสามpredicateที่ตรวจนี้ ข้อความส่วนเกินอื่นไม่ถือว่าผ่านอัตโนมัติ',
 'วัด atomic claims ที่อ้าง source ได้แยกจาก first-line/exactquote; เปิดด้วยคำตอบสามส่วนสั้นแล้วแนบหลักฐาน',
 ['competition_competition_rules_rov_blueket_2025_men_section_006']),
('38b729fb','source_supported_fact_localization_review',
 'ตอบmanagerชื่อไทยภายใต้requested English ไม่ถือว่าชื่อเฉพาะภาษาไทยเป็นThai proseผิดทั้งหมด แต่ยังมี machine-translation disclaimer และกลุ่มMembersที่ควรตรวจภาษา/ขอบเขต ไม่ยืนยันชื่อปัจจุบันนอกsnapshot',
 'แยกproper namesจากภาษาเนื้อหา และตรวจคำแปลที่เจ้าของยังไม่reviewตามfield',
 ['member_17d23bd43ffdcfb0']),
('43fd5b84','appropriate_clarification_in_saved_context',
 'ถาม this game โดยไม่มีชื่อเกมในข้อความ และ saved jobไม่มีประวัติที่ระบุตัวเกม จึงถามเกมและplatformได้ ไม่บังคับตอบมั่วเพราะold outcomeคาดanswer',
 'คงการถามกลับเมื่อไม่มี antecedent; ถ้ามีtrustedhistoryจริงต้องผูกให้ครบก่อนถามซ้ำ',[]),
('22979a6f','ambiguity_review_required',
 'มี1ชั่วโมงและ3ชั่วโมงโดยไม่บอกว่าเปรียบเทียบหรือเล่นรวม/แบ่งsession การถามให้ระบุมีเหตุผล แต่ยังตัดสินไม่ได้ว่าควรตีเป็นcompareโดยอัตโนมัติ; ไม่ให้ oldgraderที่คาดanswerเป็นคำสั่งเลือกเลขแรก',
 'ถามทางเลือกที่สั้น: ต้องการเทียบราคา1กับ3ชั่วโมง หรือเล่นรวม3ชั่วโมง; ประเมินจาก contextที่มีจริง',[]),
('ddbd104b','controlled_live_unavailable_not_real_provider_verdict',
 'คำถามมีเวลา/บริการจึงต้องlive; targetศุกร์2026-09-25ถูกตามjobreference2026-09-24 ไม่ใช่วันที่วันนี้ ตัวharnessคืนfixture_offlineโดยตั้งใจ จึงยังพิสูจน์ไม่ได้ว่าWordPressจริงเสียหรือslotจริงว่าง',
 'เก็บmockกับactualproviderproofแยกกัน และรายงานวันที่/เวลา/ทรัพยากรตามrequest; ห้ามใช้ตารางบริการแทน occupancy',[]),
('a47addbf','confirmed_model_execution_failure_unanswered',
 'JSONทั่วไปไม่ได้ต้องการbusinessdataที่หาย แต่ admissionไม่พร้อมก่อนcontext/generic answer ทำให้ตอบretry ผลผู้ใช้คือไม่ได้คำตอบ; ไม่ใช่คำอธิบายJSONผิดและไม่ใช่เหตุให้ย้ายข้อมูลศูนย์เพิ่ม',
 'ตรวจrequestbudget/admission/queueและgeneral-assistant contract; แสดงสาเหตุเมื่อโมเดลไม่พร้อมและอย่าซ่อนเป็นmissingbusinesssource',[]),
('6da6641f','confirmed_model_protocol_failure_unanswered',
 'selectorHTTPสำเร็จและactualbaseprofileถูก แต่คืนarray i/question/evidence แทนplans schema จึงplans_not_array ตอบไม่ได้ ไม่มีหลักฐานว่าผู้ใช้ได้รับsourceถูกต้อง แม้โมเดลคืนJSONที่อ่านได้',
 'ทำstage-specificschema enforcementพร้อมpromptversionและvalidation; ห้ามยอมรับinput echoหรือปรับparserให้รับข้อมูลโดยไม่ตรวจselection',[]),
('ae809828','confirmed_model_protocol_failure_unanswered',
 'ถามจำนวนผู้เล่นแข่งขันVALORANT selectorใช้เวลาราว46sแล้วส่งevidenceechoที่ไม่ผ่านplans schema และยก MatchPrep6ซึ่งไม่ใช่startingteamcount; outputถูกreject จึงไม่เรียกว่าระบบให้จำนวน6ผิดแก่ผู้ใช้ แต่คำถามไม่ได้รับคำตอบ',
 'แยกMatchPrepกับteamcompositionก่อนselect; บังคับschema/semanticpredicateและจัดtimeoutตามstage',
 ['competition_competition_rules_valorant_psu_phuket_2026_section_002']),
('473dd47b','source_gap_with_qualified_owner_recommendations',
 'ถามNintendo1–2players ระบบไม่ยืนยันรายการตามmode ข้อมูลเจ้าของมีrecommendationsสำหรับมา2คน แต่ไม่มีgame_mode/maxplayersที่ยืนยันทุกเกม คำตอบควรแยกแนะนำจากรับรองโหมด ไม่ถือว่าrecommendationเท่ากับmode proof และไม่บอกว่าไม่มีข้อมูลเกมเลย',
 'เพิ่มview ownerrecommendationsตามเงื่อนไขที่มี พร้อมระบุส่วนmodeที่ยังunknown; จะรับรองmodeต้องมีsourceเฉพาะ',[]),
('db498449','appropriate_partial_source_coverage',
 'HorizonVRมีเพียงGesture/Analogue/gripที่sourceยืนยัน คำตอบบอกว่าไม่ครบlayoutชัดเจน จึงไม่ถือpartialหรือcomplete-clausefailทั้งหมดเป็นcontentwrong และไม่เอาจำนวน3แถวเป็นจำนวนปุ่มทั้งหมด',
 'คงpartialcoverageและเครื่อง/เวอร์ชันที่sourceรองรับ; ขอsourceเพิ่มเฉพาะเมื่อต้องใช้layoutครบ',
 ['controls_vr_horizon_call_of_the_mountain']),
('5fe49766','appropriate_scope_boundary_with_presentation_review',
 'สิทธิ์captureในเกมไม่ครอบคลุมการถ่ายบุคคล/สถานที่ คำถามอัดวิดีโอในศูนย์กว้างกว่าข้อมูล จึงระบุscopeและข้อที่ยังไม่ยืนยันเหมาะสม ไม่ถือว่าownerตอบYesแล้วแปลว่าYesทุกแบบ',
 'รักษาคำถามclarificationให้สั้น: บันทึกในเกมหรือถ่ายสถานที่/บุคคล แล้วแสดงข้อที่sourceยืนยัน',
 ['r114_q033_owner_policy']),
('689469ba','overcautious_equivalence_review_required',
 'แหล่งยกเลิกสองฉบับในตัวอย่างนี้ต่างwordingอังกฤษแต่เงื่อนไขไทยล่วงหน้า1ชั่วโมงตรงกัน การเตือนconflictทุกกรณีดูเกินจำเป็น อย่างไรก็ดีไม่ใช้ความเหมือนข้อความยืนยันsupersession/validityทั้งชุด ต้องตรวจactor/condition/version',
 'ทำsource-backedatomiccondition equivalenceและเก็บทั้งprovenance; ยังคงconflictเมื่อamount/time/exceptionต่างจริง',
 ['migrated_faq_rule_cancel_advance','migrated_faq_curated_cancel_1_hour']),
('95e77247','appropriate_unknown_named_item',
 'ExampleQuestไม่อยู่ในrecords จึงบอกไม่ยืนยันofferingได้ ไม่อนุมานว่าเกมไม่มีอยู่จริงทั่วโลก',
 'รักษาความหมายdatasetabsenceกับrealworldnonexistenceแยกกัน',[]),
('05880449','source_supported_regular_calendar_not_live',
 'ตอบอังคาร09–12/13–16ตรงservice timetableที่บันทึก ใช้regular play serviceไม่ใช่อาคารเปิดหรือเครื่องว่าง; ไม่สรุปจากข้อนี้ว่าตรวจวัน/วันหยุดทุกกรณีถูกครบ',
 'คงregularcalendar/buildinghours/maintenance/occupancyคนละpredicate และใช้specialclosureเฉพาะวันที่ที่ตรวจได้',
 ['migrated_schedule_1']),
('ca7b6119','source_supported_independent_needs_with_limits',
 'ตอบขั้นตอนจองและตารางทั้ง7วันโดยไม่ทิ้งงานหลัง แม้labelpartial; เป็นตัวอย่างว่ากลไกmulti-taskทำได้บางเคส ไม่ใช่หลักฐานว่าบริบทเชื่อมโยงถูกทุกเคส',
 'รักษาการตอบงานอิสระและแยกตารางประจำจากlive; ตรวจsourceเวลาเดิมต่างรุ่นในbaseline',
 ['migrated_faq_curated_booking_steps','migrated_schedule_0','migrated_schedule_4']),
('ed0be633','review_required_billing_and_compiled_scope',
 'มีคำถามNintendo30นาที/กลุ่มนักศึกษาต่างมหาวิทยาลัย แต่แสดงสองrateของขนาดกลุ่มโดยไม่labelและส่วนจองinvalidscope ต้องตรวจbillingruleเต็มก่อนตัดสินจำนวนเงินผิด; ยืนยันได้ว่าคำตอบยังไม่ครบและคลุมเครือ',
 'แสดงperson-range/roundingruleและข้อที่ยังไม่ทราบ; ส่งsharedserviceเข้าbookingพร้อมspanmappingที่ถูก ไม่คิดราคาต่อเวลาเอง',
 ['migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student','migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student']),
('38b729fb','source_supported_fact_localization_review',
 'proper name ภาษาไทยในคำตอบอังกฤษต้องแยกจากข้อความอธิบายไทย ไม่ควรนับThai proseflagเป็นชื่อผิด; ชื่อและroleตรงsnapshotแต่ยังต้องตรวจความเป็นปัจจุบัน',
 'แยกproper name/localeจากcurrentfactvalidity', ['member_17d23bd43ffdcfb0']),
('527eab96','source_gap_and_wrong_clarification_wording',
 'ไม่มีrecordชนิดnewsจริงในsnapshot การไม่ยืนยันข่าวการเมืองล่าสุดจึงไม่ใช่ย้ายข้อมูลเกมไม่ครบ แต่ข้อความให้ระบุเกม/เครื่องไม่ตรงคำถาม ควรบอกข้อจำกัดข่าวล่าสุดหรือใช้general/current-sourcecapabilityที่แยกชัด',
 'กำหนดC14news/current-sourcecapabilityและข้อความno-sourceตามdomainไม่ใช้gameentitypromptเดียวทุกหมวด',[]),
]
# Remove any repeated authored entry for the same saved request.
unique={}
for x in reviews: unique.setdefault(x[0],x)
reviews=list(unique.values())
decisions=[];selected_records={};selected_sources={}
for prefix,status,diagnosis,repair,extra in reviews:
 x=next(row for row in rows if row['key'].startswith(prefix))
 ids=list(dict.fromkeys([*(x.get('query_plan') or {}).get('record_ids',[]),*extra]))
 evidence=[]
 for rid in ids:
  rec=records.get(rid)
  if not rec:continue
  fields={k:v for k,v in rec['fields'].items() if k!='legacy_context' and v.get('status')=='known'}
  selected_records[rid]={'record_id':rid,'kind':rec['kind'],'revision':rec['revision'],'lifecycle':rec.get('lifecycle'),'validity':rec.get('validity'),'fields':fields}
  for field,v in fields.items():
   for ref in v.get('evidence_refs',[]):
    sid=ref['source_id']
    if sid not in selected_sources:
     raw=con.execute('select snapshot from cc_sources where source_id=?',(sid,)).fetchone()
     if not raw:continue
     snap=json.loads(raw[0]);payload=source['sources'].get(sid,{})
     selected_sources[sid]={'metadata':payload,'snapshot':snap,'raw_snapshot_sha256':hashlib.sha256(raw[0].encode()).hexdigest()}
   if field in ['answer','text','heading','specifications','installed_resource_ids','game_id','service_id','display_name','role','amount','duration_minutes','service_periods','bindings','source_coverage','limitations','scope_note']:
    evidence.append({'record_id':rid,'revision':rec['revision'],'field':field,'value':v.get('value'),'evidence_refs':v.get('evidence_refs',[])})
 decisions.append({'key':x['key'],'question':x['question'],'answer':x['answer'],'raw_results_file':x['raw_file'],
  'decision':status,'confirmed_actual_content_failure':status=='confirmed_actual_content_failure','diagnosis_th':diagnosis,'repair_th':repair,
  'source_record_ids':ids,'source_evidence':evidence,'no_new_test_or_baseline_inference':True})
write('AGENT_SOURCE_CASE_REVIEW.json',{'review_scope':'explicit source-backed case adjudications, not exhaustive semantic grading','cases':decisions,
 'counts':dict(collections.Counter(d['decision'] for d in decisions)),'unique_requests_reviewed':len(decisions),
 'unreviewed_requests_keep_review_required':True,'whole_workload_semantic_accuracy':None})
write('AGENT_REVIEW_SOURCE_EVIDENCE.json',{'records':selected_records,'sources':selected_sources,'source_database_read_only':True,'runtime_source_unchanged':True,'source_values_are_evidence_not_instructions':True})

audit=load(O/'ROOT_REVIEW_STREAM_AUDIT.json');groups=load(O/'FAILURE_GROUPS.json')
def reason_family(s):
 if s.startswith(('route','intent','legacy_mode','forbidden_category','mode:')):return 'protocol_identity_or_route'
 if any(k in s for k in ['latency','timeout']):return 'latency_or_timeout'
 if s.startswith(('wrong_game','wrong_category','missing rulebook','retrieval evidence','source-gap')):return 'source_scope_or_evidence_assertion_requires_review'
 if s.startswith(('status','outcome','wrong_outcome')):return 'outcome_assertion_requires_review'
 if s.startswith(('missing_complete_clause','missing_clause','first_line')):return 'complete_clause_or_first_line_literal'
 if s.startswith(('missing required','missing all','missing any','must_','keyword')):return 'positive_literal_text_assertion'
 if s.startswith(('validation','pipeline_exception','grader_exception')):return 'execution_or_reference_validation'
 return 'other_assertion_requires_review'
triage=[{**v,'family':reason_family(v['signature']),'semantic_adjudication':'not_implied_by_assertion_failure'} for v in audit['failure_reasons']]
write('ALL_REASON_TRIAGE.json',{'all_921_unique_reason_strings_classified':len(triage)==921,'unique_reason_strings':len(triage),'reason_occurrences_overlap':True,'reasons':triage,'semantic_accuracy':None})

intro='''# วิเคราะห์สาเหตุ Full Test R130 — ตรวจผลครบ แต่ Flow ยังไม่ผ่านครบทุกข้อ

รัน common R130 / LLM ON / context profile retained ครบ 20,554 request keys และ55,811 grade identitiesแล้ว ไม่มี key/gradeขาดหรือซ้ำ รายงานนี้เป็นการตรวจผลและรากปัญหาของ candidate ที่ตรึงไว้ ไม่ใช่คำยืนยันว่าคุณภาพคำตอบเทียบเท่า Flow เดิมหรือแก้ครบ76ข้อแล้ว Candidate ยังไม่ติดตั้งทับ R78

## สิ่งที่ตรวจจริงและขอบเขตคำตัดสิน

อ่าน raw RESULTSทั้งสองไฟล์แบบstreamingครบ20,554 requests/55,811 grades, ALL_FAILURESครบ54,333 failed-grade rows, PER_REQUESTครบ20,554 rows และreason stringsทั้ง921แบบ แยกเป็นทุกกลุ่มที่ปรากฏ เก็บ225specimensจากทุกcategory/terminal-reason signatureที่พบรวมตัวอย่างที่เลือกเจาะจงไว้ใน REVIEW_SPECIMENS.jsonl.gz ไม่ได้รันคำถามใหม่ ไม่ regradeหรือเรียกbaselineเดิม ไม่มีLLM judge

AGENT_SOURCE_CASE_REVIEW.json เป็นคำวินิจฉัยที่ agentตรวจคำถาม/คำตอบ/แผน/โค้ด/ค่าsourceและlocatorจริงเฉพาะกรณีที่ระบุ ดึงrecordrevisionและsource snapshotจากSQLiteแบบread-onlyไว้ใน AGENT_REVIEW_SOURCE_EVIDENCE.json การอ่านทุกแถวเพื่อจัดกลุ่มไม่เท่ากับตัดสินความหมายทุกคำตอบ ข้อที่ไม่ได้adjudicateยังต้องreview; ไม่คิดoverall semantic accuracyจากกลุ่มตัวอย่างหรือจากreceipt

ต้องแยก (1)ข้อเท็จจริงเท็จ (2)ตอบไม่ครบ/ผิดpredicate/ผิดscopeทั้งที่sourceมี (3)แหล่งไม่พอจริง (4)การปฏิเสธจากprotocol/transport (5)เกณฑ์ข้อความไม่ตรง ทั้ง5อย่างทำให้คะแนนต่างกัน แต่ไม่ใช่เหตุเดียวกัน

## Coverage และความคงเดิมของการทดลอง

- COVERAGE.json และ ROOT_REVIEW_STREAM_AUDIT.json ตรวจทั้งkeyและ(file,row,variant) identitiesเทียบfrozen FULL_JOBS อีกครั้งครบทุกตัว ไม่มีการเทียบแค่จำนวนรวม
- INDEPENDENT_COMPLETION_VERIFICATION.json ตรวจhash frozen2,361files รวมcode/data/inputs/prompt/modelassets; เปรียบlogical snapshot BEFORE/AFTERที่ครอบsource bodies/revisionsและWAL และprofile/adapter/digest/messages/schema/stageจากactual successful gateway calls ไม่อาศัยชื่อโมเดลอย่างเดียว
- contextใช้retained R121adapterบนengine/dataR130 ส่วนselector/genericใช้base Actual model name psu-r129:latest; HF NF4 double-quant BF16 ต่างbackend/precisionจากsavedlegacy
- newadapterฝึกจริงแล้วแต่ไม่promote เพราะsource-critical regressionsที่walk-in/receipt/bookingและCS2format ดู PLANNER_ADJUDICATION_REVIEW_TH.md การที่newwireดีขึ้นไม่พอ; retainedไม่ใช่R64legacy และwire0ไม่ใช่accuracy0
- sourceเป็นevaluation draft847active/24withdrawn เก็บ824เดิมและapprovalsเดิม ไม่มีการอนุมัติเผยแพร่แทนเจ้าของ; sourceอยู่ในsnapshotไม่ยืนยันcurrentrealworldทุกข้อ
- fixedclockส่วนใหญ่2026-10-16 และreference_dateเฉพาะjob ไม่ใช้เวลาที่ผู้ตรวจเปิดรายงาน เช่นศุกร์นี้ในjob2026-09-24หมายถึง2026-09-25

## คะแนนที่ใช้ตัวหารเดียวกันกับsaved Flow

ไทย/อังกฤษ/autoแยกตามrequested_locale ไม่ใช่effective_locale ค่าpositive literalเป็นเกณฑ์ข้อความที่กำหนดจากinput ไม่ใช่เปอร์เซ็นต์ตอบถูกเชิงความหมาย

| ภาษา | gradesทั้งหมด | R64 strict | R95 strict | R130 strict | positive eligible | R64 literalผ่าน/eligible | R95 literalผ่าน/eligible | R130 literalผ่าน/eligible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ไทย |25,100|70.57%|8.33%|0.92%|13,142|95.47%|75.51%|78.06%|
| อังกฤษ |27,319|83.09%|9.05%|2.94%|9,466|95.95%|71.00%|75.81%|
| auto |3,392|64.53%|13.71%|13.12%|2,301|81.79%|71.23%|70.19%|

R64 literalยังประเมินไม่ได้ไทย74/อังกฤษ9/auto111 รวม194 คงไว้ในeligible denominator ไม่ตัดออกเพื่อเพิ่มคะแนน R95/R130ไม่มีunassessedในliteral tableนี้ แต่ยังไม่ได้semanticadjudicationทุกข้อ

รวมR130 strict1,478/55,811 (2.6482%); literal19,050/24,909 (76.4784%) ส่วนR95literal18,283/24,909 ต่าง+767checks: R130ผ่านเฉพาะ3,397 แต่เสียให้R95 2,630 โดยใช้identitiesเดียวกัน ไทย+336อังกฤษ+455auto−24 ไม่ได้แปลว่าทุกหมวดดีขึ้น และยังตามsavedR64อยู่มาก

strictR95ผ่าน5,030 เทียบR1301,478: R95-only3,761/R130-only209/both1,269 ส่วนR64strict42,601/55,811 ต้องแยกroute/protocol/contractก่อนสรุปquality ข้อมูลsource/backend/precision/clock/deadline/admissionและpolicyversionsต่างกัน จึงไม่ใช่causal effectของFlowหรือน้ำหนักล้วน ๆ

ไม่เปลี่ยนหรือregradeผลbaselineเพื่อแก้ตัวเลข ดู FIXED_DENOMINATOR_SCORES.json และ SAVED_FLOW_COMPARISON_TH.md

## วิเคราะห์ครบทุกfailure group

จำนวนด้านล่างเป็นrequestsที่ซ้อนทับได้ ไม่บวกเป็นจำนวนคำตอบผิด ไม่มีการเอาfailedgrades54,333ไปเรียกว่า54,333คำถามผิด

### 1. protocol_mismatch — 19,221 requests

routeของcandidateเป็นknowledge/common_read ขณะที่graderเดิมต้องการgames/reservation/service_fee/competition_rules ฯลฯ จึงตกstrictจำนวนมาก บางเกณฑ์บังคับlegacy pipeline modeที่ระบบใหม่ไม่ได้ใช้ มี12,808requestsที่failedgradesทั้งหมดมีเพียงroute/intent assertions แต่ห้ามนับ12,808ว่าsemanticถูกทั้งหมด: Tekkenformatที่ตอบแค่ชื่อเอกสารเป็นตัวอย่างactualomissionแม้graderพบเพียงroute

ตัวอย่างชื่อประธานตรงsourceแต่routeตก แยกจากPC10ที่routeตกพร้อมละresourceจริง แนวแก้คือรายงานcontract compatibilityแยกจากsource/meaning โดยเก็บstrictเดิมไว้ ไม่เพียงเปลี่ยนrouteให้ผ่านแล้วอ้างว่าตอบดีขึ้น

### 2. controlled_provider_unavailable — 4,132 requests: ชื่อกลุ่มอัตโนมัตินี้กว้างเกินไป

analyze_full.pyใส่ทุกterminal provider_unavailableรวมกัน จึงห้ามอ้างว่าทั้ง4,132เกิดจากlivefixture: taskเหตุmodel_transport_failure1,588, r101_model_unavailable1,546, model_plan_missing26 รวม3,160 เป็นmodel-coded ส่วน972ไม่มีreasoncodeในtaskและต้องดูnative live artifactsในverificationประกอบ ไม่อนุมานproviderจริงล่มจากชื่อterminal

คำถามliveที่ถูกscope เช่นVRศุกร์10:00ตอบไม่ยืนยันตามfixture_offlineที่harnessตั้งใจ เป็นbehaviorของtestเท่านั้น แต่Which game is available in Cockpitถูกส่งไปliveเป็นactualroutingfailureแม้unavailablemessageปลอดภัย ข้อJSONทั่วไปถูกadmissionปฏิเสธเป็นอีกสาเหตุ ไม่ใช่businessdataขาด

แนวแก้: reasonnamespaceแยกlive_fixture/model_busy/model_timeout/schema_failure; static offeringต้องไม่รอlive provider; external liveการตรวจจริงต้องมีresource/date/window/provideridentity/TTLครบจากAPIruntimeจริง

### 3. source_id_or_evidence_requirement_review_required — 2,781 requests

missing rulebook IDs/retrievalevidence/wronggameflagsรวมทั้งกรณีไม่มีhitsเพราะไม่ตอบ จึงไม่พิสูจน์ว่าเสิร์ฟกติกาผิดเกมทุกแถว ต้องmapcanonicaloldIDsกับnativecompetition/sectionIDsพร้อมsourcehashและfieldpointerก่อนตัดสิน กรณีCS2streamดูsourceผิดscopeยืนยันได้; ส่วนคำถามorganizer equipmentที่โมเดลไม่พร้อมและไม่มีhitsคือunansweredไม่ใช่wronggamefactsที่ผู้ใช้ได้รับ

sourceมีเนื้อหาจริงแต่facetผิดก็เกิดปัญหา เช่นCS2settings045ถูกจัดfaceteligibility_registrationทั้งที่ข้อความเป็นmatchsettings ต้องแก้data/compiler taxonomyเฉพาะrevisionถัดไป ไม่ฝึกโมเดลเพิ่มเพื่อกลบmetadataและไม่แก้frozenผลรอบนี้

### 4. literal_or_reference_contract_review_required — 2,431 requests

Fortniteราคาตรงrateแต่ไม่เอ่ยชื่อเกม/ฐานคิดในข้อความคือpresentation+predicateclarity; ชื่อไทยในคำตอบEnglishไม่เท่ากับThai proseทั้งย่อหน้า; บางmissingalternativesเป็นactualunansweredจากadmission เช่นJSON ไม่ใช่literalfalsepositiveทุกข้อ ต้องตรวจsource/currentmode/translationstatusแยกรายcase

### 5. outcome_mismatch_review_required — 1,883 requests

clarificationแทนanswerอาจเหมาะเมื่อไม่มีชื่อเกม/มีdurationสองค่า; อาจผิดเมื่อtargetถูกresolveแล้วแต่ยังถามซ้ำ เช่นTekken8→it ตัวสถานะanswerก็ไม่ยืนยันว่าตอบครบ: ledgerรองรับclaimที่ผิดpredicateยังเป็นsupportedได้ C07offsite notebookกลับตอบonsitepackagesเป็นactualscopeerror ไม่ใช่แค่outcomelabel

### 6. keyword_firstline_clause_mismatch_review_required — 702 requests

RoVupperbracket/loserchoosesside/GlobalBanPickมีเนื้อหาตรงsourceแต่ถ้อยคำอังกฤษต่างcanonicalcompleteclause จึงไม่เรียกว่าfactwrong ขณะCS2streamหรือMacroไม่ตอบจริงเป็นfailureที่sourceยืนยัน คำว่าfirst_line_off_topicอาจเกิดจากขึ้นหัวเอกสารยาวซึ่งเป็นUXผิดแม้ข้อมูลข้างล่างถูก

พบverifierผิดสองทิศ: text==headingทำให้ประโยคกติกาเต็มถูกปฏิเสธ (CS2brightness/macro); title-onlyถูกปล่อยเป็นsupportedเมื่อไม่เข้าregexcan/may/where/allowed จึงตอบTekkenformatไม่ครบ ต้องตรวจpredicates+conditions/dependency closure ไม่ใช่literalheadinginequality

### 7. source_gap_validity_or_conflict_review_required — 575 requests

missing_sourceเป็นstatusไม่ใช่หลักฐานdataหาย: GPUมีsourceแต่readerหาไม่เจอ, cancelFAQมีแต่negation/actorผิด, relationทีมCS2ไปอ่านgamecardผิด ส่วนgame_mode/playercounts/installedversion/privatefieldsไม่ยืนยันจริง และHorizoncontrolsมีsourcecoveragepartialตามที่บอก ต้องแยกmigration gap/reader gap/current validity gap

คำเตือนpolicyconflict320task occurrencesอาจมีทั้งconflictจริงและequivalent wordingที่ยังไม่normalize เช่นcancel1hourไทยตรงกัน ห้ามเลือกฉบับล่าสุดจากtimestampเฉย ๆ แต่ควรยอมรับexact/atomic equivalenceที่ตรวจscopeactorconditionแล้ว อัตราเจ้าของยืนยัน2026-10-20ภายใต้clock2026-10-16ยังมีtemporalconfound ไม่อ้างเป็นcurrentpriceที่พิสูจน์แล้ว

### 8. performance — 388 requestsตามlatency assertions

rawlatencymedian0.663s/p953.575s/p9947.175s/max151.130s; >10s350requests, >20s340requests ตัว388ใช้ceilingต่างกันตามgradeจึงไม่ควรเทียบตรงกับ350 Normaltypedpathเร็วแต่modeltailยังช้ามาก

actualHTTP425attempts/263successes/162transportfailures ไม่ใช่ทั้ง20,554เรียกLLM มีadmission/modelconcurrencylimit1/wait0.20sร่วม2workersและserverqueue จึงมีโมเดลไม่พร้อมโดยไม่ยิงHTTPอีกจำนวนมาก ตามeventcodeและlog ไม่ใช่networkproviderภายนอกทั้งหมด สำเร็จHTTPแล้วยังselectorJSONผิดschemaหรือretainedwireผิดversionได้ จ่ายเวลาแล้วต้องfallback/retry

APIowner50ก่อนFullmedian0.474s/p950.608s แต่building/floorข้อ6ใช้41.187sเพราะเรียกcontext40.469sโดยไม่จำเป็นแล้วจึงอ่านtypedได้ ไม่ใช่ไม่มีที่อยู่ งานแก้คือsource-backednativefielddispatch+context-awaregate, queue/backpressure/timeoutตามstage และprotocolenforcement ไม่เพิ่มretryหรือtimeoutทุกจุด

### 9. model_protocol_failure — 162 requests (คนละตัวหารกับ162HTTPfailures)

พบtransport_okแต่schemafalse185eventoccurrencesในdomain_flow: retainedcontext r121_root_fields121 กับselectorbase64 บางrequestมีมากกว่าหนึ่งeventจึงเหลือ162requests ไม่ใช่162คำตอบที่โมเดลกล่าวfactผิดโดยตรง

HFbackendเก็บschemahashแต่ไม่ได้constrainserialization ส่วนSYSTEMไม่ระบุJSON/versionliteralชัด ทำให้retainedversion1.0/hybridgraphและbaseinputechoไม่ผ่าน เป็นintegration/protocolproblemจริง newadapterช่วยwireแต่เสียcriticalsourceanswersจึงไม่promote ดูactualstage/profile/messages/schema proof ไม่อ้างwire0ว่าFlowเก่าตอบถูก0%

## ภาพรวม14หมวด: มีreaderไม่เท่ากับหมวดผ่านครบ

| หมวด | สิ่งที่ตรวจพบจากผลจริง | สิ่งที่ต้องแก้/ยืนยันต่อ |
|---|---|---|
| C01 ศูนย์/ติดต่อ | addressอ่านได้ แต่building/floorมีtail41sก่อนFull | dispatchfieldsetsก่อนmodel; sourcevalidity/publication |
| C02 บุคลากร | president/managerตรงsnapshot แต่publicถูกจับmembersและชื่อสะกดใกล้บางคนbindไม่ติด | phraseintent/personidentity/publicscope/period |
| C03 อุปกรณ์ | zoneinventory/usageบางข้ออ่านได้; GPUบอกไม่มีทั้งที่มี | equipmentbinding+componentprojection; อย่าให้receiptแทนrequestedfacet |
| C04 เกม | relation/cockpitcatalogบางข้ออ่านได้; PC10scopeหายและavailableไปlive | game→service→resource, temporalpredicate, modeunknownแยกrecommendations |
| C05 ปุ่ม | tableบางเกมครบตามsource; Horizonpartialถูกระบุ; itboundแล้วแต่ยังถามเกมซ้ำ | ambiguityreconciliation/platform/version/controlsubset |
| C06 ราคา | rates/multidurationบางเคสอ่านได้ แต่audience/count/30minbillingต้องreview | typedbillingrule/rounding/group-size labels/effectiveinterval |
| C07 เหมา | onsitepackagesอ่านได้แต่offsite notebookถูกตีเป็นเหมาโซน | service/item/location capabilityต้องตรงก่อนใช้ราคา |
| C08 จอง | ขั้นตอน6ข้อ/บางcompoundทำได้; cancelnegation/actorและtypoยังพลาด | action/actor/polarity/validity/duplicate-equivalence |
| C09 ชำระ/คืนเงิน | refundอ่านsourceได้บางข้อ; policiesมีเงื่อนไขขัดหรือคนละscenario | แยกrefund/credit/paidchange/rain ไม่ขยายสิทธิ์จากคำว่าแจ้ง |
| C10 กฎศูนย์ | sourceowner50ฟื้นแล้วแต่stream/capture/foodต้องคงscope | tournamentvsstudio/watchingvsbroadcasting/conditionalpermission |
| C11 ตาราง | weekly7days/weekdayอ่านได้หลายข้อ; typo/fallbackบางข้อไม่ตอบ | regularservice/buildingaccess/maintenance/closure/currentdateแยกกัน |
| C12 live | binding/provider/windowmechanismsมีและreadinessแยก; workloadfixtureoffline | ห้ามใช้ผลmockยืนยันslotจริง; แก้catalogmisroute |
| C13 แข่งขัน | มี104clauserecordsแต่header/metadata/closure/verifierทำให้ละคำตอบที่มี | สำคัญสุด: exactpredicate+eventscope+multi-clause+substantiveverification |
| C14 ข่าว/ทั่วไป | ไม่มีrealnewsrecord; generalJSONถูกadmissionblock | แยกlatest-sourcecapabilityกับgeneralknowledgeและno-sourcewording |

## คำถาม/คำตอบ/sourceที่agentตรวจรายกรณี

สถานะconfirmed_actual_content_failureด้านล่างรวมคำตอบไม่ครบและผิดscopeตามsource ไม่ได้หมายความว่าทุกประโยคในคำตอบเป็นfactเท็จ Sourceเหล่านี้เป็นหลักฐานในfrozenevaluation ไม่ใช่ใบรับรองpublished/currentworld ส่วนcaseที่semanticยังไม่ชัดคงreview_required ไม่เพิ่มคะแนนเอง

'''
body=[intro]
for i,d in enumerate(decisions,1):
 body += [f"### กรณี {i}: {d['decision']}\n",f"Key: `{d['key']}`; raw: `{d['raw_results_file']}`\n",f"คำถาม: {d['question']}\n",'คำตอบที่บันทึกไว้ (excerptเมื่อยาว):\n',d['answer'][:2400]+'\n',f"วินิจฉัย: {d['diagnosis_th']}\n",f"แนวแก้: {d['repair_th']}\n"]
 ev=d['source_evidence']
 if ev:
  body.append('หลักฐานsource (รายละเอียดและsource snapshotsเต็มใน AGENT_REVIEW_SOURCE_EVIDENCE.json):\n')
  preferred=[v for v in ev if v['field'] in ['text','answer','specifications','installed_resource_ids','role','display_name','service_periods','source_coverage','limitations']]
  for v in (preferred or ev)[:8]:
   text=json.dumps(v['value'],ensure_ascii=False);refs='; '.join(ref['source_id']+'#'+ref.get('locator','') for ref in v['evidence_refs'])
   body.append(f"- `{v['record_id']}` rev{v['revision']}.{v['field']}: {text[:1400]} — `{refs}`\n")
 else:body.append('หลักฐาน: saved request/trace/harnessหรือabsenceของชนิดข้อมูลที่อธิบายไว้ ไม่สร้างsourcefactเพิ่มเพื่อปิดช่องว่าง\n')
body.append('''
## ลำดับแก้ที่ได้จากหลักฐานรอบนี้

1. **Protocol/backendและadmission**: สร้างcandidateถัดไปแยกfreeze แก้explicitversion/JSON+schemaenforcementทุกstage, selectorcontractและbusy/timeoutreason โดยตรวจsemanticไม่ใช่แค่parseได้ ห้ามยอมรับinputecho
2. **C13และscope propagation**: เก็บevent/edition/actor/actionในทุกneed ตรวจsubstantiveclauseแบบatomicconditions แก้settings045facet และheader/dependencyselection ทั้งcaseที่rejectผิดและปล่อยheadingผิด
3. **Binding/obligation completeness**: PC10resource/GPUcomponent/explicitit/negativecancel/publicnounphrase ต้องส่งconstraintsไปถึงreader และตรวจwholequestioncoverageไม่ใช่แค่coverageของแผนที่อาจตกneedตั้งแต่ต้น
4. **Source authority/validity**: ตรวจequivalenceแบบมีactorconditionและrevision; แยกownerrecommendationจากgame_modeและcurrentinstallation; แก้effectiveinterval/translationreview/sourcegapsที่sourceยังไม่มีจริง ห้ามสรุปว่าต้องย้ายข้อมูลเพิ่มทั้งหมด
5. **Rendererและlatency**: เปิดด้วยคำตอบตรงpredicate ระบุperson-range/เวลา/ราคาอย่างอ่านง่าย แสดงสาระกติกาแทนชื่อเอกสาร; ทำlocalfieldreadก่อนmodelในคำถามที่พิสูจน์scopeได้ แล้ววัดหางlatencyด้วยprofileเดิมที่ตรึงไว้

ใช้savedfailingcasesเดิมเป็นregressions ไม่ต้องเพิ่มคำถามเพื่อกลบผล การเปลี่ยนruntime/prompt/backendหลังวัดต้องอยู่candidate/freezeถัดไปพร้อมbaselineคู่ที่เหมาะสม ไม่แก้rawRESULTS/grade/source/approvalsเดิม และไม่ตีว่าการฝึกLoRAเพิ่มเป็นคำตอบของreader/verifier/data-taxonomyทุกปัญหา

## สถานะงานจริง

Fullcoverageและการวิเคราะห์รากปัญหาทุกกลุ่มเสร็จแล้ว แต่Flowยังไม่ผ่านครบ76requirementsเชิงคุณภาพ ไม่มีการประกาศoverallsemanticaccuracyหรือ100%completion REQUIREMENTS_TRACEABILITY.jsonคง76หัวข้อและแยกimplementationevidence/evaluationevidence/remainingacceptance ไม่ตีว่าทุกหัวข้อcompleteเพราะAPIหรือlocaltestsผ่าน

ยังต้องreviewsemanticของคำตอบที่ไม่ได้adjudicate, billingบางscope/validity/edition/sourceconflicts/unknownmode และแก้confirmedfailuresข้างต้น ผลนี้ไม่ใช่เกณฑ์ติดตั้งทับR78 การปิดheartbeatหมายถึงFull Testรอบนี้และรายงานวิเคราะห์เสร็จ ไม่ใช่รับรองFlowพร้อมใช้งานครบแล้ว
''')
(O/'ROOT_CAUSE_REVIEW_TH.md').write_text('\n'.join(body),'utf8')
print(json.dumps({'cases':len(decisions),'decisions':dict(collections.Counter(d['decision'] for d in decisions)),'source_records':len(selected_records),'source_snapshots':len(selected_sources),'all_reason_strings':len(triage),'report_chars':sum(len(x) for x in body)},ensure_ascii=False))
