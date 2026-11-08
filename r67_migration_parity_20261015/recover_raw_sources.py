"""Recover business data omitted before canonical export (31 descriptions, 21 rows).

Only exact source identities or exact row correspondence establish links.
Descriptive profiles never create venue offerings, machines, prices or bookings.
"""
import collections,copy,hashlib,json,re,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
catalog=json.loads((H/'catalog.json').read_text('utf8'));by={x['kind']:x for x in catalog}
local=copy.deepcopy(next(f['value_schema'] for f in by['game']['fields'] if f['key']=='summary'))
for kind,fields in {
 'game':[('official_description','คำบรรยายจากหน้าเกมต้นฉบับ',local),('profile_role','บทบาทของรายการข้อมูล (ไม่ใช่สถานะให้บริการ)',{'type':'string','enum':['game','source_listing']})],
 'control_set':[('verification_note','ข้อจำกัดการตรวจชุดปุ่มจากต้นฉบับ',local),('source_coverage','สถานะความครบของผังปุ่มตามต้นฉบับ',{'type':'string','minLength':1})]
}.items():
 schema=json.loads((H/'schemas'/f'{kind}.schema.json').read_text('utf8'));t=json.loads((H/'templates'/f'{kind}.draft.json').read_text('utf8'));base=copy.deepcopy(next(iter(schema['properties']['fields']['properties'].values())))
 for key,meaning,vs in fields:
  by[kind]['fields'].append({'key':key,'meaning_th':meaning,'publish_core':False,'reference_kind':None,'value_schema':vs});slot=copy.deepcopy(base);slot['description']=meaning;slot['oneOf'][0]['properties']['value']=vs;schema['properties']['fields']['properties'][key]=slot
  t['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่มีข้อมูลยืนยันสำหรับช่องนี้'}
 write(H/'schemas'/f'{kind}.schema.json',schema);write(H/'templates'/f'{kind}.draft.json',t)
write(H/'catalog.json',catalog)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,template,now
from app.knowledge.common.query_scope import same_platform
from app.knowledge.records import canonical_json
from migrate_ids import stable
store=CommonStore(B/'common.sqlite')
with store.connect() as c:rs=store.heads(c)
before=copy.deepcopy(rs);changes=collections.defaultdict(dict);lineage=[];unresolved=[]
def n(s):return re.sub(r'[^\w]','',str(s).casefold())
def game_id(name):
 exact=[r['record_id'] for r in rs.values() if r['kind']=='game' and n(name) in [n(s) for s in (value(r,'title') or {}).values() if s]]
 alias=[r['record_id'] for r in rs.values() if r['kind']=='game' and n(name) in [n(s) for s in r['aliases']['th']+r['aliases']['en']]]
 ids=exact or alias
 return ids[0] if len(ids)==1 else None
def put(rid,key,v,rel,index,rule):
 changes[rid][key]=v;lineage.append({'record_id':rid,'field':key,'source_path':rel,'source_sha256':hashlib.sha256((B/'source_snapshot'/rel).read_bytes()).hexdigest(),'locator':'/'+str(index),'transform':rule,'mapped_value':v})
rel='data/curated/our_games_scraped_details.jsonl';descriptions=[json.loads(s) for s in (B/'source_snapshot'/rel).read_text('utf-8-sig').splitlines() if s.strip()]
for i,x in enumerate(descriptions):
 rid=game_id(x['game'])
 if rid is None:
  rid=stable('source_listing_'+x['id']);rs[rid]=template('game');rs[rid]['record_id']=rid
  put(rid,'title',{'th':x['game'],'en':x['game']},rel,i,'exact source listing title; not a new venue offering')
  put(rid,'profile_role','source_listing',rel,i,'reference-only source entry; no game_service created')
 put(rid,'official_description',{'th':x['summary_th'],'en':None},rel,i,'complete literal scraped description including original ellipsis; not replacing curated summary; English pending')
 # Full listing label is searchable; broad aliases are not added to other editions.
 if x['game'] not in rs[rid]['aliases']['en']:rs[rid]['aliases']['en'].append(x['game'])

