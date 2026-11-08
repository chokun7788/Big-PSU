"""Exhaustive source retention and native evidence audit, no model calls."""
import base64,collections,gzip,hashlib,json,sqlite3,sys,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.registry import SCHEMAS,CATALOG,pointer
from jsonschema import Draft202012Validator,FormatChecker
write=lambda name,v:(R/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((R/'NATIVE_BEFORE.json').read_text('utf8'))
c=sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
sources={sid:(json.loads(meta),json.loads(snap),snap) for sid,meta,snap in c.execute('SELECT source_id,payload,snapshot FROM cc_sources')}
source_errors=[]
for sid,(meta,snap,raw) in sources.items():
 if hashlib.sha256(raw.encode()).hexdigest()!=meta['sha256']:source_errors.append({'source_id':sid,'error':'source_hash_mismatch'})
validators={k:Draft202012Validator(s,format_checker=FormatChecker()) for k,s in SCHEMAS.items()}
def validate_fields(recs,src):
 errors=[];count=collections.Counter();rows=[]
 for rid,r in recs.items():
  for err in validators[r['kind']].iter_errors(r):errors.append({'record_id':rid,'field':'$schema','error':err.message,'path':list(err.absolute_path)})
  for key,f in r['fields'].items():
   count['all_fields']+=1;count[f['status']]+=1
   refs=f.get('evidence_refs',[])
   if f['status']=='known' and not refs:errors.append({'record_id':rid,'field':key,'error':'known_without_evidence'})
   for ref in refs:
    count['evidence_refs']+=1
    if ref['source_id'] not in src:errors.append({'record_id':rid,'field':key,'error':'missing_source'});continue
    entry=src[ref['source_id']];metadata=entry[0];document=entry[1]
    if r['kind'] not in metadata['authority_for']:errors.append({'record_id':rid,'field':key,'error':'authority_kind_mismatch'})
    try:actual=pointer(document,ref['locator'])
    except (KeyError,ValueError,IndexError,TypeError):errors.append({'record_id':rid,'field':key,'error':'invalid_pointer'});continue
    if f['status']=='known' and actual!=f['value']:errors.append({'record_id':rid,'field':key,'error':'pointer_value_mismatch'})
   if f['status']=='known':
    spec=next((x for x in CATALOG[r['kind']]['fields'] if x['key']==key),{})
    if spec.get('reference_kind'):
     for target in f['value'] if isinstance(f['value'],list) else [f['value']]:
      if target not in recs:errors.append({'record_id':rid,'field':key,'error':'missing_target','target':target})
      elif spec['reference_kind']!='*' and recs[target]['kind']!=spec['reference_kind']:errors.append({'record_id':rid,'field':key,'error':'wrong_target_kind','target':target})
   rows.append({'record_id':rid,'kind':r['kind'],'field':key,'status':f['status'],'evidence_refs':refs})
 return errors,count,rows
oldsrc={sid:(x['metadata'],x['snapshot']) for sid,x in before['sources'].items()}
base_errors,base_count,_=validate_fields(before['records'],oldsrc)
errors,count,field_rows=validate_fields(records,sources)
signature=lambda x:json.dumps(x,ensure_ascii=False,sort_keys=True)
base_signatures={signature(x) for x in base_errors};new_errors=[x for x in errors if signature(x) not in base_signatures]
write('NATIVE_FIELD_AUDIT.json',{'records':len(records),'counts':dict(count),'baseline_errors':base_errors,'current_errors':errors,'introduced_errors':new_errors,'source_integrity_errors':source_errors})
(R/'NATIVE_FIELD_CHECKLIST.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in field_rows),'utf8')
files=json.loads((R/'FILE_DISPOSITIONS.json').read_text('utf8'));retention=[]
for item in files:
 if item['disposition']!='source_preserved_losslessly':retention.append({'path':item['path'],'status':item['disposition']});continue
 snapshot=sources[item['archive_source_id']][1]['original']
 raw=gzip.decompress(base64.b64decode(snapshot['bytes']))
 assert len(raw)==snapshot['original_bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256']
 assert raw==(S/item['path']).read_bytes()
 retention.append({'path':item['path'],'status':'byte_exact_archive_verified','sha256':item['sha256']})
write('BYTE_RETENTION_AUDIT.json',retention)
def leaves(x,path=''):
 if isinstance(x,dict):
  for k,v in x.items():yield from leaves(v,path+'/'+str(k).replace('~','~0').replace('/','~1'))
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from leaves(v,path+'/'+str(i))
 else:yield path,x
mapping={x['content_id']:x for x in json.loads((R/'RECORD_MAPPING.json').read_text('utf8'))};leaf_rows=[]
for item in json.loads((R/'LEGACY_RECORDS.json').read_text('utf8')):
 row=item['record'];m=mapping[row['content_id']];rid=m['native_record_id']
 if m['status']=='current_native_root_linked':
  context=records[rid]['fields']['legacy_context']['value'];assert context==row
  disposition='native_lossless_context_and_existing_typed_fields'
 else:context=row;disposition=m['status']
 for p,v in leaves(row):
  assert pointer(context,p)==v
  leaf_rows.append({'source_path':item['path'],'content_id':row['content_id'],'json_pointer':p,'native_record_id':rid,
                   'disposition':disposition,'typed_restored':any(p.startswith('/'+x.replace('.','/')) for x in m.get('typed_restored_paths',[])),
                   'value_sha256':hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()})
(R/'LEGACY_LEAF_CHECKLIST.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in leaf_rows),'utf8')
# Read the source workbook's actual cells, including formula text/cached values.
workbook=S/'data/sources/zone_rental_fees_20261006.xlsx';workbook_cells=[]
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(workbook) as z:
 shared=[]
 if 'xl/sharedStrings.xml' in z.namelist():
  shared=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',ns)]
 for name in z.namelist():
  if not name.startswith('xl/worksheets/sheet') or not name.endswith('.xml'):continue
  for cell in ET.fromstring(z.read(name)).findall('.//s:c',ns):
   v=cell.find('s:v',ns);inline=cell.find('s:is',ns);formula=cell.find('s:f',ns)
   raw=v.text if v is not None else ''.join(inline.itertext()) if inline is not None else None
   text=shared[int(raw)] if cell.get('t')=='s' and raw is not None else raw
   workbook_cells.append({'sheet':name,'cell':cell.get('r'),'value':text,'formula':formula.text if formula is not None else None})
write('WORKBOOK_CELL_AUDIT.json',{'sha256':sha(workbook),'cells':workbook_cells,'formulas_recalculated':False,'basis':'read source values and formulas; no workbook mutation'})
# Compare the actual old checkout as well. Differences are preserved as source
# variants, never allowed to overwrite the newer owner-confirmed candidate.
external=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
external_rows=[];canonical_external=[]
if external.exists():
 for p in sorted((external/'data').rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts:continue
  rel=p.relative_to(external);inside=S/rel
  if p.suffix in {'.sqlite','.sqlite-wal','.sqlite-shm','.db'}:
   external_rows.append({'path':rel.as_posix(),'disposition':'external_runtime_database_not_mutated','bytes':p.stat().st_size});continue
  raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest();same=inside.exists() and h==sha(inside)
  record={'path':rel.as_posix(),'sha256':h,'bytes':len(raw),'same_as_candidate_legacy':same}
  if p.suffix in {'.json','.jsonl'}:
   try:
    parsed=json.loads(raw.decode('utf-8-sig')) if p.suffix=='.json' else [json.loads(s) for s in raw.decode('utf-8-sig').splitlines() if s.strip()]
    record['parsed']=True
    if isinstance(parsed,dict) and parsed.get('content_id'):canonical_external.append({'path':rel.as_posix(),'id':parsed['content_id'],'same':same})
   except (UnicodeError,ValueError) as exc:record['parsed']=False;record['parse_error']=str(exc)[:200]
  record['disposition']='same_source_version' if same else 'different_or_external_only_source_version_reviewed_separately'
  external_rows.append(record)
write('EXTERNAL_SOURCE_AUDIT.json',{'root':str(external),'read_only':True,'files':external_rows,'canonical':canonical_external})
protected=json.loads((R/'PROTECTED_INPUTS.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in protected.items())
summary={'audit_complete':not new_errors and not source_errors,'candidate_files_accounted':len(files),'byte_exact_archives_verified':sum(x['status']=='byte_exact_archive_verified' for x in retention),
 'canonical_records_accounted':len(mapping),'canonical_leaf_values_checked':len(leaf_rows),'unclassified_canonical_leaves':0,'native_records_checked':len(records),
 'native_fields_checked':count['all_fields'],'native_evidence_refs_checked':count['evidence_refs'],'native_sources_checked':len(sources),'introduced_native_errors':len(new_errors),
 'baseline_native_errors':len(base_errors),'source_hash_errors':len(source_errors),'workbook_cells_checked':len(workbook_cells),'external_files_checked':len(external_rows),
 'external_source_variants':sum(x.get('same_as_candidate_legacy') is False for x in external_rows),'protected_files_unchanged':True,
 'scope_note':'Lossless retention is separate from typed reader parity and semantic accuracy. Reader checks and saved-question HTTP validation are separate gates.'}
write('FULL_AUDIT_GATE.json',summary);print(json.dumps(summary));assert summary['audit_complete']
