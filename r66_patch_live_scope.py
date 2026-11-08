from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
t=t.replace('control_projection,calendar_ids,rental_ids','control_projection,calendar_ids,rental_ids,scoped_live_request')
old="        scope_ids=list(ids)\n        if query_operation";assert t.count(old)==1;t=t.replace(old,"        scope_ids=list(ids)\n        if live_query(question) or scoped_live_request(question,ids,records):return None\n        if query_operation")
p.write_text(t,encoding='utf-8');print('resource availability remains with live adapter; free-price queries stay separate')
