"""Verify the inventory artifact references and counts, not chatbot answers."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parent;p=R/'PARITY_COMPONENTS_TH.md';text=p.read_text('utf8')
targets=re.findall(r'\]\(([^)]+)\)',text)
missing=[x for x in targets if not x.startswith(('https://','http://')) and not (R/x).is_file()]
items=re.findall(r'^\| ([A-F]\d\d) \|',text,re.M)
fields=[json.loads(x) for x in (R/'ALL_FIELD_STATUSES.jsonl').read_text('utf8').splitlines()]
summary=json.loads((R/'DATA_INVENTORY.json').read_text('utf8'))
checks={'local_links_exist':not missing,'inventory_items_unique':len(items)==len(set(items))==62,
 'all_fields_count_matches':len(fields)==sum(summary['field_status_totals'].values())==6428,
 'current_database_unmodified':summary['same_database_sha256_before_after'],
 'no_new_api_model_or_test_calls':summary['new_api_calls']==summary['new_model_calls']==0 and not summary['new_tests']}
out={'checks':checks,'inventory_items':len(items),'field_rows':len(fields),'missing_links':missing,'all_passed':all(checks.values())}
(R/'INVENTORY_CHECK.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False,indent=2));assert all(checks.values())
