"""Explain historical failures against current code; no inference or test run."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent;S=R/'r78_web_session_check_20261016/system'
cases=json.loads((B/'PAIRED_CASE_EVIDENCE.json').read_text(encoding='utf8'))
audit=json.loads((B/'CURRENT_DATA_AUDIT.json').read_text(encoding='utf8'))
install=json.loads((R/'r84_correction_scope_rental_20261017/INSTALLATION.json').read_text(encoding='utf8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert all(digest(S/name)==sha for name,sha in install['installed_files'].items()),'Installed code changed; do not mislabel the audited version'
assert digest(S/'data/knowledge/common.sqlite')==install['database_sha256']
def link(label,rel,needle=None):
 p=R/rel;n=None
 if needle:
  n=next((i for i,line in enumerate(p.read_text(encoding='utf8').splitlines(),1) if needle in line),None)
  assert n,(rel,needle)
 return '['+label+']('+p.as_posix()+(':'+str(n) if n else '')+')'
engine='r78_web_session_check_20261016/system/app/pipeline/engine.py'
server='r78_web_session_check_20261016/system/app/web_api/server.py'
common='r78_web_session_check_20261016/system/app/knowledge/common/'
lines=['# R85 วิเคราะห์ Flow เดิมกับ Format กลางจากโค้ดและผลที่บันทึกไว้','',
'## คำตอบสั้น','',
'วิเคราะห์เทียบได้ และหลักฐานชี้ว่าการเปลี่ยนครั้งนี้เปลี่ยนทั้งโครงข้อมูลและเครื่องยนต์อ่านคำถาม ไม่ได้เปลี่ยนแค่ที่เก็บข้อมูล เดิมมีตัวจัดการเฉพาะหมวดที่พัฒนาสะสมไว้ ส่วนใหม่พยายามเลือก record → field → related records → projection ผ่านตัวอ่านกลาง ความสามารถตีความ/บริบทเดิมจึงไม่ได้ตามข้อมูลมาทั้งหมด','',
'สาเหตุหลักมีทั้งข้อมูลที่เคยย้ายไม่ครบ การไม่ได้ใช้ตัวตีความเดิม การเลือก record/field ผิด การสืบความสัมพันธ์ผิดขอบเขต ความจำคนละรูปแบบ และเกณฑ์ตรวจที่ผูกกับรูปแบบเก่า ข้อมูลอยู่ในฐานจึงยังไม่พอ ต้องมีเส้นทางเลือกและอ่านตรงสิ่งที่ถามด้วย','',
'## ขอบเขตหลักฐาน ไม่เอาผลเก่ามาเรียกเป็นคะแนนปัจจุบัน','',
'- R64: เปรียบเทียบคำถามเดียวกันที่บันทึกไว้ 20,554 unique requests/55,811 grades ต่อแขน ทั้ง legacy/common และ OFF/ON เป็น snapshot ข้อมูล R63 จำนวน 582 รายการ','- R85 นี้อ่านผล R64/R65 และโค้ดที่ติดตั้งล่าสุดหลัง R84 พร้อมตรวจข้อมูลปัจจุบัน ไม่รันคำถามใหม่ ไม่เรียก LLM ไม่รัน full test และไม่เปลี่ยนโค้ด/ข้อมูลใช้งาน','- ตัวอย่าง 10 คู่ในรายงานเป็นคำถามที่ผลเก่า legacy ผ่านและ common ไม่ผ่านตาม evaluator จึงต้องวิเคราะห์ซ้ำว่าผิดเนื้อหาจริง หรือเพียง source/route/text compatibility ไม่เหมารวมว่าทั้ง 10 คู่ตอบผิดสาระ','- R84 26/26 บนเว็บจริงเป็นชุดเฉพาะจุดคนละชุดกับ R64 ไม่ใช้แทนคะแนนครบ 20,554 ข้อของระบบปัจจุบัน','',
'## 1. โค้ดยืนยันว่าทั้งสองโหมดใช้เส้นทางต่างกัน','',
'### 1.1 โหมดปัจจุบันเข้าตัวอ่านใหม่แล้ว return','',
link('engine: migrated_chat_enabled แล้ว return migrated_answer',engine,'if migrated_chat_enabled():'),
'เมื่อ profile เป็น r69-migration-preview จะเข้าฟังก์ชัน migrated_chat.answer ก่อนตัวจัดการราคาเหมาและตัวจัดการหมวดเดิมด้านล่าง ไม่มีการนำ facts เก่ามาตอบเมื่อ common miss ซึ่งช่วยแยกข้อมูลใหม่จากข้อมูลเดิม แต่การตีความเดิมที่อยู่ด้านล่างก็ไม่ได้ถูกใช้โดยอัตโนมัติ','',
'### 1.2 เว็บปิด request_plan เดิมสำหรับโหมดใหม่โดยเจตนา','',
link('server: ใช้ original question และ request_plan=None',server,"reason='migrated_common_server_history'"),
'โหมดเดิมใช้ parent_typed_request_plan และ resolved_query ที่สืบบริบทมาแล้ว ส่วนโหมดใหม่ส่งคำถามต้นฉบับกับ server history ไปให้ common_read_state ตัดสินใหม่ จึงไม่ใช่ว่าเว็บไม่ส่งประวัติทั้งหมด แต่เป็นคนละตัวตีความประวัติ ความสามารถที่ยังไม่มีใน common state จึงไม่ตามมาเพียงเพราะข้อมูล source เดิมอยู่ครบ','',
'### 1.3 R64 ยังไม่ใช่ migrated dispatcher ตัวปัจจุบัน','',
link('R64 engine: common answer แซงก่อน specialized routes','r64_full_comparison_20261013/system/app/pipeline/engine.py','if common is not None:'),
'R64 ใช้ common hook ก่อน route เดิม ถ้า common เลือกคำตอบผิดแต่ผ่าน validation และคืน result มา engine ก็ return ก่อนถึงตัวจัดการเฉพาะหมวด ส่วนปัจจุบันแยก migrated dispatcher ทั้งเส้นทางแล้ว สองรุ่นมีรายละเอียดต่างกัน ไม่เอา early return รุ่นใหม่ไปอ้างว่าเป็นโค้ดเดียวกับทุก failure ใน R64','',
'## 2. Flow เดิมทำอะไรได้มากกว่าการเปิดไฟล์หาเนื้อหา','',
'```mermaid','flowchart TD','    A[คำถามและประวัติที่ server บันทึก] --> B[แยกงาน หมวด ตัวเลือก และสิ่งที่ยังขาด]','    B --> C[ตัวตีความเฉพาะหมวดและ request plan]','    C --> D{หมวดคำถาม}','    D --> E[ราคา: บริการ กลุ่ม เวลา จำนวนคน]','    D --> F[กฎแข่ง: เกม ฉบับ หมวดข้อ เงื่อนไข]','    D --> G[เกม: คำบรรยาย โซน หรือชุดปุ่ม]','    D --> H[การจอง: วิธีทำ สถานะ หรือแก้รายการ]','    E --> I[อ่าน source แล้วสร้างคำตอบตามงาน]','    F --> I','    G --> I','    H --> I','    I --> J[เก็บ active task และ offered options]','```','',
'ตัวอย่างราคาเหมาเดิมมี plan แยก targets/groups/periods/asks, scoped_requests ต่อเงื่อนไข, exclusions และการถามต่อ ไม่ได้อาศัยว่าข้อความไหนเหมือนกันที่สุดเพียงอย่างเดียว ตัวอย่าง “PC เต็มวันภายนอก และ VR ครึ่งวันภายใน” ต้องเป็น 2 ชุดเงื่อนไข ไม่ทำทุกโซน × ทุกกลุ่ม × ทุกช่วงวัน','',
link('zone_rental: ตัวตีความและ renderer เดิม','r78_web_session_check_20261016/system/app/pipeline/zone_rental.py','def resolve_zone_rental_plan'),
link('task_memory: เก็บ task/operation/targets/options/rental_plan','r78_web_session_check_20261016/system/app/session/task_memory.py','def task_from_response'),
'',
'## 3. Flow ใหม่เพิ่มจุดที่ต้องเลือกให้ถูกหลายชั้น','',
'```mermaid','flowchart TD','    A[คำถามต้นฉบับและ common_read_state] --> B[หา entity และ record IDs]','    B --> C[เลือก operation และกลุ่มข้อมูล]','    C --> D[เลือก field ตาม schema หรือ LLM planner]','    D --> E[เดิน FK และเลือก related records]','    E --> F[จำกัด projection ตามสิ่งที่ถาม]','    F --> G[ตรวจ source validity revision และ coverage]','    G --> H[แสดงข้อมูลหรือถามยืนยัน]','    H --> I[เก็บสถานะ common ของคำตอบนี้]','```','',
'ถ้าชั้นแรกเลือก FAQ จองแทนกติกา RoV การเลือก field=answer ในชั้นถัดไปอาจถูก schema ทุกประการ แต่จะตอบผิดเรื่อง ถ้าเลือก CS2 ถูกแต่ขยายกฎลูกทั้งหมด ก็อาจตอบยาว 22,902 ตัวอักษรทั้งที่ขอข้อประท้วงเพียงข้อเดียว ถ้าเลือกเกมได้แต่เลือกเฉพาะ game_id ก็จะตอบเพียงชื่อเกม','',
'การผ่าน schema/source validation บอกว่าอ่าน field ที่อนุญาตและมีหลักฐานได้ ไม่รับประกันว่าสิ่งนั้นตรงเจตนาของผู้ใช้ คะแนน confidence ของ route เดิมและ common จึงไม่ใช่ความน่าจะเป็นความถูกต้องที่สอบเทียบแล้ว','',
'## 4. ประเภทสาเหตุ และหลักฐานที่ชี้ไปแต่ละชั้น','',
'| ประเภท | ทำไมเดิมตอบได้ | ทำไมกลางพลาด | สถานะหลัง R84 |','|---|---|---|---|',
'| ย้ายเนื้อหาไม่ถึงช่องที่ใช้ตอบ | handler เดิมอ่านไฟล์ curated/raw ตรง | ปุ่มเคยอยู่ใน limitations แต่ bindings ว่าง; บางคำบรรยายถูกตัดก่อนย้าย | R67/R68 เติมแล้วหลายส่วน ปัจจุบันมี 43 ชุดปุ่ม/448 binding rows และ 104 rule facets known |',
'| ย้ายข้อมูลแต่ไม่ได้ใช้ parser เดิม | มี resolver เฉพาะราคา/เหมา/แข่ง/ปุ่ม | ชุดใหม่ต้องตัดสิน operation/record/field ใหม่ | ยังเป็นความต่างเชิงสถาปัตยกรรม ต้องย้าย behavior ผ่าน adapter |',
'| ดึง record ผิด | route จำกัดพื้นที่ค้นตามหมวด | candidate คล้ายคำว่า “สรุป” ไปหยิบสรุปจองแทน RoV | มี typed scopes และ guard เพิ่มแล้ว แต่ไม่ได้ full rerun ปัจจุบัน |',
'| เลือก field ผิดหรือไม่ครบ | handler รู้ว่า “คืออะไร” ต้องบรรยายและวิธีเล่น | ส่งเฉพาะชื่อเกม หรือถาม field ที่ root ไม่มี | มี query contract/projection/relations เพิ่ม ต้องพิสูจน์ด้วยคู่เดิม |',
'| กฎลูกและขอบเขตย่อย | ใช้ facet + clause source | เลือกเอกสารถูกแต่รวมทุก section | reader ปัจจุบันมี rule_selection/facet/lexical sections แล้ว ไม่สรุปว่าทุกคำถามหายผิด |',
'| บริบทการถามต่อ | เก็บงาน กลุ่ม เวลา ตัวเลือก และแกนที่เลือก | state ใหม่เก็บ IDs/fields และกติกาสืบคนละชุด | R75–R84 แก้หลายทาง ผลเฉพาะจุดผ่าน ไม่ใช่ parity ทุกบทสนทนา |',
'| จำนวนหรือกลุ่มของราคา | ราคาเหมาเดิมแยก group/period เป็นข้อมูลใน plan | ภาษาอังกฤษ singular/group noun หรือ how much priority ทำ scope ผิด | R84 แก้ 3 จุดและเว็บ 6 คำถามราคาเหมาในชุด 26 ผ่าน |',
'| Unknown กับ interpretation ปะปน | domain handler รู้ว่าข้อมูลส่วนไหนมี | เลือกไม่ถูกอาจแจ้งคล้ายไม่มีข้อมูล | ต้องแยก scope_unresolved, fact_unknown, model_failure, expired ชัดเจน |',
'| LLM เป็นคอขวดเพิ่ม | คำถามที่ resolver ตรงตอบจาก source โดยตรง | คำถามตรง ๆ กลับต้องเลือก record/field ผ่านโมเดล | R83 ลด protocol/candidate; ไม่ได้พิสูจน์ความเร็วทุกเส้นทาง |',
'| ภาษาที่ใช้ตอบและ label | แม่แบบเดิมเป็นภาษาคนเฉพาะงาน | บาง field label เป็นคำสอนกรอก/ชื่อ schema และ EN เคยหาย | R67/R68 แปล/จัดช่องเพิ่ม; audit ตอนนี้ตรวจ top-level localized fields ไม่ใช่ human translation certification |',
'| เกณฑ์ตรวจ | expected ผูก route/source IDs เก่า | common ใช้ knowledge/common_read และ source IDs ใหม่ | ต้องเทียบเนื้อหาแยก compatibility และไม่เปลี่ยน expected แบบไม่มีหลักฐาน |',
'| วันที่มีผล | เดิมอาจแสดงราคาที่บันทึกพร้อมหมายเหตุหมดอายุ | common ระงับการยืนยันราคาเมื่อเลย validity | ต้องแยกความต่างตามนโยบายวันมีผลจาก retrieval bug ห้ามเติมวันมีผลเพื่อให้คะแนนผ่าน |','',
'## 5. ข้อมูลเคยย้ายไม่ครบจริง แต่ไม่ควรสรุปว่าย้ายเพิ่มอย่างเดียวจะแก้หมด','',
'R67 พบปุ่มควบคุมที่เก็บผิดรูปแบบและกู้แหล่งก่อน canonical เพิ่ม R68 พบคำบรรยาย raw ที่ยาวกว่าฉบับกลาง 23 รายการ และชื่อเรียกเกมที่ไม่ได้ตามฐานมา จึงมีความผิดพลาดของ migration จริง ไม่ใช่ข้อมูลครบทุกช่องมาตั้งแต่ต้น','',
'Audit ฐานที่ติดตั้งหลัง R84 ในรอบนี้อ่านแบบ read-only ได้:',
f"- {audit['records']} records, {len(audit['controls'])} control sets, {sum(v['binding_count'] or 0 for v in audit['controls'].values())} binding rows",
f"- competition_rule facet: {audit['rule_facets']}",
f"- {len(audit['profiles'])} records มี query_profile ที่ known จาก FAQ/policy/procedure รวม {sum(audit['kinds'].get(k,0) for k in ['faq','policy','procedure'])} records",
f"- localized field ที่มี th แต่ไม่มี en ที่ระดับ field value: {len(audit['localized_english_missing'])} ช่อง (ไม่ใช่การตรวจ recursive ทุก text leaf หรือคุณภาพการแปลโดยคน)",
'- DB SHA256: `'+audit['current_database_sha256']+'`','',
'ตัวเลขนี้ยืนยันสถานะโครงข้อมูลในขอบเขตที่ตรวจ ไม่เท่ากับ 602/602 ตอบคำถามทุกรูปแบบ และ query_profile มีเพียง 2 records ก็ไม่ได้แปลว่าอีก 192 รายการตอบไม่ได้เลย เพราะยังมี exact/typed readers แต่มันชี้ว่ากลไก task+subject ที่เพิ่มใหม่ยังไม่ได้เป็น capability ทั่วไปทุกหมวด','',
'## 6. คู่คำถามจาก log เดิมที่ชี้สาเหตุได้ชัด','']
explanations={
'rules_overview':('ผิด record/ข้ามหมวดจริง','เดิมจัดเป็นกติกา RoV และสรุป source ของการแข่งขัน ใหม่เลือก FAQ สรุปจอง แม้ validation ผ่าน เป็นปัญหาการเลือก record ไม่ใช่ RoV source ไม่มี','ปัจจุบันมี competition scope/rule_selection แล้ว ยังไม่ได้รันคู่ R64 นี้ใหม่ใน R85'),
'rules_dispute':('ขอบเขตใหญ่เกิน + source identity compatibility','เดิมเลือกข้อประท้วงตรง ๆ 236 ตัวอักษร ใหม่เลือก parent CS2 แต่คืนข้อความกฎ 22,902 ตัวอักษร เกณฑ์เก่ายังจับ ID ต่างรูปแบบด้วย จึงต้องแยกการเลือก clause/verbosity จริงออกจากชื่อ ID','ปัจจุบัน facets known104 และเลือก sections ได้ตามโค้ด ต้องตรวจ scope ด้วย clause IDs ไม่ใช้ความยาวอย่างเดียว'),
'controls':('เก็บปุ่มคนละช่อง/reader ไม่อ่านช่องเดิม','bindings ที่ reader ขอเคย unknown ทั้งที่เดิมอ่านรายการปุ่มจาก source อีกโครงสร้างได้','R67 ย้ายปุ่มเป็น bindings; ปัจจุบัน448 rows แต่ผลของคำถามนี้ใน runtime ล่าสุดยังไม่ได้รันใหม่ใน R85'),
'fee_target':('การตีความกลุ่ม/เส้นทางต้องเรียกโมเดลและ retry','เดิมอ่าน service+audience แล้วตอบแพ็กเกจตรง ใหม่ common_retry จึงไม่มีราคา การไม่ตอบเป็น execution/selection failure ไม่ได้พิสูจน์ว่าราคาไม่มี','R84 แก้กลุ่มหน่วยงานของราคาเหมา ไม่ใช่หลักฐานว่าคำถามนักศึกษา PSU รายชั่วโมงทุกข้อหายผิด'),
'fee_validity':('ไม่ควรเรียกเป็น price retrieval bug โดยอัตโนมัติ','เดิมแสดงราคาแพ็กเกจ 1,050 พร้อมเตือนวันมีผลหมดแล้ว ใหม่ไม่ยืนยันราคาเพราะ validity ทั้งสองตอบภายใต้ข้อจำกัดเวลา แต่เกณฑ์เดิมต้องมีบาท/จำนวนเงินจึงตก','ต้องกำหนดการตอบราคาประวัติเทียบราคาปัจจุบันแยกกัน ไม่ต่ออายุราคาเอง'),
'booking':('ความหมายใกล้คำว่า penalty แต่คนละสถานการณ์','ไปสายควรดู check-in/no-show ใหม่เลือกละเมิดร้ายแรง/ระงับถาวร เป็น factual relevance failure แม้ข้อความนั้นเป็น source จริง','มี typed FAQ/procedure roles เพิ่มแล้ว ไม่อ้างว่าคำถามเดิมรันทวนครั้งนี้'),
'game_description':('เลือก field ผิด/คำตอบหายสาระ','เดิมให้คำบรรยายเกม ใหม่อ่านเพียง game_id แล้วแสดงชื่อ Animal Crossing จึงไม่ตอบว่าเกมอะไร','R67/R68 คืนคำบรรยายและความสัมพันธ์ ไม่ใช้จำนวน record แทนการตรวจ answer projection'),
'equipment':('สาระใกล้เคียง แต่รูปแบบ/contract ยังต่าง','ใหม่มีชื่อรุ่น Logitech และ usage จริง พร้อม specs quantity/zone จึงไม่ควรประกาศว่าคำถามนี้ไม่รู้ข้อมูลทั้งหมด failure มี route/intent และ quality contract ปะปน ส่วนที่เห็นชัดคือ label และ None ภายใน','device_type/specs ถูกเติมภายหลัง การประเมินต้องตรวจ substantive fields แยกการแสดงผล'),
'equipment_list':('เลือกชนิด/root และเดินความสัมพันธ์ไม่ครบ','เดิมเลือกอุปกรณ์ตามโซน ใหม่ได้ zone/service IDs แต่ขอ equipment_model_ids ที่ root นั้นไม่ได้ตอบตาม fieldplan จึงคืน out-of-scope ทั้งที่ equipment source มี','ปัจจุบัน relations รองรับ service→resource→equipment และ source zone grouping ต้องตรวจผลกับขอบเขตที่ถาม'),
'schedule':('เกณฑ์คำตอบและถ้อยคำไม่ตรง ไม่ใช่พิสูจน์เวลาผิด','ทั้งสองบอกจันทร์ช่วงเช้าเป็น Maintenance ใหม่ใช้เล่นไม่ได้/ไม่ใช่ Open for Service และมีหัวข้อ regex เหตุผล missing alternatives เป็นเงื่อนไขข้อความอ่อน ไม่ควรนับเป็นเวลาเปิดผิดทันที','R80 compact day opening และ presentation ถูกแก้แล้ว ต้องแยก weekday period จากสถานะวันนี้ และตรวจ date/timezone ในชุดของมัน')}
for case in cases:
 label=case['label'];category,why,status=explanations[label];old=case['legacy_llm'];new=case['common_llm'];plan=(new['artifact'].get('query_plan') or {})
 reasons=list(dict.fromkeys(x for grade in new['grades'] for x in json.loads(grade['reasons_json'])))
 lines+=['### '+case['question'],'','ประเภท: **'+category+'**','',why,'','สถานะปัจจุบันที่พิสูจน์ได้: '+status,'',
 'Legacy mode: `'+old['mode']+'`; Common R64 mode: `'+new['mode']+'`','',
 'คำตอบเดิม:','',*['> '+s for s in old['answer'][:1400].splitlines()], '',
 'คำตอบ Format กลางใน R64'+(' (แสดงต้น 1,400 ตัวอักษรจาก '+str(new['answer_characters'])+')' if new['answer_characters']>1400 else '')+':','',*['> '+s for s in new['answer'][:1400].splitlines()], '',
 'Common plan:','```json',json.dumps({k:plan.get(k) for k in ['record_ids','requested_fields','method','operation','semantic_review_needed','semantic_plan_accepted']},ensure_ascii=False,indent=2),'```','',
 'ตัวอย่างเกณฑ์ที่ไม่ผ่าน:','',*['- '+x for x in reasons[:6]],'',
 'หลักฐานคู่: key `'+case['key']+'` ใน PAIRED_CASE_EVIDENCE.json เก็บ answer/trace/plan/grades เต็มทั้งสองข้าง; ต้น log: `'+str(new['source_file'])+':'+str(new['source_line'])+'`','']
lines+=['## 7. ตัวอย่างล่าสุดที่ยืนยันว่าข้อมูลครบก็ยังพลาดได้','',
'R84 ก่อนแก้มีราคาเหมาใน DB ครบ 24 รายการและจำนวนเงินตรง workbook แล้ว แต่ 3 คำถามยังเลือก scope ผิด:',
'- How much is half-day PS5 zone rental for an internal organization? ถูกจัดเป็น price รายชั่วโมงแทน rental','- Full-day PC zone rental for an external organization เลือกทั้ง external และ internal เพราะรูปคำ audience ไม่ตรง','- เหมาทุกโซนเต็มวันหน่วยงานภายนอก เลือกแพ็กเกจแยกทุกโซน แทน package All Zones หนึ่งชุด','',
'หลังแก้ operation priority/audience grammar/bundle scope คำถามเหล่านี้ผ่านโดย DB hash ไม่เปลี่ยน นี่เป็นหลักฐานตรงว่า reader/flow เป็นสาเหตุได้โดยไม่ต้องเพิ่มข้อมูลราคาอีก',
link('รายงานและหลักฐาน R84','r84_correction_scope_rental_20261017/REPORT_R84_TH.md'),'',
'## 8. จุดเสี่ยงที่ยังอ่านพบจาก flow ปัจจุบัน','',
'### P0 สำหรับเป้าหมาย “เพิ่มข้อมูลแล้วตอบได้” — known-unknown guard ต้องตรวจข้อมูลปัจจุบันด้วย','',
link('unconfirmed_request.topic: รายการหัวข้อที่ตอบว่ายังไม่ยืนยัน',common+'unconfirmed_request.py','def topic'),
link('answer: เรียก unconfirmed ก่อน semantic selector เมื่อไม่มี ids',common+'answer.py','# An explicit unresolved need'),
'รอบ R84 ป้องกันยอดเงินผิด/เอกสารตัวตนผิดไปเลือก FAQ สลิปหรือรายการเอกสารเช็กอินได้จริง แต่หัวข้อ unknown เหล่านี้ยังมาจาก logic ภาษาที่เขียนไว้ในโค้ด ถ้าเจ้าของเติมวิธีแก้ที่มีหลักฐานภายหลัง และถ้อยคำใหม่ยังไม่ match record ก่อน gate นี้ ระบบมีความเสี่ยงบอกว่ายังไม่ยืนยันก่อน semantic retrieval ได้อ่านข้อมูลใหม่นั้น','',
'นี่เป็น risk จากลำดับโค้ด ไม่ใช่ผลทดสอบเพิ่ม policy ใหม่ของหัวข้อนี้ในรอบ R85 ต้องแก้ให้ known/unknown มาจาก source coverage และสถานะ field ณ revision ปัจจุบัน พร้อม conflict/validity gates ใช้ grammar เพื่อระบุหัวข้อได้ แต่ไม่ใช้ grammar ตัดสินว่าข้อมูลนั้นไม่มีตลอดไป','',
'### P1 — Semantic selection ยังทำงานหลายขั้น','',
link('planner.semantic_guard: ปฏิเสธเมื่อไม่มี strong typed need',common+'planner.py','def semantic_guard'),
'ถ้อยคำที่เป็นภาษาคนแต่ไม่ตรง typed field grammar อาจเลือก entity ได้แล้ว แต่ fieldplan ไม่ถูกยอมรับ การเพิ่ม alias หรือเพิ่ม text ใน FAQ อย่างเดียวไม่แก้จุดนี้ ต้องมี request-level contract ที่แยกสิ่งที่ถามและตรวจ coverage จาก record/relations','',
'### P1 — บริบทใหม่ไม่ได้เป็นสำเนาความสามารถเก่า','',
link('common dialogue: state มี ids/fields/scope/operation/constraints',common+'dialogue.py','def state_from_answer'),
'มี common_read_state และ server history จริง จึงไม่ควรสรุปว่า “ไม่มีความจำ” แต่ยังต้องเทียบ operation scopes, offered options, exclusions และการกลับมางานเดิมกับ task_memory รุ่นเก่าเป็นราย capability','',
'### P1 — การกู้คำผิดเดิมบางส่วนอยู่หลัง migrated return','',
link('engine: intent cue preflight รุ่นเดิมอยู่ด้านล่าง return',engine,'cue_preflight, cue_recoveries'),
'ตัวอ่านกลางมี recovery ของชื่อและ schema language ของตัวเองแล้ว จึงไม่ได้ไม่มี typo support ทั้งหมด แต่เส้นทาง intent-cue repair เดิมที่อยู่ด้านล่างไม่ได้ถูกรันโดยอัตโนมัติ ต้องแยก recovery ที่แก้ภาษาทั่วไปได้จาก recovery ที่ผูกคำตอบหรือ alias เฉพาะรายการ ก่อนนำกลับมาใช้ร่วมกัน','',
'## 9. แนวทางที่ควรทำต่อจากบทเรียนของ Flow เดิม','',
'เป้าหมายคือ **รักษาความสามารถตีความที่เคยทำได้ แล้วให้อ่าน facts จาก Format กลางทุกครั้ง** ต้องแยก parser/การคำนวณ/การจัดคำตอบออกจากไฟล์ facts เก่าที่ handler เดิมผูกไว้ ไม่เปิด fallback ไปอ่านราคา/นโยบายคนละ revision แบบเงียบ ๆ','',
'### Flow เสนอ','',
'```mermaid','flowchart TD','    A[คำถามและ trusted history] --> B[กู้ภาษาที่มั่นใจ โดยเก็บต้นฉบับ]','    B --> C[แผนงานกลาง: หมวด งาน เป้าหมาย เงื่อนไข และส่วนที่ขาด]','    C --> D[ตัวตีความเฉพาะหมวดที่ปรับมาจากเดิม]','    D --> E[แปลงแผนเป็น IDs และ relations ของ Format กลาง]','    E --> F[อ่าน revision/source/validity ปัจจุบัน]','    F --> G{ครอบคลุมทุกส่วนที่ถามหรือยัง}','    G -- ครบ --> H[จัดคำตอบตามหมวด จาก facts ที่อ่านได้]','    G -- ยังขาดตัวเลือก --> I[ถามเฉพาะตัวเลือกที่ขาด]','    G -- ข้อมูลไม่มีหรือขัดกัน --> J[ตอบส่วนที่ยืนยันได้และระบุส่วนที่ขาด]','    E -- ถ้อยคำยังไม่ตรง --> K[LLM เสนอ request plan ที่จำกัด schema]','    K --> F','    H --> L[บันทึก task state ที่อ้าง revision/IDs]','    I --> L','    J --> L','```','',
'### ลำดับลงมือที่เหมาะสม','',
'1. ทำ capability matrix เดิม→กลาง: ราคา/เหมา, กฎแข่ง, ปุ่ม, รายชื่อเกม, ข้อมูลศูนย์, จอง/แก้รายการ และบทสนทนา ระบุ parser, source fields, links, rendering, pending state ของแต่ละงาน','2. ทำ common-data adapters ให้ behavior เดิมอ่าน DB กลางได้โดยตรง โดยย้ายเฉพาะ interpretation/calculation/projection และ source provenance ต้องออกจาก DB กลาง ห้ามเรียก load_zone_rental_data หรือ FAQ เก่าเป็น facts ทางลัด','3. เริ่มราคาเหมาและคำถามต่อเนื่อง เพราะมี plan เดิมที่ชัดและ source oracle 24 ช่องอยู่แล้ว จากนั้นกฎแข่ง (facet/clause) และปุ่มเกม (action/binding/summary)','4. เปลี่ยน unknown gating ให้ดู records/fields ที่มีจริง ณ revision ปัจจุบันก่อนปิด semantic lookup เพื่อให้ข้อมูลใหม่ตอบได้จริง','5. ใช้ request contract เดียวตลอด record/field/relations/projection เช่น game=CS2, operation=rules, facet=protest_dispute ไม่ปล่อยให้ field planner เปลี่ยน game/task ระหว่างทาง','6. แยก factual renderer ของหมวดจากชื่อ schema/คำสอนกรอกข้อมูล คำถามกว้างคืนครบตามขอบเขตที่ขอ คำถามเฉพาะไม่แถมทุก child','7. ทำ paired regression จาก log เดิมเฉพาะกรณี legacy ผ่านและ common พลาด ตรวจคำตอบ/เงื่อนไข/source fields ไม่บังคับชื่อ route เก่าทุกจุด และแยกกรณี expired policy ที่การไม่ยืนยันอาจถูกต้อง','8. ทดสอบข้อมูลใหม่/แก้ราคา/ถอน record ในฐานทดลองแยกด้วย parser เดียวกัน ต้องไม่แก้ router รายชื่อเกมหรือราคาเพื่อให้ผ่าน','9. เทสเฉพาะจุดก่อนเทสใหญ่ตามที่ผู้ใช้พักไว้ ไม่รัน full corpus จากการวิเคราะห์ครั้งนี้','',
'## 10. สิ่งที่ไม่ควรใช้เป็นทางแก้หลัก','',
'- เพิ่มข้อมูลซ้ำลง FAQ เพื่อเลี่ยง relation ที่ตัวอ่านยังไม่รองรับ จะทำให้แหล่งจริงและ revision ตีกัน','- คืน fallback ไปอ่านข้อความชุดเก่าเมื่อข้อมูลใหม่อ่านไม่ออก เพราะราคา/กฎที่เจ้าของแก้ใน Format กลางอาจถูกทับด้วยคำตอบเก่า','- บังคับ LLM เรียบเรียงทุกคำถามเมื่อ metadata/typed resolver ตอบได้ตรงอยู่แล้ว','- เอา HTTP 200, JSON ถูก schema, confidence .99 หรือจำนวน records เป็นหลักฐานว่าคำตอบถูก','- ขยาย/ลดเกณฑ์คะแนนตามคำตอบที่ได้ โดยไม่กลับไปตรวจ source, วันที่มีผล และขอบเขตที่ผู้ใช้ถาม','',
'## หลักฐานหลัก','',
link('R64 full comparison','r64_full_comparison_20261013/FINAL_FULL_TEST_REPORT.md'),
link('R64 paired counts','r64_full_comparison_20261013/PAIRED_COMPARISON.json'),
link('R67 migration parity','r67_migration_parity_20261015/FINAL_REPORT_R67_TH.md'),
link('R68 raw source completion','r68_source_completion_20261016/FINAL_REPORT_R68_TH.md'),
link('R73 metadata scope','r73_scope_completion_20261016/REPORT_R73_TH.md'),
link('R84 latest focused behavior','r84_correction_scope_rental_20261017/REPORT_R84_TH.md'),
'- PAIRED_CASE_EVIDENCE.json: 10 คู่พร้อม trace/plan/grades/source-file-line เต็มจาก evidence.sqlite แบบ read-only','- CURRENT_DATA_AUDIT.json: โครงข้อมูลปัจจุบันที่อ่านจริง ไม่ใช่รายงานจำนวน prepared records','',
'ข้อสรุป: การย้าย facts กับการรักษา behavior ต้องตรวจคนละบัญชี การทำ Format กลางให้ใช้งานได้ควรย้ายความสามารถของตัวตีความและตัวจัดคำตอบเดิมมาครอบการอ่านข้อมูลกลางด้วย ข้อมูลใหม่จึงได้รับประโยชน์จาก behavior เดิมโดยไม่ต้องเพิ่ม handler รายรายการ']
with (B/'LEGACY_VS_COMMON_FLOW_ANALYSIS_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
preservation={'production_code_changed':False,'production_data_changed':False,'new_chat_requests':0,'new_model_calls':0,'full_test_executed':False,
              'installed_r84_hashes_unchanged':all(digest(S/name)==sha for name,sha in install['installed_files'].items()),'database_unchanged':digest(S/'data/knowledge/common.sqlite')==install['database_sha256'],
              'sample_count':len(cases),'historical_samples_only':True,'current_runtime_accuracy_reestimated':False}
with (B/'READ_ONLY_AUDIT.json').open('x',encoding='utf8') as f:json.dump(preservation,f,ensure_ascii=False,indent=2)
print(json.dumps({'report':str(B/'LEGACY_VS_COMMON_FLOW_ANALYSIS_TH.md'),'preservation':preservation},ensure_ascii=False))
