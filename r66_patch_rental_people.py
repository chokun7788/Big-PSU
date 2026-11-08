from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
def replace(old,new):
 global t
 assert t.count(old)==1,(t.count(old),old[:60]);t=t.replace(old,new)
replace('control_projection,calendar_ids','control_projection,calendar_ids,rental_ids')
replace("        if query_operation=='people' and not ids:\n            ids=[rid for rid,r in records.items() if r['kind']=='person'];method='common_people_directory'", "        if query_operation=='people':\n            if not ids:ids=[rid for rid,r in records.items() if r['kind']=='person']\n            if ids and all(records[rid]['kind']=='person' for rid in ids):method='common_people_directory'\n        if query_operation=='rental':\n            packages=rental_ids(question,ids,records)\n            if packages:ids=packages;method='common_rental_scope'")
replace("        if method=='common_procedure_topic':requested=['answer'];broad=False", "        if method=='common_rental_scope' and not requested and not broad:requested=['amount_minor','equipment_included','terms'];broad=False\n        if method=='common_procedure_topic':requested=['answer'];broad=False")
p.write_text(t,encoding='utf-8');print('rental period/zone/audience and person follow-ups')
