import json
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());rows=[]
for line in (r/'http8090_G6_path_guard.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['group']!='live_path':continue
    traces=[t for t in x['response'].get('trace',[]) if t.get('stage')=='live_booking_status'];assert len(traces)==1
    m=traces[0]['metadata'];ok=m.get('transport')=='wordpress' and m.get('source')=='remote_csv_live' and m.get('cached') is False and not m.get('error_code')
    rows.append({'id':x['id'],'question':x['question'],'transport_success':ok,'fetch_metadata':m,'http_elapsed_sec':x['elapsed'],'reported_answer':x['response'].get('answer'),'real_booked_free_correctness':'not verified; no independently known current booking oracle'})
assert len(rows)==8
ms=[x['fetch_metadata']['fetch_elapsed_ms'] for x in rows]
data={'total':len(rows),'transport_success':sum(x['transport_success'] for x in rows),'fetch_ms_min':min(ms),'fetch_ms_max':max(ms),'real_occupancy_verified':False,'scope':'read-only WordPress transport/freshness provenance, not booked/free correctness','rows':rows}
with (r/'http8090_G6_live_transport_audit.json').open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in data.items() if k!='rows'}))
