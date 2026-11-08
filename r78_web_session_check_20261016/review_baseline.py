"""Regrade saved responses only; no requests or overwritten logs."""
import json,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
db=B/'system/data/knowledge/common.sqlite'
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as c:kinds=dict(c.execute('select record_id,kind from cc_heads'))
rows=[]
for line in (B/'baseline02/TURNS.jsonl').read_text(encoding='utf8').splitlines():
 r=json.loads(line);p=(r['response'].get('decision_artifact') or {}).get('query_plan') or {};ids=set(p.get('record_ids',[]))|{x['record_id'] for x in p.get('response_projection',[]) if x.get('fields')};errors=list(r['errors']);a=r['response'].get('answer','')
 if 'missing_personal_rule' in errors and 'migrated_owner_claim_personal_keyboard_mouse' in ids and any(x in a for x in ['ไม่อนุญาต','not allowed']):errors.remove('missing_personal_rule')
 if 'missing_pc_rate' in errors and any(kinds.get(i)=='rate' for i in ids) and 'PC' in a:errors.remove('missing_pc_rate')
 rows.append({'case':r['case'],'turn':r['turn'],'question':r['question'],'raw_errors':r['errors'],'reviewed_errors':errors,'passed':not errors,'protocol_mismatch_removed':len(r['errors'])-len(errors)})
result={'method':'Saved baseline regraded against common query_plan record_ids and response_projection; API exposes sources, not internal PipelineAnswer.hits. No model/dispatcher rerun.','count':len(rows),'passed':sum(x['passed'] for x in rows),'protocol_mismatches':sum(x['protocol_mismatch_removed'] for x in rows),'checks':rows}
with (B/'BASELINE_ORACLE_REVIEW.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
