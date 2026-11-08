import os,sys,json
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.dialogue_task import resolve
s=MigratedView(S/'data/knowledge/common.sqlite').snapshot();i=Engine.from_snapshot(s,cache_key=S).index;a=datetime.fromisoformat('2026-10-24T12:00:00+07:00')
for q,q2 in [('PC2 วันที่ 27 ตุลาคม 2026 เวลา 15:00-16:00 ว่างไหม','แล้ว PC3 ล่ะ'),('ราคาเหมา PC เต็มวัน หน่วยงานภายใน','แล้วครึ่งวันล่ะ')]:
 c=resolve(i,q,[],s['active'],a);d=resolve(i,q2,[{'role':'assistant','delivery_status':'client_acknowledged','common_read_state':{'schema_version':1,'dialogue_task':c['task']}}],s['active'],a)
 print(json.dumps([c,d],ensure_ascii=False,indent=2))
