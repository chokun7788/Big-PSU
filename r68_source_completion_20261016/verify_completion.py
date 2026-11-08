import collections,hashlib,json,re,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,validate,pointer
from app.knowledge.common.answer import named,title
from app.knowledge.common.query_contract import live_request
db=B/(sys.argv[1] if len(sys.argv)>1 else 'candidate04.sqlite');tag=sys.argv[2] if len(sys.argv)>2 else 'initial'
store=CommonStore(db);old=CommonStore(B/'before.sqlite')
with store.connect() as c:rs=store.heads(c);sources=store.sources(c);meta=dict(c.execute('select key,value from cc_meta'));approvals=c.execute('select count(*) from cc_approvals').fetchone()[0];releases=c.execute('select count(*) from cc_releases').fetchone()[0]
with old.connect() as c:prev=old.heads(c);previous_sources=old.sources(c);oldrows=[tuple(r) for r in c.execute('select * from cc_revisions')]
checks=[]
def check(label,ok,detail=None):checks.append({'check':label,'passed':bool(ok),'detail':detail})
def raw(rel):
 p=B/'source_snapshot'/rel
 return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()] if p.suffix=='.jsonl' else json.loads(p.read_text('utf-8-sig')) if p.suffix=='.json' else {'text':p.read_text('utf-8-sig')}
check('all_schema_and_semantic_checks',not {rid:validate(r,rs,sources) for rid,r in rs.items() if validate(r,rs,sources)})
with store.connect() as c:
 for row in oldrows:check('immutable_revision:'+row[0]+':'+str(row[1]),tuple(c.execute('select * from cc_revisions where record_id=? and version=?',row[:2]).fetchone())==row)
for sid,pair in previous_sources.items():check('immutable_source:'+sid,sources.get(sid)==pair)
for x in json.loads((B/('MIGRATION_LINEAGE_final.json' if (B/'MIGRATION_LINEAGE_final.json').exists() else 'MIGRATION_LINEAGE.json')).read_text('utf8')):
 p=B/'source_snapshot'/x['source_path'];check('source_field:'+x['record_id']+':'+x['field'],hashlib.sha256(p.read_bytes()).hexdigest()==x['source_sha256'] and pointer(raw(x['source_path']),x['locator'])==x['source_value'] and value(rs[x['record_id']],x['field'])==x['mapped_value'])
for x in raw('data/sources/our_games_raw.jsonl'):
 normalize=lambda s:re.sub(r'[^\w]','',s.casefold())
 r=next(r for r in rs.values() if r['kind']=='game' and normalize(x['game']) in [normalize(v) for v in (value(r,'title') or {}).values() if v])
 language='th' if re.search('[\u0e00-\u0e7f]',x['description']) else 'en';check('raw_full_text:'+x['id'],value(r,'official_description')[language]==x['description'])
def offers(records):return sorted((r['record_id'],value(r,'game_id'),value(r,'service_id'),value(r,'offered'),value(r,'installed_resource_ids')) for r in records.values() if r['kind']=='game_service')
check('game_service_relations_unchanged',offers(rs)==offers(prev))
check('offered_game_ids_unchanged',{value(r,'game_id') for r in rs.values() if r['kind']=='game_service' and value(r,'offered')}=={value(r,'game_id') for r in prev.values() if r['kind']=='game_service' and value(r,'offered')})
for rid,r in prev.items():
 if r['kind'] in {'rate','rental_package','schedule','closure','resource','control_set','person','policy'}:
  for field,f in r['fields'].items():check('protected_fact:'+rid+':'+field,rs[rid]['fields'].get(field)==f)
 for k in ['validity','review','lifecycle']:check('protected_state:'+rid+':'+k,r[k]==rs[rid][k])
check('no_approval_or_release',approvals==0 and releases==0 and meta.get('active')=='')
for q,expect in [('Change a wrongly booked machine steps',False),('How do I change an incorrectly booked machine?',False),('Change a wrongly booked machine. Is PC1 booked at 15:00?',True),('Is PC1 booked at 15:00?',True),('ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง',True),('Is PC1 available now?',True),('Can I play free of charge?',False)]:check('live_scope:'+q,live_request(q)==expect)
def names(records):return {rid:list(dict.fromkeys(r['aliases']['th']+r['aliases']['en']+list((value(r,'title') or {}).values()))) for rid,r in records.items() if r['kind']=='game'}
ns=names(rs);oldns=names(prev);alias_results=[]
for x in json.loads((B/'ALIAS_LINEAGE.json').read_text('utf8')):
 ids,method=named(x['alias'],ns,allow_fuzzy=False);ok=set(ids)=={x['record_id']};alias_results.append({**x,'selected_ids':ids,'passed':ok});check('alias_identity:'+x['alias'],ok)
negative=[]
for q in ['TEKKEN 7','เทคเคน7','Counter-Strike 3','CS3','Mario Kart 9','มาริโอ้คาร์ท9','Overcooked! 3','Resident Evil 5','Resident Evil 6','The Last of Us Part III','FIFA 23','EA Sports FC 25','God of War 3','FINAL FANTASY XV','Animal Crossing Pocket Camp','PUBG Mobile','VALORANT Mobile','Monster Hunter World','Luigi Mansion 2']:
 ids,_=named(q,ns,allow_fuzzy=False);before_ids,_=named(q,oldns,allow_fuzzy=False)
 negative.append({'query':q,'before':before_ids,'after':ids,'new_matches':sorted(set(ids)-set(before_ids))})
# Full source manifest remains exactly as observed in the real project.
root=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
source_changes=[]
for x in json.loads((B/'SOURCE_MANIFEST.json').read_text('utf8')):
 p=root/x['path'];ok=p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'];check('actual_source:'+x['path'],ok)
 if not ok:source_changes.append(x['path'])
(B/('ALIAS_IDENTITY_'+tag+'.json')).write_text(json.dumps(alias_results,ensure_ascii=False,indent=2),encoding='utf8')
(B/('NEGATIVE_EDITION_PROBES_'+tag+'.json')).write_text(json.dumps(negative,ensure_ascii=False,indent=2),encoding='utf8')
out={'checks':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x for x in checks if not x['passed']],'old_revisions':len(oldrows),'old_sources':len(previous_sources),'heads':len(rs),'counts_by_kind':dict(collections.Counter(r['kind'] for r in rs.values())),'offered_unique_games':len({value(r,'game_id') for r in rs.values() if r['kind']=='game_service' and value(r,'offered')}),'approvals':approvals,'active':meta.get('active'),'source_files_changed':source_changes,'negative_probe_new_matches':[x for x in negative if x['new_matches']],'details':checks}
(B/('VERIFICATION_'+tag+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k!='details'},ensure_ascii=False,indent=2))
