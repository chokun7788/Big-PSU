"""Document nouns and source-attested underpayment proof, no provider calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.request_verifier import observe
from app.knowledge.common.domain_flow.payment_intent import request
O=R/('payment_predicate_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);snapshot=view.snapshot();index=Engine.from_snapshot(snapshot).index;checks={};details=[]
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 c=r.decision_artifact['execution_contract'];tasks=c['request_plan']['tasks'];claims=[v for x in c['executor_results'] for v in x.get('claims',[])];receipts=[v for x in c['executor_results'] for v in x.get('receipts',[])];details.append({'q':q,'answer':r.answer,'artifact':r.decision_artifact});return r,tasks,claims,receipts
q='ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม';r,tasks,claims,receipts=run(q)
checks['three_document_objects_one_payment_predicate']=len(tasks)==1 and tasks[0]['category']=='C09'
checks['quotation_noun_does_not_invent_price_obligation']=len(observe(index,q)['needs'])==1 and not any(t['category']=='C06' for t in tasks)
checks['actual_recorded_document_distinctions_preserved']=all(s in r.answer for s in ['ใบกำกับภาษี','ใบเสนอราคา','ใบเสร็จ','คำตอบก่อนหน้า']) and bool(receipts)
checks['unknown_document_policy_validity_retained']='ช่วงที่นโยบายมีผลยังไม่ยืนยัน' in r.answer
q='ขอใบเสนอราคาได้ไหม; VR เล่น 30 นาที ราคาเท่าไหร่';r,tasks,claims,receipts=run(q);checks['real_document_and_fee_siblings_both_preserved']={t['category'] for t in tasks}=={'C09','C06'} and any(c['facet']=='amount' for c in claims)
q='Can you issue a receipt or tax invoice?';r,tasks,claims,receipts=run(q);checks['english_document_permission_keeps_C09']=len(tasks)==1 and tasks[0]['category']=='C09' and bool(receipts) and 'invoice' in r.answer.lower()
q='ขอสอบถามหน่อยครับ ยอดที่โอนขาดไป ต้องส่งหลักฐานเพิ่มอย่างไร';r,tasks,claims,receipts=run(q)
checks['underpayment_proof_has_typed_task_and_receipts']=len(tasks)==1 and tasks[0]['category']=='C09' and tasks[0]['operation']!='bounded_compatibility' and bool(claims) and bool(receipts)
checks['actual_scoped_source_question_actor_alignment']=any(c['record_id']=='r130_owner_42_scoped' for c in claims) and not r.decision_artifact['execution_contract']['verifier_result']['evidence_support']['fatal']
checks['underpayment_source_proof_and_no_invented_deadline']='สลิป' in r.answer and 'หลักฐานการจอง' in r.answer and not any(s in r.answer for s in ['ภายใน 24','ภายใน 30','ภายใน 60'])
checks['underpayment_unknown_policy_validity_visible']='ช่วงที่นโยบายมีผลยังไม่ยืนยัน' in r.answer
for q in ['โอนขาดไป ต้องโอนเพิ่มกี่บาท','VR ราคาเท่าไหร่','What equipment is in PC Zone?']:
 checks['other_predicate_not_forced_into_proof_'+str(len(checks))]=request(q) is None
# The real owner writer updates the attestation as part of an authorized edit.
record=copy.deepcopy(snapshot['release']['records']['r130_owner_42_scoped']);record['fields']['answer']['value']={'th':'ข้อความจากแหล่งนโยบายที่แก้แล้ว','en':'Edited source policy'};save_owner_record(store,record,record['revision'],'isolated-source-control')
r,tasks,claims,receipts=run('ยอดที่โอนขาดไป ต้องส่งหลักฐานเพิ่มอย่างไร');checks['actual_owner_edit_changes_source_answer_without_training']='ข้อความจากแหล่งนโยบายที่แก้แล้ว' in r.answer and any(c['record_id']=='r130_owner_42_scoped' for c in claims)
class Unattested:
 path=view.path
 def __init__(self):
  self.pinned=copy.deepcopy(view.snapshot());self.pinned['epoch']=time.time_ns();self.pinned['release']['records']['r130_owner_42_scoped']['fields']['answer']['value']={'th':'ข้อความปลอมที่ไม่มีการรับรองแหล่ง','en':'Unattested answer mutation'}
 def snapshot(self):return copy.deepcopy(self.pinned)
 def still_current(self,s):return s['epoch']==self.pinned['epoch']
r,tasks,claims,receipts=run('ยอดที่โอนขาดไป ต้องส่งหลักฐานเพิ่มอย่างไร',Unattested());checks['unattested_answer_mutation_cannot_be_certified']='ข้อความปลอม' not in r.answer and not any(c['record_id']=='r130_owner_42_scoped' for c in claims)
store.withdraw('r114_q018_owner_policy',actor='isolated-source-control');r,tasks,claims,receipts=run('ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม');checks['withdrawn_document_source_does_not_restore_constants']=len(tasks)==1 and tasks[0]['category']=='C09' and not any(c['record_id']=='r114_q018_owner_policy' for c in claims) and 'ออกใบกำกับภาษีไม่ได้' not in r.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'whole_payment_semantics_accepted':False,'source_review':'Original q015 and current attested owner42 both ask underpayment; owner42 actual source question now aligns with independently recomputed underpayment action. No new unique manual label review.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
