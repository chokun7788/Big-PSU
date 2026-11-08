"""Optional owner data field, no edits to any content record or database."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parent/'system/app/knowledge/common'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
catalog=read(R/'catalog.json');kind=next(x for x in catalog if x['kind']=='control_set');key='input_device_model';meaning='รุ่นอุปกรณ์ควบคุมที่ตรวจยืนยันกับชุดปุ่มนี้ ไม่อนุมานจากแพลตฟอร์มเกม'
if not any(x['key']==key for x in kind['fields']):kind['fields'].insert(3,{'key':key,'meaning_th':meaning,'publish_core':False,'reference_kind':None,'value_schema':{'type':'string','minLength':1}})
schema=read(R/'schemas/control_set.schema.json');field=copy.deepcopy(schema['properties']['fields']['properties']['preset']);field['description']=meaning;schema['properties']['fields']['properties'][key]=field
template=read(R/'templates/control_set.draft.json');template['fields'].setdefault(key,{'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่มีข้อมูลยืนยันรุ่นอุปกรณ์ควบคุม ไม่อนุมานจากชื่อแพลตฟอร์ม'})
write(R/'catalog.json',catalog);write(R/'schemas/control_set.schema.json',schema);write(R/'templates/control_set.draft.json',template)
print(json.dumps({'optional_field':key,'existing_records_modified':False,'wire_changed':False}))
