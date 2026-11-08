import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.projection import value
rs=MigratedView(S/'data/knowledge/common.sqlite').snapshot()['release']['records']
for rid,r in rs.items():
 if r['kind']!='faq':continue
 q=str(value(r,'question'));a=str(value(r,'answer'))
 if any(t in q for t in ['สองคน','สี่คน','2 คน','4 คน','กี่คน','two people','four people','ผู้เล่นพร้อม','player','video','record','capture','ถ่าย','วิดีโอ']):
  print(json.dumps({'id':rid,'q':q,'a':a},ensure_ascii=False))
