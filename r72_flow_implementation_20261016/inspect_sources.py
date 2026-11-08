import os,sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
os.environ['PSU_KNOWLEDGE_DB']=str(B/'system/data/knowledge/common.sqlite')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value
s=MigratedView(Path(os.environ['PSU_KNOWLEDGE_DB'])).snapshot();rs=s['release']['records']
rows=[]
for rid,r in rs.items():
    intent=value(r,'intent_key') or ''
    if r['kind']=='faq' and any(k in intent for k in ['payment','bank','session','studio_rules','maximum','booking_steps']):
        rows.append({'id':rid,'intent':intent,'question':value(r,'question'),'answer':value(r,'answer'),'validity':r['validity']})
    if r['kind']=='game' and 'god_of_war' in rid:
        rows.append({'id':rid,'record':r})
(B/'SOURCE_INSPECTION.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(rows,ensure_ascii=False,indent=2))
