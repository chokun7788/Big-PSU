"""Distinct guest membership and identification requirements with source controls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('guest_membership_documents_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='Does a non-PSU guest need a membership or national ID?';r=run(q);claims=r.decision_artifact.get('domain_flow',{}).get('typed_claims',[]);ids={x['record_id'] for x in claims};checks['membership_and_checkin_have_distinct_source_claims']=bool(ids&{'migrated_owner_claim_membership','migrated_policy_text_public_access_membership'}) and bool(ids&{'migrated_faq_curated_checkin_id_required','migrated_owner_claim_checkin_documents'})
checks['source_variants_and_validity_caveat_retained']='unconfirmed' in r.answer.lower() or 'confirm' in r.answer.lower()
x=run('What games are available in the studio?');checks['game_catalog_not_guest_documents']=x is None or not ({'migrated_owner_claim_membership','migrated_faq_curated_checkin_id_required'}&{c['record_id'] for c in x.decision_artifact.get('domain_flow',{}).get('typed_claims',[])})
rid='migrated_owner_claim_membership';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['answer']['value']['en']='Controlled source: membership status requires a staff decision.';save_owner_record(store,record,record['revision'],'isolated-membership-control');x=run(q);checks['actual_owner_edit_visible']=bool(x and 'Controlled source' in x.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['answer']['value']['en']='Forged membership answer.';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
x=run(q,Forged());checks['unattested_edit_not_delivered']=x is None or 'Forged membership answer.' not in x.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_http_or_model_calls':0,'owner_data_modified':False,'complete_authority_or_id_applicability_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
