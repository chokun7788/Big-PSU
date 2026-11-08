import json,sys
from r27_fixture import REPORT
rows=[json.loads(x) for x in (REPORT/(sys.argv[1]+'_details.jsonl')).read_text(encoding='utf-8').splitlines()]
seen=set()
for row in rows:
    if row['passed'] or row['anchor'] in seen:continue
    if len(sys.argv)>2 and not row['anchor'].startswith(sys.argv[2]):continue
    seen.add(row['anchor'])
    print(json.dumps({'id':row['id'],'q':row['question'],'fail':row['failures'],'answer':row['response']['answer'],'mode':row['response']['mode']},ensure_ascii=False))
