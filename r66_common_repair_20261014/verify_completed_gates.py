"""Read completed gate evidence; never mark an incomplete arm complete."""
import sys,json,re,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];out=B/('VERIFIED_'+tag+'.json')
if out.exists():raise FileExistsError(out)
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
status=read(B/('FINAL_'+tag)/'STATUS.json')
assert status.get('complete') and status.get('code_unchanged') and status.get('database_unchanged'),status
stages=status['completed_stages'];assert all(s['exit_code']==0 for s in stages)
expected={'focused','faq_projection','billing_recovery','versioned_contracts','person_off','discovered_off','residual_off','scoped_topics_off','support_off','new_categories_off','common_native','matrix_off','http_off','http_slow_off','matrix_llm','http_llm','http_slow_llm','discovered_llm','residual_llm','scoped_topics_llm','support_llm','person_llm','new_categories_llm'}
expected.update({'audience_policy_off','validation_regressions_off','audience_policy_llm','validation_regressions_llm'})
expected.update({'owner_preview_off','owner_preview_llm'})
expected.update({'price_comparison_off','price_comparison_llm'})
expected.update({'intent_priority_off','intent_priority_llm'})
expected.update({'translation_completeness_off','translation_completeness_llm'})
expected.update({'selector_latency_off','selector_latency_llm'})
expected.update({'return_policy_off','return_policy_llm'})
assert {s['stage'] for s in stages}==expected and len(stages)==len(expected),(len(stages),stages)
for stage in ('focused','faq_projection','billing_recovery','versioned_contracts','discovered_off','residual_off','scoped_topics_off','discovered_llm','residual_llm','scoped_topics_llm','audience_policy_off','audience_policy_llm','validation_regressions_off','validation_regressions_llm','owner_preview_off','owner_preview_llm','price_comparison_off','price_comparison_llm','intent_priority_off','intent_priority_llm'):
 raw=(B/('FINAL_'+tag)/(stage+'.log')).read_text(encoding='utf-8');assert re.search(r'\nOK\s*$',raw),stage
 if stage.startswith('residual_'):assert 'Ran 15 tests' in raw,stage
 if stage.startswith('scoped_topics_'):assert 'Ran 11 tests' in raw,stage
 if stage.startswith('audience_policy_'):assert 'Ran 18 tests' in raw,stage
 if stage.startswith('validation_regressions_'):assert 'Ran 8 tests' in raw,stage
 if stage.startswith('owner_preview_'):assert 'Ran 2 tests' in raw,stage
 if stage.startswith('price_comparison_'):assert 'Ran 10 tests' in raw,stage
 if stage.startswith('intent_priority_'):assert 'Ran 10 tests' in raw,stage
for stage in ('translation_completeness_off','translation_completeness_llm'):
 raw=(B/('FINAL_'+tag)/(stage+'.log')).read_text(encoding='utf-8');assert 'Ran 9 tests' in raw and re.search(r'\nOK\s*$',raw),stage
for stage in ('selector_latency_off','selector_latency_llm'):
 raw=(B/('FINAL_'+tag)/(stage+'.log')).read_text(encoding='utf-8');assert 'Ran 7 tests' in raw and re.search(r'\nOK\s*$',raw),stage
for stage in ('return_policy_off','return_policy_llm'):
 raw=(B/('FINAL_'+tag)/(stage+'.log')).read_text(encoding='utf-8');assert 'Ran 6 tests' in raw and re.search(r'\nOK\s*$',raw),stage
checks={}
for flag in ('off','llm'):
 matrix=[json.loads(s) for s in (B/('MATRIX_'+tag+'_'+flag+'.jsonl')).read_text(encoding='utf-8').splitlines()]
 jobs=[json.loads(s) for s in (B/'COMMON_STRATIFIED_JOBS.jsonl').read_text(encoding='utf-8').splitlines()]
 assert {r['key'] for r in matrix}=={r['key'] for r in jobs} and len(matrix)==223
 assert sum(len(r['grades']) for r in matrix)==503
 assert not any(r.get('exception') for r in matrix)
 assert not any((r.get('result') or {}).get('validation',{}).get('ok') is False for r in matrix)
 assert all(r.get('r66_config',{}).get('harness_sha256')==hashlib.sha256((B/'harness.py').read_bytes()).hexdigest() for r in matrix)
 newer=read(B/('NEW_ALL_CATEGORIES_SUMMARY_'+tag+'_'+flag+'.json'));assert newer['passed']==newer['requests']==480
 person=read(B/('PERSON_TEST_'+tag+'_'+flag+'.json'));assert person['passed']==person['tests_run']==82
 support=read(B/('SUPPORT_'+tag+'_'+flag+'.json'));assert support['tests_run']==33 and not support['failures'] and not support['errors']
 for suffix in ('','_slow'):
  http=read(B/('http_'+tag+'_'+flag+suffix)/'SUMMARY.json');assert http['passed_literal_contract']==http['turns']==24
 checks[flag]={'matrix_requests':223,'old_grades':503,'matrix_exceptions':0,'validation_rejections':0,'new_category_canonical_requests':480,'person_source_contracts':82,'provider_calendar_fixtures':33,'http_normal_turns':24,'http_slow_delivery_turns':24,'residual_tests':15,'scoped_new_data_tests':11,'audience_policy_and_followup_tests':18,'validation_regression_tests':8,'owner_preview_http_tests':2,'price_comparison_tests':10,'intent_priority_tests':10,'translation_completeness_tests':9,'selector_latency_tests':7}
for flag in checks:checks[flag]['return_policy_tests']=6
out.write_text(json.dumps({'tag':tag,'complete':True,'common_only':True,'legacy_arm_run':False,'full_20554_sweep':False,'checks':checks,'database_sha256':status['database_sha256'],'native_known_contract_mismatches_are_not_semantic_accuracy':True},ensure_ascii=False,indent=2),encoding='utf-8')
print(out)
