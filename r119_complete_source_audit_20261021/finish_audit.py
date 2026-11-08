"""Publish audit reports only after final source and HTTP gates pass."""
import collections,hashlib,json,sqlite3
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system'
load=lambda n:json.loads((R/n).read_text('utf8'))
write=lambda n,x:(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
link=lambda n,label=None:f'[{label or n}](<{(R/n).as_posix()}>)'
done=load('http03/TEST_COMPLETE.json');assert done['complete'] and done['unique_request_keys']==48 and done['grades']==164 and done['model_identity_verified'] and done['source_code_inputs_unchanged']
audit=load('FULL_AUDIT_GATE.json');state=load('PRESERVED_STATE_GATE.json');contracts=load('READER_CONTRACTS.json');typed=load('TYPED_VARIANT_DECISIONS.json');ext=load('EXTERNAL_VARIANT_REVIEW.json');docx=load('PRIMARY_DOCX_AUDIT.json');rental=load('RENTAL_WORKBOOK_PRICE_AUDIT.json');aliases=load('CODE_ALIAS_MIGRATION.json')
assert audit['audit_complete'] and state['passed'] and contracts['passed']==contracts['total'] and typed['unresolved']==0 and not docx['unmatched'] and rental['passed']==24 and not ext['counts'].get('unclassified',0)
freeze=load('http03/RUN_FREEZE.json')['files'];assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in freeze.items())
analysis=load('http03/analysis/COMPARISON.json');scores=analysis['versions'];latest=scores['R119_revision03']
files=load('FILE_DISPOSITIONS.json');mapping=load('RECORD_MAPPING.json');changes=load('MIGRATED_FIELDS.json');protected=load('PROTECTED_INPUTS.json')
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items())
byfield=collections.defaultdict(set)
for c in changes:byfield[c['field']].add(c['record_id'])
db=sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in db.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
base=load('NATIVE_BEFORE.json')['records'];changed_roots=[rid for rid,r in records.items() if r!=base[rid]]
added_aliases=len(load('MIGRATED_ALIASES.json'))+aliases['new_aliases']
def ratio(c,n,d):return f"{c.get(n,0)}/{c.get(d,0)} ({100*c.get(n,0)/c[d]:.2f}%)" if c.get(d) else 'N/A'
overview=[
 '# R119 ผลตรวจการย้ายข้อมูลเดิมเข้าสู่ Format กลาง', '',
 '## ผลสรุป', '',
 'ตรวจชุดต้นฉบับที่พบครบแล้ว และย้ายส่วนที่ตกหล่นพร้อมต่อตัวอ่านใน candidate R119 revision03 ข้อผิดพลาดเดิมหลายส่วนเกิดจากการแปลงข้อมูล/ความสัมพันธ์/ชื่อเรียกไม่ครบ และมีข้อมูลอยู่ใน native แล้วแต่ตัวอ่านไม่ใช้ ไม่ใช่เจ้าของยังไม่ได้ให้ข้อมูลทุกกรณี', '',
 '**ยังไม่รับรองว่า Flow ตอบถูกทั้งหมด** ผลทดสอบคำถามเดิมดีขึ้น แต่ยังพบปัญหาเก็บบริบท เลือกหมวด และรวมกติกาบางกรณี รายงานนี้แยกความครบของข้อมูลออกจากคุณภาพคำตอบ ไม่ขอให้เจ้าของกรอกข้อมูลเดิมซ้ำเพื่อแก้ปัญหาที่ตัวอ่านหรือการตีเจตนา', '',
 'candidate ยังไม่ได้ติดตั้งทับ R78/ระบบที่ใช้อยู่ ไม่ได้เปลี่ยน production data, approvals, releases, withdrawals หรือ log/result เดิม', '',
 '## 1 ขอบเขตที่บังคับตรวจ', '',
 '| รายการ | ผลตรวจ |','|---|---:|',
 f"| ไฟล์ข้อมูลใน candidate ที่มีคำตัดสินทุกไฟล์ | {audit['candidate_files_accounted']} |",
 f"| ไฟล์ต้นฉบับที่เก็บใน source registry และตรวจคืน byte ตรง | {audit['byte_exact_archives_verified']} |",
 '| อีก 14 ไฟล์ | workload/intent 11 และ native runtime 3; คงไฟล์ไว้ แต่ไม่เป็น answer authority |',
 f"| canonical records | {audit['canonical_records_accounted']} |",
 f"| ค่าปลายทางของ JSON ที่ตรวจตาม pointer | {audit['canonical_leaf_values_checked']:,} |",
 '| active canonical roots / guard templates | 249 / 21 |',
 f"| เอกสาร/ไฟล์ประกอบ structured rows ที่ parse เพิ่ม | 229 ไฟล์ / {load('AUXILIARY_DOCUMENT_CHECKLIST.json')['structured_rows_parsed']:,} rows |",
 f"| โมดูล literal constants ที่ทำบัญชีแยก | {len(load('CODE_LITERAL_CHECKLIST.json')['constants'])} |",
 f"| actual Legacy checkout ที่เทียบแบบอ่านอย่างเดียว | {audit['external_files_checked']:,} ไฟล์ |",
 f"| Word กติกาต้นฉบับ | {docx['documents_checked']} เอกสาร / {docx['matched']}/{docx['paragraphs_checked']} ย่อหน้าตรงกับ native rule text |",
 '| Excel ราคาเหมา | 52 เซลล์มีค่า จาก 25,740 cell elements; ราคา 24/24 แถวตรงทั้ง workbook → curated → native |',
 f"| native records / fields / evidence refs | {audit['native_records_checked']} / {audit['native_fields_checked']:,} / {audit['native_evidence_refs_checked']:,} |",
 f"| source snapshots ตรวจ hash | {audit['native_sources_checked']:,} |",
 '| schema, source hash, pointer และ FK errors ที่เพิ่ม | 0 |',
 f"| source/operator/alias contracts | {contracts['passed']}/{contracts['total']} |",
 f"| การเทียบค่าที่แปลงเป็น typed fields | {typed['total']:,} checks: {typed['literal_matches']:,} literal ตรง และ {typed['explicitly_reviewed_variants']} รูปแบบ/ข้อความขยายที่ตรวจแยก |", '',
 'จำนวนเซลล์ Excel ส่วนใหญ่เป็นเซลล์เปล่าที่มี formatting จึงไม่ใช้ 25,740 เป็นจำนวนข้อเท็จจริงทางธุรกิจ ส่วน Word ตรวจข้อความ body/table paragraphs ไม่ได้อ้างว่าตรวจ layout ของเอกสารใหม่', '',
 '## 2 สิ่งที่เพิ่มและซ่อม', '',
 f"เพิ่ม native revisions แบบ append-only {state['append_only_tables']['cc_revisions']['new_rows']} ครั้ง กระทบ active roots ไม่ซ้ำ {len(changed_roots)} รายการ; ฐานยังมี active roots 806 รายการเท่าเดิม ไม่สร้างเกมหรือเครื่องใหม่เพื่อกลบข้อมูลที่ไม่ทราบ", '',
 '| ส่วนที่แก้ | จำนวน/ลักษณะ | เหตุผล |','|---|---|---|',
 '| ต้นฉบับ canonical เต็มรายการ | legacy_context 249 roots | ไล่ตรวจค่าเดิมและ locale/provenance ได้ครบ; ไม่เอา raw context ไปแสดงเป็นคำตอบ |',
 f"| โซนที่ต้นฉบับระบุโดยตรง | {len(byfield['studio_zone_ids'])} ช่องใน game/service; มี 53 field writes เพราะบางเกมรวมหลายแหล่ง | แก้ข้อผิดพลาดที่บังคับมี resource ก่อนจึงตอบโซนได้ |",
 '| รูปแบบคำถามเดิม | legacy_search 73 roots | ใช้ช่วยเมื่อ typed reader ยังจับคำถามไม่ได้; ไม่แย่งตอบก่อนช่องตรง |',
 '| ขอบเขตโปรไฟล์สาธารณะที่บันทึกไว้ | 25 คน | ย้ายสถานะเผยแพร่ของต้นฉบับ ไม่สร้าง approval หรือยืนยันตำแหน่งปัจจุบันแทนเจ้าของ |',
 '| ค้นจากตำแหน่ง | role_aliases 22 คน | role → person ใช้คำเรียกเดิมได้ |',
 '| สังกัด/ช่วงเวลาบุคลากร | เปิด reader ให้ค่าที่มีอยู่แล้ว 12/5 คน | ไม่อ้างว่าสร้างข้อมูลใหม่; เก็บคำแปลที่ใหม่กว่า |',
 '| กฎคำนวณราคา | calculation_rule เติม 18 จาก 24 rates | คัดลอกกฎปัดรอบเฉพาะ service/group/amount/duration ที่ตรงต้นฉบับ |',
 '| ตารางให้เล่น | service_slots/service_closed ครบ 7 วัน | แยกจากเวลาเปิดอาคารและสถานะจองจริง |',
 '| คำบรรยายเกมต้นทางฉบับเต็ม | projection 31 เกม | ค่ามีใน native แล้ว ต่อ reader พร้อมวันที่บันทึกและ source scope |',
 '| ช่วงผู้ใช้บริการ | projection 8 บริการ | ไม่แปลงเป็นจำนวนเล่นพร้อมกันโดยไม่มีหลักฐาน |',
 f"| aliases ที่เติมรวม | {added_aliases} รายการ = เดิม 183 + code aliases {aliases['new_aliases']} | ชุดหลังมีอุปกรณ์ 91, โซน 24, เกม 13; ไม่ย้ายข้อความคำตอบลัดมาทับ business facts |",
 f"| alias ที่ชนกับ entity อื่น | {aliases['ambiguous_aliases_not_added']} รายการไม่เติม | ไม่เลือก entity เดียวจากคำเรียกกำกวม |", '',
 '17 กรณีคงค่า native ที่ใหม่กว่าไว้ เป็นข้อมูลบุคลากรที่มีค่าเดิมภาษาไทยพร้อมคำแปล/ข้อมูลเพิ่ม ไม่ใช่ 17 ข้อมูลที่ย้ายตกหล่น ดู RETAINED_VARIANTS_AND_LIMITS.json และ TYPED_VARIANT_DECISIONS.json', '',
 '## 3 ผล API บนคำถามเดียวกัน', '',
 'ใช้ 48 keys เดิมจากชุด Full ที่เคยเทส ไม่สร้างคำถามเพิ่มและไม่รัน Legacy baseline ใหม่ มี 164 grades แต่มีเพียง 62 positive literal/clause checks ใน 18 คำถาม จึงห้ามแปล 62/62 ว่าถูก 100% ของคำถามทั้งระบบ', '',
 'ทดสอบ R119 สามรอบเพื่อแก้ปัญหาที่พบระหว่างตรวจ รวม 144 HTTP attempts แต่มีเพียง 48 คำถามไม่ซ้ำ รอบล่าสุดคือ revision03 แบบ LLM ON ไม่มีการส่ง category hint/expected answer เข้าแชท', '',
 'Clock อ้างอิงของชุดนี้ตรึงตาม R118 ที่ 2026-10-21T12:00:00+07:00 จึงไม่ใช่การตรวจว่าเวลาที่กำลังอ่านรายงานศูนย์เปิดจริงหรือไม่', '',
 '| รุ่น | Positive literal/clause | ข้อผ่าน positive ทุกแถว | Strict compatibility |','|---|---:|---:|---:|',
]
for name,sc in scores.items():
 t=sc['total'];overview.append(f"| {name} | {ratio(t,'positive_pass','positive_grades')} | {ratio(t,'positive_all_pass','positive_requests')} | {ratio(t,'strict_pass','grades')} |")
