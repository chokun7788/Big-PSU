"""Apply additive schema/code support, after the preceding run has finished."""
import json,sys,shutil,pprint
from pathlib import Path
B=Path(__file__).resolve().parent;S=B/'system/app/knowledge/common'
catalog=json.loads((S/'catalog.json').read_text(encoding='utf-8'))
rate=next(r for r in catalog if r['kind']=='rate');rule=next(f for f in rate['fields'] if f['key']=='calculation_rule')
if 'session_ceil' not in rule['value_schema']['enum']:rule['value_schema']['enum'].append('session_ceil')
(S/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
schema=json.loads((S/'schemas/rate.schema.json').read_text(encoding='utf-8'))
def extend(x):
 if isinstance(x,dict):
  if x.get('enum')==['fixed','linear','no_extrapolation']:x['enum'].append('session_ceil')
  for v in x.values():extend(v)
 elif isinstance(x,list):
  for v in x:extend(v)
extend(schema);(S/'schemas/rate.schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
shutil.copyfile(B/'proposed_billing.py',S/'billing.py')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.query_contract import CUES
updates={'usage':['ใช้ทำอะไร','ใช้สำหรับ','ทำอะไรได้','used for','purpose','use this for'],
 'role':['ตำแหน่ง','หน้าที่','job title','position'],
 'specifications':['การ์ดจอ','ซีพียู','หน่วยความจำ','แรม','GPU','CPU','RAM','graphics card'],
 'amount_minor':['ต้องจ่าย','จ่ายไหม','เสียเงิน','ต้องเสียเงิน','pay for','payment required']}
for k,terms in updates.items():CUES[k]=list(dict.fromkeys(CUES.get(k,[])+terms))
p=S/'query_contract.py';text=p.read_text(encoding='utf-8');start=text.index('CUES={');end=text.index('\nLOCATION=',start);text=text[:start]+'CUES='+pprint.pformat(CUES,width=110,sort_dicts=False)+ '\n'+text[end:];p.write_text(text,encoding='utf-8')
p=S/'rendering.py';text=p.read_text(encoding='utf-8');anchor='OPERATORS={';text=text.replace(anchor,"ENUMS['calculation_rule']['session_ceil']=('คิดเต็มรอบ ปัดขึ้นตามระยะเวลา','Round up to a whole billing session')\n"+anchor,1);p.write_text(text,encoding='utf-8')
p=S/'budget.py';text=p.read_text(encoding='utf-8');text=text.replace("rule=='linear' and price>0","rule in {'linear','session_ceil'} and price>0");p.write_text(text,encoding='utf-8')
profiles=json.loads((S/'answer_profiles.json').read_text(encoding='utf-8'));labels=profiles.setdefault('labels',{})
for kind,fields in {'faq':{'answer':('ข้อมูลที่ยืนยันได้','Confirmed information'),'scope_note':('ขอบเขตของข้อมูล','Scope')},'service':{'name':('บริการ','Service'),'session_minutes':('เวลาเล่นต่อรอบ','Play time per session'),'occupancy_minutes':('เวลาที่กันช่องจอง','Booking occupancy')},'game':{'supported_platforms':('แพลตฟอร์มที่ตัวเกมรองรับ','Game-supported platforms')},'person':{'role':('ตำแหน่ง/หน้าที่','Role')}}.items():
 for key,(th,en) in fields.items():labels.setdefault(kind,{})[key]={'th':th,'en':en}
(S/'answer_profiles.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Additive session_ceil schema support applied; records and approvals untouched')
