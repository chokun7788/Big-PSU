import ast
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022'
x=(OLD/'launch_candidate.py').read_text('utf8')
x=x.replace("R/'revision04_system'","R/'revision02_system'").replace("R/'train02/TRAINING_COMPLETE.json'","R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json'")
x=x.replace('r121-context-guard-r04','r122-context-scope-r02').replace('R121-context-guard-r04','R122-context-scope-r02').replace('serve_reader.py','serve_candidate02.py')
x=x.replace('Profile config addresses the unprofiled /api/generate requests found in api02. That old API comparison has not been remeasured with this launcher.','R122 revision02; unified profiles for every caller. See saved API comparison; live provider remains a controlled unavailable fixture.')
ast.parse(x);(R/'launch_candidate.py').write_text(x,'utf8')
