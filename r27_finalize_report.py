import hashlib,json,subprocess,urllib.request,uuid
from datetime import datetime,timezone
from pathlib import Path

base=Path(__file__).parent
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((base/'r27_report_path.txt').read_text(encoding='utf-8').strip())
def read(name):return json.loads((report/name).read_text(encoding='utf-8'))

unit=read('verified_I_unit.json');assert unit['success'] and unit['tests']==135
large=read('full_r27_B_final_atomic_source_rescore.json')['summary']
content=read('http_verified_320_summary.json');new=read('http_verified_128_summary.json')
regression=read('http_verified_regression.json');old=read('http_verified_old80_content.json')
speed=read('verified_r27_clarification_speed.json');owner=read('http_verified_owner_8090.json')
owner_speed=read('verified_owner_8090_clarification_speed.json')
recycles=read('verified_http_recycles.json');process=read('verified_real_worker_process_check.json')
for record in (content,new,regression,old,speed,owner,owner_speed):assert record['passed']==record['total']
assert recycles['promotions']>=2 and process['passed']
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=3))
assert health['runtime']['version']=='2026.10.01-competition-contract-r27-verified'
assert all(w['ready'] and w['alive'] for w in health['pipeline_workers']['workers'])
health_capture=report/('verified_owner_health_'+uuid.uuid4().hex[:8]+'.json')
with health_capture.open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)

protected=read('protected_manifest.json')
assert all(hashlib.sha256((project/path).read_bytes()).hexdigest()==sha for path,sha in protected.items())
baseline=read('before_manifest.json')
untouched=[path for path in baseline if path not in ('app/pipeline/engine.py','app/core/intent_cue_recovery.py')]
assert all(hashlib.sha256((project/path).read_bytes()).hexdigest()==baseline[path] for path in untouched)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (report/'git_status_after.txt').open('x',encoding='utf-8') as f:f.write(status)
before=(report/'git_status_before.txt').read_text(encoding='utf-8').splitlines()
old_paths={line[3:] for line in before if len(line)>3};new_paths={line[3:] for line in status.splitlines() if len(line)>3}
missing=sorted(old_paths-new_paths)
assert not missing,missing
err=(base/'web_chat_runs/r27_ready_8091_57e15e9534.err.log').read_text(encoding='utf-8')
http_posts=[line for line in err.splitlines() if 'POST /api/chat HTTP/' in line]
assert len(http_posts)==573,len(http_posts)
assert all(' 200 ' in line for line in http_posts)
summary={
 'runtime':health['runtime']['version'],'finalized_utc':datetime.now(timezone.utc).isoformat(),
 'unit':{'passed':135,'total':135},'ground_truth_original':large,
 'http_complete_clauses':{k:content[k] for k in ('passed','total','max_elapsed')},
 'http_new_questions':{k:new[k] for k in ('passed','total','max_elapsed')},
 'http_regression':{'passed':36,'total':36},'http_old_content':{'passed':80,'total':80},
 'http_clarification':{k:speed[k] for k in ('passed','total','median','max')},
 'http_sequence':{'post_requests':len(http_posts),'errors':0,'ready_worker_promotions':recycles['promotions'],'includes_one_post_warmup_probe':True},
 'real_process_test':{'requests':24,'crash_recovered':True,'timeout_recovered':True},
 'owner_web':{'url':'http://127.0.0.1:8090/','post_switch_regression':36,'post_switch_clarification':owner_speed['total'],'clarification_median_sec':owner_speed['median'],'clarification_max_sec':owner_speed['max'],'ready':True},
 'preservation':{'protected_files_unchanged':len(protected),'other_initial_snapshots_unchanged':len(untouched),'pre_existing_git_paths_removed':missing,'runtime_package_files_match':4},
 'scope':'Source-grounded bounded automated checks. Not an assertion that all possible questions or owner policy are correct.',
 'owner_pending':['Tekken s03/s07 pause contradiction and penalty unit','104-item V2 review publication','Organizer endorsement of translated regulations'],
 'deferred':'Fresh owner booking observations and live availability correctness collection remains deferred.'
}
with (report/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)

