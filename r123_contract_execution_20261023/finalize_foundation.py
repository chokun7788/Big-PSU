"""Report verified implementation scope; never equate replay with accuracy."""
import collections,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;S=R/'revision03_system';DESIGN=ROOT/'r123_plan_distillation_architecture_20261023'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
valid=[]
for p in sorted(R.glob('verification_*/VERIFICATION.json')):
 value=read(p)
 if value['all_passed'] and any('revision03_system' in name for name in read(p.parent/'RUN_FREEZE.json')):valid.append(p)
assert valid
V=valid[-1].parent;summary=read(valid[-1]);packpath=sorted(R.glob('PACKAGE_VERIFICATION_*.json'))[-1];package=read(packpath);assert package['all_passed']
new=read(V/'SAVED_PLANNER_REPLAY.json')+read(V/'RETAINED_API_PROPOSAL_REPLAY.json');oldpath=sorted(R.glob('PARENT_REPLAY_*.json'))[-1];old=read(oldpath)
assert len(old)==len(new)==40
changes=[]
for i,(a,b) in enumerate(zip(old,new)):
 assert (a['key'],a['question'])==(b['key'],b['question'])
 def claims(row):return {(c['fact_id'],c.get('numeric'),c['value']) for c in row['result']['claims']}
 if a['result']['answer']!=b['result']['answer'] or a['result']['status']!=b['result']['status']:
  changes.append({'row':i,'key':b['key'],'question':b['question'],'before_status':a['result']['status'],'after_status':b['result']['status'],'removed_claims':sorted(claims(a)-claims(b),key=str),'added_claims':sorted(claims(b)-claims(a),key=str),'before_answer':a['result']['answer'],'after_answer':b['result']['answer'],'task_contracts':b['result'].get('execution_contract',{}).get('tasks',[])})
regression={'parent':'R122 revision04','candidate':'R123 foundation revision03','saved_proposals':40,'unique_question_keys':len({x['key'] for x in new}),'changed_rows':len(changes),'removed_claim_count':sum(len(x['removed_claims']) for x in changes),'added_claim_count':sum(len(x['added_claims']) for x in changes),'new_model_calls':0,'semantic_accuracy':None,'changes':changes}
(R/'REGRESSION_REVIEW.json').write_text(json.dumps(regression,ensure_ascii=False,indent=2),'utf8')
protected=read(R/'PARENT_FREEZE.json')
for path in [ROOT/'r121_context_planner_training_20261022/PROTECTED_INPUTS.json',ROOT/'r121_context_planner_training_20261022/train02/RUN_FREEZE.json',*[p for p in R.glob('verification_*/RUN_FREEZE.json')]]:
 for name,h in read(path).items():
  assert name not in protected or protected[name]==h,('contradictory_frozen_identity',name)
  protected[name]=h
