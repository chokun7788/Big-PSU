import ast,json
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/'REMAINING_ISSUES_R55_20261010.md'
technical=[
('P0','เกณฑ์ความครบของคำตอบ','REVIEW 47 ข้อไม่มี oracle เนื้อหาครบ บางข้ออ่านแล้วถูก แต่ยังไม่ให้คะแนน semantic correctness ได้','แยก required facts/units/conditions/source ต่อเคสและเพิ่ม omission/contradiction checks'),
('P0','เกณฑ์ 109 CHECKED ยังตรวจเฉพาะบางเงื่อนไข','contains/ชื่อเกม/mode ถูกไม่รับรองว่าทุก claim ถูก; c124 เคยผ่านทั้งที่ตอบกฎย่อยแทนภาพรวม','ตรวจ facet/coverage/ข้อยกเว้นและข้อความส่วนเกินจาก source'),
('P1','ทดสอบ regression บน r55.7 ให้ครบขอบเขตที่เลือก','156 ข้อรัน r55.6; r55.7 ตรวจ 54 requests ที่เกี่ยวข้อง ไม่ใช่ 156 ทั้งชุด','รันชุดบริการที่เกี่ยวข้องและ legacy gates ที่จำเป็นบนรุ่นเดียว ไม่รัน full20k ตามข้อจำกัดผู้ใช้'),
('P1','Oracle เก่าบางชุดยังล้าสมัย','r52 มีเกณฑ์ URL/ข้อความ membership/case ของ ID ไม่ตรง owner source ใหม่; calendar casefold แก้แล้วใน r55','ตรวจ source lineage ก่อนปรับ oracle เก่า เก็บ baseline เกณฑ์และเหตุผลไว้'),
('P1','คำถามใหม่ที่ไม่เคยใช้พัฒนา','เคสหลายรอบกลายเป็น regression แล้ว จึงใช้แทน holdout ไม่ได้','แยกชุดใหม่ที่ยังไม่ใช้ปรับ code ทั้ง TH/EN'),
('P1','Typo หลายจุด/เบิ้ล/ขาด','บางกลุ่มผ่าน แต่ยังไม่รับประกันเมื่อ subject, action และชื่อเกมเสียพร้อมกัน','ทดสอบ per-operation กับคำเสียหลายระดับ และ false corrections'),
('P1','Real-word typo และข้อความขาดมาก','คำผิดอาจกลายเป็นอีกคำจริง หรือไม่มี anchor ให้กู้','ใช้บริบท/ความกำกวม ถามยืนยันเมื่อแยกเจตนาไม่ได้ ไม่แก้ทุกคำเป็นคำที่ใกล้สุด'),
('P1','คำปฏิเสธและขอบเขตหลาย clause','semantic validator ยังเป็น pattern/presence บางส่วน ไม่ครอบคลุม not only/เงื่อนไขซ้อน','ตรวจ negation scope, exception และ target แยกแต่ละ clause'),
('P1','ชื่อเกม ภาค รุ่นย่อย และเลขโรมัน','แก้ CS2/Tekken control adapter แล้ว แต่ตัวค้นชื่อยังมีหลาย registry ในระบบ','จัด canonical IDs และ resolution contract ร่วม; ทดสอบครอบครัวเกม/ภาคใกล้กัน'),
('P1','คำถามมากกว่า 3 ส่วน/หลายงานชนิดต่างกัน','adapter ใหม่รองรับ 2–3 ส่วน ไม่รับประกันแปล+ราคา+จอง+กฎพร้อมกัน','task graph ที่เก็บทุกส่วนและแสดงสถานะส่วนที่ตอบได้/ขาด/ล้มเหลว'),
('P1','เลือกหลายเป้าหมายและทุกมิติ','ทั้งหมดอาจหมายถึงทุกโซน ทุกกลุ่มราคา หรือทุกหัวข้อ; แก้เคส scope ชัดแล้ว','ทดสอบ short selection หลายเกม/บริการ พร้อมราคา เวลา และกลุ่มที่ต่างกัน'),
('P1','บทสนทนายาวและการแก้เงื่อนไขกลางทาง','สองรอบและ resume บางชุดผ่าน ไม่ใช่ทุกลำดับ TTL/revision/topic shift','ตรวจหลาย turn เปลี่ยนบริการ/วัน/เวลา/คน/กลุ่ม แล้วกลับเรื่องเดิม'),
('P1','กฎครบทุกเกมและหลายหลักฐาน','CS2 TH/EN 56/56 ล่าสุดผ่าน; ไม่ใช่ full coverage ทุก facet/ทุกเกม/ทุกปี','ตรวจ VALORANT/RoV/Tekken และ multi-hop บน source ที่รองรับจริง'),
('P1','ภาษาอังกฤษ/ไทยปนอังกฤษและการแปล','อังกฤษชุดเดิมผ่านและ r55 เพิ่ม checks แต่ยังไม่ครอบคลุมคำแปลทุก conditional clause','ทดสอบเลข หน่วย modality negation omissions และ additions; source Thai เปลี่ยนต้องตรวจ English ใหม่'),
('P1','การรวมข้อมูลสดหลายเป้าหมายให้สอดคล้อง','fixture/parser ผ่านและผู้ใช้ยืนยันสถานะจริงเดิมแล้ว; atomic snapshot ระหว่างหลาย lookups/เปลี่ยนวันยังไม่ตรวจครบ','ตรึง timestamp/date/source ใน multi-zone tests; ไม่สรุปว่าของจริงผิด'),
('P1','WordPress ช้า/ล่ม/ข้อมูลว่าง/ผิดวัน','มี guards เดิม แต่ sustained failure และเปลี่ยนสถานะระหว่างคำขอยังไม่ตรวจครบใน r55','mock/fault-injection ทั้ง TH/EN; ทดสอบไม่ตอบว่าว่างจาก stale/unavailable'),
('P1','จำนวนคำขอ LLM พร้อมกัน','งานโมเดลยังใช้ shared limit 1; admission สำเร็จไม่ได้หมายถึง inference พร้อมกัน','วัดคิวและ latency แยก fast/LLM/live; parallel 2 ต้องทดลอง memory/quality ใน runtime แยก'),
('P1','โหลดต่อเนื่องและความเป็นธรรมของคิว','r52 มี burst ถึง 6 งานสั้น แต่ r55 ไม่มี sustained load และไม่รับรองจำนวนสูงสุด','ramp-up/soak test, mixed lengths, wait time, retries, rejection และ session ordering'),
('P1','deadline ของ job กับ backend ไม่ใช่ค่าเดียว','backend attempt ประมาณ20s แต่ queued job TTL90s ตามระบบเดิม','แสดง queue wait/processing/end-to-end แยก และออกแบบ end-to-end budget ตามบริการ'),
('P1','worker/model restart, hang และคำขอซ้ำ','unit/reopen/recycle tests มี แต่ยังไม่พิสูจน์ hard-kill ระหว่าง generation ทุกจังหวะ','fault injection ตรวจ idempotency, in-flight failure และ queued recovery บนเว็บจริง'),
('P1','Memory/cold start/โมเดลหาย','รุ่นปัจจุบัน pin Python และ warmup ผ่าน; ยังไม่พิสูจน์ทุกสภาพ RAM/เครื่องใหม่','ตรวจ interpreter/dependency/model/RAM พร้อม cold launch และ recovery'),
('P2','trace ของ timeout ยังไม่ระบุ root cause ทุกครั้ง','partial_progress เพิ่มแล้ว; stage ล่าสุดไม่พิสูจน์ว่า GPU/provider/queue เป็นสาเหตุ','เชื่อม request/job/attempt/worker/model timings; แยก provider_done จาก legacy flags'),
('P2','การวัดว่าชั้นใดช่วยจริง','เวลาลดในเคสเฉพาะ แต่ยังไม่มี ablation ที่ควบคุม workload/cache/warmup ครบ','วัด normalization/retrieval/validation/LLM/queue กับชุดเดียวและระบุ cold/warm'),
('P2','Job result/log lifecycle','chat_jobs เก็บ durable results ยังไม่พบ terminal-result cleanup ในโมดูลนี้; disk-full/restore ยังไม่ตรวจครบ','ออกแบบ retention/backup/cleanup โดยรักษา owner logs; ต้องตกลงอายุเก็บก่อนลบข้อมูลจริง'),
('P2','Refresh/Clear กับการกลับไปงานเดิม','หน้าเว็บเริ่ม anonymous session ใหม่โดยตั้งใจ ไม่ใช่ bug ความจำที่แก้ตกหล่น','ถ้าต้องการ recover job/history ให้กำหนด UX/session access ก่อน; ไม่ restore โดยเดา'),
('P2','ชุดแจกสองแบบยังเป็นรุ่นก่อน r55','local candidate พึ่ง Python/Ollama/models ในเครื่อง; แพ็กเกจ r50 เคย sync แล้วแต่ไม่ใช่ r55','build DownloadModels/WithModels รุ่นใหม่ version/hash/docs ตรงกัน'),
('P2','ใช้บนเครื่องใหม่/แตก ZIP/path ยาว','ยังไม่มี clean-machine cold-start หลักฐานของ r55 สองแบบ','ทดสอบไม่มี Python/Ollama/model, path ไทย/ช่องว่าง/ยาว และ model download failure'),
('P2','หลายโฟลเดอร์/หลายพอร์ต/ข้อมูล drift','ยังมีชุดเก่า; เปิด URL เก่าจะไม่ได้โค้ดล่าสุด และข้อมูล local admin ต่างโฟลเดอร์ไม่ sync เอง','กำหนดชุดใช้งานหลัก ตรวจ health/version/manifest/canonical/index/translation hash ทุก build'),
('P2','อัปเดต/rollback ที่รักษาข้อมูลเจ้าของ','มี snapshots และ candidates แยก ไม่ใช่ updater ที่ย้าย state/logs อย่างครบวงจร','ทำ migration/rollback rehearsal ก่อนแจกชุดอัปเดต'),
('P2','Git metadata ใช้งานไม่ได้','fatal ชี้ path Learn-LLM; มี diff จาก snapshot แทน ไม่ทราบว่า working tree clean','ตรวจ worktree linkage และซ่อมอย่างรักษา uncommitted files หลังสำรอง'),
('P2','local source links และ provenance ใน UI','local:// ไม่ใช่หน้าอ่านต้นฉบับสาธารณะ; translation/copy metadata บางส่วนยังไม่แสดงแยกใน UX','source viewer เฉพาะข้อมูลเผยแพร่ และ provenance แยกจาก answer'),
('P2','ช่องทางเพิ่ม/ทบทวนข้อมูลสำหรับเจ้าของ','มี formats/approval workflow แต่ยังไม่ใช่หน้า Local ที่เจ้าของจัดการทุกหมวดได้','ทำ UI review/publish พร้อม source hash/version และ regenerate projections/index'),
('ภายหลัง','โหมดให้บริการต่อเนื่อง','WordPress ไม่ต้องเปิด Dashboard เพื่อให้ chat ดึงแล้ว แต่ chatbot server/เครื่องยังต้องเปิด','กำหนดเครื่องให้บริการและการเริ่ม background/monitor เมื่อเลือกวิธีใช้งาน'),
('นอก priority ร้านเกม','งานยาว/บทความ500คำ','r53 ยังมี timeout/coverage reject; ภาษาไทยยังไม่ยืนยัน word count ทุกกรณี','long-job/progressive delivery และ Thai tokenizer เฉพาะหากจะรองรับงานนี้'),
('นอก priority ร้านเกม','ความรู้ทั่วไปและ translation แบบซับซ้อน','validators มีขอบเขตและบางภาษาไม่ลื่น ไม่ใช่ chatbot general-purpose ที่รับรองครบ','จำกัด supported scope; source-backed claims และ compositional translation tests'),
]
extra=[
('ราคา PS5/Switch/Cockpit/VR ปัจจุบัน','ตารางเดิมหมดอายุ31/03/2026 ยังใช้ราคาเดิมหรือไม่ เริ่ม/สิ้นสุดวันไหน?'),
('เปลี่ยนวันหลังจ่าย vs เลื่อนแทนคืนเงิน','สองกรณีข้อ45/46 ต่างกันอย่างไร ติดต่อช่องทางใดและมีกำหนดเวลาอะไร?'),
('เงินสด','รับเงินสดไหม และรายการจองที่ยังไม่โอนต้องทำอย่างไร?'),
('ค่าจอดรถ','ฟรีหรือมีค่าบริการ แยกประเภท/เจ้าของพื้นที่ไหม?'),
('ค่าเข้าดูเพื่อน','ต้องจ่ายหรือฟรี มีข้อจำกัดจำนวนคน/พื้นที่ไหม?'),
('มาก่อนเวลาจอง','ใช้ที่นั่งโซนกลางรอได้หรือมีจุดรอเฉพาะ? มีที่นั่งพักไม่ได้ยืนยันขั้นตอนรอก่อนจองโดยอัตโนมัติ'),
('เช่าเหมา','ครึ่งวัน/เต็มวันเป็นกี่ชั่วโมง ช่วงเวลาใด วิธีจอง/จ่ายและ validity ราคาเป็นอย่างไร?'),
('จองล่วงหน้า/หลายเครื่อง','จองล่วงหน้ากี่วัน และหนึ่งรายการเลือกเครื่องพร้อมกันกี่เครื่อง? 3 sessions ใช้แทนสองหน่วยนี้ไม่ได้'),
('Tekken pause','เลือกข้อความข้อห้าม/ข้อยกเว้นและบทลงโทษฉบับใดเมื่อ source ขัดกัน?'),
('RoV ข้อ6.1.5–6.1.5.1','ประโยคท้ายฉบับเต็มคืออะไร ต้องมีเอกสารต้นฉบับเพื่อเติม ไม่เขียนเอง'),
('กติกา/อุปกรณ์ปัจจุบัน','rulebook ใดใช้ในรายการถัดไป และปุ่ม/รุ่น/setting ที่ติดตั้งจริงตรงแหล่งรองไหม?'),
('อาหารและสิทธิ์ตามกิจกรรม','ข้อยกเว้นเรื่องนำอาหารเข้ากับรับประทาน และบริการทั่วไปกับการแข่งขันยังต้องมี clause ตรง; ไม่ถามซ้ำ public access/ID ที่ผู้ใช้ยืนยันแล้ว'),
('ชื่อภาษาอังกฤษทางการ','ชื่อบุคคล/กิจกรรมที่ไม่มีชื่ออังกฤษยืนยัน ให้คงชื่อเดิม ไม่แต่ง romanization เป็นชื่อทางการ'),
('อายุ/ค่าสมัครแข่ง','ข้อกำหนดแต่ละรายการแยกจากอายุใช้บริการทั่วไป ต้องมี source ของรายการนั้น'),
]
pending=[]
for n in ast.walk(ast.parse((ROOT/'app/pipeline/user_service_facts.py').read_text(encoding='utf-8'))):
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='pending_conditions' for t in n.targets):pending=ast.literal_eval(n.value)
gaps=[json.loads(l) for l in (ROOT/'data/competition_rules/source_coverage_manifest.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
gaps=[x for x in gaps if 'unsupported' in x.get('status','')]
old=json.loads((BASE/'r41_task_memory_20261006_142223_26da94/BACKLOG_STATUS_R41.json').read_text(encoding='utf-8'))
lines=['# ประเด็นค้างทั้งหมดที่พบหลักฐาน · หลัง r55.7 · 10 ตุลาคม 2026','',
'นี่เป็น inventory จาก report r42/r49/r50/r52/r53/r55 และโค้ดปัจจุบัน ไม่ได้รันทดสอบใหม่ในรอบจัดรายการนี้ ไม่มีการเปลี่ยน code หรือ owner data', '',
'**ไม่ใช่ทุกแถวเป็นบั๊กที่ยังเกิด:** แยกข้อจำกัดที่เห็นในโค้ด, สิ่งที่ยังตรวจไม่ครบ, ข้อมูลรอยืนยัน และฟังก์ชันเสริม แบบทดสอบ r55 ที่เลือกไม่มี failed checks ตามเกณฑ์นั้น แต่ไม่ใช่ความถูกต้องทุกคำถาม', '',
'## A. งานเทคนิค/การตรวจที่ทำต่อเองได้','', '| ID | ลำดับ | ประเด็น | สถานะ/หลักฐาน | สิ่งที่ต้องทำ |','|---|---|---|---|---|']
for i,(priority,title,status,action) in enumerate(technical,1):lines.append(f'| T{i:02} | {priority} | {title} | {status} | {action} |')
lines+=['','## B. ข้อมูลบริการที่ runtime ระบุว่ายังไม่ยืนยัน 26 เรื่อง','',
'แถวเหล่านี้เป็นข้อมูลขาดจริงใน handler ไม่ใช่ 26 คำตอบผิด เราทำ guard/fixture/คำถามยืนยันได้เอง แต่กำหนดนโยบายแทนเจ้าของไม่ได้', '', '| ID | Field | สิ่งที่ยังไม่ทราบ |','|---|---|---|']
for i,r in enumerate(pending,1):lines.append(f'| O{i:02} | {r[0]} | {r[3]} |')
lines+=['','## C. ข้อมูล/ขอบเขตอื่นที่ต้องมีหลักฐานเพิ่ม','', '| ID | เรื่อง | คำถามเจาะจง/สิ่งที่ต้องได้ |','|---|---|---|']
for i,(t,q) in enumerate(extra,1):lines.append(f'| D{i:02} | {t} | {q} |')
lines+=['','## D. Competition source gaps ที่ manifest ปัจจุบันระบุ','',
'แสดงตาม imported source ไม่ใช่การยืนยันว่าเกมจริงไม่มีกฎเรื่องนั้น บางหมวดซ้ำกับรายการด้านบน ต้องได้ clause ของรายการแข่งขันก่อนตอบ', '', '| เกม | Facet | เหตุผลที่ยังตอบยืนยันไม่ได้ |','|---|---|---|']
for x in gaps:lines.append(f"| {x['game_id']} | {x['facet']} | {x['reason']} |")
lines+=['','## E. เมื่อเลือกเปิดให้เครื่องอื่น/คนภายนอกใช้','',
'เป็นเงื่อนไขของการ deploy ใหม่ ไม่ใช่ข้อผิดของ localhost ที่กำลังใช้: ต้องกำหนด session/access ของผู้ดูแลและ log, TLS/network exposure, retention/backup/consent, rate limits และ capacity ของบริการจริงก่อนเปิดออกเครือข่าย ไม่มีการเปิด public ในรอบนี้', '',
'## F. งานเดิมที่ไม่ควรนับว่าเป็นบั๊กค้างเหมือนเดิม','',
'- สถานะจริง: ผู้ใช้แจ้งว่าตรวจแล้วถูกต้อง; fixture ใหม่ผ่าน แยกจาก fault/load ที่ยังไม่ตรวจครบ ไม่ขอให้เจ้าของตรวจเรื่องเดิมซ้ำโดยไม่มีเหตุ',
'- English: ผู้ใช้แจ้งชุดเดิมผ่าน; คำใหม่/conditional translation ยังต้อง regression ไม่เปลี่ยนผ่านเดิมเป็นตก',
'- ราคา→PC/ทั้งหมด, PC2 สืบทอดเวลา, เกม+ราคา, typo เลขเวลาVR, continuation CS2, ROV ล่ะ, CS2/Tekken controls และ timeout trace: แก้และผ่านเคสที่เกี่ยวข้องแล้ว; ไม่ลงรายการเป็นบั๊กที่ยังเกิด',
'- refresh เริ่มแชทใหม่: พฤติกรรมตั้งใจ ต้องแยกจาก server persistence ที่เพิ่มแล้วใน r50',
'- งาน full20k: ไม่รันตามคำสั่งผู้ใช้ ไม่ถือเป็น gate ที่ต้องเปิดเพื่อปิดงานนี้', '',
'## G. ครบ66หัวข้อจากทะเบียนเดิม เพื่อไม่ทำรายการหาย','',
'ตารางนี้เก็บหัวข้อย้อนหลัง ไม่ใช่66บั๊กปัจจุบัน และไม่รับรองการปิดทุกหัวข้อ; สถานะรายเคสต้องใช้หลักฐานรุ่นใหม่ด้านบน บางข้อแก้แล้วหรือเปลี่ยนเป็นงานตรวจต่อ ไม่ใช้ not_reassessed ของ r41 ตัดสินว่า r55 ยังผิด', '', '| ID เดิม | หัวข้อย้อนหลัง |','|---|---|']
for x in old:lines.append(f"| {x['id']} | {x['title']} |")
lines+=['','## H. ลำดับแนะนำ','',
'1. ตรวจเนื้อหาและ required facts ของ REVIEW47 และยกระดับ CHECKED ที่ตรวจเพียงบางเงื่อนไข',
'2. ทำ holdout typo/negation/หลาย clause/บทสนทนายาว และกฎหลายเกมจาก source ที่มี',
'3. ตรวจ regression รุ่นเดียว แล้ว load/recovery ของรุ่นล่าสุด แยกคำขอสั้นกับ LLM และ WordPress',
'4. sync portable bundles + clean-machine tests และ version/update/rollback',
'5. ปิด owner data gaps ตามราคาปัจจุบัน ข้อยกเว้นจอง และนโยบายใช้บริการก่อน ข้อมูลที่ยังไม่ได้ตอบคง unknown', '',
'## แหล่งหลักฐาน','',
'- r55_service_fixes_20261010_030151/RESULTS_ANALYSIS_TH.md, FLOW_FINAL.md, SUMMARY.json, FINAL_REVIEW.md',
'- r53_semantic_research_20261009_222545/RESULTS_ANALYSIS.md',
'- r52_research_flow_20261009_191123/RESULTS_ANALYSIS.md',
'- r50_flow_load_20261009_66d96bb7/REPORT_FINAL_R50.md',
'- r42_domain_resume_20261006_152553_b21f30/REMAINING_ISSUES_R42_TH.md',
'- ROOT/app/pipeline/user_service_facts.py (pending_conditions 26), ROOT/data/competition_rules/source_coverage_manifest.jsonl (unsupported9), ROOT/web_chat/app.js, ROOT/app/web_api/chat_jobs.py', '',
'บันทึก: รายการ T มีความเกี่ยวเนื่องกัน D/B/competition gaps มีหัวข้อซ้ำกัน จึงไม่บวกเป็นจำนวนบั๊กหรือจำนวนคำถามที่เจ้าของต้องตอบทั้งหมด']
with OUT.open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(OUT);print('technical',len(technical),'pending_service_fields',len(pending),'extra_evidence',len(extra),'competition_gaps',len(gaps),'historic_topics',len(old))
