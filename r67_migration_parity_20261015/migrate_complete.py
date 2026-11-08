"""Reconcile every canonical public-content field against the latest R66 draft.

All writes are additive revisions in this workspace. No approval or validity is
invented. The coverage ledger distinguishes read-ready facts from archived text.
"""
import copy,collections,hashlib,json,re,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.registry import value,now,validate,CATALOG,pointer
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
from app.pipeline.competition_source_facets import competition_source_facets

def dump(n,x):(B/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf8')
def stable(s):
 v=re.sub('[^a-z0-9_:-]','_',s.lower())
 return v if len(v)<=100 else v[:78]+'_'+hashlib.sha256(s.encode()).hexdigest()[:20]
def sid(s):return re.sub('[^a-z0-9_]+','_',s.lower()).strip('_')
def loc(th,en=None):return {'th':th or None,'en':en or None}
store=CommonStore(B/'common.sqlite')
with store.connect() as c:before=store.heads(c);original_sources=store.sources(c);original_revisions=[tuple(r) for r in c.execute('select * from cc_revisions')];active=dict(c.execute('select key,value from cc_meta')).get('active');approvals=c.execute('select count(*) from cc_approvals').fetchone()[0]
records=copy.deepcopy(before);lineage=[];unresolved=[];changed=set()
sources={};canonical=[]
for p in sorted((B/'source_snapshot/data/content').rglob('*.json')):
 if any(x in p.relative_to(B/'source_snapshot/data/content').parts for x in ('schema','review','projections','releases')):continue
 x=json.loads(p.read_text('utf-8-sig'))
 if 'content_id' in x:canonical.append((p.relative_to(B/'source_snapshot').as_posix(),x))

def put(rid,key,v,rel,locator,rule='exact source copy'):
 if v is None or v=='' or isinstance(v,dict) and set(v)=={'th','en'} and not any(v.values()):return
 r=records[rid]
 if key not in r['fields']:r['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':'Additive optional field'}
 old=value(r,key)
 if old==v:return
 # Existing confirmed values are never overwritten by an optional migration.
 if old is not None:
  unresolved.append({'record_id':rid,'field':key,'reason':'existing_value_differs_preserved','incoming':v,'current':old});return
 source=json.loads((B/'source_snapshot'/rel).read_text('utf-8-sig'))
 r['fields'][key]={'status':'known','value':v,'evidence_refs':[],'note':'R67 source-derived draft: '+rule}
 lineage.append({'record_id':rid,'field':key,'source_path':rel,'source_sha256':hashlib.sha256((B/'source_snapshot'/rel).read_bytes()).hexdigest(),'locator':locator,'source_value':pointer(source,locator),'mapped_value':v,'transform':rule})
 changed.add(rid)

notes_en={
 'availability_cockpit_01_02':'There are 2 Cockpit stations, and both have the same game list.',
 'availability_nintendo_1_2':'The Nintendo Switch 1–2 Persons and 1–4 Persons options have the same game list.',
 'availability_nintendo_1_4':'The Nintendo Switch 1–2 Persons and 1–4 Persons options have the same game list.',
 'availability_pc_01_02':'PC #01–#02 have TEKKEN 8 but do not have Call of Duty: Warzone.\nPC #01–#02 and PC #03–#10 share Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, and VALORANT.',
 'availability_pc_03_10':'PC #03–#10 have Call of Duty: Warzone but do not have TEKKEN 8.\nPC #01–#02 and PC #03–#10 share Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, and VALORANT.',
 'availability_ps5_01_02':'PlayStation 5 #01 and #02 have the same game list.',
 'availability_vr_30':'The VR Station 30-minute and 1-hour options have the same game list.',
 'availability_vr_60':'The VR Station 30-minute and 1-hour options have the same game list.'}
aff_en={
 'มหาวิทยาลัยสงขลานครินทร์':'Prince of Songkla University',
 'มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต':'Prince of Songkla University, Phuket Campus',
 'วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต':'College of Computing, Prince of Songkla University, Phuket Campus',
 'PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต':'PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus',
 'วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง':'IoT and Information Systems Engineering, King Mongkut’s Institute of Technology Ladkrabang'}
row_count=0
for rel,x in canonical:
 k=x['kind'];rid=stable(x['content_id']);th=x['locales']['th']['fields'];en=x['locales']['en']['fields'];f=x['facts']
 if k=='member':
  if th.get('affiliation'):
   a=th['affiliation'];put(rid,'affiliation',loc(a,en.get('affiliation') or aff_en.get(a) or (a if a.isascii() else None)),rel,'/locales/th/fields/affiliation','exact TH; source-bound agent English draft, not official-name approval')
  if f.get('period'):put(rid,'period',loc(f['period'],f['period']),rel,'/facts/period','literal historical period; not current appointment guarantee')
 elif k=='service_availability':
  put(rid,'notes',loc('\n'.join(th.get('notes',[])),notes_en.get(x['content_id'])),rel,'/locales/th/fields/notes','join all note rows; reviewed source-bound agent English draft')
 elif k=='control_map':
  put(rid,'source_summary',loc(th.get('summary'),en.get('summary') or f"{f['game']} on {f['platform']}: {len(th['controls'])} control entries are recorded."),rel,'/locales/th/fields/summary','source summary and literal game/platform/row-count English rendering')
  rows=[];old=value(records[rid],'limitations') or {};english=(old.get('en') or '').splitlines()
  raw=th['controls'];aligned=len(english)==len(raw) and all(a.get('button','').strip()==b.split(' | ')[0].strip() for a,b in zip(raw,english))
  if not aligned:
   unresolved.append({'record_id':rid,'field':'bindings','reason':'parallel_table_alignment_failed; raw rows retained; no row guessed'});continue
  for i,a in enumerate(raw):
   pieces=english[i].split(' | ');original_en=en.get('controls',[]);e=original_en[i] if i<len(original_en) else {}
   buttons=a.get('buttons') or [a['button']]
   rows.append({'buttons':list(dict.fromkeys(buttons)),'gesture':'unknown','action':loc(a.get('action_th'),pieces[1] if len(pieces)>1 else e.get('action')),'context':loc(None),'notes':loc(a.get('description_th'),pieces[2] if len(pieces)>2 else e.get('description')),'section':loc(a.get('section'),pieces[3] if len(pieces)>3 else e.get('section')),'source_order':i+1})
  put(rid,'bindings',rows,rel,'/locales','structured original rows + button-aligned reviewed R66 English; gesture/context unspecified, no inferred key presses');row_count+=len(rows)
 elif k=='competition_document':
  put(rid,'source_title',loc(th.get('title'),en.get('title')),rel,'/locales/th/fields/title')
  for i,a in enumerate(th['sections']):
   rr=stable(x['content_id']+'_section_'+str(i+1).zfill(3))
   put(rr,'source_order',i+1,rel,'/locales/th/fields/sections/'+str(i),'occurrence order; does not invent a rule number')
   facets=sorted(competition_source_facets(a))
   if facets:put(rr,'facets',facets,rel,'/locales/th/fields/sections/'+str(i),'derived multi-topic search metadata; not a new rule or factual approval')

# Save new fields with immutable source snapshots and exact transformation lineage.
for rid in sorted(changed):
 rows=[r for r in lineage if r['record_id']==rid]
 payload={'mapped_fields':{r['field']:r['mapped_value'] for r in rows},'field_lineage':rows,'status':'draft_only_not_owner_approved'}
 raw=canonical_json(payload);source_id='r67_'+hashlib.sha256((rid+raw).encode()).hexdigest()[:28]
 src={'source_id':source_id,'kind':'derived_curated','path':'migration://r67/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[records[rid]['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 store.add_source(src,raw,actor='r67-source-reconciliation')
 for row in rows:records[rid]['fields'][row['field']]['evidence_refs']=[{'source_id':source_id,'locator':'/mapped_fields/'+row['field']}]
 records[rid]['localization']['en_status']='agent_translated'
 store.save(records[rid],expected_version=before[rid]['revision'],actor='r67-source-reconciliation',change_note='Preserve missing original fields and structured partial facts; no approval or validity change')
with store.connect() as c:
 after=store.heads(c);srcs=store.sources(c)
 errors={rid:validate(r,after,srcs) for rid,r in after.items() if validate(r,after,srcs)}
 assert not errors,errors
 assert c.execute('select count(*) from cc_approvals').fetchone()[0]==approvals
 assert dict(c.execute('select key,value from cc_meta')).get('active')==active
 for row in original_revisions:assert tuple(c.execute('select * from cc_revisions where record_id=? and version=?',row[:2]).fetchone())==row
 for key,pair in original_sources.items():assert srcs[key]==pair
dump('MIGRATION_LINEAGE.json',lineage);dump('UNRESOLVED_MIGRATION.json',unresolved)
dump('MIGRATION_RESULT.json',{'canonical_sources':len(canonical),'original_records':len(before),'result_records':len(after),'changed_records':len(changed),'added_fields':len(lineage),'structured_control_rows':row_count,'schema_validation_errors':errors,'original_revisions_preserved':len(original_revisions),'original_sources_preserved':len(original_sources),'new_approvals':0,'active_release_unchanged':True,'unresolved':unresolved})
print((B/'MIGRATION_RESULT.json').read_text('utf8'))
