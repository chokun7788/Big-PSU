import json,sys
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip())
for l in (r/'candidate_G_competition_G_details.jsonl').open(encoding='utf-8'):
    x=json.loads(l)
    if x['failures'] and ('เปลี่ยน' in x['case']['question'] or 'RoV' in x['case']['question']):
        print(json.dumps({'q':x['case']['question'],'trace':[t for t in x['trace'] if not t['stage'].startswith('timing:') and any(s in t['stage'] for s in ['preprocess','normal','intent','route','competition','entities'])]},ensure_ascii=False))
