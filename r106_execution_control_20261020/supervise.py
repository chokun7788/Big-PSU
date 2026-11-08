"""Final changed-path gate then one immutable common-only LLM-ON full run."""
import hashlib,json,os,subprocess,sys,time,traceback,urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from analyze import full
C=Path(__file__).resolve().parent;B=C.parent;R=B/'r106_complete_flow_20261020';PRE=B/'r105_complete_flow_20261020'
def dump(p,x):
 temp=p.with_suffix('.tmp');temp.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str),'utf8');os.replace(temp,p)
def emit(**kw):dump(C/'STATUS.json',{'supervisor_pid':os.getpid(),'updated_at':datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(),**kw})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(root):return {p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
def unchanged():
 frozen=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));inputs=json.loads((R/'FROZEN_INPUTS.json').read_text('utf8'))
 return manifest(R/'system')==frozen and all(sha(R/p)==h for p,h in inputs.items())
def model_identity():
 try:
  with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as f:tags=json.load(f)
  conf=json.loads((R/'MODEL_CONFIG_MANIFEST.json').read_text('utf8'));expected={x['digest'] for x in conf['installed_candidates']}
  actual={x['digest'] for x in tags.get('models',[]) if str(x.get('name','')).removesuffix(':latest')==conf['name'].removesuffix(':latest')}
  return {'verified':bool(expected) and actual==expected,'expected_digests':sorted(expected),'actual_digests':sorted(actual)}
 except Exception as e:return {'verified':False,'error_type':type(e).__name__}
try:
 base=json.loads((PRE/'integrated04/BATCH_COMPLETE.json').read_text('utf8'))
 assert base['all_lanes_executed'] and base['source_unchanged']
 inherited={'retained_flow','owner_24','semantic_protocol','simulated_live','published_profiles','typed_conflicts','rental','competition','actual_http','real_new_game'}
 assert all(x['exit_code']==0 for x in base['lanes'] if x['lane'] in inherited)
 old=json.loads((PRE/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));new=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'))
 assert manifest(PRE/'system')==old
 changed=[p for p in set(old)|set(new) if old.get(p)!=new.get(p)]
 allowed={'app/knowledge/common/complete_flow.py','app/knowledge/common/intent_contracts.py','app/knowledge/common/qualified_tasks.py','app/knowledge/common/rules_reader.py','app/knowledge/common/source_rows.py'}
 assert set(changed)<=allowed and unchanged()
 dump(C/'LINEAGE.json',{'inherited_r105_batch':str(PRE/'integrated04/BATCH_COMPLETE.json'),'changed_runtime_files':sorted(changed),'same_real_database':old['data/knowledge/common.sqlite']==new['data/knowledge/common.sqlite'],'inherited_lanes':sorted(inherited),'r106_is_not_claimed_to_have_rerun_all_19_lanes':True})
 env=os.environ.copy();env.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_MAX_CONCURRENCY='1')
 gate=R/'final_gate';gate.mkdir(exist_ok=False);lanes=[('model_readiness_lane.py','model_readiness'),('test_r102_contracts.py','updated_contracts'),('test_contract_flow.py','retained_contracts'),('test_flow_v2.py','retained_v2'),('test_task_matrix.py','task_matrix'),('run_acceptance.py','r97_acceptance')];rows=[]
 for script,name in lanes:
  assert unchanged();emit(stage='final_grouped_gate',running=True,current_lane=name,lanes_complete=len(rows),lanes_total=len(lanes))
  tag='final_gate_'+name
  with (gate/(name+'.log')).open('x',encoding='utf8') as log:result=subprocess.run([sys.executable,'-B','-X','utf8',str(R/script),tag],cwd=B,env=env,stdout=log,stderr=subprocess.STDOUT)
  summary=R/'verification'/tag/'SUMMARY.json';data=json.loads(summary.read_text('utf8')) if summary.exists() else None
  rows.append({'lane':name,'exit_code':result.returncode,'summary':data,'summary_path':str(summary),'log':str(gate/(name+'.log'))});dump(gate/'RESULTS.json',rows)
 assert unchanged()
 if any(x['exit_code'] or not x['summary'] for x in rows):
  emit(stage='needs_grouped_revision',running=False,lanes=rows,source_unchanged=True);sys.exit(2)
 lines=['# R106 final gate','', 'R105 integrated04 เป็นหลักฐานการตรวจทุก lane; R106 ตรวจซ้ำเฉพาะสาขาที่แก้ และจะตรวจ E2E ด้วย Full Test ใหม่ ไม่มีการรวมต่างหน่วยเป็น accuracy เดียว','', '| Lane | Passed | Total |','|---|---:|---:|']
 for x in rows:lines.append(f"| {x['lane']} | {x['summary'].get('passed')} | {x['summary'].get('count')} |")
 (gate/'REPORT_TH.md').write_text('\n'.join(lines),'utf8')
 identity=model_identity();dump(C/'MODEL_IDENTITY_BEFORE.json',identity);assert identity['verified']
 jobs=B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl';jobs_rows=[json.loads(x) for x in jobs.read_text('utf8').splitlines()]
 assert len(jobs_rows)==20554 and len({j['key'] for j in jobs_rows})==20554 and sum(len(j['entries']) for j in jobs_rows)==55811
 dump(C/'FULL_INPUT.json',{'path':str(jobs),'sha256':sha(jobs),'unique_requests':20554,'grades':55811,'format':'common_only','llm_enabled':True})
 with (C/'FULL_RUN.log').open('x',encoding='utf8') as log:
  proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'run_common.py'),'--workers','2','--tag','full01','--jobs',str(jobs)],cwd=B,env=env,stdout=log,stderr=subprocess.STDOUT)
  emit(stage='full_running',running=True,full_pid=proc.pid,expected_requests=20554,expected_grades=55811,source_unchanged_before=True)
  while proc.poll() is None:
   time.sleep(15)
   try:progress=json.loads((R/'full01/PROGRESS.json').read_text('utf8'))
   except (OSError,ValueError):progress={}
   emit(stage='full_running',running=True,full_pid=proc.pid,progress=progress)
 if proc.returncode:raise RuntimeError('Full runner exit code '+str(proc.returncode))
 emit(stage='full_analysis',running=True);coverage=full();stable=unchanged();after=model_identity();dump(C/'MODEL_IDENTITY_AFTER.json',after)
 result={'status':'complete' if coverage['complete'] and stable and after['verified'] else 'incomplete','coverage':coverage,'source_and_frozen_inputs_unchanged':stable,'model_identity_verified':after['verified'],'report':str(R/'full_analysis/FINAL_REPORT_TH.md'),'not_installed_over_production':True}
 dump(R/'FULL_TEST_COMPLETE.json',result);emit(stage=result['status'],running=False,**result)
except Exception:
 (C/'SUPERVISOR_ERROR.txt').write_text(traceback.format_exc(),'utf8');emit(stage='failed',running=False,error_log=str(C/'SUPERVISOR_ERROR.txt'));raise
