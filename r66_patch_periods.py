from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system';p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
old="                    elif key=='conditions_all':out=conditions_text(v,lang,text)";new="                    elif key in {'open_periods','bookable_periods','maintenance_periods'} and v:out=' / '.join(period['start']+'–'+period['end'] for period in v)\n                    elif key=='conditions_all':out=conditions_text(v,lang,text)";assert t.count(old)==1;t=t.replace(old,new)
t=t.replace("+' to '+str(until or '?')", "+' until (exclusive) '+str(until or '?')").replace("+' ถึง '+str(until or '?')", "+' ถึงก่อน '+str(until or '?')")
p.write_text(t,encoding='utf-8');print('natural period labels and explicit exclusive validity end')
