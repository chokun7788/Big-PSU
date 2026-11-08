import json,re
from pathlib import Path
B=Path(__file__).resolve().parent
data=json.loads((B/'TRANSLATION_CHECK.json').read_text(encoding='utf-8'))
for row in data['results']:
 en=row['english'].casefold()
 if row['kind']=='policy':semantic=bool(re.search(r'prohibited|forbidden|cannot|not allowed|must not',en))
 elif row['kind']=='news':semantic=bool(re.search(r'no .*extension|cannot .*extend|not allowed.*extend|must not.*extend',en))
 else:semantic='booked' in en and 'listed' in en and 'or' in en and 'cannot' in en
 row['passed']=row['source_unchanged'] and row['not_saved_or_published'] and semantic
data['passed']=sum(x['passed'] for x in data['results'])
data['original_evaluator_error']='The original lexical negative check omitted the valid English word No. Its result and actual model output are preserved.'
(B/'TRANSLATION_CHECK_REVIEWED.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print(data['passed'],data['cases'])
