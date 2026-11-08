import sys,json,re
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c)
out=[]
for rid,r in rs.items():
 if r['kind']=='faq':
  q=json.dumps(value(r,'question'),ensure_ascii=False)
  if not re.search(r'address|location|damage|penalt|payment|walk|without.book|booking.required|ที่ตั้ง|อยู่ที่|อยู่ไหน|เสียหาย|ค่าปรับ|หลังจอง|ไม่จอง|ต้องจอง|ชำระ|จ่าย|ที่อยู่',q,re.I):continue
 elif r['kind']=='equipment_model':
  if 'Gaming PC' not in json.dumps(value(r,'name'),ensure_ascii=False):continue
 elif r['kind']=='game_service':
  game=rs.get(value(r,'game_id'));g=json.dumps(value(game,'title'),ensure_ascii=False) if game else ''
  if 'Warzone' not in g:continue
 else:continue
 out.append(r);print(json.dumps({'id':rid,'kind':r['kind'],'fields':{k:value(r,k) for k in r['fields']}},ensure_ascii=False))
(B/'RESIDUAL_SOURCE_RECORDS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
