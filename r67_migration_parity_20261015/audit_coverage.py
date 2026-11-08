"""Independent source-to-field comparison, never treats archived bytes as readable facts."""
import collections,json,re,sqlite3,sys,unicodedata
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from migrate_ids import stable,sid

def leaves(v,path=''):
 if isinstance(v,dict):
  for k,x in v.items():yield from leaves(x,path+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):yield from leaves(x,path+'/'+str(i))
 elif v not in (None,''):yield path,v
def normalized(v):return re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(v))).strip().casefold()
def audit(db):
 store=CommonStore(db)
 with store.connect() as c:records=store.heads(c)
 rows=[];counts=collections.Counter()
 for p in sorted((B/'source_snapshot/data/content').rglob('*.json')):
  if any(x in p.relative_to(B/'source_snapshot/data/content').parts for x in ('schema','review','projections','releases')):continue
  x=json.loads(p.read_text('utf-8-sig'))
  if 'content_id' not in x:continue
  kind=x['kind'];rid=stable(x['content_id']);counts[kind]+=1
  if kind in {'policy_rule','knowledge_fact','service_fee_policy'}:rid='migrated_faq_'+sid(x['content_id'])
  for lang,locale in x['locales'].items():
   for path,original in leaves(locale['fields']):
    target=rid;key=None;sub=None;reason=None
    parts=path.split('/')[1:];name=parts[0]
    if kind=='game_profile':key={'title':'title','summary_th':'summary','summary_en':'summary','how_to_play_th':'how_to_play','how_to_play_en':'how_to_play','genre':'genre'}.get(name)
    elif kind=='member':key={'name':'display_name','role':'role','affiliation':'affiliation'}.get(name)
    elif kind=='service_availability':key='notes'
    elif kind=='equipment':key='name' if name=='item' else 'usage'
    elif kind=='service_closure':key='reason'
    elif kind=='competition_document':
     if name=='title':key='source_title'
     elif name=='sections':
      target=stable(x['content_id']+'_section_'+str(int(parts[1])+1).zfill(3));key={'section_title':'heading','text':'text','section_index':'section_number'}.get(parts[2])
    elif kind=='control_map':
     if name=='summary':key='source_summary'
     elif name=='controls':
      key='bindings';sub=int(parts[1]);rowkey={'button':'button_label','buttons':'buttons','action_th':'action','action':'action','description_th':'notes','description':'notes','section':'section'}.get(parts[2]);keypath=parts[2]
    elif kind in {'knowledge_fact','service_fee_policy','policy_rule'}:key='question' if name=='title' else 'answer'
    r=records.get(target);v=value(r,key) if r and key else None
    if kind=='control_map' and sub is not None and isinstance(v,list) and sub<len(v):
     v=v[sub].get(rowkey)
     if parts[2]=='buttons' and len(parts)>3 and isinstance(v,list):v=v[int(parts[3])] if int(parts[3])<len(v) else None
    if isinstance(v,dict) and set(v)=={'th','en'}:v=v.get(lang)
    candidates=[str(a) for _,a in leaves(v)] if isinstance(v,(dict,list)) else [str(v)] if v is not None else []
    # A whole source field may be one block within a losslessly joined field.
    exact=any(normalized(original) in normalized(a) for a in candidates)
    if not r and kind=='policy_rule' and x['facts'].get('route_category',x['category']) in {'no_answer','english_support'}:
     status='engine_configuration_archived';reason='Refusal/language routing configuration, not a center fact'
    elif exact:status='readable_exact'
    elif key and v is not None:status='different_requires_review';reason='Target exists but original text is not verbatim in its corresponding locale'
    else:status='missing_readable_field';reason='No readable mapped field; archive presence does not count'
    rows.append({'source':p.relative_to(B/'source_snapshot').as_posix(),'source_kind':kind,'locale':lang,'pointer':'/locales/'+lang+'/fields'+path,'original':original,'target':target,'field':key,'row':sub,'status':status,'reason':reason})
 return {'canonical_sources':sum(counts.values()),'by_kind':dict(counts),'counts':dict(collections.Counter(r['status'] for r in rows)),'rows':rows}
before=audit(B/'before.sqlite');after=audit(B/'common.sqlite')
for name,data in [('COVERAGE_BEFORE.json',before),('COVERAGE_AFTER.json',after)]:
 target=Path(name);target=target.with_stem(target.stem+'_'+sys.argv[1]) if len(sys.argv)>1 else target
 (B/target).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'before':before['counts'],'after':after['counts']},ensure_ascii=False))
