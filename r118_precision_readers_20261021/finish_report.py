"""Compare saved evidence only and write the final candidate review."""
import ast,collections,hashlib,json,statistics
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;S=R/'system';run=R/'http02'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(s) for s in p.open(encoding='utf8')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
done=read(run/'TEST_COMPLETE.json');assert done['complete'] and done['unique_request_keys']==48 and done['grades']==164
assert all(done[k] for k in ['all_selected_keys_recorded','source_code_inputs_unchanged','original_sources_and_results_unchanged','model_identity_verified'])
current=rows(run/'RESULTS.jsonl');jobs=rows(R/'SELECTED_JOBS.jsonl');keys={j['key'] for j in jobs}
assert len(current)==len({r['key'] for r in current})==len(keys)==48 and {r['key'] for r in current}==keys
baselines={'Legacy R64 saved':rows(R/'BASELINE_SCORED_V2.jsonl'),'R115 saved':rows(R/'SAVED_R115_RESULTS.jsonl'),
 'R117 revision03 saved':rows(ROOT/'r117_context_understanding_20261021/http03/RESULTS.jsonl'),
 'R118 revision01':rows(R/'http01/RESULTS.jsonl'),'R118 revision02':current}
all_stats={};by_locale={};by_domain={};maps={}
for version,data in baselines.items():
 m={r['key']:r for r in data};assert set(m)==keys;maps[version]=m
 c=collections.Counter();loc=collections.defaultdict(collections.Counter);dom=collections.defaultdict(collections.Counter)
 for r in current:
  b=m[r['key']];assert b['question']==r['question'];gs=b['grades'];assert len(gs)==len(r['grades'])
  for g,new in zip(gs,r['grades']):assert all(g[k]==new[k] for k in ['file','row','variant','positive_literal'])
  positive=[g for g in gs if g['positive_literal']]
  for target in [c,loc[r['requested_locale']],dom[r['domain']]]:
   target['requests']+=1;target['grades']+=len(gs);target['strict_pass']+=sum(g['passed'] for g in gs)
   target['positive_grades']+=len(positive);target['positive_pass']+=sum(g['literal_passed'] for g in positive)
   target['positive_requests']+=bool(positive);target['positive_requests_all_pass']+=bool(positive) and all(g['literal_passed'] for g in positive)
 all_stats[version]=dict(c);by_locale[version]={k:dict(v) for k,v in loc.items()};by_domain[version]={k:dict(v) for k,v in dom.items()}
checks=[read(R/p) for p in ['PRECISION_CONTRACTS.json','CONTRACT_CHECKS.json','RENDER_REGRESSION.json']]
assert all(x['passed']==x['total'] for x in checks)
protected=read(R/'REFERENCE_HASHES.json');assert all(sha(Path(p))==h for p,h in protected.items())
database_equivalence=read(R/'DATABASE_EQUIVALENCE.json')
assert database_equivalence['schema_equal'] and database_equivalence['all_tables_and_rows_equal']
changes=[]
for p in S.rglob('*.py'):
 old=ROOT/'r117_context_understanding_20261021/system'/p.relative_to(S)
 if not old.exists() or sha(p)!=sha(old):
  ast.parse(p.read_text('utf-8-sig'));changes.append({'file':str(p.relative_to(S)),'sha256':sha(p),'baseline_sha256':sha(old) if old.exists() else None})
write(R/'IMPLEMENTED_FILES.json',changes)
transport=collections.Counter();errors=[]
for e in rows(run/'MODEL_TRANSPORT.jsonl'):
 transport['attempts']+=1;transport['successful_transport']+=bool(e['transport_ok']);transport['failed_transport']+=not e['transport_ok']
 if not e['transport_ok']:errors.append(e)
failures=[{'key':r['key'],'question':r['question'],'answer':r['response']['answer'],
 'literal_failed_grades':sum(g['positive_literal'] and not g['literal_passed'] for g in r['grades']),
 'review':'source_relation_gap' if r['key'].startswith(('1f7c4f9','df43bd')) else 'public_scope_unconfirmed' if r['key'].startswith('e869467') else 'calendar_source_conflict_and_generic_unconfirmed_response' if r['key'].startswith('b32fb6') else 'requires_semantic_review'}
 for r in current if any(g['positive_literal'] and not g['literal_passed'] for g in r['grades'])]
