"""Read-only coherent logical observations; never a replacement live backup."""
import json,sqlite3,hashlib,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;root=R.parent
receipt=json.loads((root/'r134_resolution_scope_20261026/INSTALLATION_RECEIPT.json').read_text('utf8'))
paths={'R135_candidate':R/'system/data/knowledge/common.sqlite','R134_frozen':root/'r134_resolution_scope_20261026/system/data/knowledge/common.sqlite','R134_actual_installed':Path(receipt['installed_path'])/'system/data/knowledge/common.sqlite'}
def quote(s):return '"'+s.replace('"','""')+'"'
def table_state(path):
 c=sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True);c.execute('BEGIN');result={}
 try:
  for name, in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"):
   rows=sorted(json.dumps(list(row),ensure_ascii=False,separators=(',',':'),default=lambda b:{'blob_hex':b.hex()}) for row in c.execute('SELECT * FROM '+quote(name)))
   result[name]={'rows':len(rows),'logical_sha256':hashlib.sha256(('\n'.join(rows)).encode('utf8')).hexdigest()}
 finally:c.rollback();c.close()
 return result
tables={label:table_state(path) for label,path in paths.items()}
def diff(other):
 a=tables['R135_candidate'];b=tables[other];return [key for key in sorted(set(a)|set(b)) if a.get(key)!=b.get(key)]
try:
 with urllib.request.urlopen('http://127.0.0.1:8115/health',timeout=8) as response:health=json.load(response)
 observed={'ok':health.get('ok'),'common_loaded_build':health.get('common_loaded_build')}
except Exception as e:observed={'observation_error_type':type(e).__name__}
result={'checked_at':time.time(),'read_only_sqlite_transactions':True,'includes_wal_logical_rows':True,'paths':{k:str(v) for k,v in paths.items()},'tables':tables,'candidate_vs_frozen_parent_differences':diff('R134_frozen'),'candidate_vs_live_differences':diff('R134_actual_installed'),'installed_health_observation':observed,'installation_data_copy_still_must_use_actual_live_backup':True,'source_edits_or_approvals_performed':False,'final_freeze_or_model_asset_gate_claimed':False}
out=R/('SOURCE_PRESERVATION_OBSERVATION_'+str(time.time_ns())+'.json');out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(out),'parent_differences':result['candidate_vs_frozen_parent_differences'],'live_differences':result['candidate_vs_live_differences'],'health':observed},ensure_ascii=False))
