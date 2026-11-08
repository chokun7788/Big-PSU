"""Synthetic owner workflow in a new isolated DB; no real approvals or facts."""
import copy,dataclasses,json,os,sys
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B/'system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0')
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'system/app/knowledge/common'))
if True:
 import app.pipeline as pipeline_pkg;pipeline_pkg.__path__.insert(0,str(B/'system/app/pipeline'))
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore,Conflict
from app.knowledge.common.owner_server import save_owner_record,preview_answer
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
db=T/'ISOLATED_NOT_PRODUCTION.sqlite';store=CommonStore(db);store.initialize();checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def new(kind,rid,values):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 return save(r,values,0)
def save(r,values,rev=None):
 for key,val in values.items():r['fields'][key]={'status':'known','value':val,'note':'ISOLATED SYNTHETIC TEST; NOT REAL STUDIO DATA','evidence_refs':[]}
 return save_owner_record(store,r,r['revision'] if rev is None else rev,'isolated_test_actor',source_title='SYNTHETIC OWNER FORM TEST',change_note='Only isolated test DB')['record']
def publish(ids,key):
 for rid in ids:
  row=store.get(rid);store.approve(rid,row['record']['revision'],row['hash'],actor='isolated_test_actor')
 return store.publish(ids,actor='isolated_test_actor',expected_active=store.snapshot()['active'],request_key=key)
def ask(q,lang='th',history=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No network in owner lifecycle fixture')):
  return CommonAnswerer(store).answer(q,locale=lang,history=history or [],planner=None)
def history(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
g=new('game','fixture_aurora_paths',{'title':{'th':'เส้นทางออโรร่า ข้อมูลทดลอง','en':'Aurora Paths Fixture'},'summary':{'th':'เกมทดลองสำรวจเส้นทาง VERSION_ONE','en':'An exploration fixture game VERSION_ONE'},'genre':{'th':'ผจญภัยทดลอง','en':'Fixture adventure'},'how_to_play':{'th':'เดินตามเส้นทางและแก้ปริศนา METHOD_ONE','en':'Follow paths and solve puzzles METHOD_ONE'}})
q='เส้นทางออโรร่า ข้อมูลทดลอง คือกมอะๆร'
check('Unpublished new game is not visible in published reader',ask(q) is None)
preview=preview_answer(store,q,locale='th',draft=True)
check('Owner draft preview uses the same task interpretation','VERSION_ONE' in preview.answer,dataclasses.asdict(preview))
publish([g['record_id']],'game-v1')
for lang,qry in [('th',q),('en','Aurora Paths Fixture what is this gmae?'),('en','Aurora Paths Fixture how do you play?')]:
 r=ask(qry,lang);marker='METHOD_ONE' if 'how do' in qry else 'VERSION_ONE'
 check('New game no code changes: '+lang+' '+marker,r.validation.ok and marker in r.answer,dataclasses.asdict(r))
old=ask(q);h=history(q,old)
g=save(store.get(g['record_id'])['record'],{'summary':{'th':'ข้อมูลเกมฉบับแก้ VERSION_TWO','en':'Revised fixture game VERSION_TWO'}})
check('Editing draft does not replace published facts yet','VERSION_ONE' in ask(q).answer)
try:store.publish([g['record_id']],actor='isolated_test_actor',expected_active=store.snapshot()['active'],request_key='unapproved');blocked=False
except Conflict:blocked=True
check('Old approval cannot publish new revision',blocked)
publish([g['record_id']],'game-v2')
r=ask('summary',history=h)
check('Follow-up reads newly published revision instead of old answer','VERSION_TWO' in r.answer and 'VERSION_ONE' not in r.answer,dataclasses.asdict(r))
f=new('faq','fixture_moonlight_policy',{'question':{'th':'นโยบายคืนแสงจันทร์ ข้อมูลทดลอง','en':'Moonlight policy fixture'},'answer':{'th':'นโยบายทดลอง POLICY_ONE','en':'Synthetic policy POLICY_ONE'},'topic':'fixture_only'})
publish([f['record_id']],'faq-v1')
r=ask('What is the policy for Moonlight policy fixture?','en')
check('New FAQ content read by task without custom router','POLICY_ONE' in r.answer,dataclasses.asdict(r))
f=save(store.get(f['record_id'])['record'],{'answer':{'th':'นโยบายทดลองฉบับแก้ POLICY_TWO','en':'Revised synthetic policy POLICY_TWO'}});publish([f['record_id']],'faq-v2')
r=ask('What is the policy for Moonlight policy fixture?','en')
check('FAQ edit takes effect without changing task grammar','POLICY_TWO' in r.answer and 'POLICY_ONE' not in r.answer,dataclasses.asdict(r))
z=new('zone','fixture_aurora_zone',{'name':{'th':'โซนออโรร่าทดลอง','en':'Aurora Test Zone'}})
e=new('equipment_model','fixture_aurora_pad',{'name':{'th':'แพดออโรร่าทดลอง','en':'Aurora Fixture Pad'},'device_type':'peripheral','specifications':[{'key':'zone','value':'Aurora Test Zone','unit':None}]})
publish([z['record_id'],e['record_id']],'equipment-v1')
r=ask('Aurora Test Zone equipment list','en')
check('New equipment relation supports list without game/shop constants','Aurora Fixture Pad' in r.answer and r.validation.ok,dataclasses.asdict(r))
store.withdraw(g['record_id'],actor='isolated_test_actor');r=ask(q)
check('Withdrawn game is not resurrected from old release/state',r is None or 'VERSION_TWO' not in r.answer)
r=ask('summary',history=h)
check('Withdrawn game facts do not leak through old conversation state',r is None or 'VERSION_TWO' not in r.answer and 'VERSION_ONE' not in r.answer)
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'isolated_database':str(db),'simulated_approvals_only':True,'real_owner_approvals_created':False,'new_record_kinds':['game','faq','zone','equipment_model'],'model_calls':0}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed']))
