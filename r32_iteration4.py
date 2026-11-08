from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');p=P/'app/pipeline/competition_name_recovery.py';s=p.read_text(encoding='utf-8');a='                distance=_osa(value,name,budget)';assert a in s;s=s.replace(a,'''                # Facet prefixes may overlap only to repair a longer phrase.
                # Never consume a following word after an already exact alias.
                if allow_same_target_overlap and name in value:continue
                distance=_osa(value,name,budget)''',1);p.write_text(s,encoding='utf-8')
print('protected exact vocabulary from consuming neighboring words')
