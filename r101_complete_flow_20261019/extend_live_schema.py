"""Add optional typed freshness metadata; never change existing owner records."""
import copy,json
from pathlib import Path
B=Path(__file__).resolve().parent/'system/app/knowledge/common'
path=B/'catalog.json';catalog=json.loads(path.read_text('utf8'));row=next(x for x in catalog if x['kind']=='live_binding')
key='freshness_max_age_seconds'
if not any(f['key']==key for f in row['fields']):
 row['fields'].append({'key':key,'meaning_th':'ยอมรับข้อมูลสดที่เก่าได้ไม่เกินกี่วินาที (ระบุจากนโยบายจริง ไม่กำหนดให้เอง)','publish_core':False,'reference_kind':None,'value_schema':{'type':'integer','minimum':1,'maximum':3600}})
 path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n','utf8')
schema_path=B/'schemas/live_binding.schema.json';schema=json.loads(schema_path.read_text('utf8'))
cell=copy.deepcopy(schema['properties']['fields']['properties']['external_resource_key'])
cell['description']=row['fields'][-1]['meaning_th']
for alternative in cell['oneOf']:
 if alternative.get('properties',{}).get('status',{}).get('const')=='known':alternative['properties']['value']={'type':'integer','minimum':1,'maximum':3600}
schema['properties']['fields']['properties'][key]=cell
schema_path.write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n','utf8')
template_path=B/'templates/live_binding.draft.json';template=json.loads(template_path.read_text('utf8'))
template['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่ได้ระบุอายุข้อมูลสดสูงสุดจากนโยบายที่ยืนยัน'}
template_path.write_text(json.dumps(template,ensure_ascii=False,indent=2)+'\n','utf8')
print('Optional typed freshness field added; stored data untouched')
