"""Inventory both typed-engine claims and native compatibility fields, read-only."""
import json
import sqlite3
from pathlib import Path

P=Path(__file__).resolve().parent
E=P.parent/'r135_bounded_eval200_20261111/evaluation'
db=sqlite3.connect((E/'runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
source=sqlite3.connect((E.parent/'system/data/knowledge/evaluation_frozen.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(payload) for rid,payload in source.execute('SELECT r.record_id,r.payload FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}

def observed(artifact,locale):
 claims=artifact.get('domain_flow',{}).get('typed_claims',[])
 if claims:return claims
 out=[]
 for obligation in artifact.get('obligations',[]):
  record=records.get(obligation.get('record_id'),{})
  field=record.get('fields',{}).get(obligation.get('field'),{})
  if obligation.get('status')!='known' or field.get('status')!='known':continue
  value=field.get('value')
  if isinstance(value,dict):value=value.get(locale) or value.get('th') or value.get('en')
  if not isinstance(value,str):continue
  out.append({'record_id':obligation['record_id'],'facet':obligation['field'],'value':value,'native_field':True})
 return out

def build():
 groups={}
 for row in map(json.loads,(E/'RESULTS.jsonl').open(encoding='utf-8')):
  message=db.execute('SELECT metadata_json FROM chat_messages WHERE session_id=? AND role=? ORDER BY id DESC LIMIT 1',(row['session_id'],'assistant')).fetchone()
  artifact=json.loads(message[0]).get('decision_artifact',{}) if message else {}
  for claim in observed(artifact,row.get('locale','th')):
   key=(claim['record_id'],claim['facet'])
   g=groups.setdefault(key,{'record_id':key[0],'field':key[1],'value':claim['value'],'values':[],'count':0})
   g['count']+=1
   if claim['value'] not in g['values']:g['values'].append(claim['value'])
 (P/'EVAL200_CLAIM_INVENTORY.json').write_text(json.dumps(list(groups.values()),ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'unique_record_fields':len(groups)}))

if __name__=='__main__':build()