summary={'complete':True,'candidate':'R118 revision03','http_comparison_applies_to':'R118 revision02; revision03 changes only public visibility of FAQ topic field and is verified by saved-plan renderer replay',
 'unique_existing_requests':48,'grades':164,'new_benchmark_questions':0,
 'full_test_run':False,'production_installed':False,'development_http_attempts':96,'contracts_passed':sum(x['passed'] for x in checks),
 'contracts_total':sum(x['total'] for x in checks),'source_database_logically_equal_to_R117':True,'source_database_unchanged_during_each_HTTP_run':True,'protected_R117_files_and_results_unchanged':True,
 'model_identity_verified':True,'stats':all_stats,'by_locale':by_locale,'by_domain':by_domain,'positive_failures':failures,
 'model_transport':dict(transport),'model_transport_errors':errors,'http_ok':sum(r['http_status']==200 for r in current),
 'validation_ok':sum(r['response'].get('validation_ok') is True for r in current),'capture_mismatch':sum(r['capture_body_matches_api'] is False for r in current),
 'latency_median_sec':statistics.median(r['elapsed_sec'] for r in current),'changed_python_files':len(changes),'semantic_accuracy_claimed':False}
write(R/'ANALYSIS_FINAL.json',summary)
def ratio(c,key='positive_pass',den='positive_grades'):
 d=c[den];return f"{c[key]}/{d} ({100*c[key]/d:.2f}%)" if d else 'ไม่มี positive grade'
doc=['# R118 revision03 — ผลการเสริมความเข้าใจ ตัวอ่าน และการตรวจคำตอบ','',
 '## สรุป','','พัฒนาจาก R117 revision04 และตรวจซ้ำด้วยคำถามเดิม 48 keys ผ่าน HTTP API จริง เปิด LLM โดยไม่มี category hints/expected answers ส่งเข้าแชท มีการแก้จากการอ่านคำตอบรายข้อเพิ่มเติมหลัง revision01 จึงมี 96 HTTP attempts รวมสองรุ่น แต่มีคำถามไม่ซ้ำเพียง 48 ข้อ ไม่ใช่ Full ใหม่ และไม่ใช่ชุดสุ่มเพื่อประมาณความถูกต้องทั้งระบบ','',
 'รุ่น HTTP ล่าสุดที่ทดสอบครบคือ revision02 หลังตรวจพบ metadata topic ยังหลุดในคำตอบ จึงมี revision03 เพิ่ม topic ในรายการช่องภายในที่ไม่แสดงต่อผู้ใช้เพียงจุดเดียว ตรวจด้วยการ replay แผนเดิมผ่าน renderer จริง (ไม่เรียก LLM/HTTP ใหม่) และเก็บ source code ของ revision02 ไว้ครบ การเทียบคะแนนในตารางยังติดป้าย revision02 ตรงตามรุ่นที่รัน',
 '','### คะแนนบนคำถามเดียวกัน','','| รุ่น | Positive literal/clause | ข้อที่ผ่าน positive ทุกแถว | Strict compatibility |','|---|---:|---:|---:|']
