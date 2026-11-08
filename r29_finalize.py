import json,hashlib,statistics,ast,urllib.request
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
preflight=json.loads((report/'release_preflight_verified.json').read_text(encoding='utf-8'))
for name in preflight['changed_production_files']:
    ast.parse((project/name).read_text(encoding='utf-8'));assert hashlib.sha256((project/name).read_bytes()).hexdigest()==preflight['changed_production_files'][name]['after_sha256']
protected=json.loads((report/'protected_manifest.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((project/name).read_bytes()).hexdigest()==sha for name,sha in protected.items())
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=5));assert health['runtime']['version']==preflight['runtime_version']
assert json.loads((report/'http_ready_noise36_summary.json').read_text(encoding='utf-8'))['passed']==36
assert json.loads((report/'http_ready_old36.json').read_text(encoding='utf-8'))['passed']==36
records=[]
for name in ['http_noise36_B_details.jsonl','http_composition280_details.jsonl','http_contract320_details.jsonl','http_resolution12_details.jsonl']:
    for r in map(json.loads,(report/name).read_text(encoding='utf-8').splitlines()):
        records.append(float(r.get('elapsed',r.get('elapsed_sec',0))))
records += [r['elapsed_sec'] for r in json.loads((report/'http_old36.json').read_text(encoding='utf-8'))['cases']]
assert len(records)==684
sorted_times=sorted(records);latency={'total':684,'median_sec':statistics.median(records),'p95_sec':sorted_times[int(.95*(len(records)-1))],'max_sec':max(records),'scope':'sequential API suite, mixed static/clarification/layout/live path; not concurrent-user capacity or real booking correctness'}
with (report/'latency_summary.json').open('x',encoding='utf-8') as f:json.dump(latency,f,ensure_ascii=False,indent=2)
flow=(project/'docs/129_input_guard_context_r29_flow_20261002.md').read_text(encoding='utf-8')
flow+='''
## การปรับ Flow หลังทดลองจริง

1. ต้องแยก intentional keyboard layout จาก noisy questions ก่อนนับ false rejection: 36 เดิม = ordinary31 + layout5.
2. Guard-pass → ตรวจ clean/noisy pair → ตรวจเนื้อหาที่ต่าง → เทียบ source clauses/price group/duration/operation/review status. Legacy route-passอย่างเดียวไม่พอ.
3. English guard ใช้ lexical one-edit neighborsเฉพาะ sentence context. Recover task wordใน syntax frameแยกต่างหาก; raw input/ชื่อ/เลขยังอยู่ในlog. Price much/costฟื้นได้หลายspan; eligibility labelsต้องมี independent price/resource/institution context.
4. Full-name mismatchใช้ directory-only suggestionใน explicit role frame: budget≤2, ratio≤.16, runner-up margin≥2. แสดง “หากหมายถึง…” +ชื่อจริง ไม่แทนชื่อผู้ใช้และไม่เลือกเมื่อใกล้หลายคน.
5. Secondary control source noteต้องติดไปกับsource rowsก่อนลดmetadata. ทั้ง structured/vector pathต้องบอกว่าคนยังไม่ได้ตรวจเทียบเครื่องจริง.
6. Live HTTPเปิดLLM/semanticต่างจากdirect regressionที่ปิด; หากคำตอบต่างให้ทดสอบ cleanคู่ใน environmentเดียวกัน. ห้ามผ่อน expectedเพียงให้ผ่าน. Video-policy clean/noisy safe unknownยังมี explanation defectแยกไว้.
7. Package freeze/hash → actualHTTPชุดเดิม+ใหม่แบบ sequential → ตรวจowned process/port → เปลี่ยน8090 → smoke72 → ปิด8091เฉพาะตัวที่สร้าง. เก็บ package/logs/snapshotsเดิม.

## ผลสุดท้าย r29

| การทดสอบ | ผล | สิ่งที่ยืนยันได้ |
|---|---:|---|
| Ordinary noiseเดิม | 31/31ไม่ถูกblock | input guardเปิดทางให้pipeline |
| Intentional layoutsเดิม | 5/5ยังblock | ข้อความขอพิมพ์ใหม่ TH/EN |
| Guard controlsรวม | 100/100 | 36เดิม+64 controls; ไม่ใช่ human traffic |
| Guard regression | 4,283, newly blocked0 | ตัดfalse reject31; เป็นguard-only |
| Unit/regression modules | 168/168 | recovered cues, conditional names, notes, booking fixture,competition/worker |
| Direct clean/noisy | 31/31legacy; เหมือน29คู่ | 62responses; 2คู่ต่างแบบอธิบายได้; clean semanticsยังมีงานต่อ |
| Actual HTTP test port8091 | 684/684ตามcontracts | 280+320+12+36เดิม+36noise/layout; 2liveเคสpath-only |
| หลังเปลี่ยนเว็บ8090 | 72/72 | รุ่นr29บนพอร์ตใช้งาน |
| Preservation | ผ่าน | 9protectedfiles unchanged; snapshotsverified; appตรงpackage; ไม่มีevalในpackage |

684/684 ไม่ใช่การรับรองว่าแชทบอทตอบถูกทุกคำถาม หรือว่าเจ้าของอนุมัติทุกข้อ. 4,283ไม่ได้รันคำตอบทั้งหมด. สถานะจองจริงยังไม่มีoracleตามที่ผู้ใช้พักไว้.

## ลำดับงานต่อจากผลที่พบ

1. P1 ราคาแบบ “1 hour or 2 hours”: รองรับทุกduration alternativeพร้อมผลคำนวณที่ตรวจแยกกัน.
2. P1 คำถามปุ่มเฉพาะ: explicit button matchingต้องชนะgeneric description; ไทยOptionsมีCircleปน/อังกฤษD-Padคืนรายการกว้าง.
3. P1 “need to book to play [game]”: เพิ่มคำตอบว่าต้องเลือกบริการใดจากgame→serviceข้อมูลเดิม หรือclarifyถ้าต้องการขั้นตอน/อุปกรณ์ต่างกัน.
4. P2 ภาษาอังกฤษ safe unknown: แยกข้อมูลต้นฉบับไม่มีจากไม่มีคำแปล; photo/video policyยังรอเจ้าของ.
5. Owner decisions: Tekken pause, RoV6.1.5.1, rulebook/version, English names,controllers,photo/video/public/food policyและfee/ageที่ไม่มีข้อมูล. ใช้แบบฟอร์มเดิม ไม่เดานโยบาย.

หลักฐานรายกรณี: reports/r29_input_guard_context_20261002_005246_30dbb7/DETAILED_CAUSE_ANALYSIS_TH.md และ JSONLก่อน/หลังทุกครั้ง. Runtime: 2026.10.02-input-context-r29-verified. เว็บ: http://127.0.0.1:8090/
'''
with (report/'flow_final.md').open('x',encoding='utf-8') as f:f.write(flow)
(project/'docs/129_input_guard_context_r29_flow_20261002.md').write_text(flow,encoding='utf-8')
summary=f'''# ผลรอบ r29 — input guard และคำถามพิมพ์ผิดหลายจุด

เว็บพร้อม: http://127.0.0.1:8090/ — รุ่น `{preflight['runtime_version']}`

## แก้แล้ว

- ordinary noisy31ข้อที่เคยถูกguardหยุด ผ่านไปตอบได้ทั้งหมด; 5 intentional layoutsยังขอพิมพ์ใหม่.
- คำถามอังกฤษ muc/xost/cot, stydent, Slumni และ bok/ook ในกรอบไวยากรณ์ที่ชัด ฟื้น operation/group/durationถูกจุด. ใช้ระยะedit/บริบท ไม่aliasทั้งคำถาม.
- ชื่อเต็มไทยผิดสองจุดเสนอชื่อจากdirectoryแบบ “หากหมายถึง…” ด้วยชื่อและตำแหน่งจริง; ไม่เขียนทับชื่อผู้ใช้.
- vector control pathรักษาหมายเหตุว่าข้อมูลจากแหล่งรองยังรอคนตรวจเครื่องจริง.

## ผ่านอัตโนมัติ (แยกขอบเขต)

- guard100/100; guard4,283ไม่มี newly blocked. ไม่ใช่ accuracyของคำตอบ4,283ข้อ.
- unit168/168; directclean/noisy31คู่ผ่านlegacy31/31และเหมือน29คู่. สองคู่ที่ต่างคือconditionalname/รูปแบบcontrolsพร้อมnote.
- actualHTTP684/684ตามชุดcontracts; หลังเปลี่ยน8090อีก72/72. รวม2live-noiseเคสทดสอบเฉพาะpath/transport ไม่มีreal booked/freeoracle.
- APIชุด684 median {latency['median_sec']:.3f}s, p95 {latency['p95_sec']:.3f}s, max {latency['max_sec']:.3f}s. เป็นsequential mixed workload ไม่ใช่ผลโหลดหลายคน.
- protected9filesไม่เปลี่ยน; snapshotก่อนแก้ตรวจhashผ่าน; appทุกไฟล์ตรงpackage; packageไม่มีeval.

## ยังพบปัญหา (ไม่ซ่อนในผลผ่าน)

1. ราคา1หรือ2ชั่วโมงยังตอบทางเลือกเดียว.
2. คำถามปุ่มเฉพาะบางข้อยังมีปุ่มอื่นปน/ตอบรายการกว้าง.
3. “ต้องจองอะไรเพื่อเล่นเกมนี้” อาจต้องการบริการที่เลือก แต่ตอนนี้ตอบขั้นตอน.
4. safe unknownอังกฤษบางเส้นทางบอกว่าไม่มีคำแปล ทั้งที่นโยบายต้นฉบับยังไม่มีหลักฐาน.

ประเด็นเหล่านี้พบทั้งclean input จึงไม่ใช่ false rejectionที่r29แก้ และยังไม่นับเป็นsemanticpass. ขั้นต่อไปตามFlowคือduration alternatives→focusedbuttons→bookingresource→source-gapexplanation.

## คน/เจ้าของยังไม่ได้ยืนยัน

กฎTekken pauseที่ขัดกัน, RoVท้ายข้อ6.1.5.1, version/scopeและ104reviewitems, ชื่ออังกฤษทางการ, PS5controllerรายละเอียด, photo/video/public/foodpolicy formalapproval, age/registrationfeesที่ไม่มีข้อมูล. การจองจริงยังพักไว้. ไม่มีการเปลี่ยนนโยบาย/ไฟล์ที่เจ้าของกรอกเพื่อให้testผ่าน.

## หลักฐาน

- `DETAILED_CAUSE_ANALYSIS_TH.md`: สาเหตุ/คำตอบเดิม/คำตอบใหม่/การเลือกrouteของ8เคสเนื้อหาต่าง
- `downstream_changed_cases_analysis.json`: traceก่อน/หลังเต็ม
- `pipeline31_A/B/C_details.jsonl`: ทุก62responseต่อรอบ
- `candidate_C_guard100.json`, `candidate_C_guard_regression4283.json`: guardspans/scores/profile
- `candidate_C_unit.json/log` เก็บผลที่ไม่ผ่านก่อนแก้; `candidate_D_unit.json/log`ผล168/168
- `http_noise36_details.jsonl`: graderครั้งแรกเข้าใจmodeผิด5controlsและพบsafeunknown1ต่างenvironment; `http_safe_unknown_clean_probe.json`พิสูจน์clean/noisyบนเว็บตรงกัน; `http_noise36_B_details.jsonl`ผลแก้graderโดยไม่เปลี่ยนexpected
- `release_preflight_verified.json`, `FINAL_VERIFICATION.json`, `change_audit.json`, `before/`, `changes/`, `git_status_before/after.txt`
- `flow_initial.md`, `flow_final.md`; เอกสารทำงาน `docs/129_input_guard_context_r29_flow_20261002.md`

แพ็กเกจเดิมr28และlogเดิมยังอยู่. ตัวทดสอบ8091หยุดแล้ว; เว็บ8090launcherPID34508พร้อมใช้. ไม่commit/reset/stashไฟล์เดิม.
'''
with (report/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as f:f.write(summary)
final={**preflight,'ready_url':'http://127.0.0.1:8090/','ready_smoke_passed':72,'ready_launcher_pid':34508,'test_launcher_pid_stopped':16504,'latency':latency,'ready_health':health,
       'flow_final_sha256':hashlib.sha256(flow.encode('utf-8')).hexdigest(),'semantic_accuracy_all_queries_claimed':False}
with (report/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(final,f,ensure_ascii=False,indent=2)
with (root/'r29_completion_record.json').open('x',encoding='utf-8') as f:json.dump({'report':str(report),'package':preflight['package'],'runtime_version':preflight['runtime_version'],'url':final['ready_url'],'launcher_pid':34508,'ready_smoke_passed':72},f,ensure_ascii=False,indent=2)
print(json.dumps({'report':str(report),'url':final['ready_url'],'latency':latency,'protected_files':len(protected)},ensure_ascii=False))