overview+=['','### แยกภาษา','','| ภาษา | Legacy saved | R118 revision02 saved | R119 revision03 |','|---|---:|---:|---:|']
for locale in ['th','en','auto']:
 overview.append('| '+locale+' | '+' | '.join(ratio(scores[n]['by_locale'][locale],'positive_pass','positive_grades') for n in ['Legacy_R64_saved','R118_revision02_saved','R119_revision03'])+' |')
overview += ['',
 'Strict ยังมี route/mode/contract รุ่น Legacy รวมอยู่ด้วย ทุก grade ของ candidate ยังมี protocol mismatch จึงไม่ใช้ strict 0 เป็นหลักฐานว่าคำตอบเนื้อหาผิดทุกข้อ และไม่แก้ grader ให้เข้าข้าง candidate ส่วน positive เป็น literal checks ไม่ได้ตรวจความครบของคำตอบทุกมิติ', '',
 'Legacy R64 กับ candidate ใช้ข้อมูลต่างรุ่น โดยเฉพาะข้อยืนยันเจ้าของ/หน่วยราคา/แปลภาษา จึงไม่ใช่ causal effect ของ Flow เพียงอย่างเดียว', '',
 '### Transport และความถูกต้อง', '',
 f"- API ล่าสุด HTTP 200 ครบ {done['stats']['http_ok']}/48; capture mismatch {done['stats']['capture_mismatch']}; ไม่มีคำตอบว่างหรือ API timeout ตาม flag ของ API",
 f"- Model transport: {analysis['transport']}; เป็นสถานะการเชื่อมต่อถึง response headers ไม่ใช่ semantic score",
 f"- เวลา median {analysis['latency']['median_sec']:.2f} วินาที; สูงสุด {analysis['latency']['max_sec']:.2f} วินาที",
 '- ตรวจ model name และ digest ต้น/ท้ายรอบ: scb10x/typhoon2.5-qwen3-4b:latest',
 '- การสร้าง JSON/schema ผ่าน การตีเจตนาถูก การเลือกข้อมูลครบ และการตอบถูก เป็นคนละเกณฑ์กัน',
 '- live provider ใน workload ถูกตั้ง unavailable เพื่อเทียบสถานการณ์เดิม ไม่ใช่ผลยืนยันว่าเครื่องจริงว่าง/ไม่ว่าง', '',
 '## 4 เคสที่ยืนยันว่าดีขึ้นจากข้อมูลที่เติม', '',
 '- Mario และ Little Nightmares II: อ่าน Nintendo Switch Zone จาก direct source relation ได้',
 '- ประธาน: ค้นชื่อจากตำแหน่งได้ภายใต้ published-profile scope',
 '- Kamlawan Nuansai: จับกับชื่อเรียกที่มีแหล่งเดิมและคนเดียว ไม่สร้างชื่อบุคคลใหม่',
 '- ศุกร์บ่าย/จันทร์เช้า: ตอบไม่เปิดให้เล่นเพราะบำรุงรักษาตามตารางที่บันทึกไว้',
 '- PS5 2 ชั่วโมง: ใช้กฎปัดรอบที่ถ่ายจาก calculator เดิม พร้อมหน่วย/ข้อยืนยันราคาล่าสุด',
 '- Gaming Chair: revision02 เปลี่ยนกลับมาอ่าน location: PC Zone โดยตรง',
 '- เมาส์ภาษาไทย: เติม aliases จากโค้ดเดิม และมี source contract ตรวจว่าคำถามพิมพ์ผิดเดิมเข้าถึง Gaming Mouse ได้; ดูผล HTTP revision03 รายข้อประกอบ', '',
 '## 5 สิ่งที่ยังไม่จบที่ระดับคุณภาพคำตอบ', '',
 'ข้อมูลครบในขอบเขตที่ตรวจไม่ได้แปลว่า reader/การตีเจตนาสมบูรณ์ทั้งหมด โดยเฉพาะราคาเกม การทิ้งบริบท AOV การรักษา duration ภาษาอังกฤษ และการรวมบทลงโทษหลาย clause ต้องอ่านผลล่าสุดและสาเหตุใน ROOT_CAUSE_REVIEW_TH.md', '',
 'ไม่ควรขอให้เจ้าของตอบว่า Gaming Mouse มีหรือไม่ หรือส่งเอกสารกติกาใหม่ เพื่อแก้ปัญหาที่ระบบมีข้อมูลอยู่แล้วแต่เลือก/อ่านผิด ส่วนสิ่งที่ต้นฉบับไม่ยืนยันจริง เช่น physical video recording, unqualified game edition และ live occupancy ต้องคงขอบเขตไว้', '',
 '## 6 หลักฐานและไฟล์อ่านต่อ', '',
 '- '+link('FLOW_AND_MAPPING_TH.md','Flow และ mapping แบบละเอียด'),
 '- '+link('ROOT_CAUSE_REVIEW_TH.md','วิเคราะห์ปัญหาที่ยังพบและแนวทางแก้'),
 '- '+link('ALL_RECORDS_CHECKLIST_TH.md','canonical ทั้ง 270 รายการ'),
 '- '+link('ALL_FILES_CHECKLIST_TH.md','ไฟล์ข้อมูลทั้ง 502 ไฟล์'),
 '- '+link('http03/analysis/CASEBOOK_TH.md','คำถาม คำตอบ แผน และหลักฐานทุกข้อ'),
 '- '+link('FULL_AUDIT_GATE.json','ผลตรวจข้อมูลและอ้างอิง'),
 '- '+link('PRIMARY_DOCX_AUDIT.json','เทียบ Word ต้นฉบับทุกย่อหน้า'),
 '- '+link('RENTAL_WORKBOOK_PRICE_AUDIT.json','เทียบราคาเหมา workbook กับ native'),
 '- '+link('CODE_ALIAS_MIGRATION.json','aliases ในโค้ดเดิมที่ย้าย/ไม่ย้ายพร้อมเหตุผล'),
 '- '+link('PRESERVED_STATE_GATE.json','ตรวจ revisions/sources/approvals/withdrawals เดิม'), '',
 '## 7 ข้อสรุปเรื่องความครบ', '',
 'ครบในความหมายว่าไฟล์/record/ค่าต้นฉบับที่อยู่ในขอบเขตตรวจมีบัญชีครบ เก็บต้นฉบับได้ตรง ย้ายค่าธุรกิจที่แปลงได้อย่างมีหลักฐาน และเปิดตัวอ่านส่วนที่ระบุในรายงานแล้ว ไม่มีข้อผิดพลาดด้าน schema/evidence เพิ่ม ไม่ใช่คำรับรองว่าทุกข้อความจาก cache เป็น business authority หรือทุกคำถามเข้า Flow ถูก 100%', '',
 '21 guard templates, 12 aliases ที่ชน entity อื่น, ข้อความ cache ที่ไม่มีหลักฐานธุรกิจอิสระ และ Minecraft ที่ไม่มี native business entity ไม่ถูกนำมาแต่งเป็นรายการบริการใหม่ ต้นฉบับเหล่านี้ยังคงอยู่และมีเหตุผลกำกับครบ', '',
]
(R/'REPORT_TH.md').write_text('\n'.join(overview),'utf8')
doc=['# รายการตรวจ canonical ทุก record','','249 active roots เชื่อมกับ native; อีก 21 guard/no-answer templates เก็บเป็นต้นฉบับและไม่สร้าง permanent negative business facts รายการนี้คือการบัญชีข้อมูล ไม่ใช่คะแนน semantic ของทุก intent','','| # | ชนิด | Content ID | Native root | คำตัดสิน | ไฟล์ต้นฉบับ |','|---:|---|---|---|---|---|']
canonical={x['record']['content_id']:x['record'] for x in load('LEGACY_RECORDS.json')}
for i,m in enumerate(mapping,1):doc.append(f"| {i} | {canonical[m['content_id']]['kind']} | {m['content_id']} | {m['native_record_id'] or '—'} | {m['status']} | [{m['path']}](<{(S/m['path']).as_posix()}>) |")
(R/'ALL_RECORDS_CHECKLIST_TH.md').write_text('\n'.join(doc)+'\n','utf8')
doc=['# รายการตรวจไฟล์ข้อมูลทุกไฟล์','','SHA และการเก็บคืน byte ตรวจใน BYTE_RETENTION_AUDIT.json; native runtime เป็นฐานที่แก้แบบ append-only จึงตรวจแยก การไม่เป็น answer authority ไม่ได้หมายถึงไฟล์ถูกลบ','','| # | ไฟล์ | ประเภท | คำตัดสิน |','|---:|---|---|---|']
for i,f in enumerate(files,1):doc.append(f"| {i} | [{f['path']}](<{(S/f['path']).as_posix()}>) | {f['classification']} | {f['disposition']} |")
(R/'ALL_FILES_CHECKLIST_TH.md').write_text('\n'.join(doc)+'\n','utf8')
write('ANALYSIS_FINAL.json',{'complete':True,'revision':'R119 revision03','source_audit_complete_with_scoped_limits':True,'all_questions_semantically_correct':False,'production_installed':False,'new_questions':0,'http_attempts':144,'unique_requests':48,'latest_grades':164,'source_contracts':contracts['total'],'typed_value_checks':typed['total'],'new_aliases':added_aliases,'new_revisions':state['append_only_tables']['cc_revisions']['new_rows'],'changed_roots':len(changed_roots),'score_latest':latest,'model_transport':analysis['transport'],'originals_unchanged':True,'completed_at':datetime.now().astimezone().isoformat()})
write('STATUS.json',{'phase':'completed_source_audit_and_saved_question_validation','complete':True,'production_installed':False,'full_test_run':False,'new_questions':0,'semantic_accuracy_claimed':False})
print(json.dumps({'report':str(R/'REPORT_TH.md'),'source_audit_complete':True,'contracts':contracts['total'],'aliases_added':added_aliases,'revisions_added':state['append_only_tables']['cc_revisions']['new_rows'],'active_roots_changed':len(changed_roots)},ensure_ascii=False))