rel='data/curated/game_control_facts.jsonl';raw=[json.loads(s) for s in (B/'source_snapshot'/rel).read_text('utf-8-sig').splitlines() if s.strip()];groups=collections.defaultdict(list)
for i,x in enumerate(raw):groups[(x['game'],x['platform'])].append((i,x))
new_rows=0;control_groups=[]
for (name,platform),items in groups.items():
 summary=next((pair for pair in items if pair[1]['id'].startswith('game_control_summary_')),None);buttons=[pair for pair in items if pair[1].get('button')]
 if not summary:unresolved.append({'game':name,'reason':'missing_summary'});continue
 ix,head=summary;gid=game_id(name)
 candidates=[]
 for rid,r in rs.items():
  if r['kind']!='control_set' or not same_platform(value(r,'platform'),platform):continue
  existing=value(r,'bindings') or []
  if len(existing)==len(buttons) and existing and all(a['action'].get('th')==b.get('action_th') and (a.get('button_label') or {}).get('th')==b['button'] for a,(_,b) in zip(existing,buttons)):candidates.append(rid)
 if len(candidates)==1:rid=candidates[0]
 elif not candidates and gid:
  rid=stable('recovered_controls_'+head['id'].removeprefix('game_control_summary_'));rs[rid]=template('control_set');rs[rid]['record_id']=rid
  put(rid,'game_id',gid,rel,ix,'unique exact title/alias match to existing game; no installation claim')
  put(rid,'platform',platform,rel,ix,'literal platform label')
  rs[rid]['aliases']['en']=[name]
  rows=[]
  for j,(_,x) in enumerate(buttons):
   rows.append({'buttons':x.get('buttons') or [x['button']],'button_label':{'th':x['button'],'en':x['button']},'gesture':'unknown','action':{'th':x['action_th'],'en':x.get('action_en')},'context':{'th':None,'en':None},'notes':{'th':x.get('description_th') or None,'en':None},'section':{'th':x.get('section') or None,'en':None},'source_order':j+1})
  if rows:put(rid,'bindings',rows,rel,ix,'all literal rows in source group; notes English pending; gesture/context unspecified');new_rows+=len(rows)
  else:rs[rid]['fields']['bindings']['note']='Source explicitly reports no verified mapping; not a claim that the game has no controls'
  put(rid,'source_summary',{'th':head['text'].split('\nหมายเหตุ:')[0],'en':f'{name} on {platform}: {len(buttons)} control entries are recorded.'},rel,ix,'literal summary; recorded count is not a claim of source completeness')
 else:unresolved.append({'game':name,'platform':platform,'reason':'ambiguous_control_identity','candidates':candidates,'game_id':gid});continue
 if head.get('note'):put(rid,'verification_note',{'th':None,'en':head['note']},rel,ix,'preserve original source warning, not an agent or owner verification')
 put(rid,'source_coverage',head['coverage_status'],rel,ix,'literal original coverage status')
 control_groups.append({'game':name,'platform':platform,'record_id':rid,'source_rows':len(buttons),'summary_index':ix})

if unresolved:write(B/'RAW_RECOVERY_UNRESOLVED.json',unresolved);raise RuntimeError(unresolved)
for rid,fields in changes.items():
 rows=[x for x in lineage if x['record_id']==rid];raw=canonical_json({'mapped_fields':fields,'field_lineage':rows,'status':'draft_only; original coverage restrictions retained'})
 source_id='r67_raw_'+hashlib.sha256((rid+raw).encode()).hexdigest()[:26]
 store.add_source({'source_id':source_id,'kind':'derived_curated','path':'migration://r67/raw/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[rs[rid]['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r67-raw-source-recovery')
 for key,v in fields.items():rs[rid]['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':source_id,'locator':'/mapped_fields/'+key}],'note':'Source-derived draft; see immutable original JSONL lineage'}
 rs[rid]['localization']['en_status']='agent_translated'
 store.save(rs[rid],expected_version=before[rid]['revision'] if rid in before else 0,actor='r67-raw-source-recovery',change_note='Recover omitted raw source material and retain original verification restrictions')
write(B/'RAW_RECOVERY_LINEAGE.json',lineage)
write(B/'RAW_RECOVERY.json',{'scraped_descriptions':len(descriptions),'control_groups':control_groups,'new_control_rows':new_rows,'new_records':len(set(rs)-set(before)),'new_record_ids':sorted(set(rs)-set(before)),'unresolved':unresolved})
print(json.dumps({'descriptions':len(descriptions),'control_groups':len(control_groups),'new_rows':new_rows,'new_records':len(set(rs)-set(before))}))
# Source meaning is shared across existing and future records.
p=H/'query_contract.py';s=p.read_text('utf8').replace("CUES={'affiliation':", "CUES={'official_description':['คำบรรยายต้นฉบับ','คำบรรยายจากหน้าเกม','official description','source description'], 'verification_note':['ข้อจำกัดการตรวจ','verification note'], 'source_coverage':['ความครบของผังปุ่ม','control coverage'], 'affiliation':");p.write_text(s,encoding='utf8')
profiles=json.loads((H/'answer_profiles.json').read_text('utf8'))
profiles['kinds'].setdefault('control_set',{}).setdefault('context',[]).append({'when':['bindings'],'include':['verification_note','source_coverage']})
write(H/'answer_profiles.json',profiles)
p=H/'answer.py';s=p.read_text('utf8');needle="                    refs=f['evidence_refs'];labels=[]"
new="""                    if isinstance(v,dict) and set(v)=={'th','en'} and not v.get(lang) and v.get('th' if lang=='en' else 'en'):
                        out=('[Translation pending; Thai source] ' if lang=='en' else '[รอแปล; ต้นฉบับภาษาอังกฤษ] ')+out
                        plan.setdefault('localization_gaps',[]).append({'record_id':r['record_id'],'field':key,'target_language':lang})
                        plan.setdefault('scope_limits',[]).append({'requested':key,'reason':'translation_pending'})
                    refs=f['evidence_refs'];labels=[]"""
assert needle in s;s=s.replace(needle,new);p.write_text(s,encoding='utf8')