for version,c in all_stats.items():doc.append(f"| {version} | {ratio(c)} | {ratio(c,'positive_requests_all_pass','positive_requests')} | {ratio(c,'strict_pass','grades')} |")
doc+=['','R117 ที่มีผลครบ 48 keys เปรียบเทียบในตารางคือ revision03; R118 สร้างจาก revision04 ซึ่งมีการตรวจเฉพาะ 8 keys ใน R117 รอบสุดท้าย จึงไม่ติดป้ายผล R117 revision03 ว่าเป็นคะแนน revision04',
 '','**คะแนน literal ไม่ใช่ semantic accuracy** รวมถึงกรณี Part I/Part II ที่ผ่าน keyword ได้จากส่วนที่ตอบ Part I แต่ยังตอบ Part II ไม่ครบ ต้องดูสถานะ partial และส่วนที่ขาดด้วย Strict ยังเทียบ route/mode/contract รุ่นเก่า จึงห้ามแปล strict 0 ว่าคำตอบเนื้อหาผิดทั้งหมด',
 '', 'คะแนน revision01 53/62 ลดเป็น revision02 49/62 จากคำถามศุกร์บ่ายเปิดไหม 4 grades: รุ่นแรกใส่หัวข้อทวนคำถามที่มีคำว่า “เปิด” จึงผ่าน keyword ทั้งที่ข้อความจริงยังตอบว่าไม่มีข้อมูลยืนยัน รุ่นหลังตัด general-style task ออกจึงไม่ทวนคำถามและไม่ผ่านคำเหล่านั้น ไม่ใช่หลักฐานว่าเนื้อหาที่เคยยืนยันถูกหายไป และไม่เพิ่มคำ keyword กลับเพื่อเอาคะแนน ตารางวันศุกร์มี open_periods=conflicted จริง แต่ข้อความ no-confirmation ยังอธิบายเหตุผลนี้ไม่ดีพอ เป็นจุดที่ต้องเสริมต่อ ดู CASEBOOK_TH.md',
 '', 'Legacy R64 ใช้ source data และกฎราคาคนละรุ่นกับ candidate จึงไม่ใช่ causal comparison ของ Flow ล้วน ๆ ไม่มีการรัน baseline ใหม่',
 '', '### แยกภาษา','','| ภาษา | Legacy R64 | R115 | R117 revision03 | R118 revision02 |','|---|---:|---:|---:|---:|']
versions=['Legacy R64 saved','R115 saved','R117 revision03 saved','R118 revision02']
for loc in ['th','en','auto']:doc.append('| '+loc+' | '+' | '.join(ratio(by_locale[v].get(loc,{'positive_grades':0})) for v in versions)+' |')
doc+=['','## สิ่งที่แก้และตรวจยืนยันจาก source','','1. R2 ของ God of War Ragnarök อ่าน Heavy Attack/Heavy Runic Attack จากคอลัมน์ R2 ไม่เลือก R3 Lock-On',
 '2. ยกเลิกจองผูกหัวข้อ customer cancellation ได้ เก็บเงื่อนไขอย่างน้อย 1 ชั่วโมงจาก source แยกจาก studio cancellation/penalty/refund',
 '3. ค้น role→person ได้ แต่ไม่คืนชื่อเมื่อ public_scope ไม่ยืนยัน ข้อความระบุว่าพบ source แล้วแทนการบอกเหมือนไม่มีข้อมูล',
 '4. Part I / Part II แยกเป็นสองชื่อ ชื่อไม่ระบุ Remastered จะไม่ใช้ฉบับ Remastered แทน ตอบ Part I และบอกขาด Part II',
 '5. เช็กอินก่อนเล่นเกมต้องอ่านขั้นตอน C08 ไม่ตอบ service catalogue ของเกม',
 '6. map pool ในกติกา CS2 ต้องอ่าน clause ของการแข่งขัน ไม่ตอบคำอธิบายเกม เพิ่ม bilingual topic bridge โดยไม่ฝังรายชื่อแผนที่ในโค้ด',
 '7. วิธีจองต้องอ่าน booking_steps ที่มี source ไม่ติด entity_not_bound เพราะคำถามใช้ถ้อยคำทั่วไป',
 '8. รุ่น GPU ใน PCs ผูกจากชนิดอุปกรณ์ pc และช่อง specifications.GPU คืนค่าที่บันทึกไว้โดยไม่สร้างสเปกใหม่',
 '9. คำเกริ่นที่เป็น general task ว่าง เช่น กำลังวางแผนไปใช้บริการ/รบกวนเช็กข้อมูล ไม่ถูกแยกเป็นคำถามธุรกิจเพิ่ม โดยไม่ตัด factual clause/constraints',
 '10. FAQ ไม่แสดง topic/intent_key/scope_note/คำถามตั้งต้นเป็นคำตอบลูกค้า แต่คงสถานะและหลักฐานใน audit; topic ตรวจยืนยันด้วย renderer replay หลัง HTTP revision02',
 '11. คง explicit facets ของ typed reader และตรวจตัวตน/หลักฐานหลังเลือก; all controls ยังได้ครบ scoped source set',
 '12. เก็บสมาชิก catalog เป็น game IDs ไม่ซ้ำสำหรับ operator list/count/group; รอบ HTTP นี้ยังไม่ได้วัดคุณภาพ natural-language count เป็นเปอร์เซ็นต์',
 '', '## สิ่งที่ยังขาดและความผิดที่คะแนนไม่บอกทั้งหมด','','อ่านรายงาน `02_SOURCE_GAPS_TH.md` ประกอบ: snapshot มี person 25 รายที่ public_scope unknown, rate 18 จาก 24 รายยังไม่มี calculation_rule ยืนยัน และเกมที่มีบริการยืนยัน 19 จาก 42 เกมยังไม่มีเส้นทางถึงโซนที่ยืนยันได้',
 '', '- Nintendo/VR บางบริการไม่ทราบ resource_ids จึงตอบบริการที่มีเกมได้ แต่ยืนยันโซนไม่ได้ ไม่เติม relation จากความคล้ายของชื่อ',
 '- การคำนวณระยะเวลาที่ไม่ได้ประกาศสูตรยังให้ unit rate พร้อมข้อจำกัด ไม่อ้างยอดรวม; ถ้า interpreter พลาด audience อาจยังแสดงหลายกลุ่ม ต้องเสริม alias/slot completeness โดยยึด source',
 '- ชื่อบุคคลภาษาอังกฤษที่ source มีเพียงภาษาไทยยังจับไม่ได้บางราย และ public_scope ก็ยังต้องยืนยันแยกกัน',
 '- คำเรียกอุปกรณ์ภาษาไทย/พิมพ์ผิดบางแบบยังจับเป้าหมายไม่ได้ แม้มีอุปกรณ์อยู่ใน source',
 '- คำถามกว้างเรื่องบทลงโทษอาจเลือกได้เพียง clause บางส่วน ต้อง review parent/child scope และความครบถ้วน ไม่ถือว่าทุกย่อหน้าถูกครอบคลุมแล้ว',
 '- คำถามราคาเกมที่ต้องไปผ่านหลายบริการ/หลาย duration อาจยังถาม slot ไม่เฉพาะเจาะจงพอ',
 '- physical video recording กับ in-game capture เป็นคนละ predicate; source แบบหนึ่งไม่อนุญาตให้อ้างสิทธิ์อีกแบบ',
 '- schedule มี open_periods ขัดแย้ง; ไม่อนุมานเปิด/ปิดจาก bookable/maintenance และไม่ใช้ provider ที่ตั้ง unavailable ใน test เป็นสถานะจริง',
 '- compare/recommendation หลายเงื่อนไขและ paraphrase ที่ยังไม่ผูก target ไม่ได้ถือว่าแก้ครบ',
 '', '### Positive literal ที่ยังไม่ผ่าน','','| คำถาม | Failed grades | การจำแนกหลังดู source |','|---|---:|---|']
