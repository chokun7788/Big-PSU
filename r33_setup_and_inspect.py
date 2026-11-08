import json,hashlib,shutil,subprocess,uuid
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');OLD=Path((ROOT/'r32_report_path.txt').read_text().strip())
R=P/'reports'/('r33_usable_answers_'+datetime.now(ZoneInfo('Asia/Bangkok')).strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);R.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before={}
for folder in ['app','tests','tools','web_chat','deployment_templates']:
 for p in (P/folder).rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
  rel=p.relative_to(P).as_posix();before[rel]=sha(p);dest=R/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
previous=json.loads((OLD/'protected_manifest.json').read_text());protected={k:sha(P/k) for k in previous};changes=[k for k in previous if previous[k]!=protected[k]]
for name,data in [('before_manifest.json',before),('protected_manifest.json',protected),('owner_changes_since_r32.json',changes)]:
 with (R/name).open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=P,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (R/'git_status_before.txt').open('x',encoding='utf-8') as f:f.write(status)
with (ROOT/'r33_report_path.txt').open('x',encoding='utf-8') as f:f.write(str(R)+'\n')
rows=[json.loads(l) for l in (OLD/'REMAINING_107_FINAL13_DETAILED.jsonl').open(encoding='utf-8')]
for i,x in enumerate(rows,1):
 print(str(i)+'. ['+x['id']+']['+str(x['positive_contract'])+'] '+x['clean']['question']+' => '+x['noisy']['question']+' | '+x['noisy']['result'].get('route',{}).get('category','')+' | '+x['noisy']['result'].get('answer','').replace('\n',' ')[:100])
print(json.dumps({'report':str(R),'snapshots':len(before),'protected':len(protected),'owner_changes':changes},ensure_ascii=False))
