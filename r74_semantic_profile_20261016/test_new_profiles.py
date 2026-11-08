"""Source-backed isolated fixtures, normal dispatcher and real SQLite revisions."""
import copy,hashlib,json,os,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
S=B/'system';fixture_system=T/'system';db=fixture_system/'data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
source_db=S/'data/knowledge/common.sqlite';dbhash=hashlib.sha256(source_db.read_bytes()).hexdigest()
a=sqlite3.connect(source_db.as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db)
try:a.backup(z)
finally:z.close();a.close()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_BILINGUAL_EN_ENABLED='1')
sys.path.insert(0,str(S))
from app.knowledge.common import migrated_view
migrated_view.SYSTEM_ROOT=fixture_system.resolve()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,now,validate,schema_errors
from app.knowledge.records import canonical_json
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
store=CommonStore(db);checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(json.dumps({'case':name,'passed':bool(ok)}),flush=True)
def save(record,values):
 try:expected=store.get(record['record_id'])['record']['revision']
 except ValueError:expected=0
 raw=canonical_json(values);sid='fixture_r73_'+hashlib.sha256(raw.encode()).hexdigest()[:26]
 source={'source_id':sid,'kind':'derived_curated','path':'isolated-fixture://'+sid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[record['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 store.add_source(source,raw,actor='automated-isolated-fixture')
 for key,val in values.items():record['fields'][key]={'status':'known','value':val,'evidence_refs':[{'source_id':sid,'locator':'/'+key}],'note':'ISOLATED FIXTURE, not production facts'}
 store.save(record,actor='automated-isolated-fixture',expected_version=expected,change_note='Fixture only')
 return store.get(record['record_id'])['record']
def ask(q,lang='en'):
 loc=LocaleDecision(lang,lang,lang,1,'explicit_test_locale');r=answer(q,locale=loc,allow_llm=True)
 return r,{'answer':r.answer,'mode':r.mode,'artifact':r.decision_artifact,'hits':r.hits}
profile={'task':'permission','subjects':[{'th':'แผงฟ้าทดสอบ','en':'cobaltpad'}],'ownership':'personal','context':'studio'}
record=template('faq');record.update(record_id='fixture_r73_subject_410',aliases={'th':[],'en':[]})
record['localization']['en_status']='agent_translated'
record=save(record,{'question':{'th':'หัวข้อตัวอย่าง 410','en':'Example topic 410'},'answer':{'th':'ข้อมูลตัวอย่างแยก RULE_V1','en':'ISOLATED FIXTURE RULE_V1'},'topic':'fixture_topic','query_profile':profile})
r,d=ask('Can I use my own cobaltpad?');check('New unseen subject is read without router or record alias changes','RULE_V1' in r.answer and d['artifact'].get('query_plan',{}).get('method')=='declared_question_profile',d)
r,d=ask('ใช้แผงฟ้าทดสอบส่วนตัวได้ไหม','th');check('New Thai subject is read from the same metadata','RULE_V1' in r.answer,d)
old=migrated_view.MigratedView(db).snapshot()
record=save(record,{'answer':{'th':'ข้อมูลตัวอย่างแยก RULE_V2','en':'ISOLATED FIXTURE RULE_V2'}})
r,d=ask('Can I use my own cobaltpad?');check('Updated source revision is read immediately','RULE_V2' in r.answer and 'RULE_V1' not in r.answer,d)
check('Epoch invalidates old snapshot',not migrated_view.MigratedView(db).still_current(old))
check('Previous revision remains available',store.revision(record['record_id'],1)['record']['fields']['answer']['value']['en']=='ISOLATED FIXTURE RULE_V1')
r,d=ask('Can I use my own cobaltpad at a tournament?');check('Studio profile cannot answer a competition context','RULE_V2' not in r.answer,d)
r,d=ask('Can I buy my own cobaltpad?');check('Permission profile does not answer a purchase question',d['artifact'].get('query_plan',{}).get('method')!='declared_question_profile',d)
duplicate=copy.deepcopy(record);duplicate['record_id']='fixture_r73_conflict_411';duplicate['revision']=1
duplicate=save(duplicate,{'question':{'th':'หัวข้อตัวอย่างอีกขอบเขต','en':'Another fixture scope'},'answer':{'th':'ข้อมูลแยก RULE_CONFLICT','en':'ISOLATED FIXTURE RULE_CONFLICT'}})
r,d=ask('Can I use my own cobaltpad?');check('Conflicting matching profiles require clarification',r.mode=='pipeline:common_clarification' and 'RULE_V2' not in r.answer and 'RULE_CONFLICT' not in r.answer,d)
store.withdraw(duplicate['record_id'],actor='automated-isolated-fixture')
r,d=ask('Can I use my own cobaltpad?');check('Withdrawal removes conflicting profile from selection','RULE_V2' in r.answer,d)
for field,bad in [('task','invent_answer'),('subjects',[]),('subjects',[{'th':'','en':''}]),('context','all_contexts')]:
 broken=copy.deepcopy(record);broken['fields']['query_profile']['value'][field]=bad
 check('Reject invalid profile '+field+' '+str(bad),bool(schema_errors(broken)))
unknown=copy.deepcopy(record);unknown['fields']['query_profile']={'status':'unknown','value':None,'evidence_refs':[],'note':'Unconfirmed routing scope in isolated fixture'}
store.save(unknown,actor='automated-isolated-fixture',expected_version=record['revision'])
r,d=ask('Can I use my own cobaltpad?');check('Unknown metadata is not used as a declared scope',d['artifact'].get('query_plan',{}).get('method')!='declared_question_profile',d)
store.withdraw(record['record_id'],actor='automated-isolated-fixture')
r,d=ask('Can I use my own cobaltpad?');check('Withdrawn source facts are not revived by metadata','RULE_V2' not in r.answer,d)
procedure=template('procedure');procedure.update(record_id='fixture_r73_procedure_512',aliases={'th':[],'en':[]})
procedure['localization']['en_status']='agent_translated'
procedure=save(procedure,{'name':{'th':'แก้ตัวอย่างป้าย','en':'Correct a fixture badge'},'topic':'fixture_badge','preconditions':[{'field':'issue','operator':'eq','value':'fixture_badge'}],'steps':[{'order':1,'instruction':{'th':'ข้อมูลแยก ขั้นตอน STEP_512','en':'ISOLATED FIXTURE STEP_512'},'contact_id':None}],'query_profile':{'task':'correction','subjects':[{'th':'ป้ายทดสอบ','en':'samplebadge'}],'ownership':'any','context':'studio'}})
r,d=ask('My samplebadge is wrong. How do I correct it?');check('New correction procedure uses the same profile mechanism','STEP_512' in r.answer and 'issue' not in r.answer,d)
policy=template('policy');policy.update(record_id='fixture_r73_policy_613',aliases={'th':[],'en':[]})
policy['localization']['en_status']='agent_translated'
policy=save(policy,{'subject':{'th':'ตัวอย่างวัตถุเขียว','en':'Fixture green item'},'topic':'fixture_green','decision':'conditional','details':{'th':'ข้อมูลแยก POLICY_613 ใช้เฉพาะจุด A','en':'ISOLATED FIXTURE POLICY_613, only at desk A.'},'conditions_all':[{'field':'desk','operator':'eq','value':'A'}],'exceptions':{'th':'ข้อมูลแยก ยกเว้นวันที่ปิดทดสอบ','en':'ISOLATED FIXTURE except on test closure dates.'},'query_profile':{'task':'permission','subjects':[{'th':'วัตถุเขียวทดสอบ','en':'greenfixture'}],'ownership':'personal','context':'studio'}})
r,d=ask('Can I use my personal greenfixture?');check('Policy projection preserves decision, conditions and exceptions','Conditional' in r.answer and 'POLICY_613' in r.answer and 'desk' in r.answer and 'closure' in r.answer,d)
with store.connect() as c:
 rs=store.heads(c);ss=store.sources(c);errors={rid:validate(r,rs,ss) for rid,r in rs.items() if validate(r,rs,ss)}
 check('All old and fixture records validate with optional profile field',not errors,errors)
 check('No approvals or active publication created',c.execute('select count(*) from cc_approvals').fetchone()[0]==0 and dict(c.execute('select key,value from cc_meta'))['active']=='')
check('Actual R73 database unchanged by fixture run',dbhash==hashlib.sha256(source_db.read_bytes()).hexdigest())
result={'cases':len(checks),'passed':sum(x['passed'] for x in checks),'llm_enabled':True,'scope':'isolated SQLite fixtures, real common dispatcher; no model transport/browser or owner approval claim','details':checks}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='details'}))
raise SystemExit(any(not x['passed'] for x in checks))
