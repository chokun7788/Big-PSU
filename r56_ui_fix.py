from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'web_chat/chat_request.js';t=p.read_text(encoding='utf-8');t=t.replace("message:jobData.status === 'running' ?", "message:(jobData.status === 'running' ?",1).replace("'รับคำถามแล้ว กำลังรอคิว…') + elapsedText", "'รับคำถามแล้ว กำลังรอคิว…')) + elapsedText",1);p.write_text(t,encoding='utf-8')
(OUT/'UI_FIX_NOTE.md').write_text('Node protocol test found elapsed timer was appended only to queued text due to conditional precedence. Fixed parentheses for running and queued messages. Failed assertion output preserved in tool history; protocol result is written only after passing.',encoding='utf-8')
print('queued and processing elapsed messages fixed')
