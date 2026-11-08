"""Backward-compatible optional metadata; does not change factual values."""
import copy,json
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
localized={'type':'object','properties':{'th':{'type':'string','maxLength':120},'en':{'type':'string','maxLength':120}},'required':['th','en'],'additionalProperties':False,'anyOf':[{'properties':{'th':{'minLength':1}}},{'properties':{'en':{'minLength':1}}}]}
profile={'type':'object','properties':{'task':{'type':'string','enum':['permission','correction']},'subjects':{'type':'array','minItems':1,'maxItems':12,'items':localized},'ownership':{'type':'string','enum':['any','personal']},'context':{'type':'string','enum':['studio','competition']}},'required':['task','subjects','ownership','context'],'additionalProperties':False}
catalog=json.loads((H/'catalog.json').read_text('utf8'))
for kind in ['faq','policy','procedure']:
 item=next(x for x in catalog if x['kind']==kind)
 if any(f['key']=='query_profile' for f in item['fields']):raise ValueError('Already extended')
 item['fields'].append({'key':'query_profile','meaning_th':'ช่วยเลือกคำตอบ: ประเภทคำถาม เรื่อง และขอบเขต','value_schema':profile,'reference_kind':None,'publish_core':False})
 schema_path=H/'schemas'/f'{kind}.schema.json';schema=json.loads(schema_path.read_text('utf8'))
 field=copy.deepcopy(schema['properties']['fields']['properties'][next(iter(schema['properties']['fields']['properties']))])
 # Reuse the existing provenance/status envelope; substitute its typed value.
 field['description']='ข้อมูลช่วยเลือกคำตอบตาม task/subject/scope ไม่ใช่ข้อเท็จจริงใหม่'
 field['oneOf'][0]['properties']['value']=profile
 schema['properties']['fields']['properties']['query_profile']=field
 schema_path.write_text(json.dumps(schema,ensure_ascii=False,indent=2),encoding='utf8')
 template_path=H/'templates'/f'{kind}.draft.json';r=json.loads(template_path.read_text('utf8'))
 r['fields']['query_profile']={'status':'unknown','value':None,'evidence_refs':[],'note':'ข้อมูลช่วยค้น ไม่ใช่ข้อเท็จจริงหรือนโยบายใหม่'}
 template_path.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf8')
(H/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Added optional query_profile to 3 kinds; existing records are not rewritten.')
