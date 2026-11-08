"""Generate planning documents from retained evidence; no chatbot execution or data writes."""
from pathlib import Path
import json, hashlib

B=Path(__file__).resolve().parent.parent
O=Path(__file__).resolve().parent
S=B/'r78_web_session_check_20261016/system'
R=B/'r90_full_flow_analysis_20261018'
problems=json.loads((R/'PROBLEM_CATALOG_REVIEWED.json').read_text('utf-8'))
catalog=json.loads((S/'app/knowledge/common/catalog.json').read_text('utf-8'))

def link(label,p): return f'[{label}](<{p.as_posix()}>)'
def save(name,txt):
    with (O/name).open('x',encoding='utf-8',newline='\n') as f:f.write(txt)

# Phase, dependency / concrete change, main failure to prevent.
repairs={
'P01':('A→B','ทำ inventory ของ early returns และ legacy handlers; แต่ละ handler ระบุ task contract แล้วแยก interpreter ออกจาก source loader ก่อนต่อเข้า common dispatcher','การเรียก legacy answer ตรงทำให้ข้อมูลเก่าทับสิ่งที่เจ้าของแก้'),
'P02':('B','รวม recovery เป็น candidate generator เดียวสำหรับชื่อและ task cue แยกกัน พร้อม raw spans/protected tokens; ใช้กับ typed และ LLM paths','fuzzy correction เปลี่ยน valid word เช่น pay เป็น play หรือ PC11 เป็น PC1'),
'P03':('B→C','แยก entity_resolution_result จาก task_resolution_result; การพบ entity ห้ามตั้ง operation/default fields โดยไม่มี task support','เลือกเมนู field หรือราคาทั้งที่ถามวิธีเล่น'),
'P04':('A→B','สำรวจ regex/priority เดิมทีละ capability; แปลงผลเป็น TaskPlan และให้ alias ของ owner เป็น literal entity name ต่อไป','เจ้าของต้องเขียน regex หรือ alias รายคำถามเพื่อเพิ่ม record'),
'P05':('B→I','ทำ candidate-stage trace รวม source ที่ควรเจอแต่ไม่ผ่าน kind/topic/recall gate; ออกแบบค้นชื่อ+topic+semantic proposals ตาม task','เพิ่ม top-k จน noise สูง หรือส่งข้อมูลทั้งหมดให้ LLM โดยไม่ล็อกขอบเขต'),
'P06':('B→C','แยก guard เป็น shape, task binding, qualifier preservation และ evidence checks; รองรับ whole-task contracts ก่อน; semantic proposals ที่กว้างกว่านั้นต้องมี acceptance policy แยก','ปิด guard ทั้งหมด หรือใช้ regex เดิมเพียงตัวเดียวตัดสิน LLM paraphrase'),
'P07':('C','กำหนด primary/optional/forbidden fields ต่อ task: game overview=summary/genre, how-to=how_to_play, FAQ content=answer; โมเดลเสนอเฉพาะ task-compatible fields','profile broad เกินไปจนตอบ publisher/edition/ชื่อคำถามแทนสาระ'),
'P08':('B→E','ทำ Need ledger และ dependency graph; คืนผลต่อ clause; รวมเฉพาะ independent answered needs และอธิบาย unresolved needs','partial answer ถูกเรียกว่าครบ หรือ dependent calculation ถูกตอบทั้งที่ input ขาด'),
'P09':('C→H','ระบุ root kind/output granularity ใน EvidencePlan; เชื่อม resource→equipment, game→service→resource→zone ด้วย explicit refs; audit inferred joins','เลือก relation ถูกแต่แสดงระดับผิด หรือ deduplicate จนทำเครื่องจริงหาย'),
'P10':('D','แยก duration role ออกจาก package label, audience scope, player quantity และ billing unit; ตรวจ validity ก่อน calculation','VR30 ในชื่อกับเล่น 3 ชั่วโมงถูกจับเป็นเลขเดียวกัน หรือเติม audience โดยเดา'),
'P11':('D→H','ให้ rental task ใช้ dynamic current package catalog; terms/duration/validity แยก readiness ต่อ need; ไม่คำนวณแพ็กเกจ custom ที่ source ไม่อนุญาต','ตอบแพ็กเกจ 5 ชั่วโมงจากราคาเต็มวันหรือหัก VR ออกเอง'),
'P12':('C','ย้าย task resolution ก่อน game→service projection และให้ overview/how-to ใช้ทุก game ID จาก snapshot; จำกัด required fields ตาม task','เพิ่มเฉพาะชื่อ Zelda หรือบังคับต้องมีวิธีเล่นก่อนตอบแนวเกมได้'),
'P13':('E','กำหนด control action vocabulary, platform/preset/mode resolution, requested/all coverage และ source verification flags','มีคำว่า jump ในคำตอบแต่เป็นปุ่มคนละแพลตฟอร์มหรือ source ยังไม่รับรอง'),
'P14':('E','จัด ordered rule clauses, dependencies, exceptions และ per-proposition obligations; all/overview/detail แยก renderer','summary ซ่อนข้อยกเว้น หรือเอากฎปีอื่นมาเติมส่วนที่ขาด'),
'P15':('F→H','แยก semantic field open/bookable/maintenance พร้อมนำ user confirmation เดิมไปผูก provenance ตามขอบเขต; ส่ง conflict เฉพาะ need ที่ยังคลุมเครือ','ตีความจองไม่ได้ว่าเข้าอาคารไม่ได้ หรือถามผู้ใช้ยืนยันเที่ยงซ้ำ'),
'P16':('F','ทำ time context เดียวและ calendar precedence ต่อ zone/date พร้อม intervals ชัด; ordinary weekday FAQ ไม่ override closure','วันนี้อ้างวันของ host แทนเวลาไทย หรือปิดโซนเดียวแล้วตอบปิดทุกโซน'),
'P17':('F→I','แยก controlled unavailable fixture กับ live provider ที่ผู้ใช้ยืนยันแล้วในรายงาน; runtime ให้ unknown/unavailable distinct','ไปแก้ WordPress จากความล้มเหลวใน mock หรือ API200 ถูกนับเป็น free-correct'),
'P18':('B→C→G','ทำ pending need/selection state ที่มี scope และ delivered turn; short replies สร้าง TaskPlan แบบเดียวกับ full question แล้วอ่าน revision ใหม่','สรุปว่า history หายทั้งที่ guard ปฏิเสธ หรือ carry stale facts'),
'P19':('B→E','เก็บ action/object/ownership/context/polarity/exception เป็น typed constraints และตรวจ source applicability ก่อนตอบ','คำตอบใกล้เคียงด้านการชำระเงินถูกใช้กับอีกนโยบายหนึ่ง'),
'P20':('H','ตรวจ localized fields จริงทีละ field; เติมเฉพาะที่มีต้นฉบับ; แยก proper names/prose; translation revision/hash ตามต้นฉบับ','แก้ภาษาเพื่อผ่าน literal แต่เปลี่ยนตัวเลข/negation หรือประกาศ owner-reviewed เอง'),
'P21':('C→G','task renderer แยกจาก schema form labels; debug/source pointers อยู่ trace ส่วนผู้ใช้เห็นคำตอบตาม need และชื่อแหล่งอ่านได้','ผู้ใช้ถามเปิดไหมแต่เห็น weekday/open_periods/unknown ดิบทั้ง record'),
'P22':('B→I','สร้าง per-need statuses/coverage และแยก evidence-valid จาก task-correct; ยกเลิกการใช้ fixed confidence เป็นคะแนนความถูกต้อง','safe clarification schema-valid ถูกนับเหมือนตอบครบ'),
'P23':('I เริ่ม trace ตั้งแต่ A','บันทึก attempt/connect/body/parse/schema/semantic/final stages; timeout อยู่ phase ไหนต้องเห็นจาก trace ไม่อาศัย HTTP status อย่างเดียว','เพิ่ม alias เพื่อแก้ transport error หรืออ้าง model success จาก headers'),
'P24':('A','ตรวจ dependency ของ helper ที่นำจาก legacy; ไม่ย้าย retrieve_curated ทั้งก้อน; บันทึก bug scope เดิมไว้ต่างหาก','copy code เดิมทั้ง subtree แล้วพา NameError กลับเข้าระบบใหม่'),
'P25':('D→H→I','ทำ outcome not_current พร้อม source date และ data request ที่เฉพาะเจาะจง; evaluator แยก historical/current','ลบ end date หรือเลื่อน clock ให้เกณฑ์เก่าผ่าน'),
'P26':('G→H','SnapshotProvider ต้องระบุ publication mode; approval ผูก revision/hash; form แสดง draft/published ให้ตรง runtime','preview ผ่านแล้ว agent เปลี่ยน approval หรือสลับใช้ draft ใน production'),
'P27':('B→H','Task registry ต่อชนิดข้อมูล + per-task readiness + automatically rebuilt name/text/relation indexes; new kind ต้องมี versioned contract','schema รับ record ใหม่แต่ renderer/dispatcher ไม่มีทางอ่าน หรือทำ per-ID aliases'),
'P28':('I','evaluator adapter แปลง outcomes/source lineage เป็น contract กลาง พร้อมเก็บ strict legacy score เดิมในรายงานต่างหาก','เปลี่ยนเกณฑ์แล้วประกาศคะแนนดีขึ้นเหมือนใช้เกณฑ์เดิม'),
'P29':('I','ใช้ needs/required propositions/forbidden claims/numbers/qualifiers/citations; semantic judge เป็นหลักฐานเสริมพร้อม uncertainty','LLM judge ให้ผ่านเพราะคำตอบฟังดี หรือ literal keywords ให้ผ่านผิด task'),
'P30':('I','ออกแบบ task×language×style×context×data-status matrix และ held-out records/wording; targeted ไม่แทน full','เลือกเฉพาะโจทย์ที่เพิ่งแก้แล้วประกาศ production ready'),
'P31':('A→I','ใช้ correlation IDs ต่อ request/task/model call/source; เก็บ selected/rejected plans, reason codes, phase enter/exit และ outcome','นับ audit events เป็น unique requests หรือไม่มี final trace แล้วเดาสาเหตุ'),
'P32':('B→I','ลด model calls ที่ไม่จำเป็นด้วย typed tasks และ cache plans ตาม schema/version; จัด global budget/queue deadline; วัดหลัง correctness นิ่ง','เพิ่ม threads ไม่จำกัดหรือ cache คำตอบราคานานข้าม release'),
'P33':('H','สร้าง task-level missing-fact map; optional unknown ไม่บล็อกทุกงาน; confirmation เดิมต้องมี provenance','บังคับเจ้าของกรอกทุก field หรือเดาเพื่อให้ JSON ดูครบ'),
'P34':('A→I','บันทึก corpus/checker/build/data/reference-clock/LLM config/booking fixture ในทุก comparison; รายงานสาเหตุได้เท่าที่ trace รองรับ','อ้าง causal effect ของ schema จาก archives ที่ตัวแปรอื่นต่างกัน'),
'P35':('I หลัง runtime พร้อม','ทำ manifest ของ helpers/dependencies/config/data/model options; build สอง package ตาม requirement เดิมภายหลัง','R78 แก้แล้วอ้างว่า portable และเครื่องอื่นอัปเดตแล้วด้วย'),
'P36':('B','แยก detection/recovery/task-selection/factual-answer outcomes; ไม่ให้ warning ตัวเบิ้ลแทนการพิสูจน์ว่าฟื้นความหมายถูก','ตัวอักษรถูกลบแบบ global ทำ edition/จำนวน/ชื่อจริงเสีย'),
'P37':('G','owner preview กับ chat เรียก dispatcher contract เดียวกันโดยเปลี่ยน snapshot provider; มี draft capability limits ที่บอกชัด','preview เรียก CommonAnswerer ตรงแล้วอ้างว่า follow-up/live/outer validation เหมือนเว็บ')
}

