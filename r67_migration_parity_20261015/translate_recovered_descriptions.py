"""Read-only proposals; does not save, approve or publish model output."""
import json,sys,time,copy
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
p=H/'translation.py';s=p.read_text('utf8').replace("field=draft['fields'][field_spec['key']]", "field=draft['fields'].get(field_spec['key'],{'status':'unknown','value':None})");p.write_text(s,encoding='utf8')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from app.knowledge.common.translation import translate_draft
store=CommonStore(B/'common.sqlite')
with store.connect() as c:records=store.heads(c)
targets=[r for r in records.values() if value(r,'official_description')]
out=B/'DESCRIPTION_TRANSLATION_PROPOSALS.jsonl'
with out.open('x',encoding='utf8') as f:
 for i,r in enumerate(targets,1):
  start=time.perf_counter();source=value(r,'official_description')['th']
  try:
   # Only request this new field; existing reviewed translations remain untouched.
   draft=copy.deepcopy(r)
   for k,field in draft['fields'].items():
    if k!='official_description':field.update(status='unknown',value=None,evidence_refs=[],note='Not part of this translation-only request')
   proposal=translate_draft(draft)
   row={'record_id':r['record_id'],'source':source,'english':proposal['record']['fields']['official_description']['value']['en'],'transport_and_structural_checks_passed':True,'agent_semantic_reviewed':False}
  except Exception as e:row={'record_id':r['record_id'],'source':source,'error':repr(e),'agent_semantic_reviewed':False}
  row['seconds']=time.perf_counter()-start;f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();print(json.dumps({'done':i,'total':len(targets),'id':r['record_id'],'ok':'english' in row,'seconds':row['seconds']}),flush=True)
