import json,sys,os
from pathlib import Path
from unittest.mock import patch
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(ROOT))
import app.pipeline.experimental_fallback as f
CASES=[
 ('network_narrowed','แปลประโยค Please check your network connection เป็นภาษาไทย','กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ตครับ','th',False),
 ('network_correct','แปลประโยค Please check your network connection เป็นภาษาไทย','กรุณาตรวจสอบการเชื่อมต่อเครือข่ายของคุณ','th',True),
 ('internet_correct','แปลประโยค Please check your internet connection เป็นภาษาไทย','กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ตของคุณ','th',True),
 ('number_changed','Translate "Wait 15 minutes." into Thai.','รอ 50 นาที','en',False),
 ('number_correct','Translate "Wait 15 minutes." into Thai.','รอ 15 นาที','en',True),
 ('negation_lost','Translate "You cannot cancel the booking." into Thai.','คุณสามารถยกเลิกการจองได้','en',False),
 ('negation_correct','Translate "You cannot cancel the booking." into Thai.','คุณไม่สามารถยกเลิกการจองได้','en',True),
 ('device_changed','Translate "Use PC1 for 60 minutes." into Thai.','ใช้ PC2 เป็นเวลา 60 นาที','en',False),
 ('device_correct','Translate "Use PC1 for 60 minutes." into Thai.','ใช้ PC1 เป็นเวลา 60 นาที','en',True),
 ('unit_changed','Translate "Wait 15 minutes." into Thai.','รอ 15 ชั่วโมง','en',False),
 ('quoted_note_valid','Translate "Note: Check your network." into Thai.','หมายเหตุ: ตรวจสอบเครือข่ายของคุณ','en',True),
 ('meta_leak','Explain latency briefly.','Latency is a delay.\nNote: The term latency is preserved as it was part of the original query.','en',False),
 ('question_tail','Explain latency briefly.','Latency is a delay.\nClarifying question: Are you seeking a general explanation?','en',False),
 ('greeting_only_sentence','Write a friendly two-sentence invitation to a study session.','Hi everyone! Join our study session.','en',False),
 ('invitation_content','Write a friendly two-sentence invitation to a study session.','Join our study session. We can learn together.','en',True),
 ('ping_bandwidth','Explain ping briefly.','Ping measures network bandwidth in Mbps.','en',False),
 ('ping_correct','Explain ping briefly.','Ping tests reachability and round-trip time using ICMP.','en',True),
 ('http_unqualified','Explain HTTP briefly.','HTTP always operates over TCP.','en',False),
 ('http_exception','Explain HTTP briefly.','HTTP/1.1 and HTTP/2 commonly use TCP; HTTP/3 uses QUIC.','en',True),
 ('ram_nonvolatile','Explain RAM and SSD briefly.','RAM retains its data after power is removed; SSD provides storage.','en',False),
 ('ram_correct','Explain RAM and SSD briefly.','Conventional RAM is volatile working memory; SSD is non-volatile storage.','en',True),
]
rows=[]
for name,q,a,l,expected in CASES:
 with patch.object(f,'effective_locale',return_value=l):
  meta={'ollama_done_reason':'stop'};p=f.select_general_generation_profile(q);ok,reason=f._general_output_contract(a,p,meta)
 rows.append(dict(name=name,question=q,answer=a,locale=l,expected_accept=expected,actual_accept=ok,reason=reason,passed=ok==expected,metadata=meta))
with (OUT/(sys.argv[1]+'.json')).open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
print('passed',sum(r['passed'] for r in rows),'/',len(rows));print([(r['name'],r['reason']) for r in rows if not r['passed']])
