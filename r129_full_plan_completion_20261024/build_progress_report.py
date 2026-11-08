"""Trace every frozen plan heading to code and real acceptance artifacts."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p,default=None):return json.loads(p.read_text('utf-8-sig')) if p.exists() else default
req=read(R/'REQUIREMENTS.json');modules='system/app/knowledge/common/'
mapping={
 'data':['registry.py','store.py','migrated_view.py','domain_flow/projection.py','domain_flow/index.py','claim_bindings.py'],
 'context':['flow_context.py','domain_flow/dialogue_task.py','domain_flow/request_provenance.py','domain_flow/span_provenance.py'],
 'planner':['domain_flow/graph_protocol.py','domain_flow/understanding.py','domain_flow/meaning_review.py'],
 'graph':['domain_flow/context_guard.py','domain_flow/context_bindings.py','domain_flow/plan_contract.py'],
 'executors':['domain_flow/executor_registry.py','domain_flow/capabilities.py','domain_flow/engine.py','domain_flow/readers.py','domain_flow/meaning_reader.py','domain_flow/comparison_executor.py','domain_flow/source_operations.py'],
 'verify':['domain_flow/obligation_verifier.py','domain_flow/native_contract.py','domain_flow/result_contract.py'],
 'gateway':['domain_flow/model_gateway.py','flow_context.py'],
 'render':['domain_flow/customer_render.py','domain_flow/engine.py'],
 'authority':['domain_flow/authority_resolution.py','claim_bindings.py'],
}
references={'FLOW-27','FLOW-29','CONTRACT-07','CONTRACT-14','CONTRACT-16','PHASE-01','PHASE-18','PHASE-21'}
training={'FLOW-23','FLOW-24','FLOW-26','CONTRACT-15','PHASE-07','PHASE-08','PHASE-09'}
evaluation={'FLOW-01','FLOW-02','FLOW-28','PHASE-10','PHASE-11','PHASE-13','PHASE-14','PHASE-15','PHASE-16','PHASE-17','PHASE-20'}
direct={'FLOW-04':'data','FLOW-05':'data','FLOW-06':'data','FLOW-07':'data','FLOW-09':'context','FLOW-10':'planner','FLOW-11':'planner','FLOW-12':'graph','FLOW-13':'graph','FLOW-14':'graph','FLOW-15':'executors','FLOW-16':'executors','FLOW-17':'gateway','FLOW-18':'verify','FLOW-19':'verify','FLOW-20':'render','FLOW-21':'verify','FLOW-22':'executors','FLOW-25':'data','CONTRACT-01':'data','CONTRACT-02':'context','CONTRACT-03':'planner','CONTRACT-04':'executors','CONTRACT-05':'graph','CONTRACT-06':'graph','CONTRACT-08':'executors','CONTRACT-09':'verify','CONTRACT-10':'authority','CONTRACT-11':'verify','CONTRACT-12':'verify','CONTRACT-13':'gateway','PHASE-03':'executors','PHASE-04':'graph','PHASE-05':'executors','PHASE-06':'data','PHASE-19':'verify'}
train=read(R/'training_v2/train01/TRAINING_COMPLETE.json',{});paired=read(R/'three_arm02/COMPLETE.json',{});full=read(R/'FULL_TEST_COMPLETE.json',{});analysis=read(R/'full_analysis/ANALYSIS_FINAL.json',{})
evidence=[]
for pattern,file in [('verification_*','VERIFICATION.json'),('graph_verification_*','RESULT.json'),('gateway_verification_*','RESULT.json'),('comparison_verification_*','RESULT.json'),('extended_*','RESULTS.json'),('source_guard_verification_*','VERIFICATION.json'),('live_verification_*','VERIFICATION.json'),('harness_verification_*','RESULT.json')]:
 for p in sorted(R.glob(pattern),key=lambda p:p.name,reverse=True):
  v=read(p/file,{})
  if v.get('summary',v).get('all_passed'):evidence.append(str((p/file).relative_to(R)));break
lines=['# สถานะเทียบ Flow ใหญ่ต้นฉบับ R129','','## ขอบเขต','', 'ใช้เอกสารต้นฉบับ R123 ที่ตรึงไว้ใน spec/ รวม P0–P8, R00–R12 และ C01–C14 ไม่มีการลดขอบเขตให้เหลือเฉพาะเคสตัวอย่างของ R128','', 'จำนวนหัวข้อในตารางเป็นรายการตรวจรับ ไม่ใช่เปอร์เซ็นต์ความแม่นยำหรือเปอร์เซ็นต์งานเสร็จ การมี module ไม่เท่ากับผ่านการตรวจรับ','', '## สถานะรอบนี้','',f'- ฝึกน้ำหนักใหม่เสร็จและมี optimization proof: {bool(train.get("complete"))}',f'- เปรียบเทียบสามแขนเสร็จ: {bool(paired.get("complete"))}',f'- Full Test 20,554 keys / 55,811 grades ตรวจ coverage แล้ว: {bool(full.get("complete"))}',f'- Root cause review หลัง Full Test เสร็จ: {bool(analysis.get("human_agent_root_cause_review_complete"))}','', 'รอบฝึกแรกไม่ถูกนำมาตรวจรับ เพราะพบ original family ข้าม train/validation เก็บไว้ที่ train01/NOT_ACCEPTED_SPLIT_REVIEW.json รอบที่ใช้จริงคือ training_v2/ ซึ่งรวม semantic family กับ original multilingual/core family แบบ transitive union แล้ว','', '## แผนที่ข้อกำหนดครบทุกหัวข้อ','', '| ข้อกำหนด | สถานะหลักฐาน | โค้ด/เอกสารที่ตรวจได้ |','|---|---|---|']
trace=[]
for item in req['requirements']:
 rid=item['id'];status='implementation_present_acceptance_pending';paths=[]
 if rid in references:status='reference_section_retained';paths=['spec/'+item['source']]
 elif rid in training:
  status='training_and_review_evidence_present' if train.get('complete') else 'review_complete_training_running';paths=['training_v2/ANNOTATION_REVIEW_SUMMARY.json','training_v2/DATASET_FREEZE.json','training_v2/train01/PROGRESS.json']
 elif rid in evaluation:
  status='final_adjudication_pending' if full.get('complete') else 'paired_comparison_complete_full_test_pending' if paired.get('complete') else 'evaluation_pipeline_prepared_not_yet_complete';paths=['EVALUATION_PROTOCOL.json','EVALUATION_GATE_ADDENDUM.json','compare_planners_v2.py','continue_execution.py','analyze_full_v2.py']
 else:
  key='executors' if rid.startswith('C0') or rid.startswith('C1') else direct.get(rid,'verify');paths=[modules+n for n in mapping[key]]
  if rid in {'PHASE-06','FLOW-25'}:paths+=['SOURCE_DIAGNOSTICS_TH.md','SOURCE_DIAGNOSTICS.json']
 assert paths and all((R/p).is_file() for p in paths),(rid,paths)
 trace.append({'requirement_id':rid,'title':item['title'],'source_spec_sha256':item.get('sha256') or hashlib.sha256(item['text'].encode()).hexdigest(),'status':status,'implementation':paths,'acceptance_artifacts':evidence if status=='implementation_present_acceptance_pending' else [],'section_has_not_been_deleted':True})
 lines.append('| '+rid+' '+item['title'].replace('|','/')+' | '+status+' | '+', '.join('`'+p+'`' for p in paths[:3])+' |')
lines+=['','## Flow runtime ที่ใช้','','```mermaid','flowchart TD',' A[Raw input + trusted delivered context + pinned clock] --> B[Source-backed native intent or bounded planner proposal]',' B --> C[Validate wire, quotes, local slots and shared edges]',' C --> D[Compile capability-specific task graph and obligations]',' D --> E[Finish independent typed reads]',' E --> F[Scoped fallback through one gateway and request budget]',' F --> G[Verify record/field/revision/source and recompute arithmetic]',' G --> H[Verify requested needs/options and choose per-task state]',' H --> I[Operation renderer: short answer, steps, lists or comparison table]',' I --> J[Audit, provenance and review queue without automatic training]','```','', '## สิ่งที่พัฒนาและข้อจำกัดที่ยังต้องรายงาน','', '- เพิ่ม shared prefix, local override, explicit anaphora และ ambiguity เมื่อมีหลาย antecedents พร้อม source spans','- Slot จากประวัติ/ตัวเลขที่ normalize ถูกแยกจากข้อความปัจจุบัน ไม่อ้าง derived text ว่าเป็น raw quote','- คืน ExecutorResult และ ledger ร่วม พร้อมหลักฐานการคำนวณ และเก็บส่วนที่ยังตอบไม่ครบ','- เปรียบเทียบแพ็กเกจ/กติกาโดยเก็บตัวเลือกแยก และแสดงการเปรียบเทียบเป็นตาราง','- Gateway ตรวจ profile/messages/schema จริง และคง base สำหรับ selector/compatibility callers พร้อม shared budget','- ยังคง compatibility readers อย่างเปิดเผย การมีข้อมูลบางส่วนหรือ pointer ที่ถูกไม่ยืนยัน semantic accuracy','- ข้อมูล unknown/conflicted/ช่วงมีผลที่ไม่ยืนยันคงเดิม ไม่เพิ่มข้อมูลธุรกิจหรือเปลี่ยน approvals เพื่อทำคะแนน','- ข้อมูลกับ R95 ต่างรุ่นและ full deadline ต่างกัน จึงไม่อ้างคะแนนที่เปลี่ยนว่าเกิดจาก Flow เพียงตัวเดียว','- Candidate ยังไม่ติดตั้งทับ R78','', '## หลักฐานการตรวจรับที่มีแล้ว','',*['- `'+p+'`' for p in evidence],'', 'ยังไม่ประกาศว่างานทั้งหมดเสร็จจนกว่าจะมีผลสามแขน, coverage Full Test, source/model proof และรายงาน root cause ที่ตรวจต่อครบ']
(R/'REQUIREMENTS_TRACEABILITY.json').write_text(json.dumps({'requirements':trace,'all_76_sections_accounted_for':len(trace)==76,'overall_complete':False,'accuracy_percent':None},ensure_ascii=False,indent=2),'utf8')
(R/'IMPLEMENTATION_REVIEW_TH.md').write_text('\n'.join(lines)+'\n','utf8');print(json.dumps({'sections_accounted_for':len(trace),'training_complete':bool(train.get('complete')),'paired_complete':bool(paired.get('complete')),'full_test_complete':bool(full.get('complete'))}))
