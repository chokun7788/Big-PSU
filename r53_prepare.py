from pathlib import Path
import datetime,hashlib,json,shutil,subprocess
BASE=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r53_semantic_research_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
OUT.mkdir();(OUT/'before').mkdir();(OUT/'test_tmp').mkdir();(BASE/'r53_current_path.txt').write_text(str(OUT),encoding='utf-8')
hashes={}
for folder in ('app','web_chat','tests','data/curated','data/rules','booking_dashboard'):
 shutil.copytree(ROOT/folder,OUT/'before'/folder,ignore=shutil.ignore_patterns('__pycache__','*.pyc','logs','node_modules','.git'))
 for p in (OUT/'before'/folder).rglob('*'):
  if p.is_file():hashes[p.relative_to(OUT/'before').as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'before_hashes.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
p=subprocess.run(['git','status','--short'],cwd=ROOT,capture_output=True,text=True)
(OUT/'git_status_before.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
(OUT/'query_plan.json').write_text(json.dumps({'scope':'translation meaning, claim factuality, meta output, provenance, Thai length','method':'targeted primary-source fallback','helper_setup':{'openalex':False,'ncbi':False,'semantic_scholar':False},'year_window':None,'recent_leg':'2025-2026','skipped':['multi-database helper blocked by missing configuration','citation counts/ranks','saturation/PRISMA compliance','heavy COMET evaluator installation'],'queries':['translation quality estimation MQM xCOMET error annotations','FActScore atomic factual precision','Chain of Verification external feedback self correction','Thai word segmentation benchmark','2025 2026 translation hallucination factuality correction']},ensure_ascii=False,indent=2),encoding='utf-8')
print(OUT)
