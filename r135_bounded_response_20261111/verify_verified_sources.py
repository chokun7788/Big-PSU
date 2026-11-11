"""Source scope, positive delivery, then isolated actual edit and withdrawal."""
import copy,json,re,sqlite3,time
from types import SimpleNamespace
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.policy_subject_scope import check
from app.web_api.server import _source_list

OUT=R/('verified_sources_controls_'+str(time.time_ns()));OUT.mkdir()
DB=R/'system/data/knowledge/verified_sources.sqlite'
IDS=['migrated_faq_rule_booking_max_sessions','migrated_faq_curated_reservation_max_sessions','migrated_faq_rule_booking_session_and_payment']
view=MigratedView(DB);snap=view.snapshot()
class Pinned:
 path=view.path
 def snapshot(self):return snap
 def still_current(self,s):return True
 def connect(self,**kw):return view.connect(**kw)
reader=CommonAnswerer(Pinned());checks={};rows=[]
def ask(q,lang='th',reader=reader):
 result=reader.answer(q,locale=lang,planner=None)
 rows.append({'question':q,'answer':result.answer,'sources':_source_list(result.hits),'artifact':result.decision_artifact})
 (OUT/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 return result
for i,(q,lang) in enumerate([('จองได้สูงสุดกี่รอบ','th'),('How many sessions can I book in one booking?','en'),('How many sessions can I book at PSU Esports Studio - Phuket?','en')]):
 r=ask(q,lang);checks['normal_six_'+str(i)]='6' in r.answer and bool(_source_list(r.hits)) and not re.search(r'\b3\s+Sessions?',r.answer,re.I)
 if lang=='en':checks['direct_answer_heading_'+str(i)]=r.answer.startswith('One booking')
r=ask('จองได้สูงสุดกี่ session และต้องจ่ายภายในกี่นาที');checks['sessions_and_payment']='6' in r.answer and '10' in r.answer
r=ask('PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองได้สูงสุดกี่รอบ');checks['price_and_booking_both']='0 บาท' in r.answer and '6 Sessions' in r.answer
for i,(q,lang) in enumerate([('โรงแรมอันดามันจองได้สูงสุดกี่รอบ','th'),('How many sessions can I book at Andaman Hotel?','en'),('Not PSU Esports Studio - Phuket, how many sessions can I book?','en')]):
 r=ask(q,lang);checks['wrong_subject_withheld_'+str(i)]='6' not in r.answer and not r.hits
 checks['scope_reason_'+str(i)]='policy_requested_subject' in json.dumps(r.decision_artifact) and ('สถานที่' in r.answer or 'place' in r.answer)
# Independent direct relationship corruption controls against the current index.
from app.knowledge.common.domain_flow.engine import Engine
index=Engine.from_snapshot(snap,cache_key=DB.resolve()).index
from app.knowledge.common.domain_flow.intent_source_binding import price_chain
pc=ask('PC นักศึกษา PSU ราคาเท่าไหร่')
pc_claims=pc.decision_artifact.get('domain_flow',{}).get('typed_claims',[])
checks['price_source_platform_positive']=bool(pc_claims) and not price_chain(index,'C06','PC ราคาเท่าไหร่',pc_claims)['errors']
checks['wrong_price_platform_rejected']='intent_price_requested_platform_mismatch' in price_chain(index,'C06','PS5 ราคาเท่าไหร่',pc_claims)['errors']
rid=IDS[2]
for name,mutate in [('missing_relation',lambda r:r['fields']['related_ids'].update(status='unknown',value=None,evidence_refs=[])),('forged_relation',lambda r:r['fields']['related_ids'].update(value=['another_center']))]:
 records=dict(index.records);records[rid]=copy.deepcopy(records[rid]);mutate(records[rid]);fake=SimpleNamespace(records=records,source_pairs=index.source_pairs)
 checks[name]=bool(check(fake,'จองได้สูงสุดกี่รอบ',[rid])['errors'])
records=dict(index.records);del records['center_psu_phuket'];checks['missing_center']=bool(check(SimpleNamespace(records=records,source_pairs=index.source_pairs),'จองได้สูงสุดกี่รอบ',[rid])['errors'])
# Clone again: owner controls never change the imported candidate database.
control=R/'system/data/knowledge'/('lifecycle_'+str(time.time_ns())+'.sqlite')
a=sqlite3.connect(DB.resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(control);a.backup(b);a.close();b.close()
store=CommonStore(control);live=CommonAnswerer(MigratedView(control))
before=ask('จองได้สูงสุดกี่รอบ',reader=live);checks['lifecycle_before_six']='6 Sessions' in before.answer
for rid in IDS:
 record=store.get(rid)['record'];record['fields']['answer']['value']={'th':'การจอง 1 ครั้งสามารถจองได้สูงสุด 5 Sessions','en':'One booking can include a maximum of 5 sessions.'}
 save_owner_record(store,record,record['revision'],'isolated-lifecycle-fixture',change_note='Fixture 5 sessions, not a real policy')
edited=ask('จองได้สูงสุดกี่รอบ',reader=live);checks['lifecycle_new_value']='5 Sessions' in edited.answer and '6 Sessions' not in edited.answer
checks['edit_invalidates_web_citation']=not _source_list(edited.hits)
for rid in IDS:store.withdraw(rid,actor='isolated-lifecycle-fixture')
withdrawn=ask('จองได้สูงสุดกี่รอบ',reader=live);checks['withdrawn_not_claimed']=not any(h.get('record_id') in IDS for h in withdrawn.hits) and not re.search(r'[56]\s+Sessions',withdrawn.answer,re.I)
report={'all_passed':all(checks.values()),'checks':checks,'scope':'source-only natural delivery + direct relation mutations + isolated actual edit/withdraw; 5 sessions is fixture only; not full semantic/authority proof'}
(OUT/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(OUT),**report},ensure_ascii=False));assert report['all_passed']