p=['# วิเคราะห์ปัญหาและแผนแก้รายข้อ P01–P37','',
'วันที่ 18 ตุลาคม 2026 — เป็นแผน ยังไม่ใช่รายการแก้เสร็จและไม่รันเทสใหม่ในรอบนี้','',
'อ่านคู่กับ '+link('Flow หลัก',O/'01_PROPOSED_COMMON_FLOW_TH.md')+'; หลักฐานต้นทางคือ '+link('R90 problem catalog',R/'PROBLEM_CATALOG_REVIEWED.json')+' และ '+link('R90 casebook',R/'05_CASEBOOK_TH.md')+'.','',
'## วิธีอ่านหลักฐาน','',
'C ในบันทึกเดิมหมายถึงมีหลักฐานจาก code/log/ผลที่บันทึก; R หมายถึงความเสี่ยงหรือขอบเขตที่ยังต้องพิสูจน์ ไม่ใช่ทุกข้อเป็น failure ที่นับแล้ว แต่ละ count ด้านล่างใช้หน่วยตามต้นทาง ห้ามบวก audit events/grades/requests/fields เป็นจำนวนคำถามผิดทั้งหมด','',
'## ลำดับการแก้','',
'| ลำดับ | ปัญหาที่เกี่ยว | เหตุผล |','|---|---|---|',
'| 1 | P01–P07, P12, P18, P36 | shared interpretation เป็นฐานให้หลายหมวดกลับมาตอบได้ |',
'| 2 | P08–P11, P14, P19, P22 | ความครบของคำตอบ ราคา เงื่อนไขและกติกามีผลต่อการใช้งานจริง |',
'| 3 | P13, P15–P16, P20–P21, P27, P33 | projection/time/language และ readiness รายงาน |',
'| 4 | P26, P37 และ P27 | owner workflow และ published path ต้องใช้ semantics เดียว |',
'| ประกอบทุกช่วง | P23–P25, P28–P32, P34–P35, P17 | แยก measurement/runtime/data risks และเตรียมส่งมอบ |','',
'ลำดับนี้ไม่หมายถึงเลื่อนงานป้องกันข้อเท็จจริงผิดไปทีหลัง: validity, qualifier และ source-authority gates ต้องคงอยู่ตั้งแต่เริ่ม ไม่มีการผ่อน guard ระหว่างรอพัฒนา','']
for x in problems:
 phase,action,risk=repairs[x['id']]
 p += [f"## {x['id']} — {x['title']}",'',
 f"**ตำแหน่ง:** {x['stage']}  ",f"**หลักฐาน/ข้อจำกัด:** {x['status']}  ",f"**ตัวเลขที่รายงานไว้:** {x['count']}",'',
 '### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด','',x['why'],'',
 '### หลักฐานตัวอย่างจากผลที่เก็บไว้','',x['evidence'],'',
 '### พฤติกรรมที่ควรได้','',x['expected_behavior'],'',
 '### แผนแก้ที่เจาะจง','',f'ช่วงพัฒนา: **{phase}**','',action,'',
 'กรอบวิธีแก้จากการวิเคราะห์เดิม: '+x['solution'],'',
 '### ข้อผิดพลาดใหม่ที่ต้องกัน','',risk,'',
 '### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้','',x['verification'],'',
 '### ทำเองได้แค่ไหน','',x['human'],'',
 '**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว','']
 if x.get('source_refs'):
  p+=['### ไฟล์ที่เกี่ยวข้อง','']
  for ref in x['source_refs']:
   root=B/('r64_full_comparison_20261013/system' if ref[0]=='legacy' else 'r88_full_common_llm_20261017/system')
   p+=['- '+link(ref[0]+' / '+ref[1],root/ref[1])+(' — '+ref[2] if len(ref)>2 else '')]
  p+=['']
