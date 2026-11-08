import hashlib,json,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));out=Path(c['output'])
files={str(p.relative_to(R/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['app','web_chat'] for p in (R/'system'/folder).rglob('*') if p.is_file() and p.suffix in {'.py','.js','.json','.html','.css'} and '__pycache__' not in p.parts}
(out/'FINAL_SOURCE_FREEZE.json').write_text(json.dumps(files,indent=2),'utf8')
run={'started':time.time(),'api':c,'source_files':len(files),'scripts':[],'completed':False};(R/'FINAL_RUN.json').write_text(json.dumps(run,indent=2),'utf8')
for name in ['run_acceptance.py','run_context_acceptance.py','run_broad.py']:
 t=time.perf_counter();result=subprocess.run([sys.executable,'-B','-X','utf8',str(R/name)],cwd=R.parent)
 run['scripts'].append({'name':name,'exit_code':result.returncode,'seconds':time.perf_counter()-t})
 (R/'FINAL_RUN.json').write_text(json.dumps(run,indent=2),'utf8')
 if result.returncode:raise RuntimeError(name+' failed; preserve the run and inspect actual responses')
run['source_unchanged']=all(hashlib.sha256((R/'system'/p).read_bytes()).hexdigest()==h for p,h in files.items());run['completed']=True;run['finished']=time.time()
(R/'FINAL_RUN.json').write_text(json.dumps(run,indent=2),'utf8');assert run['source_unchanged'];print(json.dumps(run,indent=2))
