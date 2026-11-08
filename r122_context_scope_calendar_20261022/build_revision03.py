"""Support source-related service-to-game ellipsis, preserve prior API source."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision03_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'api02/RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(R/'revision02_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
p=S/'app/knowledge/common/domain_flow/context_guard.py';x=p.read_text('utf8')
x=x.replace("if anaphor and previous is not None:\n            names=named_targets(index,previous.quote)\n            if len(names)==1:shared=names[0]", """shared_basis='unique_previous_source_named_referent'
        if previous is not None:
            names=named_targets(index,previous.quote)
            if anaphor and len(names)==1:shared=names[0]
            elif (not anaphor and len(names)==1 and task.category=='C04'
                  and previous.category in {'C03','C06','C07','C08'}
                  and not named_targets(index,local)
                  and task.facet in {'game_catalog','studio_services'}
                  and index.bind('C04',names[0])):
                shared=names[0];shared_basis='source_related_service_game_ellipsis'
""")
x=x.replace("'action':'unique_previous_source_named_referent','task_quote':local,'source_quote':shared", "'action':shared_basis,'task_quote':local,'source_quote':shared")
ast.parse(x);p.write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
x=(R/'serve_candidate02.py').read_text('utf8').replace("R/'revision02_system'","R/'revision03_system'");(R/'serve_candidate03.py').write_text(x,'utf8')
(R/'REVISION03_BUILD.json').write_text(json.dumps({'parent':'R122 revision02','parent_frozen_unchanged':True,'data_unchanged':sha(S/'data/knowledge/common.sqlite')==sha(R/'revision02_system/data/knowledge/common.sqlite'),'change':'inherit one source-related service name into an elliptical game-catalog need, never another need duration/audience/price','production_installed':False},indent=2),'utf8')
print('Revision03 source prepared; revision02 measurement unchanged')
