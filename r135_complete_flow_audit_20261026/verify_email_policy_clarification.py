"""Do not replace an unspecified email policy with a contact address."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('email_policy_clarification_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
r=run('Could you please help me with this: What is the studio policy for e-mail');checks['ambiguous_policy_clarifies_without_address']=bool(r and 'Which email policy' in r.answer and '@' not in r.answer and not r.decision_artifact.get('domain_flow',{}).get('typed_claims'))
r=run('What is the studio contact email address?');checks['direct_address_not_replaced_by_clarification']=bool(r and '@' in r.answer and 'Which email policy' not in r.answer)
r=run('What is the cancellation policy for a studio booking?');checks['other_policy_not_replaced_by_email_prompt']=r is None or 'Which email policy' not in r.answer
r=run('What is the studio email address and also what is its physical address?');checks['both_email_and_physical_address_retained']=bool(r and '@' in r.answer and 'Building 5' in r.answer)
rid='migrated_faq_rule_contact_email';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['answer']['value']['en']='Contact email is controlled@example.org.';save_owner_record(store,record,record['revision'],'isolated-email-source-control')
r=run('What is the studio contact email address?');checks['actual_source_edit_visible']=bool(r and 'controlled@example.org' in r.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['answer']['value']['en']='Contact email is forged@example.org.';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run('What is the studio contact email address?',Forged());checks['unattested_email_not_delivered']=r is None or 'forged@example.org' not in r.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_http_or_inference':False,'owner_data_modified':False,'policy_semantics_verified':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
