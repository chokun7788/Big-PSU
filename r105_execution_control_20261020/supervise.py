"""Owned supervisor: wait for integrated gates, then one common-only full run."""
import hashlib,json,os,subprocess,sys,time,traceback
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from analyze import integrated,full
B=Path(__file__).resolve().parent.parent;R=B/'r105_complete_flow_20261020';C=Path(__file__).resolve().parent
STATUS=C/'STATUS.json'
def dump(p,x):
 temp=p.with_suffix('.tmp');temp.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8');os.replace(temp,p)
def emit(**kw):dump(STATUS,{'supervisor_pid':os.getpid(),'updated_at':datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(),**kw})
def unchanged():
 frozen=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));inputs=json.loads((R/'FROZEN_INPUTS.json').read_text('utf8'))
 current={p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
 return frozen==current and all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in inputs.items())
try:
 emit(stage='waiting_integrated',running=True)
 while not (R/'integrated04/BATCH_COMPLETE.json').exists():time.sleep(15)
 batch=integrated();emit(stage='integrated_analysis_complete',running=True,integrated_source_unchanged=batch['source_unchanged'])
 mandatory={'model_readiness','new_contracts','retained_contracts','retained_flow','owner_24','simulated_live','published_profiles','typed_conflicts','actual_http','semantic_protocol','retained_v2','competition','task_matrix'}
 failed=[x['lane'] for x in batch['lanes'] if x['lane'] in mandatory and x['exit_code']]
 if failed or not batch['source_unchanged'] or not unchanged():
  emit(stage='needs_grouped_revision',running=False,blocking_lanes=failed,reason='Integrated safety gates or source integrity require review before full run',report=str(R/'analysis_integrated04/REPORT_TH.md'));sys.exit(2)
 jobs=B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl'
 rows=[json.loads(x) for x in jobs.read_text('utf8').splitlines()];assert len(rows)==20554 and len({j['key'] for j in rows})==20554 and sum(len(j['entries']) for j in rows)==55811
 dump(C/'FULL_INPUT.json',{'path':str(jobs),'sha256':hashlib.sha256(jobs.read_bytes()).hexdigest(),'unique_requests':len(rows),'grades':55811,'format':'common_only','llm_enabled':True})
 args=[sys.executable,'-B','-X','utf8',str(R/'run_common.py'),'--workers','2','--tag','full01','--jobs',str(jobs)]
 with (C/'FULL_RUN.log').open('x',encoding='utf8') as log:
  proc=subprocess.Popen(args,cwd=B,stdout=log,stderr=subprocess.STDOUT)
  emit(stage='full_running',running=True,full_pid=proc.pid,source_unchanged_before=True,expected_requests=20554,expected_grades=55811)
  while proc.poll() is None:
   time.sleep(15)
   try:progress=json.loads((R/'full01/PROGRESS.json').read_text('utf8'))
   except (OSError,ValueError):progress={}
   emit(stage='full_running',running=True,full_pid=proc.pid,progress=progress)
 if proc.returncode:raise RuntimeError('Full runner exit code '+str(proc.returncode))
 emit(stage='full_analysis',running=True)
 coverage=full();stable=unchanged()
 completion={'coverage':coverage,'source_and_frozen_inputs_unchanged':stable,'report':str(R/'full_analysis/FINAL_REPORT_TH.md'),'not_installed_over_production':True,'status':'complete' if coverage['complete'] and stable else 'incomplete'}
 dump(R/'FULL_TEST_COMPLETE.json',completion)
 emit(stage=completion['status'],running=False,**completion)
except Exception:
 (C/'SUPERVISOR_ERROR.txt').write_text(traceback.format_exc(),'utf8');emit(stage='failed',running=False,error_log=str(C/'SUPERVISOR_ERROR.txt'));raise
