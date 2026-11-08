"""Prepare a new manual entry point; preserve all earlier launcher files."""
import ast
from pathlib import Path
R=Path(__file__).resolve().parent
for old,new in [('serve_candidate.py','serve_revision05.py'),('launch_candidate.py','launch_revision05.py')]:
 text=(R/old).read_text('utf8').replace('revision03_system','revision05_system').replace('serve_candidate.py','serve_revision05.py')
 text=text.replace('r123-foundation-r03','r123-native-context-r05').replace('R123-foundation-r03','R123-native-context-r05')
 text=text.replace('R123 foundation revision03; unified profiles for every caller. P0/P1 foundation; no new model inference benchmark yet; native calendar/live special adapters remain; live provider controlled unavailable.',
 'R123 revision05: native calendar/live receipt bridge and honest input provenance. Existing R121 adapter, no new semantic accuracy benchmark. Native compound scheduling remains sequential; live provider controlled unavailable.')
 ast.parse(text);target=R/new
 assert not target.exists();target.write_text(text,'utf8')
print('New revision05 launcher prepared; earlier entry points unchanged')
