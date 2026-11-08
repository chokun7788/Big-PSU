"""Source-backed regression assertions on existing reviewed questions."""
import json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.understanding import Understanding,parse
from app.knowledge.common.domain_flow.scope import reference_time
e=Engine.from_snapshot(snapshot());at=reference_time('2026-10-25T12:00:00+07:00')
cases=json.loads((R.parent/'r131_diagnostic_review_20261025/CONSOLIDATED_SOURCE_REVIEW.json').read_text('utf8'))['cases'];bykey={x['key']:x for x in cases}
checks=[];details=[]
def run(q):
 u=propose(e.index,q)
 if u is None:u=review(q,e.index,Understanding(reason='local_core_verification',event={'model_called':False}))
 return e.answer(q,'auto',at=at,allow_llm=False,understanding=u)
def known(prefix):return next(x['question'] for x in cases if x['key'].startswith(prefix))
def check(name,result,detail=None):
 checks.append({'name':name,'passed':bool(result)})
 if detail is not None:details.append({'name':name,'detail':detail})
def ids(result):return {c['record_id'] for c in result['claims']}
gpu=json.loads((R.parent/'r131_diagnostic_review_20261025/POST_GATE_GPU_CAUSAL_REFINEMENT.json').read_text('utf8'))['cases']
for c in gpu:
 result=run(c['question'])
 check('gpu_'+c['key'][:8],ids(result)=={'equipment_gaming_pc'} and any(c['facet']=='specifications' and 'GPU' in c['value'] for c in result['claims']))
related=json.loads((R.parent/'r131_diagnostic_review_20261025/POST_GATE_RELATED_SOURCE_REVIEW.json').read_text('utf8'))['cases']
format_cases=[c for c in related if c.get('root_cause_group')=='tekken_format_to_document_title']
for c in format_cases:
 result=run(c['question'])
 check('format_body_'+c['key'][:8],ids(result)=={'competition_competition_rules_tekken8_psu_esports_section_002'} and 'FT2' in result['answer'] and '60S' in result['answer'])
for prefix,expected in [
 ('934b6162',{'r114_q037_owner_policy'}),
 ('9749c57f',{'migrated_faq_rule_damage_responsibility'}),
 ('0c25d981',{'competition_competition_rules_cs2_psu_phuket_2026_section_037','competition_competition_rules_cs2_psu_phuket_2026_section_038'}),
 ('06563f1a',{'competition_competition_rules_cs2_psu_phuket_2026_section_046'}),
]:
 result=run(known(prefix));check('correct_source_'+prefix,expected<=ids(result),{'question':known(prefix),'answer':result['answer'],'source_ids':sorted(ids(result))})
result=run(known('b9fa6734'))
check('bound_controls_answered_without_reasking_game',any(c['record_id']=='controls_ps5_tekken_8' for c in result['claims']) and {n['category'] for n in result['needs']}=={'C05','C06'})
result=run(known('7e3ed641'))
check('static_catalog_not_live_occupancy',any(c['facet']=='game_catalog' for c in result['claims']) and all(n['category']=='C04' for n in result['needs']))
result=run(known('db84ae34'))
check('pc10_not_inferred_from_zone_offering',not result['claims'] and any(n['reason']=='requested_resource_offering_not_confirmed' for n in result['needs']))
# Counterfactual unit scope, not a new benchmark question or model inference.
result=run(known('db84ae34').replace('#10','#1'))
check('known_pc1_installation_has_resource_receipts',bool(result['claims']) and any(n['plan']['metadata'].get('resource_installation_source_verified') for n in result['needs']) and not any(n['execution_contract'].get('fatal') for n in result['needs']),result)
for c in cases:
 if 'notebook' in c['question'] and 'กลับบ้าน' in c['question']:
  result=run(c['question']);check('offsite_not_onsite_package_'+c['key'][:8],not result['claims'] and any(n['reason']=='offsite_rental_scope_not_recorded' for n in result['needs']))
result=run(known('4dc69c73'))
check('negative_cancel_keeps_customer_actor',bool(result['claims']) and all('invalid_info' not in c['record_id'] for c in result['claims']),result)
for q,expected in [
 ('How much does PC cost and how do I book?',{'C06','C08'}),
 ('What is CS2 tournament format and how much does PC cost?',{'C06','C13'}),
]:
 u=propose(e.index,q);check('independent_needs_'+str(sorted(expected)),u is not None and {t.category for t in u.tasks}==expected,u.as_dict() if u else None)
out=R/('core_verification_'+str(time.time_ns()));out.mkdir()
report={'all_passed':all(c['passed'] for c in checks),'checks':checks,'details':details,'inferences':0,'new_benchmark_questions':0,'controlled_counterfactual_scope_tests':3,'semantic_accuracy':None}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8')
(R/'LATEST_CORE_VERIFICATION.json').write_text(json.dumps({'output':str(out),'all_passed':report['all_passed'],'checks':len(checks)},indent=2),'utf8')
print(json.dumps({'output':str(out),'checks':len(checks),'failed':[c['name'] for c in checks if not c['passed']]},ensure_ascii=False))
assert report['all_passed']
