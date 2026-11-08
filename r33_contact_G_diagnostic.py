import sys,traceback,json,urllib.request,urllib.error
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P))
try:
 from app.pipeline.closed_query_improvements import answer_closed_query_improvement
 print(answer_closed_query_improvement('ขออีเมลและเบอร์โทรติดต่อศูนย์หน่อย','th'))
except Exception:traceback.print_exc()
try:
 payload={'question':'ขออีเมลและเบอร์โทรติดต่อศูนย์หน่อย','locale':'th','recent_history':[],'debug':True}
 print(json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8091/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30)))
except urllib.error.HTTPError as e:print(e.code,e.read().decode())
