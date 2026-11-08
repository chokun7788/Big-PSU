from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert old in s,rel;p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/competition_name_recovery.py','def recover_names(query: str,registry: tuple[tuple[str,str],...])', 'def recover_names(query: str,registry: tuple[tuple[str,str],...],allow_same_target_overlap: bool = False)')
edit('app/pipeline/competition_name_recovery.py','    for _,alias in registry:', '    for protected_target,alias in registry:')
edit('app/pipeline/competition_name_recovery.py','protected.append((a,b))','protected.append((a,b,protected_target))')
edit('app/pipeline/competition_name_recovery.py','if any(original_start<b and a<original_end for a,b in protected):continue','if any(original_start<b and a<original_end and (not allow_same_target_overlap or protected_target!=game_id) for a,b,protected_target in protected):continue')
edit('app/pipeline/competition_facet_recovery.py',"FACET_ALIASES+(('match_settings',('game settings','การตั้งค่าในเกม')), )", "FACET_ALIASES+(('match_settings',('game settings','การตั้งค่าในเกม')),('eligibility_registration',('คุณสมบัติ','eligibility')),('rulebook_identity',('event information',)), )")
edit('app/pipeline/competition_facet_recovery.py','recover_names(query,registry)', 'recover_names(query,registry,allow_same_target_overlap=True)')
# Full valid phrases remain protected against expansions even within one facet.
edit('app/pipeline/competition_facet_recovery.py',"        if re.search(r'\\d',edit.original+edit.canonical):continue", "        if edit.original.casefold() in {'game settings','การตั้งค่าในเกม'}:continue\n        if re.search(r'\\d',edit.original+edit.canonical):continue")
print('whole facet span can retain an exact prefix within the same facet; names keep strict default')
