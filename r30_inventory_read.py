import json,ast
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path(Path('r30_report_path.txt').read_text().strip())
inventory=json.loads((report/'test_inventory_initial.json').read_text(encoding='utf-8'))
for c in inventory['corpora']:
    f=p/c['file'];data=json.loads(f.read_text(encoding='utf-8-sig')) if f.suffix=='.json' else [json.loads(l) for l in f.read_text(encoding='utf-8-sig').splitlines() if l.strip()]
    rows=data if isinstance(data,list) else next((v for k,v in data.items() if isinstance(v,list) and v and isinstance(v[0],dict)),[])
    print(f.name,len(rows),json.dumps(rows[0] if rows else data,ensure_ascii=False)[:1700])
print('SMOKE SIDE EFFECT CHECKS')
for f in sorted((p/'tests').glob('smoke_test*.py')):
    s=f.read_text(encoding='utf-8');flags=[l.strip() for l in s.splitlines() if any(k in l for k in ['write_text','write_bytes','unlink','subprocess','POSTGRES','DATABASE_URL','TemporaryDirectory','tempfile','requests.post','method="POST"'])]
    if flags:print(f.name,flags)
print('EXTRA ROUTING FILES',*[str(f.relative_to(p)) for f in (p/'data/routing').glob('*')],sep='\n')
