import json
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
for name in ['catalog.json','schemas/control_set.schema.json']:
 p=H/name;x=json.loads(p.read_text('utf8'))
 enum=next(f for c in x if c['kind']=='control_set' for f in c['fields'] if f['key']=='bindings')['value_schema']['items']['properties']['gesture']['enum'] if isinstance(x,list) else x['properties']['fields']['properties']['bindings']['oneOf'][0]['properties']['value']['items']['properties']['gesture']['enum']
 enum.remove('unknown');enum.insert(0,'unknown');p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
p=H/'answer.py';s=p.read_text('utf8')
needle="        return self.finish(snap,started,'\\n\\n'.join(blocks),hits,plan,obligations)"
new="""        # A consumption-area rule does not prove permission for every food origin.
        if any('food' in str(value(records[rid],'intent_key') or '') for rid in ids) and re.search(r'ข้างนอก|ภายนอก|\\boutside\\b',normal(raw_query)):
            source_body=' '.join(text(value(records[rid],'answer') or {},lang) for rid in ids)
            if not re.search(r'ข้างนอก|ภายนอก|\\boutside\\b',normal(source_body)):
                blocks.append('ข้อมูลที่มีระบุพื้นที่รับประทานอาหารและเครื่องดื่ม แต่ยังไม่ได้ระบุแยกว่าการนำอาหารจากภายนอกเข้ามามีเงื่อนไขเพิ่มเติมหรือไม่' if lang=='th' else 'The source specifies where food and drinks may be consumed. It does not separately confirm whether bringing outside food has additional conditions.')
                plan['uncovered_source_scope']='outside_food_conditions'
        return self.finish(snap,started,'\\n\\n'.join(blocks),hits,plan,obligations)"""
assert needle in s;s=s.replace(needle,new)
s=s.replace("        if response=='answer':\n", "        if response=='answer':\n            if plan.get('uncovered_source_scope'):errors.append('uncovered_source_scope:'+plan['uncovered_source_scope'])\n",1)
p.write_text(s,encoding='utf8')
# Update stale prototype-only descriptions; schema version remains compatible.
for p in (H/'schemas').glob('*.schema.json'):
 x=json.loads(p.read_text('utf8'))
 if x.get('description')=='Research prototype; not loadable by current application.':x['description']='Common content schema loaded by the registry; publication requires source, validity and review checks.'
 if isinstance(x.get('title'),str):x['title']=x['title'].replace(' — research design','')
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Source coverage boundary and safe control defaults updated')
