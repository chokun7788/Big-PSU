"""Check actual source receipt for rate calculations, not historical R132 grade."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('rate_calculation_receipt_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R.parent/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();view=DraftSnapshotView(CommonStore(O/'source.sqlite'));details=[];checks={}
for name,q in [('thirty','นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท'),('three_hours','How much does a PSU student pay to play PC for 3 hours?')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});raw=json.dumps(r.decision_artifact,ensure_ascii=False) if r else ''
 checks[name+'_calculation_rule_locator']= '/mapped_fields/calculation_rule' in raw
 checks[name+'_zero_and_validity_caveat']=bool(r and '0' in r.answer and ('2026-10-16' in r.answer or 'ยืนยัน' in r.answer))
ids=['rate_recovered_pc_availability_pc_01_02_psu_student_staff','rate_recovered_pc_availability_pc_03_10_psu_student_staff']
q='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท'
for rid in ids:
 record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['calculation_rule']['value']='no_extrapolation';save_owner_record(view.store,record,record['revision'],'isolated-rate-rule-control')
with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(view).answer(q,locale='th',at='2026-10-16T12:00:00+07:00',planner=None)
details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None,'case':'owner_rule_changed'})
checks['changed_rule_does_not_deliver_30_minute_zero']=bool(r and any(n.get('terminal_state')=='partial' and any('30 นาที' in str(o.get('expected')) and o.get('fulfilled') is False for o in n.get('execution_contract',{}).get('obligations',[])) for n in r.decision_artifact.get('need_results',[])) and all('30 นาที' not in str(c.get('value')) for n in r.decision_artifact.get('need_results',[]) for c in n.get('claim_packets',[])))
class Forged:
 path=view.path
 def connect(self):return view.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot())
  for rid in ids:s['release']['records'][rid]['fields']['calculation_rule']['value']='session_ceil'
  s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(Forged()).answer(q,locale='th',at='2026-10-16T12:00:00+07:00',planner=None)
details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None,'case':'forged_rule'})
checks['forged_rule_does_not_deliver_30_minute_zero']=r is None or not ('0 บาท' in r.answer and '30 นาที' in r.answer)
result={'checks':checks,'all_passed':all(checks.values()),'source_only':True,'http_or_inference':False,'historical_r132_regraded':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**result}));assert result['all_passed']
