import json
from pathlib import Path
report=Path(Path(__file__).with_name('r29_report_path.txt').read_text(encoding='utf-8').strip())
for r in map(json.loads,(report/'pipeline31_C_details.jsonl').read_text(encoding='utf-8').splitlines()):
    print(json.dumps({'id':r['id'],'q':r['clean']['question'],'answer':r['clean']['answer'],'hits':r['clean']['hits'],'noisy_mode':r['noisy']['mode'],'same':r['answers_identical']},ensure_ascii=False))
