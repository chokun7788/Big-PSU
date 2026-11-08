import json,shutil,hashlib,sqlite3
from pathlib import Path
import r50_probe as r
release=Path((r.OUT/'release_r50_2_path.txt').read_text());destination=Path((r.OUT/'share_path.txt').read_text())
for name in ['01_Download_Models','02_With_Models']:
 target=destination/name;inner=target/'system/PSU_Esports_Chatbot_Local'
 shutil.copytree(release/'data',inner/'data',dirs_exist_ok=True,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc'))
 checks={p.relative_to(release).as_posix():(inner/p.relative_to(release)).is_file() and p.read_bytes()==(inner/p.relative_to(release)).read_bytes() for directory in ['app','web_chat','data'] for p in (release/directory).rglob('*') if p.is_file() and not {'logs','state','__pycache__'}.intersection(p.relative_to(release).parts)}
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 assert not list(target.rglob('*.sqlite3'))
 with (target/'R50_FULL_RUNTIME_DATA_CHECKS.json').open('x',encoding='utf-8') as f:json.dump(dict(equal_files=sum(checks.values()),checks=checks,no_private_sqlite_state=True),f,indent=2)
# Recover what was committed by the first concurrent restart probe; HTTP
# errors were not captured by its original harness, so do not invent them.
seed=json.loads((r.OUT/'HTTP_RESTART_SEED.json').read_text(encoding='utf-8'));state=release/'data/logs/dialogue_state_v1.sqlite3';rows=[]
from contextlib import closing
with closing(sqlite3.connect(f'file:{state.as_posix()}?mode=ro',uri=True)) as db:
 for original in seed['cases']:
  record=db.execute('SELECT state_json FROM dialogue_state_v1 WHERE session_id=?',(original['payload']['client_session_id'],)).fetchone()
  if record:
   parsed=json.loads(record[0]);turns=[t for t in parsed['turns'].values() if t.get('question') in ['ฟรีไหม','Is it free?','แล้วจอยล่ะ','What about a controller?']]
   rows.append(dict(session_id=original['payload']['client_session_id'],committed_followups=sum(bool(t.get('response')) for t in turns),pending_followups=sum(not bool(t.get('response')) for t in turns)))
with (r.OUT/'RESTART_CONCURRENT_FIRST_ATTEMPT_RETROSPECTIVE.json').open('x',encoding='utf-8') as f:json.dump(dict(scope='retrospective committed-state evidence only; first harness stopped on HTTP 503; no complete HTTP latency/error records',rows=rows),f,ensure_ascii=False,indent=2)
print('Full recipient data mirrored; first restart attempt preserved',len(rows),'sessions',flush=True)
