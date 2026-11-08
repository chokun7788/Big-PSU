"""Exact source rate duration vs unsupported alternative; no model calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('exact_rate_duration_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='How much does it cost for a student from another university to play Cockpit for one hour, and how do I book it?';a=run(q);a_json=json.dumps(a.decision_artifact);checks['actual_exact_duration_supported']= 'exact_single_source_rate_duration_and_scoped_receipt_recomputed' in a_json and 'Application of these requested constraints remains unverified: 1 hour' not in a.answer
checks['booking_and_rate_both_retained']='Booking steps' in a.answer and '65 THB for 60 minutes' in a.answer
b=run('How much does a PSU student pay to play VR for 1 hour or 2 hours');checks['alternatives_not_pretended_complete']='2 hours' in b.answer and 'unverified' in b.answer.lower()
rid='migrated_rate_cockpit_60_1_1_psu_alumni_general_student';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['duration_minutes']['value']=90;save_owner_record(store,record,record['revision'],'isolated-duration-source-control');c=run(q);checks['changed_source_duration_no_stale_60_minute_proof']='exact_single_source_rate_duration_and_scoped_receipt_recomputed' not in json.dumps(c.decision_artifact)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['duration_minutes']['value']=60;s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
d=run(q,Forged());checks['unattested_duration_does_not_prove_scope']=d.decision_artifact['response_type']=='retry' and all(not n.get('claim_packets') for n in d.decision_artifact.get('need_results',[]))
report={'checks':checks,'all_passed':all(checks.values()),'actual_http_or_model_calls':0,'owner_data_modified':False,'alternative_duration_semantics_complete':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
