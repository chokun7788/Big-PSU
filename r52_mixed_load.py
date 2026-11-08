import json,time,uuid
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from r52_web_cases import run,request,OUT

cases=[
 ('Explain DNS, TCP, TLS, HTTP and latency in approximately 500 words.','en'),
 ('อธิบายว่า network latency คืออะไรแบบสั้นๆ','th'),
 ('Compare TCP and UDP, including one advantage and one disadvantage of each.','en'),
 ('Give three steps for learning touch typing.','en'),
 ('ค่าบริการ PC สำหรับบุคคลทั่วไป','th'),
 ('Is membership required to use the studio?','en'),
]
def one(item):
 index,(question,locale)=item
 time.sleep(index*.12)
 return dict(index=index,**run(question,locale))
if __name__=='__main__':
 status,health=request('/health')
 assert status==200 and health['runtime']['version']==sys.argv[2]
 start=time.perf_counter()
 with ThreadPoolExecutor(max_workers=len(cases)) as pool:rows=list(pool.map(one,enumerate(cases)))
 output={'health_before':health,'total_sec':time.perf_counter()-start,'rows':rows,'health_after':request('/health')[1]}
 # Check actual API idempotency and conflict after completion; no new inference.
 row=rows[-1];job=row['job'];payload=dict(question=row['question'],locale=row['locale'],debug=True,experimental_rag_fallback=True,client_session_id=row['session_id'],client_turn_id=job['turn_id'])
 s,duplicate=request('/api/chat/jobs',payload);s2,conflict=request('/api/chat/jobs',dict(payload,question='Changed question'))
 output['idempotency']={'duplicate_status':s,'same_job':duplicate.get('job_id')==job['job_id'],'conflict_status':s2,'conflict':conflict}
 with (OUT/(sys.argv[1]+'.json')).open('x',encoding='utf-8') as stream:json.dump(output,stream,ensure_ascii=False,indent=2)
 print('duplicate',s,output['idempotency']['same_job'],'conflict',s2,flush=True)
