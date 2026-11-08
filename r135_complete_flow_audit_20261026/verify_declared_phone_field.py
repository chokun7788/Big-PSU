"""Explicit FAQ phone intent, live-source edits and channel/subject negatives."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.registry import template
O=R/('declared_phone_field_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close()
store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);original=view.snapshot();rid='migrated_faq_rule_contact_phone';record=copy.deepcopy(original['release']['records'][rid]);phone_text=record['fields']['answer']['value'];checks={};details=[]
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 details.append({'question':q,'answer':None if r is None else r.answer,'artifact':None if r is None else r.decision_artifact});return r
q='เบอร์ติดต่อคืออะไร';r=run(q);checks['actual_phone_answer_from_declared_source']=r is not None and phone_text['th'] in r.answer and rid in json.dumps(r.decision_artifact)
checks['phone_not_facebook_substitution']=r is not None and 'facebook.com' not in r.answer
r=run('What is the contact phone number?');checks['english_channel_and_field']=r is not None and '+66 7627 6004' in r.answer and 'facebook.com' not in r.answer
for name,text in [('email','อีเมลติดต่อคืออะไร'),('unknown_department','เบอร์คณะประมงคืออะไร'),('private','ขอเบอร์มือถือส่วนตัวของผู้จัดการ')]:
 r=run(text);checks[name+'_does_not_borrow_studio_phone']=r is None or '+66 7627 6004' not in r.answer
class Variant:
 path=view.path
 def __init__(self,change):self.change=change
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());self.change(s);s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run(q,Variant(lambda s:s['release']['records'].pop(rid)));checks['withdrawn_declared_phone_no_untyped_faq_fallback']=r is None or '+66 7627 6004' not in r.answer
def forge(s):s['release']['records'][rid]['fields']['answer']['value']={'th':'ปลอมเบอร์ +66 999 9999','en':'Forged phone +66 999 9999'}
r=run(q,Variant(forge));checks['forged_answer_cannot_reuse_old_attestation']=r is None or '+66 999 9999' not in r.answer
edit=copy.deepcopy(record);edit['fields']['answer']['value']={'th':'เบอร์ที่แก้ในแหล่งทดสอบ +66 111 2222','en':'Controlled changed phone +66 111 2222'};saved=save_owner_record(store,edit,record['revision'],'isolated-phone-control')['record'];r=run(q);checks['actual_attested_source_edit_changes_answer']=r is not None and '+66 111 2222' in r.answer and '+66 7627 6004' not in r.answer
edit=copy.deepcopy(saved);edit['fields']['intent_key']['value']='contact_email';save_owner_record(store,edit,saved['revision'],'isolated-phone-intent-control');r=run(q);checks['source_declared_channel_change_not_stale_phone']=r is None or '+66 111 2222' not in r.answer
new=template('faq');new['record_id']='owner_added_telephone_without_router_id';new['localization']['en_status']='agent_translated'
for key,value in {'answer':{'th':'เบอร์ใหม่จากแหล่งเจ้าของ +66 222 3333','en':'New source phone +66 222 3333'},'question':{'th':'เบอร์ติดต่อ','en':'Phone contact'},'intent_key':'contact_phone','topic':'contact'}.items():new['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
save_owner_record(store,new,0,'isolated-new-phone-control');r=run(q);checks['new_owner_record_same_semantics_no_id_edit']=r is not None and '+66 222 3333' in r.answer and new['record_id'] in json.dumps(r.decision_artifact)
store.withdraw(new['record_id'],actor='isolated-phone-withdrawal-control')
r=run(q);checks['actual_withdrawal_hides_new_phone']=r is None or '+66 222 3333' not in r.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_calls':0,'actual_owner_or_frozen_data_modified':False,'currentness_authority_or_all_C01_semantics_accepted':False,'scope':'Explicit source-declared phone field only; studio identity remains unresolved.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