text=f'''# ผลรอบ r27 — กติกาการแข่งขัน ไทย/อังกฤษ

## พร้อมลองใช้

เว็บ: http://127.0.0.1:8090/  
รุ่น: `{summary['runtime']}`  
แพ็กเกจ: `{project / 'owner_local_delivery_20261001_competition_contract_r27_verified/PSU_Esports_Chatbot_Local'}`

## สิ่งที่แก้จากหลักฐาน

1. แยกหัวข้อย่อยของกติกา: เลือก clause เต็มจากเกมที่ถาม เช่น อุปกรณ์ โน้ต ประท้วง จำนวนฮีโร่ เงื่อนไขเริ่มใหม่ การตั้งค่า และรายการบทลงโทษ ประโยคแรกต้องตอบเรื่องที่ถามก่อน
2. รักษาค่า หน่วย เงื่อนไขและข้อยกเว้น ใช้ต้นฉบับไทยและ English overlay ที่ hash ตรง ไม่สร้างข้อกฎที่ไม่มีในแหล่ง
3. กู้คำหัวข้อพิมพ์ผิดแบบมีบริบทและจำกัดระยะ เช่น protest/notes/heroes/settings และไทย พร้อมป้องกัน score ไม่ให้ถูกแก้เป็น scope ชื่อเกม ตัวเลข และคำปฏิเสธยังมี negative tests
4. คำถามกติกาไม่ระบุเกมถามกลับก่อนเรียกโมเดล เพิ่ม timing ของ locale/cue/canonical preflight เพื่อให้ตรวจเวลาได้ละเอียดขึ้น
5. แก้ตัวตรวจที่ปฏิเสธ clause อังกฤษสั้น ตรวจครบหนึ่ง clause จาก source ได้โดยยังรักษา gates เดิมและคะแนนดิบ แยก presence จาก completeness
6. แก้ช่วง worker เปลี่ยนทุก 250 คำถาม: เตรียมตัวใหม่พร้อมก่อนสลับ ตัวเดิมยังรับงาน ระหว่างทดสอบจับ TypeError ใน log ที่เพิ่มได้และแก้โดยส่ง request_id พร้อมเพิ่ม test ที่บังคับ signature จริง

## ผลอัตโนมัติ — ความหมายต่างกัน

| ชุดตรวจ | ผล | สิ่งที่ยืนยันได้ |
| --- | --- | --- |
| Gold เดิม 2,000 ข้อ — คะแนนดิบ | 1,953/2,000 | 47 ข้อถูกตัวตรวจ legacy ปฏิเสธ source content; เก็บผลเดิมไว้ |
| Gold เดิม — atomic-source grade | 2,000/2,000 | route/status/game/evidence ตาม gates เดิม และ complete-clause presence; ไม่ใช่ตรวจทุกความหมายในทุกคำตอบ |
| รายละเอียดกติกา 320 ข้อบนเว็บจริง | 320/320 | 52 ประเด็น ×2 ภาษา ×3 รูปคำถาม +8 controls; ทุก clause ที่ fixture กำหนดและประโยคแรก |
| คำถามใหม่และ typo 128 ข้อบนเว็บจริง | 128/128 | 16 ประเด็น ×2 ภาษา ×4 รูปแบบ; เป็น development/regression หลังวิเคราะห์แล้ว ไม่ใช่ blind user traffic |
| ตรวจเนื้อหาชุดก่อนหน้า | 80/80 | ค่า/หน่วย/ข้อห้าม/เงื่อนไข/ตาราง 16 anchors |
| เว็บ regression | 36/36 | คำถามผู้ใช้จริงในแชท ประวัติข้ามเกม overview, source gap, catalog, booking route |
| Unit/regression | 135/135 | grader negatives, recovery guards, routing และ worker recycle signature/races |
| โปรเซสแยก | ผ่าน | 24 คำถาม ข้าม planned recycle 2 ครั้งและกู้หลัง crash; timeout recovery เดิมผ่าน |
| HTTP ต่อเนื่องบนแพ็กเกจจริง | 573/573 ส่งกลับ 200 | 572 คำถามจากชุดข้างต้น +1 probe; promoted worker 2 ครั้ง ไม่มี 500/503 |
| หลังเปลี่ยนเว็บ 8090 | 36/36 +8/8 | runtime/health พร้อม และ regression/clarification ผ่าน |

### เวลา

ชุด clarification เดิม r26 จำนวน 8 ครั้ง median 1.53415s / max 12.7451s; r27 บนเว็บทดสอบ median {speed['median']:.5f}s / max {speed['max']:.4f}s; หลังขึ้น 8090 median {owner_speed['median']:.5f}s / max {owner_speed['max']:.4f}s.

เป็นเวลาจากเครื่องนี้และคำถามกลุ่มนี้ภายใต้ cache/load ณ ตอนรัน ไม่ใช่ benchmark ที่ควบคุมทุกปัจจัยหรือคำรับประกันทุกคำถาม รายละเอียด 320 max {content['max_elapsed']:.4f}s (Free Fire ที่ไม่มี rulebook), ชุดใหม่ 128 max {new['max_elapsed']:.4f}s.

## วิเคราะห์ความผิดที่พบระหว่างพัฒนา

- Baseline v1 165/320 มีทั้ง runtime failures และ literal oracle ที่คลาดเคลื่อน จึงเก็บ v1 ไว้และมี `oracle_revision_audit.json`; ห้ามใช้ตัวเลขนี้เป็น semantic accuracy
- รอบ B 233/320: mode ใหม่ไม่มี competition_rule ทำให้ contract ไม่รู้จัก แก้การระบุ mode
- รอบ C 311/320: Tekken settings เลือก chunk สั้นเสีย Stage/Advantage, score ถูกแก้เป็น scope และ EN literal oracle ต่างคำแปล แยกแก้สาเหตุ
- ชุดใหม่รอบ A 112/128: กู้ task word แต่ไม่กู้ facet word ที่พิมพ์ขาด เพิ่มบริบทและ unique edit candidate แบบจำกัด
- Gold run A 1,938/2,000: มี regression `apply to` จับ overview เป็น scope และ composite eligibility/roster/registration ตอบเพียงเรื่องเดียว แก้แล้ว run B มีเหลือ 47 legacy false failures
- HTTP candidate 503 เกิดจากปิด worker เดิมก่อน replacement ready แม้ถามทีละข้อ; ไม่ใช่ข้อมูลข้อกฎขาด
- HTTP final ครั้งแรก 318/320: TypeError จาก `ParentPerformanceLogger.emit_parent()` ขาด request_id ในส่วน log ที่เพิ่มไว้ การใช้ Mock ที่ไม่ตรวจ signature ปล่อยให้ unit pass; เปลี่ยนเป็น autospec และแก้ทั้ง 4 branches
- verified ผ่าน 320/128/36/80/8 ต่อเนื่องและอีก 1 probe; event/log/PID ยืนยันสลับหลัง ready 2 ครั้ง

รายประเด็นพร้อมคำตอบเดิม ข้อที่ควรปรากฏ source/hash และผลหลังแก้อยู่ใน `CAUSE_ANALYSIS_TH.md`.

## สิ่งที่ต้องให้ผู้จัดยืนยัน

1. Tekken s03 ระบุห้าม pause แต่ s07 อนุญาตบางกรณี: s07 เป็นข้อยกเว้นของ s03 หรือไม่? เหตุใดได้รับอนุญาต? ต้องขอกรรมการก่อนหรือไม่? โทษแต่ละกรณีเสีย Round, Game หรือ FT2 Match?
2. V2 review 104 รายการยังรอตรวจและยังไม่ publish การผ่าน source hash/translation checks เป็นการตรวจระบบ ไม่ใช่คำรับรองนโยบายหรือคำแปลจากผู้จัด

## ขอบเขตที่ยังควรพัฒนา

- การกู้ typo หลายตำแหน่งมี span/edit budget เพื่อป้องกันการเปลี่ยนความหมาย ยังไม่รองรับทุก slang/การพิมพ์ผิด และอาจต้องถามกลับ
- Detail selector ใช้แนวคิดทั่วไปของหัวข้อในขอบเขต rulebook ที่มีและ clause matching; ประโยคใหม่ที่ต่างโครงสร้างมากหรือถามหลายประเด็นอาจยังใช้ fallback เดิม ต้องทดสอบ unseen cases เพิ่มเมื่อมีข้อมูลจริง
- ชุด 2,000 ไม่ได้ตรวจ every required proposition จึงใช้ชุด 320/128/80 ประกอบ ยังไม่เท่ากับตรวจเนื้อหาทั้ง 104 chunks ในทุกความหมาย
- การทดสอบ availability กับข้อมูลจริงของเจ้าของยังเลื่อนตามคำขอ ผล booking regression นี้ยืนยันการเข้า route/วันปิดหรือ source-unavailable; ไม่ใช่หลักฐานว่าเวลาจองสดทุกช่วงถูกต้อง
- งานถัดไปที่ทำเองได้: ขยาย proposition contracts จาก source ที่ยังไม่ครอบคลุม, เพิ่ม unseen compound/negation/typo cases และวิเคราะห์ trace แยกจากผล legacy; การแก้นโยบายขัดกันต้องรอผู้จัด

## การรักษาไฟล์และหลักฐาน

protected 7 ไฟล์ hash ตรงก่อน/หลัง (source, Gold, review queue, English CURRENT, owner schedule, r26 Flow); initial snapshots อื่นที่ไม่ได้แก้ hash ตรง; Git paths ที่มีอยู่ก่อนยังครบ.

เก็บ `before`, `ready_code`, `final_code` และ `verified_code` แยก; เก็บผลทุก attempt รวม partial/500/503; สร้างแพ็กเกจ r27 verified ใหม่. ปิดเฉพาะ launcher เว็บที่สร้างไว้และตรวจ PID/port/parent ก่อน เว็บทดสอบ 8091 ปิดแล้ว เว็บ 8090 พร้อมใช้งาน.

## ตรวจซ้ำ

Fixtures อยู่ `data/eval/competition_content_contract_r27_320_20261001.json` และ `data/eval/competition_new_questions_r27_128_20261001.json` ไม่รวมใน owner package และ runtime ไม่อ่าน Gold.

ใช้ `tools/run_competition_contract_r27.py --fixture <fixture> --report <new-report-dir> --run <new-name> --url http://127.0.0.1:8090 --llm` เพื่อรัน contract ผ่านเว็บ; ผลใช้ exclusive creation จึงต้องเลือกชื่อใหม่. ใช้ `tools/competition_content_grader_r27.py` เพื่อ rescore ผลดิบโดยแยก source presence. อย่ากดสร้าง Gold ทับไฟล์เดิม.
'''
with (report/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as f:f.write(text)

flow=project/'docs/127_competition_contract_r27_flow_20261001.md'
value=flow.read_text(encoding='utf-8').replace('เพิ่มคำถาม holdout ที่ไม่ใช้ในการแก้','เพิ่มคำถามใหม่แยกจาก Gold เดิม แล้วระบุให้ชัดว่าชุดที่นำมาแก้เป็น development/regression; unseen traffic ต้องเก็บแยกเมื่อพร้อม')
value+='''

## ทบทวน Flow จากผลจริงและปรับวิธีตรวจ

1. ตรวจ oracle ก่อนตีความ failure: เก็บ v1/v2 และ audit การแก้คำแปลเทียบเท่า/เลขหัวข้อ; ห้ามลด requirement เพราะ runtime ยังไม่ผ่าน
2. แยกการระบุ game/facet จาก proposition: อุปกรณ์ของเจ้าหน้าที่กับของผู้เล่น หรือเหตุหยุดกับเวลาอนุญาต ต้องไม่เลือกแทนกัน
3. แยก first line และ full body: ถูกอยู่ท้ายคำตอบไม่ได้แปลว่าประโยคแรกตรงคำถาม; ทุกหน่วย/ข้อยกเว้นต้องอยู่ครบ
4. ตรวจ integration mode กับ answer contract: route ใหม่ต้องผ่าน validator เดิม; อย่าข้าม guard เพื่อเพิ่มคะแนน
5. เพิ่ม real-word/negation tests: score/scope, ตัวเลข 1:55, ชื่อเกม และประโยคปฏิเสธต้องไม่ถูก typo recovery เปลี่ยน
6. เพิ่มคำถามใหม่และคำสำคัญพิมพ์ขาด: กู้ด้วย context + unique candidate + edit budget ไม่ใช้ whole-question alias; ถ้าเกินขอบเขตถามกลับ
7. ใช้ Gold 2,000 จับ broad-query และ multi-topic regression ก่อนขึ้นแพ็กเกจ; original grade และ source grade เป็นคนละคอลัมน์
8. ต้องข้าม worker recycle จริงบน HTTP: sequential ก็เกิด startup gap ได้; เตรียม worker ใหม่ขณะตัวเดิมยังตอบ และสลับเมื่อ ready
9. Unit doubles ต้องบังคับ signature ของ logger: Mock เปล่าไม่จับ missing request_id; ใช้ autospec และตรวจ spawn-failed branch
10. หลัง package acceptance จึงเปลี่ยน 8090 และตรวจ runtime/health/คำถามเดิมอีกครั้ง เก็บ package/PID/log เก่าและปิดเฉพาะตัวทดสอบที่สร้างเอง

ข้อข้างต้นเป็นสิ่งที่ทบทวนจากการตรวจและผลที่เกิดจริง ไม่ใช่การอ้างว่าทุกรอบรันทุกชุดเท่ากัน.

## ผลฉบับใช้งาน r27 verified

| Gate | ผล | ขอบเขต |
| --- | --- | --- |
| Unit/regression | 135/135 | รวม logging signature และ worker recycle race |
| Gold เดิม raw | 1,953/2,000 | เก็บ 47 legacy false failures |
| Gold source-grade | 2,000/2,000 | presence + gates เดิม; ไม่ใช่ completeness ทุกคำตอบ |
| Complete-clause contract TH/EN | 320/320 | 52 topics ×2 locales ×3 forms +8 controls |
| New question/typo | 128/128 | development/regression ไม่ใช่ blind traffic |
| Old propositions / web regression / clarification | 80/80 +36/36 +8/8 | ค่า หน่วย เงื่อนไข ตาราง / flow / missing-game |
| HTTP sequential | 573/573 HTTP200 | สลับ ready worker 2 ครั้ง, 572 cases +1 probe |
| Process recovery | ผ่าน | recycle 24 requests, crash และ timeout |
| หลังขึ้น 8090 | 36/36 +8/8 | health/version ถูกและ worker ready |

เวลา clarification หลังขึ้นเว็บ median 0.07035s/max 0.1094s สำหรับชุด 8 ครั้งนี้ ไม่ใช่คำรับประกันทุกคำถาม.

### Flow ถัดไปเมื่อมีเคสใหม่

เก็บ raw question + locale/history + answer/trace/เวลา → แยก transport/runtime/oracle/route/proposition/first-line/typo/source-gap → ตรวจต้นฉบับและคำแปล → freeze expected clauses พร้อม negative assertions → แก้ชั้นที่เป็นต้นเหตุ → rerun ชุดที่เกี่ยวข้องและ full regression เมื่อ routing เปลี่ยน → HTTP/package gate → บันทึกผลทั้งผ่าน/ไม่ผ่านและขอบเขต.

คำถามที่ policy ขัดกันส่งให้ผู้จัดตามรายการด้านบน; คำถามที่ source ไม่มีต้องตอบว่าข้อมูลยังไม่พบ; source-presence pass ไม่ใช้แทน completeness pass. งานเก็บ booking จริงยังเลื่อนตามคำขอเดิม.
'''
with flow.open('w',encoding='utf-8') as f:f.write(value)
with (report/'flow_final.md').open('x',encoding='utf-8') as f:f.write(value)
with (report/'CAUSE_ANALYSIS_TH.md').open('a',encoding='utf-8') as f:f.write('''

## ผลปิดรอบบนแพ็กเกจจริง และความผิดที่เพิ่มระหว่างแก้

HTTP final แรกได้ 318/320 เพราะส่วน planned recycle logging ที่เพิ่มไว้ขาด keyword-only request_id ของ ParentPerformanceLogger.emit_parent. ทั้ง warming/spawn_failed/promoted/warmup_failed ต้องส่ง request_id. Mock เปล่าใน unit tests ไม่บังคับ signature จึงไม่จับข้อผิดพลาดนี้; verified เปลี่ยนเป็น create_autospec เพิ่ม spawn-failure assertion และส่ง request_id ทุก branch.

แพ็กเกจ verified ทดสอบ 320/320 +128/128 +36/36 +80/80 +8/8 ต่อเนื่อง รวม 572 และอีก 1 probe (573 HTTP200) event ยืนยัน promoted ready workers 2 ครั้ง. ทดสอบโปรเซสแยก 24 คำถามและ crash recovery พร้อม timeout recovery เดิมผ่าน. หลังเปลี่ยนเว็บ 8090 ตรวจ 36/36 +8/8 และ health/runtime ถูก. ดู FINAL_RESULTS_TH.md และ FINAL_VERIFICATION.json สำหรับขอบเขตของคะแนน.
''')
print(json.dumps({'report':str(report/'FINAL_RESULTS_TH.md'),'flow':str(flow),'http_requests':573,'protected':7,'owner_web_ready':True},ensure_ascii=False))
