import json,hashlib,statistics,subprocess,urllib.request
from pathlib import Path
from datetime import datetime
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip());package=project/'owner_local_delivery_20261002_competition_composition_r28_guard_verified/PSU_Esports_Chatbot_Local'
owner=Path((root/'owner_information_request_latest.txt').read_text(encoding='utf-8').strip())
def read(name):return json.loads((report/name).read_text(encoding='utf-8'))
def rows(name):return [json.loads(x) for x in (report/name).read_text(encoding='utf-8').splitlines() if x.strip()]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=5));assert health['runtime']['version']=='2026.10.02-competition-composition-r28-guard-verified'
ready=read('http_final_ready_8090.json');assert ready['total']==ready['passed']==36
preflight=read('release_preflight_verified.json')
protected=read('protected_manifest.json');protected_checks={p:sha(project/p)==s for p,s in protected.items()};assert all(protected_checks.values())
before=read('before_manifest.json');snapshot_checks={}
for name,digest in before.items():
    path=report/'before'/name
    if not path.exists():path=report/'before'/name.replace('/','__')
    snapshot_checks[name]=path.exists() and sha(path)==digest
assert all(snapshot_checks.values()),snapshot_checks
app_checks={str(p.relative_to(project)).replace('\\','/'):sha(p)==sha(package/p.relative_to(project)) for p in (project/'app').rglob('*.py')};assert all(app_checks.values())
initial=read('full_r28_A_summary.json');merged=read('full_merge_audit.json');graded=read('full_r28_corrected_source_grade.json')['summary'];assert graded['source_grade_passed']==2000 and merged['merged_legacy_passed']==1953
unit=read('candidate_G_unit.json');assert unit['success'] and unit['tests']==154
http_records=[]
for name,n in [('verified_http280',280),('verified_http_resolution12',12),('verified_http320',320)]:
    summary=read(name+'_summary.json');assert summary['passed']==summary['total']==n
    http_records+=rows(name+'_details.jsonl')
