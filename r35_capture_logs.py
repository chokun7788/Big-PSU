import json
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r35_report_path.txt').read_text().strip())
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
log=P/'owner_local_delivery_20261003_source_task_boundaries_r34_finalI/PSU_Esports_Chatbot_Local/data/logs/web_chat_2026-10-03.jsonl'
rows=[]
for line in log.read_text(encoding='utf-8').split('\n'):
 try:x=json.loads(line)
 except ValueError:continue
 if str(x.get('question','')).casefold() in ('valorant','ขอกฏการแข่ง','มีรายการแข่งอะไรบ้าง') and '08:43' in str(x.get('timestamp','')):rows.append(x)
with (R/'USER_HISTORY_LOG_EVIDENCE_UTC.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print(json.dumps([dict(question=x.get('question'),recent_history_count=x.get('recent_history_count'),context=x.get('context_resolution'),keys=list(x.keys())) for x in rows],ensure_ascii=False))
