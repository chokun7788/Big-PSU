import sys
from pathlib import Path
P=Path(sys.argv[1])
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8')
old="    rows={row['id']:row for row in load_curated_rows()}";assert s.count(old)==1
s=s.replace(old,"    rows={row['id']:row for row in load_curated_rows() if row.get('id')}")
f.write_text(s,encoding='utf-8');print('H: ignore non-record metadata rows in curated source index')