reg=read('http_guard_verified_regression.json');assert reg['total']==reg['passed']==36
latencies=[r['elapsed'] for r in http_records]+[r['elapsed_sec'] for r in reg['cases']]
ordered=sorted(latencies)
percentile=lambda p:ordered[min(len(ordered)-1,round((len(ordered)-1)*p))]
test_health=read('http_final_health_after.json');performance=Path(test_health['pipeline_workers']['performance']['path']);events=[json.loads(x) for x in performance.read_text(encoding='utf-8').splitlines() if x.strip()]
recycle=[e for e in events if e.get('event')=='worker_recycle'];promotions=sum(e.get('status')=='promoted' for e in recycle)
assert promotions>=2
with (report/'worker_recycle_events.json').open('x',encoding='utf-8') as f:json.dump(recycle,f,ensure_ascii=False,indent=2)
guard=read('guard_prior_audit.json')['summary'];assert guard['newly_blocked']==0
checks={'completed_at_bangkok':datetime.now().astimezone().isoformat(),'runtime_version':health['runtime']['version'],'ready_url':'http://127.0.0.1:8090/','package':str(package),'protected_files_unchanged':protected_checks,'prechange_snapshots_match':snapshot_checks,'app_source_matches_package':app_checks,'unit':{'passed':154,'total':154},'new_composition':{'baseline':63,'total':280,'after_pipeline':280,'after_actual_web':280},'old_pipeline_regressions':{'320':320,'128':128,'80':80},'full_gold':dict(merged,source_grade=graded),'actual_web':{'sequential_requests':648,'passed':648,'ready_8090_smoke':36,'worker_promotions':promotions,'http_errors_in_verified_suite':0,'timings_sec':{'median':round(statistics.median(latencies),4),'p95':round(percentile(.95),4),'max':max(latencies)},'scope':'transport, competition clause contracts and mixed-route smoke; booking HTTP success not real booked/free oracle'},'guard_scan':guard,'owner_forms':{p.name:sha(p) for p in owner.glob('*.md')},'owner_confirmation':'pending; original V2 queue unchanged','real_booking_oracle':'deferred by user; automated booking fixtures only'}
with (report/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(checks,f,ensure_ascii=False,indent=2)
with (report/'ready_health_8090.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (report/'git_status_after.txt').open('x',encoding='utf-8') as f:f.write(status)
changed={p:{'before':digest,'after':sha(project/p)} for p,digest in before.items() if sha(project/p)!=digest}
with (report/'changed_file_manifest.json').open('x',encoding='utf-8') as f:json.dump(changed,f,ensure_ascii=False,indent=2)
result=f'''# ผล r28 — กติกาหลายประเด็นและ input guard

เสร็จวันที่ {checks['completed_at_bangkok']}. เริ่มงาน/ชื่อ report ใช้วันที่ 1 ตุลาคม ระหว่างงานข้ามเป็น 2 ตุลาคม

## เว็บพร้อมลอง

[เปิดแชท](http://127.0.0.1:8090/) รุ่น `{health['runtime']['version']}`

แพ็กเกจใหม่: `{package}`. Launcher PID 2976; เว็บทดสอบ 8091 หยุดแล้ว. ต้องให้โปรแกรมเว็บรันอยู่ขณะใช้; โหมดจองดึง WordPress ต่อคำถาม ไม่ต้องมี Dashboard แยกสำหรับแพ็กเกจนี้. ไม่เปลี่ยนหรือหยุด Dashboard ต้นฉบับ/Ollama

## เปลี่ยนอะไรและเหตุผล

- เพิ่มการเลือก clause ของ 24 แนวคิดทั่วไปสองภาษา ครอบคลุมคำถามแคบเรื่อง bugs, streams, macros, install, equipment responsibility, prep, drinks, technical reasons, abilities, customization และอื่น ๆ จากต้นฉบับเดิม
- แก้เงื่อนไขที่ตัดหัวข้อจากคำทั้งประโยค: normal money/overtime, language/protest, map pool/map tool, equipment permission/quality. ชุดทดสอบตรวจ 16 คู่ประเด็นต่อภาษา
- แยก final decision จาก final match และ dispute resolution จาก screen resolution. ข้อผิดจริง 12 ข้อจากชุดใหญ่แก้และตรวจผ่านเว็บอีกครั้ง
- ค่าสมัครที่ไม่มีหลักฐานไม่ใช้ข้อ late registration แทน. คำถาม scripts+fee เก็บข้อ scripts และแจ้งว่า fee ไม่พบ; validation ของ partial ยังบังคับแหล่งเกมถูก
- เลขข้อที่ถามต้องตรง; RoV 6.1.5.1 ที่ต้นฉบับขาดไม่ใช้โทษข้อใกล้เคียงเติม. Tekken pause แจ้งเอกสารขัดกันตั้งแต่บรรทัดแรกและแสดงทั้งสองข้อ ไม่เลือกนโยบายแทนผู้จัด
- เพิ่ม pronouns/คำหน้าที่จริงใน English language prior เพราะ its ถูกตีเป็นแป้นผิด. ไม่ปิด guard ไม่ลด threshold และไม่สร้าง alias ทั้งประโยค. Profile hash รวม prior แล้ว
- Freeze เวลาเฉพาะ fixture tests วันที่ 1 ตุลาคม เพื่อให้ “วันนี้” ตรง CSV หลังข้ามวัน. Runtime ยังตรวจวันที่จริง

## ผลอัตโนมัติ

| ชุดตรวจ | ผล | ความหมาย |
|---|---:|---|
| ชุดใหม่ 280 ข้อ | ก่อน 63/280 → หลัง 280/280 | 28 ประเด็นเดี่ยว + 16 คู่ + 8 controls ต่อภาษา; clean/polite/task typo |
| ชุดเดิม 320 / 128 / 80 | 320 / 128 / 80 ผ่านครบ | Regression ใน pipeline; ไม่ใช่ owner Gold |
| Unit | 154/154 | รวม routing, source gaps/conflicts, negation, source target, booking fixtures และ worker behavior |
| Ground Truth 2,000 รอบแรก | legacy 1,941/2,000 | ผิดประเด็นจริง 12 + ตัวตรวจ source presence พลาด 47 |
| หลังทดสอบ 59 ข้อที่ผิดซ้ำ | legacy รวม 1,953/2,000; source-grade 2,000/2,000 | ผลรวมจากรอบแรก 1,941 ข้อ + retest 59; ไม่ใช่รันเต็มรอบสองหรือ semantic correctness ทั้งชุด |
| เว็บแพ็กเกจจริง | 280 + 12 + 320 + 36 = 648/648 | รันทีละชุด; เนื้อหาตาม contracts/route smoke; ไม่มี 500/503 |
| หลังเปลี่ยน 8090 | 36/36 | Health/runtime รุ่นตรงและ mixed-route smoke |
| Guard ก่อน/หลัง | 4,283 ข้อ; newly blocked 0; ปลด false rejection 3 | Guard-only; ยังมี 36 ข้อชุด multi-error เก่าที่ต้องวิเคราะห์ พร้อม negative controls 2 ข้อที่ถูกหยุดตามเดิม |

เว็บ verified median {checks['actual_web']['timings_sec']['median']} s, p95 {checks['actual_web']['timings_sec']['p95']} s, max {checks['actual_web']['timings_sec']['max']} s. ไม่ใช่ benchmark ทุกคำถาม. ข้อช้าที่สุดคือ unsupported-game clarification/no-answer ยังผ่านเส้นทาง LLM บางส่วนราว 10–11 s. Worker recycle เปลี่ยนตัวสำเร็จ {promotions} ครั้งในชุดเว็บ โดยไม่มี transport error

รอบเว็บก่อนแก้ guard 275/280: ข้อผิด guard 3 + HTTP 503 จากการรันสอง clients พร้อมกัน 2. เก็บ logs/คำตอบ/trace เดิมทั้งหมดและรันทดสอบใหม่ทีละชุด ไม่ปรับเกณฑ์ให้คำตอบผิดผ่าน

## สิ่งที่คนหรือเจ้าของยังไม่ได้ยืนยัน

1. Tekken pause s03/s07: ข้อห้ามทั่วไปกับยินยอมทุกคนใช้เงื่อนไขใด กรรมการต้องอนุญาตหรือไม่ และปรับแพ้ Round/Game/Match ระดับใด
2. RoV 6.1.5–6.1.5.1: ขอข้อความต้นฉบับฉบับเต็ม เพราะท้ายข้อจบที่ “ออกจาก”
3. รายการ/ฉบับ/วันที่ใช้จริงของ rulebook และ V2 104 ข้อ. Translation approval ในระบบไม่ใช่ owner policy signoff
4. รุ่น/จำนวนจอย PS5, นโยบายภาพและวิดีโอ, ชื่ออังกฤษทางการ 23 คน/ชื่อรายการ Tekken
5. การเข้าใช้ของบุคคลทั่วไป และการนำอาหารเข้า/พื้นที่รับประทาน: ปัจจุบันมี user review+site context; ยังไม่มี owner signoff ในไฟล์
6. อายุขั้นต่ำ/ค่าสมัครแต่ละรายการ ถ้าต้องการให้ตอบได้: ต้องส่งประกาศพร้อมหน่วย/วันนับอายุ/ข้อยกเว้น. ห้ามใช้ราคาจองเครื่องเป็นค่าสมัครแข่ง
7. Oracle จองจริงกับเจ้าของยังเลื่อนไว้ตามคำสั่งผู้ใช้. API เชื่อมได้/HTTP 200 ไม่ยืนยัน booked/free ถูกต้องของข้อมูลจริง. ผล booked/free ที่ยืนยันอัตโนมัติเป็น fixture เท่านั้น

## งานต่อที่จัดลำดับได้

1. ตรวจ 36 noisy inputs ที่ guard ยังหยุดจากชุดเก่า ตาม span และบริบท; ยังไม่ใช่ผลตอบผิดทั้งหมด ต้องตรวจความหมายก่อน
2. เสริมการวัดความครบของคำถามที่มีมากกว่า 2 ประเด็น, หลายเกม, หลายเลขข้อ และ missing age+eligibility. ปัจจุบัน missing-age guard อาจตอบ no-answer ทั้งคำถาม; ไม่อ้างว่ารวมทุกประเด็นได้
3. ลดเวลาตอบกรณีเกมไม่รองรับ/ถามกลับที่ไม่ต้องใช้ LLM และตรวจผู้ใช้พร้อมกันหลายคน. การรันทีละคำถามผ่านไม่ได้พิสูจน์ concurrency
4. นำข้อมูลเจ้าของกลับมาทบทวนเฉพาะข้อที่ยืนยันแล้ว พร้อม source/version/hash และ regression; ไม่เติมนโยบายหรือข้อความ source ที่ขาดเอง

## หลักฐานและการรักษาไฟล์

Protected source/Gold/V2 queue/English CURRENT/owner schedule/service policies/r27 Flow 9 ไฟล์ hash ตรงเดิม. Snapshot ก่อนเปลี่ยนทุกไฟล์เดิมที่แก้เก็บใน before พร้อม manifest. ไม่ reset/checkout/stash Git ไม่ลบไฟล์ที่ยังไม่ commit. แพ็กเกจและ logs เก่าทั้งหมดเก็บไว้; แพ็กเกจใหม่ไม่มี eval corpus

รายงานละเอียด: CAUSE_ANALYSIS_TH.md, FULL_GROUND_TRUTH_ANALYSIS_TH.md, INPUT_GUARD_ANALYSIS_TH.md. ผลดิบ/trace อยู่ใน *_details.jsonl; สรุปตรวจสุดท้าย FINAL_VERIFICATION.json

แบบฟอร์มข้อมูลเจ้าของ: `{owner}` มีแบบเดิม 3 ไฟล์ พร้อม addendum 04/05 ที่เพิ่มใหม่โดยไม่ทับแบบเดิม
'''
with (report/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as f:f.write(result)
flow_append=f'''
## ทบทวนจากผลจริงและ Flow ฉบับเสร็จ

1. Baseline 63/280: เพิ่มตัวจับ clause จาก source และแก้ global excludes; Candidate A 257/280
2. ตรวจ Candidate A: final decision ไม่ใช่ final match, macro/customization English source wording, no-answer contract และ oracle ที่ overspec Cypher 3 ข้อ; แก้เป็น v3 โดยเก็บ audit. Candidate B/C 280/280
3. Regression 320/128/80 ผ่าน; unit C 151 ผ่าน. รัน Gold เต็ม 2,000 แล้วพบ dispute resolution 12 ข้อผิดจริง; source presence ตัวตรวจเดิม false failure 47
4. Mask dispute/conflict resolution เฉพาะ display matching. Retest 59 ข้อและ source-grade รวมผ่าน 2,000 ข้อ; ไม่เรียกว่า second full run. Unit D ยังเห็น fixture-clock หลังข้ามวันและเลข source assertion ที่สมมติผิด; snapshot/แก้เฉพาะ testsแล้ว unit E 153 ผ่าน
5. Actual HTTP จำเป็น: direct pipeline ไม่ผ่าน input guard ของเว็บ. รอบแรก 275/280 พบ its false layout 3 และ concurrent busy 2. เพิ่ม English function-word prior; guard scan 4,283 ไม่มี newly blocked. Unit G 154 ผ่าน; ไม่บังคับ l;ylfu ให้ block เพราะก่อน/หลังไม่ block อยู่แล้ว เก็บ diagnostic
6. สร้าง package ใหม่ทุกครั้งและตรวจ app hash ตรง source. รัน HTTP ทีละชุด 648 ผ่าน; worker promotion {promotions} ครั้ง ไม่มี error. หลังเปลี่ยน 8090 ผ่าน 36; test8091หยุดแล้ว

### จุดที่ต้องเพิ่มใน Flow เมื่อพัฒนารอบถัดไป

- ก่อนเริ่ม pipeline ต้องตรวจ input guard ในสภาพ enforce จริง พร้อม raw span scores และ wrong-layout controls. ตรวจประโยคอังกฤษที่มีคำหน้าที่และหลายประเด็น; อย่าใช้ direct pipeline เป็นหลักฐานของทั้งเว็บ
- ดึง expected clauses จาก source/version/hash ก่อนแก้; ตรวจแต่ละประเด็นไม่ใช่เพียง citation. Source presence 2,000 pass ไม่เท่ากับทุกเงื่อนไขครบหรือ owner approval
- ก่อนสรุป semantic failure ให้แยก transport, guard, target/facet, completeness, source conflict/gap และ evaluator error
- เทส fixture ที่ใช้ today/tomorrow ต้อง freeze test clock ให้ตรง fixture; ไม่แก้ runtime ให้รับข้อมูลวันที่ผิด
- ห้ามทดสอบหลายชุดพร้อมกันบน backendหนึ่งตัวเมื่อไม่ได้กำลังตรวจ concurrency. หากจะตรวจ concurrency ต้องมีชุดและเกณฑ์ retry/busy ที่ประกาศแยก
- ต่อไปอ่าน noisy inputs เก่า 36 ข้อ, composites มากกว่า 2 ประเด็น/หลายเลข/หลายเกม, missing age+eligibility และ latency ของ unsupported games. ยังไม่รวมเป็นงานที่ผ่านแล้ว
- Owner pending ระบุคำถามเฉพาะตามแบบ 01–05; ไม่ใช้ OK ของการพัฒนาเป็นการเซ็นรับรองข้อกฎ

### ผลและเอกสาร

ผลสุดท้ายและข้อจำกัด: `{report/'FINAL_RESULTS_TH.md'}`. Verification: `{report/'FINAL_VERIFICATION.json'}`. วิเคราะห์ทุก anchor ที่ผิด: CAUSE_ANALYSIS_TH.md; ชุดใหญ่: FULL_GROUND_TRUTH_ANALYSIS_TH.md; input guard: INPUT_GUARD_ANALYSIS_TH.md

เว็บใช้รุ่น `{health['runtime']['version']}` ที่ http://127.0.0.1:8090/
'''
flow=project/'docs/128_competition_composition_r28_flow_20261001.md'
with flow.open('a',encoding='utf-8') as f:f.write(flow_append)
with (report/'flow_final.md').open('x',encoding='utf-8') as f:f.write(flow.read_text(encoding='utf-8'))
for name in ['FINAL_RESULTS_TH.md','CAUSE_ANALYSIS_TH.md','FULL_GROUND_TRUTH_ANALYSIS_TH.md','INPUT_GUARD_ANALYSIS_TH.md','flow_final.md']:
    assert (report/name).stat().st_size>100
with (root/'r28_completion_record.json').open('x',encoding='utf-8') as f:json.dump({'report':str(report),'flow':str(flow),'owner_forms':str(owner),'package':str(package),'url':checks['ready_url'],'launcher_pid':2976,'scope':'r28 completed; owner confirmations and listed follow-up limitations remain'},f,ensure_ascii=False,indent=2)
print(json.dumps({'report':str(report),'web_verified':36,'sequential_http_verified':648,'unit':154,'worker_promotions':promotions,'protected_unchanged':len(protected_checks),'timings':checks['actual_web']['timings_sec']},ensure_ascii=False))
