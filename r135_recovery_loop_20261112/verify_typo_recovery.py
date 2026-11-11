"""Mechanism-separated edit tests and natural source delivery, no HTTP/model."""
import copy,json,re,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.typo_recovery import propose,edits_allowed
from app.core.keyboard_neighbor_recovery import adjacent_key_substitution
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.input_derivation import register,check
from app.knowledge.common.domain_flow.engine import Engine

out=R/('typo_controls_'+str(time.time_ns()));out.mkdir();checks={};mechanisms={};details=[]
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=view.snapshot();records=snap['release']['records']
checks['keyboard_geometry_supports_example']=adjacent_key_substitution('ส','ม')
for kind,q in [('keyboard','มีเกสอะไรบ้าง'),('missing_character','มีเกอะไรบ้าง'),('repeated_character','มีเกมมอะไรบ้าง'),('repeated_suffix','มีเกมอะไรบ้างง'),('transposition','มีกเมอะไรบ้าง'),('repeated_word','มีเกมเกมอะไรบ้าง')]:
 r=propose(q,records);checks[kind]=r.status=='accepted' and r.execution=='มีเกมอะไรบ้าง';mechanisms[kind]={'input':q,'status':r.status,'execution':r.execution}
for q in ['มีเกมอะไรบ้าง','ใช้จอยยังไง','มีเมนูอะไรบ้าง','มีเกมใหม่อะไรบ้าง','ดีมากกกก','TEKKEN 9 ราคาเท่าไหร่','ไม่จองได้ไหม','PC 22 คน เล่น 120 นาที']:
 r=propose(q,records);checks['clean_or_constraint_'+q]=r.execution==q
for q in ['"มีเกสอะไรบ้าง"','https://example.test/มีเกสอะไรบ้าง']:
 checks['literal_protected_'+q]=propose(q,records).execution==q
r=propose('มีอะไรบ้าง',records);checks['whole_word_missing_clarifies']=r.status=='clarify' and r.execution==r.original and len(r.candidates)==3
r=propose('PS5 2 คน ราคเท่าไหร่',records);checks['numeric_platform_preserved']=r.status=='accepted' and 'PS5 2 คน' in r.execution
r=propose('ไม่มีเกสอะไรบ้าง',records);checks['polarity_not_deleted']=r.execution.startswith('ไม่มี')
fake={'game_test':{'record_id':'game_test','kind':'game','aliases':{'th':[],'en':[]},'fields':{'title':{'status':'known','value':{'th':'มีเกสอะไรบ้าง','en':None}}}}}
checks['owner_defined_name_not_corrected']=propose('มีเกสอะไรบ้าง',fake).execution=='มีเกสอะไรบ้าง'
checks['protected_constraint_edit_denied']=not edits_allowed([{'start':0,'end':3,'replacement':''}],[{'start':0,'end':3}])
class Pinned:
 path=view.path
 def snapshot(self):return snap
 def still_current(self,s):return True
 def connect(self,**kw):return view.connect(**kw)
reader=CommonAnswerer(Pinned())
def ask(q):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=reader.answer(q,locale='th',planner=None)
 details.append({'question':q,'answer':r.answer,'artifact':r.decision_artifact,'hits':r.hits})
 (out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8');return r
base=ask('มีเกมอะไรบ้าง')
identity=lambda r:{(h.get('record_id'),h.get('field'),h.get('source_id'),h.get('locator')) for h in r.hits}
checks['normal_positive_not_vacuous']=len(base.hits)>0
for q in ['มีเกสอะไรบ้าง','มีเกอะไรบ้าง','มีเกมมอะไรบ้าง']:
 r=ask(q);checks['same_source_delivery_'+q]=bool(r.hits) and identity(r)==identity(base) and r.answer==base.answer
 checks['raw_and_edits_retained_'+q]=r.decision_artifact['intent_edit_recovery']['original']==q and bool(r.decision_artifact['intent_edit_recovery']['edits'])
r=ask('มีอะไรบ้าง');checks['ambiguous_no_claims']=not r.hits and r.decision_artifact['response_type']=='clarification'
r=ask('ไม่มีเกสอะไรบ้าง');checks['edited_negation_not_auto_executed']=not r.hits and r.decision_artifact['response_type']=='clarification' and r.decision_artifact['intent_edit_recovery']['reason']=='polarity_sensitive_recovery_requires_confirmation'
r=ask('ไม่มีเกมอะไรบ้าง');checks['clean_negative_catalog_not_positive_list']=not r.hits
r=ask('PC นักศึกษา PSU ราคเท่าไหร่');checks['price_from_source_not_generated']='0 บาท' in r.answer and bool(r.hits)
r=ask('มีเกสอะไรบ้าง แล้ว PC นักศึกษา PSU ราคาเท่าไหร่');checks['compound_keeps_two_needs']='0 บาท' in r.answer and any(h.get('record_id','').startswith('availability_') for h in r.hits)
with request_context() as ctx:
 ctx.input={'raw_question':'มีเกสอะไรบ้าง'};ctx.bind_snapshot(snap);index=Engine.from_snapshot(snap,cache_key=view.path).index
 proof=register('PC ราคา 0 บาท','bounded_intent_edit_recovery',[],index=index,parent_question='มีเกสอะไรบ้าง')
 checks['forged_execution_not_authorized']=not proof['verified'] and not check('PC ราคา 0 บาท')['verified']
report={'all_passed':all(checks.values()),'checks':checks,'mechanisms':mechanisms,'scope':'purpose-built mechanism/control cases; source-only actual reader delivery, not unseen typo accuracy or complete linguistic proof','model_calls':0,'http_calls':0}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
