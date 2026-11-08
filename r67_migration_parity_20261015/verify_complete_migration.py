"""Independent raw-row, provenance, revision and graph checks for final candidate."""
import collections,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,validate
store=CommonStore(B/'common.sqlite');old=CommonStore(B/'before.sqlite')
with store.connect() as c:
 rs=store.heads(c);srcs=store.sources(c);revs={tuple(r[:2]):tuple(r) for r in c.execute('select * from cc_revisions')};meta=dict(c.execute('select key,value from cc_meta'));approvals=c.execute('select count(*) from cc_approvals').fetchone()[0]
with old.connect() as c:
 old_rs=old.heads(c);old_srcs=old.sources(c);old_revs=[tuple(r) for r in c.execute('select * from cc_revisions')]
checks=[]
def check(label,ok,detail=None):checks.append({'check':label,'passed':bool(ok),'detail':detail})
check('original_heads_retained',set(old_rs)<=set(rs));check('original_revisions_unchanged',all(revs.get(tuple(r[:2]))==r for r in old_revs),len(old_revs));check('original_sources_unchanged',all(srcs.get(k)==v for k,v in old_srcs.items()),len(old_srcs));check('no_approvals',approvals==0);check('no_active_release',meta['active']=='')
errors={rid:err for rid,r in rs.items() if (err:=validate(r,rs,srcs))};check('schema_fk_source_integrity',not errors,errors)
raw=[json.loads(s) for s in (B/'source_snapshot/data/curated/game_control_facts.jsonl').read_text('utf-8-sig').splitlines() if s.strip()]
groups=json.loads((B/'RAW_RECOVERY.json').read_text('utf8'))['control_groups'];total=0;gaps=[]
for group in groups:
 r=rs[group['record_id']];items=[x for x in raw if x['game']==group['game'] and x['platform']==group['platform']];head=next(x for x in items if x['id'].startswith('game_control_summary_'));source_rows=[x for x in items if x.get('button')];rows=value(r,'bindings') or []
 check('control_row_count:'+r['record_id'],len(rows)==len(source_rows)==head['control_count'])
 if not source_rows:check('unavailable_not_fabricated:'+r['record_id'],value(r,'bindings') is None)
 for i,(a,x) in enumerate(zip(rows,source_rows)):
  total+=1
  check('button_label:'+x['id'],a['button_label']['th']==x['button'])
  check('button_array:'+x['id'],a['buttons']==(x.get('buttons') or [x['button']]))
  check('action:'+x['id'],a['action']['th']==x['action_th'])
  check('description:'+x['id'],(a['notes']['th'] or '')==x.get('description_th',''))
  check('section:'+x['id'],(a.get('section',{}).get('th') or '')==x.get('section',''))
  if a['notes'].get('th') and not a['notes'].get('en'):gaps.append({'record_id':r['record_id'],'row':i,'field':'notes'})
 if head.get('note'):check('warning_preserved:'+r['record_id'],head['note'] in (value(r,'verification_note') or {}).values())
 check('coverage_status:'+r['record_id'],value(r,'source_coverage')==head['coverage_status'])
lineage=json.loads((B/'RAW_RECOVERY_LINEAGE.json').read_text('utf8'));targets={x['locator']:x['record_id'] for x in lineage if x['field']=='official_description'}
descriptions=[json.loads(s) for s in (B/'source_snapshot/data/curated/our_games_scraped_details.jsonl').read_text('utf-8-sig').splitlines() if s.strip()]
for i,x in enumerate(descriptions):
 r=rs[targets['/'+str(i)]];v=value(r,'official_description');check('description_preserved:'+x['id'],x['summary_th'] in v.values());check('description_bilingual:'+x['id'],bool(v['th'] and v['en']))
 sections=x['listed_under'] if isinstance(x['listed_under'],list) else [x['listed_under']];check('listing_sections:'+x['id'],value(r,'source_listing_sections')==sections)
offered={value(r,'game_id') for r in rs.values() if r['kind']=='game_service' and value(r,'offered') is True};old_offered={value(r,'game_id') for r in old_rs.values() if r['kind']=='game_service' and value(r,'offered') is True}
check('offered_game_identity_set_unchanged',offered==old_offered,len(offered));check('no_missing_control_note_english',not gaps,gaps)
for item in json.loads((B/'FROZEN_CODE_MANIFEST_final05.json').read_text('utf8')):check('code_frozen:'+item['path'],hashlib.sha256((B/'system'/item['path']).read_bytes()).hexdigest()==item['sha256'])
result={'records':len(rs),'kinds':dict(collections.Counter(r['kind'] for r in rs.values())),'canonical_control_sets':38,'all_raw_control_groups':len(groups),'all_raw_control_rows':total,'original_control_facts_including_summaries':len(raw),'descriptions':len(descriptions),'original_heads':len(old_rs),'original_revisions':len(old_revs),'original_sources':len(old_srcs),'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x for x in checks if not x['passed']],'missing_control_note_english':gaps,'details':checks,'database_sha256':hashlib.sha256((B/'common.sqlite').read_bytes()).hexdigest()}
(B/'FINAL_MIGRATION_VERIFICATION_final05.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False))
