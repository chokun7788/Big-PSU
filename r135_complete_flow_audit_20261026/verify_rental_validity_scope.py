"""Unknown source interval is disclosed; it is not fabricated owner policy."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.projection import title
O=R/('rental_validity_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);record=copy.deepcopy(view.snapshot()['release']['records']['package_9']);name=title(record);checks={};details=[]
def run(q):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 c=r.decision_artifact['execution_contract'];claims=[v for ex in c['executor_results'] for v in ex.get('claims',[])];details.append({'q':q,'answer':r.answer,'artifact':r.decision_artifact});return r,claims
r,claims=run('แพ็กเกจ '+name['th']+' ราคาเท่าไหร่');checks['actual_unknown_package_price_interval_disclosed']='ช่วงวันที่มีผลยังไม่ยืนยัน' in r.answer and r.decision_artifact['response_type']=='partial_answer' and any(c['record_id']=='package_9' and c['numeric']==3000 for c in claims)
r,claims=run('What is the price of '+name['en']+'?');checks['english_unknown_interval_disclosed']='effective interval is unconfirmed' in r.answer and r.decision_artifact['response_type']=='partial_answer' and any(c['numeric']==3000 for c in claims)
r,claims=run('ห้อง '+name['th']+' มีที่นั่งกี่ที่');checks['nonprice_package_field_does_not_claim_current_interval']='ช่วงวันที่มีผลยังไม่ยืนยัน' in r.answer and any(c['facet']=='room_seats' and c['numeric']==34 for c in claims)
def interval(start,end):
 r=copy.deepcopy(view.snapshot()['release']['records']['package_9']);r['validity']={'state':'known','effective_from':start,'effective_until':end};save_owner_record(store,r,r['revision'],'isolated-source-control')
interval('2026-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00');r,claims=run('แพ็กเกจ '+name['th']+' ราคาเท่าไหร่');checks['actual_owner_known_current_interval_no_unknown_warning']='ช่วงวันที่มีผลยังไม่ยืนยัน' not in r.answer and any(c['record_id']=='package_9' and c['numeric']==3000 for c in claims)
interval('2020-01-01T00:00:00+07:00','2021-01-01T00:00:00+07:00');r,claims=run('แพ็กเกจ '+name['th']+' ราคาเท่าไหร่');checks['expired_package_price_not_current_confirmation']=not claims and '3000' not in r.answer
interval('2027-01-01T00:00:00+07:00','2028-01-01T00:00:00+07:00');r,claims=run('แพ็กเกจ '+name['th']+' มีอุปกรณ์อะไรให้');checks['future_package_nonprice_field_not_current_confirmation']=not claims
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'owner_interval_facts_invented':False,'whole_rental_category_accepted':False,'scope':'Actual owner source interval controls on an isolated copy; currentness of real unknown owner data remains unknown.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
