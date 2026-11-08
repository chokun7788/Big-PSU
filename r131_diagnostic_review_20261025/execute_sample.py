"""One authorized sample execution, gated on completed item02 diagnosis."""
import hashlib,json,os,sqlite3,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,x):
 p=R/n;t=p.with_name(p.name+'.new');t.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8');os.replace(t,p)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def health():
 with urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5) as f:return json.load(f)
def logical():
 c=sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
 records={x['record_id']:json.loads(x['payload']) for x in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
 pairs={x['source_id']:(json.loads(x['payload']),x['snapshot']) for x in c.execute('SELECT * FROM cc_sources')};meta=dict(c.execute('SELECT key,value FROM cc_meta'))
 payload={'active':'migration-preview-r69','epoch':int(meta['epoch']),'records':records,'sources':{k:v[0] for k,v in pairs.items()},'source_pairs':pairs,'withdrawn':[x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]}
 c.close();return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def phase(name,**v):write('STATUS.json',{'phase':name,'pid':os.getpid(),'updated_at':time.time(),'complete':False,'diagnosis_before_retest':True,'production_installed':False,**v})
try:
 gate=load(R/'DIAGNOSIS_PRETEST_COMPLETE.json');assert gate['complete'] and gate['runtime_fixes']==0
 selection=load(R/'SELECTION_FREEZE.json');assert sha(R/'SELECTED_JOBS.jsonl')==selection['sample_sha256']
 assert sha(R/'ITEM02_DETAILED_DIAGNOSIS_TH.md')==gate['report_sha256']
 assert not (R/'sample01').exists(),'Never duplicate or overwrite a sample run'
 phase('verify_frozen_inputs_before_sample')
 freeze=load(P/'EXECUTION_FREEZE_R130.json');changed=[p for p,h in freeze.items() if not Path(p).exists() or sha(p)!=h];assert not changed,changed
 before=health();assert before==load(P/'MODEL_IDENTITY_AFTER.json')
 source_before=logical();assert source_before==load(P/'SOURCE_SNAPSHOT_BEFORE.json')['sha256']
 for name in ['prepare_diagnostics.py','forensic_probes.py','publish_diagnosis.py','execute_sample.py','run_sample.py','SELECTED_JOBS.jsonl','CATEGORY_MEMBERSHIP.json','SELECTION_FREEZE.json','ITEM02_DETAILED_DIAGNOSIS_TH.md','DIAGNOSIS_PRETEST_COMPLETE.json']:
  freeze[str((R/name).resolve())]=sha(R/name)
 write('RUN_FREEZE.json',freeze);write('MODEL_BEFORE.json',before);write('SOURCE_LOGICAL_BEFORE.json',{'sha256':source_before})
 stdout=R/'sample01.stdout.log';stderr=R/'sample01.stderr.log'
 with stdout.open('x',encoding='utf8') as out,stderr.open('x',encoding='utf8') as err:
  args=[sys.executable,'-B','-u',str(R/'run_sample.py'),'--workers','2','--tag','sample01','--jobs',str(R/'SELECTED_JOBS.jsonl')]
  child=subprocess.Popen(args,cwd=R.parent,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  write('TEST_PROCESS.json',{'pid':child.pid,'command':args,'stdout':str(stdout),'stderr':str(stderr),'diagnosis_gate_verified':True,'new_questions':0,'runtime_changed':False})
  while child.poll() is None:phase('sample01_running',child_pid=child.pid,stdout=str(stdout),stderr=str(stderr));time.sleep(15)
  assert child.returncode==0,('sample_exit',child.returncode)
 phase('verify_frozen_inputs_after_sample')
 changed=[p for p,h in freeze.items() if not Path(p).exists() or sha(p)!=h];assert not changed,changed
 after=health();assert after==before
 source_after=logical();assert source_after==source_before
 write('MODEL_AFTER.json',after);write('SOURCE_LOGICAL_AFTER.json',{'sha256':source_after})
 write('EXECUTION_COMPLETE.json',{'complete':True,'source_input_code_prompt_weights_unchanged':True,'model_profile_identity_verified':True,'frozen_files_checked':len(freeze),'diagnosis_completed_before_new_test':True,'test_database_unchanged':load(R/'sample01/RUN_FINISHED.json')['test_database_unchanged'],'runtime_fixes':0,'baseline_new_inferences':0,'flow_quality_acceptance_complete':False})
 phase('sample_execution_complete_analysis_pending',execution_complete=True)
except BaseException as exc:
 name='EXECUTION_FAILURE_'+str(time.time_ns())+'.json';write(name,{'error':repr(exc),'traceback':traceback.format_exc()});phase('execution_failure_requires_diagnosis',failure_record=name,error=repr(exc));raise
