import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r124_legacy_guided_parity_20261023';S=R/'system'
freeze=json.loads((P/'FINAL_SOURCE_REVISION05.json').read_text('utf8'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert all(sha(Path(p))==h for p,h in freeze.items())
assert not S.exists();shutil.copytree(P/'revision05_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
(R/'PARENT_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
for name in ['serve_live.py','start_api.py']:
 text=(P/name).read_text('utf8').replace("S=R/'revision05_system'","S=R/'system'").replace('r124-legacy-guided-live','r125-date-context-live').replace('R124-revision05-live','R125-date-context-live')
 (R/name).write_text(text,'utf8')
config=json.loads((P/'LIVE_API_PROCESS.json').read_text('utf8'));rows=[]
for line in (Path(config['output'])/'PIPELINE_CAPTURE.jsonl').read_text('utf8').splitlines():
 row=json.loads(line);q=row.get('question','')
 if '26' not in q and '๒๖' not in q:continue
 result=row['pipeline'];art=result.get('decision_artifact',{})
 summary={'question':q,'answer':result['answer'],'elapsed':result['elapsed'],'understanding':art.get('understanding'),'needs':[{k:n.get(k) for k in ['category','status','reason_codes']} for n in art.get('need_results',[])]}
 rows.append({'summary':summary,'raw':row});print(json.dumps(summary,ensure_ascii=False))
(R/'BEFORE_DATE_FAILURES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
