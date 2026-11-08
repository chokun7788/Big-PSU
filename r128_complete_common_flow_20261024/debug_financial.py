import os,sys,json
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.dialogue_task import resolve
from app.knowledge.common.domain_flow.financial import rate_pool,billing,unit_calculation
from app.knowledge.common.domain_flow.projection import value
from app.knowledge.common.domain_flow.native_intents import propose
s=MigratedView(S/'data/knowledge/common.sqlite').snapshot();e=Engine.from_snapshot(s,cache_key=S);i=e.index;a=datetime.fromisoformat('2026-10-24T12:00:00+07:00')
c=resolve(i,'นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง ราคาเท่าไหร่',[],s['active'],a)
d=resolve(i,'แล้วสามชั่วโมงล่ะ',[{'role':'assistant','delivery_status':'client_acknowledged','common_read_state':{'schema_version':1,'dialogue_task':c['task']}}],s['active'],a);q=d['execution_question']
fs=[f for f in rate_pool(i,q) if f['facet']=='amount'];out={'context':d,'rates':[{'id':f['record_id'],'subject':f['subject'],'period':value(i.records[f['record_id']],'duration_minutes'),'rule':f.get('calculation_rule'),'billing':f.get('billing_unit'),'validity':i.records[f['record_id']]['validity'],'unit':unit_calculation(i,f,q)} for f in fs],'billing':str(billing(i,q,fs)),'answer':e.answer(q,'th',at=a,allow_llm=False,understanding=propose(i,q))}
(R/'DEBUG_FINANCIAL.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str),'utf8');print(json.dumps(out,ensure_ascii=False,indent=2,default=str)[:18000])
