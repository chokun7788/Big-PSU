import os,sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value
s=MigratedView(B/'system/data/knowledge/common.sqlite').snapshot();rows=[]
for rid,r in s['release']['records'].items():
 if r['kind'] in {'policy','procedure'} or r['kind']=='faq' and any(t in json.dumps(r,ensure_ascii=False).lower() for t in ['keyboard','overpaid','underpaid','installment','โอนเกิน','โอนขาด','อายุขั้นต่ำ','minimum age','wrong slip']):rows.append({'id':rid,'record':r})
(B/'SOURCE_INSPECTION.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for x in rows:
 r=x['record'];print(json.dumps({'id':x['id'],'kind':r['kind'],'fields':{k:value(r,k) for k in r['fields'] if value(r,k) is not None}},ensure_ascii=False))
print('Kinds',[(r['kind'],r['record_id']) for r in s['release']['records'].values() if r['kind']=='contact'])
