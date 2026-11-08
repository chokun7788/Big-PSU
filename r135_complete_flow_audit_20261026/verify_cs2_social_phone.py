"""Source-bound CS2 map-selection controls; no model calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('cs2_social_phone_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def claims(r):return {c['record_id'] for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if r else set()

social='competition_competition_rules_cs2_psu_phuket_2026_section_048';phone='competition_competition_rules_cs2_psu_phuket_2026_section_051'
q1='กติกา CS2 เข้าโซเชียลบนเครื่องแข่งได้ไหม';q2='กติกา CS2 นำโทรศัพท์เข้าเขตแข่งได้ไหม'
x=run(q1);checks['social_source_and_exception']=bool(x and social in claims(x) and 'นอกจาก' in x.answer and 'ตรวจสอบ' in x.answer)
x=run(q2);checks['phone_source_and_time_condition']=bool(x and phone in claims(x) and 'จนกว่าจะจบแมตช์' in x.answer and 'ตรวจสอบ' in x.answer)
x=run('TEKKEN 8 นำโทรศัพท์เข้าเขตแข่งได้ไหม');checks['other_game_not_cs2']=not bool(claims(x)&{social,phone})
x=run('เบอร์โทรศัพท์ติดต่อศูนย์คืออะไร');checks['contact_phone_not_competition']=not bool(claims(x)&{social,phone})
x=run('กติกา CS2 ใช้โซเชียลบนเครื่องแข่งได้ไหม และราคา PC เท่าไหร่');checks['compound_price_and_social']=bool(x and social in claims(x) and any('rate' in c.lower() for c in claims(x)))
x=run('Can players access social media on competition computers in CS2?');checks['english_social_source']=social in claims(x)
x=run('Can players bring mobile phones into the CS2 competition area?');checks['english_phone_source']=phone in claims(x)
x=run('In PSU Phuket CS2 2026 Tournament can players bring mobile phones into competition area?');checks['named_event_phone_source']=phone in claims(x)
for rid,q,th,en,marker in [(social,q1,'5. ห้ามเข้าโซเชียลมีเดียบนคอมพิวเตอร์แข่งขัน ยกเว้น OWNER-SOCIAL.TEST','5. Social media is forbidden on competition computers except OWNER-SOCIAL.TEST','OWNER-SOCIAL.TEST'),(phone,q2,'2. ห้ามนำโทรศัพท์เข้าไปในพื้นที่แข่งจนกว่า OWNER-PHONE.TEST','2. Mobile phones are forbidden in competition area until OWNER-PHONE.TEST','OWNER-PHONE.TEST')]:
 record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['text']['value']['th']=th;record['fields']['text']['value']['en']=en;save_owner_record(store,record,record['revision'],'isolated-social-phone-control');x=run(q);checks['owner_edit_'+rid[-3:]]=bool(x and marker in x.answer and rid in claims(x))
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][phone]['fields']['text']['value']['th']='ห้ามนำโทรศัพท์เข้าไปในพื้นที่แข่ง FORGED.PHONE';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(q2,Forged());checks['forged_source_not_delivered']=x is None or 'FORGED.PHONE' not in x.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_model_calls':0,'owner_data_modified':False,'scope':'source-only, not event authority or whole C13'};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**report}));assert report['all_passed']
