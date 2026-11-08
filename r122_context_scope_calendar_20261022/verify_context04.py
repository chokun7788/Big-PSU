"""Offline execution of previously saved proposals. No model/API requests."""
import ast,hashlib,json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022';S=R/'revision04_system'
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1')
sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse,Understanding,MeaningTask
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.meaning_reader import apply as reader_apply
from app.knowledge.common.domain_flow.contracts import Plan
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot());idx=engine.index
gold=[json.loads(s) for s in (OLD/'test.jsonl').read_text('utf8').splitlines()]
saved=[json.loads(s) for s in (OLD/'train02/trained_test.jsonl').read_text('utf8').splitlines()]
out=[]
for g,s in zip(gold,saved):
 assert g['key']==s['key']
 u=parse(s['raw_output'],g['question']);u.event['raw_content']=s['raw_output'];u=review(g['question'],idx,u)
 u=apply(g['question'],idx,u)
 out.append({'key':g['key'],'question':g['question'],'accepted':u.accepted,'tasks':[t.as_dict() for t in u.tasks],'review':u.event.get('context_scope_review',[])})
def task(i):return out[i]['tasks'][0]
checks={
 'now_vacancy_is_live':task(0)['category']=='C12',
 'unspecified_free_slot_clarifies_resource':task(24)['category']=='C12' and task(24)['ambiguous'],
 'unresolved_it_clarifies':task(25)['ambiguous'],
 'two_unassigned_duration_roles_clarify':task(12)['ambiguous'],
 'compound_controls_not_pc':not any(c['quote']=='PC' for c in out[9]['tasks'][0]['constraints']),
 'compound_price_not_button_count':not any('buttons' in c['quote'] for c in out[9]['tasks'][1]['constraints']),
 'cockpit_reference_inherited':out[21]['tasks'][1]['target'].casefold()=='cockpit',
}
at='2026-10-21T12:00:00+07:00'
u=parse(saved[21]['raw_output'],gold[21]['question']);u.event['raw_content']=saved[21]['raw_output'];u=review(gold[21]['question'],idx,u)
answer=engine.answer(gold[21]['question'],'en',at=at,allow_llm=False,understanding=u)
calendar=answer['needs'][1]
checks['weekly_calendar_has_seven_source_claims']=len(calendar['claims'])==7
checks['weekly_calendar_applicability_not_invented']=calendar['status']=='partial' and bool(calendar['plan']['metadata'].get('calendar_source_limits'))
amb=MeaningTask(gold[25]['question'],'games','C04','availability','studio_services',ambiguous=True)
plan=reader_apply(idx,amb.quote,amb,Plan(ids=['untrusted'],status='answer',locked=True),at)
checks['ambiguity_blocks_preconfirmed_plan']=plan.status=='missing_input' and not plan.ids and plan.locked
# Adversarial assignment uses an existing question, not a new benchmark item.
bad=parse(json.dumps(gold[9]['label'],ensure_ascii=False),gold[9]['question'])
fixed=apply(gold[9]['question'],idx,bad)
checks['known_old_annotation_cross_task_leak_removed']=not any(c['quote']=='PC' for c in fixed.tasks[0].constraints) and not any('buttons' in c['quote'] for c in fixed.tasks[1].constraints)
for p in S.rglob('*.py'):ast.parse(p.read_text('utf-8-sig'))
result={'checks':checks,'all_passed':all(checks.values()),'saved_proposals':30,'new_model_calls':0,'new_questions':0,'semantic_accuracy':None,'calendar_answer':answer,'per_request':out}
(R/'OFFLINE_CONTEXT_VERIFICATION04.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(checks,ensure_ascii=False,indent=2));assert all(checks.values())
