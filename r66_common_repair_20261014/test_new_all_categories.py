"""Ten independent synthetic catalogs; no record enters studio data."""
import sys,os,json,time,copy
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
os.environ['PYTHONPATH']=str(B/'system')
from tests.test_common_content_r58 import CommonTests,ORDER,record
from app.knowledge.common.registry import CATALOG,value
from app.knowledge.common.answer import CommonAnswerer
from datetime import datetime
tag=sys.argv[1] if len(sys.argv)>1 else '02'
llm_enabled=len(sys.argv)>2 and sys.argv[2]=='1'
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='1' if llm_enabled else '0'
from app.knowledge.common.planner import plan_fields
rows=[];start=time.perf_counter()
for n in range(10):
 t=CommonTests();t.setUp()
 try:
  records=[record(kind) for kind in ORDER]
  mapping={r['record_id']:f'r66_synthetic_{n}_{r["kind"]}' for r in records}
  for r in records:
   old=r['record_id'];r['record_id']=mapping[old]
   r['aliases']={'th':[f'ข้อมูลตัวอย่างรอบ{n}หมวด{r["kind"]}'],'en':[f'R66 synthetic {n} {r["kind"]}']}
   for spec in CATALOG[r['kind']]['fields']:
    f=r['fields'][spec['key']]
    if spec['reference_kind'] and f['status']=='known':
     v=f['value'];f['value']=[mapping.get(x,x) for x in v] if isinstance(v,list) else mapping.get(v,v)
   t.approve(t.save(r))
  t.publish()
  reader=CommonAnswerer(t.store)
  for r in records:
   for lang in ('th','en'):
    q=(r['aliases'][lang][0]+(' ข้อมูลทั้งหมด' if lang=='th' else ' all details'))
    before=time.perf_counter()
    try:
     a=reader.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if llm_enabled else None)
     art=a.decision_artifact if a else {};ids=art.get('query_plan',{}).get('record_ids',[])
     expected_known={k for k,f in r['fields'].items() if f['status']=='known'}
     returned_known={o['field'] for o in art.get('obligations',[]) if o['record_id']==r['record_id'] and o['status']=='known'}
     fail=[]
     if a is None:fail.append('no_common_response')
     if r['record_id'] not in ids:fail.append('wrong_primary_target')
     if expected_known-returned_known:fail.append('missing_known_fields:'+str(sorted(expected_known-returned_known)))
     if a and not a.validation.ok:fail.extend(a.validation.errors)
     row={'catalog':n,'kind':r['kind'],'locale':lang,'question':q,'passed':not fail,'failures':fail,'expected_known':sorted(expected_known),'returned_known':sorted(returned_known),'answer':a.answer if a else None,'elapsed':time.perf_counter()-before}
    except Exception as e:row={'catalog':n,'kind':r['kind'],'locale':lang,'passed':False,'failures':[repr(e)]}
    rows.append(row)
 finally:t.tearDown()
out=B/('NEW_ALL_CATEGORIES_'+tag+'.jsonl')
with out.open('x',encoding='utf-8') as f:
 for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
summary={'catalogs':10,'categories':24,'requests':len(rows),'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows),'elapsed':time.perf_counter()-start,'fixture_only':True,'production_facts':False,'llm_enabled':llm_enabled,'llm_calls':0,'reason_no_model_call':'explicit all-details queries are deterministic; real calls measured separately in matrix/HTTP'}
(B/('NEW_ALL_CATEGORIES_SUMMARY_'+tag+'.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary),flush=True)
sys.exit(0 if summary['failed']==0 else 1)
