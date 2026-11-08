"""Reconcile evidence and freeze the experimental candidate for measurement."""
import ast,hashlib,json,pathlib,datetime
R=pathlib.Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
evidence={}
for name in ['hybrid_routes','hybrid_finance','hybrid_ranges','http_lifecycle']:
 p=sorted(R.glob(name+'_*/RESULT.json'))[-1];d=read(p);assert d['all_passed'];evidence[name]={'path':str(p.relative_to(R)),'sha256':sha(p),'checks':len(d['checks']),'scope':d['scope']}
assert read(R/'FOCUSED_BATCH.json')['all_passed']
for p in (R/'system/app').rglob('*.py'):
 if 'vendor' not in p.parts and '__pycache__' not in p.parts:ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
mapping=read(R/'REQUIREMENT_MAP.json')
for row in mapping['rows']:
 row['hybrid_acceptance']='experimental_component_evidence; full requirement not closed'
 row['evidence_index']='IMPLEMENTATION_EVIDENCE.json'
 if row['id']=='C03':row['reader_assignment']='R134 plan algorithm for detail/device_type; R135 for other registered operations; mechanical subtype definition withheld'
 elif row['id'].startswith('C') and row['id'][1:].isdigit():row['reader_assignment']='R135 inherited reader; source/scope/coverage guards required; full category semantics unaccepted'
 elif row['hybrid_role']=='retained_model_training_deferred':row['hybrid_acceptance']='deferred; use retained planner, no new training or adapter promotion'
(R/'REQUIREMENT_MAP.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),'utf8')
record={'actual_evidence':evidence,'affected_regression':'FOCUSED_BATCH.json','historical_failed_batch_preserved':sorted(p.name for p in R.glob('FOCUSED_BATCH_HISTORY_*.json')),'harness_amendments':'HARNESS_AMENDMENTS.json','paired_question_triage':'PAIRED_REVIEW.json','score_semantics':'not measured by source tests','full_48_or_76_acceptance':False,'owner_original_live_frozen_modified':False,'model':'existing retained weights; separate app and model Python environments; no package installation'}
(R/'IMPLEMENTATION_EVIDENCE.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),'utf8')
files=[{'path':p.relative_to(R).as_posix(),'sha256':sha(p)} for p in sorted((R/'system').rglob('*')) if p.is_file() and '__pycache__' not in p.parts and 'data' not in p.relative_to(R/'system').parts and p.suffix in {'.py','.json','.html','.js','.css'}]
(R/'CANDIDATE_MANIFEST.json').write_text(json.dumps({'created_at':datetime.datetime.now().astimezone().isoformat(),'files':files,'runtime_data_manifest':'RUNTIME_DATA_MANIFEST.json','runtime_data_manifest_sha256':sha(R/'RUNTIME_DATA_MANIFEST.json'),'source_database':'evaluation/source.sqlite','sqlite_backup_sha256':sha(R/'evaluation/source.sqlite'),'selected_sha256':sha(R/'evaluation/SELECTED_5_PERCENT_v2.jsonl'),'frozen_for_measurement':True,'trial_editor_database_separate':True},indent=2),'utf8')
report='''# ผลการประกอบ R135 รุ่นทดลองแบบผสม

แชตทดลอง: http://127.0.0.1:8125/ — editor 8126 ใช้ฐานสำเนาของตนเอง
เซิร์ฟเวอร์ประเมิน: 8127 — ฐานข้อมูล snapshot แยกจาก editor

- เอกสาร flow.md และ REQUIREMENT_MAP.json เก็บการใช้ชุด48 historical IDs และส่วนพึ่งพาจากข้อที่เหลือ โดยไม่ปิดข้อกำหนดเดิมเอง
- ลงทะเบียนเส้นทาง104 category/operation/field; R134 ใช้เฉพาะ C03/detail/device_type ผ่าน shared R135 helpers/index/renderer/verifier ไม่อ้างว่าเป็นR134ทั้งระบบ
- เพิ่ม bounded independent calculation checks, direct output-total tamper checks, missing-total notice และ source-specific person bounds ที่ไม่จับบริการต่างกันด้วย platform เดียว
- ผ่าน controlled lifecycle/forgery และ actual owner/chat HTTP add→edit→withdraw ของ synthetic record แยก ไม่มีการยืนยัน authority ของธุรกิจ
- เก็บ failed attempts และ harness amendments ครบ ตัวทดสอบเก่าบางส่วนตั้งเป้ากว้างกว่าพฤติกรรมที่guardตั้งใจอนุญาต ไม่ได้นำการปรับ assertion มาอ้างเป็นproduction fix
- แยก30คำถามที่ literal ต่างจากR134 เป็นsource/runtime/clarification/formatting/content triage ยังไม่ให้semantic score
- known limits: operator FAQ ยังไม่มีcenter/authority binding; mechanical subtype definitionยังระงับ; range labelsยังไม่พิสูจน์group allocation; all14 bounded lanesไม่ใช่การรับรองทุกoperation
- รันทดสอบ5%จากmanifestเดิม1056คำถามหนึ่งรอบ ผล literal/transport/unassessedแยกจากsemantic correctness

เปิด RESULTS_VIEW.html เพื่อดูผลโดยไม่ต้องเปิด JSON โดยตรง หลัง evaluation/PROGRESS.json running=false ให้ตรวจผลดิบ จำนวนแถว scores และข้อผิดพลาดก่อนสรุป รุ่นนี้ยังไม่แทนตัวใช้งานจริง และR135เต็มยังเก็บไว้
'''
(R/'IMPLEMENTATION_REPORT_TH.md').write_text(report,'utf8')
status=read(R/'STATUS.json');status.update(phase='frozen_evaluation_starting',evaluation_started=True,full_48_complete=False,full_76_complete=False,trial_ready=True,remaining_work='frozen 1056 evaluation, inspect results and group actual failures; original full requirements remain open');(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'evidence':evidence,'code_files_frozen':len(files)}))
