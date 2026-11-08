"""Preserve original composite button labels; a list must not lose '/' meaning."""
import copy,hashlib,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
catalog=json.loads((H/'catalog.json').read_text('utf8'));entry=next(f for c in catalog if c['kind']=='control_set' for f in c['fields'] if f['key']=='bindings')
label=copy.deepcopy(entry['value_schema']['items']['properties']['action'])
entry['value_schema']['items']['properties']['button_label']=label
write(H/'catalog.json',catalog)
schema=json.loads((H/'schemas/control_set.schema.json').read_text('utf8'));schema['properties']['fields']['properties']['bindings']['oneOf'][0]['properties']['value']=entry['value_schema'];write(H/'schemas/control_set.schema.json',schema)
p=H/'control_rows.py';s=p.read_text('utf8').replace("parts=[', '.join(row['buttons'])", "parts=[local(row.get('button_label')) or ', '.join(row['buttons'])");p.write_text(s,encoding='utf8')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.registry import value,now
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
from migrate_ids import stable
store=CommonStore(B/'common.sqlite');saved=[]
for p in sorted((B/'source_snapshot/data/content').rglob('*.json')):
 x=json.loads(p.read_text('utf-8-sig'))
 if x.get('kind')!='control_map':continue
 rid=stable(x['content_id']);r=store.get(rid)['record'];rows=value(r,'bindings');th=x['locales']['th']['fields']['controls'];en=x['locales']['en']['fields'].get('controls',[])
 assert len(rows)==len(th)
 for i,row in enumerate(rows):row['button_label']={'th':th[i]['button'],'en':en[i]['button'] if i<len(en) else None}
 data={'bindings':rows,'original_field_evidence':r['fields']['bindings']['evidence_refs'],'source_path':p.relative_to(B/'source_snapshot').as_posix(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rule':'preserve original label verbatim; arrays remain separate; no simultaneity inferred'}
 raw=canonical_json(data);sid='r67_buttons_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r67/buttons/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['control_set'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r67-label-preservation')
 r['fields']['bindings']['evidence_refs']=[{'source_id':sid,'locator':'/bindings'}]
 saved.append(store.save(r,actor='r67-label-preservation',expected_version=r['revision'],change_note='Keep original composite button label alongside structured inputs'))
write(B/'BUTTON_LABEL_REPAIR.json',saved);print('Preserved labels in',len(saved),'control sets')
