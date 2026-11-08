"""Actual owner new/edit/withdraw over 24 kinds, isolated synthetic data only."""
import copy,dataclasses,hashlib,json,os,sqlite3,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-12T15:00:00+07:00')
from app.knowledge.common.registry import CATALOG,value,template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.read_graph import REQUIRED,compile,evaluate,all_of,any_of,optional,fact,not_applicable
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.grounded_plan import validate,discover
from app.knowledge.common.span_binding import bind
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.task_registry import readiness
from app.calendar.service_calendar import now_bangkok
src=R.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite';before=hashlib.sha256(src.read_bytes()).hexdigest()
db=T/'SYNTHETIC_ONLY.sqlite'
with sqlite3.connect(src.as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
store=CommonStore(db);original=store.snapshot()['release']['records'];checks=[];answers=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def ask(q,lang):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model network in source-contract cases')):
  r=CommonAnswerer(store).answer(q,locale=lang,planner=None)
 answers.append({'question':q,'locale':lang,'result':dataclasses.asdict(r) if r else None})
 with (T/'ANSWERS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(answers[-1],ensure_ascii=False)+'\n')
 return r
def publish(ids,key):
 for rid in ids:
  row=store.get(rid);store.approve(rid,row['record']['revision'],row['hash'],actor='isolated-r101-test')
 return store.publish(ids,actor='isolated-r101-test',expected_active=store.snapshot()['active'],request_key=key)
chosen={kind:next(r for r in original.values() if r['kind']==kind) for kind in CATALOG}
mapping={r['record_id']:'r101_fixture_'+kind for kind,r in chosen.items()};new={}
for kind,old in chosen.items():
 r=copy.deepcopy(old);r['fields']={**template(kind)['fields'],**r['fields']};r['record_id']=mapping[old['record_id']];r['revision']=1
 r['aliases']={'th':['ทดลองใหม่ R101 '+kind],'en':['R101 Fresh '+kind]}
 saved=save_owner_record(store,r,0,'isolated-r101-test',source_title='SYNTHETIC R101 ONLY',change_note='New category fixture, not production')['record']
 new[kind]=saved
for kind,r in new.items():
 for spec in CATALOG[kind]['fields']:
  if spec.get('reference_kind') and r['fields'][spec['key']]['status']=='known':
   v=value(r,spec['key']);r['fields'][spec['key']]['value']=[mapping.get(x,x) for x in v] if isinstance(v,list) else mapping.get(v,v)
 new[kind]=save_owner_record(store,r,r['revision'],'isolated-r101-test',change_note='Link new identities after creation')['record']
check('new records for every registered kind',set(new)==set(CATALOG))
publish([r['record_id'] for r in new.values()],'r101-new-all-24')
check('published coherent new release, 24 new identities',all(r['record_id'] in store.snapshot()['release']['records'] for r in new.values()))
for kind,r in new.items():
 for lang,alias in [('th',r['aliases']['th'][0]),('en',r['aliases']['en'][0])]:
  q=alias+(' ขอข้อมูลทั้งหมดทุกส่วน' if lang=='th' else ' give all details')
  result=ask(q,lang)
  check('new '+kind+' '+lang,result is not None and result.validation.ok and bool((result.decision_artifact or {}).get('flow_contract')),{'mode':result.mode if result else None,'errors':list(result.validation.errors) if result else []})
 report=readiness(r,store.snapshot()['release']['records'])
 check('owner graph readiness '+kind,'runtime_tasks' in report)
# Edit a schema-valid value for every kind, without changing owner approvals
# for the old version. Pick fields by actual type, avoiding enums/references.
edits={}
for kind,r in new.items():
 clone=copy.deepcopy(store.get(r['record_id'])['record']);selected=None
 preferred={'control_set':'preset','game_service':'game_version','schedule':'reason','closure':'reason','live_binding':'external_resource_key','rate':'tax_note','policy':'details','procedure':'outcome','competition_rule':'text'}.get(kind)
 for spec in CATALOG[kind]['fields']:
  key=spec['key'];v=value(clone,key);schema=spec['value_schema']
  if preferred and key!=preferred:continue
  if spec.get('reference_kind') or v is None:continue
  if isinstance(v,dict) and set(v)=={'th','en'}:
   selected=key;clone['fields'][key]['value']={k:(s or '')+' R101_EDIT' for k,s in v.items()};break
  if isinstance(v,str) and schema.get('type')=='string' and not any(k in schema for k in ('enum','const','format','pattern')):
   selected=key;clone['fields'][key]['value']=v+'R101_EDIT';break
 if selected is None:
  # Live mapping has only typed strings; an external provider key is a valid
  # isolated source change, not a fabricated live observation.
  selected=next(spec['key'] for spec in CATALOG[kind]['fields'] if type(value(clone,spec['key'])) is int)
  clone['fields'][selected]['value']+=1
 saved=save_owner_record(store,clone,clone['revision'],'isolated-r101-test',change_note='Isolated edit marker')['record']
 edits[kind]=(saved,selected)
 check('draft does not replace release '+kind,store.snapshot()['release']['records'][r['record_id']]['revision']==r['revision'])
publish([r['record_id'] for r,_ in edits.values()],'r101-edit-all-24')
for kind,(r,key) in edits.items():
 snap=store.snapshot();graph,_,_=compile('schema_attributes',[r['record_id']],snap['release']['records'],fields=[key])
 result=evaluate(graph,snap,now_bangkok())
 check('edited value re-read with new revision '+kind,result['status']=='supported' and any(p['value']==value(r,key) and p['revision']==r['revision'] for p in result['receipts']))
# Counterexamples to the graph: alternatives, optional fields, unsupported
# dependents, cross-game joins and pointer failures.
snap=store.snapshot();rs=snap['release']['records'];g=new['game']['record_id'];known=next(k for k,f in rs[g]['fields'].items() if f['status']=='known')
node=all_of(any_of(fact(g,'not_a_field'),fact(g,known)),optional(fact(g,'not_a_field')),not_applicable('no fee requested'))
check('any_of + optional + not_applicable do not over-require absent fields',evaluate(node,snap,now_bangkok())['status']=='supported')
othergame=next(k for k,r in rs.items() if r['kind']=='game' and k!=g)
from app.knowledge.common.read_graph import linked
targets,_=linked(rs,[g],'game_players')
check('reverse mode read cannot cross through shared service to another game',all(value(rs[k],'game_id')==g for k in targets))
check('Unicode case span binding preserves original text',bind('HOW TO PLAY VALORANT?','valorant')['quote']=='VALORANT')
rows,explicit=discover('R101 Fresh game what is this game?',rs,snap['release']['names'])
proposal={'needs':[{'task':'game_overview','record_ids':[g],'quote':'R101 Fresh game what is this game?'}],'unresolved':[]}
plan,reason=validate(proposal,'R101 Fresh game what is this game?',rows,rs,explicit)
check('whole semantic proposal binds owner-added identity',plan is not None,reason)
bad=copy.deepcopy(proposal);bad['needs'][0]['quote']='what is this game?'
check('semantic proposal cannot silently drop subject or clause',validate(bad,'R101 Fresh game what is this game?',rows,rs,explicit)[0] is None)
with request_context() as ctx:
 check('semantic attempt budget is shared',ctx.reserve_semantic() and not ctx.reserve_semantic())
 check('one corrective read budget is shared',ctx.reserve_corrective() and not ctx.reserve_corrective())
remaining=dict(edits)
while remaining:
 progress=False
 for kind,(r,key) in list(remaining.items()):
  snap=store.snapshot();revoked=set(snap.get('withdrawn',[]))
  if any(rid not in revoked and rid!=r['record_id'] for rid in snap['release']['reverse_refs'].get(r['record_id'],[])):continue
  store.withdraw(r['record_id'],actor='isolated-r101-test');progress=True;del remaining[kind]
  snap=store.snapshot();node=fact(r['record_id'],key)
  check('withdrawn data cannot produce receipts '+kind,evaluate(node,snap,now_bangkok())['status']=='broken_relation')
 if not progress:raise AssertionError('Fixture withdrawal cycle: '+repr(list(remaining)))
check('original synthetic fixture untouched',hashlib.sha256(src.read_bytes()).hexdigest()==before)
(T/'ANSWERS.json').write_text(json.dumps(answers,ensure_ascii=False,indent=2),'utf8')
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],
 'kinds':len(new),'chat_requests':len(answers),'live_observations':0,'model_calls':0,'data':'isolated synthetic only','original_unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==before}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
