"""Prepare an isolated manual launcher, never start the app as part of build."""
import ast,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r122_context_scope_calendar_20261022'
shutil.copy2(OLD/'runtime_profile.py',R/'runtime_profile.py')
shutil.copy2(OLD/'serve_planner.py',R/'serve_planner.py')
x=(OLD/'serve_candidate04.py').read_text('utf8').replace('revision04_system','revision03_system');ast.parse(x);(R/'serve_candidate.py').write_text(x,'utf8')
x=(OLD/'launch_candidate.py').read_text('utf8').replace('revision04_system','revision03_system').replace('serve_candidate04.py','serve_candidate.py')
x=x.replace('r122-context-scope-r04','r123-foundation-r03').replace('R122-context-scope-r04','R123-foundation-r03').replace('R122 revision04','R123 foundation revision03')
x=x.replace('See saved API comparison; live provider remains a controlled unavailable fixture.','P0/P1 foundation; no new model inference benchmark yet; native calendar/live special adapters remain; live provider controlled unavailable.')
ast.parse(x);(R/'launch_candidate.py').write_text(x,'utf8')
print('Manual launcher prepared, model/server not started')