save('02_PROBLEM_TO_REPAIR_PLAN_TH.md','\n'.join(p)+'\n')

tasks={
'center':('ข้อมูลศูนย์/เจ้าของ/ที่อยู่/แผนที่','overview ใช้ description/operator; directions ต้อง address/building/floor/map ตามสิ่งที่ถาม','ไม่ต้องบังคับมีทุกช่องเพื่อบอกชื่อศูนย์ แต่ห้ามแต่งตำแหน่งที่ไม่ได้กรอก'),
'contact':('ติดต่อเรื่องใด/ทางไหน/เมื่อใด','purpose + channel/value; office_hours เมื่อถามช่วงตอบ','เก็บเป็นช่องติดต่อสาธารณะ ไม่ดึง private contact มาแทน'),
'facility':('ที่จอดรถ/ที่พัก/สิ่งอำนวยความสะดวก','name/location; usage_conditions/accessibility ตาม need','การมีที่จอดรถไม่ยืนยันค่าจอดหรือ accessibility ถ้าไม่ได้ระบุ'),
'zone':('หมวดพื้นที่/รายการในโซน/ตำแหน่ง','name/description/location และ reverse refs จาก resource/rental','room_seats ไม่ใช่จำนวนผู้เล่นพร้อมกัน'),
'equipment_model':('รุ่น/สเปก/อุปกรณ์ที่ใช้','name/device_type/specifications/usage + resource references','อุปกรณ์ส่วนตัวกับอุปกรณ์ศูนย์เป็นคนละ policy'),
'resource':('เครื่องรายตัว/จำนวนเครื่อง/ความสัมพันธ์','zone_id + equipment_model_ids + operational_status + physical_pool_key','operational_status ไม่ใช่ live booking occupancy'),
'service':('บริการ/รอบเล่น/ความจุ/ขอบเขตจอง','resource_ids/platform/session_minutes/occupancy_minutes; capacity ตามคำถาม','เวลาเล่นกับเวลาที่กินช่องจองไม่ใช่ค่าเดียวกันเสมอ'),
'game':('ภาพรวม/แนว/วิธีเล่น/คำบรรยาย','summary/genre สำหรับ overview; how_to_play สำหรับวิธีเล่น; edition เมื่อแยกรุ่น','supported_platforms ไม่ยืนยันว่าศูนย์มีเกม; ไม่สร้าง task profile รายชื่อเกม'),
'game_service':('เกมอยู่บริการใด/มีติดตั้งที่เครื่องไหน','game_id/service_id/offered; installed_resource_ids เมื่อถามการติดตั้ง','offered=true ไม่ยืนยันว่าทุกเครื่องว่างหรือติดตั้งล่าสุด'),
'game_mode':('เล่นกี่คน/โหมดไหน/ออนไลน์ไหม','mode_name/platform/players_min/players_max/network_requirement/studio_supported','schema มีหมวดนี้แต่ R88 inventory ไม่มี records; ห้ามรับรองความพร้อมจริงจาก schema'),
'control_set':('ปุ่ม action/ปุ่มทั้งหมด/อุปกรณ์ควบคุม','game_id/platform/input_device/preset/bindings; limitations/coverage/verification','all ต้องมี cardinality และแจ้ง source partial; ปุ่มอาจยังไม่ตรวจบนอุปกรณ์จริง'),
'audience':('กลุ่มผู้ใช้/สิทธิ์/หลักฐาน','name/eligibility/required_proofs; เชื่อม rate/package','นักศึกษาทั่วไปกับ PSU ห้ามรวมกลุ่มด้วยคำว่า student อย่างเดียว'),
'rate':('ราคาต่อหน่วย/รวมเวลา/งบประมาณ','service_id/audience_id/amount_minor/currency/unit/duration/calculation_rule + validity','current price ต้องตรวจช่วงมีผล; ห้ามใช้ expired เป็นปัจจุบัน'),
'rental_package':('ราคาเหมา/ครึ่งวัน/เต็มวัน/รวมอุปกรณ์','zone_ids/audience_id/period_label/amount_minor/currency; terms/duration เมื่อถาม','label เต็มวันไม่ใช่จำนวนชั่วโมงที่อนุมานได้'),
'schedule':('วันเปิด/ช่วงเปิด/ช่วงจอง/Maintenance','timezone/zone_ids/weekday/open_periods/bookable_periods/maintenance_periods','แยก open กับ bookable; closure ที่มีผลมาก่อน weekly schedule'),
'closure':('วันปิดพิเศษ/เปลี่ยนเวลาบริการ','local_date/zone_ids/state/reason และช่วงเวลาที่ override','ถ้าถามจัดการรายการจองหลังปิดพิเศษต้องมี resolution policy ไม่เดาจาก state'),
'policy':('อนุญาตไหม/เงื่อนไข/ข้อยกเว้น/ผลตามมา','topic/subject/decision/conditions_all/details + exceptions/consequence ตาม need','ต้อง preserve action/object/context/polarity; unknown ไม่ใช่ denied'),
'procedure':('ทำอย่างไร/ต้องเตรียมอะไร/กำหนดเวลา','topic/preconditions/steps; required_documents/deadline/outcome ตาม need','ตอบตามลำดับจริง ไม่เอาขั้นตอนชำระเงินไปแทนการแก้ข้อมูลจอง'),
'competition':('รายการแข่ง/ปี/เล่ม/ขอบเขตกติกา','game_id/event_name/rulebook_release/coverage + competition_rule children','supersedes ไม่ลบการถามเล่มเก่า แต่ห้ามถือเล่มเก่าใช้กับปีใหม่โดยไม่มีหลักฐาน'),
'competition_rule':('กฎเฉพาะข้อ/ทั้งหมด/บทลงโทษ','competition_id/section_number/facet/heading/text/completeness + dependencies/order','แม้ heading ตรง ต้องรวม condition/exception/penalty ที่ผูกกัน'),
'news':('ข่าว/กิจกรรม/ลงทะเบียน/ช่วงจัด','title/body/event_start/event_end/audience/contact/URL','R88 inventory ไม่มี records หมวดนี้; ข่าวไม่ override policy ถาวรโดยอัตโนมัติ'),
'person':('บุคลากร/หน้าที่/ทีม/ติดต่อสาธารณะ','display_name/role/team/affiliation/period/public_scope','แสดงข้อมูลเฉพาะที่ public_scope อนุญาต'),
'faq':('คำตอบข้อสงสัยที่เป็นข้อความ','question/topic/query_profile ช่วยค้น; answer เป็นเนื้อหาคำตอบ; related_ids ช่วย scope','ไม่ให้ owner กรอกทุก paraphrase; FAQ ที่ขัด typed policy ต้องตรวจ authority'),
'live_binding':('ผูกบริการกับ provider สถานะสด','service_id/provider/external_resource_key/physical_pool_key/status_mapping/timezone/freshness_policy','R88 inventory ไม่มี records หมวดนี้ ไม่ได้แปลว่าไม่มี live adapter: runtime มี config ภายนอก ต้อง reconcile ตอน cutover')
}

