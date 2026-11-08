"""Event title binding after an actual isolated owner edit and forged snapshot."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('named_event_owner_edit_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={};event='competition_competition_rules_rov_blueket_2025_men';old="Under Blueket Games 2025 Men's Team AOV tournament rules what is the competition format?";new='Under Controlled Tournament 2025 Men AOV tournament rules what is the competition format?'
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def scopes(r):return [z.get('requested_scope',{}) for n in (r.decision_artifact.get('need_results',[]) if r else []) for z in n.get('execution_contract',{}).get('receipts',[])]
r=run(old);checks['initial_exact_event_bound']=bool(scopes(r) and all(x.get('verified') and x.get('target_binding_verified') for x in scopes(r)))
record=copy.deepcopy(view.snapshot()['release']['records'][event]);record['fields']['event_name']['value']={'en':'Controlled Tournament 2025 Men','th':'รายการควบคุม 2025 ชาย'};save_owner_record(store,record,record['revision'],'isolated-event-rename-control')
r=run(old);checks['old_full_title_no_longer_verified']=not any(x.get('verified') and 'explicit_full_source_event_title_and_typed_game_relation' in x.get('basis',[]) for x in scopes(r))
r=run(new);checks['new_source_title_verified']=bool(scopes(r) and any(x.get('verified') and 'explicit_full_source_event_title_and_typed_game_relation' in x.get('basis',[]) for x in scopes(r)))
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][event]['fields']['event_name']['value']['en']='Forged Tournament 2025 Men';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run('Under Forged Tournament 2025 Men AOV tournament rules what is the competition format?',Forged());checks['forged_title_not_authorized']=not any(x.get('verified') for x in scopes(r))
result={'checks':checks,'all_passed':all(checks.values()),'http_or_inference':False,'owner_data_modified':False,'rulebook_authority_or_completeness_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),**result}));assert result['all_passed']
