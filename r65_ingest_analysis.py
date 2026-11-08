"""Read-only R64 forensic indexing. Never executes the chatbot or changes old evidence."""
import collections,hashlib,json,sqlite3,sys,zlib,time
from pathlib import Path
BASE=Path(__file__).resolve().parent;B=BASE/'r64_full_comparison_20261013';O=BASE/'r65_detailed_failure_analysis_20261014'
sys.path.insert(0,str(B));from analyze import read
O.mkdir(exist_ok=False)
c=sqlite3.connect(O/'evidence.sqlite')
c.executescript('''
PRAGMA journal_mode=WAL;
CREATE TABLE jobs(key TEXT PRIMARY KEY,question TEXT,locale TEXT,reference_date TEXT);
CREATE TABLE expected(key TEXT,file TEXT,rownum INTEGER,variant TEXT,domain TEXT,case_json TEXT,PRIMARY KEY(key,file,rownum,variant));
CREATE TABLE results(arm TEXT,key TEXT,question TEXT,locale TEXT,exception TEXT,mode TEXT,category TEXT,intent TEXT,confidence REAL,elapsed REAL,answer TEXT,validation_ok INTEGER,source_file TEXT,source_line INTEGER,raw BLOB,PRIMARY KEY(arm,key));
CREATE TABLE grades(arm TEXT,key TEXT,file TEXT,rownum INTEGER,variant TEXT,passed INTEGER,evidence_level TEXT,content_asserted INTEGER,content_passed INTEGER,issues TEXT,reasons_json TEXT,grade_json TEXT,PRIMARY KEY(arm,key,file,rownum,variant));
CREATE INDEX grade_file ON grades(file,arm,passed);
CREATE INDEX expected_domain ON expected(domain);
''')
def dumps(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
for line in (B/'JOBS.jsonl').open(encoding='utf-8'):
 j=json.loads(line);c.execute('INSERT INTO jobs VALUES(?,?,?,?)',(j['key'],j['question'],j['locale'],j.get('reference_date','')))
 for e in j['entries']:
  case=e['case'];domain=case.get('domain') or case.get('expected_category') or case.get('category') or case.get('expected_route_categories') or case.get('expected_categories') or 'unspecified'
  if isinstance(domain,list):domain=' / '.join(map(str,domain))
  c.execute('INSERT INTO expected VALUES(?,?,?,?,?,?)',(j['key'],e['file'],e['row'],e['variant'],str(domain),dumps(case)))
c.commit()
def paths(m,arm):
 if arm=='offline':return [B/(m+'_offline')/'RESULTS.jsonl',B/(m+'_offline_resumed')/'RESULTS.jsonl',B/(m+'_bounded')/'RESULTS.jsonl']+sorted(B.glob(m+'_bounded_*/RESULTS.jsonl'))
 return [B/'model_matrix'/(m+'_RESULTS.jsonl.gz')]+sorted(B.glob('model_matrix_*/'+m+'_RESULTS.jsonl.gz'))
def reason_type(s):
 if s.startswith(('pipeline_exception','worker_error')):return 'runtime'
 if 'grader_exception' in s:return 'grader_error'
 if 'watchdog' in s or 'timeout' in s or s=='latency_ceiling':return 'deadline'
 if s.startswith(('route:','intent:','legacy_mode_prefix:','forbidden_category')) or s in {'wrong_category','wrong_intent'}:return 'protocol'
 if s.startswith('status:') or s=='wrong_outcome':return 'outcome'
 if 'validation' in s:return 'validation'
 if any(w in s for w in ('english_thai','Thai prose','localization')):return 'language'
 if any(w in s for w in ('source','target','evidence')):return 'source_target'
 if any(w in s for w in ('forbidden','off_topic')):return 'forbidden_content'
 if any(w in s for w in ('missing','required','clause','coverage')):return 'missing_content'
 return 'other'
manifest=[];counts={};started=time.perf_counter()
for m in ('legacy','common'):
 for kind in ('offline','llm'):
  arm=m+'_'+kind;seen=set();grades=0;duplicates=0
  for path in paths(m,kind):
   if not path.exists():continue
   consumed=0
   for lineno,r in enumerate(read(path),1):
    consumed+=1
    if r['key'] in seen:duplicates+=1;continue
    seen.add(r['key']);response=r.get('result') or {};route=response.get('route') or {};validation=response.get('validation') or {}
    c.execute('INSERT INTO results VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(arm,r['key'],r['question'],r.get('effective_locale',r.get('requested_locale','auto')),r.get('exception'),response.get('mode'),route.get('category'),route.get('intent'),response.get('confidence'),r.get('elapsed_wall'),response.get('answer'),None if 'ok' not in validation else bool(validation['ok']),str(path.relative_to(B)),lineno,zlib.compress(dumps(r).encode('utf-8'),1)))
    for g in r['grades']:
     issues=sorted(set(reason_type(s) for s in g.get('failures',[])))
     c.execute('INSERT INTO grades VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(arm,r['key'],g['file'],g['row'],g['variant'],bool(g['passed']),g.get('evidence_level'),bool(g.get('content_asserted')),None if g.get('content_checks_passed') is None else bool(g['content_checks_passed']),','.join(issues),dumps(g.get('failures',[])),dumps(g)))
     grades+=1
    if len(seen)%1000==0:c.commit();print(dumps({'arm':arm,'requests':len(seen),'elapsed':round(time.perf_counter()-started,1)}),flush=True)
   manifest.append({'arm':arm,'path':str(path),'bytes':path.stat().st_size,'rows_read':consumed,'mtime_ns':path.stat().st_mtime_ns})
  c.commit();counts[arm]={'requests':len(seen),'grades':grades,'duplicates_ignored':duplicates}
  assert len(seen)==20554 and grades==55811,(arm,len(seen),grades)
c.execute('CREATE INDEX grade_issue ON grades(arm,issues,passed)');c.commit()
(O/'INPUT_MANIFEST.json').write_text(json.dumps({'files':manifest,'counts':counts,'precedence':'identical to R64 analyzer: first result per key; earlier failures are not replaced','all_original_files_read_only':True,'pipeline_calls':0},ensure_ascii=False,indent=2),encoding='utf-8')
c.close();print(dumps(counts),flush=True)