q=['# Format กลาง: ข้อมูล 24 หมวด → งานที่แชทควรตอบได้','',
'วันที่ 18 ตุลาคม 2026 — รายชื่อ field และ publish_core ดึงจาก catalog.json ของ R78 แบบอ่านอย่างเดียว ส่วน task/readiness/UI เป็นข้อเสนอพัฒนา ไม่ใช่สิ่งที่ระบบรับรองครบแล้ว','',
link('Catalog ปัจจุบัน',S/'app/knowledge/common/catalog.json'),' ',
'## หลักในการกรอกและบอกความพร้อม','',
'- ทุก record มี stable identity, revision, lifecycle, localization, evidence และ validity ตาม envelope นอก fields; ตารางนี้แสดง fields ภายใน kind','- `publish_core` เป็นเงื่อนไขปัจจุบันของ schema ไม่ใช่ required_for_task ครบทุกชนิดคำถาม; validation จริงยังมีเงื่อนไขอื่น','- known = มีค่าที่อ้างอิงได้; unknown = ยังไม่ทราบ; conflicted = หลักฐานขัดกัน; ห้ามใช้เลข 0, false หรือ list ว่างแทน unknown','- เจ้าของเห็นชื่อหมวด/คำอธิบายภาษาไทยและเลือกรายการอ้างอิงจาก UI ระบบจัดการ record IDs ให้','- ต้องมีสามสถานะแยก: record พร้อมเผยแพร่หรือไม่, task ใดตอบได้แล้ว, ภาษาใดมีข้อมูลและ review สถานะใด','- R88 มี 602 heads ใน 21 kinds; schema มี 24 kinds อีกสาม kind คือ game_mode, news, live_binding การไม่มี records ไม่ใช่หลักฐานว่าคำตอบทุกข้อในหมวดนั้นหาย และ live runtime อาจมาจาก adapter/config','',
'## ตัวอย่างการใช้งานร่วมกัน','',
'เกมใหม่ → game + game_service + service/resource ที่มีอยู่; เพิ่ม game_mode/control_set ตามข้อมูลจริง  \nราคาใหม่ → rate เดิมหรือ versioned rate ตามช่วงมีผล + audience/service ที่ถูกต้อง  \nกฎใหม่ → competition edition + ordered competition_rule + depends_on_ids  \nเครื่องใหม่ → resource + zone/equipment_model + service + live mapping ที่ตรวจได้','']
for c in catalog:
 kind=c['kind'];t,need,caution=tasks[kind]
 q += [f'## {kind}','',f'**งานที่ต้องรองรับ:** {t}','',f'**Readiness ต่อคำถาม:** {need}','',f'**ข้อระวังเฉพาะหมวด:** {caution}','',
 '| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |','|---|---|---|---|']
 for f in c['fields']:
  meaning=str(f.get('meaning_th','')).replace('|',' / ').replace('\n',' ')
  q += [f"| `{f['key']}` | {meaning} | {'ใช่' if f.get('publish_core') else 'ไม่'} | {f.get('reference_kind') or '—'} |"]
 q+=['', '**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ','']
