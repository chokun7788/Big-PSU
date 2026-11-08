"""Read saved raw outputs only. Serialization is not answer correctness."""
import collections,hashlib,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r129_full_plan_completion_20261024'
path=P/'three_arm02/RESULTS.jsonl';rows=[json.loads(s) for s in path.read_text('utf8').splitlines()]
assert len(rows)==330 and len({(r['arm'],r['key']) for r in rows})==330
arms={};samples={}
for arm in ['base','retained','new']:
 rs=[r for r in rows if r['arm']==arm];assert len(rs)==110
 parseable=0
 for row in rs:
  try:json.loads(row['raw_output']);parseable+=1
  except ValueError:pass
 arms[arm]={'requests':110,'json_parseable':parseable,'runtime_wire_accepted':sum(bool(r['raw_metrics']['schema_ok']) for r in rs),'actual_model_identity_verified':sum(bool(r.get('identity_verified')) for r in rs),'raw_semantic_accuracy':None}
 samples[arm]=[{k:r.get(k) for k in ['key','question','raw_output','wire_version','protocol_error','provenance']} for r in rs[:2]]
stage=collections.defaultdict(collections.Counter);selector_examples=[];request_log=P/'model_1792867147669903000/REQUESTS.jsonl'
with request_log.open(encoding='utf8') as f:
 for line in f:
  try:row=json.loads(line)
  except ValueError:continue # A live trailing write is not a transport failure.
  name=row.get('provenance',{}).get('stage','unknown')
  try:json.loads(row.get('raw_output',''));parsed=True
  except ValueError:parsed=False
  stage[name]['observed_calls']+=1;stage[name]['json_parseable']+=int(parsed)
  if name=='evidence_selection' and len(selector_examples)<3:selector_examples.append({'json_parseable':parsed,'raw_output':row.get('raw_output','')[:2500],'provenance':row.get('provenance')})
result={'saved_raw_only':True,'new_inferences':0,'baseline_answers_regraded':False,'candidate_runtime_modified':False,'all_330_saved_rows_read':True,'raw_file_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'arms':arms,'samples':samples,'observed_live_log_stages_not_final':dict(stage),'selector_samples':selector_examples,'source_execution_review_still_required':True,'semantic_accuracy_not_inferred_from_wire_acceptance':True,'findings':[
 'graph_protocol.SYSTEM requests a graph but does not literally specify JSON serialization or the version value; the requested format schema is carried separately.',
 'serve_model.py hashes and records the format schema but does not apply constrained JSON/schema decoding to model.generate; template and greedy generation are identical for all arms.',
 'Base emits YAML-like output for all 110 saved context requests. Retained produces parseable JSON for 95 requests, but its hybrid/new-version output is not an accepted old or new wire. These failures are not 0% answer correctness.',
 'New adapter protocol transfer is substantially stronger, but operation/slot metrics and source-backed execution must be reviewed separately. A passed JSON/schema gate cannot by itself promote weights.',
 'A parseable selector response may echo the input and still violate the selection contract. JSON parseability counts are not selector success counts.',
 'Original legacy Ollama/GGUF and this Transformers NF4 backend have different format-enforcement behavior; saved legacy comparisons cannot isolate planner/Flow effect.'
]}
(R/'RAW_PROTOCOL_REVIEW.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
md=['# ตรวจ protocol จาก raw330 ที่บันทึกไว้','','อ่านผลที่มีอยู่ ไม่รันคำถามหรือโมเดลใหม่ ไม่แก้ frozen runtime/weights/prompt และไม่ regrade คำตอบ baseline','',
 '| แขน | JSON parse ได้ | Wire ผ่าน | จำนวน |','|---|---:|---:|---:|']
for arm,c in arms.items():md.append(f"| {arm} | {c['json_parseable']} | {c['runtime_wire_accepted']} | {c['requests']} |")
md+=['','## ข้อวินิจฉัยก่อนเลือกน้ำหนัก','','- ค่า wire0 ของ base/retained ไม่ใช่คำตอบถูก0%: baseส่งข้อความคล้ายYAML ส่วนretainedส่วนใหญ่ส่งJSONแต่ผิดversion/โครงสร้างและมีgraph fieldsปะปน','- SYSTEMไม่ได้ระบุชัดว่าให้ส่งJSONและversion literal ขณะที่backendรับformatเพื่อบันทึกhash แต่ไม่ได้ใช้grammar/schema constrained decodingในgenerate ตัวแปรนี้เหมือนกันทั้ง3แขน จึงวัดการถ่ายโอนprotocolภายใต้backendนี้ได้ แต่ห้ามอธิบายทั้งหมดว่าเข้าใจบริบทไม่ได้','- newผ่านwire90/110 แต่ยังต้องตรวจoperation/target/slot/critical-domain และคำตอบกับsourceจริงของR130ก่อนเลือก ห้ามpromoteเพียงเพราะJSONผ่าน','- ตัวอย่างselectorบางรายการส่งรูปinputกลับมา แม้JSONparseได้ก็ไม่ใช่การเลือกevidenceที่ผ่านcontract จำนวนที่สำรวจจากlogยังเปลี่ยนระหว่างreplay ต้องอ่านเป็นหลักฐานระหว่างรัน','- Backendดั้งเดิมที่ใช้Ollama/GGUFมีพฤติกรรมenforceformatต่างกัน การเทียบsavedlegacyต้องระบุbackend/source/clock/deadlineconfounds','',
 '## งานที่ต้องทำใน adjudication','','1. ใช้ R130/paired_replay03 ที่ครบแล้ว ไม่ใช้คะแนน execution R129 ทดแทน','2. อ่านทุก execution regression และกลุ่มcriticalกับsource/คำถาม/คำตอบ ไม่ถือreceiptที่ถูกว่าsemanticถูกทั้งคำถาม','3. แยกprotocol adaptation, invalid proposal fallback, selector-contract failure และ actual source/content failures','4. หากเลือกnewต้องมีเหตุผลจากexecutionและcriticalreviewเพิ่มเติมตามpromotion gates; ระบุข้อจำกัดprotocolนี้ในรายงานสุดท้าย','5. การแก้prompt/decoderในอนาคตต้องเป็นinput/backendรุ่นใหม่ที่ตรึงแยกกัน ไม่แก้รอบfrozenหรือแอบใช้rawเก่ากับpromptใหม่','',
 '## หลักฐานโค้ดและ raw','','- `system/app/knowledge/common/domain_flow/graph_protocol.py`: SYSTEM/messages/extend_schema','- `../r129_full_plan_completion_20261024/serve_model.py`: apply_chat_template/model.generate/provenance','- `../r129_full_plan_completion_20261024/three_arm02/RESULTS.jsonl`','- `RAW_PROTOCOL_REVIEW.json`: ตัวอย่างrawและprovenanceแยกแขน/selector','']
(R/'RAW_PROTOCOL_REVIEW_TH.md').write_text('\n'.join(md)+'\n','utf8');print(json.dumps(arms))
