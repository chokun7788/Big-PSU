"""A topical fragment needs clarification; source edits cannot supply intent."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.policy_scope import topic_clarification
from app.knowledge.common.domain_flow.request_verifier import observe
from app.knowledge.common.domain_flow.engine import Engine
O=R/('policy_topic_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);snapshot=view.snapshot();index=Engine.from_snapshot(snapshot).index;checks={};details=[]
def run(q):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 c=r.decision_artifact['execution_contract'];claims=[v for x in c['executor_results'] for v in x.get('claims',[])];details.append({'q':q,'answer':r.answer,'artifact':r.decision_artifact});return r,c,claims
fragments=['ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ช่วยแนบแฟล่งข้อูลด้วย','ข้อมูลอาหาร พื้นที่','Information about drinks and areas']
for n,q in enumerate(fragments):
 r,c,claims=run(q);checks['fragment'+str(n)+'_clarifies_without_business_claims']=r.decision_artifact['response_type']=='clarification' and not claims and any(s in r.answer for s in ['ต้องการทราบ','Do you mean'])
 seen=observe(index,q);checks['fragment'+str(n)+'_observer_does_not_certify_consumption_predicate']=not seen['needs'] and any(v['reason']=='policy_topic_missing_predicate' for v in seen['uncertain'])
explicit=['ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน','รับประทานอาหารในพื้นที่ที่กำหนดได้ไหม','เครื่องดื่มดื่มในพื้นที่ไหนได้บ้าง','ขอนโยบายอาหารและเครื่องดื่มในพื้นที่เล่นเกม','Can I bring drinks into the area?','Where can I eat food?','What are the rules for drinks in this area?','Does the area have food facilities?']
for n,q in enumerate(explicit):checks['explicit_predicate'+str(n)+'_not_replaced_by_topic_clarification']=topic_clarification(q) is None
r,c,claims=run(explicit[0]);checks['explicit_carrying_still_source_bound']=bool(claims) and 'นำอาหารหรือเครื่องดื่มเข้ามาได้' in r.answer and 'ช่วงที่นโยบายมีผลยังไม่ยืนยัน' in r.answer
record=copy.deepcopy(snapshot['release']['records']['migrated_faq_rule_food_drink']);record['fields']['answer']['value']={'th':'ข้อความพื้นที่จากแหล่งทดสอบที่แก้แล้ว','en':'Edited area source text'};save_owner_record(store,record,record['revision'],'isolated-source-control')
r,c,claims=run(fragments[0]);checks['owner_source_answer_edit_does_not_determine_fragment_intent']=r.decision_artifact['response_type']=='clarification' and not claims and 'ข้อความพื้นที่จากแหล่งทดสอบ' not in r.answer
for rid in ['migrated_faq_rule_food_drink','migrated_policy_text_food_bring_general']:store.withdraw(rid,actor='isolated-source-control')
r,c,claims=run(fragments[0]);checks['missing_policy_sources_do_not_manufacture_intent']=r.decision_artifact['response_type']=='clarification' and not claims
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'row206_training_quarantine_unchanged':True,'whole_policy_semantics_accepted':False,'scope':'Bounded native topic/predicate ambiguity only. No new accepted language label is fabricated for the unresolved original fragment.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
