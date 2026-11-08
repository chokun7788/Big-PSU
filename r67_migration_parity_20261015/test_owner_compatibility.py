import os,sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='0'
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import preview_answer
from app.knowledge.common.registry import validate
from app.knowledge.common.translation import translate_draft
store=CommonStore(B/'common.sqlite');old=CommonStore(B/'before.sqlite');results=[]
with old.connect() as c:
 rs=old.heads(c);src=old.sources(c)
 errors={rid:err for rid,r in rs.items() if (err:=validate(r,rs,src))}
results.append({'name':'all_older_payloads_validate_with_additive_schema','passed':not errors,'errors':errors,'records':len(rs)})
# No pending strings -> no model/network call. This older payload lacks new optional keys.
r=next(r for r in rs.values() if r['kind']=='control_set')
import copy
empty=copy.deepcopy(r)
for field in empty['fields'].values():field.update(status='unknown',value=None,evidence_refs=[],note='Compatibility-only draft')
translated=translate_draft(empty);results.append({'name':'older_translation_form_no_keyerror','passed':translated['translated_count']==0})
for q,lang,need in [('PC มีหมายเหตุอะไรบ้าง','th','Warzone'),('What time is the afternoon session?','en','13:00'),('พกอาหารจากข้างนอกเข้าไปได้ไหม','th','ยังไม่ได้ระบุ'),('TEKKEN 8 การแก้ข้อพิพาททำยังไง','th','กรรมการ'),('Mario Kart 8 Deluxe ปุ่ม A ทำอะไร','th','เร่งเครื่อง')]:
 try:
  r=preview_answer(store,q,locale=lang,draft=True);results.append({'name':q,'passed':r is not None and need in r.answer and r.validation.ok and r.decision_artifact['content_view']=='evaluation_draft','answer':r.answer if r else None})
 except Exception as e:results.append({'name':q,'passed':False,'exception':repr(e)})
(B/('OWNER_COMPATIBILITY_'+(sys.argv[1] if len(sys.argv)>1 else 'initial')+'.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(results,ensure_ascii=False))
