"""Source-bound CS2 map-selection controls; no model calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('map_selection_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def claims(r):return {c['record_id'] for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if r else set()
q='ช่วยดูหน่อย Counter-Strike 2 แข่งจริง กฎเกี่ยวกับแผนที่และการเลือกแผนที่ เป็นแบบไหน ครับ';rid='competition_competition_rules_cs2_psu_phuket_2026_section_031';x=run(q);checks['correct_map_source']=rid in claims(x);checks['mismatched_heading_bodies_not_delivered']=not bool(claims(x)&{'r114_cs2_33_rule_clause','r114_cs2_34_rule_clause'});checks['incomplete_event_scope_disclosed']=bool(x and 'ความครบถ้วน' in x.answer and 'ตรวจสอบ' in x.answer)
x=run('TEKKEN 8 กติกาการเลือกแผนที่เป็นอย่างไร');checks['other_game_not_cs2']=rid not in claims(x)
x=run('ราคา PC เท่าไหร่');checks['price_not_map']=rid not in claims(x)
x=run('How is map selection done in Counter-Strike 2 competition?');checks['english_map_source']=rid in claims(x) and not bool(claims(x)&{'r114_cs2_33_rule_clause','r114_cs2_34_rule_clause'})
x=run('กติกาการเลือกแผนที่ CS2 เป็นอย่างไร และราคา PC เท่าไหร่');checks['compound_map_and_price']=bool(x and rid in claims(x) and any('rate' in c.lower() for c in claims(x)))
record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['text']['value']['th']='1. การเลือกแผนที่ ใช้ OWNER-EDIT.TEST';record['fields']['text']['value']['en']='1. Map selection uses OWNER-EDIT.TEST';save_owner_record(store,record,record['revision'],'isolated-map-selection-control');x=run(q);checks['owner_edit_visible']=bool(x and 'OWNER-EDIT.TEST' in x.answer and rid in claims(x))
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['text']['value']['th']='1. การเลือกแผนที่ ใช้ FORGED.TEST';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(q,Forged());checks['forged_source_not_delivered']=x is None or 'FORGED.TEST' not in x.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_model_calls':0,'owner_data_modified':False,'scope':'source-only, not whole C13 or authority'};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**report}));assert report['all_passed']