for f in failures:doc.append(f"| {f['question']} | {f['literal_failed_grades']} | {f['review']} |")
doc+=['', 'กลุ่มข้างบนไม่ได้ถูกนับทั้งหมดเป็น actual content failure: สองคำถามขาดความสัมพันธ์โซนใน source อีกคำถามถูก public-scope guard และคำถามวันศุกร์มีเวลาเปิดขัดแย้งพร้อมปัญหาข้อความตอบกว้างเกินไป ส่วนการตอบครบความหมายของคำถามอื่นยังต้องอ่าน casebook ไม่ใช่สรุปจาก keyword pass',
 '', '## การตรวจและข้อจำกัดการทดลอง','', f"- Contract checks: {summary['contracts_passed']}/{summary['contracts_total']} (แยกเป็น operator/source guards และสัญญา R117 เดิม)",
 f"- HTTP {summary['http_ok']}/48; validation_ok {summary['validation_ok']}/48; capture mismatch {summary['capture_mismatch']}",
 f"- Model transport: {dict(transport)}; median latency {summary['latency_median_sec']:.2f}s",
 '- ตรวจรุ่นและ digest ของ scb10x/typhoon2.5-qwen3-4b:latest ก่อน–หลัง; transport/schema/ความถูกต้องเป็นคนละชั้น',
 '- candidate source และ inputs ไม่เปลี่ยนระหว่างรัน; R117/ผลเก่าที่ป้องกันไว้ไม่เปลี่ยน; schema และข้อมูลทุกแถวใน DB ทั้ง 15 ตารางเท่ากับ R117 revision04 โดยตรวจ read-only ส่วน byte hash ของ SQLite file ต่างกันหลัง SQLite backup จึงไม่อ้างว่าไฟล์เหมือนกันทุก byte ดู DATABASE_EQUIVALENCE.json',
 '- revision01/02 เก็บ source code ที่รันไว้ใน http01/FROZEN_SYSTEM และ http02/FROZEN_SYSTEM พร้อม ARCHIVED_CODE_VERIFIED.json; system เป็น revision03 ซึ่งเปลี่ยนการซ่อน topic เพียงจุดเดียว ดู RENDER_REGRESSION.json',
 '- เปิด LLM หมายถึง Flow เลือกใช้ตามงาน ไม่ได้หมายถึง LLM สร้างคำตอบทุกคำถาม',
 '- baseline เป็น saved results; 48 keys นี้เคยใช้พัฒนาแล้ว ไม่ใช่ holdout หรือหลักฐานว่าคะแนน Full เท่ากัน',
 '', '## เอกสารและหลักฐาน','','- [แผน Flow และการทบทวน](01_FLOW_AND_REVIEW_TH.md)',
 '- [ช่องว่างของ source](02_SOURCE_GAPS_TH.md)','- [ทุกคำตอบและก่อน–หลัง](CASEBOOK_TH.md)',
 '- [ตัวเลขผลวิเคราะห์](ANALYSIS_FINAL.json)','- [source contracts](PRECISION_CONTRACTS.json)','- [R117 contracts](CONTRACT_CHECKS.json)',
 '- [HTTP latest completion](http02/TEST_COMPLETE.json)','- [HTTP latest raw](http02/RESULTS.jsonl)','- [การตรวจ renderer รุ่นสุดท้าย](RENDER_REGRESSION.json)','- [ความเท่ากันของข้อมูล SQLite](DATABASE_EQUIVALENCE.json)','- [ไฟล์โค้ดที่แก้](IMPLEMENTED_FILES.json)',
 '', 'Candidate R118 ยังไม่ติดตั้งทับ R78 และไม่ใช่การประกาศว่าแก้ครบทุกหมวดแล้ว']