for name,h in read(DESIGN/'PLAN_STATUS.json')['document_sha256'].items():protected[str((DESIGN/name).resolve())]=h
changed=[name for name,h in protected.items() if not Path(name).is_file() or sha(Path(name))!=h];assert not changed,changed
assert sha(S/'data/knowledge/common.sqlite')==read(R/'LINEAGE.json')['database_sha256']
adapter=ROOT/'r121_context_planner_training_20261022/train02/adapter/adapter_model.safetensors'
assert sha(adapter)==read(ROOT/'r122_context_scope_calendar_20261022/LINEAGE.json')['same_adapter_sha256']
(R/'CAPABILITY_MATRIX.json').write_text((V/'CAPABILITY_MATRIX.json').read_text('utf8'),'utf8')
verification={'files_checked':len(protected),'changed':changed,'database_sha256':sha(S/'data/knowledge/common.sqlite'),'same_r121_adapter_sha256':sha(adapter),'production_installed':False,'new_training':False,'new_model_calls':0}
(R/'FINAL_VERIFICATION.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),'utf8')
status={'status':'foundation_implemented_and_verified','candidate':str(S),'design_version':'R123','implementation_revision':'foundation-r03','full_r123_architecture_implemented':False,
 'phase_scope':{'P0':'compiled IR/capability vocabulary/adapters implemented; new model wire and full raw RequestContext pending','P1':'typed-first scheduler, local/shared receipts, source/option verifier implemented; shared-prefix/history completeness pending','P2':'native readers adapted in Engine; calendar/live API special paths still native','P3_P8':'not completed in this foundation turn'},
 'verification':{'foundation_checks_passed':sum(summary['checks'].values()),'foundation_checks_total':len(summary['checks']),'packaging_checks_passed':sum(package['checks'].values()),'packaging_checks_total':len(package['checks']),'annotation_rows_compiled':289,'saved_proposals_replayed':40,'unique_question_keys':regression['unique_question_keys'],'new_model_inferences':0,'actual_http_benchmark':False,'fresh_semantic_accuracy':None,'full_test':False},
 'artifacts':{'verification':str(valid[-1]),'packaging_verification':str(packpath),'parent_replay':str(oldpath)},
 'preservation':verification,'candidate_ready_for_production':False,'candidate_ready_for_new_distillation':False,
 'next_work':['native calendar/live integration and full trusted RequestContext/span mapping','extend operation/authority adapters and collection scope diagnostics','review complete training labels before new optimization','freeze heldout families and compare three planner arms on the same engine']}
(R/'IMPLEMENTATION_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
body=['# R123 foundation revision03 — ผลลงมือทำตาม Flow','',
'## สถานะที่ทำได้จริง','',
'เริ่ม implement แล้วใน candidate แยก `revision03_system` ต่อจาก R122 revision04 รอบนี้ทำฐานของ P0/P1 และ adapter ของ reader เดิม ไม่ใช่ทำ R123 ทั้งแผนจบแล้ว ไม่ได้ฝึกเพิ่ม ไม่ได้รันโมเดลใหม่ และไม่ได้ติดตั้งทับ production','',
'## 1. สิ่งที่เพิ่มใน runtime','',
'1. **Compiled request/task graph**: มี task IDs, spans, slot owners, normalized duration roles, shared bindings และ obligations ต่อ task/option','2. **Capability registry**: ครอบคลุมชื่อหมวด C01–C14 และระบุ operator/field combinations ที่มี native adapter; unsupported operation ถูกแสดงตรง ไม่เปลี่ยนเป็น detail เงียบ ๆ','3. **Typed-first scheduling**: วางแผนและอ่านด้วย native readers ของทุกงานก่อน แล้วค่อยใช้งบ evidence selector กับงานที่ยังจำเป็น','4. **Obligation verifier**: ตรวจ field/ตัวเลือกของ comparison และหลักฐานความครบของ collection ก่อนถือว่าตอบครบ','5. **Source receipts**: ตรวจ fact/record/category/ref ให้ตรง pinned snapshot และคำนวณตัวเลขใหม่จาก source รวมทั้งตรวจรูปข้อความราคาที่อนุญาต','6. **Terminal reason mapping**: budget หมดแยกจากบริการ/model transport ล้ม และคงคำตอบของงานอิสระที่อ่านได้','7. **Public artifact audit**: package ของ domain-reader path ส่ง compiled plan, per-need obligations, receipts และ schedule ไปกับ decision artifact','',
'Source เป็น schema/business operators ทั่วไป ไม่ใส่ question keys หรือ expected answers ของ benchmark ลงในโค้ดใหม่','',
'## 2. Flow ที่ runtime ใหม่ทำจริง','',
'```mermaid','flowchart TD',' A[Validated legacy planner proposal] --> B[Review and scoped context guard]',' B --> C[Compile tasks slots shared edges and obligations]',' C --> D[Check capability]',' D --> E[Read every deterministic task]',' E --> F[Bounded selector for remaining unresolved tasks]',' F --> G[Native source finalizer and candidate claims]',' G --> H[Source receipts and option coverage verifier]',' H --> I[Deliver supported parts or explicit gaps]','```','',
'ยังใช้ planner wire/schema และ checkpoint R121 เดิม การ enrich slots/context ของ compiler ไม่ใช่สิ่งที่โมเดลเพิ่งเรียนรู้มา ผลแต่ละขั้นถูกแยกใน audit','',
'## 3. ตรวจอะไรแล้ว','',
f"- จุดตรวจหลัก {len(summary['checks'])} จุด ผ่านทั้งหมด และ package/artifact อีก {len(package['checks'])} จุดผ่านทั้งหมด",
'- ตรวจ compile ป้ายเดิม 289 แถว: train 244 / validation 15 / test 30 เป็น structural audit ไม่ใช่การ review semantic ของป้ายครบแล้ว',
f"- Replay saved proposals 40 รายการ จาก {regression['unique_question_keys']} question keys: raw planner outputs 30 รายการ และ actual API proposals ที่เก็บไว้ 10 รายการ มีคำถามซ้ำข้ามแหล่ง จึงไม่เรียกว่า 40 คำถามอิสระ",
'- ไม่เรียก LLM ใหม่ ไม่รัน original legacy baseline inference และไม่ตี replay results เป็นคะแนน generalization','',
'### Fault injection ที่ตรวจแล้ว','',
'- เอา 60 นาทีออกจากคำตอบ compare แล้วต้องถูกจับว่าตัวเลือกหาย','- เปลี่ยนตัวเลขแต่ใช้ source ID เดิม ต้องถูกปฏิเสธ','- เปลี่ยนข้อความราคาเป็น permission ที่แต่งขึ้นทั้งที่ numeric ยังเดิม ต้องถูกปฏิเสธ','- ลบ numeric ของราคา หรืออ้าง evidence ref ที่ไม่มี ต้องถูกปฏิเสธ','- แก้ข้อความ policy ที่ยังใช้ refs เดิม ต้องถูกปฏิเสธ','- สร้าง shared-reference cycle ต้องไม่ผ่าน contract','- บังคับงานราคาแรกให้ pending และ budget=0 แต่ task จองต้องอ่านได้ก่อน selector และยังมี claims','- ขอ compare ที่ไม่มี adapter ต้องได้ unsupported_operation แต่ส่วนจองไม่หาย','- quote ที่ไม่อยู่ในคำถามต้องจบแบบ bounded missing_input ไม่ส่ง facts และไม่ crash','',
'## 4. สิ่งที่พบและแก้ระหว่างตรวจ','',
'- ตัวตรวจแรกมอง input_bindings ไม่ตรงกับ native binding_3 จึงเตือน false gap แก้ด้วยการจับคู่ native controls projection ใหม่จาก source','- contact value บางรายการเป็น FAQ owner_policy แก้ด้วย declared-query-profile adapter ที่ตรวจ query/source ซ้ำ ไม่อนุญาต owner_policy ทุก record แบบเหมารวม','- count ของ capacity/quantity field ต้องเป็น field lookup ไม่บังคับ proof แบบการ enumerate ชุดอุปกรณ์','- การตัด duration ออกจาก comparison scope ต้องตัดทั้ง raw และ normalized form เพื่อไม่ให้คำว่า one hour ที่ normalize แล้วกรอง source ผิด','- trusted history/raw offset mapping ยังไม่ครบ จึงคง native compatibility path ที่มีป้ายบอก แทนการอ้างว่า compiler ผูก current-user spans ครบแล้ว','',
'เก็บ candidate และผลการตรวจแต่ละ revision แยกกัน ไม่เขียนทับผลรอบก่อน','',
'## 5. เทียบการ execute กับ parent R122','',
f"เทียบด้วย source/เวลา/คำถามและ saved proposals เดียวกัน 40 รายการ พบข้อความหรือสถานะเปลี่ยน {len(changes)} รายการ claims ที่หาย {regression['removed_claim_count']} และ claims เพิ่ม {regression['added_claim_count']} ตัวเลขนี้บอกความต่างของ execution เท่านั้น ไม่ใช่ correct/incorrect accuracy",'',
'รายการที่ต่าง:','']
for c in changes:
 body += ['### '+c['question'],'',f"สถานะ {c['before_status']} → {c['after_status']}; removed claims {len(c['removed_claims'])}; added claims {len(c['added_claims'])}",'',c['after_answer'],'']
body+=['Nintendo usage ที่ถูกเสนอเป็น list ยังเป็น partial เมื่อไม่มี proof ว่ารายการครอบคลุมทั้งหมด ข้อความที่มี source ยังแสดงอยู่ การเตือนนี้ตั้งใจรักษาความต่างระหว่างข้อมูลที่มี กับการยืนยันว่า list ครบทุกอย่าง ไม่ใช่ข้อมูลหาย','',
'## 6. สิ่งที่ยังไม่ครบตาม R123','',
'| ส่วน | สถานะจริง |','|---|---|',
'| Internal task/slot/binding/obligation contracts | เชื่อม Engine แล้ว ผ่าน structural/source gates |',
'| Planner output wire R123 ใหม่ | ยังไม่ได้ implement; ใช้ legacy wire adapter |',
'| Shared-prefix audience/date และเงื่อนไขซ้อน | ยังไม่ครบ ใช้ guard/ambiguity ขอบเขตเดิม |',
'| Trusted history และ raw→normalized span mapping | ยังอยู่ native compatibility ที่มีเครื่องหมายบอก |',
'| All operations ของ 14 หมวด | ยังไม่ครบ registry แสดง adapter combinations กับ unsupported โดยไม่อ้างว่ารองรับทั้งหมด |',
'| Calendar/live special paths ใน public API | ยังใช้ native adapters เดิม ไม่ได้ผ่าน scheduler ใหม่ทั้งเส้น |',
'| Authority/supersession/compiler สำหรับข้อมูลใหม่ | ยังต้องทำต่อ ไม่แก้ approvals/ข้อมูลเอง |',
'| Numeric/reference/value receipts | เพิ่มแล้ว; registered calendar/spec transformations ยังไม่เป็น semantic entailment proof ทุกกรณี |',
'| Labels ที่ semantic-review ครบ | ยังไม่มี ชุด 289 ข้อรอบนี้ตรวจ compile เท่านั้น |',
'| New distillation/three-arm heldout evaluation | ยังไม่ได้เริ่ม |',
'| Actual new-model API / Full Test | ยังไม่ได้ทำใน foundation turn |','',
'แม้ gates ผ่านทั้งหมด ยังไม่ประกาศเปอร์เซ็นต์ความถูกต้องหรือความพร้อม production เพราะยังไม่ได้วัดความหมายปลายทางด้วยชุดที่กันไว้','',
'## 7. ข้อมูลและ source เดิม','', '```json',json.dumps(verification,ensure_ascii=False,indent=2),'```','',
'## 8. การรัน candidate และลำดับถัดไป','',
'มี launch_candidate.py สำหรับ candidate แยก ใช้ checkpoint R121 เดิมและ model profile ทั้งห้าตัวตรงกัน ตรวจ --check-config แล้วเท่านั้น ยังไม่ได้เปิดเซิร์ฟเวอร์เพื่อทำ inference ในงานนี้ live provider ของ launcher คง fixture unavailable จึงไม่ยืนยัน occupancy จริง','',
'ขั้นถัดไปตามแผนคือปิดช่องว่าง P1/P2 โดยเชื่อม native calendar/live และ trusted RequestContext, ขยาย operator/authority adapters และตรวจ labels ทั้งชุด ก่อนฝึก planner ต่อ การมี contracts ผ่านไม่ใช่เหตุให้ข้ามไปฝึกจาก draft labels โดยตรง','',
'ไฟล์หลัก:','',
'- IMPLEMENTATION_STATUS.json: สถานะเฟสและงานที่เหลือ','- CAPABILITY_MATRIX.json: adapter combinations และข้อจำกัดรายหมวด','- REGRESSION_REVIEW.json: ความต่างจาก parent รายข้อ','- FINAL_VERIFICATION.json: hash/source/model preservation','- verification_*/VERIFICATION.json และ replay JSON: หลักฐานการตรวจแต่ละรอบ','- PACKAGE_VERIFICATION_*.json: การส่ง audit ใน native packaging unit check','',
'Source ใหม่อยู่ใต้ revision03_system/app/knowledge/common/domain_flow/: plan_contract.py, capabilities.py, task_execution.py, obligation_verifier.py และจุดเชื่อม engine.py/integration.py','']
(R/'FOUNDATION_REPORT_TH.md').write_text('\n'.join(body),'utf8')
print(json.dumps({'candidate':'foundation-r03','checks_passed':len(summary['checks']),'packaging_checks_passed':len(package['checks']),'protected_files':len(protected),'execution_changes':len(changes),'removed_claims':regression['removed_claim_count'],'new_inference':0,'full_r123_complete':False,'report':str(R/'FOUNDATION_REPORT_TH.md')},ensure_ascii=False,indent=2))
