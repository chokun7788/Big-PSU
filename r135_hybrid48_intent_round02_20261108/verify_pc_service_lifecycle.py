"""Owner mutations and answer checks against a private SQLite backup."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
out=R/('pc_service_lifecycle_'+str(time.time_ns()));out.mkdir()
src=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(out/'source.sqlite');src.backup(dst);src.close();dst.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
view=DraftSnapshotView(CommonStore(out/'source.sqlite'));answerer=CommonAnswerer(view);rows=[];checks={}
def ask(label):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
  r=answerer.answer('PC ราคาเท่าไหร่',locale='th',at='2026-11-08T12:00:00+07:00',planner=None)
 rows.append({'stage':label,'answer':r.answer,'artifact':r.decision_artifact});return r
baseline=ask('before');checks['before_both_services']='PC #01-#02' in baseline.answer and 'PC #03-#10' in baseline.answer
rid='availability_pc_01_02';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['name']['value']={'th':'เครื่องทดลอง A','en':'Test Station A'}
save_owner_record(view.store,record,record['revision'],'isolated-service-name-edit')
edited=ask('renamed');checks['edited_service_name_visible']='เครื่องทดลอง A' in edited.answer;checks['other_service_retained']='PC #03-#10' in edited.answer
rate='rate_recovered_pc_availability_pc_01_02_general_adult';record=copy.deepcopy(view.snapshot()['release']['records'][rate]);record['fields']['amount_minor']['value']=7300
save_owner_record(view.store,record,record['revision'],'isolated-rate-edit')
changed=ask('rate_changed');claims=changed.decision_artifact.get('domain_flow',{}).get('typed_claims',[])
checks['changed_rate_not_stale']=all(c.get('numeric')!=70 for c in claims if c.get('record_id')==rate)
view.store.withdraw(rate,actor='isolated-rate-withdrawal');withdrawn=ask('rate_withdrawn');claims=withdrawn.decision_artifact.get('domain_flow',{}).get('typed_claims',[])
checks['withdrawn_rate_not_claimed']=all(c.get('record_id')!=rate for c in claims);checks['other_rates_still_delivered']=any(c.get('record_id')!=rate and c.get('facet')=='amount' for c in claims)
report={'checks':checks,'all_passed':all(checks.values()),'scope':'isolated owner operation and source-only natural response; no HTTP, model or authority proof','model_calls':0}
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}),flush=True);assert report['all_passed']
