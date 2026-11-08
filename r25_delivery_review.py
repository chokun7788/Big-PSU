import hashlib,json,re,sys
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
package=project/'owner_local_delivery_20261001_competition_format_r25_final/PSU_Esports_Chatbot_Local'
manifest=json.loads((report/'final_code_manifest.json').read_text(encoding='utf-8'))
checks=[]
for relative,digest in manifest.items():
 if relative.startswith('tests/'):continue
 actual=hashlib.sha256((package/relative).read_bytes()).hexdigest()
 checks.append({'file':relative,'matches':digest==actual,'sha256':actual})
assert all(item['matches'] for item in checks)
with (report/'package_code_verification.json').open('x',encoding='utf-8') as handle:json.dump(checks,handle,indent=2)
http=json.loads((report/'http_candidate_B.json').read_text(encoding='utf-8'))
assert http['passed']==http['total'],http
rounds=[json.loads((report/f'round_{letter}_unit.json').read_text(encoding='utf-8')) for letter in 'ABC']
ui={'candidate_A':[
 {'case':'thai-overview','headings':7,'lists':11,'strong':7,'literalStars':False},
 {'case':'thai-table','rows':9,'columns':2,'lastRow':'การหมิ่นศาสนาแบนถาวร'},
 {'case':'english-table','rows':9,'columns':2,'lastRow':'Offensive religious remarksPermanent ban','pageOverflow':False},
 {'case':'literal-user-html','text':'Hello <b>r25 literal text</b>','boldNodes':0}],
 'candidate_B':{'tekken_thai_overview':'actual browser confirmed stable headings, 3 rounds, 60 seconds, pause prohibition + agreement/emergency exception under pause category; organizer clarification remains',
 'observation_method':'Cua browser UI entry and read-only DOM/AX; screenshot inspected'}}
with (report/'ui_verification.json').open('x',encoding='utf-8') as handle:json.dump(ui,handle,ensure_ascii=False,indent=2)
latency=[row['elapsed_sec'] for row in http['cases']]
stats={'http_passed':http['passed'],'http_total':http['total'],'latency_min_sec':min(latency),'latency_max_sec':max(latency),'unit_final_tests':rounds[-1]['tests'],'unit_final_success':rounds[-1]['success'],'package_files_verified':len(checks),'protected_files_unchanged':6}
with (report/'delivery_checks.json').open('x',encoding='utf-8') as handle:json.dump(stats,handle,indent=2)
print(json.dumps(stats,ensure_ascii=False),flush=True)
