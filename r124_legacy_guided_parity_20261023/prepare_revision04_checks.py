from pathlib import Path
R=Path(__file__).resolve().parent
for name in ['verify_foundation','verify_live','verify_source_guards','verify_exact_faq']:
 src=(R/(name+'.py')).read_text('utf8').replace("S=R/'revision03_system'","S=R/'revision04_system'")
 if name=='verify_live':src=src.replace('reference=clock-timedelta(days=1)','reference=clock-timedelta(days=6)')
 if name=='verify_source_guards':
  src=src.replace("r=run('69812416');", "r=run('3cc3c5c3');checks['full_compound_binding_not_reduced_to_final_letter']=bool(r.decision_artifact['need_results'][0]['claim_packets'])\nr=run('9be5826b');checks['map_pool_is_competition_not_equipment']=categories(r)==['C13']\nr=run('69812416');")
  src=src.replace("len(r.decision_artifact['need_results'][0]['claim_packets'])>1", "len(r.decision_artifact['need_results'][0]['claim_packets'])>1 and r.decision_artifact['execution_contract']['tasks'][0]['terminal_state']=='partial'")
 (R/(name+'04.py')).write_text(src,'utf8')
print('Prepared four retained/fault gate suites for revision04')
