"""R102 source/authority/schema/lifecycle checks, part of integrated batch only."""
import os,sys,json,copy,dataclasses,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path[:0]=[str(R/'system'),str(R)]
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-20T12:00:00+07:00')
from scenario_support import Fixture,bi,AT
from app.knowledge.common.registry import VERSION,template,validate,release_errors,schema_errors
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.claim_bindings import conflicts,current_claims
from app.knowledge.common.grounded_plan import validate as validate_plan
from app.knowledge.common.request_plan import make_plan
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.read_graph import compile,evaluate
f=Fixture.clone(T/'SYNTHETIC_ONLY.sqlite',R/'fixtures/BASE_SYNTHETIC.sqlite');checks=[]
def check(case,ok,detail=None):
 row={'case':case,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(case,bool(ok),flush=True)
def snap():return DraftSnapshotView(f.store).snapshot()
def record_fields(kind,fields):return f.new(kind,'fx_'+kind+'_extra',fields)
check('registry supports 24 kinds and 32 task graphs',len(__import__('app.knowledge.common.registry',fromlist=['CATALOG']).CATALOG)==24 and len(__import__('app.knowledge.common.task_contracts',fromlist=['TASKS']).TASKS)==32)
old=template('game');old.pop('claim_bindings');old['schema_version']='studio-content-3.0';old['record_id']='fx_legacy_payload'
check('schema 3.0 payload remains accepted',not schema_errors(old))
r=f.new('faq','fx_price_faq',{'question':bi('ราคา PC ภายนอก','External PC price'),'answer':bi('ราคา 200 บาท','Price 200 THB'),'topic':'price'})
r['claim_bindings']=[f.binding('current_rate','fx_pc','fx_price_faq','answer',actors=['fx_external'],services=['fx_pc'],unit='per_hour',duration=60,projection='currency_literal',path='/en')]
r=f.save(r);s=snap();check('mapping is tied to an immutable source',bool(r['claim_bindings'][0]['evidence_refs']) and any(c['record_id']=='fx_price_faq' and c['value']==20000 for c in current_claims(s,AT)))
check('structured rate and FAQ contradiction share a claim key',bool(conflicts(['fx_rate'],s,AT)))
with f.store.connect() as c:errs=release_errors(f.store.heads(c),f.store.sources(c),demo=True)
check('publication refuses unresolved mapped conflicts',any('Unresolved mapped claim conflict' in x for x in errs))
r['claim_bindings'][0]['supersedes_refs']=['fx_rate#amount_minor'];r=f.save(r)
check('supersedes without authority cannot win',bool(conflicts(['fx_rate'],snap(),AT)))
r=f.save(r,mapping_authority_confirmed=True)
check('explicit scoped authority can resolve declared supersession',not conflicts(['fx_rate'],snap(),AT))
staff=f.ask('PC price for PSU staff, not External Visitors',llm=False)
check('superseded external price does not block independent staff rate',staff is not None and '50.00' in staff.answer and any(h.get('record_id')=='fx_staff_rate' for h in staff.hits),dataclasses.asdict(staff) if staff else None)
blocked=f.ask('PC price for external visitors for 2 hours',llm=False)
check('supersession never computes with obsolete numeric rate',blocked is not None and not blocked.hits and blocked.decision_artifact.get('response_type')=='unconfirmed',dataclasses.asdict(blocked) if blocked else None)
mixed=f.ask('PC price for external visitors and how do I book PC?',llm=False)
check('independent booking survives superseded price',mixed is not None and 'BOOK_STEPS' in mixed.answer,dataclasses.asdict(mixed) if mixed else None)
tampered=copy.deepcopy(r);tampered['claim_bindings'][0]['applicability']['duration_minutes']=30
with f.store.connect() as c:errs=validate(tampered,{**f.store.heads(c),tampered['record_id']:tampered},f.store.sources(c),demo=True)
check('mapping tamper fails original evidence equality',any('mapping does not match' in x or 'supersession scope' in x for x in errs))
unknown=copy.deepcopy(r);unknown['claim_bindings'][0]['conditions_status']='unknown';unknown['claim_bindings'][0]['authority_refs']=[];unknown=f.save(unknown)
check('unknown conditions are not current executable claims',not any(c['record_id']==unknown['record_id'] for c in current_claims(snap(),AT)))
with f.store.connect() as c:errs=validate(unknown,f.store.heads(c),f.store.sources(c),publish=True,demo=True)
check('unknown conditions cannot be published',any('conditions and exceptions' in x for x in errs))
f.store.withdraw('fx_price_faq',actor='isolated')
check('withdrawn mapping cannot conflict with current price',not conflicts(['fx_rate'],snap(),AT))
empty=f.new('faq','fx_empty_set',{'question':bi('รายการอุปกรณ์ครบ','Complete equipment inventory'),'answer':bi('รายการว่าง','Empty inventory'),'topic':'equipment','related_ids':[]})
empty['claim_bindings']=[f.binding('equipment_inventory','fx_center','fx_empty_set','related_ids')];empty=f.save(empty)
result=f.ask('Is there any equipment?',llm=False)
check('known empty set has explicit exhaustive scope receipt',result is not None and result.decision_artifact.get('scope_receipt',{}).get('total_members')==0,dataclasses.asdict(result) if result else None)
empty['claim_bindings'][0]['applicability']['status']='unknown';f.save(empty);result=f.ask('Is there any equipment?',llm=False)
check('unknown scope cannot certify an empty inventory',result is None or result.decision_artifact.get('scope_receipt',{}).get('completeness')!='explicit_source_declared')
# A new owner FAQ linked to a new policy retains every condition/exception.
policy=f.new('policy','fx_linked_policy',{'topic':'synthetic_access','subject':bi('เงื่อนไขทดลอง','Fixture access'),'decision':'conditional','conditions_all':[{'field':'fixture_code','operator':'eq','value':'FIXTURE_CODE'}],
 'exceptions':bi('ยกเว้นกรณี FIXTURE_EXCEPTION','Except FIXTURE_EXCEPTION'),'details':bi('อนุญาตตามเงื่อนไข','Allowed under these conditions')})
linked=f.new('faq','fx_linked_faq',{'question':bi('สิทธิ์ทดลองนี้เป็นยังไง','How does fixture access work?'),'answer':bi('คำอธิบายทดลอง','Synthetic explanation'),'topic':'synthetic_access'})
b=f.binding('fixture_permission','fx_pc','fx_linked_policy','details');b['condition_refs']=[{'record_id':'fx_linked_policy','field':'conditions_all'}];b['exception_refs']=[{'record_id':'fx_linked_policy','field':'exceptions'}];linked['claim_bindings']=[b];linked=f.save(linked)
check('new cross-kind mapping resolves source conditions and exceptions',any(c['record_id']=='fx_linked_faq' and c['condition_refs'] and c['exception_refs'] for c in current_claims(snap(),AT)))
from app.knowledge.common.mapped_claims import render
from app.knowledge.common.request_plan import Need
from app.knowledge.common.answer import CommonAnswerer
n=Need('n1','policy','fixture access','fixture access',['fx_pc'],[],predicate='fixture_permission')
mapped=render(CommonAnswerer(DraftSnapshotView(f.store)),n,[c for c in current_claims(snap(),AT) if c['record_id']=='fx_linked_faq'],snap(),AT,'en')
check('mapped renderer includes condition and exception source receipts',mapped is not None and 'FIXTURE_CODE' in mapped.answer and 'FIXTURE_EXCEPTION' in mapped.answer and len(mapped.hits)>=3)
# Raw source authority mismatches remain blocking even with valid-looking IDs.
sc=copy.deepcopy(snap());ref=policy['fields']['details']['evidence_refs'][0];sc['release']['sources'][ref['source_id']]['authority_for']=['game']
bad_graph,_,_=compile('schema_attributes',['fx_linked_policy'],sc['release']['records'],fields=['details'])
check('wrong source-kind authority is still rejected',evaluate(bad_graph,sc,AT)['status']=='broken_relation')
with request_context() as c:
 check('all branches share one model and one corrective quota',c.reserve_semantic() and not c.reserve_semantic() and c.reserve_corrective() and not c.reserve_corrective())
plan=make_plan('PC price for 2 hours and VR price for 30 minutes for external visitors',snap()['release']['records'],snap()['release']['names'])
check('coordinated prices preserve distinct durations and share only trailing actor',len(plan.needs)==2 and '2 hours' in plan.needs[0].query and '30 minutes' in plan.needs[1].query and bool(plan.needs[0].slots.get('audience')))
rows=[{'record_id':k,'kind':r['kind'],'name':k} for k,r in snap()['release']['records'].items() if k in {'fx_pc','fx_vr','fx_booking'}]
p={'needs':[{'task':'procedure','record_ids':['fx_booking'],'quote':'Is PC available now?'}],'unresolved':[]}
check('semantic proposal cannot replace a recognized live predicate',validate_plan(p,'Is PC available now?',rows,snap()['release']['records'],['fx_pc'])[0] is None)
# Data growth after a material-context question: no rule may leak into normal play.
question='ROV what should I do if I disconnect?';first=f.ask(question,llm=False)
before=f.ask('general play',history=f.history(question,first),llm=False)
check('ordinary-play gap does not quote competition policy',before is not None and 'RULE_EXCEPTION' not in before.answer)
f.new('faq','fx_normal_disconnection',{'question':bi('ROV เล่นทั่วไปเกมหลุด','ROV ordinary play disconnection'),
 'answer':bi('ติดต่อผู้ดูแล NORMAL_PLAY_NEW_DATA','Contact staff NORMAL_PLAY_NEW_DATA'),'topic':'disconnection','related_ids':['fx_rov'],
 'query_profile':{'task':'correction','subjects':[bi('เกมหลุด','disconnection')],'ownership':'any','context':'studio'}})
after=f.ask('general play',history=f.history(question,first),llm=False)
check('owner-added ordinary-play FAQ is answered without code aliases',after is not None and 'NORMAL_PLAY_NEW_DATA' in after.answer and 'RULE_EXCEPTION' not in after.answer,dataclasses.asdict(after) if after else None)
rr=f.store.get('fx_rule')['record'];rr['fields']['completeness'].update(status='unknown',value=None,evidence_refs=[]);f.save(rr)
reference=f.ask('All ROV competition rules',llm=False)
check('available rule text survives unknown completeness as explicit partial reference',reference is not None and 'RULE_EXCEPTION' in reference.answer and reference.decision_artifact.get('response_type')=='partial_answer' and reference.decision_artifact.get('query_plan',{}).get('complete_rulebook_confirmed') is False,dataclasses.asdict(reference) if reference else None)
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x['case'] for x in checks if not x['passed']],
 'new_capabilities':'source-bound mappings, conflicts, publication, scoped empty sets, conditions, shared plan, audit','data':'isolated synthetic only','model_calls':0}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
