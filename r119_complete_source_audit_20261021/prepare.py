import collections,hashlib,json,shutil,sqlite3,ast
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r118_precision_readers_20261021';S=R/'system'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
protected={str(p.resolve()):sha(p) for p in (OLD/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm'))}
for sub in ['http01','http02']:
 for name in ['RESULTS.jsonl','TEST_COMPLETE.json','RUN_FREEZE.json']:
  p=OLD/sub/name
  if p.exists():protected[str(p.resolve())]=sha(p)
(R/'PROTECTED_INPUTS.json').write_text(json.dumps(protected,indent=2),'utf8')
shutil.copytree('\\\\?\\'+str((OLD/'system').resolve()),'\\\\?\\'+str(S.resolve()),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.pyo','*-wal','*-shm','owner-session.json'))
with sqlite3.connect((OLD/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as source,sqlite3.connect(S/'data/knowledge/common.sqlite') as dest:source.backup(dest)
inventory=[];canonical=[];keys=collections.defaultdict(collections.Counter);kinds=collections.Counter();parse_errors=[]
for p in sorted((S/'data').rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(S)).replace('\\','/');part=p.relative_to(S/'data').parts[0]
 item={'path':rel,'sha256':sha(p),'bytes':p.stat().st_size,'classification':None}
 if part in {'eval','ground_truth','intent'}:item['classification']='evaluation_or_intent_workload_not_business_authority'
 elif part=='knowledge':item['classification']='native_database_or_runtime_state'
 else:item['classification']='source_or_derived_business_candidate'
 if p.suffix.lower() in {'.json','.jsonl'}:
  try:
   text=p.read_text('utf-8-sig');parsed=json.loads(text) if p.suffix=='.json' else [json.loads(s) for s in text.splitlines() if s.strip()]
   item['parsed']=True;item['json_type']=type(parsed).__name__
   if part=='content' and isinstance(parsed,dict) and parsed.get('content_id') and parsed.get('category'):
    row={'path':rel,'sha256':item['sha256'],'record':parsed};canonical.append(row);kind=parsed.get('kind');kinds[kind]+=1
    for k in parsed.get('facts',{}):keys[kind]['facts.'+k]+=1
    for lang,locale in parsed.get('locales',{}).items():
     for k in locale.get('fields',{}):keys[kind]['locales.'+lang+'.'+k]+=1
    item['classification']='canonical_legacy_record'
  except (UnicodeError,ValueError) as exc:item['parsed']=False;item['parse_error']=str(exc)[:200];parse_errors.append(item)
 inventory.append(item)
constants=[]
for p in sorted((S/'app').rglob('*.py')):
 if any(x in p.parts for x in ['vendor','__pycache__']):continue
 try:tree=ast.parse(p.read_text('utf-8-sig'))
 except (ValueError,UnicodeError,SyntaxError) as exc:constants.append({'path':str(p.relative_to(S)),'parse_error':str(exc)});continue
 for node in tree.body:
  if not isinstance(node,(ast.Assign,ast.AnnAssign)):continue
  names=[t.id for t in node.targets if isinstance(t,ast.Name)] if isinstance(node,ast.Assign) else [node.target.id] if isinstance(node.target,ast.Name) else []
  try:v=ast.literal_eval(node.value)
  except (ValueError,TypeError,AttributeError):continue
  if isinstance(v,(dict,list,tuple,set)) and names:
   constants.append({'path':str(p.relative_to(S)).replace('\\','/'),'line':node.lineno,'names':names,'value':v if not isinstance(v,set) else sorted(map(str,v))})
def write(name,v):(R/name).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str),'utf8')
write('FILE_INVENTORY.json',inventory);write('LEGACY_RECORDS.json',canonical);write('CODE_CONSTANTS.json',constants)
write('INVENTORY_SUMMARY.json',{'data_files':len(inventory),'classification':dict(collections.Counter(x['classification'] for x in inventory)),
 'canonical_records':len(canonical),'canonical_kinds':dict(kinds),'fields_by_kind':{k:dict(v) for k,v in keys.items()},'parse_errors':parse_errors,'literal_code_constants':len(constants),
 'protected_files':len(protected),'stage':'inventory_complete_not_migration_complete'})
print(json.dumps({'data_files':len(inventory),'canonical':len(canonical),'kinds':dict(kinds),'parse_errors':len(parse_errors),'constants':len(constants)}))
