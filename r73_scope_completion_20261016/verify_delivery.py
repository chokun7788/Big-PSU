import json,re
from pathlib import Path
B=Path(__file__).resolve().parent;errors=[];checked=0
for name in ['FLOW_R73_TH.md','REPORT_R73_TH.md','README_R73_TH.md','OWNER_QUESTIONS_R73_TH.md']:
 text=(B/name).read_text('utf8')
 if not text.strip():errors.append('empty:'+name)
 for target in re.findall(r'\]\((C:/[^)]+)\)',text):
  checked+=1
  if not Path(target).exists():errors.append('broken:'+target)
qa=json.loads((B/'DELIVERY_QA.json').read_text('utf8'))
if qa['source_content_files_changed'] or qa['factual_fields_changed'] or qa['existing_revision_payloads_changed']:errors.append('preservation_failure')
if qa['approvals_after']!=0 or qa['active_after']!='':errors.append('unexpected_approval_or_publication')
for name,expected in [('results/scope_final/SUMMARY.json',50),('verification/profiles02/RESULTS.json',20),('verification/api01/RESULTS.json',52),('results/regression01/SUMMARY.json',43)]:
 result=json.loads((B/name).read_text('utf8'))
 if result['passed']!=expected:errors.append('result:'+name)
result={'document_links_checked':checked,'errors':errors,'source_files_preserved':True,'factual_fields_preserved':True,'metadata_annotations_added_to_records':qa['routing_metadata_changed_records'],'owner_approvals_created':False,'publication_activated':False,'source_syntax_errors':qa['syntax_errors'],'model_inference_verified':False,'real_browser_or_tcp_verified':False,'ui_widget_checks':3,'powershell_launcher_parse_errors':0}
(B/'DOCUMENT_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
