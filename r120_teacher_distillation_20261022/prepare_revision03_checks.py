from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'verify_revision02.py').read_text('utf8').replace('REVISION02_CONTRACTS.json','REVISION03_CONTRACTS.json').replace('REVISION02_CONTRACT_CASES.json','REVISION03_CONTRACT_CASES.json')
s=s.replace("result={'total':len(checks)","""out=run('42582c1e','games','C04','detail','summary');ck('equipment_definition_uses_native_usage',bool(out['claims']) and all(c['facet']=='usage' for c in out['claims']))
out=run('d7158a36','rules','C10','detail','owner_policy');ck('fact_first_policy_hides_internal_identifier','food_drink_rule' not in out['answer'] and 'confirmed answer:' not in out['answer'] and 'designated' in out['answer'] and 'permission to bring' in out['answer'])
out=run('104194c2','competition_rules','C13','rule_lookup','rule_clause');ck('all_source_penalty_types_retained_after_presentation',len({c['record_id'] for c in out['claims']})>=6 and all(s in out['answer'] for s in ['Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit']))
result={'total':len(checks)""")
(R/'verify_revision03.py').write_text(s,'utf8')
print('Prepared eight source contracts on the final candidate.')
