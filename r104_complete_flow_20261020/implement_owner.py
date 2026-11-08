"""Guided mapping controls; no raw JSON required in the owner flow."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent/'system/app/knowledge/common'
labels={'binding_id':'รหัสข้อเท็จจริง (ตั้งครั้งเดียว)','predicate':'ใช้ตอบเรื่องใด','subject_ref':'รายการที่ข้อเท็จจริงนี้กล่าวถึง','unit':'หน่วยคิดค่าบริการ (ถ้าเกี่ยวข้อง)',
 'actor_scope':'กลุ่มผู้ใช้ที่ใช้ข้อมูลนี้','value_ref':'เลือกช่องที่เป็นหลักฐานคำตอบ','condition_refs':'ช่องที่ระบุเงื่อนไข','exception_refs':'ช่องที่ระบุข้อยกเว้น',
 'conditions_status':'ทราบเงื่อนไขครบแล้วหรือไม่','exceptions_status':'ทราบข้อยกเว้นครบแล้วหรือไม่','applicability':'ขอบเขตและวันที่ใช้ข้อมูลนี้',
 'dependency_refs':'ข้อเท็จจริงที่ต้องอ่านด้วย (รหัสรายการ#รหัสข้อ)','supersedes_refs':'ใช้แทนข้อใด (ต้องมีหลักฐานยืนยันการแทนที่)',
 'status':'สถานะการยืนยัน','value':'กลุ่มผู้ใช้ (ไม่เลือกรายการเมื่อยืนยันว่าใช้กับทุกกลุ่ม)',
 'record_id':'เลือกรายการต้นทาง','field':'เลือกช่องข้อมูล','path':'เลือกภาษา: /th หรือ /en; เว้นว่างสำหรับค่าตัวเลข',
 'projection':'อ่านเป็นข้อความ/ค่าตรงต้นฉบับ หรือจำนวนเงินที่ระบุชัด','quote':'ข้อความอ้างตรงต้นฉบับ (ถ้าต้องการเฉพาะส่วน)',
 'service_ids':'ใช้กับบริการใด','duration_minutes':'เวลาที่ราคาครอบคลุม (นาที)','platform':'แพลตฟอร์ม (ถ้าจำกัด)','effective_from':'เริ่มมีผล (ISO พร้อมเขตเวลา)','effective_until':'สิ้นสุด (ถ้ามี)'}
p=R/'schemas/claim_binding.schema.json';schema=json.loads(p.read_text('utf8'))
for k in ('conditions_status','exceptions_status'):schema['properties'][k]={'enum':['unknown','known']};schema['required'].append(k)
p.write_text(json.dumps(schema,ensure_ascii=False,indent=2),'utf8')
catalog=json.loads((R/'catalog.json').read_text('utf8'))
for c in catalog:
 p=R/'schemas'/f"{c['kind']}.schema.json";x=json.loads(p.read_text('utf8'));x['properties']['claim_bindings']['items']=schema;p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
ui=json.loads(json.dumps(schema));ui['properties']={k:v for k,v in ui['properties'].items() if k not in {'evidence_refs','authority_refs'}}
ui['required']=[k for k in ui['required'] if k in ui['properties']]
fields=sorted({f['key'] for c in catalog for f in c['fields']})
def decorate(x,key=''):
 if isinstance(x,dict):
  if key in labels:x['x-label']=labels[key]
  if key in {'subject_ref','record_id'}:x['x-reference-kind']='*'
  if key=='service_ids':x['x-reference-kind']='service'
  if key=='field':x['enum']=fields
  for k,s in x.get('properties',{}).items():decorate(s,k)
  if 'items' in x:decorate(x['items'],key)
decorate(ui);(R/'schemas/claim_binding.ui.json').write_text(json.dumps(ui,ensure_ascii=False,indent=2),'utf8')
p=R/'owner_server.py';t=p.read_text('utf8');old="'kinds':24})";assert t.count(old)==1;t=t.replace(old,"'kinds':24,'claim_schema':json.loads((HOME/'schemas/claim_binding.ui.json').read_text('utf8'))})")
t=t.replace("change_note=body.get('change_note')))","change_note=body.get('change_note'),mapping_authority_confirmed=body.get('mapping_authority_confirmed') is True))")
p.write_text(t,'utf8')
p=R/'ui/owner.js';t=p.read_text('utf8')
t=t.replace("function valueEditor(schema,val,refKind=null,key=\"\"){","function valueEditor(schema,val,refKind=null,key=\"\"){\n refKind=refKind||schema['x-reference-kind']||null;")
t=t.replace("let l=node('label',SUB_LABELS[k]||k)","let l=node('label',sub['x-label']||SUB_LABELS[k]||k)")
t=t.replace("function collect(){let r=structuredClone(record);","function collect(){let r=structuredClone(record);if(claimEditor){r.claim_bindings=claimEditor.get().map(cleanClaim);if(r.claim_bindings.length)r.schema_version='studio-content-3.1';}")
t=t.replace(" showGuide(r.kind);updateReadiness();renderEditTools();"," renderClaimEditor(r);showGuide(r.kind);updateReadiness();renderEditTools();")
t=t.replace("let x=await api('/api/registry');catalog=","let x=await api('/api/registry');claimSchema=x.claim_schema;catalog=")
t+='''
let claimSchema=null,claimEditor=null;
function cleanClaim(b){
 b.evidence_refs=[];b.authority_refs=record.claim_bindings?.find(x=>x.binding_id===b.binding_id)?.authority_refs||[];
 for(let k of ['unit'])if(!b[k])b[k]=null;
 if(b.actor_scope.status==='unknown')b.actor_scope.value=null;
 for(let k of ['platform','effective_from','effective_until','duration_minutes'])if(!b.applicability[k])b.applicability[k]=null;
 for(let ref of [b.value_ref,...b.condition_refs,...b.exception_refs])if(!ref.quote)ref.quote=null;
 return b;
}
function renderClaimEditor(r){
 if(!claimSchema)return;
 let box=node('details'),title=node('summary','เชื่อมข้อเท็จจริงระหว่างรายการ (สำหรับข้อมูลซ้ำหรืออ้างอิงข้ามหมวด)');
 box.append(title,node('p','ปกติกรอกข้อมูลในหมวดนั้นได้เลย ส่วนนี้ใช้เมื่อ FAQ อ้างราคา/กฎจากรายการอื่น เลือกรายการและช่องต้นทาง พร้อมเงื่อนไขและวันมีผล ไม่มีการสร้างสิทธิ์หรือเปลี่ยนราคาให้อัตโนมัติ'));
 claimEditor=valueEditor({type:'array',items:claimSchema},r.claim_bindings||[],null,'claim_bindings');box.append(claimEditor.root);
 box.addEventListener('change',()=>{dirty=true;updateReadiness();});$('fields').append(box);
}
'''
p.write_text(t,'utf8')
print('Owner guided mapping controls and metadata confirmation schema installed')
