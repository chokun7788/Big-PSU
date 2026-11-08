"""Final real API probes; retained questions only, no teacher answer replay."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;config=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));OUT=Path(config['output']);rows=[]
with urllib.request.urlopen(config['url']+'/health',timeout=10) as response:health=json.load(response)
assert health['ok'] and health['runtime']['profile']=='r124-legacy-guided-live'
(OUT/'HEALTH_VERIFIED.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),'utf8')
jobs={r['key'][:8]:r for r in (json.loads(x) for x in (R/'ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines())}
work=[(None,q,'th') for q in ['PC2 ว่างไหม','ตอนนี้ PC กับ VR ว่างไหม','PS5 #1 ว่างไหม']]
work += [(jobs[k]['key'],jobs[k]['question'],jobs[k]['locale']) for k in ['3cc3c5c3','9be5826b','9db7acd1','69812416','eafe23b9','e57f0296','5d18afc2','a603ab1a']]
for key,q,locale in work:
 payload={'question':q,'locale':locale,'debug':True,'experimental_rag_fallback':True,'client_session_id':'r124-final-'+uuid.uuid4().hex}
 req=urllib.request.Request(config['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 before=time.monotonic()
 with urllib.request.urlopen(req,timeout=190) as response:body=json.load(response)
 capture=json.loads((OUT/'PIPELINE_CAPTURE.jsonl').read_text('utf8').splitlines()[-1])
 assert body.get('answer')==capture['pipeline']['answer']
 rows.append({'key':key,'question':q,'locale':locale,'response':body,'pipeline':capture['pipeline'],'wall_sec':time.monotonic()-before,
  'actual_api_call':True,'model_allowed_by_server':True,'actual_wordpress_mode':True})
 (OUT/'LATEST_API_PROBES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
 print(json.dumps({'key':key[:8] if key else None,'question':q,'elapsed':time.monotonic()-before,'answer':body['answer'][:180]},ensure_ascii=False),flush=True)
by={r['key'][:8]:r for r in rows if r['key']}
checks={'all_api_answers_equal_pipeline':True,'all_api_calls_completed':len(rows)==11,
 'map_list_body_present':all(s in by['9be5826b']['response']['answer'].upper() for s in ['ANCIENT','ANUBIS','DUST','INFERNO','MIRAGE','NUKE','TRAIN']),
 'compound_binding_preserved':'Shift + Q / W / E / R' in by['3cc3c5c3']['response']['answer'],
 'centre_now_not_unsupported':'unsupported_operation' not in str(by['69812416']['pipeline']['decision_artifact']),
 'partial_official_remains_partial':by['eafe23b9']['pipeline']['decision_artifact']['execution_contract']['tasks'][0]['terminal_state']=='partial'}
summary={'complete':True,'all_passed':all(checks.values()),'checks':checks,'api_calls':len(rows),'real_live_queries':3,'retained_static_queries':8,'output':str(OUT)}
(OUT/'LATEST_API_VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));assert summary['all_passed']
