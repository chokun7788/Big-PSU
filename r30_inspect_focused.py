import sys,json
from pathlib import Path
report=Path(Path(__file__).with_name('r30_report_path.txt').read_text(encoding='utf-8').strip());run=sys.argv[1]
for r in map(json.loads,(report/(run+'_focused_details.jsonl')).read_text(encoding='utf-8').splitlines()):
    if r['failures']:
        if r['case']['id'] in ('price-en-pc-0','price-en-fractional','price-en-fractional-noise','book-en-48','book-en-49') or r['case']['group']=='booking_service_selection':
            print(json.dumps({'id':r['case']['id'],'q':r['case']['question'],'mode':r['mode'],'failures':r['failures'],'answer':r['answer'][:1100],'trace':[t for t in r['trace'] if t['stage'] in ('preprocess','intent_cue_preflight','multi_question','closed_query_improvement','surface_recovery','entity_resolution','query_plan')]},ensure_ascii=False))
