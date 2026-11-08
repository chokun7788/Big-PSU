"""Read existing comparison evidence. Does not execute chatbot or model tests."""
import hashlib,json,sqlite3,zlib
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent;S=R/'r78_web_session_check_20261016/system'
db=R/'r65_detailed_failure_analysis_20261014/evidence.sqlite'
c=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
keys=[
 ('rules_overview','c3d18fcf8bfd49617031552acce0ce34c758229e4ab9cb022eda66fcb32e3922'),
 ('rules_dispute','b5f7868f6c248900a96caef02c4d9798948aef63ff0b2acc9e40150f24699fef'),
 ('controls','409b95184862113c90e7e99bff4584d634e275bcf2af848c9f6397dd7acfacb7'),
 ('fee_target','50b511eb7bab6b00caadaa326829717c36afeecf5d08f8f789a1d8cbb41c746b'),
 ('fee_validity','dbda06de43cf51b76a922aaa1ee2e86deb601ee1bd51f804b0eee0435b0a564d'),
 ('booking','591b2bee8f8b4c67f3e37efc6742a2bed443d924b362d59d8d1a77d4aea4b547'),
 ('game_description','6e1b7e05542fce698ea7aad0dd226b48e5818b3f59ac4033f7fc6b620a9d3194'),
 ('equipment','5b886d61edcf917718ab054c81ebe0deac13ef1576075e8a9fc7f703cd5081d4'),
 ('equipment_list','9201b84e6f1696f544c0e08172c6a0ebce88d3dfa5164cf8c33d2c47442443e7'),
 ('schedule','dd0f2ba1cef6d36751c223437bea240599d44985c42d352d9ec7d90012908314')]
output=[]
for label,key in keys:
 pair={'label':label,'key':key,'historical_run':'R64; not current R84 test'}
 for arm in ['legacy_llm','common_llm']:
  row=c.execute('select * from results where arm=? and key=?',(arm,key)).fetchone()
  raw=json.loads(zlib.decompress(row['raw']));r=raw['result'];art=r.get('decision_artifact') or {}
  grades=[dict(g) for g in c.execute('select file,rownum,variant,passed,content_asserted,content_passed,reasons_json from grades where arm=? and key=?',(arm,key))]
  pair['question']=row['question'];pair['locale']=row['locale']
  pair[arm]={'mode':row['mode'],'route':r.get('route'),'answer':row['answer'],'answer_characters':len(row['answer']),'validation':r.get('validation'),
             'artifact':art,'trace':r.get('trace'),'hits':r.get('hits'),'grades':grades,'source_file':row['source_file'],'source_line':row['source_line']}
 output.append(pair)
 print(json.dumps({'case':label,'q':pair['question'],'old':pair['legacy_llm']['answer'][:650],'common':pair['common_llm']['answer'][:650],'common_plan':pair['common_llm']['artifact'].get('query_plan',{})},ensure_ascii=False)[:2300])
c.close()
with (B/'PAIRED_CASE_EVIDENCE.json').open('x',encoding='utf8') as f:json.dump(output,f,ensure_ascii=False,indent=2)
p=S/'data/knowledge/common.sqlite';c=sqlite3.connect(p.resolve().as_uri()+'?mode=ro',uri=True)
records=[json.loads(x[0]) for x in c.execute('select r.payload from cc_revisions r join cc_heads h on r.record_id=h.record_id and r.version=h.head where h.withdrawn=0')]
summary={'current_database_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'records':len(records),'kinds':{},'profiles':[], 'controls':{},'rule_facets':{},'rate_validity':{},'localized_english_missing':[]}
for r in records:
 k=r['kind'];summary['kinds'][k]=summary['kinds'].get(k,0)+1
 if (r['fields'].get('query_profile') or {}).get('status')=='known':summary['profiles'].append({'record_id':r['record_id'],'profile':r['fields']['query_profile']['value']})
 if k=='control_set':
  f=r['fields'].get('bindings',{});v=f.get('value');summary['controls'][r['record_id']]={'status':f.get('status'),'binding_count':len(v) if isinstance(v,list) else None}
 if k=='competition_rule':
  f=r['fields'].get('facet',{});s=f.get('status');summary['rule_facets'][s]=summary['rule_facets'].get(s,0)+1
 if k=='rate':
  s=json.dumps(r.get('validity'),sort_keys=True);summary['rate_validity'][s]=summary['rate_validity'].get(s,0)+1
 for field,envelope in r['fields'].items():
  val=envelope.get('value')
  if envelope.get('status')=='known' and isinstance(val,dict) and 'th' in val and not val.get('en'):summary['localized_english_missing'].append(r['record_id']+':'+field)
c.close()
with (B/'CURRENT_DATA_AUDIT.json').open('x',encoding='utf8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps({'records':summary['records'],'profiles':len(summary['profiles']),'controls':len(summary['controls']),'bindings':sum(v['binding_count'] or 0 for v in summary['controls'].values()),'facets':summary['rule_facets'],'top_level_localized_english_missing':len(summary['localized_english_missing'])},ensure_ascii=False))
