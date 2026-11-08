"""Necessary retest of three observed API regressions, preserved separately."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text());out=Path(c['output']);rows=[]
cases=[('building_floor','อยู่ตึกอะไร ชั้นไหน?',{'center_psu_phuket'},['5','1']),('guardian','เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองหรือเปล่า?',{'r114_q032_owner_policy'},['เซ็นยินยอม']),('documents','What ID does an external visitor need to use the studio?',set(),[])]
with (out/'TARGETED_REGRESSIONS.jsonl').open('x',encoding='utf8') as f:
 for name,q,expected,words in cases:
  p={'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':'r132-followup-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex};t=time.perf_counter()
  req=urllib.request.Request(c['url']+'/api/chat',json.dumps(p,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=195) as response:a=json.load(response)
  art=a['decision_artifact'];ids=set(art['query_plan']['record_ids']);u=art.get('understanding') or {};tasks=u.get('tasks') or []
  passed=expected<=ids and all(w in a['answer'] for w in words) and a['validation_ok'] and not a.get('timed_out')
  if name=='documents':passed=passed and any(t.get('canonical_operation')=='policy.checkin_documents' for t in tasks) and 'r114_q037_owner_policy' not in ids
  row={'name':name,'question':q,'response':a,'passed':passed,'elapsed_sec':time.perf_counter()-t};rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  print(json.dumps({'name':name,'passed':passed,'answer':a['answer'],'ids':sorted(ids)},ensure_ascii=False),flush=True)
(out/'TARGETED_COMPLETE.json').write_text(json.dumps({'all_passed':all(x['passed'] for x in rows),'requests':len(rows),'retest_reason':'actual source selection regressions fixed; no whole owner50 rerun','semantic_accuracy':None},indent=2),'utf8')
assert all(x['passed'] for x in rows)
