import json,sys,hashlib
from pathlib import Path
root=Path(__file__).parent
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
for r in map(json.loads,(report/'pipeline31_A_details.jsonl').read_text(encoding='utf-8').splitlines()):
    if r['answers_identical']:continue
    print(json.dumps({k:r[k] for k in ('id','domain','locale')},ensure_ascii=False))
    for form in ('clean','noisy'):
        print(json.dumps({k:r[form][k] for k in ('question','answer','mode','failures')},ensure_ascii=False))
sys.path.insert(0,str(project))
from app.pipeline.structured_tools import _member_rows,_compact
from app.core.typo_similarity import osa_distance
query='ผศ.ดร.ณัฐงศ์ ทอวเทพ'
print('MEMBER CANDIDATES')
for row in _member_rows():
    name=row['name'];print(json.dumps({'name':name,'distance':osa_distance(_compact(query),_compact(name)),'row':row},ensure_ascii=False))
