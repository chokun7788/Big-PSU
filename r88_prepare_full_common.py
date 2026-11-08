"""Freeze R87's installed common chat and the entire retained full corpus."""
import collections,hashlib,json,shutil,sqlite3
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;R=B/'r88_full_common_llm_20261017';SRC=B/'r78_web_session_check_20261016';S=SRC/'system';R.mkdir(exist_ok=False)
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
installation=json.loads((B/'r87_common_behavior_bridge_20261017/INSTALLATION_2.json').read_text('utf8'))
assert all(digest(S/n)==sha for n,sha in installation['installed_files'].items())
assert digest(S/'data/knowledge/common.sqlite')==installation['database_sha256']
manifest=[];excluded=[]
for folder in ['app','tools','data','booking_dashboard','web_chat']:
 for p in sorted((S/folder).rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(S)
  if '__pycache__' in rel.parts or p.suffix=='.pyc':continue
  if rel.parts[:2] in [('data','knowledge'),('data','logs'),('data','state'),('data','common_test_tmp')]:continue
  # Nested eval folders hold old outputs, not corpus inputs.
  if rel.parts[:2]==('data','eval') and len(rel.parts)>3:continue
  if p.suffix in {'.sqlite','.sqlite-wal','.sqlite-shm','.db'}:continue
  z=R/'system'/rel;z.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,z)
  manifest.append({'path':rel.as_posix(),'sha256':digest(p),'bytes':p.stat().st_size})
db=R/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True,exist_ok=True)
with sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as z:a.backup(z)
for name in ['SESSIONS.json','GUARDS.json','INVENTORY.json']:shutil.copy2(B/'r64_full_comparison_20261013'/name,R/('CORPUS_'+name))
shutil.copy2(B/'r64_full_comparison_20261013/grade_legacy.py',R/'reference_grader.py')
source_jobs=B/'r64_full_comparison_20261013/JOBS.jsonl';jobs=[json.loads(s) for s in source_jobs.read_text('utf8').splitlines() if s.strip()]
assert len(jobs)==len({j['key'] for j in jobs})==20554
assert sum(len(j['entries']) for j in jobs)==55811
for job in jobs:
 c=job['entries'][0]['case'];domain=next((c.get(k) for k in ['domain','group','expected_category','expected_intent','category','topic','kind'] if c.get(k)),'unclassified')
 if not isinstance(domain,str):domain=json.dumps(domain,ensure_ascii=False,sort_keys=True)
 style=next((c.get(k) for k in ['noise','mutation','question_style','case_type'] if c.get(k)),job['entries'][0]['variant'])
 job['r70_stratum']={'locale':job['locale'],'corpus':job['entries'][0]['file'],'domain':domain,'style':style}
# Fixed hash order avoids corpus grouping from changing warmup/queue bias.
jobs.sort(key=lambda j:hashlib.sha256(('r88-full-v1|'+j['key']).encode()).hexdigest())
with (R/'SELECTED_JOBS.jsonl').open('x',encoding='utf8') as f:
 for job in jobs:f.write(json.dumps(job,ensure_ascii=False)+'\n')
config={'created_at_utc':datetime.now(timezone.utc).isoformat(),'population_requests':len(jobs),'selected_requests':len(jobs),'fraction':1.0,'selected_grades':55811,'llm_enabled':True,'only_format':'common','profile':'r69-migration-preview','source_installation':str(SRC),'source_release':'R87 installed stage 2','source_database_sha256':digest(S/'data/knowledge/common.sqlite'),'test_database_sha256':digest(db),'population_jobs_sha256':digest(source_jobs),'frozen_jobs_sha256':digest(R/'SELECTED_JOBS.jsonl'),'selection':'all retained R64 unique requests; fixed hash order r88-full-v1, no pass-based selection','selected_locales':dict(collections.Counter(j['locale'] for j in jobs)),'execution':'actual current engine, isolated subprocesses; not browser or load certification','booking':'controlled unavailable, no live occupancy oracle','reference_clock':'2026-10-16T12:00:00+07:00, same as R70 for paired analysis; per-job dates override','application_snapshot_changed':False,'source_manifest':manifest,'workers':2,'model_admission_limit':1,'large_legacy_arm':False,'llm_off_arm':False,'session_cases':12,'guard_cases':500,'unit_legacy_suites_executed':False}
with (R/'CONFIG.json').open('x',encoding='utf8') as f:json.dump(config,f,ensure_ascii=False,indent=2)
assert all(digest(R/'system'/row['path'])==row['sha256'] for row in manifest)
scope='''# R88 Full test: Format กลางล่าสุด + LLM ON

ใช้สำเนาที่ตรึงจาก R78 หลังติดตั้ง R87 stage 2; ฐานข้อมูล 602 records ไม่สร้าง approval/release และไม่แก้ข้อมูลศูนย์

- Full corpus เดิม: 20,554 unique request keys และ 55,811 grades ไม่มีแขน legacy หรือ LLM OFF
- มีทั้งไทย อังกฤษ auto และ clean/noisy ตามข้อมูลเดิม ไม่เลือกเฉพาะข้อที่เคยผ่าน
- 2 evaluator workers, model admission 1 ช่อง เช่นข้อจำกัดการเรียกโมเดลในระบบ; เปิด assistance ตลอด ไม่บังคับทุกคำถามให้ใช้โมเดล
- ก่อนเริ่มต้องยืนยัน generation จริงและตรวจ pilot ว่าการเรียก selector ใช้งานได้ ไม่แทนโมเดลด้วย mock/fallback OFF
- แต่ละคำถามหลักเริ่ม history ว่าง; แยก 12 session cases และ 500 guard diagnostics ต่างหาก พร้อมส่ง trusted common_read_state สำหรับ session
- สถานะจองใช้ controlled unavailable ไม่ใช่การตรวจ WordPress occupancy สด ไม่ใช้ผลนี้ยืนยัน slot ว่าง/ถูกจองจริง
- คง reference clock เดียวกับ R70 (16 ต.ค. 2026 12:00 ไทย) เพื่อเทียบ subset ได้; reference_date เฉพาะโจทย์มีสิทธิ์เหนือกว่า ไม่แก้ effective dates ในข้อมูลราคา
- เก็บ raw answers, decision_artifact, selected source hits, model HTTP diagnostics, grades และ exceptions แบบ append-only แยกโฟลเดอร์ใหม่
- วิเคราะห์ protocol/outcome/evidence identifier/content/validation/performance/grader/model transport แยกกัน; raw fail ไม่เท่ากับเนื้อหาผิดทุกกรณี
- ทุกเกณฑ์เดิมเก็บครบ มีการตรวจ literal/source content เพิ่มโดยไม่แก้ oracle ให้คะแนนสูงขึ้น คำตอบไม่มี positive contract จะไม่อ้างว่าตอบครบ
- ตัว supervisor จะตรวจ coverage/hash แล้วสร้างรายงานอัตโนมัติเมื่อครบเท่านั้น หากหยุดจริงเก็บ partial/error ไว้ ไม่อ้างว่าเสร็จ

ขอบเขตนี้ไม่รวม unit/smoke ที่รัน profile เดิม และไม่ใช่ production/owner approval หรือ load benchmark
'''
with (R/'RUN_SCOPE_R88_TH.md').open('x',encoding='utf8') as f:f.write(scope)
print(json.dumps({k:v for k,v in config.items() if k!='source_manifest'},ensure_ascii=False))
