import ast,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.meaning_review import review
for p in [*S.rglob('*.py'),*R.glob('*.py')]:
 if '__pycache__' not in p.parts:ast.parse(p.read_text('utf-8-sig'),filename=str(p))
e=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
jobs=[j for name in ['DEVELOPMENT_JOBS.jsonl','HOLDOUT_JOBS.jsonl'] for j in map(json.loads,(R/name).open(encoding='utf8'))]
checks=[];cases=[]
def ck(name,ok):checks.append({'name':name,'passed':bool(ok)})
def run(prefix,domain,cat,op,facet):
 j=next(j for j in jobs if j['key'].startswith(prefix));q=j['question'];u=review(q,e.index,Understanding([MeaningTask(q,domain,cat,op,facet)],True,'retained_source_contract'))
 out=e.answer(q,j['locale'],at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=u);cases.append({'key':j['key'],'question':q,'result':out});return out
out=run('1806def7','games','C04','detail','zone');ck('global_multi_zone_set_not_single_game_detail',len({c['record_id'] for c in out['claims']})==4 and out['status']=='partial')
out=run('18fc2648','members','C02','role_lookup','role');ck('source_role_suffix_selects_one_matching_person',len({c['record_id'] for c in out['claims']})==1 and any('Web & AI Developer' in c['value'] for c in out['claims']))
out=run('d7158a36','rules','C10','detail','owner_policy');ck('consumption_does_not_assert_bring_permission',out['status']=='partial' and 'does not separately confirm permission to bring' in out['answer'])
ck('native_database_bytes_unchanged_since_initial_pilot',(S/'data/knowledge/common.sqlite').read_bytes()==(R/'revision01_system/data/knowledge/common.sqlite').read_bytes())
ck('reviewed_teacher_examples_unchanged',(S/'app/knowledge/common/domain_flow/teacher_lessons.json').read_bytes()==(R/'revision01_system/app/knowledge/common/domain_flow/teacher_lessons.json').read_bytes())
result={'total':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks,'new_questions':0,'model_calls':0,'evaluation_cohort_reused_for_development':True}
(R/'REVISION02_CONTRACTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');(R/'REVISION02_CONTRACT_CASES.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(result,ensure_ascii=False));assert all(c['passed'] for c in checks)
