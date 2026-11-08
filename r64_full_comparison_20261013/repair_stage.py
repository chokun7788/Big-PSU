import json,hashlib,shutil,ast
from pathlib import Path
B=Path(__file__).resolve().parent;stage=B/'system';ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
manifest=json.loads((B/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'));known={x['path'] for x in manifest}
for folder in ['app/knowledge','deployment_templates','docs']:
 for p in (ROOT/folder).rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts:continue
  rel=p.relative_to(ROOT);dest=stage/rel
  if dest.exists():continue
  dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
  if rel.as_posix() not in known:manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(B/'SOURCE_MANIFEST_REPAIRED.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
source=(B.parent/'r33_full_corpus.py').read_text(encoding='utf-8');module=ast.parse(source)
functions=[ast.get_source_segment(source,n) for n in module.body if isinstance(n,ast.FunctionDef) and n.name in ['plain','grade']]
(B/'grade_legacy.py').write_text('import dataclasses\nfrom unittest.mock import patch\n'+ '\n\n'.join(functions),encoding='utf-8')
print('Restored missing app/knowledge and direct test dependencies; extracted unchanged legacy grader')
