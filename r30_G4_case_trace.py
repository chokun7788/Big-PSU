import json
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip())
wanted={'รายการ CS2 ใช้เวอร์ชันเกมแบบไหน','CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย'}
for line in (r/'FINAL_G4_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['question'] in wanted:
        print(json.dumps({k:x['result'].get(k) for k in ['question','mode','route','language','answer']},ensure_ascii=False))
        for t in x['result']['trace']:
            if t.get('stage') not in ['timing','entities']:print(json.dumps(t,ensure_ascii=False)[:8000])
