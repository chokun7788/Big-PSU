"""Actual event-source controls; no claim of tournament authority."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('event_applicability_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='Please tell me: I am preparing for a AOV match. What is the policy for the competition format? please.';rid='competition_competition_rules_rov_blueket_2025_men_section_005'
claims=lambda x:{c['record_id'] for c in x.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if x else set()
r=run(q); scopes=[z.get('requested_scope',{}) for n in r.decision_artifact.get('need_results',[]) for z in n.get('execution_contract',{}).get('receipts',[])] if r else [];checks['unbound_event_scope_not_falsely_verified']=bool(scopes and all(not x.get('verified') and not x.get('target_binding_verified') for x in scopes));checks['unspecified_match_caveat_and_scoped_source']=bool(r and rid in claims(r) and 'displayed event rules apply to your match' in r.answer and 'Blueket' in r.answer)
r=run('Under Blueket Games 2025 Men\'s Team AOV tournament rules what is the competition format?'); scopes=[z.get('requested_scope',{}) for n in r.decision_artifact.get('need_results',[]) for z in n.get('execution_contract',{}).get('receipts',[])] if r else [];checks['explicit_named_event_scope_verified']=bool(scopes and all(x.get('verified') and x.get('target_binding_verified') for x in scopes));checks['named_event_source_preserved']=bool(r and rid in claims(r) and 'BO3' in r.answer)
r=run('What is the price for playing AOV?');checks['price_does_not_inherit_rule']=rid not in claims(r)
record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['text']['value']['en']+=' Controlled source revision.';save_owner_record(store,record,record['revision'],'isolated-event-source-control');r=run(q);checks['owner_edit_visible_with_caveat']=bool(r and 'Controlled source revision' in r.answer and 'displayed event rules apply' in r.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['text']['value']['en']='Forged competition format';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run(q,Forged());checks['unattested_clause_not_delivered']=r is None or 'Forged competition format' not in r.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_http_or_inference':False,'owner_data_modified':False,'authority_or_rulebook_completeness_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
