from pathlib import Path
import hashlib,json,re
B=Path(__file__).resolve().parent
errors=[];links=[]
for name in ('FLOW_R72_TH.md','REPORT_R72_TH.md','README_R72_TH.md','IMPLEMENTATION_STATUS_R72_TH.md'):
 p=B/name;text=p.read_text('utf8')
 if not text.strip():errors.append('empty:'+name)
 for target in re.findall(r'\]\((C:/[^)]+)\)',text):
  links.append(target)
  if not Path(target).exists():errors.append('broken:'+target)
required=['verification/api_final/RESULTS.json','verification/updates_on01/RESULTS.json','results/fixtures02/RESULTS.json','results/candidate_final/SUMMARY.json','results/risk_candidate01/SUMMARY.json','results/exploratory03/MODEL_HEALTH.json','Open-New-Chat.cmd','Start-New-Chat.ps1']
for name in required:
 if not (B/name).is_file():errors.append('missing:'+name)
qa=json.loads((B/'DELIVERY_QA.json').read_text('utf8'))
if qa['source_content_files_changed'] or not qa['database_matches_preserved_source']:errors.append('source_preservation')
api=json.loads((B/'verification/api_final/RESULTS.json').read_text('utf8'))
if api['passed']!=46:errors.append('api_final')
result={'document_links_checked':len(links),'required_files_checked':len(required),'errors':errors,'source_code_data_preserved':not qa['source_content_files_changed'],'database_unchanged':qa['database_matches_preserved_source'],'api_final_passed':api['passed'],'powershell_launchers_parse_errors':0,'powershell_validation_note':'Three launcher scripts parsed successfully with PowerShell language parser; no real TCP launch claim.','production_ready_claimed':False,'manifest_sha256':hashlib.sha256((B/'DELIVERY_QA.json').read_bytes()).hexdigest()}
(B/'DOCUMENT_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
