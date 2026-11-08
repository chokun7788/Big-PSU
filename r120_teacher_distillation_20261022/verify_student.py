"""Retained questions and source contracts, no model calls or new questions."""
import ast,copy,hashlib,json,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent; S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse,MeaningTask,Understanding
from app.knowledge.common.domain_flow.distilled_policy import demonstrations,normalize_tasks,retain_context
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.scope import requested_minutes,reference_time
read=lambda p:json.loads(p.read_text('utf8'))
checks=[];cases=[]
def ck(name,ok,**details):checks.append({'name':name,'passed':bool(ok),**details})
for p in [*S.rglob('*.py'),*R.glob('*.py')]:
 if '__pycache__' not in p.parts:ast.parse(p.read_text('utf-8-sig'),filename=str(p))
ck('all_snapshot_and_runner_python_parses',True)
examples=read(R/'TEACHER_LESSONS.json')['examples']
runtime=read(S/'app/knowledge/common/domain_flow/teacher_lessons.json')
for e in examples:
 u=parse(json.dumps(e['plan'],ensure_ascii=False),e['question'])
 ck('reviewed_task_contract_'+e['id'],u.accepted,reason=u.reason)
ck('only_reviewed_examples_installed',len(runtime['examples'])==60 and {e['id'] for e in runtime['examples']}=={e['id'] for e in examples})
ck('no_business_answer_fields',runtime['business_answers_included'] is False and all(set(e)=={'id','question','plan','technique'} for e in runtime['examples']))
jobs=list(map(json.loads,(R/'DEVELOPMENT_JOBS.jsonl').open(encoding='utf8')))
holdout=list(map(json.loads,(R/'HOLDOUT_JOBS.jsonl').open(encoding='utf8')))
ck('runtime_examples_exclude_development_and_evaluation_ids',not ({e['id'] for e in examples}&{j['key'] for j in jobs+holdout}))
def logical(db):
 c=sqlite3.connect('file:'+str(db.resolve()).replace('\\','/')+'?mode=ro',uri=True)
 try:
  tables=[r[0] for r in c.execute("select name from sqlite_master where type='table' order by name")]
  return {t:sorted((json.dumps(row,ensure_ascii=False,sort_keys=True,default=str) for row in c.execute('select * from "'+t.replace('"','""')+'"')),key=str) for t in tables}
 finally:c.close()
ck('all_native_tables_identical_including_approvals_and_withdrawals',logical(S/'data/knowledge/common.sqlite')==logical(R.parent/'r119_complete_source_audit_20261021/system/data/knowledge/common.sqlite'))
e=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
def run(prefix,domain,cat,op,facet):
 j=next(j for j in jobs if j['key'].startswith(prefix));q=j['question']
 u=review(q,e.index,Understanding([MeaningTask(q,domain,cat,op,facet)],True,'source_contract'))
 out=e.answer(q,j['locale'],at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=u)
 cases.append({'key':j['key'],'question':q,'meaning':u.as_dict(),'result':out});return out,j
out,j=run('546c4490','games','C04','detail','studio_services')
ck('explicit_price_is_not_game_catalogue',cases[-1]['meaning']['tasks'][0]['category']=='C06' and all(n['category']=='C06' for n in out['needs']),status=out['status'])
out,j=run('00301c15','rules','C10','detail','owner_policy')
ck('existing_temporary_suspension_faq_now_projects',any('temp_suspension' in f['record_id'] and f['category']=='C10' for f in e.index.facts))
ck('temporary_suspension_reaches_source',any('temp_suspension' in c['record_id'] for c in out['claims']),status=out['status'])
out,j=run('0d05eaf6','service_fee','C06','price_calculate','amount')
ck('retained_word_duration_is_sixty_minutes',requested_minutes(j['question'])==60,value=requested_minutes(j['question']))
ck('single_hour_does_not_show_half_hour_rate',bool(out['needs'][0]['computations']) and out['needs'][0]['computations'][0]['unit_calculation']['requested_minutes']==60,computations=out['needs'][0]['computations'])
placeholder={'quote':'','domain':'general','operation':'unknown','facet':'','target':'','constraints':[],'ambiguous':False}
task={'quote':j['question'],'domain':'service_fee','operation':'price_calculate','facet':'amount','target':'','constraints':[],'ambiguous':False}
ck('discard_only_exact_empty_placeholder',parse(json.dumps({'tasks':[task,placeholder]}),j['question']).accepted and not parse(json.dumps({'tasks':[placeholder]}),j['question']).accepted)
out,j=run('104194c2','competition_rules','C13','detail','rule_clause')
ids={c['record_id'] for c in out['claims']}
ck('generic_valorant_penalties_include_source_siblings',len(ids)>=6,records=sorted(ids),status=out['status'])
out,j=run('4b0fb4a4','competition_rules','C13','detail','rule_clause')
ck('aov_context_retained_for_current_source_binding',bool(out['claims']) and all(c['fact_id'].startswith('C13:') for c in out['claims']),status=out['status'])
for prefix in ['8acac2d3','0f5e0fd0']:
 domain,cat,facet=('game_controls','C05','input_bindings') if prefix=='8acac2d3' else ('equipment','C03','name')
 out,j=run(prefix,domain,cat,'detail',facet)
 ck('existing_exact_reader_'+prefix,bool(out['claims']) and all(c['fact_id'].startswith(cat+':') for c in out['claims']))
out,j=run('e8694671','members','C02','role_lookup','role')
clone=copy.deepcopy(e.index.records)
# Public withdrawal contract uses the compiler output, never writes the database.
from app.knowledge.common.domain_flow.projection import compile_snapshot
data=compile_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
for r in data['records'].values():
 if r['kind']=='person':r['fields']['public_scope']={'status':'unknown','value':None,'evidence_refs':[],'note':'contract-only withdrawal'}
tmp=Engine(data);p=tmp.finish_plan('C02',j['question'],tmp.plan('C02',j['question']),reference_time('2026-10-21T12:00:00+07:00'))
ck('public_scope_withdrawal_guard_preserved',not p.ids and p.reason=='person_public_scope_not_confirmed')
protected=read(R/'PROTECTED_INPUTS.json')
ck('protected_original_files_unchanged',all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in protected.items()),files=len(protected))
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'failed':[c for c in checks if not c['passed']],'checks':checks,'model_calls':0,'new_questions':0}
(R/'STUDENT_CONTRACTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
(R/'STUDENT_CONTRACT_CASES.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False));assert not result['failed']
