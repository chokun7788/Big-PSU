"""Additive content model: preserve partial facts, not a second opaque text dump."""
import copy,json
from pathlib import Path
H=Path(__file__).resolve().parent/'system/app/knowledge/common'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
catalog=read(H/'catalog.json');by={x['kind']:x for x in catalog}
local=copy.deepcopy(next(f['value_schema'] for f in by['game']['fields'] if f['key']=='summary'))
changes={
 'person':[('affiliation','สังกัดตามต้นฉบับ',local),('period','วาระหรือช่วงเวลาตามต้นฉบับ',local)],
 'service':[('notes','หมายเหตุของบริการ',local)],
 'control_set':[('source_summary','ภาพรวมชุดปุ่มตามต้นฉบับ',local)],
 'competition':[('source_title','ชื่อหัวเอกสารต้นฉบับ',local)],
 'competition_rule':[('facets','หัวข้อย่อยที่ข้อความส่วนนี้รองรับ (จัดหมวดจากต้นฉบับ)',{'type':'array','items':{'type':'string','minLength':1},'uniqueItems':True}),('source_order','ลำดับข้อความในเอกสารต้นฉบับ',{'type':'integer','minimum':1})]
}
for kind,fields in changes.items():
 schema=read(H/'schemas'/f'{kind}.schema.json');template=read(H/'templates'/f'{kind}.draft.json')
 base=copy.deepcopy(next(iter(schema['properties']['fields']['properties'].values())))
 for key,meaning,vs in fields:
  by[kind]['fields'].append({'key':key,'meaning_th':meaning,'publish_core':False,'reference_kind':None,'value_schema':copy.deepcopy(vs)})
  slot=copy.deepcopy(base);slot['description']=meaning;slot['oneOf'][0]['properties']['value']=copy.deepcopy(vs)
  schema['properties']['fields']['properties'][key]=slot
  # Optional for older records; the owner form supplies an explicit unknown slot.
  template['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่มีข้อมูลยืนยันสำหรับช่องนี้'}
 write(H/'schemas'/f'{kind}.schema.json',schema);write(H/'templates'/f'{kind}.draft.json',template)
# Gesture and context are independent facts, not reasons to hide a known button/action.
item=next(f for f in by['control_set']['fields'] if f['key']=='bindings')['value_schema']['items']
item['properties']['gesture']['enum'].append('unknown')
item['properties']['context'].pop('anyOf',None)
item['properties']['notes']=copy.deepcopy(local);item['properties']['notes'].pop('anyOf',None)
item['properties']['section']=copy.deepcopy(local);item['properties']['section'].pop('anyOf',None)
item['properties']['source_order']={'type':'integer','minimum':1}
schema=read(H/'schemas/control_set.schema.json')
schema['properties']['fields']['properties']['bindings']['oneOf'][0]['properties']['value']['items']=copy.deepcopy(item)
write(H/'schemas/control_set.schema.json',schema);write(H/'catalog.json',catalog)
# Reuse field meanings for open wording; do not hard-code individual people/games.
p=H/'query_contract.py';s=p.read_text('utf8');s=s.replace("CUES={'how_to_play':", "CUES={'affiliation':['สังกัด','affiliation','affiliated'], 'period':['วาระ','tenure','term of office'], 'notes':['หมายเหตุ','ข้อควรรู้','service notes'], 'source_summary':['ภาพรวมชุดปุ่ม','controls summary'], 'how_to_play':")
p.write_text(s,encoding='utf8')
p=H/'registry.py';s=p.read_text('utf8').replace("field=fields[key]; val=value(record,key)","field=fields.get(key,{'status':'unknown','value':None,'evidence_refs':[]}); val=value(record,key)");p.write_text(s,encoding='utf8')
# UI supports additive optional fields and older revision payloads without rewriting them.
p=H/'ui/owner.js';s=p.read_text('utf8')
s=s.replace("let unit=r.fields[f.key];", "let unit=r.fields[f.key]||{status:'unknown',value:null,evidence_refs:[],note:''};")
s=s.replace("let h=FIELD_HELP[r.kind][f.key];", "let h=FIELD_HELP[r.kind]?.[f.key]||{hint:f.meaning_th+' — กรอกเฉพาะที่มีหลักฐาน เว้นส่วนที่ไม่ทราบไว้',example:null};")
s=s.replace("OPTION_LABELS[v]||v", "(v==='unknown'?'ไม่ทราบ / ต้นฉบับไม่ระบุ':OPTION_LABELS[v]||v)")
p.write_text(s,encoding='utf8')
# Typed controls use the same source-preserving projection as migrated partial text.
p=H/'answer.py';s=p.read_text('utf8');old="out='\\n'.join('• '+text(b['action'],lang)+' → '+', '.join(b['buttons'])+' ('+b['gesture']+'; '+text(b['context'],lang)+')' for b in v)"
new="from .control_rows import render_bindings\n                        out=render_bindings(v,raw_query,lang)\n                        plan.setdefault('partial_controls',[]).append({'record_id':r['record_id'],'unknown_gesture_rows':sum(b['gesture']=='unknown' for b in v),'typed_source_rows':len(v)})"
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf8')
p=H/'query_scope.py';s=p.read_text('utf8').replace("occurrence=re.search(r'_section_(\\d+)$',r['record_id'])", "if value(r,'source_order') is not None:return ((0,value(r,'source_order')), )\n        occurrence=re.search(r'_section_(\\d+)$',r['record_id'])")
s=s.replace("if declared:supported=set(supported)|{declared}","if declared:supported=set(supported)|{declared}\n            supported=set(supported)|set(value(r,'facets') or [])")
p.write_text(s,encoding='utf8')
profiles=read(H/'answer_profiles.json')
for kind,fields in changes.items():
 for key,meaning,_ in fields:
  profiles.setdefault('labels',{}).setdefault(kind,{})[key]={'th':meaning,'en':key.replace('_',' ')}
write(H/'answer_profiles.json',profiles)
print('Additive format and reader extension written')