q+=['## ช่องว่าง schema/ข้อมูลที่ต้องสำรวจระหว่างทำ','',
'1. equipment relations บางเส้นทางอาศัย source grouping: เมื่อไม่มี explicit resource reference ต้องแยก inferred mapping ออกจาก confirmed reference','2. query_profile มีอยู่บาง kinds แต่ task registry/need ledger ร่วมยังเป็นงานออกแบบ ไม่ให้ owner ต้องสร้าง profile ทางเทคนิคเอง','3. วันที่มีผลและ future release ต้องตรวจความสามารถ store จริง; ไม่ออกแบบฟอร์มที่บอกว่าจะสลับอัตโนมัติทั้งที่ยังไม่มี scheduler','4. derived readiness/index/cache ต้องผูก schema_version และ release epoch เพื่อไม่ใช้ field contract เก่ากับข้อมูลรูปใหม่','5. หากสร้าง schema ใหม่ ต้องมี migration/version/read executor/renderer/validation มากกว่าการเพิ่มชื่อ kind ใน dropdown','']
save('03_OWNER_SCHEMA_TASK_MAP_TH.md','\n'.join(q)+'\n')

review='''# ทบทวนแผนสามรอบและข้อจำกัดก่อนเริ่มพัฒนา

วันที่ 18 ตุลาคม 2026 — เป็น document/code-evidence review ไม่ใช่การรันทดสอบแชทบอท

## รอบ 1: ตรวจเหตุที่ข้อมูลครบแต่ตอบไม่ได้

| จุดที่ทบทวน | ข้อบกพร่องของแนวคิดเริ่มต้น | สิ่งที่ปรับใน Flow |
|---|---|---|
| Early return | คิดว่ามี legacy helpers ใน repo แล้วระบบจะเรียกเอง | ทำ explicit interpreter adapters ก่อน field selection |
| Entity | พบชื่อ exact ถูกใช้เสมือนเข้าใจทั้งคำถาม | แยก entity result กับ task result |
| LLM JSON | ตรวจ schema ผ่านแล้วอาจยังเลือก field ผิด | TaskPlan/Need ledger และ task-compatible field profiles |
| Guard | ปิด guard แก้ over-rejection แต่เพิ่ม wrong-answer risk | แยก guard ชั้น task/qualifier/evidence และ acceptance ของ paraphrase |
| Data migration | นับ records แล้วสรุปความครบ | ตรวจ field/relations/conditions/authority ตาม task |
| Comparison | คิดว่าเดิมชนะทุกหมวด | รักษา competition/control และ validity ที่กลางมีข้อดี |

## รอบ 2: ตรวจความผิดใหม่ที่แผนอาจสร้าง

| Counterexample | ความเสี่ยง | การปรับ |
|---|---|---|
| how to pay / how to play | fuzzy ใกล้แต่เป็นคนละงาน | valid-word/slot protection, ambiguity, task binding |
| ไม่เอา VR / เอา VR | recovery ลบคำปฏิเสธ | protected polarity + excluded IDs |
| PC11 / PC1 | ลบตัวซ้ำผิดหมายเลขเครื่อง | numeric target invariant |
| ทั้งหมด หลังเลือกบริการราคา | ตีความ all fields ทั้งฐาน | scope quantifier ผูก pending need |
| ตอบราคา+ที่อยู่ แต่ราคา expired | เลือกตอบไม่ได้ทั้งก้อนหรือเดาราคา | per-need outcome + dependency graph |
| เกมรองรับ PS5 | ตอบว่าศูนย์มีติดตั้งทุกเครื่อง | แยก platform/offered/installed/live |
| เกมใหม่ไม่มีวิธีเล่น | บังคับทุก field จนตอบแนวเกมไม่ได้ | required_for_task แยก primary/optional |
| FAQ ใกล้เคียงแต่คนละเงื่อนไข | wrong policy แม้มี source | typed subject/action/context/qualifiers |
| all rules ยาวเกิน UI | ตัดข้อมูลแล้วบอกครบ | cardinality, source-order และแบ่งส่วนที่ระบุครบ/ค้าง |

## รอบ 3: ตรวจ owner workflow และการส่งมอบ

| จุด | ช่องว่าง | สิ่งที่เพิ่มในแผน |
|---|---|---|
| Preview vs chat | ใช้คนละ entrypoint | dispatcher contract เดียว ต่างที่ SnapshotProvider |
| Draft vs published | เห็นคำตอบแล้วคิดว่าเผยแพร่แล้ว | publication mode และ revision/hash approval ชัด |
| Price update | history/cache ใช้ค่าราคาเดิม | cache key/version invalidation และ reread evidence |
| Withdraw | pending state คืนรายการที่ถอน | revalidate IDs/authority ต่อคำขอ |
| Relations | form เติมชื่อแต่ไม่มี mapping | dropdown refs + readiness ต่อ task |
| Translation | ไทยแก้แล้วอังกฤษยังยืนยัน review เดิม | translation lineage และ stale status |
| Future date | ฟอร์มอาจสัญญาสลับข้อมูลอัตโนมัติเกิน code | ตรวจ store/scheduler capability ก่อนทำ UI promise |
| Portable | แก้ R78 แล้วคิดว่าแพ็กเกจตามทัน | build/config/dependency manifest ในขั้นส่งมอบ |
| Metrics | full score ปน protocol/transport/content | แยกตารางและรักษาเกณฑ์เก่าทั้งหมด |

## ประเด็นที่ยังต้องตัดสินทางเทคนิคระหว่าง implementation

1. Semantic acceptance ของ LLM paraphrase ที่ไม่เข้า shared grammar: schema/span check อย่างเดียวไม่พิสูจน์ความหมายทั้งหมด ต้องกำหนด task-specific checks และ calibration โดยยังรักษาการ abstain
2. Conflict resolution ของ source ที่มี authority เท่ากัน: ถ้า mapping/เอกสารอธิบายไม่ได้ให้คง conflict ไม่ใช้ timestamp ชนะทุกกรณี
3. Scheduled publication ของราคาใหม่: ตรวจว่าทำด้วย store ปัจจุบันได้อย่างไร ก่อนเลือก scheduler หรือ temporal lookup ที่เพิ่มใหม่
4. Long-answer all coverage: เลือก UI split/pagination ที่รับรองจำนวนและ scope ต่อเนื่อง ไม่ทำให้ผู้ใช้เข้าใจว่า chunk แรกคือทั้งหมด
5. Task registry versioning และแผนจาก state รุ่นเก่า: ต้องมีการ invalidate/upgrade ที่ระบุได้
6. Owner translation review กับ technical validation: เป็นคนละสิทธิ์และหลักฐาน ไม่ยกให้คะแนนเทสแทนการอนุมัติ
7. Generic FAQ/topic retrieval ที่ไม่มี entity: ต้องเพิ่ม recall โดยยังรักษา policy qualifiers และ studio scope

## ข้อที่ไม่ควรใช้เป็นเหตุหยุดงานพัฒนา

- ข้อมูลราคาปัจจุบันยังต้องยืนยัน: พัฒนา interpreter/calculator ด้วย isolated fixtures ภายหลังได้ และรักษา not_current ในข้อมูลจริง
- ไม่มีทุก field ในเกม: พัฒนา task readiness และตอบเฉพาะ known needs ได้
- เจ้าของยังไม่ได้ review English ทุกข้อความ: ปรับ translation lineage และจัดทำร่างแปลได้ โดยไม่แก้สถานะอนุมัติแทน
- ไม่ได้ทดสอบเครื่องปลายทาง: เตรียม build/dependency manifest ได้ แต่ไม่ประกาศว่าทุกเครื่องใช้ได้แล้ว

## สถานะการทำงานเมื่อรับคำสั่ง “วางแผนก่อน”

หยุดที่งานเอกสาร ไม่เริ่ม test ใหม่ ไม่ติดตั้ง candidate ไม่ restart เว็บ ไม่แก้ facts/approval ของ production เก็บ candidate/ผลก่อนคำสั่งไว้แยก การตรวจเอกสาร เช่น ลิงก์ จำนวนหมวด และ hash เป็นการตรวจ artifact ไม่ใช่ทดสอบคำตอบของแชทบอท

แผนนี้ไม่ใช่ production sign-off และไม่มีการรับรองว่า common เท่าหรือดีกว่า legacy แล้ว เป้าหมายคือมีลำดับงานและ acceptance criteria ที่นำไปทำต่อได้โดยไม่ย้อนกลับไป hard-code ข้อมูลรายรายการ
'''
save('04_PLAN_REVIEW_TH.md',review)

