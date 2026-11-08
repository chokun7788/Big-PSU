import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask
from app.knowledge.common.domain_flow.financial import audience_mentions,rate_pool,billing
from app.knowledge.common.domain_flow.projection import value
e=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot(),cache_key=S);rows={}
for q,cat,domain,facet in [('God of War Ragnarök เล่นได้ที่โซนไหน','C04','games','zone'),('แล้วถ้าต้องการยกเลิกล่ะ การจอง booking','C08','reservation','owner_policy'),('นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง รวมกี่บาท','C06','service_fee','amount'),('แข่ง VALORANT ถ้าทำผิดกฎจะโดนลงโทษอะไรบ้าง','C13','competition_rules','rule_clause')]:
 m=MeaningTask(q,domain,cat,'rule_lookup' if cat=='C13' else 'price_calculate' if cat=='C06' else 'detail',facet)
 p=e.plan(cat,q,meaning=m)
 rows[q]={'plan':p.__dict__,'facts':[{k:f.get(k) for k in ['id','record_id','facet','subject','value','event_id']} for f in e.index.bind(cat,q)],'audiences':list(audience_mentions(e.index,q)[0]) if cat=='C06' else None}
 if cat=='C04':rows[q]['games']=[r for r in e.index.records.values() if r['kind']=='game' and 'god' in str(r).lower()]
 if cat=='C06':rows[q]['rate_pool']=[{k:f.get(k) for k in ['id','numeric','billing_unit','calculation_rule','confirmation_as_of']}|{'rate':e.index.records[f['record_id']]} for f in rate_pool(e.index,q) if f['facet']=='amount']
(R/'DEBUG_CONTRACTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2,default=str),'utf8')
for q,r in rows.items():print(json.dumps({'q':q,'plan':r['plan'],'bound_records':sorted({f['record_id'] for f in r['facts']}),'audiences':r['audiences']},ensure_ascii=False,default=str))
