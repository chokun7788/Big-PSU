"""Specific source-bound player boosting, not a general exploit judgment."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('valorant_boost_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='Under VALORANT tournament rules, may teammates boost a player above normal jump height?';rid='competition_competition_rules_valorant_psu_phuket_2026_section_025';claims=lambda r:{c['record_id'] for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if r else set();r=run(q);checks['source_specific_boost_rule_present']=rid in claims(r) and 'boost' in r.answer.lower() and 'prohibited' in r.answer.lower();checks['authority_or_complete_rulebook_not_claimed']='not confirmed' in r.answer.lower()
x=run('Under CS2 tournament rules, may teammates boost a player above normal jump height?');checks['other_game_cannot_receive_valorant_rule']=rid not in claims(x)
x=run('What is the price for playing VALORANT?');checks['price_is_not_competition_boost']=rid not in claims(x)
record=copy.deepcopy(view.snapshot()['release']['records'][rid]);
for lang in ['th','en']:record['fields']['text']['value'][lang]=record['fields']['text']['value'][lang].replace('is prohibited','is prohibited pending controlled review')
save_owner_record(store,record,record['revision'],'isolated-boost-source-control');x=run(q);checks['actual_source_edit_visible']=bool(x and 'pending controlled review' in x.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['text']['value']['en']='Using teammates to boost to locations higher than normal jump height is prohibited by forged clause.';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
f=run(q,Forged());checks['unattested_clause_suppressed']=f is None or 'forged clause' not in f.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_model_calls':0,'owner_data_modified':False,'authority_or_rulebook_completeness_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
