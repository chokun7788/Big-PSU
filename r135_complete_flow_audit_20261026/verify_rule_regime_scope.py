"""Independent source controls for regulation and overtime rule scopes."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('rule_regime_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);original=view.snapshot();checks={};details=[]
reg='competition_competition_rules_cs2_psu_phuket_2026_section_025';ot='competition_competition_rules_cs2_psu_phuket_2026_section_027'
q='Could you help me? Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?'
def run(question,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(question,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 assert r is not None
 details.append({'question':question,'answer':r.answer,'artifact':r.decision_artifact});return r
r=run(q);encoded=json.dumps(r.decision_artifact);checks['actual_source_both_regimes_selected']=reg in encoded and ot in encoded and '$800' in r.answer and '$10,000' in r.answer
checks['unresolved_rulebook_coverage_disclosed']='not confirmed all linked rule clauses' in r.answer and 'complete' in r.answer
checks['contextual_overtime_not_mistaken_for_round_duration']='1:55' not in r.answer
r=run('Under CS2 tournament rules, what are starting money and bomb time in regulation?');checks['regulation_alone_does_not_include_overtime']='$800' in r.answer and '$10,000' not in r.answer
r=run('Under CS2 tournament rules, what are overtime rounds and starting money?');checks['overtime_alone_does_not_include_regulation']='$10,000' in r.answer and 'Bomb time: 40' not in r.answer
r=run('Under VALORANT tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?');checks['different_game_cannot_borrow_cs2_values_or_timeout_clause']='$10,000' not in r.answer and '$800' not in r.answer and 'Tactical Timeout' not in r.answer
class Variant:
 path=view.path
 def __init__(self,change):self.change=change
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());self.change(s);s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run(q,Variant(lambda s:s['release']['records'].pop(ot)));checks['missing_overtime_not_invented']='$10,000' not in r.answer and ('unconfirmed' in r.answer.lower() or 'not confirmed' in r.answer.lower() or 'retry' in r.answer.lower())
def forge(s):
 x=s['release']['records'][reg];x['fields']['text']['value']={'en':'Initial amount: $9999 | Bomb time: 40 seconds','th':'เงินเริ่มต้น $9999 | เวลาของระเบิด 40 วินาที'}
r=run(q,Variant(forge));checks['forged_body_fails_source_attestation']='$9999' not in r.answer
for rid,old,new in [(reg,'$800','$1200'),(ot,'$10,000','$12,000')]:
 x=copy.deepcopy(view.snapshot()['release']['records'][rid])
 for key in ['heading','text']:
  for lang,value in x['fields'][key]['value'].items():x['fields'][key]['value'][lang]=value.replace(old,new)
 save_owner_record(store,x,x['revision'],'isolated-rule-regime-control')
r=run(q);checks['actual_authorized_source_edits_update_both_clauses']='$1200' in r.answer and '$12,000' in r.answer and '$800' not in r.answer and '$10,000' not in r.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_or_http_calls':0,'actual_owner_or_frozen_data_modified':False,'whole_rulebook_or_authority_accepted':False,'scope':'Recorded source-bound regime clauses, not proof of complete rulebook.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
