"""Append evidence-backed corrections in R66's separate draft DB only."""
import sys,json,copy,hashlib
from pathlib import Path
from datetime import date,timedelta
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.records import canonical_json
s=CommonStore(B/'common.sqlite')
with s.connect() as c:records=s.heads(c);before_meta=dict(c.execute('SELECT * FROM cc_meta'))
changes=[];audit=[]
canonical={}
for p in (B/'system/data/content').rglob('*.json'):
 try:r=json.loads(p.read_text(encoding='utf-8-sig'))
 except (ValueError,OSError):continue
 if isinstance(r,dict) and r.get('content_id'):canonical[r['content_id']]=(p,r)
for rid,old in records.items():
 r=copy.deepcopy(old);changed={};lineage=[]
 def set_field(key,v,basis):
  if r['fields'][key]['status']=='known' and r['fields'][key]['value']==v:return
  r['fields'][key]={'status':'known','value':v,'note':'R66 derived mapping; draft only; '+basis,'evidence_refs':[]};changed[key]=v;lineage.append({'field':key,'basis':basis,'prior':old['fields'][key]})
 if r['kind']=='equipment_model' and rid in canonical:
  p,source=canonical[rid];note=source['locales']['th']['fields'].get('note_th')
  if note:
   specs=copy.deepcopy(value(r,'specifications') or [])
   specs=[x for x in specs if x.get('key')!='recorded_source_detail']
   specs.append({'key':'recorded_source_detail','value':note,'unit':None})
   set_field('specifications',specs,'literal note_th retained as source detail; no hardware inference')
   lineage.append({'source_path':p.relative_to(B/'system').as_posix(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':'/locales/th/fields/note_th','original_value':note})
 if r['kind']=='schedule':
  from app.calendar.service_calendar import regular_service_slots
  wd=value(r,'weekday');slots=regular_service_slots(date(2026,10,12)+timedelta(days=wd))
  set_field('timezone','Asia/Bangkok','app.calendar.service_calendar.BANGKOK_TZ key')
  set_field('bookable_periods',[{'start':x['start'],'end':x['end']} for x in slots if x['state']=='open'],'existing regular_service_slots; user already confirmed 12:00–13:00 no bookings; not asserting area opening')
  set_field('maintenance_periods',[{'start':x['start'],'end':x['end']} for x in slots if x['state']=='maintenance'],'existing regular_service_slots maintenance states')
  p=B/'system/app/calendar/service_calendar.py';lineage.append({'source_path':p.relative_to(B/'system').as_posix(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'original_timezone':'Asia/Bangkok','weekday':wd,'literal_slots':slots})
 if r['kind']=='control_set' and rid in canonical:
  # Existing English descriptions use *_en keys; R63 dropped those descriptions.
  p,source=canonical[rid];en=source['locales']['en']['fields'].get('controls',[])
  if en:
   full='\n'.join(' | '.join(str(x.get(k) or '') for k in ['button','action_en','description_en','section']) for x in en)
   if any(x.get('action_en') for x in en):
    loc=copy.deepcopy(value(r,'limitations'));loc['en']=full
    set_field('limitations',loc,'complete original English control rows, including description_en')
    lineage.append({'source_path':p.relative_to(B/'system').as_posix(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':'/locales/en/fields/controls','original_value':en})
 if not changed:continue
 payload={'mapped_fields':changed,'lineage':lineage,'migration_status':'draft_only_not_factually_approved'}
 raw=canonical_json(payload);sid='r66_'+hashlib.sha256((rid+raw).encode()).hexdigest()[:28]
 src={'source_id':sid,'kind':'derived_curated','path':'migration://r66/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 with s.connect() as c:existing=c.execute('SELECT payload FROM cc_sources WHERE source_id=?',(sid,)).fetchone()
 if existing:src=json.loads(existing['payload'])
 s.add_source(src,raw,actor='r66-evidence-mapping')
 for key in changed:r['fields'][key]['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/'+key}]
 try:saved=s.save(r,actor='r66-evidence-mapping',expected_version=old['revision'],change_note='Append derived source mapping; no owner approval/publication')
 except ValueError as e:audit.append({'record_id':rid,'error':str(e),'changed_fields':list(changed)});continue
 changes.append({'record_id':rid,'fields':list(changed),'revision':saved['version'],'source_id':sid})
with s.connect() as c:after_meta=dict(c.execute('SELECT * FROM cc_meta'))
assert before_meta['active']==after_meta['active']
out=B/'DRAFT_ENRICHMENT.json'
if out.exists():out=B/('DRAFT_ENRICHMENT_'+str(len(list(B.glob('DRAFT_ENRICHMENT*.json')))+1).zfill(2)+'.json')
out.write_text(json.dumps({'changes':changes,'errors':audit,'active_release_unchanged':True,'production_writes':0},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'revisions':len(changes),'errors':audit,'published':False},ensure_ascii=False))
