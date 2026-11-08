import json
from pathlib import Path
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
data=json.loads((report/'baseline_content.json').read_text(encoding='utf-8'))
for row in data['cases']:
 if row['case']['id'] not in ('ipad-th-0','format-en-4','ipad-en-4','penalties-th-0'):continue
 print(json.dumps(row['case'],ensure_ascii=False))
 print(row['response']['answer'])
 for trace in row['response']['trace']:
  if trace['stage'] in ('preprocess','competition_source_contract','competition_source_grounding','question_frame','universal_intent','bilingual_english','normalization'):
   print(json.dumps(trace,ensure_ascii=False))