readme=['# แผนปรับ Flow กลางให้รักษาความสามารถเดิมและเพิ่มข้อมูลได้จริง','',
'จัดทำ 18 ตุลาคม 2026 (เวลาไทย) ตามคำขอให้วิเคราะห์และวางแผนก่อน ยังไม่เริ่มเทสเพิ่มหรือติดตั้ง candidate','',
'## เริ่มอ่าน','',
'1. '+link('Flow กลางฉบับเสนอใหม่ — หลักฐานเปรียบเทียบ, Full Flow 3 แบบ, runtime 12 ขั้น, owner workflow, ลำดับพัฒนา',O/'01_PROPOSED_COMMON_FLOW_TH.md'),
'2. '+link('วิเคราะห์และแผนแก้ครบ P01–P37 — สาเหตุ หลักฐาน พฤติกรรมที่ควรได้ ความเสี่ยง และเกณฑ์ตรวจภายหลัง',O/'02_PROBLEM_TO_REPAIR_PLAN_TH.md'),
'3. '+link('Format กลางครบ 24 หมวด — fields ปัจจุบัน งานที่ควรตอบได้ และ readiness',O/'03_OWNER_SCHEMA_TASK_MAP_TH.md'),
'4. '+link('การตรวจทานแผน 3 รอบ — ข้อบกพร่องที่พบและสิ่งที่ปรับ',O/'04_PLAN_REVIEW_TH.md'),' ',
'## ข้อสรุป','',
'ข้อมูลกลางไม่ได้แย่ลงเพราะเป็น format กลางอย่างเดียว ตัวใหม่เปลี่ยน interpreter/guards/projection พร้อมย้ายข้อมูล ทำให้ความสามารถเดิมบางส่วนไม่ถูกเรียก แผนจึงนำการตีความเดิมที่ใช้ซ้ำได้มาออก TaskPlan แล้วอ่าน facts จากข้อมูลกลางปัจจุบันผ่าน Need ledger/evidence contracts โดยไม่ fallback ราคาหรือนโยบายจากไฟล์เก่า','',
'## หลักฐานที่ใช้อ้างอิง','',
'- '+link('Flow เดิม as built',R/'01_FULL_FLOW_LEGACY_TH.md'),
'- '+link('Flow กลาง as built',R/'02_FULL_FLOW_COMMON_TH.md'),
'- '+link('ผลเปรียบเทียบเกณฑ์เดียวกัน R89',B/'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json'),
'- '+link('รายละเอียดปัญหา R90',R/'03_PROBLEM_ANALYSIS_ALL_TH.md'),
'- '+link('ตัวอย่างคำถามและ trace R90',R/'05_CASEBOOK_TH.md'),
'- '+link('Data inventory',R/'DATA_INVENTORY.json'),
'- '+link('Catalog ที่อ่านจริง',S/'app/knowledge/common/catalog.json'),
'- '+link('Engine early return',S/'app/pipeline/engine.py')+' — บรรทัด 881–885',
'- '+link('Common answer/projection',S/'app/knowledge/common/answer.py')+' — บรรทัด 315 เป็นต้นไป',
'- '+link('Owner preview/save',S/'app/knowledge/common/owner_server.py')+' — บรรทัด 17 และ 52',
'- '+link('Approve/snapshot/publish',S/'app/knowledge/common/store.py')+' — บรรทัด 132, 142 และ 167','',
'## ขอบเขต candidate ที่เก็บไว้ก่อนคำสั่งล่าสุด','',
'โฟลเดอร์ candidate/ และ verification/ เป็นงานเตรียมและหลักฐานก่อนผู้ใช้ขอให้เน้นแผน ไม่ใช่ระบบติดตั้งล่าสุดและไม่ใช่หลักฐานว่าแผนทั้งฉบับเสร็จแล้ว ไม่เปลี่ยนหรือทำผลเดิมให้หายไป รายงานฉบับนี้ใช้ผลเก่า R89/R90 เพื่อเปรียบเทียบและใช้โค้ดปัจจุบันเพื่อยืนยัน call paths','',
'ข้อเท็จจริงที่ผู้ใช้ยืนยันแล้ว เช่น สถานะสดถูกต้อง ช่วงเที่ยงไม่เปิดจอง และ VR30 กินช่องชั่วโมงเต็ม ให้รักษาตามขอบเขตนั้น ไม่ขอยืนยันซ้ำหรือขยายเป็นนโยบายอื่น','']
save('README_TH.md','\n'.join(readme)+'\n')

# Read-only preservation accounting, no test invocation.
baseline=json.loads((O/'BASELINE_MANIFEST.json').read_text('utf-8'))
changed=[rel for rel,h in baseline.items() if not (S/rel).exists() or hashlib.sha256((S/rel).read_bytes()).hexdigest()!=h]
sources=[R/'PROBLEM_CATALOG_REVIEWED.json',S/'app/knowledge/common/catalog.json',B/'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json']
save('PLAN_SOURCE_CHECK.json',json.dumps({'scope':'documentation planning only; no new chatbot tests or installation','tracked_installed_files':len(baseline),'changed_tracked_files':changed,'problem_count':len(problems),'schema_kinds':len(catalog),'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'documents_created':5,'problem_count':len(problems),'schema_kinds':len(catalog),'installed_changed':changed},ensure_ascii=False))
