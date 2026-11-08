"""Optional typed registration observation fields; no existing record rewrite."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parent/'system/app/knowledge/common'
fields=[('registration_status','สถานะรับสมัครที่แหล่งข้อมูลยืนยัน',{'type':'string','enum':['not_open','open','closed','cancelled']}),('registration_status_as_of','เวลาอ้างอิงการตรวจสถานะรับสมัคร',{'type':'string','format':'date-time'}),('registration_status_max_age_seconds','อายุสูงสุดของหลักฐานสถานะรับสมัคร หน่วยวินาที',{'type':'integer','minimum':1})]
p=R/'catalog.json';catalog=json.loads(p.read_text('utf8'));news=next(x for x in catalog if x['kind']=='news')
schema=json.loads((R/'schemas/news.schema.json').read_text('utf8'));template=json.loads((R/'templates/news.draft.json').read_text('utf8'))
for key,label,value_schema in fields:
 if not any(f['key']==key for f in news['fields']):news['fields'].append({'key':key,'meaning_th':label,'publish_core':False,'reference_kind':None,'value_schema':value_schema})
 if key not in schema['properties']['fields']['properties']:
  field=copy.deepcopy(schema['properties']['fields']['properties']['event_start']);field['description']=label
  field['oneOf'][0]['properties']['value']=value_schema;schema['properties']['fields']['properties'][key]=field
 template['fields'].setdefault(key,{'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่มีข้อมูลยืนยันสำหรับช่องนี้'})
for path,data in [(p,catalog),(R/'schemas/news.schema.json',schema),(R/'templates/news.draft.json',template)]:path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
