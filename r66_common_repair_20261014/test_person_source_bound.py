import sys,json,os,hashlib,sqlite3,time
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B/'system'),str(B)]
from harness import configure,test_temp
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.planner import plan_fields
from datetime import datetime
tag=sys.argv[1];llm=sys.argv[2]=='1';test_temp('person_'+tag);configure('common',llm);s=CommonStore(B/'common.sqlite');reader=CommonAnswerer(s)
with s.connect() as c:rs=s.heads(c)
review=json.loads((B/'PERSON_TRANSLATION_REVIEW.json').read_text(encoding='utf-8'));roles={x['record_id']:x['reviewed_en'] for x in review['reviewed_fields'] if x['field']=='role'};rows=[]
for rid,r in rs.items():
 if r['kind']!='person':continue
 for lang in ['th','en']:
  name=value(r,'display_name');q=name['th']+' ทำตำแหน่งอะไร' if lang=='th' else 'What is '+name['th']+"'s role?";start=time.perf_counter()
  a=reader.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if llm else None);fail=[]
  if not a:fail.append('no_answer')
  else:
   if name['th'] not in a.answer:fail.append('source_name_not_preserved')
   if (value(r,'role')['th'] if lang=='th' else roles[rid]) not in a.answer:fail.append('role_not_source_bound')
   if not a.validation.ok:fail.extend(a.validation.errors)
   if a.decision_artifact['query_plan']['record_ids']!=[rid]:fail.append('wrong_person')
  rows.append({'record_id':rid,'locale':lang,'question':q,'passed':not fail,'failures':fail,'answer':a.answer if a else None,'elapsed':time.perf_counter()-start})
byrole={}
for rid,r in rs.items():
 if r['kind']!='person':continue
 for lang,role in value(r,'role').items():byrole.setdefault((lang,role),[]).append(rid)
for (lang,role),expected in byrole.items():
 q='ใครเป็น'+role if lang=='th' else 'Who is the '+role+'?';start=time.perf_counter();a=reader.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if llm else None);fail=[]
 if not a:fail.append('no_answer')
 elif set(a.decision_artifact['query_plan']['record_ids'])!=set(expected):fail.append('wrong_role_members')
 elif not a.validation.ok:fail.extend(a.validation.errors)
 rows.append({'role':role,'locale':lang,'question':q,'passed':not fail,'failures':fail,'answer':a.answer if a else None,'elapsed':time.perf_counter()-start})
out=B/('PERSON_TEST_'+tag+'.json');out.write_text(json.dumps({'tests_run':len(rows),'passed':sum(x['passed'] for x in rows),'llm_enabled':llm,'official_romanization_verified':False,'translation_review':'agent reviewed against Thai role text; not owner approval','rows':rows},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'tests_run':len(rows),'passed':sum(x['passed'] for x in rows),'llm_enabled':llm}));raise SystemExit(0 if all(x['passed'] for x in rows) else 1)
