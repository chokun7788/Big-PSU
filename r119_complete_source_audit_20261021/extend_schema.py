"""Add explicit, owner-editable fields missing from the canonical adapter."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parent;H=R/'system/app/knowledge/common'
catalog=json.loads((H/'catalog.json').read_text('utf8'));changes=[]
def extend(kind,key,meaning,schema,reference=None):
 item=next(x for x in catalog if x['kind']==kind)
 if any(f['key']==key for f in item['fields']):return
 item['fields'].append({'key':key,'meaning_th':meaning,'publish_core':False,'reference_kind':reference,'value_schema':schema})
 p=H/'schemas'/f'{kind}.schema.json';s=json.loads(p.read_text('utf8'))
 field=copy.deepcopy(next(iter(s['properties']['fields']['properties'].values())))
 field['description']=meaning
 field['oneOf'][0]['properties']['value']=schema
 s['properties']['fields']['properties'][key]=field
 p.write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8')
 p=H/'templates'/f'{kind}.draft.json';t=json.loads(p.read_text('utf8'))
 t['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':meaning}
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2),'utf8');changes.append({'kind':kind,'field':key})
for item in catalog:
 extend(item['kind'],'legacy_context','บริบทต้นทางเดิมเพื่อการตรวจสอบ ไม่ใช่คำตอบลูกค้าโดยตรง',{'type':'object'})
for kind in ['game','service']:
 extend(kind,'studio_zone_ids','โซนบริการที่ต้นทางระบุโดยตรง ไม่จำเป็นต้องผ่าน resource',{'type':'array','items':{'type':'string'},'uniqueItems':True},'zone')
extend('faq','legacy_search','หัวข้อ รูปแบบคำถาม และลำดับจากข้อมูลเดิมเพื่อค้นเท่านั้น',{'type':'object'})
extend('person','role_aliases','คำเรียกตำแหน่งสำหรับค้น ไม่เปลี่ยนตำแหน่งจริง',{'type':'array','items':{'type':'string'},'uniqueItems':True})
slot={'type':'object','properties':{k:{'type':'string'} for k in ['code','label','start','end','state','time_range','note']},'required':['start','end','state'],'additionalProperties':False}
extend('schedule','service_slots','ตารางช่วงให้บริการเล่นตาม Flow เดิม แยกจากเวลาเปิดพื้นที่',{'type':'array','items':slot})
extend('schedule','service_closed','วันหยุดบริการตามตารางประจำ',{'type':'boolean'})
(H/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),'utf8')
(R/'SCHEMA_EXTENSIONS.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'extensions':len(changes)}))
