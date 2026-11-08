"""Exactly one frozen post-fix execution of R131's outcome-blind sample."""
import hashlib,json,os,sqlite3,subprocess,sys,time,urllib.request,traceback
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;D=B/'r131_diagnostic_review_20261025';P=B/'r130_owner_context_completion_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,x):
 p=R/n;t=p.with_suffix(p.suffix+'.new');t.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8');os.replace(t,p)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def logical():
 c=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
 records={x['record_id']:json.loads(x['payload']) for x in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')};pairs={x['source_id']:(json.loads(x['payload']),x['snapshot']) for x in c.execute('SELECT * FROM cc_sources')};meta=dict(c.execute('SELECT key,value FROM cc_meta'))
 payload={'active':'migration-preview-r69','epoch':int(meta['epoch']),'records':records,'sources':{k:v[0] for k,v in pairs.items()},'source_pairs':pairs,'withdrawn':[x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]};c.close()
 return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def health():
 with urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5) as f:return json.load(f)
def phase(name,**kw):write('STATUS.json',{'phase':name,'complete':False,'requirements_scope':76,'categories_scope':14,'weights_changed':False,'source_data_changes':0,'production_installed':False,'updated_at':time.time(),**kw})
def main():
 assert not (R/'sample01').exists(),'Never overwrite/repeat this sample'
 api=load(R/'PROCESS.json');assert load(Path(api['output'])/'TARGETED_COMPLETE.json')['all_passed'];assert load(Path(api['output'])/'CONTEXT_COMPLETE.json')['all_passed']
 assert load(R/'LATEST_CORE_VERIFICATION.json')['all_passed']
 sel=load(D/'SELECTION_FREEZE.json');assert sha(D/'SELECTED_JOBS.jsonl')==sel['sample_sha256']
 jobs=[json.loads(l) for l in (D/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines()];assert len(jobs)==2111 and sum(len(x['entries']) for x in jobs)==5584
 phase('freeze_post_fix_sample')
 parent=load(P/'EXECUTION_FREEZE_R130.json');changed=[p for p,h in parent.items() if sha(p)!=h];assert not changed,changed
 before=health();assert before==load(P/'MODEL_IDENTITY_AFTER.json');digest=logical();assert digest==load(R/'SOURCE_DATABASE_LINEAGE.json')['source_logical_digest']
 freeze={str(p.resolve()):sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm'))}
 for p in [*R.glob('*.py'),D/'SELECTED_JOBS.jsonl',D/'CATEGORY_MEMBERSHIP.json',D/'SELECTION_FREEZE.json'] :freeze[str(p.resolve())]=sha(p)
 # Retain actual base/adapter assets from the parent freeze, not just names.
 for p,h in parent.items():
  if not str(Path(p)).lower().startswith(str(P).lower()):freeze[p]=h
 write('RUN_FREEZE.json',freeze);write('MODEL_BEFORE.json',before);write('SOURCE_LOGICAL_BEFORE.json',{'sha256':digest})
 args=[sys.executable,'-B','-u',str(R/'run_common.py'),'--workers','2','--tag','sample01','--jobs',str(D/'SELECTED_JOBS.jsonl')]
 with (R/'sample01.stdout.log').open('x',encoding='utf8') as out,(R/'sample01.stderr.log').open('x',encoding='utf8') as err:
  proc=subprocess.Popen(args,cwd=B,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0));write('TEST_PROCESS.json',{'pid':proc.pid,'controller_pid':os.getpid(),'command':args,'new_questions':0,'baseline_inferences':0,'weights_changed':False,'source_changes':0,'intentional_changes':['R132 runtime/readers/protocol prompts','lossless protocol surface adapter','admission wait and reservation accounting']});phase('post_fix_sample_running',child_pid=proc.pid)
  code=proc.wait();assert code==0,('sample_exit',code)
 changed=[p for p,h in freeze.items() if sha(p)!=h];assert not changed,changed
 after=health();assert after==before;assert logical()==digest
 write('MODEL_AFTER.json',after);write('EXECUTION_COMPLETE.json',{'complete':True,'candidate_input_source_weights_unchanged_during_measurement':True,'frozen_files_checked':len(freeze),'actual_model_identity_verified':True,'baseline_inferences':0,'new_benchmark_questions':0,'semantic_accuracy':None,'flow_quality_acceptance_complete':False})
 phase('post_fix_sample_complete_analysis_pending',sample_complete=True)
if __name__=='__main__':
 try:main()
 except BaseException as exc:
  write('EXECUTION_FAILURE_'+str(time.time_ns())+'.json',{'error':repr(exc),'traceback':traceback.format_exc()});raise