(R/'REPORT_TH.md').write_text('\n'.join(doc),'utf8')
casebook=['# R118 — Casebook ก่อน–หลังทุก 48 keys','','คำตอบ R115/R117/R118 จาก saved logs; ไม่เรียก baseline ใหม่ คะแนน literal ไม่ทดแทนการอ่าน source/สถานะ partial','']
for i,r in enumerate(current,1):
 casebook += [f"## {i}. {r['question']}",'',f"Key: `{r['key']}`; locale `{r['requested_locale']}`; original domain `{r['domain']}`",'']
 for version in ['R115 saved','R117 revision03 saved','R118 revision02']:
  b=maps[version][r['key']];casebook += [f'### {version}','','```text',b['response'].get('answer',''),'```','']
 art=r['response'].get('decision_artifact') or {}
 details={'understanding':art.get('understanding'),'need_results':art.get('need_results'),'sources':r['response'].get('sources'),'positive_contracts':[g for g in r['grades'] if g['positive_literal']]}
 casebook += ['### แผน ขอบเขต source และเกณฑ์','','```json',json.dumps(details,ensure_ascii=False,indent=2),'```','']
(R/'CASEBOOK_TH.md').write_text('\n'.join(casebook),'utf8')
final_hashes={str(p.relative_to(S)):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm'))}
write(R/'FINAL_SYSTEM_HASHES.json',final_hashes)
status={k:v for k,v in summary.items() if k in ['complete','candidate','unique_existing_requests','grades','new_benchmark_questions','full_test_run','production_installed','development_http_attempts','contracts_passed','contracts_total','source_database_logically_equal_to_R117','model_identity_verified']}
status.update(phase='complete',completed_at=datetime.now().astimezone().isoformat(),latest_run='http02',report='REPORT_TH.md',flow='01_FLOW_AND_REVIEW_TH.md')
write(R/'STATUS.json',status)
print(json.dumps({'stats':all_stats,'contracts':status,'model_transport':dict(transport)},ensure_ascii=False))
